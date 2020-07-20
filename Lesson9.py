from random import shuffle, choice      # Подключил методы


class Fool:
    deck = ['6♠', '6♥', '6♣', '6♦', '7♠', '7♥', '7♣', '7♦',
            '8♠', '8♥', '8♣', '8♦', '9♠', '9♥', '9♣', '9♦',
            '10♠', '10♥', '10♣', '10♦', 'J♠', 'J♥', 'J♣', 'J♦',
            'Q♠', 'Q♥', 'Q♣', 'Q♦', 'K♠', 'K♥', 'K♣', 'K♦',
            'A♠', 'A♥', 'A♣', 'A♦']
    player_deck = list()
    ai_deck = list()
    trump = ''

    def __init__(self):
        self.mix_deck()
        print(f'\nКолода, до выдачи карт - {self.deck}\n\n')
        self.select_trump()
        print(f'Козырь - {self.trump}\n\n')
        self.on_hand()
        print(f'Колода игрока - {self.player_deck}\nКолода ИИ - {self.ai_deck}\n\n')
        print(f'Колода, после выдачи карт - {self.deck}')

    def mix_deck(self):
        shuffle(self.deck)

    def select_trump(self):
        self.trump = choice(self.deck)

    def on_hand(self):
        """Функция раздает стартовый набор карт игроку и ИИ"""
        for i in range(len(self.deck)):
            if i < 12:
                if (i % 2) == 0:
                    self.player_deck.append(self.deck[i])  # Создаем стартовую колоду для игрока
                else:
                    self.ai_deck.append(self.deck[i])  # Создаем стартовую колоду для ИИ
            else:
                break
        self.deck = self.deck[12:]


if __name__ == '__main__':
    new_game = Fool()
