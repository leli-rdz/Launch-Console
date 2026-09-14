def launch_console():
  print("Welcome to the Launch Console!")
  user_name = input("What is your name?: ")
  print(f"Hello, {user_name}! Nice to meet you.")
  while True:
    print("Main Menu")
    print("1. About me")
    print("2. My Goals")
    print("3. Fun Fact")
    print("4. Exit")
    choice = input("What would you want to know? (1-4): ")
    if choice == '1':
      print('About me: My name is Leslie Rodriguez. I am a Junior at Weiss Highschool')
    elif choice == '2':
      print("My Goals: I want to become an Enginner, but I'm still unsure as to which field.")
    elif choice == '3':
      print('Fun Fact: I am the oldest in my family and I have a younger sister!')
    elif choice == '4':
      print('Goodbye!')
      break
    else:
      print('To learn about me choose a number 1 - 4: ')
    
    
