def DisplayMenu():
  print()
  print()
  print('MAIN MENU')
  print()
  print('1. Add 10 to the number')
  print('2  Is the number odd?')
  print('3. Subtract 10 from the number')
  print('4. Enter a new number')
  print('5. Quit')
  print()
  print('Please enter your choice: ', end='')

def GetNumber():
  Number = int(input('Please enter a number: '))
  return Number 

def GetChoice():
  OptionSelected = int(input())
  while OptionSelected < 1 or OptionSelected > 5:
    print('Please enter a number between 1 and 5')
    OptionSelected = int(input())
  return OptionSelected

def AddTen():
  global NumberEntered
  BiggerNumber = Number + 10
  return BiggerNumber

if __name__ == '__main__':
  Number = GetNumber()
  Choice = 0
  while Choice != 5:
    DisplayMenu()
    Choice = GetChoice()
    print()
    if Choice == 1:
      print('The number 10 bigger than ', Number, end = '')
      Number = AddTen()
      print(' is: ', Number)
    elif Choice == 2:
      input()
    elif Choice == 3:
      input()
    elif Choice == 4:
      input()
  input()
