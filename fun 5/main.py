#algoritmo com função de inverter numero:
def f_tam(n):
  cont = 0
  while (n > 0):
    n = n // 10
    cont += 1
  return cont

def f_inverte(n):
  valor = 0
  tam = f_tam(n)
  p = tam - 1
  while (n > 0):
    resto = n % 10
    valor += resto * 10 ** p
    p = p - 1
    n = n // 10
  return valor

def main():
  n = int(input("n: "))
  invertido = f_inverte(n)
  print(invertido)
  return 0

if __name__ == "__main__":
  main()






     
     
        