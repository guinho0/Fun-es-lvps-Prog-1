def main():
    conta = 0
    palavra = input().upper()
    print(palavra)
    while palavra != "":
        palavra2= ""
        n = False
        for letra in palavra:
            if letra not in palavra2:
                palavra2+=letra
            else:
                n = True
        if n == True:        
            for letra in palavra2:
                freq = palavra.count(letra)
                
                print(f'{letra} = {freq}')
        else:
           
            print("NÃO EXISTEM LETRAS REPETIDAS")
           
        palavra = input().upper()
        print(palavra)
    return 0
main()
