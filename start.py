from tkinter import *
from tkinter.font import BOLD, Font
from functools import partial
from itertools import product
from player import Player
from ship import Ship
from place_board import PlaceBoard
from PIL import ImageTk, Image

def show_frame(frame): #raises a frame when called
    frame.tkraise()

### Global Variables
num_ships = 0
player_1 = Player("Player 1") #initialize player_1
player_2 = Player("Player 2") #initialize player_2
place_board = PlaceBoard() #initialize the board placement

P1_ENEMY_CREATED = False
P2_ENEMY_CREATED = False

p1_fired = False
p2_fired = False
###

root = Tk()
root.state('zoomed') #puts the window mode in zoomed
root.title("Battleship") #labels our frame

### Images Used
image=Image.open("assets/sunk.jpeg") #image for sunk (bg for button will be set to black)
img_s=image.resize((40,40))
img_sunk=ImageTk.PhotoImage(img_s)

image=Image.open("assets/hit.jpeg") #image for hit (bg for button will be set to red)
img_r=image.resize((40,40))
img_hit=ImageTk.PhotoImage(img_r)

image=Image.open("assets/miss.jpeg") #image for miss (bg for button will be set to white)
img_w=image.resize((40,40))
img_miss=ImageTk.PhotoImage(img_w)

image=Image.open("assets/start.jpeg") 
#img_w=image.resize((40,40))
img_start=ImageTk.PhotoImage(image) #image for just the start button (bg set to blue)
###

root.rowconfigure(0, weight=1) #configures rows to a weight of 1
root.columnconfigure(0, weight=1) #configures columns to weight of 1

#creates frames 1 - 10
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
frame6 = Frame(root)
frame7 = Frame(root)
frame8 = Frame(root)
frame9 = Frame(root)
frame10 = Frame(root)
for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10):
    frame.grid(row=0, column=0, sticky = 'nsew') #frame 1 - 10 rows and columns initiliazed to 0 and widgest are sticky.

show_frame(frame1)
#Frame code below functions

def set_player_names(): #sets player names, then makes a label with the corresponding player name for frames 4 and 5 respectively
    global player_1
    global player_2
    print(e.get())
    print(b.get())
    player_1.name = e.get() #gets player 1 name
    player_2.name = b.get() #gets player 2 name

    show_frame(frame4) # shows frame 4, when frame 3's button gets clicked. 

    #set up frame 4 label
    p1_label = "Player 1 (" + player_1.name + ")"
    frame4_label = Label(frame4, text=p1_label).grid(row=2, column=22)

    #set up frame 5 label
    p2_label = "Player 2 (" + player_2.name + ")"
    frame4_label = Label(frame5, text=p2_label).grid(row=2, column=22) 

def ship_count(x):
    global num_ships
    global player_1
    global player_2
    num_ships = x
    num = str(x) # get the number as a string
    mylabel = Label(frame4, text="Place your ships (" + num + ")").grid(row=1, column=22) #label for p1 on frame4
    mylabel = Label(frame5, text="Place your ships (" + num + ")").grid(row=1, column=22) #label for p2 on frame5
    choose_ship_number()

    #instantiate players' ships
    player_1.set_ships(num_ships)
    player_2.set_ships(num_ships)

    show_frame(frame4)

def choose_ship_number():
    global num_ships
    x = num_ships

    #Frame 4 code   
    #label created inside set_player_names function
    board('p1_set', 40)

    #frame 5 code
    #label created inside set_player_names function
    board('p2_set', 40)


    if x >= 1: 
        ship1 = Button(frame4, text="A", padx=20, pady=10, fg='red').grid(row = 3, column = 22) #sets a ship button for ship 1 on frame 4
        ship1 = Button(frame5, text="A", padx=20, pady=10, fg='red').grid(row = 3, column = 22) #sets a ship button for ship 1 on frame 5
        if x >= 2:
            ship2 = Button(frame4, text="BB", padx=40, pady=10, fg='blue').grid(row = 4, column = 22) #sets a ship button for ship 2 on frame 4
            ship2 = Button(frame5, text="BB", padx=40, pady=10, fg='blue').grid(row = 4, column = 22) #sets a ship button for ship 2 on frame 5
            if x >= 3:
                ship3 = Button(frame4, text="CCC", padx=60, pady=10, fg='orange').grid(row = 5, column = 22) #sets a ship button for ship 3 on frame 4
                ship3 = Button(frame5, text="CCC", padx=60, pady=10, fg='orange').grid(row = 5, column = 22) #sets a ship button for ship 3 on frame 5
                if x >= 4:
                    ship4 = Button(frame4, text="DDDD", padx=80, pady=10, fg='green').grid(row = 6, column = 22) #sets a ship button for ship 4 on frame 4
                    ship4 = Button(frame5, text="DDDD", padx=80, pady=10, fg='green').grid(row = 6, column = 22) #sets a ship button for ship 4 on frame 5
                    if x >= 5:
                        ship5 = Button(frame4, text="EEEEE", padx=100, pady=10, fg='purple').grid(row = 7, column = 22) #sets a ship button for ship 5 on frame 4
                        ship5 = Button(frame5, text="EEEEE", padx=100, pady=10, fg='purple').grid(row = 7, column = 22) #sets a ship button for ship 5 on frame 5

def setup_frame5():#simple function that resets all the variables so player 2 sees a fresh board and frame 5 is shown so player 2 can start placing their ships.
    global place_board 

    place_board.reset()#important that reset doesn't happen until Finalize Ship Placement is pressed otherwise variables will be reset too early and player 1 can keep placing more ships 
    show_frame(frame5)

def p1_place_ships(i):
    global num_ships
    global player_1

    place_board.place_ship(i, player_1.my_board, num_ships)

    if (place_board.p1_is_finalized()):
        frame4_button = Button(frame4, text="Finalize Ship\nPlacement", padx=20, pady=20, command=partial(setup_frame5)).grid(row = 11, column = 22)#when Finalize Ship Placement is pressed then setup_frame5 function is called

def p2_place_ships(i):
    global num_ships
    global player_1

    place_board.place_ship(i, player_2.my_board, num_ships)

    if (place_board.p2_is_finalized()):
        frame5_button = Button(frame5, text="Finalize Ship\nPlacement", padx=20, pady=20, command=partial(show_frame,frame6)).grid(row = 11, column = 22)#when Finalized Ship Placement is pressed then frame6 displays on the screen


# @drawBoard:Helper Function for drawing the boards for the player turn screens
    #frame = frame to draw board on 
    #type = "p1" or "p2" - specifies which enemy board to work with
    #size = size of button i.e. value of padx and pady
    #offset_r = number of rows to offset by
    #offset_c = number of columns to offset by
def draw_boards(type, size, offset_r, offset_c):
    print("test DRAWBOARDS")
    global player_1
    global player_2
    if type == "p1":
        print("HERE P1")
    
        #draw player board, creates a 10 x 10 canvas for the buttons to be placed in
        for i in range(10):
            # shape the grid
            setsize2 = Canvas(frame7, width=size, height=0).grid(row=11, column=i)
            setsize2 = Canvas(frame7, width=0, height=size).grid(row=i, column=11)

        pos = product(range(10), range(10))
        for i, item in enumerate(pos):
            #copy important attributes of current button
            img= player_1.my_board[i].cget("image")
            txt = player_1.my_board[i].cget("text")
            b = player_1.my_board[i].cget("bg")

            temp = player_1.my_board[i]
            button = Button(master=frame7, image=img, text=txt, compound=CENTER, bg=b) #make a copy
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player_1.my_board[i] = button #replace button with copied button
            temp.destroy() #destroy old button

       
        #draw enemy board
        for i in range(10):
            # shape the grid, creates a 10 x 10 canvas for buttons to be placed in
            setsize1 = Canvas(frame7, width=size, height=0).grid(row=11, column=i+offset_c)
            setsize1 = Canvas(frame7, width=0, height=size).grid(row=i, column=11+offset_c)
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

#@pre: ships are already placed on the player's board
#@post sets the positions of each ship
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
    elif type == "p2":
        for i in range(len(player_2.my_board)): #iterate through the player's board
            btn_text = player_2.my_board[i].cget("text")
            if btn_text != "": #will either be "A", "B", "C", "D", or "E"
                print("i and button text: " + str(i) + " " + btn_text)
                player_2.ships[btn_text].positions.append(i) #add this index to the position of the corresponding ship

def board(type, size): #size = width and length of the canvas
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
            setsize = Canvas(frame4, width=size, height=0).grid(row=11, column=i)
            setsize = Canvas(frame4, width=0, height=size).grid(row=i, column=11)
        for i, item in enumerate(pos):
            button = Button(frame4, command=partial(p1_place_ships, i=i))
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player_1.my_board.append(button)
    if type == 'p1_attack': #it is player 1's turn and they are attacking 
        if not P1_ENEMY_CREATED:
            assign_positions("p2") # assign positions indices for player 2's own ships, so that p1 may attack them
            pos = product(range(10), range(10))
            #create
            for i in range(10):
                # shape the grid
                setsize = Canvas(frame7, width=size, height=0).grid(row=11, column=i)
                setsize = Canvas(frame7, width=0, height=size).grid(row=i, column=11)
            for i, item in enumerate(pos):
                button = Button(frame7, text="", command=partial(attack, i, "p1"))
                button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
                player_1.enemy_board.append(button)
            P1_ENEMY_CREATED = True   

        #draw the frame7 screen
        draw_boards("p1", size, offset_r=0, offset_c=14) #offset between boards
        show_frame(frame7) #shows frame 7

    if type == 'p2_set': #it is player 1's turn and they are placing their ships
        pos = product(range(10), range(10))

        for i in range(10):
            # shape the grid, creates a 10 x 10 canvas for buttons to be placed in
            setsize = Canvas(frame5, width=size, height=0).grid(row=11, column=i)
            setsize = Canvas(frame5, width=0, height=size).grid(row=i, column=11)
        
        for i, item in enumerate(pos):
            button = Button(frame5, command=partial(p2_place_ships, i=i))
            button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
            player_2.my_board.append(button)

    if type == 'p2_attack': #it is player 2's turn and they are attacking 
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
        show_frame(frame9) #shows frame 9


def setup_frame3(number_of_ships):
    ship_count(number_of_ships) #passes in number_of_ships value
    show_frame(frame3) #shows frame 3
    
myButton1 = Button(frame2, text="1 ship  ",font=("Arial",20, BOLD), padx=25, pady=25, command=partial(setup_frame3, 1)).place(relx=.5,rely=.3,anchor= CENTER) #button to select 1 ship, calls setup_frame3
myButton2 = Button(frame2, text="2 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=partial(setup_frame3, 2)).place(relx=.5,rely=.4,anchor= CENTER) #button to select 2 ships, calls setup_frame3
myButton3 = Button(frame2, text="3 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=partial(setup_frame3, 3)).place(relx=.5,rely=.5,anchor= CENTER) #button to select 3 ships, calls setup_frame3
myButton4 = Button(frame2, text="4 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=partial(setup_frame3, 4)).place(relx=.5,rely=.6,anchor= CENTER) #button to select 4 ships, calls setup_frame3
myButton5 = Button(frame2, text="5 ships",font=("Arial",20, BOLD), padx=25, pady=25, command=partial(setup_frame3, 5)).place(relx=.5,rely=.7,anchor= CENTER) #button to select 5 ships, calls setup_frame3

def show_done_button(type): #toggles button on player 1 or player 2's screen based on "type" (button not active until player has fired)
    global frame7_button
    global frame9_button
    if type == "p1":
        frame9_button.configure(state=DISABLED)
        frame7_button.configure(state=NORMAL)
    elif type == "p2":
        frame7_button.configure(state=DISABLED)
        frame9_button.configure(state=NORMAL)

#Attack_Method
def attack(i, type): #playerId = "p1" or "p2"
    global player_1
    global player_2


    global p1_fired
    global p2_fired
    global img_miss
    global img_hit
    if(type == "p1"): #miss
        p2_fired = False
        if not p1_fired:
            btn_text = player_2.my_board[i].cget("text")
            if(btn_text == ""): #miss!
                player_1.enemy_board[i].configure(bg="white", image=img_miss, compound=CENTER, state ='disabled') #miss 
                player_2.my_board[i].configure(bg="white", image=img_miss, compound=CENTER, state ='disabled')
                show_done_button("p1")
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

#Frame 1 code
myLabel1 = Label(frame1, text="Battleship!\nPress start to begin playing.",font=("Arial", 25)).place(relx=.5, rely=.2,anchor= CENTER)
frame1_button = Button(frame1, text="Start",font=("Arial",70, BOLD), command=partial(show_frame,frame2), bg="white", padx=20,pady=20, image=img_start, compound=CENTER).place(relx=.50, rely=.5,anchor= CENTER)

#Frame 2 code
myLabel2 = Label(frame2, text="Choose the number of ships each player will have.",font=("Arial",30, BOLD)).place(relx=.51, rely=.2,anchor= CENTER)

#Frame 3 code
e = Entry(frame3,width=50)
e.place(anchor=CENTER, relx=0.5, rely=0.45)
e.insert(0, "Player 1")
b = Entry(frame3, width=50)
b.place(anchor=CENTER, relx=0.5, rely=0.5)
b.insert(0, "Player 2")
#button
frame3_button = Button(frame3, text="Enter", command=partial(set_player_names), padx= 15, pady=15).place(anchor=CENTER, relx=0.5, rely=0.58,) #calls set_player_names when clicked and moves to frame 4

def check_win(nextFrame): #checks for a win condition (after player 1's turn and after player 2's turn)
    global player_1
    global player_2
    
    #keeps track of how many lives player 1 has
    p1_lives = 0
    for k in player_1.ships.keys():
        num = player_1.ships[k].lives
        p1_lives += num

    #keeps track of how many lives player 2 has
    p2_lives = 0
    for k in player_2.ships.keys():
        num = player_2.ships[k].lives
        p2_lives += num

    if p2_lives == 0:
        show_frame(frame10) #shows frame 10
        label_10_p1 = Label(frame10, text=player_1.name + " Wins!!!", font=("Arial", 60)) #label for if player 1 wins
        label_10_p1.place(relx=.5, rely=.2,anchor= CENTER)
    elif p1_lives == 0:
        show_frame(frame10), #shows frame 10
        label_10_p2 = Label(frame10, text=player_2.name + " Wins!!!", font=("Arial", 60)) #label for if player 2 wins
        label_10_p2.place(relx=.5, rely=.2,anchor= CENTER)
    else:
        show_frame(nextFrame) #shows next frame in the loop 6 - 9 if no one has won yet

#frame 6 code = popup player 1
frame6_button = Button(frame6, text="Ready " + player_1.name + "?", padx=20, pady=20, command=partial(board, "p1_attack", 40)).place(anchor=CENTER, relx=0.5, rely=0.3)

#frame 7 = player 1 turn, creates six labels for selecting a grid to attack, color key for hitting or missing, and which board is who's
mylabel = Label(frame7, text="Select a grid to attack").grid(row=1, column=12)
label_key_red = Label(frame7, text="Red = HIT", fg='red', bg='grey').grid(row=2, column=12)
label_key_white = Label(frame7, text="White = MISS", fg='white', bg='black').grid(row=3, column=12)
label_key_black = Label(frame7, text="Black = SUNK", fg='black', bg='white').grid(row=4, column=12)
my_board_label = Label(frame7, text="Your Board").grid(row=12, column=3, columnspan=3)
enemy_board_label = Label(frame7, text="Enemy Board").grid(row=12, column=17,columnspan=3)

frame7_button = Button(frame7, text=player_1.name + " Done", padx=20, pady=20, state = DISABLED, command=partial(check_win, frame8)) #player 1 done button on frame 7
frame7_button.grid(row=14, column=12)

#frame 8 = popup player 2   
frame8_button = Button(frame8, text="Ready " + player_2.name + "?", padx=20, pady=20, command=partial(board, "p2_attack",40)).place(anchor=CENTER, relx=0.5, rely=0.3,)

#frame 9 = player 2 turn, creates six labels for selecting a grid to attack, color key for hitting or missing, and which board is who's
mylabel = Label(frame9, text="Select a grid to attack").grid(row=1, column=12)
label_key_red = Label(frame9, text="Red = HIT", fg='red', bg='grey').grid(row=2, column=12)
label_key_white = Label(frame9, text="White = MISS", fg='white', bg='black').grid(row=3, column=12)
label_key_black = Label(frame9, text="Black = SUNK", fg='black', bg='white').grid(row=4, column=12) 
my_board_label = Label(frame9, text="Your Board").grid(row=12, column=3, columnspan=3)
enemy_board_label = Label(frame9, text="Enemy Board").grid(row=12, column=17,columnspan=3)  

frame9_button = Button(frame9, text=player_2.name + " Done", padx=20, pady=20, state=DISABLED, command=partial(check_win, frame6)) #player 2 done button on frame 9
frame9_button.grid(row=14, column=12)

#Frame 10 = endscreen
frame10_button = Button(frame10, text="Press to Quit" ,font=("Arial",50, BOLD), bg="white", padx=20,pady=20, command=root.destroy) #press to quit button, closes program
frame10_button.place(relx=.50, rely=.5,anchor= CENTER)

root.mainloop()
