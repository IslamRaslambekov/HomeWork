from random import shuffle, choice, randint  # Подключил методы


class Fool:
    __deck = [('♠6', 6), ('♥6', 6), ('♣6', 6), ('♦6', 6),
              ('♠7', 7), ('♥7', 7), ('♣7', 7), ('♦7', 7),
              ('♠8', 8), ('♥8', 8), ('♣8', 8), ('♦8', 8),
              ('♠9', 9), ('♥9', 9), ('♣9', 9), ('♦9', 9),
              ('♠10', 10), ('♥10', 10), ('♣10', 10), ('♦10', 10),
              ('♠J', 11), ('♥J', 11), ('♣J', 11), ('♦J', 11),
              ('♠Q', 12), ('♥Q', 12), ('♣Q', 12), ('♦Q', 12),
              ('♠K', 13), ('♥K', 13), ('♣K', 13), ('♦K', 13),
              ('♠A', 14), ('♥A', 14), ('♣A', 14), ('♦A', 14)]  # Словарь в списке - dict in list
    __player_deck = []
    __ai_deck = []

    def __init__(self):
        shuffle(self.__deck)  # Перемешка колоды

        self.__on_hand()  # Раздача карт

    # ############################# Это трудно, поэтому на потом
    # def __select_trump(self):
    #     self.__trump = list(choice(self.__deck))[0]   # Выбирается козырь
    #     trump_dict = dict(self.__deck)
    #     temp_list = []
    #     for key in trump_dict:
    #         temp_list.append(key)
    #     for i in range(len(self.__deck)):
    #         if temp_list[i] == self.__trump[i]:   # Значения всех козырных карт увеличиваются на 10
    #             trump_dict

    #############################
    def __on_hand(self):
        """Функция раздает стартовый набор карт игроку и ИИ"""
        for i in range(len(self.__deck)):
            if i < 12:  # Пока i меньше 12
                if (i % 2) == 0:  #
                    self.__player_deck.append(self.__deck.pop(0))  # Создаем стартовую колоду для игрока
                else:
                    self.__ai_deck.append(self.__deck.pop(0))  # Создаем стартовую колоду для ИИ
            else:
                break  # Нужно раздать только 12 карт, поэтому дальше цикл можно ломать

    #############################
    def __add_cards(self, deck_name):
        """Функция добавляет карты в колоду, если длина колоды меньше 6"""
        while len(deck_name) < 6:
            deck_name.append(self.__deck.pop(0))

        return deck_name  # Возвращает дополненную колоду

    #############################
    def __game_result(self):
        """Функция определяет результат игры"""
        if len(self.__player_deck) == 0:
            return 'Вы победили!!!'
        if len(self.__ai_deck) == 0:
            return 'Вы проиграли.'

    #############################
    def start_action(self):
        while len(self.__deck) != 0:
            print('Ваша колода:')
            [print(f'\t{i + 1} - {self.__player_deck[i][0]}') for i in range(len(self.__player_deck))]  # Показ колоду
            print('\n')

            player_choice = int(input('Выберите карту: ')) - 1
            self.__player_deck.pop(player_choice)

        self.__game_result()   # Когда колода станет пустой вызовется эта функция


if __name__ == '__main__':
    new_game = Fool()
    new_game.start_action()
