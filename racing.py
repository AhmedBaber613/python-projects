command = ''
started = False
while command != "quit":
  command = input('> ').lower()
  if command == "start":
    if started:
       print("car is already started!!!")
    else:
     started = True
     print("car started")
  elif command == "stop":
    if not started:
      print("car is already stopped!!!")
    else:
      started = False
      print("car stoped")
  elif command == "help":
    print("start - to start the car\nstop - to stop the car\nquit - to exit the game")
  elif command == "quit":
    break
  else:
    print("I dont understand that....")
      