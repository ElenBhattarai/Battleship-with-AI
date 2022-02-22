from ship import Ship

class Player:
    def __init__(self, name):
        self.name = name #string for player's name
        self.my_board = [] # board to show player's full board
        self.enemy_board = [] #board to show player this player has marked on the other player's board
                              # all buttons in my_board array will be DISABLED so you can't click your own grid

        #Our 10x10 board will be represented by a 100-element array that will store 100 Buttons, one for each grid space 
        #Ex:
        # [a1][a2][a3]....[b10]
        # [b1][b2][b3]....[b10]
        # .
        # .
        # .
        # .
        # .
        # .
        # .
        # [j1][j2][j3]....[j10]


        self.ships = {} # dictionary (Python hashmap) of Ships for player

        '''Example of a ships dictionary at the start of a 5 ship game
        player1.ship_lives = {
            "A": {Ship(1)}, #ship with 1 life
            "B": {Ship(2)}, #ship with 2 lives
            "C": {Ship(3)}, #ship with 3 lives
            "D": {Ship(4)}, #ship with 4 lives
            "E": {Ship(5)}, #ship with 5 lives
        }
        '''

    def set_ships(self, num_ships): # properly sets up self.ships based on number of ships passed to the function
        for i in range(num_ships):
            self.ships.update({
                chr(i + 65): Ship(i + 1)
            })

    def to_string(self): 
        print("name: " + self.name)
        for k in self.ships.keys():
            self.ships[k].shipToString()
