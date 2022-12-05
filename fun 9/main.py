import f

def main():
  n = int(input("n: "))
  while (n >= 0):
   print(f"DEC={n} BIN={f.f_decToBin(n)} HEX={f.f_decToHex(n)}")
   n = int(input())
  return 0

if __name__ == "__main__":
 main()