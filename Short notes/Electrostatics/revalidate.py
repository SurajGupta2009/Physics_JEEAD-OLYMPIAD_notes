"""Additional pre-publication physics checks using direct quadrature and numerical derivatives.

This complements, not replaces, test_exports.py. It checks the stated mathematical
models independently; it is not exhaustive certification of every prose sentence.
"""
from pathlib import Path
import json,math
import numpy as np
ROOT=Path(__file__).resolve().parent
RESULTS=[]
def close(name,value,expected,rtol=2e-7,atol=2e-9):
 value=float(value);expected=float(expected)
 assert math.isfinite(value) and abs(value-expected)<=atol+rtol*abs(expected),(name,value,expected)
 RESULTS.append({'name':name,'value':value,'expected':expected})
def derivative(f,x,h=1e-5):return (f(x+h)-f(x-h))/(2*h)
def integral(f,a,b):
 u,w=np.polynomial.legendre.leggauss(128)
 x=(a+b)/2+(b-a)*u/2
 return float((b-a)/2*np.dot(w,f(x)))
def main():
 RESULTS.clear()
 # Dimensionless k, source charge/length and characteristic radius = 1 unless noted.
 for x in [.15,.7,2.4]:
  close(f'ring -dV/dx at {x}',-derivative(lambda z:1/np.sqrt(1+z*z),x),x/(1+x*x)**1.5)
  close(f'disc ring-element field integral at {x}',integral(lambda s:2*np.pi*s*x/(x*x+s*s)**1.5,0,1),2*np.pi*(1-x/np.sqrt(x*x+1)))
  close(f'disc -dV/dx at {x}',-derivative(lambda z:np.sqrt(1+z*z)-z,x),1-x/np.sqrt(x*x+1))
  close(f'annulus -dV/dx at {x}',-derivative(lambda z:np.sqrt(z*z+4)-np.sqrt(z*z+.25),x),x*(1/np.sqrt(x*x+.25)-1/np.sqrt(x*x+4)))
  close(f'finite rod bisector integral at {x}',integral(lambda s:x/(x*x+s*s)**1.5,-1,1),2/(x*np.sqrt(1+x*x)))
  close(f'finite rod -dV/dd at {x}',-derivative(lambda d:2*np.arcsinh(1/d),x),2/(x*np.sqrt(1+x*x)))
  close(f'end-on rod integral at {x}',integral(lambda s:1/(x+s)**2,0,1),1/(x*(x+1)))
 # Unequal rod: direct Cartesian integral verifies BOTH component signs.
 for a,b,d in [(.7,1.4,.8),(2,.3,.6)]:
  close(f'rod parallel a={a}',integral(lambda s:-s/(s*s+d*d)**1.5,-a,b),1/np.sqrt(b*b+d*d)-1/np.sqrt(a*a+d*d))
  close(f'rod perpendicular a={a}',integral(lambda s:d/(s*s+d*d)**1.5,-a,b),(a/np.sqrt(a*a+d*d)+b/np.sqrt(b*b+d*d))/d)
 for angle in [.4,math.pi/2,math.pi,2*math.pi]:
  close(f'arc bisector integral angle={angle}',integral(np.cos,-angle/2,angle/2),2*math.sin(angle/2))
 for r in [1.2,2.5,6]:
  a=.5;p=2*a
  close(f'dipole exact axial pair sum r={r}',1/(r-a)**2-1/(r+a)**2,2*p*r/(r*r-a*a)**2)
  close(f'dipole exact equator r={r}',-2*a/(r*r+a*a)**1.5,-p/(r*r+a*a)**1.5)
 for theta in [.3,1.1,math.pi/2]:
  r=2.
  close(f'dipole angular gradient theta={theta}',-derivative(lambda t:np.cos(t)/r**2,theta)/r,np.sin(theta)/r**3)
  close(f'dipole torque from energy theta={theta}',-derivative(lambda t:-np.cos(t),theta),-np.sin(theta))
 for n in [0,1,2]:
  for r in [.2,.8]:
   close(f'radial density Q n={n} r={r}',integral(lambda s:4*np.pi*s**(n+2),0,r),4*np.pi*r**(n+3)/(n+3))
 for r in [.2,.7,1.4,3]:
  pot=lambda s:(3-s*s)/2 if s<1 else 1/s
  close(f'uniform sphere -dV/dr at {r}',-derivative(pot,r),r if r<1 else 1/r**2)
 for x in [-2,-.5,.5,2]:
  pot=lambda y:-y*y/2 if abs(y)<1 else -abs(y)+.5
  close(f'slab signed -dV/dx at {x}',-derivative(pot,x),np.clip(x,-1,1))
 a=np.array([.2,-.1,.3]);r=np.array([.35,.25,-.2])
 # k=1 => epsilon0=1/(4pi), fixed uniform density=1.
 efull=4*np.pi*r/3;eremoved=-4*np.pi*(r-a)/3
 for i in range(3):close(f'insulating spherical cavity component {i}',(efull+eremoved)[i],4*np.pi*a[i]/3)
 # Image construction must satisfy the entire spherical boundary, not a single axis point.
 d=2.3;qp=-1/d;b=1/d
 for theta in np.linspace(0,np.pi,9):
  ds=np.sqrt(1+d*d-2*d*np.cos(theta));di=np.sqrt(1+b*b-2*b*np.cos(theta))
  close(f'grounded sphere V(boundary) theta={theta}',1/ds+qp/di,0)
  close(f'neutral sphere V(boundary) theta={theta}',1/ds+qp/di+1/d,1/d)
 for h in [.3,1,3]:
  close(f'plane image energy gradient h={h}',-derivative(lambda z:-1/(4*z),h),-1/(4*h*h))
 for d in [1.3,2,4]:
  close(f'sphere image force energy d={d}',-derivative(lambda s:-1/(2*(s*s-1)),d),-d/(d*d-1)**2)
  close(f'neutral sphere two-image force d={d}',(-1/d)/(d-1/d)**2+(1/d)/d**2,-d/(d*d-1)**2+1/d**3)
 # For q=1, h=1, induced density normalisation is -1/(2pi(1+s^2)^(3/2)).
 close('plane density integrates to minus source charge',integral(lambda t:-np.sin(t),0,math.pi/2),-1)
 close('hemisphere projected area integral',integral(lambda t:2*np.pi*np.sin(t)*np.cos(t),0,math.pi/2),math.pi)
 for radius in [.6,1.7]:
  close(f'pressure from shell energy R={radius}',-derivative(lambda R:.5/R,radius)/(4*np.pi*radius**2),1/(8*np.pi*radius**4))
 # Near-centre off-axis ring checks: numerical Hessian signs and trace.
 phi=np.linspace(0,2*np.pi,40000,endpoint=False)
 vplane=lambda s:np.mean(1/np.sqrt(1+s*s-2*s*np.cos(phi)))
 vaz=lambda z:1/np.sqrt(1+z*z)
 h=1e-3
 transverse=(vplane(h)+vplane(-h)-2*vplane(0))/h**2
 axial=(vaz(h)+vaz(-h)-2*vaz(0))/h**2
 close('ring transverse potential curvature',transverse,.5,rtol=2e-6)
 close('ring axial potential curvature',axial,-1,rtol=2e-6)
 close('ring numerical Hessian trace',2*transverse+axial,0,atol=2e-6)
 # Quadrature convergence of singularity-transformed cube kernel.
 values=[]
 for order in [24,48,96]:
  u,w=np.polynomial.legendre.leggauss(order);x=(u+1)/2;w=w/2
  X,Y=np.meshgrid(x,x);values.append(1.5*np.sum(np.outer(w,w)/np.sqrt(1+X*X+Y*Y)))
 close('cube 24/96 point quadrature convergence',values[0],values[-1],rtol=1e-12)
 close('cube 48/96 point quadrature convergence',values[1],values[-1],rtol=1e-12)
 report={'status':'PASS','independent_checks':len(RESULTS),'method':'direct Gaussian quadrature, Cartesian sums, finite differences and boundary residuals','checks':RESULTS}
 (ROOT/'verification-recheck.json').write_text(json.dumps(report,indent=2)+'\n')
 print(f'PASS: {len(RESULTS)} additional independent pre-publication physics checks.')
if __name__=='__main__':main()
