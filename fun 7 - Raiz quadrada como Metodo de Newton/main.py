import f


def main():
  n =  int(input())
  while (n >= 0):
    q = f.f_quad(n)
    print(f'N={n:.4f} RAIZ={q:.6f}')
    n = int(input())
  return 0
if __name__=="__main__":
  main()