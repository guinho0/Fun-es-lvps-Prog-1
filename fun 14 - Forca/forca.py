import os #peguei do seu replit , mas editei pois não estava rodando no ava!!

def f_forca(s):
  forca = ""
  for i in range(len(s)):
    forca += "_"
  return forca

def f_print(texto):
  for i in range(len(texto)):
    print(texto[i],end=" ")
  print()

def f_atualiza(letra,forca,segredo):
  s = ""
  for i in range(len(segredo)):
    if (letra == segredo[i]):
      s += letra
    else:
      s += forca[i]
  return s

def f_verifica(f,s):
  return f == s
      
def main():
  ganhou = False
  jogadas = 0
  erradas = ""
  cont = 0
  segredo = input("Segredo: ").upper()
  os.system("clear")
  forca = f_forca(segredo)
  
  while (cont < 6 and not ganhou): #falta condição de parada quando o usuário vence
    
    #print(erradas)
    letra = str(input()).upper()
    #colocar validação para letras repetidas
    jogadas += 1
    #if (f_verifica(letra,segredo)):
    if letra in segredo:
      forca = f_atualiza(letra,forca,segredo)
    else:
      erradas += letra
      cont += 1
    ganhou = f_verifica(segredo, forca)
    f_print(forca)
    print(erradas)
   
    
  if (ganhou):
    print(f"Parabéns, você ganhou com {jogadas} jogadas")
  else:
    print(f"Que pena, você não acertou a palavra {segredo}")
  return 0

if __name__ == "__main__":
 main()