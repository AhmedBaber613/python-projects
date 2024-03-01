name = input('Hi I am robo What is your name? ')
print(name,'lets talk but you have to answer me in yes or no ')
mood = input('are you fine ')
if mood.lower() == 'yes':
  print('Great')
  sport = input('Do you like sports? ')
  if sport.lower() ==  'yes':
    print('Oh I love sports to ')
  elif sport.lower() == 'no':
    print('Try playing cricket its realy fun ')
  trav = input('Do you like to travel I love Berlin in Germany do you like Germany? ')
  if trav.lower() == 'yes':
    print(' Oh I think we have a lot in common')
  elif trav.lower() == 'no':
    print('Oh I think you need to go to the UAE ')
  code = input('Do you like to code? ')
  if code.lower() == 'yes':
    print('wich language do you prefer')
  elif code.lower() == 'no':
    print('Oh you poor thing you should code to it is very fun')
  Ger = input('Do you know some german ')
  if Ger.lower() == 'yes':
    print('I love german to!! ')
  elif Ger.lower() == 'no':
    print('Lets learn german together ')
elif mood.lower() == 'no':
  print('what happend ')