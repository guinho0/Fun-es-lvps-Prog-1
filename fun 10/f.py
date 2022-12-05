def f_tam(n):
 cont = 0
 while (n > 0):
   n = n // 10
   cont += 1
 return cont

def f_inverte(n):
 x = 0
 p = f_tam(n)-1
 while (n > 0):
   resto = n % 10
   x += resto*10**p
   p = p - 1
   n = n // 10
 return x

def f_qp(n):
 metade = n // 2 + 1
 divisor = 1
 if (n == 1):
   return True
 while (divisor < metade):
   if (divisor ** 2 == n):
     return True
   divisor += 1
 return False

def f_ehCapicua(n):
 if (n == f_inverte(n) and n > 9) :
   return True
 else:
   return False