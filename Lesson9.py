from random import shuffle, choice, randint  # Подключил методы


class Fool:
    __deck = ['6♠', '6♥', '6♣', '6♦', '7♠', '7♥', '7♣', '7♦',
              '8♠', '8♥', '8♣', '8♦', '9♠', '9♥', '9♣', '9♦',
              '10♠', '10♥', '10♣', '10♦', 'J♠', 'J♥', 'J♣', 'J♦',
              'Q♠', 'Q♥', 'Q♣', 'Q♦', 'K♠', 'K♥', 'K♣', 'K♦',
              'A♠', 'A♥', 'A♣', 'A♦']
    __player_deck = list()
    __ai_deck = list()
    __trump = ''

    def __init__(self):
        pass
        # shuffle(self.__deck)  # Перемешка колоды
        # self.__trump = choice(self.__deck)  # Выбор козыря

        # print(f'Козырь - {self.__trump}\n\n')
        # print(f'Колода, до выдачи карт - {self.__deck}\n\n')

        # self.on_hand()  # Раздача карт

        # print(f'Колода игрока - {self.__player_deck}\nКолода ИИ - {self.__ai_deck}\n\n')
        # print(f'Колода, после выдачи карт - {self.__deck}')

    #############################
    def on_hand(self):
        """Функция раздает стартовый набор карт игроку и ИИ"""

        for i in range(len(self.__deck)):
            if i < 12:
                if (i % 2) == 0:
                    self.__player_deck.append(self.__deck[i])  # Создаем стартовую колоду для игрока
                else:
                    self.__ai_deck.append(self.__deck[i])  # Создаем стартовую колоду для ИИ
            else:
                break

        self.__deck = self.__deck[12:]  # Перезапись колоды

    def add_card(self, deck_name):
        """Функция добавляет карты в колоду, если длина колоды меньше 6"""

        while len(deck_name) < 6:
            deck_name.append(self.__deck.pop(0))

        return deck_name  # Возвращает дополненную колоду

    #############################
    def first_move(self):
        """Функция выбирает за кем будет первый ход"""

        if randint(0, 1) == 1:
            return True
        else:
            return False

    def start_action(self):
        pass


if __name__ == '__main__':
    new_game = Fool()

    # Возможная реализицая метода start_action() если больше ничего не придумаю
    # some_list = ['6♠', '10♣', 'A♦', 'Q♥']
    # print(int(some_list[1][0:-1]) > int(some_list[0][0:-1]))  # Может ли бить одна карта другую
