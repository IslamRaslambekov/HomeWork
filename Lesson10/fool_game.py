from random import shuffle


class Fool:
    deck = [('♠6', 6), ('♥6', 6), ('♣6', 6), ('♦6', 6),
            ('♠7', 7), ('♥7', 7), ('♣7', 7), ('♦7', 7),
            ('♠8', 8), ('♥8', 8), ('♣8', 8), ('♦8', 8),
            ('♠9', 9), ('♥9', 9), ('♣9', 9), ('♦9', 9),
            ('♠10', 10), ('♥10', 10), ('♣10', 10), ('♦10', 10),
            ('♠J', 11), ('♥J', 11), ('♣J', 11), ('♦J', 11),
            ('♠Q', 12), ('♥Q', 12), ('♣Q', 12), ('♦Q', 12),
            ('♠K', 13), ('♥K', 13), ('♣K', 13), ('♦K', 13),
            ('♠A', 14), ('♥A', 14), ('♣A', 14), ('♦A', 14)]  # Словарь в списке
    player_deck = []
    computer_deck = []

    def __init__(self):
        shuffle(self.deck)  # Перемешка колоды

        # self.on_hand()  # Раздача карт

    #############################
    def on_hand(self):
        """Функция раздает стартовый набор карт игроку и компьютеру"""
        for i in range(len(self.deck)):
            if i < 6:
                self.player_deck.append(self.deck.pop(0))  # Создаем стартовую колоду для игрока
                self.computer_deck.append(self.deck.pop(0))  # Создаем стартовую колоду для компьютера
            else:
                break  # Нужно раздать только 6 карт каждому, поэтому дальше цикл можно ломать

    #############################
    def add_cards(self, deck_name):
        """Функция добавляет карты в колоду, если длина колоды меньше 6"""
        while len(deck_name) < 6:
            deck_name.append(self.deck.pop(0))

        return deck_name  # Возвращает дополненную колоду

    #############################
    def game_result(self):
        """Функция определяет результат игры"""
        if len(self.player_deck) == 0:
            return 'Вы победили!!!'
        if len(self.computer_deck) == 0:
            return 'Вы проиграли.'

    #############################
    def cut_str(self, str_variable):
        # Проверяется длина строки
        # [('♣8', 8)] = 11 символов
        # [('♣K', 13)] = 12 символов
        # [('♠10', 10)] = 13 символов
        if len(str_variable) > 12:
            return str_variable[3:6]
        else:
            return str_variable[3:5]

    #############################
    def start_action(self):
        print(f'\nВаша колода:')

        [print(f'{i + 1} - \033[94m{self.player_deck[i][0]}\033[0m') for i in range(len(self.player_deck))]

        player_choice = int(input('Введите сответствующее картам число от 1 до 6: ')) - 1

        check_var = list()
        check_var.append(self.player_deck[player_choice])
        check_var = str(check_var)

        check_var = self.cut_str(check_var)
        print(f'\033[94m{check_var}\033[0m')

        for i in range(len(self.computer_deck)):
            temp_str = []
            temp_str.append(self.computer_deck[i])
            temp_str = str(temp_str)
            temp_str = self.cut_str(temp_str)
            if check_var[0:1] == temp_str[0:1]:
                if self.computer_deck[i][1] > self.player_deck[player_choice][1]:
                    print(f'\033[91m{self.computer_deck[i][0]}\033[0m\nКомпьютер отбил карту')
                    self.player_deck.pop(player_choice)
                    self.computer_deck.pop(i)
                    self.player_deck = self.add_cards(self.player_deck)
                    self.computer_deck = self.add_cards(self.computer_deck)
                    break
            if i == len(self.computer_deck) - 1:
                print('Компьютер берет карту')
                self.computer_deck.append(self.player_deck[player_choice])


if __name__ == '__main__':
    new_game = Fool()
    new_game.start_action()
