def f_armstrong(n):
 p = len(n)
 soma = 0
 for i in range(p):
   soma += int(n[i]) ** p
 return soma

def f_verificaArmstrong(n):
 return n == f_armstrong(str(n))

def main():
 for n in range(1,1000000):
   if (f_verificaArmstrong(n)):
     print(n)
 return 0

if __name__ == "__main__":
 main()