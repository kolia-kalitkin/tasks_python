# Класс TicTacToe
#
# Реализуйте класс TicTacToe для игры в Крестики-Нолики. Экземпляр класса TicTacToe должен представлять собой игровое поле из трех строк и трех столбцов, на котором игроки по очереди могут помечать свободные клетки. Первый ход делает игрок, ставящий крестики:
# tictactoe = TicTacToe()

# tictactoe.mark(1, 1)         # помечаем крестиком клетку с координатами (1; 1)
# tictactoe.mark(3, 1)         # помечаем ноликом клетку с координатами (3; 1)

# Помечать уже помеченные клетки нельзя. При попытке сделать это должен быть выведен текст Недоступная клетка:
# tictactoe.mark(1, 1)         # Недоступная клетка
# tictactoe.mark(1, 3)         # помечаем крестиком клетку с координатами (1; 3)
# tictactoe.mark(1, 2)         # помечаем ноликом клетку с координатами (1; 2)
# tictactoe.mark(3, 3)         # помечаем крестиком клетку с координатами (3; 3)
# tictactoe.mark(2, 2)         # помечаем ноликом клетку с координатами (2; 2)
# tictactoe.mark(2, 3)         # помечаем крестиком клетку с координатами (2; 3)

# С помощью метода winner() должна быть возможность узнать победителя игры. Метод должен вернуть:

#     символ X, если победил игрок, ставящий крестики
#     символ O, если победил игрок, ставящий нолики
#     строку Ничья, если произошла ничья
#     значение None, если победитель еще не определен

# print(tictactoe.winner())    # X

# Помечать клетки после завершения игры нельзя. При попытке сделать это должен быть выведен текст Игра окончена:
# tictactoe.mark(2, 1)         # Игра окончена

# С помощью метода show() должна быть возможность посмотреть текущее состояние игрового поля. Оно должно быть построено из символов | и -, а также X и O, если игроками были сделаны какие-либо ходы. Для приведенного выше поля tictactoe вызов tictactoe.show() должен вывести следующее:

# X|O|X
# -----
#  |O|X
# -----
# O| |X
# ---------------------------------------------------

class TicTacToe:

    _X = 'X'
    _O = 'O'

    def __init__(self) -> None:
        self.field_game = [[' '] * 3 for _ in range(3)]

        self.flag1 = False
        self.flag2 = False
        self.count = 1
        self.winner1 = None

    
    def check_win(self, object):
        if isinstance(object, list):
            for col in range(3):
                string1 = ''.join(object[col])                

                if string1 == 'XXX':
                    self.flag1 = True
                    self.winner1 = self._X
                    return self._X

                elif string1 == 'OOO':
                    self.flag1 = True
                    self.winner1 = self._O
                    return self._O

        elif isinstance(object, str):
            if object == 'XXX':
                self.flag1 = True
                self.winner1 = self._X
                return self._X

            elif object == 'OOO':
                self.flag1 = True
                self.winner1 = self._O
                return self._O

        
    def winner(self) -> str:
        """узнаёт победителя игры""" 

        # ------------------------------------------------
        # смотрим есть ли победитель по горизонталям
        # ------------------------------------------------
        check_result = self.check_win(self.field_game)
        if check_result:
            return check_result

        # ------------------------------------------------
        # смотрим есть ли победитель по вертикалям
        # ------------------------------------------------
        lst1 = []
        lst2 = []
        for col in range(3):
            for row in range(3):
                lst1.append(self.field_game[row][col])
            lst2.append(lst1)
            lst1 = []

        check_result = self.check_win(lst2)
        
        if check_result:
            return check_result

        # ------------------------------------------------
        # смотрим есть ли победитель по главной диагонали
        # ------------------------------------------------
        lst3 = []
        for i in range(3):
            lst3.append(self.field_game[i][i])

        string1 = ''.join(lst3)
        
        check_result = self.check_win(string1)        
        if check_result:
            return check_result

        # ------------------------------------------------
        # смотрим есть ли победитель по побочной диагонали
        # ------------------------------------------------
        lst4 = []
        for i in range(3):
            lst4.append(self.field_game[i][3 - i - 1])

        string2 = ''.join(lst4)
        
        check_result = self.check_win(string2)
        if check_result:
            return check_result
        
        # ------------------------------------------------
        # смотрим есть ли НИЧЬЯ
        # ------------------------------------------------
        if self.count >= 9 and not self.winner1:
            self.flag2 = True                
            return 'Ничья'
        
                
        return None

    
    
    def mark(self, row: int, col: int) -> None:
        row -= 1
        col -= 1    # т.к. работаем с индексами от 0            
        

        if (self.count <= 9) and (self.flag1 == False): # если есть ходы и нет победителя
                              
            if self.field_game[row][col] == ' ':     # если клетка пустая
                if self.count % 2:                          # если нечетный ход - крестик, четный - нолик
                    self.field_game[row][col] = self._X
                else:
                    self.field_game[row][col] = self._O
                
                self.count += 1      # считаем ходы 
                
            else:
                print('Недоступная клетка')

        else:
            if self.flag2 or self.flag1: # если есть победитель или ничья
                print('Игра окончена')
            
                
        self.winner() 
    
    def show(self) -> None:
        """посмотреть текущее состояние игрового поля"""
        for i in range(3):
            print('|'.join(self.field_game[i]))
            if i != 2:
                print('-----')


# -------тесты --------------------------------------------
print('-------1-------')
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 1)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.mark(2, 1)
tictactoe.show()


print('-------2-------')
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()


print('-------3-------')
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)
tictactoe.mark(2, 2)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)


print('-------4-------')
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(1, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)

print(tictactoe.winner())

tictactoe.mark(3, 2)
tictactoe.mark(3, 3)
tictactoe.mark(1, 2)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)
print(tictactoe.winner())
