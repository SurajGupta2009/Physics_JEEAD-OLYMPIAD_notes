#!/usr/bin/env python3
"""Install (or refresh) the vault's Obsidian community plugins from the pinned lock file.

    python3 tools/obsidian_plugins.py            # install every plugin at its pinned version
    python3 tools/obsidian_plugins.py --check    # report what is installed / missing / outdated, change nothing
    python3 tools/obsidian_plugins.py --latest   # re-pin every plugin to its latest GitHub release, then install
    python3 tools/obsidian_plugins.py dataview   # only these plugin ids

Why this exists.  Obsidian does not auto-install plugins from `.obsidian/community-plugins.json`;
a plugin only works when `.obsidian/plugins/<id>/{main.js,manifest.json,styles.css}` exist.  Those
three files are release artefacts published on GitHub, so the vault pins them in
`.obsidian/plugins.lock.json` and this script fetches exactly those versions — the same idea as a
package lock.  Settings (`data.json`) are committed and are never touched by this script.

What it fetches, per plugin: `manifest.json`, `main.js` and, when the release ships one,
`styles.css`, from `https://github.com/<repo>/releases/download/<version>/`.  The manifest's `id`
must equal the folder name or the download is rejected.  Pure standard library, no pip.

After it runs, the plugin files can be committed (that is the intent — the vault then works the
moment it is opened) or left untracked; `.gitignore` only excludes per-device state.
"""
import json
import os
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBS = os.path.join(ROOT, '.obsidian')
LOCK = os.path.join(OBS, 'plugins.lock.json')
ENABLED = os.path.join(OBS, 'community-plugins.json')
ASSETS = ('manifest.json', 'main.js', 'styles.css')      # styles.css is optional
UA = {'User-Agent': 'Physics_JEEAD-OLYMPIAD_notes vault setup'}


def read_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write('\n')


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def latest_version(repo):
    """Tag name of the latest GitHub release (manifest `version` == tag for Obsidian plugins)."""
    hdrs = dict(UA, Accept='application/vnd.github+json')
    tok = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if tok:
        hdrs['Authorization'] = 'Bearer ' + tok
    req = urllib.request.Request('https://api.github.com/repos/%s/releases/latest' % repo, headers=hdrs)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())['tag_name']


def installed_version(pid):
    m = read_json(os.path.join(OBS, 'plugins', pid, 'manifest.json'))
    has_main = os.path.exists(os.path.join(OBS, 'plugins', pid, 'main.js'))
    return (m or {}).get('version') if (m and has_main) else None


def install(pid, repo, version):
    base = 'https://github.com/%s/releases/download/%s/' % (repo, version)
    dest = os.path.join(OBS, 'plugins', pid)
    os.makedirs(dest, exist_ok=True)
    got = {}
    for name in ASSETS:
        try:
            got[name] = fetch(base + name)
        except urllib.error.HTTPError as e:
            if name == 'styles.css' and e.code == 404:
                continue                                   # a plugin without CSS is normal
            raise
    manifest = json.loads(got['manifest.json'].decode('utf-8'))
    if manifest.get('id') != pid:
        raise SystemExit('%s: release manifest id is %r — refusing to install into the wrong folder'
                         % (pid, manifest.get('id')))
    for name, blob in got.items():
        with open(os.path.join(dest, name), 'wb') as fh:
            fh.write(blob)
    stale_css = os.path.join(dest, 'styles.css')
    if 'styles.css' not in got and os.path.exists(stale_css):
        os.remove(stale_css)
    return manifest.get('version', version), sorted(got)


def main():
    args = sys.argv[1:]
    check = '--check' in args
    latest = '--latest' in args
    only = {a for a in args if not a.startswith('--')}

    lock = read_json(LOCK)
    if not lock or 'plugins' not in lock:
        raise SystemExit('missing %s' % LOCK)
    enabled = read_json(ENABLED, [])
    plugins = lock['plugins']
    failures = 0

    for pid, spec in plugins.items():
        if only and pid not in only:
            continue
        repo, want = spec['repo'], spec['version']
        have = installed_version(pid)
        flag = '' if pid in enabled else '  (not in community-plugins.json — enable it in Settings → Community plugins)'

        if latest and not check:
            try:
                new = latest_version(repo)
            except Exception as e:                          # keep the pin if the API is unreachable
                print('  ! %-28s could not query latest release (%s); keeping %s' % (pid, e, want))
                new = want
            if new != want:
                print('  ~ %-28s re-pinned %s → %s' % (pid, want, new))
                spec['version'] = want = new

        if check:
            state = 'missing' if have is None else ('ok' if have == want else 'installed %s, pinned %s' % (have, want))
            print('  %s %-28s %-8s %s%s' % ('✓' if have == want else '·', pid, want, state, flag))
            continue

        if have == want:
            print('  ✓ %-28s %s already installed%s' % (pid, want, flag))
            continue
        try:
            got_version, files = install(pid, repo, want)
            print('  + %-28s %s installed (%s)%s' % (pid, got_version, ', '.join(files), flag))
        except Exception as e:
            failures += 1
            print('  ✗ %-28s %s FAILED: %s' % (pid, want, e))
            print('      manual route: Obsidian → Settings → Community plugins → Browse → "%s" → Install;'
                  % pid)
            print('      the committed settings in .obsidian/plugins/%s/data.json are picked up as-is.' % pid)

    if latest and not check:
        write_json(LOCK, lock)

    if check:
        return 0
    if failures:
        print('\n%d plugin(s) could not be downloaded (no network to github.com?). '
              'Re-run when online, or install them from Obsidian\'s plugin browser.' % failures)
        return 1
    print('\nAll pinned plugins present. Open the repository root as a vault; if Obsidian asks, '
          'choose "Trust author and enable plugins".')
    return 0


if __name__ == '__main__':
    sys.exit(main())
