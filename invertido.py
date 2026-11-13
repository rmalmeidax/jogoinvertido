from tokenize import String


class Jogo:
    def __init__(self, player_01, player_02, word=""):
        self.player_01 = player_01
        self.player_02 = player_02
        self.word = word


    def players(self):
        self.word = input("Type the word to start the game: ")
        ##invert = word[::-1]
        qty_player = int(input("Enter the number of players: "))

        if qty_player == 2:
            print("Game Started!!!")
        else:
            print("Number of player invalid. The valid 02(two) players")

    def partida(self):

        while True:
            partida = input("Player 01 - Digit the word: ")
            if partida == self.word:
                print("Player 01 Wins!!!!!")
                break

            partida = input("Player 02 - Digit the word: ")
            if partida == self.word:
                print("Player 02 wins !!!!!")
                break

        print("No Winner")






pl01=Jogo("Player 01","Player 02","")



pl01.players()
pl01.partida()