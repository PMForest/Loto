"""== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html"""


import random
import sys

# program

barrel_in_game = 90
player1 = 15
player2 = 15
barrel = random.sample(range(90), 90)
game_set = random.sample(range(90), 30)
player1_set = random.sample(game_set, 15)
player2_set = [i for i in game_set if not i in player1_set]
player1_cart = [player1_set[:5], player1_set[5:10], player1_set[10:]]
player2_cart = [player2_set[:5], player2_set[5:10], player2_set[10:]]
for player1_line in player1_cart:
    player1_line.sort()
    player1_line.insert(random.randint(0, 4), '-')
    player1_line.insert(random.randint(0, 5), '-')
    player1_line.insert(random.randint(0, 6), '-')
    player1_line.insert(random.randint(0, 7), '-')
for player2_line in player2_cart:
    player2_line.insert(random.randint(0, 4), '-')
    player2_line.insert(random.randint(0, 5), '-')
    player2_line.insert(random.randint(0, 6), '-')
    player2_line.insert(random.randint(0, 7), '-')


# rules

def field(x):
    if x == 0:
        print('{:-^26}'.format('Карточка Игрока '))
        for line1 in player1_cart:
            for l1 in line1:
                print('{0:>2}'.format(l1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    if x == 1:
        print('{:-^26}\n'.format(' Карточка Компьютера '))
        for line2 in player2_cart:
            for l2 in line2:
                print('{0:>2}'.format(l2), end=' ')
            print()
        print('{:-^26}\n'.format('-'))


def player1_move():
    p = input('Зачеркнуть цифру? (y/n)')
    if p == 'y':
        if barr in player1_set:
            for l in player1_cart:
                try:
                    l.insert(l.index(barr), '$')
                    l.pop(l.index(barr))
                except ValueError:
                    continue
            print('\nOK')
            return 1
        else:
            print('\nGAME OVER')
            sys.exit()
    if p == 'n':
        if barr in player1_set:
            print('\nGAME OVER')
            sys.exit()
        else:
            print('\nOK')


def player2_move():
    if barr in player2_set:
        for o in player2_cart:
            try:
                o.insert(o.index(barr), '$')
                o.pop(o.index(barr))
            except ValueError:
                continue
        return 1


# game

for barr in barrel:
    barrel_in_game -= 1
    print('\nНовый боченок: {} (Осталось: {})\n'.format(barr, barrel_in_game))
    field(0)
    field(1)
    if player1_move() == 1:
        player1 -= 1
    if player2_move() == 1:
        player2 -= 1
    if player1 == 0:
        print('\nYou win!')
        sys.exit()
    if player2 == 0:
        print('\nYou lose!')
        sys.exit()
    if barrel_in_game == 0:
        print('\nGAME OVER')
        sys.exit()




