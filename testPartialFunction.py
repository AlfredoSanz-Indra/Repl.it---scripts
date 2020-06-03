
from functools import partial

def power(base, exponent):
  print('base=' + str(base))
  print('exponent=' + str(exponent))

  return base ** exponent
#


squared = partial(power, exponent=2)

a = squared(3)
print('a=' + str(a))

b = squared(base=7)
print('b=' + str(b))