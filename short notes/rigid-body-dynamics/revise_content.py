"""Dense JEE revision: expanded MOI teaching and derivations, not formula-only sheets.
Called by author_content.py; edit this file for the revised additions.
"""
from copy import deepcopy

def C(title,*items):return dict(title=title,items=list(items))
def p(s):return ('p',s)
def m(s):return ('m',s)
def why(s):return ('why',s)
def trap(s):return ('trap',s)
def sheet(slug,title,subtitle,source,diagrams,takeaway,*cards):
 return dict(section='JEE',key=slug,title=title,subtitle=subtitle,source=source,diagrams=diagrams,takeaway=takeaway,cards=list(cards))

def revise(pages):
 pages=deepcopy(pages)
 # Fill previously unused card space with useful derivation steps and results.
 extra={
 'kinematics':[
 [m(r'\vec v_B-\vec v_A=\vec\omega\times\vec r_{B/A}'),p('For any two points A and B on the body, their relative velocity has no component along AB.')],
 [m(r'\alpha=\omega\,d\omega/d\theta'),p('For variable alpha, integrate d(omega)=alpha dt or omega d(omega)=alpha d(theta); do not use constant-alpha shortcuts.')],
 [m(r'a=\sqrt{(\alpha r)^2+(\omega^2r)^2}'),p('The two components are perpendicular for fixed-axis circular motion. At the axis both are zero.')],
 [m(r'\omega=\frac{v_B-v_A}{AB}'),p('This signed shortcut needs parallel velocities perpendicular to AB and a consistent direction. Otherwise use the vector relation.')]],
 'axis-theorems':[
 [m(r'I_A=I_C+Md^2+2d\int x\,dm'),m(r'\int x\,dm=0\quad\mathrm{at\ C}'),p('For fixed orientation, the parallel COM axis minimises I. Equality occurs only at d=0.')],
 [m(r'I_{\rm ring,tangent\ in\ plane}=\frac32MR^2'),m(r'I_{\rm ring,rim\ normal}=2MR^2'),p('A thin ring diameter has I=MR²/2. Add MR² to the appropriate central-axis result.')],
 [m(r'I_x=\int y^2dm,\quad I_y=\int x^2dm'),m(r'I_z=\int(x^2+y^2)dm'),p('The three axes must share a single origin, though that point need not be C.')],
 [m(r'I_A-I_B=M(d_A^2-d_B^2)'),p('Here d(A) and d(B) are distances from the same parallel COM axis, not from each other.')]],
 'torque-energy':[
 [m(r'\vec\tau_B=\vec\tau_A-\vec r_{B/A}\times\vec F_{\rm net}'),p('If net force is zero, net torque is origin-independent. A couple has magnitude F times the separation of its force lines.')],
 [m(r'\sum F_x=Ma_{C,x},\quad\sum F_y=Ma_{C,y}'),p('Write the translation and rotation equations before inserting a no-slip or string constraint. Forces through C can still move C.')],
 [m(r'P=\vec F\cdot\vec v_C+\tau_{C,z}\omega'),p('For one applied force in planar motion, this equals its force dotted with the velocity of its actual point of application.')],
 [m(r'T_1=m_1(g+a),\quad T_2=m_2(g-a)'),p('Add the mass equations to (T2-T1)=Ia/R²; the effective inertial mass is m1+m2+I/R².')]],
 'angular-momentum':[
 [m(r'L_z=mvb\quad\mathrm{(particle)}'),p('b is the signed perpendicular distance from O to the velocity line; a line through O gives L=0 even at large speed.')],
 [m(r'\Delta L_z=\int\tau_{{\rm ext},z}\,dt'),p('Zero net force alone does not imply zero torque: a pure couple changes L without changing COM momentum.')],
 [m(r'\Delta K=\frac{L_z^2}{2}(I_2^{-1}-I_1^{-1})'),p('Conversely, spreading mass outward at fixed L decreases rotational KE; mechanical work must account for that change.')],
 [p('Derivation: conserve the sum I1 omega1+I2 omega2; insert the common final omega into Kf=(I1+I2) omega(f)²/2. Subtract Kf from Ki to obtain Q.')]],
 'rolling-geometry':[
 [m(r'v-R\omega=V_{\rm belt}'),p('For a moving horizontal belt use its signed lab speed V(belt). On a straight belt a-R alpha equals its acceleration.')],
 [m(r'\vec a_P=\vec a_C+\vec\alpha\times\vec r_{P/C}'),m(r'\qquad-\omega^2\vec r_{P/C}'),p('At the bottom, the tangential terms cancel in pure rolling; the remaining term points upward.')],
 [m(r'K=\frac12M(1+\beta)v^2,\quad\beta=I_C/(MR^2)'),p('Disc: K=3Mv²/4. Hoop: K=Mv². Solid sphere: K=7Mv²/10. All use v of C.')],
 [m(r'I_P=I_C+MR^2'),p('In the scalar shortcut keep one signed rotation convention. Friction, weight-normal reaction and any force through P have zero moment about P.')]],
 'incline':[
 [m(r'\beta=I_C/(MR^2),\quad f=\beta Ma'),p('Eliminate f from the two balances. For uphill motion the acceleration still points downhill; friction is still uphill in this force-free case.')],
 [m(r'\tan\theta\leq\mu_s(1+\beta)/\beta'),p('If this fails from release, use kinetic friction and separate a from R alpha; no-slip energy formulas cannot be imposed.')],
 [m(r'h_{\rm stop}=\frac{(1+\beta)v_0^2}{2g}'),p('For pure rolling up a straight incline, path distance is h(stop)/sin(theta). Stop and reverse if the constraint remains valid.')],
 [m(r'v_{\rm disc}/v_{\rm hoop}=\sqrt{4/3}'),p('At the same vertical drop, a smooth block has v=sqrt(2gh). A rough sliding block is not necessarily fastest.')]],
 'slip-to-roll':[
 [m(r'\dot u=-s\mu_k g(1+1/\beta)'),p('Friction direction stays fixed until u first vanishes. If v crosses zero earlier, that alone is not a reason to reverse friction.')],
 [m(r'v+\beta R\omega=v_0+\beta R\omega_0'),p('Derivation: add the two acceleration equations with the second multiplied by beta. Set the final slip to zero.')],
 [m(r'Q=\mu_k Mg\frac{|u_0|t_*}{2}'),p('The slip-speed graph is a triangle. Its area is relative sliding distance, not COM displacement.')],
 [m(r'x_*=v_0t_*-\frac12s\mu_k gt_*^2'),p('For the no-spin numerical case x*=400/49 m. This is a COM displacement measured from first contact.')]],
 'driven-rolling':[
 [m(r'|f|\leq\mu_s Mg'),p('At h=beta R no friction is needed: the applied force supplies translation and spin in exactly the rolling ratio.')],
 [m(r'f_{h=0}=-\frac{\beta F}{1+\beta}'),p('Disc centre-pull: a=2F/(3M), f=-F/3. Contrasting it with a top pull is a quick sign check.')],
 [m(r'a_{\rm upper}=\frac{F(\cos\phi+r/R)}{M(1+\beta)}'),p('For an upper-hub tangent the string torque is clockwise, so the reversal criterion differs. Draw the tangent explicitly.')],
 [m(r'\phi_c=\cos^{-1}(r/R)'),p('For r/R=1/4, phi(c)=75.52°. At the critical angle a=0 and f=-F cos(phi), provided static contact can support it.')]],
 'yoyo':[
 [m(r'v=r\omega'),p('The fixed string cancels the velocity of the hub contact; it does not make the body’s centre stationary.')],
 [m(r'Mgr=(Mr^2+I)\alpha'),p('This is the combined equation with a=r alpha. It also checks the acceleration dimensions without assuming a solid disc.')],
 [m(r'r\ll R:\quad a\simeq2g(r/R)^2'),p('As I tends to zero at fixed r, a tends to g and T tends to zero. As I grows large, a tends to zero and T tends to Mg.')],
 [m(r'Tr\omega-Tv=0'),p('Tension removes translational power and supplies the same rotational power. Gravity supplies the net increase in total KE.')]],
 'collisions':[
 [m(r'\omega_+=\frac{mvd}{Ml^2/3+md^2}'),p('If the bullet velocity makes angle gamma with the rod, replace vd by vd sin(gamma); use the signed moment arm.')],
 [p('At d→0, final spin and final KE vanish; Q tends to the whole incident bullet KE. Do not maximise omega to maximise the loss.')],
 [m(r'\cos\theta_{\max}=1-\frac{I_f\omega_+^2}{2g(Ml/2+md)}'),p('This gives a turning point only when the right-hand side lies between -1 and 1.')],
 [p('After impact the bullet and rod are one composite body. Its new inertia includes the embedded point mass; using the bare rod inertia misses angular momentum.')]],
 'equilibrium':[
 [m(r'f\leq\mu_sN_g,\quad N_w,N_g\geq0'),p('An extra person or load adds its own moment about the base. Recompute rather than reuse the uniform-ladder threshold.')],
 [m(r'F_{\rm tip}=Mgb/y,\quad F_{\rm slide}=\mu_s Mg'),p('For a level-floor block pushed horizontally at height y, compare these thresholds; b is half-width of the base.')],
 [m(r'A_{\rm tip}=gb/h'),p('For the same block carried by a horizontal support, the effective-weight line reaches the rear edge at this acceleration, if it has not slipped first.')],
 [p('For the top n blocks their combined COM must lie above the next support. Adding one block shifts that COM; balancing this shift gives l/(2n).')]],
 'oscillations':[
 [m(r'I_O=I_C+Md^2'),p('Use the pivot axis, not the COM axis, in the period. The restoring sign is negative about downward equilibrium.')],
 [m(r'T_{\rm rod,end}=2\pi\sqrt{2l/(3g)}'),m(r'T_{\rm disc,rim}=2\pi\sqrt{3R/(2g)}'),p('Memorise the standard results, but know which d and I produce each one.')],
 [m(r'U=Mgq(1-\cos\theta)'),p('Energy is K+U constant. Differentiate it to get the exact equation, then linearise; there is no small-angle step in the kinetic energy.')],
 [m(r'\frac{T}{T_{\rm simple}}=\sqrt{1+\beta}'),p('As beta→0 recover a point mass on a circular path. The effective inertia, not extra mass, lengthens the period.')]],
 'sliding-rod':[
 [m(r'v_C^2=(l^2/4)\dot\theta^2'),p('While both contacts persist, the instantaneous centre is the intersection of their velocity normals; it is not the bottom endpoint.')],
 [m(r'\frac{Ml^2}{6}\dot\theta^2=\frac{Mgl}{2}(\sin\theta_0-\sin\theta)'),p('The effective rotational inertia in this one-coordinate energy is Ml²/3, but the body is not rotating about a fixed floor point.')],
 [m(r'N_{g,*}=Mg/4'),p('The floor still pushes at detachment. Afterwards the wall force is zero and the two-contact circular-COM constraint must be dropped.')],
 [p('Fast checks: dimensions of I; moment arm perpendicular to force; torque sign; beta consistent with the body; mu(s) inequality; normal and tension nonnegative; physically allowed limiting case.')]]}
 for pg in pages:
  key=pg['slug'].split('/',1)[1][3:]
  pg['key']=key
  if key in extra:
   for c,items in zip(pg['cards'],extra[key]):c['items']=list(c['items'])+items

 moi=[]
 moi.append(sheet('moi-rods-plates','MOI I: rods, plates & axes',
  'Learn the standard results with their axes; the integral explains each coefficient. Uniform bodies unless stated.',
  '§§3.3–3.4; D8.2; added JEE MOI derivations',['rod_axes','plate_axes'],
  'A moment of inertia without an axis is an incomplete result. Read each formula together with its geometry.',
 C('Definition: weighted distance²',m(r'I_A=\int r_\perp^2dm,\quad I_A=Mk_A^2'),m(r'K=\frac12I_A\omega^2'),p('k is the radius of gyration about A. For fixed-axis rotation each mass has speed omega r(perp), so summing dm v²/2 proves the energy result.'),why('Distant mass matters quadratically, not linearly. I depends on shape and axis, not angular speed.'),m(r'0\leq I_A\leq MR_{\max}^2'),p('The bound assumes every element is within distance R(max) from A. Units: kg m².')),
 C('Thin rod: centre, end, offset',p('Length l, mass M; x along the rod measured from its midpoint. All axes here are perpendicular to the rod.'),m(r'dm=(M/l)dx'),m(r'I_C=\frac Ml\int_{-l/2}^{l/2}x^2dx=\frac{Ml^2}{12}'),m(r'I_A=M(l^2/12+d^2)'),m(r'I_{\rm end}=Ml^2/3'),why('Shift from the centre by d. An end axis has d=l/2, so 1/12+1/4=1/3.'),trap('A zero-thickness rod about its own length has I=0; a real thick rod does not.')),
 C('Rectangular and square plates',p('Rectangle a along x, b along y; origin C. x,y lie in the plate, z is normal.'),m(r'I_x=Mb^2/12,\quad I_y=Ma^2/12'),m(r'I_z=M(a^2+b^2)/12'),p('Derive Ix by strips parallel to x: dm=(M/b)dy; integrate y² dm. Use the perpendicular-axis theorem for Iz.'),m(r'I_{\rm edge\parallel x}=Mb^2/3'),m(r'a=b=s:\ I_z=Ms^2/6'),why('For a square any central in-plane axis, including a diagonal, has I=Ms²/12. Symmetry removes the cross term.')),
 C('Inclined axis through the rod',p('Axis through C makes angle phi with a thin rod. A point at signed coordinate x has perpendicular distance |x sin(phi)|.'),m(r'I_C(\phi)=\frac{Ml^2}{12}\sin^2\phi'),m(r'I_{\rm end}(\phi)=\frac{Ml^2}{3}\sin^2\phi'),why('Insert r(perp)=|x sin(phi)| into the integral, not x itself. Parallel-axis shifts must stay perpendicular to the chosen axis.'),p('Checks: phi=0 gives zero for a line rod; phi=90° gives the usual transverse result.'),trap('Do not use a simple sin² rule for a finite-width plate without accounting for its other dimension.'))))
 moi.append(sheet('moi-circular','MOI II: rings, discs & annuli',
  'Here z is the central normal to the lamina. A diameter is an in-plane axis through the circle centre O.',
  '§3.3; E1; Q1; added circular-lamina derivations',['circular_axes','semicircle'],
  'Normal-axis and diameter-axis results differ by a factor of two for a complete circular lamina or thin ring.',
 C('Thin ring: learn three axes',m(r'I_z=MR^2'),p('Every element is the same distance R from the normal axis, so the integral immediately equals R² times M.'),m(r'I_{\rm diameter}=MR^2/2'),why('Two perpendicular diameters are equivalent by symmetry and their inertias add to Iz.'),m(r'I_{\rm tangent,in-plane}=3MR^2/2'),m(r'I_{\rm rim\ normal}=2MR^2'),trap('“Tangent” alone does not specify whether the axis is in the plane or normal to it.')),
 C('Disc: concentric-ring derivation',m(r'\sigma=M/(\pi R^2),\quad dm=2\pi\sigma r\,dr'),m(r'I_z=2\pi\sigma\int_0^Rr^3dr=MR^2/2'),m(r'I_{\rm diameter}=MR^2/4'),m(r'I_{\rm rim\ normal}=3MR^2/2'),m(r'I_{\rm tangent,in-plane}=5MR^2/4'),why('A disc includes rings of every radius: it has less axial inertia than a ring of the same M and R.'),p('Radius of gyration: k(z)=R/sqrt(2), k(diameter)=R/2.')),
 C('Annulus: subtract or integrate',p('Inner radius a, outer radius b, mass M. Uniform areal density sigma=M/[pi(b²-a²)].'),m(r'I_z=2\pi\sigma\int_a^b r^3dr'),m(r'I_z=\frac12M(a^2+b^2)'),m(r'I_{\rm diameter}=\frac14M(a^2+b^2)'),why('Use b⁴-a⁴=(b²-a²)(b²+a²). Alternatively subtract two discs with their original common density.'),p('Checks: a=0 gives a disc. As a→b at fixed mass the annulus approaches a thin ring.'),trap('M is the remaining annulus mass, not the mass of the uncut outer disc.')),
 C('Half-circle: O is not its COM',p('For a semicircular disc: O is the original circle centre; C lies on its symmetry line above the diameter.'),m(r'OC=4R/(3\pi),\quad I_{O,z}=MR^2/2'),m(r'I_{C,z}=MR^2/2-M(4R/(3\pi))^2'),p('For a semicircular wire instead: OC=2R/pi and I(O,z)=MR²; subtract M(OC)² to get I(C,z).'),why('Cutting a uniform circle in half leaves the average r² about O unchanged; the new COM is displaced.'),trap('These are derivable applications, not a reason to memorise every cut shape. Always distinguish O from C.'))))
 moi.append(sheet('moi-solids','MOI III: cylinders & spheres',
  'Axial = cylinder symmetry axis; transverse = perpendicular through C; a sphere diameter passes through C.',
  '§3.3; D8.2; added standard 3-D MOI derivations',['cylinder_axes','sphere_slice'],
  'Do not apply the perpendicular-axis theorem to a 3-D body. Slice it into thin laminae and integrate instead.',
 C('Solid cylinder: both directions',p('Uniform cylinder radius R, length l. For its symmetry axis each thin disc contributes half dm R².'),m(r'I_{\rm axial}=MR^2/2'),m(r'I_{\rm transverse}=M(3R^2+l^2)/12'),m(r'dI_{\rm transverse}=(R^2/4+z^2)dm'),why('Each slice contributes its own diameter inertia plus its parallel-axis shift. Integrate z from -l/2 to l/2 with dm=(M/l)dz.'),p('l→0 gives a disc diameter; R→0 gives a thin rod transverse to its length.')),
 C('Hollow cylinder: inner radius a',p('Outer radius b, length l, total remaining mass M. Uniform material, common central axis.'),m(r'I_{\rm axial}=M(a^2+b^2)/2'),m(r'I_{\rm transverse}=M[3(a^2+b^2)+l^2]/12'),why('Derive by subtracting solid coaxial cylinders at the same density, or replace each slice by an annular lamina.'),m(r'\mathrm{thin\ wall}:\ I_{\rm axial}=MR^2'),m(r'I_{\rm transverse}=M(6R^2+l^2)/12'),trap('A thin cylindrical wall has no end caps in this model. Its transverse inertia is not that of a thin ring unless l→0.')),
 C('Solid sphere: derive by discs',p('Let x run along the diameter axis; slice radius s satisfies s²=R²-x². Density rho=3M/(4 pi R³).'),m(r'dm=\rho\pi(R^2-x^2)dx'),m(r'I=\frac{\rho\pi}{2}\int_{-R}^R(R^2-x^2)^2dx'),m(r'I_C=2MR^2/5,\quad I_{\rm tangent}=7MR^2/5'),why('A disc slice rotates about its own normal: dI=dm s²/2, not dm s².'),p('Spherical symmetry makes every central diameter equivalent. k(C)=sqrt(2/5) R.')),
 C('Spherical shells: thin and thick',p('Thin uniform shell: a latitude strip at polar angle theta has dm=(M/2)sin(theta)d(theta) and r(perp)=R sin(theta).'),m(r'I=\frac{MR^2}{2}\int_0^\pi\sin^3\theta\,d\theta'),m(r'I_{\rm thin}=2MR^2/3'),m(r'I_{\rm thick}=\frac{2M}{5}\frac{b^5-a^5}{b^3-a^3}'),why('The thick-shell formula subtracts two same-density solid spheres, inner a and outer b. a→0 gives solid; a→b gives thin shell.'),trap('A sphere has no special normal axis like a disc; specify a diameter or a displaced parallel line.'))))
 moi.append(sheet('moi-composites','MOI IV: composites & integrations',
  'Memorise the standard families; derive unfamiliar density profiles and cut shapes from a few reliable moves.',
  '§§3.3–3.4; Q18; added JEE integral/composite applications',['disc_hole','density_graph'],
  'For a cut-out use the removed piece’s original density and its own COM; shift all contributions to the requested axis.',
 C('An off-centre circular hole',p('Full disc mass M0, radius R; hole radius a, centre offset d. Hole fits inside the disc. Both densities are unchanged.'),m(r'm_h=M_0a^2/R^2,\quad M=M_0-m_h'),m(r'I_{O,z}=M_0R^2/2-m_h(a^2/2+d^2)'),m(r'x_C=-m_hd/M'),m(r'I_{C,z}=I_{O,z}-Mx_C^2'),why('Take +x toward the hole. Removing mass shifts C away from it. Subtract hole inertia about O, then shift from O to the new C.'),trap('Never assign the hole a mass M a²/R² using the remaining mass M.')),
 C('Nonuniform rod: normalise first',p('Rod from x=0 to l; linear density lambda=cx. Need its mass, COM and transverse inertia.'),m(r'M=cl^2/2,\quad c=2M/l^2'),m(r'x_C=\frac1M\int_0^l x(cx)dx=2l/3'),m(r'I_{0}=\int_0^l x^2(cx)dx=Ml^2/2'),m(r'I_C=I_0-Mx_C^2=Ml^2/18'),why('The uniform-rod formulas do not apply. Fix the density constant from the total mass before integrating.'),p('Check: C moves toward the denser end; I0 still has dimensions mass times length squared.')),
 C('Radially varying disc density',p('A circular lamina has sigma(r)=c r^n, 0<r<R, n>-2. Here c is determined by mass, not arbitrary.'),m(r'dm=2\pi c r^{n+1}dr'),m(r'M=\frac{2\pi cR^{n+2}}{n+2}'),m(r'I_z=MR^2\frac{n+2}{n+4}'),m(r'I_{\rm diameter}=I_z/2'),why('Divide the inertia integral by the mass integral; circular symmetry still equates central diameters.'),p('n=0 gives a disc; n→infinity concentrates mass near the rim and approaches MR².')),
 C('Cone & the right learning habit',p('A uniform solid cone of height h, base radius R has radius s=Rz/h at distance z from its vertex.'),m(r'dm=\rho\pi(Rz/h)^2dz'),m(r'I_{\rm axis}=\int_0^h\frac12(Rz/h)^2dm'),m(r'I_{\rm axis}=3MR^2/10'),why('Divide by M=rho pi R²h/3. This is the same disc-slicing idea as a sphere, not specialised rotational theory.'),p('Prioritise rods, rings, discs, cylinders, spheres and axis shifts. For unfamiliar shapes know how to derive the needed result rather than memorising an unbounded catalogue.'))))

 free=sheet('free-impacts','Impulses: free bodies & hinges',
  'During a short impact ignore gravity impulse; smooth supports give no horizontal impulse. Keep all spin signs consistent.',
  '§3.10; Parts 7–9; added core impulse/restitution derivations',['eccentric_impulse','percussion'],
  'A free body translates and spins after an eccentric impulse. A hinge changes which momentum equation is useful.',
 C('Impulse on an initially resting body',p('Impulse magnitude J acts horizontally with perpendicular lever arm b from the target COM. Mass M, planar COM inertia I.'),m(r'V_C=J/M,\quad |\omega|=Jb/I'),m(r'K=\frac{J^2}{2}(1/M+b^2/I)'),why('Integrate F=Ma for translation and torque=I alpha about C for spin. Add their kinetic energies.'),p('The contact-point speed component along J is J(1/M+b²/I); define an effective mass by the reciprocal of this bracket.'),trap('A force line through C (b=0) gives pure translation, not spin.')),
 C('A particle hits the free target',p('Incoming particle mass m and speed v. The target initially rests. The impact impulse is along the incident line; e is normal restitution.'),m(r'D=1/m+1/M+b^2/I'),m(r'J=(1+e)v/D'),m(r'v_{m,+}=v-J/m'),why('The target’s contact speed is J(1/M+b²/I). Restitution sets target-contact speed minus outgoing particle speed equal to e v.'),m(r'Q=(1-e^2)v^2/(2D)'),trap('e=0 means zero relative separation speed in the impact direction; it does not by itself enforce permanent sticking.')),
 C('Hinged rod: support impulse',p('A resting rod is hinged at O. Its COM is distance d from O; a perpendicular impulse J strikes distance b from O. I(O) is the hinge inertia.'),m(r'\omega_+=Jb/I_O,\quad V_C=d\omega_+'),m(r'J_H=MV_C-J'),m(r'J_H=J(Mdb/I_O-1)'),why('Angular impulse about the hinge eliminates its unknown impulse; linear impulse then determines the hinge reaction.'),p('J(H) is signed along the incoming impulse. It can oppose it, vanish, or act in the same direction.')),
 C('Centre of percussion',m(r'b_{\rm cp}=I_O/(Md)'),p('At this strike distance, J(H)=0: no transverse shock is transmitted to the ideal hinge.'),m(r'\mathrm{uniform\ rod}:\quad b_{\rm cp}=2l/3'),why('Insert I(O)=Ml²/3 and d=l/2. This is the same length I(O)/(Md) that appears in the physical pendulum.'),p('Conditions: initially stationary rigid body, fixed hinge, short transverse impulse, no other transverse impulses.'),trap('A free rod and a hinged rod are different systems. Do not conserve their linear momentum in the same way.')))
 energy=sheet('energy-contact','Energy, reactions & curved rolling',
  'Harder JEE applications still use the same core laws. Energy gives speed; force balance tests contact.',
  'Q10; §§3.8, 3.10; added support/loop applications',['falling_rod','rolling_loop'],
  'Energy conservation alone cannot establish continued contact, pure rolling, or an admissible support force.',
 C('A rod falls about a fixed hinge',p('Uniform rod length l, mass M, released horizontally from rest. theta is its downward angle from the initial horizontal.'),m(r'Mg(l/2)\sin\theta=\frac12(Ml^2/3)\omega^2'),m(r'\omega^2=(3g/l)\sin\theta'),m(r'\alpha=(3g/2l)\cos\theta'),why('Take gravitational torque about the hinge. Energy supplies omega; torque supplies alpha.'),p('At the lowest point omega=sqrt(3g/l), alpha=0, but the COM still has inward centripetal acceleration.')),
 C('Hinge reaction is not Mg',p('At release the rod is horizontal; C accelerates downward with magnitude alpha l/2=3g/4.'),m(r'H_y-Mg=-3Mg/4\ \Rightarrow\ H_y=Mg/4'),p('At the lowest point C accelerates upward at omega²l/2=3g/2.'),m(r'H_y-Mg=3Mg/2\ \Rightarrow\ H_y=5Mg/2'),why('The fixed hinge does no work, but it does supply force and impulse. “No work” does not mean “no force”.'),trap('Between these positions use BOTH tangential and radial COM acceleration before resolving the hinge reaction.')),
 C('Rolling inside a vertical loop',p('Track inner radius R; body radius r; q=R-r is the COM path radius. beta=I(C)/(M r²). theta is measured from the bottom.'),m(r'v^2=2g[h-q(1-\cos\theta)]/(1+\beta)'),m(r'N=M(v^2/q+g\cos\theta)'),why('Energy uses the COM height. Radially inward: N-Mg cos(theta)=Mv²/q. At the top this becomes N+Mg=Mv²/q.'),p('h is the initial COM height above its lowest path point. Require N>=0 along the motion.'),trap('Do not use the track radius R in the COM centripetal term.')),
 C('Minimum height: a conditional result',m(r'v_{\rm top}^2\geq gq'),m(r'h\geq\frac{5+\beta}{2}q'),p('Derive by imposing N(top)>=0 in the energy equation. beta=0 recovers the particle loop result 5q/2.'),why('This is the ideal-constraint energy/contact lower bound, not a guarantee for a real rough roller.'),m(r'|f|=\frac{\beta}{1+\beta}Mg|\sin\theta|'),trap('Check |f|<=mu(s)N everywhere. Near marginal top contact, finite friction may be insufficient even if the top-speed condition holds. A higher release height can be needed.')))

 result=[]
 for pg in pages:
  if pg['key']=='inertia':result.extend(moi);continue
  result.append(pg)
  if pg['section']=='JEE' and pg['key']=='collisions':result.append(free)
  if pg['section']=='JEE' and pg['key']=='equilibrium':result.append(energy)
 for section in ['JEE','Olympiad']:
  n=0
  for pg in result:
   if pg['section']!=section:continue
   n+=1;pg['part_page']=n;pg['slug']=f'{section}/{n:02}-{pg["key"]}'
 return result
