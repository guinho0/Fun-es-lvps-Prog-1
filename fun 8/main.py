#mdc entre 3 valores
def f_menor(a,b,c):
    if(a<b and a <c):
        return a 
    elif (b<c):
        return b
    else:
        return c
def f_mdc(a,b,c):
    x = f_menor(a,b,c)
    while (x>0):
        if (a%x==0 and b%x ==0 and c%x ==0):
            return x
        x = x-1