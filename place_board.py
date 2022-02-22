from tkinter import *

class PlaceBoard:
    def __init__(self):
        self.vertical_up      = False #check if the users second move was above the original index
        self.vertical_down    = False #check if the users second move was below the original index
        self.horizontal_right = False #check if the users second move was to the right the original index
        self.horizontal_left  = False #check if the users second move was to the left the original index
        self.left_left        = False #check if there are 2 letters to the left of the original index
        self.left_right       = False #check if there is 1 letter to the left of the original index and 1 letter to the right
        self.right_right      = False #check if there are 2 letters to the right of the original index
        self.right_left       = False #check if there is 1 letter to the left of the original index and 1 letter to the right 
        self.up_up            = False #check if there are 2 letters above the original index
        self.up_down          = False #check if there is 1 letter above the original index and 1 letter below
        self.down_down        = False #check if there are 2 letters below the original index
        self.down_up          = False #check if there is 1 letter above the original index and 1 letter below
        self.lll              = False #check if there are 3 letters to the left of the original index
        self.llr              = False #check if there are 2 letters to the left and 1 letter to the right
        self.rrr              = False #check if there are 3 letters to the right of the original index
        self.rrl              = False #check if there are 2 leters to the right and 1 letter to the left of the original index
        self.uuu              = False #check if there are 3 letters above the original index
        self.uud              = False #check if there are 2 letters above and 1 letter below the original index
        self.ddu              = False #check if there are 2 letters below and 1 leter above the original index
        self.ddd              = False #check if there are 3 letters below the original index

        self.text_variable = 'A'
        self.selected_ships = 0
        self.placing_ships = 0
        self.current_index = 0

        self.player_1_turn = True
        self.player_1_finalized = False
        self.player_2_finalized = False

    def __valid_move_2(self, i): #is the second letter being placed on a valid button in relation to the original index?
        if(i==self.current_index+1) and (i%10!=0): #if the second move is to the right of the original index and it is not wrapping around the sides of the board...
            self.horizontal_right = True #the players second move was to the right
            return(True)#this is a valid move

        if(i==self.current_index-1) and (i%10!=9): #if the second move is to the left of the original index and it is not wrapping around the sides of the board...
            self.horizontal_left = True #the players second move was to the left
            return(True)#this is a valid move

        if(i==self.current_index+10): #if the second move is below the original index...
            self.vertical_down = True #the players second move was down
            return(True)#this is a valid move

        if(i==self.current_index-10): #if the second move is above the original index...
            self.vertical_up = True #the players second move was up
            return(True)#this is a valid move

        else:
            return(False)#this is not a valid move

    def __valid_move_3(self, i): #is the third letter being placed on a valid button in relation to the original index and the second letter?
        if(self.horizontal_left): #if the players second move was to the left of the original index...
            if(i==self.current_index+1) and (i%10!=0): #if the third move is to the right of the original index and it is not wrapping around the sides of the board...
                self.left_right = True #the players third move is to the right of the original index 
                return(True) #this is a valid move
            if(i==self.current_index-2) and (i%10!=9): #if the third move is 2 to the left of the original index and it is not wrapping around the side of the board (or to the left of the second move)...
                self.left_left = True #the players third move is to the left of the second move
                return(True) #this is a valid move

        elif(self.horizontal_right): #if the players second move was to the right of the original index...
            if(i==self.current_index-1) and (i%10!=9):#if the third move is to the left of the original index and it is not wrapping around the sides of the board...
                self.right_left = True #the players third move is to the left of the original index
                return(True)#this is a valid move
            if(i==self.current_index+2) and (i%10!=0):#if the third move is 2 to the right of the original index and it is not wrapping around the sides of the board (or to the right of the second move)...
                self.right_right = True #the players third move is to the right of the second move
                return(True) #this is a valid move

        elif(self.vertical_down): #if the players second move was below the original index...
            if(i==self.current_index+20): #if the third move is 2 down from the original index (or below the second move)...
                self.down_down = True #the players third move is below the second move
                return(True) #this is a valid move
            if(i==self.current_index-10): #if the third move is above the original index
                self.down_up = True #the players third move is above the original index
                return(True) #this is a valid move

        elif(self.vertical_up): #if the players second move was above the original index...
            if(i==self.current_index-20): #if the third move is 2 above the original index (or 1 above the second move)
                self.up_up = True #the players third move is above the second move
                return(True) #this is a valid move
            if(i==self.current_index+10): #if the third move is below the original index
                self.up_down = True #the players third move is below the original index
                return(True) #this is a valid move

    def __valid_move_4(self, i): #is the fourth letter being placed on a valid button in relation to the original index, the second letter, and the third letter?
        if(self.left_left): #if the last two moves were to the left of the original index
            if(i==self.current_index+1) and (i%10!=0): #if the fourth move is to the right of the original index and it not wrapping around the sides of the board
                self.llr = True #the fourth move is to the right of the original index
                return(True) #this is a valid move
            if(i==self.current_index-3) and (i%10!=9): #if the fourth move is 3 to the left of the original index and is not wrapping around the sides of the board
                self.lll=True #the fourth move is to the left of the third move
                return(True) #this is a valid move
        elif(self.left_right or self.right_left): #if the last two moves were to the right and left of the original index
            if(i==self.current_index+2) and (i%10!=0): #if the fourth move is 2 to the right of the original index and is not wrapping around the sides of the board
                self.rrl = True #there are 2 letters to the right of the original index and 1 letter to the left of the original index
                return(True) #this is a valid move
            if(i==self.current_index-2) and (i%10!=9): #if the fourth move is 2 to the left of the original index and is not wrapping around the sides of the board
                self.llr = True #there are 2 letters to the left of the origianl index and 1 letter to the right of the origianl index
                return(True) #this is a valid move
        elif(self.right_right): #if the last two moves were to the right of the original index
            if(i==self.current_index-1) and (i%10!=9): #if the fourth move is to the left of the original index and is not wrapping around the sides of the board
                self.rrl = True #the fourth move is to the left of the original index
                return(True) #this is a valid move
            if(i==self.current_index+3) and (i%10!=0): #if the fourth move is to the right of the third move and is not wrappign around the sides of the board
                self.rrr = True #the fourth move is to the right of the third move
                return(True) #this is a valid move
        elif(self.up_up): #if the last two moves were above the original index
            if(i==self.current_index+10): #if the fourth move is below the original index
                self.uud = True #the fourth move is below the original index
                return(True) #this is a valid move
            if(i==self.current_index-30): #if the fourth move is above the third move
                self.uuu = True #the fourth move is above the third move
                return(True) #this is a valid move
        elif(self.up_down or self.down_up): #if the last two moves were above and below the original index
            if(i==self.current_index+20): #if the fourth move is 2 below the original index
                self.ddu = True #there are 2 letters below the original index and 1 letter above the original index
                return(True) #this is a valid move
            if(i==self.current_index-20): #if the fourth move is 2 above the original index
                self.uud = True #there are 2 letters above the original index and 1 letter below the original index
                return(True) #this is a valid move
        elif(self.down_down): #if the last two moves were below the original index
            if(i==self.current_index-10): #if the fourth move is above the original index
                self.ddu = True #the fourth move is above the original index 
                return(True) #this is a valid move
            if(i==self.current_index+30): #if the fourth move is below the third move
                self.ddd = True #the fourth move is below the third move
                return(True) #this is a valid move

    def __valid_move_5(self, i): #is the fifth letter being placed on a valid button in relation to the original index, the second letter, the third letter, and the fourth letter?
        if(self.llr): #if there are 2 letters to the left of the original index and 1 letter to the right of the original index
            if(i==self.current_index-3) and (i%10!=9): #if the fifth move is 3 to the left of the original index
                return(True) #this is a valid move
            if(i==self.current_index+2) and (i%10!=0): #if the fifth move is 2 to the right of the original index
                return(True) #this is a valid move
        elif(self.lll): #if there are 3 letters to the left of the original index
            if(i==self.current_index+1) and (i%10!=0): #if the fifth move is 1 to the right of the original index
                return(True) #this is a valid move
            if(i==self.current_index-4) and (i%10!=9): #if the fifth move is 4 to the left of the original index
                return(True) #this is a valid move
        elif(self.rrl): #if there are 2 letters to the right of the original index and 1 letter to the left of the original index
            if(i==self.current_index-2) and (i%10!=9): #if the fifth move is 2 to the left of the original index
                return(True) #this is a valid move
            if(i==self.current_index+3) and (i%10!=0): #if the fifth move is 3 to the right of the original index
                return(True) #this is a valid move
        elif(self.rrr): #if there are 3 letters to the right of the original index
            if(i==self.current_index-1) and (i%10!=9): #if the fifth move is 1 to the left of the original index
                return(True) #this is a valid move
            if(i==self.current_index+4) and (i%10!=0): #if the fifth move is 4 to the right of the original index
                return(True) #this is a valid move
        elif(self.uud): #if there are 2 letters above the original index and 1 letter below the original index
            if(i==self.current_index-30): #if the fifth move is 3 above the original index
                return(True) #this is a valid move
            if(i==self.current_index+20): #if the fifth move is 2 below the original index
                return(True) #this is a valid move
        elif(self.uuu): #if there are 3 letters above the original index
            if(i==self.current_index-40): #if the fifth move is 4 above the original index
                return(True) #this is a valid move
            if(i==self.current_index+10): #if the fifth move is 1 below the original index
                return(True) #this is a valid move
        elif(self.ddu): #if there are 2 letters below the original index and 1 letter above the original index
            if(i==self.current_index-20): #if the fifth move is 2 above the original index
                return(True) #this is a valid move
            if(i==self.current_index+30): #if the fifth move is 3 below the original index 
                return(True) #this is a valid move
        elif(self.ddd): #if there are 3 letters below the original index 
            if(i==self.current_index-10): #if the fifth move is 1 above the original index
                return(True) #this is a valid move
            if(i==self.current_index+40): #if the fifth move is 4 below the original index
                return(True) #this is a valid move

    def __reset_direction(self):#direction of vertical or horizontal and order of placement is reset once each ship has been finalized
        self.vertical_up = False
        self.vertical_down = False
        self.horizontal_right = False
        self.horizontal_left = False
        self.left_left = False
        self.left_right = False
        self.right_right = False
        self.right_left = False
        self.up_up = False
        self.up_down = False
        self.down_down = False
        self.down_up = False
        self.lll = False
        self.llr = False
        self.rrr = False
        self.rrl = False
        self.uuu = False
        self.uud = False
        self.ddu = False
        self.ddd = False
    
    def reset(self):#resets variables that handle the general board placement so player 2 sees fresh board when placing their battleships
        self.text_variable = 'A'
        self.selected_ships = 0
        self.placing_ships = 0
        self.current_index = 0

    def __enough_space(self, i, button_ids):#is there enough space on the board to fit the entire ship here? are the spaces to the left/right/up/down empty?
        if(self.placing_ships==3): #is there 3 spaces for C to go?
            if((i+10)<=99) and ((i+20)<=99):#check 2 spaces above index
                if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == ""):
                    return(True)
            if((i-10)>=0) and ((i-20)>=0):#check 2 spaces below index
                if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == ""):
                    return(True)
            if((i-10)>=0) and ((i+10)<=99):#check 1 space below and 1 space above index
                if(button_ids[i-10].cget('text') == "") and (button_ids[i+10].cget('text') == ""):
                    return(True)
            if((i+1)<=99) and ((i+2)<=99):#check 2 spaces to right of index
                if((i+1)%10!=0) and ((i+2)%10!=0):
                    if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == ""):
                        return(True)
            if((i-1)>=0) and ((i-2)>=0):#check 2 spaces to left of index
                if((i-1)%10!=9) and ((i-2)%10!=9):
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == ""):
                        return(True)
            if((i+1)<=99) and ((i-1)>=0):#check 1 space to the right of index and 1 space to the left of index
                if((i+1)%10!=0) and ((i-1)%10!=9):
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i+1].cget('text') == ""):
                        return(True)
            else:
                return(False)#this is not a valid move because the user won't be able to fit their entire ship in any orientation
        elif(self.placing_ships==6): #is there 4 spaces for D to go?
            if((i+10)<=99) and ((i+20)<=99) and ((i+30)<=99):#check 3 spaces above index
                if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == "") and (button_ids[i+30].cget('text') == ""):
                    return(True)
            if((i-10)>=0) and ((i-20)>=0) and ((i-30)>=0):#check 3 spaces below index
                if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i-30].cget('text') == ""):
                    return(True)
            if((i-10)>=0) and ((i+10)<=99) and ((i+20)<=99):#check 1 space below and 2 spaces above index
                if(button_ids[i-10].cget('text') == "") and (button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == ""):
                    return(True)
            if((i+1)<=99) and ((i+2)<=99) and ((i+3)<=99):#check 3 spaces to right of index
                if((i+1)%10!=0) and ((i+2)%10!=0) and ((i+3)%10!=0):
                    if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == "") and (button_ids[i+3].cget('text') == ""):
                        return(True)
            if((i-1)>=0) and ((i-2)>=0) and ((i-3)>=0):#check 3 spaces to left of index
                if((i-1)%10!=9) and ((i-2)%10!=9) and ((i-3)%10!=9):
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i-3].cget('text') == ""):
                        return(True)
            if((i-10)>=0) and ((i-20)>=0) and ((i+10)<=99):#check 1 space above and 2 spaces below index
                if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i+10].cget('text') == ""):
                    return(True)
            if((i+1)<=99) and ((i-1)>=0) and ((i-2)>=0):#check 1 space to the right of index and 2 spaces to the left of index
                if((i+1)%10!=0) and ((i-1)%10!=9) and ((i-2)%10!=9):
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i+1].cget('text') == ""):
                        return(True)
            if((i+1)<=99) and ((i+2)<=99) and ((i-1)>=0):#check 1 space to the left of index and 2 spaces to the right of index
                if((i+1)%10!=0) and ((i+2)%10!=0) and ((i-1)%10!=9):
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == ""):
                        return(True)
            else:
                return(False)#this is not a valid move because the user won't be able to fit their entire ship in any orientation
        elif(self.placing_ships==10): #is there 5 spaces for E to go?
            if((i+10)<=99) and ((i+20)<=99) and ((i+30)<=99) and ((i+40)<=99): #check 4 spaces above index
                if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == "") and (button_ids[i+30].cget('text') == "") and (button_ids[i+40].cget('text') == ""):
                    return(True)
            if((i-10)>=0) and ((i-20)>=0) and ((i-30)>=0) and ((i-40)>=0):#check 4 spaces below index
                if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i-30].cget('text') == "") and (button_ids[i-40].cget('text') == ""):
                    return(True)
            if((i+1)<=99) and ((i+2)<=99) and ((i+3)<=99) and ((i+4)<=99):#check 4 spaces to right of index
                if((i+1)%10!=0) and ((i+2)%10!=0) and ((i+3)%10!=0) and ((i+4)%10!=0):
                    if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == "") and (button_ids[i+3].cget('text') == "") and (button_ids[i+4].cget('text') == ""):
                        return(True)
            if((i-1)>=0) and ((i-2)>=0) and ((i-3)>=0) and ((i-4)>=0):#check 4 spaces to left of index
                if((i-1)%10!=9) and ((i-2)%10!=9) and ((i-3)%10!=9) and ((i-4)%10!=9):
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i-3].cget('text') == "") and (button_ids[i-4].cget('text') == ""):
                        return(True)
            if((i-10)>=0) and ((i+10)<=99) and ((i+20)<=99) and ((i+30)<=99):#check 1 space below and 3 spaces above index
                if(button_ids[i-10].cget('text') == "") and (button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == "") and (button_ids[i+30].cget('text') == ""):
                    return(True)
            if((i-10)>=0) and ((i-20)>=0) and ((i+10)<=99) and ((i+20)<=99):#check 2 spaces below and 2 spaces above index
                if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == ""):
                    return(True)
            if((i-10)>=0) and ((i-20)>=0) and ((i-30)>=0) and ((i+10)<=99):#check 1 space above and 3 spaces below index
                if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i-30].cget('text') == "") and (button_ids[i+10].cget('text') == ""):
                    return(True)
            if((i+1)<=99) and ((i+2)<=99) and ((i+3)<=99) and ((i-1)>=0):#check 1 space to the left of index and 3 spaces to the right of index
                if((i+1)%10!=0) and ((i+2)%10!=0) and ((i+3)%10!=0) and ((i-1)%10!=9):
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == "") and (button_ids[i+3].cget('text') == ""):
                        return(True)
            if((i+1)<=99) and ((i+2)<=99) and ((i-1)>=0) and ((i-2)>=0):#check 2 spaces to the left of index and 2 spaces to the right of index
                if((i+1)%10!=0) and ((i+2)%10!=0) and ((i-1)%10!=9) and ((i-2)%10!=9):
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == ""):
                        return(True)
            if((i+1)<=99) and ((i-1)>=0) and ((i-2)>=0) and ((i-3)>=0):#check 1 space to the right of index and 3 spaces to the left of index
                if((i+1)%10!=0) and ((i-1)%10!=9) and ((i-2)%10!=9) and ((i-3)%10!=9):
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i-3].cget('text') == "") and (button_ids[i+1].cget('text') == ""):
                        return(True)
            else:
                return(False) #this is not a valid move because the user won't be able to fit their entire ship in any orientation
        else:
            return(True)

    def __enough_space_2(self, i, button_ids):#is the user orientating their ship in the correct direction to fit the entire ship?
        if(self.placing_ships==4): #is the second C going to block the user from not being able to place the third C? 
            if(i==self.current_index+1): #if i is to the right of index...
                if((i+1)<=99) and ((i+1)%10!=0): #check that the next space to the right is empty
                    if(button_ids[i+1].cget('text') == ""):
                        return(True)
                if((self.current_index-1)>=0) and ((self.current_index-1)%10!=9): #check that the space to the left of the original is empty
                    if(button_ids[self.current_index-1].cget('text') == ""):
                        return(True)
            if(i==self.current_index-1): #if i is to the left of index...
                if((i-1)>=0) and ((i-1)%10!=9): #check that the next space to the left is empty
                    if(button_ids[i-1].cget('text') == ""):
                        return(True)
                if((self.current_index+1)<=99) and ((self.current_index+1)%10!=0): #check that the space to the right of the original is empty
                    if(button_ids[self.current_index+1].cget('text') == ""):
                        return(True)
            if(i==self.current_index+10): #if i is below the index...
                if((i+10)<=99): #check that the next space down is empty
                    if(button_ids[i+10].cget('text') == ""):
                        return(True)
                if((self.current_index-10)>=0): #check that the space above the original is empty
                    if(button_ids[self.current_index-10].cget('text') == ""):
                        return(True)
            if(i==self.current_index-10): #if i is above the index...
                if((i-10)>=0): #check that the next space up is empty
                    if(button_ids[i-10].cget('text') == ""):
                        return(True)
                if((self.current_index+10)<=99): #check that the space below the original is empty
                    if(button_ids[self.current_index+10].cget('text') == ""):
                        return(True)
            else:
                return(False) #this is not a valid move because the user won't be able to finish placing their ship
        elif(self.placing_ships==7): #is the second D going to block the user from not being able to place the third and fourth D?    
            if(i==self.current_index+1): #if i is to the right of index...
                if((i+1)<=99) and ((i+1)%10!=0) and ((i+2)<=99) and ((i+2)%10!=0): #check that the next 2 spaces to the right are empty
                    if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == ""):
                        return(True)
                if((self.current_index-1)>=0) and ((self.current_index-1)%10!=9) and ((self.current_index-2)>=0) and ((self.current_index-2)%10!=9): #check that 2 spaces to the left of the original index are empty
                    if(button_ids[self.current_index-1].cget('text') == "") and (button_ids[self.current_index-2].cget('text') == ""):
                        return(True)
                if((i+1)<=99) and ((i+1)%10!=0) and ((self.current_index-1)>=0) and ((self.current_index-1)%10!=9):#check that the next space to the right is empty and 1 space to the left of the original index is empty
                    if(button_ids[i+1].cget('text') == "") and (button_ids[self.current_index-1].cget('text') == ""):
                        return(True) 
            if(i==self.current_index-1): #if i is to the left of index...
                if((i-1)>=0) and ((i-1)%10!=9) and ((i-2)>=0) and ((i-2)%10!=9): #check that the next 2 spaces to the left are empty
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == ""):
                        return(True)
                if((self.current_index+1)<=99) and ((self.current_index+1)%10!=0) and ((self.current_index+2)<=99) and ((self.current_index+2)%10!=0): #check that 2 spaces to the right of the original index is empty
                    if(button_ids[self.current_index+1].cget('text') == "") and (button_ids[self.current_index+2].cget('text') == ""):
                        return(True)
                if((i-1)>=0) and ((i-1)%10!=9) and ((self.current_index+1)<=99) and ((self.current_index+1)%10!=0): #check that the next space to the left is empty and 1 space to the right of the original index is empty
                    if(button_ids[i-1].cget('text') == "") and (button_ids[self.current_index+1].cget('text') == ""):
                        return(True)
            if(i==self.current_index+10): #if i is below the index...
                if((i+10)<=99) and ((i+20)<=99): #check that the next 2 spaces down are empty
                    if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == ""):
                        return(True)
                if((self.current_index-10)>=0) and ((self.current_index-20)>=0): #check that 2 spaces above the original index is empty
                    if(button_ids[self.current_index-10].cget('text') == "") and (button_ids[self.current_index-20].cget('text') == ""):
                        return(True)
                if((i+10)<=99) and ((self.current_index-10)>=0): #check that the next space down is empty and 1 space above the original index is empty
                    if(button_ids[i+10].cget('text') == "") and (button_ids[self.current_index-10].cget('text') == ""):
                        return(True)
            if(i==self.current_index-10): #if i is above the index
                if((i-10)>=0) and ((i-20)>=0): #check that the next 2 spaces up are empty
                    if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == ""):
                        return(True)
                if((self.current_index+10)<=99) and ((self.current_index+20)<=99): #check that 2 spaces below the original index is empty
                    if(button_ids[self.current_index+10].cget('text') == "") and (button_ids[self.current_index+20].cget('text') == ""):
                        return(True)    
                if((i-10)>=0) and ((self.current_index+10)<=99): #check that the next space up is empty and 1 space below the original index is empty
                    if(button_ids[i-10].cget('text') == "") and (button_ids[self.current_index+10].cget('text') == ""):
                        return(True)
            else:
                return(False) #this is not a valid move because the user won't be able to finish placing their ship
        elif(self.placing_ships==11): #is the second E going to block the user from not being able to place the third, fourth, and fifth E?
            if(i==self.current_index+1): #if i is to the right of index...
                if((i+1)<=99) and ((i+1)%10!=0) and ((i+2)<=99) and ((i+2)%10!=0) and ((i+3)<=99) and ((i+3)%10!=0): #check that the next 3 spaces to the right are empty
                    if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == "") and (button_ids[i+3].cget('text') == ""):
                        return(True)
                if((self.current_index-1)>=0) and ((self.current_index-1)%10!=9) and ((self.current_index-2)>=0) and ((self.current_index-2)%10!=9) and ((self.current_index-3)>=0) and ((self.current_index-3)%10!=9): #check that 3 spaces to the left of the original index are empty
                    if(button_ids[self.current_index-1].cget('text') == "") and (button_ids[self.current_index-2].cget('text') == "") and (button_ids[self.current_index-3].cget('text') == ""):
                        return(True)
                if((i+1)<=99) and ((i+1)%10!=0) and ((i+2)<=99) and ((i+2)%10!=0) and ((self.current_index-1)>=0) and ((self.current_index-1)%10!=9):#check that the next 2 spaces to the right are empty and 1 space to the left of the original index is empty
                    if(button_ids[i+1].cget('text') == "") and (button_ids[i+2].cget('text') == "") and (button_ids[self.current_index-1].cget('text') == ""):
                        return(True) 
                if((i+1)<=99) and ((i+1)%10!=0) and ((self.current_index-1)>=0) and ((self.current_index-1)%10!=9) and ((self.current_index-2)>=0) and ((self.current_index-2)%10!=9): #check that the next space to the right is empty and 2 spaces to the left of the original index is empty
                    if(button_ids[i+1].cget('text') == "") and (button_ids[self.current_index-1].cget('text') == "") and (button_ids[self.current_index-2].cget('text') == ""):
                        return(True)
            if(i==self.current_index-1): #if i is to the left of index...
                if((i-1)>=0) and ((i-1)%10!=9) and ((i-2)>=0) and ((i-2)%10!=9) and ((i-3)>=0) and ((i-3)%10!=9): #check that the next 3 spaces to the left are empty
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[i-3].cget('text') == ""):
                        return(True)
                if((self.current_index+1)<=99) and ((self.current_index+2)<=99) and ((self.current_index+3)<=99) and ((self.current_index+1)%10!=0) and ((self.current_index+2)%10!=0) and ((self.current_index+3)%10!=0): #check that 3 spaces to the right of the original index are empty
                    if(button_ids[self.current_index+1].cget('text') == "") and (button_ids[self.current_index+2].cget('text') == "") and (button_ids[self.current_index+3].cget('text') == ""):
                        return(True)
                if((i-1)>=0) and ((i-1)%10!=9) and ((i-2)>=0) and ((i-2)%10!=9) and ((self.current_index+1)<=99) and ((self.current_index+1)%10!=0): #check that the next 2 spaces to the left are empty and 1 space to the right of the original index is empty
                    if(button_ids[i-1].cget('text') == "") and (button_ids[i-2].cget('text') == "") and (button_ids[self.current_index+1].cget('text') == ""):
                        return(True)
                if((i-1)>=0) and ((i-1)%10!=9) and ((self.current_index+1)<=99) and ((self.current_index+1)%10!=0) and ((self.current_index+2)<=99) and ((self.current_index+2)%10!=0): #check that the next space to the left is empty and 2 spaces to the right of the original index is empty
                    if(button_ids[i-1].cget('text') == "") and (button_ids[self.current_index+1].cget('text') == "") and (button_ids[self.current_index+2].cget('text') == ""):
                        return(True)
            if(i==self.current_index+10): #if i is below the index...
                if((i+10)<=99) and ((i+20)<=99) and ((i+30)<=99): #check that the next 3 spaces down are empty
                    if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == "") and (button_ids[i+30].cget('text') == ""):
                        return(True)
                if((self.current_index-10)>=0) and ((self.current_index-20)>=0) and ((self.current_index-30)>=0): #check that 3 spaces above the original index are empty
                    if(button_ids[self.current_index-10].cget('text') == "") and (button_ids[self.current_index-20].cget('text') == "") and (button_ids[self.current_index-30].cget('text') == ""):
                        return(True)
                if((i+10)<=99) and ((i+20)<=99) and ((self.current_index-10)>=0): #check that the next 2 spaces down are empty and 1 space above the original index is empty
                    if(button_ids[i+10].cget('text') == "") and (button_ids[i+20].cget('text') == "") and (button_ids[self.current_index-10].cget('text') == ""):
                        return(True)
                if((i+10)<=99) and ((self.current_index-10)>=0) and ((self.current_index-20)>=0): #check that the next space down is empty and 2 spaces above the original index is empty
                    if(button_ids[i+10].cget('text') == "") and (button_ids[self.current_index-10].cget('text') == "") and (button_ids[self.current_index-20].cget('text') == ""):
                        return(True)
            if(i==self.current_index-10): #if i is above the index...
                if((i-10)>=0) and ((i-20)>=0) and ((i-30)>=0): #check that the next 3 spaces up are empty
                    if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[i-30].cget('text') == ""):
                        return(True)
                if((self.current_index+10)<=99) and ((self.current_index+20)<=99) and ((self.current_index+30)<=99): #check that 3 spaces below the original index are empty
                    if(button_ids[self.current_index+10].cget('text') == "") and (button_ids[self.current_index+20].cget('text') == "") and (button_ids[self.current_index+30].cget('text') == ""):
                        return(True)    
                if((i-10)>=0) and ((i-20)>=0) and ((self.current_index+10)<=99): #check that the next 2 spaces up are empty and 1 space below the original index is empty
                    if(button_ids[i-10].cget('text') == "") and (button_ids[i-20].cget('text') == "") and (button_ids[self.current_index+10].cget('text') == ""):
                        return(True)
                if((i-10)>=0) and ((self.current_index+10)<=99) and ((self.current_index+20)<=99): #check that the next space up is empty and 2 spaces below the original index is empty
                    if(button_ids[i-10].cget('text') == "") and (button_ids[self.current_index+10].cget('text') == "") and (button_ids[self.current_index+20].cget('text') == ""):
                        return(True)
            else:
                return(False) #this is not a valid move because the user won't be able to finish placing their ship
        else:
            return(True)

    def __change(self, i, button_ids, enter_amount):#changes the button to a letter and the button ids are updated based on if the player 1 or player 2 buttons are being clicked
        print("in change")

        print(self.selected_ships)
        print(enter_amount)
        print(button_ids[i].cget('text'))

        if (self.selected_ships < enter_amount) and (button_ids[i].cget('text') == ""):#you are only allowed to change a button if you have not finished placing all your ships and if that button hasn't been clicked yet 
            print("in change 2")
            if(self.selected_ships==0): #if you haven't clicked the board yet, your first click will place ship A and placing_ships will be updated to keep track of what click the user is on in order to check for bad user input in the valid_move functions
                print("in change 3")
                self.text_variable = 'A'
                self.placing_ships += 1 
            elif(self.selected_ships>0 and self.selected_ships<=2):#if you have clicked the board once, the next two clicks will place ship B and placing_ships will be updated to keep track of what click the user is on in order to check for bad user input in the valid_move functions
                self.text_variable = 'B'
                self.placing_ships += 1
            elif(self.selected_ships>2 and self.selected_ships<=5):#if you have clicked the board three times, you are now placing ship C and placing_ships will be updated to keep track of what click the user is on in order to check for bad user input in the valid_move functions
                self.text_variable = 'C'
                self.placing_ships += 1
            elif(self.selected_ships>5 and self.selected_ships<=9):#if you have clicked the board five times, you are now placing ships D and placing_ships will be updated to keep track of what click the user is on in order to check for bad user input in the valid_move functions
                self.text_variable = 'D'
                self.placing_ships += 1
            else: #else you are placing ship E and placing_ships will be updated to keep track of what click the user is on in order to check for bad user input in the valid_move functions
                self.text_variable = 'E'
                self.placing_ships += 1
         
            bname = (button_ids[i])#store the current button id in bname
            bname.configure(text=self.text_variable)#update the current button to be a different text (either A,B,C,D,E)
            self.selected_ships = self.selected_ships + 1 #every time a button is actually changed to a letter, selected_ships is updated. Once selected_ships==enter_amount then the user can't keep placing more letters/ships

            if(self.selected_ships==enter_amount): #once the player has clicked the placing ships board the full number of times so that every ship is placed then the Finalize Ship Placement button appears
                if(self.player_1_turn):#have the button appear on player 1's screen if player 1's board was just finalized 
                    self.player_1_finalized = True
                    self.player_1_turn = False
                else:#have the button appear on player 2's screen if player 2's board was just finalized 
                    self.player_2_finalized = True

    def p1_is_finalized(self):
        return self.player_1_finalized

    def p2_is_finalized(self):
        return self.player_2_finalized

    def place_ship(self, i, button_ids, num_ships): #sends the index to be changed to change function after checking if the placement is valid
        print(self.placing_ships)
        #the amount of times the user will click the board when placing their ships
        enter_amount = 0 

        # num_ships is determined by the player, when choosing how many ships they want to play with
        match num_ships:
            case 1:               
                enter_amount = 1   #you will only be clicking the board once (A)
            case 2: 
                enter_amount = 3   #you will be clicking the board 3 times (ABB)
            case 3:
                enter_amount = 6   #you will be clicking the board 6 times (ABBCCC)
            case 4:
                enter_amount = 10  #you will be clicking the board 10 times (ABBCCCDDDD)
            case _:
                enter_amount = 15  #you will be clicking the board 15 times (ABBCCCDDDDEEEEE)

        if(self.placing_ships==0): #placing ship A
            self.__change(i, button_ids, enter_amount)#the button will be changed to A. (A can be placed anywhere on the board)

        elif(self.placing_ships==1 or self.placing_ships==3 or self.placing_ships==6 or self.placing_ships==10):#placing first letter of ship
            self.__reset_direction() #forget the previous orientations and reset for the next ship
            if(self.__enough_space(i, button_ids)):#before beginning to place a ship, it checks if there is even enough spaces on the board to fit the entire ship
                self.__change(i, button_ids, enter_amount)#the button will be changed. (The first letter placed of a ship can be placed anywhere on the board)
                self.current_index = i #the index of the first letter of a ship placement is stored

        elif(self.placing_ships==2 or self.placing_ships==4 or self.placing_ships==7 or self.placing_ships==11):#placing second letter of ship
            if(self.__enough_space_2(i, button_ids)):#there is clearly enough space on the board to fit the entire ship. This check makes sure the user starts clicking in the right direction that has enough spaces. 
                if(self.__valid_move_2(i)): #if the index of the second letter to be placed is above/below the original index or to the right/left of the original index then this is a valid move
                    self.__change(i, button_ids, enter_amount)#the button will be changed to the letter of the ship being placed

        elif(self.placing_ships==5 or self.placing_ships==8 or self.placing_ships == 12):#placing third letter of ship
            if(self.__valid_move_3(i)):#if the third index of the third letter to be placed is either above/below the other 2 letters or to the right/left of the other 2 letters then this is a valid move
                self.__change(i, button_ids, enter_amount)#the button will be changed to the letter of the ship being placed

        elif(self.placing_ships==9 or self.placing_ships==13):#placing fourth letter of ship
            if(self.__valid_move_4(i)):#if the fourth index of the fourth letter to be placed is either above/below the other 3 letters or to the right/left of the other 3 letters then this is a valid move
                self.__change(i, button_ids, enter_amount)#the button will be changed to the letter of the ship being placed

        elif(self.placing_ships==14):#placing fifth letter of ship (only applies to ship E)
            if(self.__valid_move_5(i)):#if the final E is either above/below the other E's or to the right/left of the other E's then this is a valid move
                self.__change(i, button_ids, enter_amount)#the button will be changed to E