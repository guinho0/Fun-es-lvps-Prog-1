from random import randrange
#função apenas para testar
def f_jogaDados():
  return randrange(1,7)

def f_testaResultado(dados,ponto,jogada):
  if (jogada == 1):
    if (dados == 7 or dados == 11):
      return 1
    elif (dados == 2 or dados == 3 or dados == 12):
      return 2
  else:
    if (dados == ponto):
      return 3
    elif (dados == 7):
      return 4
  return 5

def f_resultado(resultado,jogada):
  if (resultado == 1):
    print('NATURAL! VOCÊ GANHOU')
    print(f'JOGADAS = {jogada}')
  elif (resultado == 2):
    print('CRAPS! VOCÊ PERDEU')
    print(f'JOGADAS = {jogada}')
  elif (resultado == 3):   
    print('VOCÊ GANHOU')
    print(f'JOGADAS = {jogada}')
  else:
    print('VOCÊ PERDEU')
    print(f'JOGADAS = {jogada}')   

def main():
  jogada = 1
  #dados = int(input()) #para usar na LVP
  dados = f_jogaDados() + f_jogaDados()
  ponto = dados
  print(dados)
  resultado = f_testaResultado(dados,ponto,jogada)
  while (resultado == 5):  
    dados = f_jogaDados() + f_jogaDados()
    print(dados)
    jogada += 1
    resultado = f_testaResultado(dados,ponto,jogada)
  f_resultado(resultado,jogada)
  return 0

if __name__ == "__main__":
  main()