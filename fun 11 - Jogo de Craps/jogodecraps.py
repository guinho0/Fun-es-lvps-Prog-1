from random import randrange

def f_jogaDado():
  return randrange(1,7)

def f_ganhouPrimeira(dado):
  if dado == 7 or dado == 11:
    return True
  return False

def f_perdeuPrimeira(dado):
  if dado == 2 or dado == 3 or dado == 12:
    return True
  return False

def f_craps(dado):
    print(dado)
    jogadas = 1
    if f_ganhouPrimeira(dado):
      return 1, jogadas
    elif f_perdeuPrimeira(dado):
      return -1, jogadas
    else:
        continua = True
        x = int(input())
        #x = f_jogaDado() + f_jogaDado()
        while x != 7 and x != dado:
            print(x)
            jogadas +=1
            x = int(input())
            #x = f_jogaDado() + f_jogaDado() 
    return x, jogadas+1

def main():
    #dado = f_jogaDado() + f_jogaDado()
    dado = int(input())
    #print (dado)
    craps, jogadas = f_craps(dado)  
    if (craps == 1):
      print ("NATURAL! VOCÊ GANHOU")
      print(f'JOGADAS = {jogadas}')
    elif (craps == -1):
      print ("CRAPS! VOCÊ PERDEU")
      print(f'JOGADAS = {jogadas}')
    elif (craps == 7):
      print(craps)
      print ("VOCÊ PERDEU")
      print(f'JOGADAS = {jogadas}')
    elif (craps == dado):
      print(craps)
      print ("VOCÊ GANHOU")
      print(f'JOGADAS = {jogadas}') 
    return 0

if __name__ == '__main__':
    main()