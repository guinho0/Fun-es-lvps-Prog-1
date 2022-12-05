def main():
    cont  = 0
    n = int(input())
    p = int(input())
    for i in range(0,p):
        while i > 0:
            resto = i%10
            i  = i//10
            if resto == n:
                cont+=1
    print(cont)

   
    return 0
main()