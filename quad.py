from arith import arithEq
from graph import graph,addpts
import numpy as np
def quadratic(eq,x):
    eqn=eq
    abc=[0,0,0]
    term(eq,abc)
    c=abc[0]
    b=abc[1]
    a=abc[2]
    determinant = b*b-4*a*c
    res=""
    # condition for real and different roots
    if (determinant > 0):
    # sqrt() function returns square root
        root1 = (-b+(determinant**.5))/(2*a)
        root2 = (-b-(determinant**.5))/(2*a)
        addpts([root1,root2],[0,0])
        res=f"\t\t{x} = ({round(root1,2)},{round(root2,2)})\n"
    #condition for real and equal roots
    elif (determinant == 0):
        root1=root2 = -b/(2*a)
        addpts([root1],[0])
        res=f"\t\t {x} = {root1}\n"
       # if roots are not real
    else:
        realPart = -b/(2*a);
        imaginaryPart = (-determinant)**.5/(2*a);
        root1=root2= -b/(2*a)
        res=f"\t\t{x} =( {round(realPart,2)}+i{round(imaginaryPart,2)} , {round(realPart,2)}-i{round(imaginaryPart,2)})\n"
    xpts=np.linspace(-2-min(root1,root2),2+max(root1,root2),1000)
    ypts=[list(map(lambda x:a*x**2+b*x+c,xpts))]
    graph(xpts,ypts,[eqn],"Quadratic Equations")
    return res
def term(eq,abc):
    s=0  #starting index of term
    sign=1
    term=""
    for i in range(len(eq)):
        if(i==0 and eq[i]=='-'):##checks if number is negative i.e., first character is -
            i+=1
        if(eq[i] == '+' or eq[i] == '-' or eq[i] == '=' or i == len(eq)-1):#enters the block only if end of a term is reached
            e=i  #ending index of term
            if i == len(eq)-1:#includes last character if character is last index of the equation
                e=i+1 
            if(eq[s] == '+' or  eq[s] == '=' ):# skip the character
                        s+=1
            for j in range(s,e):
                term+=eq[j]
            s=i
            p=power(term)
            cof=int(abc[p])
            cof+=(sign*coeff(term))
            abc[p]=cof
            if(eq[i]=='='):
                sign=-1
            term=""
def coeff(term):
    sign=1
    c2=""
    if(term[0]=='-'):
        sign=-1
        term=term[1:]
    for i in range(len(term)):
        if(term[i].isdigit()):
            c2+=term[i]
        else:
            break
    if c2=="":
        c2="1"
    coef=arithEq(c2)*sign
    return coef
def power(term):
    for i in range(len(term)):
        if(term[i]=='-'and i==0):
            continue
        if((term[i]).isalpha()):
            i+=1 
            if(i==len(term)):
                return 1
            else:
                return int(term[i+1])
    return 0
