import random


def password():
  lower = 'qwertyuiopasdfghjklzxcvbnm'
  upper = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
  numbers = '1234567890'
  symbols = '<>?;[]@#$%^&*()!{}~`-.,+=_'
  string = lower + upper + numbers + symbols
  legnth = int(input('How many characters should your password have? '))
  password = "".join(random.sample(string,legnth))
  print('Your New 100% secure password is:', password)
  feed_back = input('Is this password good or bad? ')
  if feed_back.lower() == 'good':
    print('Thanks for your feedback! ')
  elif feed_back.lower() == 'bad':
    print('Oh sorry That was very unusual ')
password()


