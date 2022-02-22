from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial
from player import Player
from ship import Ship
from place_board import PlaceBoard
from itertools import product
from PIL import ImageTk, Image

num_ships = 0
player_1 = Player("Player 1") #initialize player_1
P1_ENEMY_CREATED = False
P2_ENEMY_CREATED = False
place_board = PlaceBoard() #initialize the board placement
visitedArray = []
p1_fired = False
player_2 = Player("Player 2") #initialize player_2


def set_images():
    image=Image.open("assets/miss.jpeg") #image for miss (bg for button will be set to white)
    img_w=image.resize((40,40))
    global img_miss
    img_miss=ImageTk.PhotoImage(img_w)

    image=Image.open("assets/hit.jpeg") #image for hit (bg for button will be set to red)
    img_r=image.resize((40,40))
    img_hit=ImageTk.PhotoImage(img_r)


def p1_place_ships(i,root):
    global num_ships
    global player_1

    place_board.place_ship(i, player_1.my_board, num_ships)

    if (place_board.p1_is_finalized()):
        frame4_button = Button(frame13, text="Finalize Ship\nPlacement", padx=20, pady=20, command = lambda: frame14_setup(root)).grid(row = 11, column = 22)#when Finalize Ship Placement is pressed then setup_frame5 function is called


def p2_place_ships(i):
    global num_ships
    global player_2
    # print(player_2.my_board)
    place_board.place_ship(i, player_2.my_board, num_ships)

    if (place_board.p2_is_finalized()):
        frame5_button = Button(frame5, text="Finalize Ship\nPlacement", padx=20, pady=20, command=partial(show_frame,frame6)).grid(row = 11, column = 22)#when Finalized Ship Placement is pressed then frame6 displays on the screen



#Attack_Method
def attack(i, type): #playerId = "p1" or "p2"

    print("Attack" + str(i))
    global player_1
    global player_2


    global p1_fired
    global p2_fired
    global img_missq
    global img_hit
    if(type == "p1"): #miss
        p2_fired = False
        if not p1_fired:
            btn_text = player_2.my_board[i].cget("text")
            print(btn_text)
            if(btn_text == ""): #miss!
                player_1.enemy_board[i].configure(bg="white", image=img_miss, compound=CENTER, state ='disabled') #miss 
                player_2.my_board[i].configure(bg="white", image=img_miss, compound=CENTER, state ='disabled')
                #show_done_button("p1")
            else: #hit! there is a ship at i
                print(btn_text)
                player_2.ships[btn_text].lives = int(player_2.ships[btn_text].lives) - 1 #update lives for hit ship

                if(player_2.ships[btn_text].lives == 0):
                    ship_positions = player_2.ships[btn_text].positions #puts the indices of the ship in an array
                    for i in ship_positions:
                        player_1.enemy_board[i].configure(bg="black", image=img_sunk, compound=CENTER, fg = "white", state ='disabled')
                        player_2.my_board[i].configure(bg="black", image=img_sunk, compound=CENTER, fg = "white", state ='disabled')   
                     #notify the player with a label
                    s = player_2.name + " Ship " + btn_text + ": SUNK!!"
                    pop_up_label = Label(frame7, text=s,font=("Arial", 25))
                    pop_up_label.place(relx=.5, rely=.2,anchor= CENTER)
                    pop_up_label.after(2000, pop_up_label.destroy)
                else:
                    player_1.enemy_board[i].configure(bg="red", image=img_hit, compound=CENTER, fg = "white", state ='disabled')
                    player_2.my_board[i].configure(bg="red", image=img_hit, compound=CENTER, fg = "white", state ='disabled')
                show_done_button("p1")
            p1_fired = True
        #show_frame(frame7)
    elif(type == "p2"):
        p1_fired = False
        if not p2_fired:
            btn_text = player_1.my_board[i].cget("text")
            if(player_1.my_board[i].cget("text") == ""): #miss
                player_2.enemy_board[i].configure(bg="white", image=img_miss, compound=CENTER, state ='disabled') #miss
                player_1.my_board[i].configure(bg="white", image=img_miss, compound=CENTER, state ='disabled')
                show_done_button("p2")
            else: #hit! there is a ship at i
                player_1.ships[btn_text].lives = int(player_1.ships[btn_text].lives) - 1 #update lives for hit ship
               
                if(player_1.ships[btn_text].lives == 0):
                    ship_positions = player_1.ships[btn_text].positions #puts the indices of the ship in an arry
                    for i in ship_positions:
                        player_2.enemy_board[i].configure(bg="black", image=img_sunk, compound=CENTER, state ='disabled')
                        player_1.my_board[i].configure(bg="black", image=img_sunk, compound=CENTER, state ='disabled')
                    #notify the player with a label
                    s = player_1.name + " Ship " + btn_text + ": SUNK!!"
                    pop_up_label = Label(frame9, text=s,font=("Arial", 25))
                    pop_up_label.place(relx=.5, rely=.2,anchor= CENTER)
                    pop_up_label.after(4000, pop_up_label.destroy)
                else:
                    player_2.enemy_board[i].configure(bg="red", image=img_hit, compound=CENTER, state ='disabled')   
                    player_1.my_board[i].configure(bg = "red", image=img_hit, compound=CENTER, state ='disabled')
                show_done_button("p2")
            p2_fired = True
        #show_frame(frame9)


def draw_boards(type, size, offset_r, offset_c):
    print("test DRAWBOARDS")
    global player_1
    global player_2
    if type == "p1":
        print("HERE P1")
    
        #draw player board, creates a 10 x 10 canvas for the buttons to be placed in
        for i in range(10):
            # shape the grid
            setsize2 = Canvas(frame15, width=size, height=0).grid(row=11, column=i)
            setsize2 = Canvas(frame15, width=0, height=size).grid(row=i, column=11)

        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            #copy important attributes of current button
            img= player_1.my_board[i].cget("image")
            txt = player_1.my_board[i].cget("text")
            b = player_1.my_board[i].cget("bg")

            temp = player_1.my_board[i]
            button = Button(master=frame15, image=img, text=txt, compound=CENTER, bg=b) #make a copy
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player_1.my_board[i] = button #replace button with copied button
            temp.destroy() #destroy old button

       
        #draw enemy board
        for i in range(10):
            # shape the grid, creates a 10 x 10 canvas for buttons to be placed in
            setsize1 = Canvas(frame15, width=size, height=0).grid(row=11, column=i+offset_c)
            setsize1 = Canvas(frame15, width=0, height=size).grid(row=i, column=11+offset_c)
        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            button = player_1.enemy_board[i]
            button.grid(row=item[0], column=item[1]+offset_c, sticky="n,e,s,w")

    else: #type = "p2"
        #detach buttons from frame5 canvas

        #draw player board  
        for i in range(10):
            # shape the grid, creates a 10 x 10 canvas for buttons to be placed in
            setsize2 = Canvas(frame9, width=size, height=0).grid(row=11, column=i)
            setsize2 = Canvas(frame9, width=0, height=size).grid(row=i, column=11)

        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            #copy important attributes of current button
            img= player_2.my_board[i].cget("image")
            txt = player_2.my_board[i].cget("text")
            b = player_2.my_board[i].cget("bg")
    
            temp = player_2.my_board[i]
            button = Button(master=frame9, image=img, text=txt, compound=CENTER, bg=b) #make a copy
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player_2.my_board[i] = button #replace button with copied button
            temp.destroy()
       
        #draw enemy board
        for i in range(10):
            # shape the grid, creates a 10 x 10 canvas for buttons to be placed in
            setsize1 = Canvas(frame9, width=size, height=0).grid(row=11, column=i+offset_c)
            setsize1 = Canvas(frame9, width=0, height=size).grid(row=i, column=11+offset_c)
        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            button = player_2.enemy_board[i]
            button.grid(row=item[0], column=item[1]+offset_c, sticky="n,e,s,w")


def assign_positions(type): 
    #type = "p1" or "p2"
    #iterate through whole array
    #if the button text doesn't = blank, add it to the positions
    global player_1 
    global player_2
    if type == "p1":
        for i in range(len(player_1.my_board)): #iterate through the player's board
            btn_text = player_1.my_board[i].cget("text")
            if btn_text != "": #will either be "A", "B", "C", "D", or "E"
                print("i and button text: " + str(i) + " " + btn_text)
                player_1.ships[btn_text].positions.append(i) #add this index to the position of the corresponding ship
                print("Found one")
    elif type == "p2":
        p2_place_ships(39)
        p2_place_ships(40)
        p2_place_ships(41)


        for i in range(len(player_2.my_board)): #iterate through the player's board
            btn_text = player_2.my_board[i].cget("text")
            if btn_text != "": #will either be "A", "B", "C", "D", or "E"
                print("i and button text: " + str(i) + " " + btn_text)
                player_2.ships[btn_text].positions.append(i) #add this index to the position of the corresponding ship

def board(type, size, root): #size = width and length of the canvas
    global player_1 
    global player_2
    global P1_ENEMY_CREATED
    global P2_ENEMY_CREATED
    print(P1_ENEMY_CREATED)
    print(P2_ENEMY_CREATED)
    print(size)
    if type == 'p1_set': #it is player 1's turn and they are placing their ships
        pos = product(range(10), range(10))
        
        #initialize player 1's board
        for i in range(10):
            #shape the grid
            setsize = Canvas(frame13, width=size, height=0).grid(row=11, column=i)
            setsize = Canvas(frame13, width=0, height=size).grid(row=i, column=11)
        for i, item in enumerate(pos):
            button = Button(frame13, command=partial(p1_place_ships, i, root))
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player_1.my_board.append(button)
    if type == 'p1_attack': #it is player 1's turn and they are attacking 
        global frame15
        frame15 = Frame(root)
        frame15.grid(row=0, column=0, sticky = 'nsew')
        if not P1_ENEMY_CREATED:
            assign_positions("p2") # assign positions indices for player 2's own ships, so that p1 may attack them
            pos = product(range(10), range(10))
            #create
            for i in range(10):
                # shape the grid
                setsize = Canvas(frame15, width=size, height=0).grid(row=11, column=i)
                setsize = Canvas(frame15, width=0, height=size).grid(row=i, column=11)
            for i, item in enumerate(pos):
                button = Button(frame15, text="", command=partial(attack, i, "p1"))
                button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
                player_1.enemy_board.append(button)
            P1_ENEMY_CREATED = True   

        #draw the frame7 screen
        draw_boards("p1", size, offset_r=0, offset_c=14) #offset between boards
        show_frame(frame15) #shows frame 7

    if type == 'p2_set': #it is player 1's turn and they are placing their ships
        pos = product(range(10), range(10))

        global frame17
        frame17 = Frame(root)

        for i in range(10):
            # shape the grid, creates a 10 x 10 canvas for buttons to be placed in
            setsize = Canvas(frame17, width=size, height=0).grid(row=11, column=i)
            setsize = Canvas(frame17, width=0, height=size).grid(row=i, column=11)
        
        for i, item in enumerate(pos):
            button = Button(frame17, command=partial(p2_place_ships, i=i))
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player_2.my_board.append(button)

       


    """if type == 'p2_attack': #it is player 2's turn and they are attacking 
        if not P2_ENEMY_CREATED:
            assign_positions("p1") # set positions indices for player 1's own ships, so that p2 may attack them
            pos = product(range(10), range(10))
            #create
            for i in range(10):
                # shape the grid, creates a 10 x 10 canvas for buttons to be placed in
                setsize = Canvas(frame9, width=size, height=0).grid(row=11, column=i)
                setsize = Canvas(frame9, width=0, height=size).grid(row=i, column=11)

            for i, item in enumerate(pos):
                button = Button(frame9, text="", command=partial(attack, i, "p2"))
                button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
                player_2.enemy_board.append(button)
            #print(player_2.enemy_board)
            P2_ENEMY_CREATED = True  
            frame5.forget()

        #draw the frame9 screen
        draw_boards("p2", size, offset_r=0, offset_c=14) #offset between boards
        show_frame(frame9) #shows frame 9"""



def choose_ship_number_AI(root):
    global frame13
    global num_ships
    x = num_ships

    #Frame 4 code   
    #label created inside set_player_names function
    board('p1_set', 40, root)

    #frame 5 code
    #label created inside set_player_names function
    board('p2_set', 40, root)


    if x >= 1: 
        ship1 = Button(frame13, text="A", padx=20, pady=10, fg='red').grid(row = 3, column = 22) #sets a ship button for ship 1 on frame 4
        if x >= 2:
            ship2 = Button(frame13, text="BB", padx=40, pady=10, fg='blue').grid(row = 4, column = 22) #sets a ship button for ship 2 on frame 4
            if x >= 3:
                ship3 = Button(frame13, text="CCC", padx=60, pady=10, fg='orange').grid(row = 5, column = 22) #sets a ship button for ship 3 on frame 4
                if x >= 4:
                    ship4 = Button(frame13, text="DDDD", padx=80, pady=10, fg='green').grid(row = 6, column = 22) #sets a ship button for ship 4 on frame 4
                    if x >= 5:
                        ship5 = Button(frame13, text="EEEEE", padx=100, pady=10, fg='purple').grid(row = 7, column = 22) #sets a ship button for ship 5 on frame 4

def ship_count_AI(x, root):
    global frame13
    global num_ships
    global player_1
    global player_2
    num_ships = x
    num = str(x) # get the number as a string
    mylabel = Label(frame13, text="Place your ships (" + num + ")").grid(row=1, column=22) #label for p1 on frame4
    choose_ship_number_AI(root)

    #instantiate players' ships
    player_1.set_ships(num_ships)
    player_2.set_ships(num_ships)

    show_frame(frame13)


def show_frame(frame): #raises a frame when called
    frame.tkraise()

def sframe13(y,root):
    frame13_setup(root)
    ship_count_AI(y, root)

def frame12_setup(root):
    frame12 = Frame(root)
    frame12.grid(row=0, column=0, sticky = 'nsew')

    myButton1 = Button(frame12, text="1 ship  ",font=("Arial",20, BOLD), padx=25, pady=25, command=lambda: sframe13(1,root)).place(relx=.5,rely=.3,anchor= CENTER) #button to select 1 ship, calls setup_frame3
    myButton2 = Button(frame12, text="2 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=lambda: sframe13(2,root)).place(relx=.5,rely=.4,anchor= CENTER) #button to select 2 ships, calls setup_frame3
    myButton3 = Button(frame12, text="3 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=lambda: sframe13(3,root)).place(relx=.5,rely=.5,anchor= CENTER) #button to select 3 ships, calls setup_frame3
    myButton4 = Button(frame12, text="4 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=lambda: sframe13(4,root)).place(relx=.5,rely=.6,anchor= CENTER) #button to select 4 ships, calls setup_frame3
    myButton5 = Button(frame12, text="5 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=lambda: sframe13(5,root)).place(relx=.5,rely=.7,anchor= CENTER) #button to select 5 ships, calls setup_frame3
    
    print("Hey")
    show_frame(frame12)

def frame13_setup(root):
    global frame13
    frame13 = Frame(root)
    frame13.grid(row=0, column=0, sticky = 'nsew')

def frame14_setup(root):
    global frame14
    frame14 = Frame(root)
    frame14.grid(row=0, column=0, sticky = 'nsew')

    choose_diff = Label(frame14, text = "Choose the level of difficulty to play with AI").pack()
    easy = Button(frame14, text = "Easy", command=partial(board, "p1_attack", 40,root)).pack()
    medium = Button(frame14, text = "Medium",command=partial(board, "p1_attack", 40,root)).pack()
    hard = Button(frame14, text = "Hard",command=partial(board, "p1_attack", 40,root)).pack()
    show_frame(frame14)

def executiveAI(root):
    frame12_setup(root)
    set_images()
 
def hit(hit_index):
    print(hit_index)

def startGame(root, visitedArray, mode):
    size = 40

    
   






    


