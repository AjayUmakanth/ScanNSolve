def checknovar(eq):
    var=["","",""]
    vtop=-1
    found=1;
    for i in range(len(eq)):
        if((eq[i]).isalpha()):
            if(vtop==-1):
                vtop+=1
                var[vtop]=eq[i]
            else:
                for j in range(vtop+1):
                    if(var[j]==eq[i]):
                        found=0
                    if(found):
                        found=1;
                        if(vtop>2):
                             return -1
                        vtop+=1
                        var[vtop]=eq[i]
    return vtop+1,var
def checkdegree(eq,x):
     degree=0
     hdeg=1
     for i in range(len(eq)):
        if(eq[i]==x):
            i+=1
            if(i==len(eq)):
                degree=1
            else:
                if(eq[i]!='^'):
                    degree=1
                else:
                    i+=1
                    degree=int(eq[i])
            if(degree>hdeg):
                hdeg=degree         
     return hdeg
