import ocr
import detect
import arith
from simult import simult
from linear import linear
import algebra as alg
from quad import quadratic
path='C:\\Users\\ajay umakanth\\Desktop\\miniproj\\database\\im.png'
def solve(path):
    eq=ocr.ocr(path)
    if(detect.isArith(eq)):
        if(detect.isArithEq(eq)):
                return(f"\t\t{arith.arithEq(eq)}\n")
        else:
                if(arith.arithIneq(eq)):
                    return("\t\tTrue\n")
                else:
                    return("\t\tFalse\n")
    else:
            nterm,var=alg.checknovar(eq)
            if(nterm==1):
                pow=alg.checkdegree(eq,var[0])
                if(pow==1):
                    return(linear(eq,var[0]))
                elif(pow==2):
                    return(quadratic(eq,var[0]))
                elif(pow==3):
                    return("Cubic equation\n")
                else:
                    return("Can solve up to 3rd degree polynomial only!!\n")
            elif(nterm==2):
                return(simult(eq,var,nterm))
            elif(nterm==3):
                print("Simultaneous equation three variables\n")
            else:
                print("Can solve equations upto 3 vaiables only!!!\n")

