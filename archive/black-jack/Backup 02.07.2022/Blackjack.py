from tkinter import *
from PIL import ImageTk, Image
from random import randint


class Bj():
    def __init__(self):
        # window
        self.main_window = Tk()
        self.main_window.title('Black Jack')
        self.main_window.geometry('1080x720')
        self.image_card = ImageTk.PhotoImage(Image.open(f'./Cards/3/14.png').resize((178, 266), Image.Resampling.LANCZOS))

        self.card_help_list = []
        self.cards = [
            [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
            [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
            [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
            [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
            [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
            [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
        ]
        self.player_value = [0, 0]
        self.dealer_value = [0, 0]
        #                   [value, number of Asses]

        # labels
        self.dealer_title_La = Label(self.main_window, text='Dealer')
        self.dealer_title_La.place(x='500', y='5')
        self.player_title_La = Label(self.main_window, text='Player')
        self.player_title_La.place(x='500', y='355')
        self.six_decks_La = Label(self.main_window, text='6 decks die ab start runtergespielt werden')
        self.six_decks_La.place(x='800', y='5')
        self.win_title_La = Label(self.main_window, text='')
        self.win_title_La.place(x='800', y='355')

        # cards
        self.player_first_card = Label(self.main_window)
        self.player_first_card.place(x='50', y='400')
        self.player_second_card = Label(self.main_window)
        self.player_second_card.place(x='250', y='400')
        self.player_3_card = Label(self.main_window)
        self.player_3_card.place(x='450', y='400')
        self.player_4_card = Label(self.main_window)
        self.player_4_card.place(x='650', y='400')
        self.player_5_card = Label(self.main_window)
        self.player_5_card.place(x='850', y='400')
        self.player_6_card = Label(self.main_window)
        self.player_6_card.place(x='1050', y='400')

        self.dealer_first_card = Label(self.main_window)
        self.dealer_first_card.place(x='50', y='50')
        self.dealer_second_card = Label(self.main_window)
        self.dealer_second_card.place(x='250', y='50')
        self.dealer_3_card = Label(self.main_window)
        self.dealer_3_card.place(x='450', y='50')
        self.dealer_4_card = Label(self.main_window)
        self.dealer_4_card.place(x='650', y='50')
        self.dealer_5_card = Label(self.main_window)
        self.dealer_5_card.place(x='850', y='50')
        self.dealer_6_card = Label(self.main_window)
        self.dealer_6_card.place(x='1050', y='50')

        # buttons
        self.next_game_btn = Button(self.main_window, text='next_game', command=self.next_game)
        self.next_game_btn.place(x='1', y='1')

        self.next_card_btn = Button(self.main_window, text='next card', command=self.player_next_card)
        self.next_card_btn.place(x='50', y='685')

        self.player_end_btn = Button(self.main_window, text='hold', command=self.dealer_end)
        self.player_end_btn.place(x='120', y='685')

        self.main_window.mainloop()

    def next_game(self):
        'start of game()'
        # player first card: choose, place open
        # dealer first card: choose, place open
        # player second card: choose, place open
        # dealer second card: choose, place closed
        # check if dealer 21 or player 21
        self.start_game()

        'player turn'
        # player has choice
        # check if player 21 or more; else has choice

        'dealer turn'
        # dealer take if < 17
        # check if dealer > 21

        'check win'
        # look who better
        # tell player

    def choose_card(self):
        self.random_card_num = randint(2, 14)
        self.random_card_num_for_list = self.random_card_num - 2
        self.random_color_num = randint(0, 3)
        for i in range(6):
            if self.cards[i][self.random_color_num][self.random_card_num_for_list] != 0:
                self.card_help_list.append(ImageTk.PhotoImage(Image.open(f'./Cards/{self.random_color_num}/{self.random_card_num}.png').resize((178, 266), Image.Resampling.LANCZOS)))
                self.value_clipboard = self.random_card_num
                self.cards[i][self.random_color_num][self.random_card_num_for_list] = 0
                break
        if self.cards[i][self.random_color_num][self.random_card_num_for_list] != 0:
            self.choose_card()


    def card_in_label(self, label):
        label.configure(image=self.card_help_list[-1], compound='top')

    def add_value(self, player1_or_dealer2, value):
        if value < 10 and value >= 0:
            if player1_or_dealer2 == 1:
                self.player_value[0] += value
            if player1_or_dealer2 == 2:
                self.dealer_value[0] += value
        if value >= 10 and value <= 13:
            if player1_or_dealer2 == 1:
                self.player_value[0] += 10
            if player1_or_dealer2 == 2:
                self.dealer_value[0] += 10
        if value == 14:
            if player1_or_dealer2 == 1:
                self.player_value[0] += 11
                self.player_value[1] += 1
            if player1_or_dealer2 == 2:
                self.dealer_value[0] += 11
                self.dealer_value[1] += 1

    def start_game(self):
        self.player_value = [0, 0]
        self.dealer_value = [0, 0]
        self.win_title_La.configure(text='')

        self.player_first_card.configure(image='', compound='top')
        self.player_second_card.configure(image='', compound='top')
        self.player_3_card.configure(image='', compound='top')
        self.player_4_card.configure(image='', compound='top')
        self.player_5_card.configure(image='', compound='top')
        self.player_6_card.configure(image='', compound='top')

        self.dealer_first_card.configure(image='', compound='top')
        self.dealer_second_card.configure(image='', compound='top')
        self.dealer_3_card.configure(image='', compound='top')
        self.dealer_4_card.configure(image='', compound='top')
        self.dealer_5_card.configure(image='', compound='top')
        self.dealer_6_card.configure(image='', compound='top')


        self.choose_card()
        self.card_in_label(self.player_first_card)
        self.add_value(1, self.value_clipboard)
        self.choose_card()
        self.card_in_label(self.dealer_first_card)
        self.add_value(2, self.value_clipboard)
        self.choose_card()
        self.card_in_label(self.player_second_card)
        self.add_value(1, self.value_clipboard)

        self.backside_card_num = randint(0, 3)
        self.card_help_list.append(ImageTk.PhotoImage(Image.open(f'./Cards/Back Covers/{self.backside_card_num}.png').resize((178, 266), Image.Resampling.LANCZOS)))
        self.card_in_label(self.dealer_second_card)
        self.choose_card()
        self.card_help_list.insert(0, self.card_help_list[-1])
        self.add_value(2, self.value_clipboard)

        if self.player_value[0] == 21 and self.dealer_value[0] != 21:
            self.player_won(1)
        elif self.player_value[0] == 21 and self.dealer_value[0] == 21:
            self.player_won(2)
            self.card_in_label(self.dealer_second_card)
        self.player_card_count_number = 2
        self.dealer_card_count_number = 2

        # '''self.card_help_list = [dealer 2, player 1, dealer 1, player 2, dealer deck card, dealer 2]
        #                               0          1        2           3       4               5
        #self.dealer_second_card.configure(image=self.card_help_list[0], compound='top')

    def player_next_card(self):
        self.choose_card()
        if self.player_card_count_number == 2:
            self.card_in_label(self.player_3_card)
        if self.player_card_count_number == 3:
            self.card_in_label(self.player_4_card)
        if self.player_card_count_number == 4:
            self.card_in_label(self.player_5_card)
        if self.player_card_count_number == 5:
            self.card_in_label(self.player_6_card)
        self.add_value(1, self.value_clipboard)
        self.player_card_count_number += 1
        self.check_asses()
        if self.player_value[0] > 21:
            self.player_won(6)

    def dealer_end(self):
        self.dealer_second_card.configure(image=self.card_help_list[0], compound='top')
        while True:
            self.check_asses()
            if self.dealer_value[0] < 17:
                self.choose_card()
                if self.dealer_card_count_number == 2:
                    self.card_in_label(self.dealer_3_card)
                if self.dealer_card_count_number == 3:
                    self.card_in_label(self.dealer_4_card)
                if self.dealer_card_count_number == 4:
                    self.card_in_label(self.dealer_5_card)
                if self.dealer_card_count_number == 5:
                    self.card_in_label(self.dealer_6_card)
                self.add_value(2, self.value_clipboard)
                self.dealer_card_count_number += 1
            else:
                self.check_win()
                break

    def check_asses(self):
        while self.player_value[1] > 0:
            if self.player_value[0] > 21 and self.player_value[1] > 0:
                self.player_value[0] -= 10
                self.player_value[1] -= 1
        while self.dealer_value[1] > 0:
            if self.dealer_value[0] > 21 and self.dealer_value[1] > 0:
                self.dealer_value[0] -= 10
                self.dealer_value[1] -= 1

    def check_win(self):
        if self.player_value[0] > self.dealer_value[0] and self.player_value[0] <= 21 and self.dealer_value[0] <= 21:
            self.player_won(3)
        if self.player_value[0] < self.dealer_value[0] and self.player_value[0] <= 21 and self.dealer_value[0] <= 21:
            self.player_won(4)
        if self.player_value[0] == self.dealer_value[0] and self.player_value[0] <= 21 and self.dealer_value[0] <= 21:
            self.player_won(5)
        if self.player_value[0] > 21:
            self.player_won(6)
        if self.player_value[0] <= 21 and self.dealer_value[0] > 21:
            self.player_won(7)

    def player_won(self, singleBj1_bothBj2_won3_loss4_same5_playerBust6_dealerBust7):
        if singleBj1_bothBj2_won3_loss4_same5_playerBust6_dealerBust7 == 1:
            self.win_title_La.configure(text='You have a Blackjack and won')
        if singleBj1_bothBj2_won3_loss4_same5_playerBust6_dealerBust7 == 2:
            self.win_title_La.configure(text='You and dealer have a Blackjack, no winner')
        if singleBj1_bothBj2_won3_loss4_same5_playerBust6_dealerBust7 == 3:
            self.win_title_La.configure(text='You win')
        if singleBj1_bothBj2_won3_loss4_same5_playerBust6_dealerBust7 == 4:
            self.win_title_La.configure(text='Dealer wins')
        if singleBj1_bothBj2_won3_loss4_same5_playerBust6_dealerBust7 == 5:
            self.win_title_La.configure(text='You and dealer win')
        if singleBj1_bothBj2_won3_loss4_same5_playerBust6_dealerBust7 == 6:
            self.win_title_La.configure(text='You are busted, you lose')
        if singleBj1_bothBj2_won3_loss4_same5_playerBust6_dealerBust7 == 7:
            self.win_title_La.configure(text='Dealer is busted, you win')





blackjack = Bj()