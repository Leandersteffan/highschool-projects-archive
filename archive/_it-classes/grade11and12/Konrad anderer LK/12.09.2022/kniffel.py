from random import randint
from time import sleep


class Kniffel:
    def __init__(self):
        self.players = []

        self.dices = []
        for _ in range(5):
            self.dices.append(Dice())

    def game(self):
        self.start_animation()

        self.names_cui()

        for _ in range(6):
            self.round_cui()

        self.end_cui()

    def start_animation(self):
        for i in reversed(range(0, 20)):
            self.print_break()
            print("""
  _  __      _  __  __     _
 | |/ /     (_)/ _|/ _|   | |
 | ' / _ __  _| |_| |_ ___| |
 |  < | '_ \| |  _|  _/ _ \ |
 | . \| | | | | | | ||  __/ |
 |_|\_\_| |_|_|_| |_| \___|_|
            """)
            print("\n" * i)
            sleep(0.1)

    def names_cui(self):
        print("Spieler: ")
        for player in self.players:
            print(f"- {player.name}")
        print("")
        answer = input("Name oder Fertig (f)? > ").strip()

        if answer == "f":
            return

        self.players.append(Player(answer))

        self.names_cui()
        self.print_break()

    def end_cui(self):
        for player in self.players:
            print("")
            print(f"Spieler: {player.name}")
            self.print_block(player.block)

        self.sleep_cui()

        maximum = 0
        name = ""
        for player in self.players:
            points = player.calculate_points()
            if points > maximum:
                name = player.name
                maximum = points

        print(f"Gewonnen hat {name} mit {maximum} Punkten")

    def round_cui(self):
        for player in self.players:
            self.unlock_dices()

            # Begrüßung
            self.print_break()
            print(f"Am Zug ist: {player.name}")
            print("")
            self.print_block(player.block)
            self.sleep_cui()

            # Spieler würfelt die Würfel
            self.roll_dices()
            self.roll_cui(0)

            # Spieler kann auswählen
            player.block = self.choose_cui(player.block)

    def choose_cui(self, block):
        self.print_dices()
        self.sleep_cui()
        self.print_block(block)

        answer = int(self.improved_input("Wo eintragen (1, 2, 3, 4, 5, 6)? > ", ["1", "2", "3", "4", "5", "6"]))
        # Verhindert das belgegen von schon beschriebenen Feldern
        if block[answer - 1] != 0:
            block[answer - 1] = -1
        else:
            block[answer - 1] = self.count_eyes(answer)

        self.print_break()
        self.print_block(block)
        self.sleep_cui()

        return block

    def roll_cui(self, count):
        self.print_dices()

        answer = self.improved_input("Nochmal würfeln (n), Würfel sperren (s) oder Fertig (f)? > ", ["n", "s", "f"])

        match answer:
            case "n":
                self.roll_dices()
                count += 1
            case "f":
                return
            case "s":
                self.lock_dice_cui()

        if count < 2:   # Es kann nur noch 2x zusätzlich gewüfelt werden. Also insgesammt 3x
            self.roll_cui(count)

    def sleep_cui(self):
        print("")
        input("Weiter mit ENTER")
        print("")

    def lock_dice_cui(self):
        self.print_dices()

        answer = self.improved_input("Würfel sperren (1-5) oder Fertig (f)? > ", ["1", "2", "3", "4", "5", "f"])

        if answer == "f":
            return

        answer = int(answer)
        answer -= 1
        self.dices[answer].locked = not self.dices[answer].locked

        self.lock_dice_cui()

    def improved_input(self, entry, answers):
        answer = ""
        while answer not in answers:
            answer = input(entry).lower().strip()

        return answer

    def count_dices(self, number):
        count = 0
        for dice in self.dices:
            if dice.eyes == number:
                count += 1

        return count

    def count_eyes(self, number):
        total = 0
        for dice in self.dices:
            if dice.eyes == number:
                total += dice.eyes

        return total

    def unlock_dices(self):
        for dice in self.dices:
            dice.locked = False

    def roll_dices(self):
        for dice in self.dices:
            if not dice.locked:
                dice.roll()

    def print_dices(self):
        self.print_break()

        for dice in self.dices:
            if dice.locked:
                print(f"{dice.eyes}*")
            else:
                print(dice.eyes)

    def print_block(self, block):
        print("Dein Block:")
        print(f"Einser:  {block[0]}")
        print(f"Zweier:  {block[1]}")
        print(f"Dreier:  {block[2]}")
        print(f"Vierer:  {block[3]}")
        print(f"Fünwer:  {block[4]}")
        print(f"Sechser: {block[5]}")

    def print_break(self):
        print("\n" * 16)


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.block = [0] * 13

    def calculate_points(self):
        # Setzt gestrichene Einträge zurück auf 0, damit keine Punkte abgezogen werden
        for entry in self.block:
            if entry == -1:
                entry = 0

        points = sum(self.block)
        return points


class Dice:
    def __init__(self):
        self.eyes = 1
        self.locked = False

    def roll(self):
        self.eyes = randint(1, 6)
        return self.eyes


kniffel = Kniffel()
kniffel.game()
