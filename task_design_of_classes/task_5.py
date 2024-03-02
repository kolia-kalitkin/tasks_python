
# Класс HighScoreTable
#
# Предположим, что у нас имеется некоторая игра. За каждую игровую сессию игрок получает определенное количество баллов в зависимости от своего результата.
# Вашей задачей является реализация класса HighScoreTable — таблицы рекордов, которую можно будет обновлять с учетом итоговых результатов игрока.
# Изначально таблица рекордов является пустой. Максимальное количество рекордов указывается при создании таблицы:
# high_score_table = HighScoreTable(3)
# Таблица должна позволять просматривать текущие рекорды и добавлять новые результаты:

# print(high_score_table.scores)    # []
# high_score_table.update(10)
# high_score_table.update(8)
# high_score_table.update(12)
# print(high_score_table.scores)    # [12, 10, 8]

# Текущие рекорды всегда должны располагаться в порядке убывания. Так как таблица содержит именно рекорды, то после заполнения таблицы добавляться должны только те результаты, которые лучше текущих:

# high_score_table.update(6)
# high_score_table.update(7)
# print(high_score_table.scores)    # [12, 10, 8]
# high_score_table.update(9)
# print(high_score_table.scores)    # [12, 10, 9]

# Таблица должна поддерживать сброс всех результатов:

# high_score_table.reset()
# print(high_score_table.scores)    # []
# ---------------------------------------------------------------

class HighScoreTable:
    """
    класс HighScoreTable — таблицы рекордов, которую можно будет обновлять с учетом итоговых результатов игрока
    """

    def __init__(self, amount: int) -> None:
        self.scores = []
        self._amount = amount

    def update(self, result: int) -> None:
        """добавлять новые результаты"""
        self.scores.append(result)
        self.scores.sort(reverse=True)

        if (len(self.scores) > self._amount):
            self.scores.pop()

    def reset(self) -> None:
        """сброс всех результатов"""
        self.scores.clear()


# ----тесты------------
high_score_table = HighScoreTable(3)

print(high_score_table.scores)
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)

high_score_table.update(18)
high_score_table.update(11)
high_score_table.update(13)
print(high_score_table.scores)