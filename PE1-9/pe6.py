#
# find the difference of the sum of the squares and the square of the sums of
# the first 100 natural numbers
#

def diff(n):
  s1 = sumofsq(n)
  s2 = sqofsums(n)
  print s2-s1

# wait. range defaults to 0. that's sweet.
def sumofsq(n):
  sum = 0
  for i in range(n + 1):
    sum += i * i
  return sum

# haha. algebra.
def sqofsums(n):
  s = (n + 1) * (n / 2)
  if n % 2 != 0:
    s += (n / 2) + 1
  return s * s


