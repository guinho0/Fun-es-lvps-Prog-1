def main():
    n = int(input('n: '))
    t1 = 1
    t2 = 1
    print(t1)
    print(t2)
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        print(t3)
        t1 = t2
        t2 = t3
        cont+=1
        
    
    return 0
    
 
main()