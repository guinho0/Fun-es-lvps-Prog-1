# se o numero for positivo retorna "p", negativo "N" e nulo "z".
def num(n):
    if n > 0:
        return "P"
    elif n < 0:
        return "N"
    else:
        return "Z"
def main():
    n = int(input())
    print(num(n))
    return 0
main()