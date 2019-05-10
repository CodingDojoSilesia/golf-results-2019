import sys
w=' '
a='@'
g=60
hstrip=lambda c,h,s:[(c+(s*w))*g]*h
vstrip=lambda c:[c*g]
empty=lambda h:[0]*int(h)
zigzag=lambda c,s:[(w*d+c+w*(s*2-1-2*d)+c+w*d)*g for d in range(s)]
def cross(c,s):
 p=s//2
 a=[(w*p+c+w*p+w)*g]*p
 return[*a,(s*c+w)*g,*a]
def maze(c,v,h):
 y=c+w*(v-1)
 return[(y+v*c)*g,*[y*g]*(h-2),(c*v+y)*g]if h>1 else[c*g]
def f():
 for c in sys.argv[1].split(':'):
  n,m,*k=c.split(',')
  yield from eval(n)(m,*map(int,k))
 yield from[0]*g
for x,z,p in zip([22,19,17,15,13,12,11,10,9,8,7,6,5,4,4,3,2,2,2,1,1,*[0]*13,1,2,2,3,5,6,8,10,12,15,19],[8,3,2,2,2,*[1]*32,2,1,2,2,2,3,4,11],f()):
 s=x+z
 l=g-2*s
 print(f'{w*x}{a*z}{p[s:s+l]if p else w*l}{a*z}{w*x}')
