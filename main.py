# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = input()
lst = filter(lambda x: 'абв' not in x, str.split(' '))
print(' '.join(lst))

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

s = 2021
while s > 28:
    x = int(input('Игрок 1, сколько вы возьмете? '))
    if x > 28:
        print('Невозможное количество. Еще раз')
    else:
        res = s - x
        print(res)
        if res <= 28:
            print('Игрок 2, вы выиграли')
            break
    y = int(input('Игрок 2, сколько вы возьмете? '))
    if y > 28:
        print('Невозможное количество. Еще раз')
        y = int(input())
        res = res - y
        s = res
        print(res)
    else:
        res = res - y
        s = res
        print(res)
        if res <= 28:
            print('Игрок 1, вы выиграли')
            break


# 3. Создайте программу для игры в ""Крестики-нолики"".
def input_check(field_status):
    while True:
        print('куда ставим?')
        try:
            pos = int(input())
            if pos > 0 and pos < 10:
                if field_status[positions[pos - 1][1]][positions[pos - 1][2]] != 'O' \
                        and field_status[positions[pos - 1][1]][positions[pos - 1][2]] != 'X':
                    return pos
                else:
                    print('поле уже занято, выберите другое')
            else:
                print('введите цифру от 1 до 9')
        except:
            print('РОДИНА ОПАСНОСТЕ!!! \n товарищ, нам нужна цифра от 1 до 9')
def rewrite_field(pole, act_field):
    pole = f'+___ ___ ___+ ' \
            f'\n| {act_field[0][0]} | {act_field[0][1]} | {act_field[0][2]} |' \
            '\n+--- --- ---+' \
            f'\n| {act_field[1][0]} | {act_field[1][1]} | {act_field[1][2]} |' \
            '\n+--- --- ---+' \
            f'\n| {act_field[2][0]} | {act_field[2][1]} | {act_field[2][2]} |' \
            '\n+--- --- ---+'
    return pole
def win_check(win_combinations, player_moves):
    for i in range(len(win_combinations)):
        if win_combinations[i][0] in player_moves \
                and win_combinations[i][1] in player_moves \
                and win_combinations[i][2] in player_moves:
            return 'победа'

positions = [(1, 0, 0), (2, 0, 1), (3, 0, 2), (4, 1, 0), (5, 1, 1), (6, 1, 2), (7, 2, 0), (8, 2, 1), (9, 2, 2)]
wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]]
actual_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
field = f'+___ ___ ___+ ' \
            f'\n| {actual_field[2][0]} | {actual_field[2][1]} | {actual_field[2][2]} |' \
            '\n+--- --- ---+' \
            f'\n| {actual_field[1][0]} | {actual_field[1][1]} | {actual_field[1][2]} |' \
            '\n+--- --- ---+' \
            f'\n| {actual_field[0][0]} | {actual_field[0][1]} | {actual_field[0][2]} |' \
            '\n+--- --- ---+'

player_1 = input('введите имя первого игрока: ')
player_2 = input('введите имя второго игрока: ')
players = [(0, player_1, 'X'), (1, player_2, 'O')]
steps = [[], []]
for i in range(9):
    player = players[i % 2][1]
    print(f'ходит {player} \n', rewrite_field(field, actual_field))
    step = input_check(actual_field)
    steps[i % 2].append(step)
    if i >= 4:
        if win_check(wins, steps[i % 2]) == 'победа':
            actual_field[positions[step - 1][1]][positions[step - 1][2]] = players[i % 2][2]
            print(f'победа игрока {player}!\n', rewrite_field(field, actual_field))
            break
    actual_field[positions[step - 1][1]][positions[step - 1][2]] = players[i % 2][2]
    if i == 8:
        print('Ничья...')

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

string = 'wwwwwwwbbbbbbbddddddd'
count = 1
rlecode = ' '
for i in range(len(string) - 1):
    if string [i] == string[i+1]:
        count += 1
    else:
        rlecode = rlecode +str(count) + string[i]
        count = 1
if count > 1 or (string[len(string) - 2] != string[-1]):
    rlecode = rlecode + str(count) + string[-1]
print(f'Текст после кодировки: {rlecode}')

