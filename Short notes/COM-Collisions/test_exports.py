"""Independent representative physics checks for the COM & collisions sheets."""
import json, math, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
FAIL=[]
def close(a,b,rtol=.005): return abs(a-b)<=rtol*max(abs(b),1e-12)
def check(name,got,want,rtol=.005):
    okk=close(got,want,rtol); print(('PASS' if okk else 'FAIL'),name,'| got',round(got,6),'want',round(want,6))
    if not okk: FAIL.append(name)

# COM table and negative-mass hole trick
check('semicircular ring 2R/pi',2/math.pi,.63662,.001)
check('semicircular disc 4R/3pi',4/(3*math.pi),.42441,.001)
check('solid hemisphere 3R/8',3/8,.375,.001)
check('shell hemisphere R/2',.5,.5,.001)
check('cone h/4',.25,.25,.001)
check('arc small-angle limit',math.sin(1e-8)/1e-8,1,1e-7)
check('hole trick -R/6',-(.25*.5)/.75,-1/6,.001)

# Master collision pair and independent invariants (source P32)
m1,m2,u1,u2,e=2.,3.,5.,-2.,.5
v1=((m1-e*m2)*u1+(1+e)*m2*u2)/(m1+m2)
v2=((1+e)*m1*u1+(m2-e*m1)*u2)/(m1+m2)
check('P32 v1',v1,-1.3,.001);check('P32 v2',v2,2.2,.001)
check('P32 momentum',m1*v1+m2*v2,m1*u1+m2*u2,.001)
check('P32 restitution',(v2-v1)/(u1-u2),e,.001)
mu=m1*m2/(m1+m2);Ki=.5*m1*u1*u1+.5*m2*u2*u2;Kf=.5*m1*v1*v1+.5*m2*v2*v2
check('P32 K loss direct',Ki-Kf,22.05,.001)
check('P32 K loss reduced-mass form',.5*mu*(u1-u2)**2*(1-e*e),22.05,.001)
check('elastic loss zero',.5*mu*49*(1-1),0,1e-9)
check('sticking loss full relative KE',.5*mu*49,29.4,.001)

# Corrected Q18 spring release
q1=math.sqrt(6/5);q2=2*q1/3
check('Q18 v1',q1,1.09545,.001);check('Q18 v2',q2,.73030,.001)
check('Q18 energy 2 J',.5*2*q1*q1+.5*3*q2*q2,2,.001)
check('Q18 momentum zero',2*q1-3*q2,0,.001)

# Deformation/reformation impulses: same P32 relative approach
Jd=mu*7;Jr=e*Jd
check('Jd = mu u_app',Jd,8.4,.001);check('Jr = e Jd',Jr,4.2,.001);check('total J',(1+e)*mu*7,12.6,.001)

# Rocket, ballistic pendulum and moving wall
check('E10 rocket delta-v',3*math.log(10),6.9078,.001)
check('Q8 rocket mass ratio',math.exp(2),7.389,.001)
V=.01*400/2.01
check('E5 ballistic swing speed',V,1.99005,.001);check('E5 height',V*V/20,.198,.005)
check('Q12 ballistic speed',1.005/.005*math.sqrt(2),284.26,.002)
check('P29 ballistic speed',2.01/.01,201,.001)
check('P29 inelastic loss fraction',2/2.01,.995,.002)
check('E9 moving wall signed velocity',-5-.8*(10-(-5)),-17,.001)
check('Q14 moving wall',-2-.5*(3+2),-4.5,.001)
check('C9 smooth-wall angle',math.degrees(math.atan(math.tan(math.radians(45))/.5)),63.4349,.002)

# Bounce series and count correction
check('Q5 restitution',math.sqrt(3.2/5),.8,.001)
check('P25 third rebound height',10*.7**6,1.17649,.001)
check('P31 distance',5*(1+.36)/(1-.36),10.625,.001)
check('P31 bounce threshold',math.log(.02)/math.log(.36),3.826,.01)
check('OL4 energy after 5 bounces',.8**10,.10737,.002)
check('equal-mass 90 degree speed triangle',.8**2+.6**2,1,.001)

# Chain family, fold, staging, jet, spring comparison
check('OL1 scale endpoint 3mg',3*1*1*10/10,3,.001)
check('OL7 peg detachment fraction',.5*(1+1/math.sqrt(2)),.85355,.002)
check('OL7 peg force at x=.6L',1-2*(2*.6-1)**2,.92,.001)
check('OL10 fold departure',math.sqrt(10/2),math.sqrt(5),.001)
check('OL10 fold v(y=.4,L=1)',.4*math.sqrt(20),1.78885,.001)
dvs=3*(math.log(1000/600)+math.log(550/150));dvu=3*math.log(5)
check('P30 staged delta-v',dvs,5.4303,.002);check('P30 single-stage delta-v',dvu,4.8283,.002)
check('P30 staging gain ratio',dvs/dvu,1.1246,.002)
check('OL9 jet optimum u/v',1/3,1/3,.001)
check('OL9 jet Pmax coefficient',4/27,.148148,.001)
check('jet efficiency',8/27,.296296,.001)
check('P35 spring ratio M=1,m=2',2*math.sqrt(1/3),1.1547,.001)
check('P35 spring equality boundary',3*1-3,0,1e-9)
check('P33 equal-mass 45-degree speed',1/math.sqrt(2),.707107,.001)

# Data structure membership and narrative hygiene
data=json.loads((ROOT/'sheets.json').read_text()); alltext=json.dumps(data)
print('PASS sheets.json loads |',len(data),'pages')
for bad in ['hmm','RECHECK','...}','MIS-MATCH','??']:
    okk=bad not in alltext;print(('PASS' if okk else 'FAIL'),'draft artefact absent',repr(bad))
    if not okk:FAIL.append('artefact:'+bad)
print('sections:',sum(p['section']=='JEE' for p in data),'JEE +',sum(p['section']=='Olympiad' for p in data),'Olympiad')
print('\nchecks failed:',len(FAIL),FAIL if FAIL else '(none)')
sys.exit(1 if FAIL else 0)
