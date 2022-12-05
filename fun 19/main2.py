#LVP f 19
def f_toUpper(s):
  s2 = ""
  for i in range(len(s)):
    if (ord(s[i]) >= 97 and ord(s[i]) < 122):
      s2 += chr(ord(s[i])-32)
    else:
      s2 += s[i]
  return s2

def main():
  s = input()
  print(f_toUpper(s))
  return 0
    
if __name__ == "__main__":
  main()   

