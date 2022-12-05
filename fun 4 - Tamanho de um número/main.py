#funçaõ que revela o tamanho de um número.
def tam(n):
    n = str(n) #primeiramente, deve-se transformar o número em uma string, assim são contados os seus caracteres.
    t = len(n)
    return t
def main():
    n = int(input('n: '))
    print(tam(n)) #chame a função na main.
    return 0
main()

