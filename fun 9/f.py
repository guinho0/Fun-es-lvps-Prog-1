def f_decToBin(n):
 s = ""
 while (n > 0):
   resto = n % 2
   s = str(resto)+s
   n = n // 2
 return s

def f_hex(resto):
   s = "ABCDEF"
   return s[resto-10]

def f_hex2(r):
 if (r == 10):
   return "A"
 elif (r == 11):
   return "B"
 elif (r == 12):
   return "C"
 elif (r == 13):
   return "D"
 elif (r == 14):
   return "E"
 elif (r == 15):
    return "F"

def f_decToHex(n):
  s = ""
  while (n > 0):
    resto = n % 16
    if (resto < 10):
      s = str(resto)+s
    else:
      s = f_hex(resto)+s
    n = n // 16
  return s

    