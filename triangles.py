import random
def which_triangle(a, b, c):
  all_sides_are_equal = a == b == c
  one_pair_of_sides_is_equal = a == b or a == c or b == c
  no_pair_of_sides_are_equal = not (a == b or a == c or b == c)

  if all_sides_are_equal:
    print('Equilateral')
  elif one_pair_of_sides_is_equal:
    print('Isosceles')
  elif no_pair_of_sides_are_equal:
    print('Scalene')

def keep_producing_random_numbers():
  a = random.randint(1,200)
  b = random.randint(1,200)
  c = random.randint(1,200)
  random_choices = [a,b,c]
  print(random_choices)

#instantiate initial variables
a = 200
b = 12
c = 11


a_con = a < b + c
b_con = b < a + c
c_con = c < a + b
all_conditions_satisfied = a_con and b_con and c_con
if(all_conditions_satisfied):
  res = [a,b,c]
  which_triangle(a,b,c)
  print(res)
else:
  print('not a triangle')
  while not all_conditions_satisfied:
      keep_producing_random_numbers()
