try:
  age = int(input('Age: '))
  income = int(input('yearly income: '))
  risk = income // age
  print('Risk is ',risk,'%')
except ZeroDivisionError:
  print('Age cannot be Zero... ')
except ValueError:
  print('Invalid value ')
