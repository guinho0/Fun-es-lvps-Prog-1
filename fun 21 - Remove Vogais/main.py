def maiu(s):
    s = s.upper()
    return s
def main():
    s = input()
    s = maiu(s)
    while s != '':#condição de parada é quando a resposta for "nada". não coloque um espaço em branco, coloque aspas vazias.
       
        for letra in s:
            if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
                s =  s.replace(letra, "")
        print(s)
        s = input().upper()
       # s = s.upper()
    return 0
main()