# Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)

import os

os.system('cls')

counter = 0 
game_on = 0

player_one_name = input('Введите имя первого игрока: ')
player_two_name = input('Введите имя второго игрока: ')

one = ' '
two = ' '
three = ' '
four = ' '
five = ' '
six = ' '
seven = ' '
eight = ' '
nine = ' '

def print_board() -> str:

    """Функция рисует игровую доску"""
    
    os.system('cls')

    print('\n' + one + ' | ' + two + ' | ' + three + '\n' + four + ' | ' + five + ' | ' + six + '\n' + seven + ' | ' + eight + ' | ' + nine)
    print()

def check_if_win() -> str:
    
    """Функция проверяте выиграл ли игрок"""
    
    if one == two and two == three and one != ' ':
        
        if counter%2 == 1:
            print('\nПоздравляем, ' + player_one_name + ', Вы выиграли!')
            exit()
        
        else:
            print('\nПоздравляем, ' + player_two_name + ', Вы выиграли!')
            exit()
  
    elif four == five == six and four != ' ':
        
        if counter%2 == 1:
            print('\nПоздравляем, ' + player_one_name + ', Вы выиграли!')
            exit()
        
        else:
            print('\nПоздравляем, ' + player_two_name + ', Вы выиграли!')
            exit()
  
    elif seven == eight == nine and seven != ' ':
        
        if counter%2 == 1:
            print('\nПоздравляем, ' + player_one_name + ', Вы выиграли!')
            exit()
            
        else:
            print('\nПоздравляем, ' + player_two_name + ', Вы выиграли!')
            exit()
  
    elif one == four == seven and one != ' ':
        
        if counter%2 == 1:
            print('\nПоздравляем, ' + player_one_name + ', Вы выиграли!')
            exit()
        
        else:
            print('\nПоздравляем, ' + player_two_name + ', Вы выиграли!')
            exit()
  
    elif two == five == eight and two != ' ':
        
        if counter%2 == 1:
            print('\nПоздравляем, ' + player_two_name + ', Вы выиграли!')
            exit()
        
        else:
            print('\nПоздравляем, ' + player_two_name + ', Вы выиграли!')
            exit()
  
    elif three == six == nine and three != ' ':
        
        if counter%2 == 1:
            print('\nПоздравляем, ' + player_one_name + ', Вы выиграли!')
            exit()
        
        else:
            print('\nПоздравляем, ' + player_two_name + ', Вы выиграли!')
            exit() 
  
    elif one == five == nine and one != ' ':
        
        if counter%2 == 1:
            print('\nПоздравляем, ' + player_one_name + ', Вы выиграли!')
            exit()
    
        else:
            print('\nПоздравляем, ' + player_two_name + ', Вы выиграли!')
            exit()
            
    elif seven == five == three and seven != ' ':
        
        if counter%2 == 1:
            print('\nПоздравляем, ' + player_one_name + ', Вы выиграли!')
            exit()
        
        else:
            print('\nПоздравляем, ' + player_two_name + ', Вы выиграли!')
            exit()
  
    elif counter == 9:
      print('\nПобедила дружба!')
      exit()
  
possible_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print('Давайте начнем. ' + player_one_name + ' начинает игру.')

print_board()

while game_on == 0: 

  while counter%2 == 0:

    move = input(player_one_name + ', выберите поле (от 1 до 9): ')

    if move in possible_inputs:

      counter += 1

      possible_inputs.remove(move)

      if move == '1':
        one = 'X'

      elif move == '2':
        two = 'X'

      elif move == '3':
        three = 'X'

      elif move == '4':
        four = 'X'

      elif move == '5':
        five = 'X'

      elif move == '6':
        six = 'X'

      elif move == '7':
        seven = 'X'

      elif move == '8':
        eight = 'X'

      elif move == '9':
        nine = 'X'
    
      print_board()
      check_if_win()
      
      continue
    
    else:
      print('Извините, либо поле уже сыграло, либо Вы ввели неправильный номер.\n')
      continue

  while counter%2 != 0:
    
    move = input(player_two_name + ', выберите поле: ')
    
    if move in possible_inputs:

      counter += 1
      possible_inputs.remove(move)

      if move == '1':
        one = 'O'

      elif move == '2':
        two = 'O'

      elif move == '3':
        three = 'O'

      elif move == '4':
        four = 'O'

      elif move == '5':
        five = 'O'

      elif move == '6':
        six = 'O'

      elif move == '7':
        seven = 'O'

      elif move == '8':
        eight = 'O'

      elif move == '9':
        nine = 'O'

      print_board()

      check_if_win()
      continue
    
    else:
      print('Извините, либо поле уже сыграло, либо Вы ввели неправильный номер.\n')
      continue