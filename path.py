import random

name = input('What is your name? ')
print(name, 'Now I will guess your age ')
upper_limit = 70
lower_limit = 8
age = random.randint(lower_limit, upper_limit)
print('I think your age is', age)

print('press 1 if I am correct')
print('press 2 if you are older')
print('press 3 if you are younger')
choice = int(input())
while True:
  if choice == 1:
    print('I am a genius')
    break
  if choice == 2:
    lower_limit = age
    age = random.randint(lower_limit, upper_limit)
    print('You are older')
    print('I think your age is', age)
  print('press 1 if I am correct')
  print('press 2 if you are older')
  print('press 3 if you are younger')
  choice = int(input())
  if choice == 3:
    print('You are younger')
    upper_limit = age
    age = random.randint(lower_limit, upper_limit)
    print('I think your age is', age)
  print('press 1 if I am correct')
  print('press 2 if you are older')
  print('press 3 if you are younger')
  choice = int(input())