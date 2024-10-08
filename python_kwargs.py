def sum1_of(**kwargs):
  sum1 = 0
  for k, v in kwargs.items():
    sum1 += v
  return sum1

#kwargs - we can pass key, value pair variables.

print(sum1_of(coffee=2.99, cake=4.55, juice=2.99))