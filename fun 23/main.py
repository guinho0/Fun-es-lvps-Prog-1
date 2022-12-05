def eh_vogal(l):
    if (l=="A"or l == "E"or l == "I" or l == "O" or l == "U"):
        return True
    return False
def remove(l,s):
    nova = ""
    for i in range(len(s)):
        if (s[i] != l):
            nova+=s[l]
    return nova
def naoexiste(l,s):
    for i in range(len(s)):
        if (s[i] == l):
            return False
    return True

def main():
    s2 = ""
    s = input().upper()
    while (s != ""):
        for letra in s:
            if (eh_vogal(letra)):
                if (naoexiste(letra,s2)):
                    s2+=letra
                    s = remove(letra,s)
            nova = s2 + s
            print(nova)
            s = input().upper()

    return 0
main()
                        
              
    

            
               

              

 