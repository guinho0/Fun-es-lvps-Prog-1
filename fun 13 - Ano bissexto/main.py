def f_bissexto(ano):
  if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
     return True
  else:
     return False

def main():
 ano = int(input("Ano: "))
 if (f_bissexto(ano)):
   print("É BISSEXTO")
 else:
   print("NÃO É BISSEXTO")
 return 0

if __name__ == "__main__":
 main()