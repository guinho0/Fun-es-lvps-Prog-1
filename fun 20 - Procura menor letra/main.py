def menorletra(s):
    menor = s[0]
    for i in range(1,len(s)):
        if (s[i]<menor):
            menor = s[i]
    return menor
def main():
        s = input().upper()
        while s != "":
            print(menorletra(s))
            s = input().upper()
    
        return 0
main()