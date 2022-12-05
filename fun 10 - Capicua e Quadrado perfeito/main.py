import f

def main():
 #n = int(input("n: "))
 #print(f.f_tam(n))
 #print(f.f_inverte(n))
 #print(f.f_qp(n))
 #print(f.f_ehCapicua(n))
 for n in range(1,5001):
   if (f.f_qp(n) and f.f_ehCapicua(n)):
     print(f'{n} É CAPICUA E QUADRADO PERFEITO')
   elif (f.f_ehCapicua(n)):
     print(f'{n} É CAPICUA')
   elif (f.f_qp(n)):
     print(f'{n} É QUADRADO PERFEITO')


 return 0

if __name__ == "__main__":
 main()