class Ship:
    def __init__(self, lives):
        self.positions = [] #indices on board where the ship has been placed
        self.lives = lives #changes lives to value passed
    
    def to_string(self):
        print("positions: " + str(self.positions))
        print("lives: " + str(self.lives))
