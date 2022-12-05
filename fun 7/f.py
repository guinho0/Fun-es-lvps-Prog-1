def f_qp(n):
  j = (n//2)+1
  for i in range(1,j+1):
    if(n > i**2):
      d = n-i**2
    else:
      d = i**2-n
    if (i == 1):
      dif = d
      q = i
    elif(d < dif):
      dif = d
      q = i
  return q
def f_quad(n):
  qp = f_qp(n)
  quad = (n+(qp**2))/(2*qp)
  return quad