

def fatorial(n):#fatorial
    fat = 1
    while n >= 1:
        fat = fat*n
        n = n-1
    return fat

def main():
    
    n = int(input())
    while n >= 0:
        
        
        fato = fatorial(n)
        print(f'Fatorial({n})={fato} ')
        while n > 0:
            n = int(input())
            fato = fatorial(n)
        
            
            if n == 0:
                print(1)
            else:
                print(fato)
            
        n = int(input())        
    return 0
main()