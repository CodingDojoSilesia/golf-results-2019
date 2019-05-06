import math,sys
def rep(s,c,st,stop):
    for x in range(st,stop):s=s[:x]+c+s[x+1:]
    return s
def egg():
    r,d='',[(22,30),(19,22),(17,19),(15,17),(13,15),12,11,10,9,8,7,6,5,4,4,3,2,2,2,1,1]+[0]*13+[1,2,2,(3,5),5,(6,8),(8,10),(10,12),(12, 15),(15, 19),(19,30)]
    l=[eval(f'rep("{" "*30}","@",{v[0]},{v[1]})') if type(v) is tuple else eval(f'rep("{" "*30}","@",{v},{v+1})') for v in d]
    return [x+x[::-1] for x in l]
def zigzag(c,s):return [(xl+" "+xrl)*40 for xl,xrl in zip([(' '*s)[:i]+c+(' '*s)[i+1:] for i in range(s)],[(' '*s)[:i]+c+(' '*s)[i+1:] for i in range(s)][::-1])]
def maze(c,v,h):
    x=[c*v if i==h-1 else c+" "*(v-1) for i in range(h)]
    return [(xl+xrl)*40 for xl, xrl in zip(x,x[::-1])]
def cross(c,s):return [xl*40 for xl in [c*s+" " if i+1==math.ceil(s/2) else (' '*s)[:math.ceil(s/2)-1]+c+(' '*s)[math.ceil(s/2):]+" " for i in range(s)]]
def hstrip(c,s,sh):return [(c+' '*sh)*40 for _ in range(s)]
def vstrip(c):return [c*60]
def empty(s):return [" "*60 for _ in range(s)]
def f_p(args):
    p=[]
    for a in args:
        f,*r=a.split(",")
        r=[int(x) if x.isnumeric() else x for x in r]
        p+=globals()[f](*r)
    return p
def p_e(args):
    eg,r,p=egg(),'',f_p(args)
    for n, l in enumerate(eg):
        if n!=0 and n!=44:
            b=l.index("@")+l.count("@")//2
            if n<len(p) and 1<len(p):l=l[:b]+(p[n])[b:60-b]+l[60-b:]
        r+=l+'\n'
    return r
if __name__=="__main__":
    try:a=sys.argv[1]
    except IndexError:
        r=''
        for x in egg():r+=x+'\n'
        print(r,end="")
    else:print(p_e(a.split(":")),end="")
