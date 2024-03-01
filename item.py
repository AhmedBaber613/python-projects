

'''
name = 'jo'

if len(name) < 3:
  print('Name must be three charachters long')
elif len(name) > 50:
  print('Name must be less than fifty charachters long')
else:
  print('Name is valid')
print('Enjoy your day')

'''

sec_num = 9
i = 0

while i < 3:
  guess = int(input('Guess: '))
  i+= 1

  if guess == sec_num:
     print('You Win!!!')
     break
else:
    print('You Lost')







