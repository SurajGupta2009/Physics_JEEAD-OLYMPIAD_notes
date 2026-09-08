#!/usr/bin/env python3
"""One-shot content patch for chapter 6 (drafting leftovers -> final prose)."""
import re, sys
p = '06-networks-and-transients.html'
s = open(p, encoding='utf-8').read()
orig = len(s)
def sub(old, new):
    global s
    if old not in s:
        sys.exit('NOT FOUND: ' + old[:70])
    s = s.replace(old, new, 1)

def cut(start_marker, end_marker, new):
    """replace from start_marker up to (not incl.) end_marker"""
    global s
    a = s.index(start_marker); b = s.index(end_marker, a)
    s = s[:a] + new + s[b:]

# 1. the branch rule's hypothesis
sub(r'''argument is the <em>proof</em>: whatever complicated exponential the current follows, its time integral is fixed by
endpoints alone. That is why these questions are answerable at all without solving the ODE.</p>''',
r'''argument is the <em>proof</em>: whatever complicated exponential the current follows, its time integral is fixed by
endpoints alone.</p>
<p>The rule has one hypothesis, and it is what makes or breaks the shortcut: <b>every other branch leaving the
surface must end on a capacitor plate.</b> If instead a resistor leads from the enclosed region to the far rail, part
of the charge drains through it and is not countable from end states alone. Q3 sits exactly on that boundary.</p>''')

# 2. Q3, replaced wholesale
cut(r'<div class="q"><div class="hd"><span class="lab">Q3</span>',
    r'<div class="q"><div class="hd"><span class="lab">Q4</span>',
r'''<div class="q"><div class="hd"><span class="lab">Q3</span><b>A cell of 50 V feeds two parallel branches through a switch: branch 1 is <m>R_1=10\ \text{k}\Omega</m> in series with <m>C_1=1\ \mu</m>F to the return rail, branch 2 is <m>R_2=5\ \text{k}\Omega</m> in series with <m>C_2=2\ \mu</m>F. Both capacitors start uncharged. Find (i) the final charge on each, (ii) the total charge that passes through the switch, (iii) each branch's time constant, (iv) the total heat, (v) whether the switch current is a single exponential.</b><span class="diff">JEE-adv · the algorithm, executed</span></div>
<div class="bd">
<details class="sol"><summary>Solution</summary><div class="bd">
<p><b>(i)</b> Steady state: open both capacitor branches — and with them both branches entirely, since each contains a
capacitor in series. No current flows anywhere, so there is no drop on either resistor and each capacitor ends with the
full cell voltage: <m>Q_1=C_1V=50\ \mu</m>C and <m>Q_2=C_2V=100\ \mu</m>C.</p>
<p><b>(ii)</b> Take the surface cutting the switch lead. It encloses the two resistors and the two upper plates, and
the only other things crossing it are capacitor dielectrics, which carry no current — so §6.3's rule is legal here and
<m>Q_{\text{sw}}=Q_1+Q_2=150\ \mu</m>C.</p>
<p><b>(iii)</b> Each branch is an independent single-capacitor loop: <m>\tau_1=R_1C_1=10</m> ms and
<m>\tau_2=R_2C_2=10</m> ms.</p>
<p><b>(iv)</b> Heat per branch is <m>\tfrac12CV^{2}</m> whatever <m>R</m> is (6.3), so
<m>H=\tfrac12(1+2)\times10^{-6}\times50^{2}=3.75</m> mJ. Audit: the battery delivered
<m>VQ_{\text{sw}}=7.5</m> mJ, the field holds <m>\tfrac12(C_1+C_2)V^{2}=3.75</m> mJ ✓.</p>
<p><b>(v)</b> <m>I_{\text{sw}}(t)=V\left(e^{-t/\tau_1}/R_1+e^{-t/\tau_2}/R_2\right)</m> — a sum of two
exponentials, so <em>not</em> a single exponential, and "the time constant of this circuit" is a category error. The
chosen numbers make the two coincide, so it collapses to one exponential with <m>\tau=10</m> ms and
<m>I(0^{+})=5+10=15</m> mA. Change either resistor and a plot of <m>\ln I</m> against <m>t</m> is visibly bent;
reading <m>\tau</m> from its initial slope then overestimates it, which is the experimental error this question is
built to punish.</p>
</div></details>
</div></div>

''')

# 3. Q4's garbled KVL
sub(r'''<div class="eqd">V_1-\frac{q}{C_1}-qR\cdot\frac{d}{dq}\ldots\qquad
R\frac{dq}{dt}+\frac{q}{C_{\text{ser}}}=V_1-V_2=50\ \text{V}
\qquad\Rightarrow\qquad q(t)=C_{\text{ser}}\Delta V\left(1-e^{-t/\tau}\right)</div>''',
r'''<div class="eqd">\text{KVL:}\quad \left(V_1-\frac{q}{C_1}\right)-\left(V_2+\frac{q}{C_2}\right)=R\frac{dq}{dt}
\quad\Rightarrow\quad \frac{dq}{dt}+\frac{q}{RC_{\text{ser}}}=\frac{\Delta V}{R},\qquad
q(t)=C_{\text{ser}}\Delta V\left(1-e^{-t/\tau}\right)</div>''')

# 4. Q5 prompt + solution
sub(r'''<b>A 12 V mains-driven half-wave rectifier feeds a load R through a smoothing capacitor C = 2200 µF. The supply is 50 Hz. Estimate the peak-to-peak ripple for R = 12 Ω, and find the condition on RC for the "ripple = linear discharge" approximation to be self-consistent.</b>''',
r'''<b>A half-wave rectifier feeds a load <m>R=12\ \Omega</m> through a smoothing capacitor <m>C=2200\ \mu</m>F; the secondary peak is 17 V (12 V RMS) and the mains is 50 Hz. Find the peak-to-peak ripple and the DC output, and the condition on <m>RC</m> for the shortcut <m>\Delta V=V_0T/RC</m> to be self-consistent.</b>''')
cut(r'<p>Between conduction intervals the capacitor discharges', r'</div></details>
</div></div>

<div class="q"><div class="hd"><span class="lab">Q6</span>',
r'''<p><b>Exact exponential first.</b> Between conduction intervals the capacitor discharges through <m>R</m> alone with
<m>\tau=RC=0.0264</m> s, so over one period <m>T=0.02</m> s:</p>
<div class="eqd">\Delta V=V_0\left(1-e^{-T/\tau}\right)=17\left(1-e^{-0.758}\right)=9.0\ \text{V},
\qquad V_{\text{DC}}\approx V_0-\frac{\Delta V}{2}=12.5\ \text{V}</div>
<p>The shortcut gives <m>V_0T/RC=12.9</m> V, a 43% overestimate, because <m>T/\tau=0.76</m> is nowhere near the small
parameter it assumes. <b>Self-consistency:</b> <m>1-e^{-x}\approx x</m> requires <m>x=T/\tau\le0.1</m>, i.e.
<m>RC\ge10T=0.2</m> s; here <m>RC=0.026</m> s, so the shortcut is invalid. The rule that survives is the one worth
memorising, and it is only <m>\Delta Q=I\,\Delta t</m> with <m>\Delta V=\Delta Q/C</m>:</p>
<div class="eqd">C\ \ge\ \frac{I_{\text{load}}\,T_{\text{rip}}}{\Delta V_{\max}}\ ,\qquad
T_{\text{rip}}=\frac1{2f}=10\ \text{ms}\ \text{(full-wave)},\ \ \frac1f=20\ \text{ms}\ \text{(half-wave)}</div>
<p><b>The stress the numbers hide.</b> The load charge <m>\Delta Q=C\Delta V=19.8</m> mC is returned to the capacitor
only while the mains sine exceeds the capacitor voltage — a window of a few milliseconds — so the diode's peak
current is an order of magnitude above the load current, and its rms value dominates the heating of the capacitor's
<m>R_{\text{ESR}}</m> (chapter 5's loss tangent, with a duty cycle). That is why the electrolytic in a cheap adaptor
dries out, and why a datasheet lists ripple <em>voltage</em> and ripple <em>current</em> as separate limits: the
first is a regulation specification, the second a thermal one, and only the second kills the part.</p>
''')

# 5. Q6 latch arithmetic + prompt
sub(r''' Above what lamp on-resistance does the circuit latch on?''',
    r''' Above what lamp on-resistance <m>r</m> does the circuit latch on?''')
sub(r'''<div class="eqd">r\,(120-20)&lt;20(200\ \text{k}\Omega+r)\ \Rightarrow\ r&lt;22.2\ \text{k}\Omega</div>
<p>A lamp (or a switch, or a trigger circuit) "harder" than <m>22\ \text{k}\Omega</m> will simply sit lit and the
relaxation action dies.''',
r'''<div class="eqd">\frac{Vr}{R+r}&lt;V_{\text{lo}}\ \Rightarrow\ 120r&lt;20\left(200\ \text{k}\Omega+r\right)
\ \Rightarrow\ r&lt;40\ \text{k}\Omega</div>
<p>A lamp (or a switch, or a trigger circuit) with on-resistance above <m>40\ \text{k}\Omega</m> holds the capacitor
above 20 V, so the discharge never extinguishes and the circuit latches on.''')

# 6. Q7 rewritten as a real two-parameter model test
cut(r'<p>Ohmic leakage through a parallel', r'</div></details>
</div></div>

<h2>Drill: say it in one line</h2>',
r'''<p><b>Test one exponential two ways: ratio and level.</b> <m>V=V_0e^{-t/\theta}</m> makes the second-hour drop
<m>e^{-1/\theta}</m> times the first, and the observed ratio <m>0.10/0.30=1/3</m> needs <m>\theta=1/\ln3=0.91</m> h —
but then the first-hour drop should have been <m>2.7(1-e^{-1/0.91})=1.8</m> V, six times what was measured. No single
exponential has both this ratio and this level, so the ohmic-leakage model is dead.</p>
<p><b>Try a diffusive relaxation.</b> Fit <m>V=V_0-at^{p}</m>: <m>a=0.30</m> V and <m>2^{p}=0.40/0.30</m> ⇒
<m>p=0.42</m>, i.e. <m>1/2</m> within two data points — the <m>\sqrt t</m> law of §6.7, deep pore regions still
equilibrating. A <m>\sqrt t</m> decay has exactly this fingerprint: a rate that keeps slowing without ever becoming
exponential.</p>
<p><b>What an "effective leakage resistance" is worth.</b> At 1 h,
<m>I=C|dV/dt|=3000\times0.30\times0.42/3600=0.105</m> A, so <m>R_{\text{eff}}=V/I\approx23\ \Omega</m> — yet an ohmic
<m>23\ \Omega</m> across <m>3000</m> F would give <m>\theta=RC=69\ \mu</m>s, not hours. The contradiction <em>is</em>
the answer: <b>there is no leakage resistance to report</b>; the bank has a nearly constant Faradaic current plus a
<m>\sqrt t</m> redistribution. Consequences: series stacks need balancing resistors of tens of ohms (not the MΩ the
word "leakage" suggests — which is why supercapacitor modules ship with bleed networks and idle at mA rather than nA),
and a quoted "self-discharge" figure is valid only for the soak time it was measured after, so two parts with
different histories cannot be compared from their datasheets alone.</p>
''')

# 7. §6.8 bullets
sub(r'''<li><b>One number does both jobs.</b> The <em>same</em> <m\tau</m> sets the −3 dB corner and the step-response
time. So a bandwidth specification is a time specification: a 100 MHz scope with 3.5 ps resolution and a
<m\tau=1/2\pi f_c</m> input network cannot show you an edge faster than <m>0.35/f_c</m> — the familiar
"0.35 rule" is just the pole of (6.10) plus a Gaussian of matched variance.</li>
<li><b>Power and phase at the corner.</b> At <m\omega\tau=1</m> the output amplitude is <m>1/\sqrt2</m>, the phase
lag is exactly <m45^\circ</m>, and the <em>real</em> power delivered to a resistive load is a quarter of the
low-frequency value times two… i.e. <m|H|^{2}=1/2</m> in power ✓. The 45° coincidence is the fastest check that a
filter really is one-pole and not one-pole-plus-stray-inductance.</li>''',
r'''<li><b>One number does both jobs.</b> The <em>same</em> <m>\tau</m> fixes the −3 dB corner and the step-response
speed, because both are properties of the single pole (6.10). That pole's 10–90% rise time is <m>\tau\ln9=2.20\tau</m>,
so <m>t_r=2.20/2\pi f_c=0.35/f_c</m>: the "0.35 rule" of oscilloscope bandwidth is this one line and nothing
else.</li>
<li><b>Everything happens at the corner.</b> At <m>\omega\tau=1</m>: amplitude <m>1/\sqrt2</m>, power into a fixed load
exactly <m>\tfrac12</m> (hence "−3 dB"), phase lag exactly <m>45^\circ</m>. That triple coincidence is the fastest
experimental check that a filter really is <em>one</em> pole — measure the phase, not just the magnitude, and a
hiding second pole cannot stay quiet.</li>''')

# 8. markdown leak
sub(r'''because the same condition appears as the
*balanced-bridge* condition''', r'''because the same condition appears as the
<em>balanced-bridge</em> condition''')

# 9. Q10 rewritten
cut(r'<div class="q"><div class="hd"><span class="lab">Q10</span>', r'<h2>Drill: say it in one line</h2>',
r'''<div class="q"><div class="hd"><span class="lab">Q10</span><b>An RC pair is driven by a square wave of amplitude <m>\pm V_0</m> and half-period <m>T</m>. Find the periodic steady-state waveforms of <m>V_C</m> and <m>I</m>, the peak-to-peak swing and the mean current; show that the load behaves as a capacitor of value <m>C\tanh(T/2\tau)</m>; and deduce why a switched-capacitor voltmeter's reading is independent of <m>R</m>.</b><span class="diff">Olympiad · periodic-state analysis</span></div>
<div class="bd">
<details class="sol"><summary>Solution</summary><div class="bd">
<p>Let the capacitor voltage reverse between <m>\pm V_a</m>. Ending a half-period of charging toward <m>+V_0</m>
from <m>-V_a</m> means <m>V_a=V_0-(V_0+V_a)e^{-T/\tau}</m>, so with <m>x=T/\tau</m>:</p>
<div class="eqd">V_a=V_0\,\frac{1-e^{-x}}{1+e^{-x}}=V_0\tanh\frac{x}{2}
\qquad\left[\text{identity: }\tanh\frac x2=\frac{e^{x/2}-e^{-x/2}}{e^{x/2}+e^{-x/2}}\right]</div>
<p>The response is a chain of exponential arcs of peak-to-peak swing <m>2V_0\tanh(T/2\tau)</m>, and inside a half
period <m>V_C(t)=V_0-(V_0+V_a)e^{-t/\tau}</m>, so</p>
<div class="eqd">I(t)=\frac{V_0-V_C}{R}=\frac{V_0+V_a}{R}\,e^{-t/\tau},\qquad 0\le t\le T</div>
<p>Two limits, both worth stating: <b>slow drive</b> (<m>T\gg\tau</m>) gives <m>V_a\to V_0</m>, an almost square
output; <b>fast drive</b> (<m>T\ll\tau</m>) gives <m>V_a\approx V_0T/2\tau</m>, a small triangular ripple — the same
component acting as an averager. Hence the mean current, from the branch rule rather than by integrating:</p>
<div class="eqd">\langle I\rangle=\frac{\Delta Q}{T}=\frac{2CV_a}{T}=\frac{2CV_0}{T}\tanh\frac{T}{2\tau}
\qquad\Longrightarrow\qquad C_{\text{eff}}=C\tanh\frac{T}{2\tau}</div>
<p>For <m>T\gg\tau</m> the transferred charge is exactly <m>\Delta Q=2CV_0</m> and <m>\tau=RC</m> has vanished from
it: charge transfer between two known potentials is an endpoint question. That is the principle of the
charge-balancing (switched-capacitor) integrating voltmeter — transfer the unknown's charge through the same
<m>RC</m> network into a virtual ground, count cycles until balance, and every series and contact resistance that
merely <em>slows</em> the transfer drops out of the result, at the price of having to wait for each transfer to
complete.</p>
<p><b>The theorem to keep:</b> endpoint quantities (charge per cycle, energy from charge, mean current over a
complete cycle) do not depend on <m>R</m>; rate quantities (<m>\tau</m>, ripple, settling time) are proportional to
it. Half the questions in this chapter are decided by noticing which of the two is being asked.</p>
</div></details>
</div></div>

''')

open(p, 'w', encoding='utf-8').write(s)
print('ok', orig, '->', len(s))
