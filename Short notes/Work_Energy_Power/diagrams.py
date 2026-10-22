"""Native analytical diagrams for the work-energy-power edition.

One wide figure per sheet, two panels at most. Every panel is a closed-form
curve, a shaded signed area, a labelled free-body diagram, an energy ledger or
a geometry construction. Nothing here is decorative and nothing is sampled:
a rebuild reproduces the same pixels.
"""
from figlib import (I, T, R, G, GOLD, HG, BLUE, GREEN, PALE, YEL, WATER,
                    txt, head, foot, arrow, panel, axes2, dimx, dimy, incline,
                    block, force, dashed, ball, spring, bars, shade_between,
                    arcarrow, rot_block)
import figs_jee as J
import figs_oly as O
import figs_circ as C

KEYS = {
    # Part I — work, energy, power
    'work_signs': J.work_signs,
    'fx_area': J.fx_area,
    'force_audit': J.force_audit,
    'we_derivation': J.we_derivation,
    'ke_frames': J.ke_frames,
    'friction_ledger': J.friction_ledger,
    'power_curve': J.power_curve,
    'constant_power': J.constant_power,
    'loop_test': J.loop_test,
    'pe_definition': J.pe_definition,
    'spring_work': J.spring_work,
    'gravity_paths': J.gravity_paths,
    'energy_ledger': J.energy_ledger,
    'u_landscape': J.u_landscape,
    'force_gradient': J.force_gradient,
    'decision_map': J.decision_map,
    'system_energy': J.system_energy,
    'efficiency': J.efficiency,
    'chain_energy': J.chain_energy,
    'spring_friction': J.spring_friction,
    'slope_power': J.slope_power,
    'wpe_map': J.wpe_map,
    # Part II — Olympiad layer
    'cm_decomposition': O.cm_decomposition,
    'effective_potential': O.effective_potential,
    'bounce_energy': O.bounce_energy,
    'rolling_energy': O.rolling_energy,
    'wedge_energy': O.wedge_energy,
    'launch_energy': O.launch_energy,
    'chain_unroll': O.chain_unroll,
    'bead_energy': O.bead_energy,
    'restitution_energy': O.restitution_energy,
    'flywheel': O.flywheel,
    'pseudo_work': O.pseudo_work,
    'path_integral': O.path_integral,
    'drag_power': O.drag_power,
    'energy_limits': O.energy_limits,
    # Part III — circular motion
    'omega_alpha': C.omega_alpha,
    'alpha_kinematics': C.alpha_kinematics,
    'omega_vector': C.omega_vector,
    'centripetal_two_ways': C.centripetal_two_ways,
    'at_an': C.at_an,
    'alpha_integral': C.alpha_integral,
    'relative_angular': C.relative_angular,
    'work_radial': C.work_radial,
    'vertical_energy': C.vertical_energy,
    'string_vs_rod': C.string_vs_rod,
    'conical_energy': C.conical_energy,
    'bank_limits': C.bank_limits,
    'rotor_wall': C.rotor_wall,
    'curvature_fit': C.curvature_fit,
}


def figure(ax, key):
    fig = ax.figure
    ax.axis('off')
    KEYS[key](fig)
    return key
