from colorama import init, Fore, Back
from random import randint
import pickle
# if you don't have colorama downloaded, Please install it using pip command "pip install colorama"
# use terminal with a black background for better experience

game_rules = Fore.GREEN + '''
This game is similar to the game "Battleship".
You are provided with a game board,
where you have to find:-
i)   An aircraft career 6 squares long
ii)  A destroyer 4 squares long
iii) A frigate 2 squares long
Enter the square you want to destroy in
the format: <row_value><column_value>
For Example: 11 -> destroys the top left square
Blue color or * denotes water.
Black color or o denotes a Ship.
Red color or x denotes a wasted move.
All the best! Try to beat your High Score!
'''

# function to get and save the highscore
def get_highscore():
    try:
        with open("Highscore.dat", "rb") as file:
            highscore = pickle.load(file)
    except:
        open("Highscore.dat", "wb+").close()
        highscore = 64
    return highscore

def save_highscore(x):
    with open("Highscore.dat", "wb") as file:
        pickle.dump(x, file)

# function to print the board
def get_board():
    print("1  2  3  4  5  6  7  8".center(50," "))
    print(("+"+("  -"*8)+"  +").center(50," "))
    for i in range(len(game_board)):
        print((" "*8) + str(i + 1) + "  | ",end="")
        for j in game_board[i]:
            if j == "*":
                print(Back.BLUE + " * ",end="")
            elif j == "x":
                print(Back.RED + " x ",end="")
            else:
                print(Back.BLACK + " o ",end="")
        print(" |   ")
    print(("+"+("  -"*8)+"  +").center(50," "))


#function to get complete coordinate of a ship given the initial coordinate length and direction
def get_coord(ic, l,d):
    c = [ic.copy()]
    for i in range(1, l):
        ic[d] += 1
        c.append(ic.copy())
    return c


# function to return the coordinates of the ship
def create_ship():
    ac_d,d_d,f_d = randint(0,1),randint(0,1),randint(0,1) # 0 for vertical, 1 for horizontal
    if ac_d:
        ac_ic = [randint(0,7),randint(0,2)] # horizontal
    else:
        ac_ic = [randint(0,2),randint(0,7)] # vertical
    ac_c = get_coord(ac_ic, 6, ac_d)
    place = False
    while not place:
        if d_d:
            d_ic = [randint(0, 7), randint(0, 4)]  # horizontal
        else:
            d_ic = [randint(0, 4), randint(0, 7)]  # vertical
        d_c = get_coord(d_ic, 4, d_d)
        for i in d_c:
            if i in ac_c:
                place = False
                break
            else:
                place = True
    place = False
    while not place:
        if f_d:
            f_ic = [randint(0, 7), randint(0, 6)]  # horizontal
        else:
            f_ic = [randint(0, 6), randint(0, 7)]  # vertical
        f_c = get_coord(f_ic, 2, f_d)
        for i in f_c:
            if (i in ac_c) or (i in d_c):
                place = False
                break
            else:
                place = True
    return [ac_c,d_c,f_c]


# function containing the game
def game():
    highscore = get_highscore()
    moves = []
    ships_found = 0
    ships_found_list = [0,0,0]
    message = Fore.GREEN + "Lets start!"
    ship_coords = create_ship()
    while not (ships_found==3):
        ships_found = (ships_found_list[0]//6)+(ships_found_list[1]//4)+(ships_found_list[2]//2)
        print("\n"*50)
        print(Fore.YELLOW + "Highscore: ", highscore, end="\t")
        print(Fore.BLUE + "Moves: ", len(moves), end="\t")
        print(Fore.BLUE + "Ships found: ", ships_found)
        print(message)
        get_board()
        if ships_found == 3:
            print(Fore.YELLOW + "Congratulations! You won!")
            if len(moves) < highscore:
                print(Fore.YELLOW + "New Highscore:", len(moves))
                save_highscore(len(moves))
            input()
            continue
        sq = input("Enter the square you want to destroy: ").replace(" ","")
        if (len(sq) == 2) and (sq[0] in "12345678") and (sq[1] in "12345678"):
            sq = [int(sq[0])-1, int(sq[1])-1]
            if sq in moves:
                message = Fore.RED + "Move has been already done!"
                continue
            for i in range(3):
                if sq in ship_coords[i]:
                    game_board[sq[0]][sq[1]] = "o"
                    ships_found_list[i] += 1
                    moves += [sq.copy()]
                    message = Fore.GREEN + "You have hit a ship!"
                    break
            else:
                game_board[sq[0]][sq[1]] = "x"
                moves += [sq.copy()]
                message = Fore.RED + "You have missed!"
        else:
            message = Fore.RED + "Invalid Input! Format is: <row_value><column_value>"


# main program
game_loop = True
init(autoreset=True)

while game_loop:
    print(Fore.YELLOW + "|Battle Ship|".center(50,"="))
    print(game_rules)
    start = input("Start Game? (Y for yes, N for no): ").lower()
    if start == "y":
        game_board = [["*","*","*","*","*","*","*","*"],
                      ["*","*","*","*","*","*","*","*"],
                      ["*","*","*","*","*","*","*","*"],
                      ["*","*","*","*","*","*","*","*"],
                      ["*","*","*","*","*","*","*","*"],
                      ["*","*","*","*","*","*","*","*"],
                      ["*","*","*","*","*","*","*","*"],
                      ["*","*","*","*","*","*","*","*"]]
        game()
    else:
        game_loop = False
print(Fore.YELLOW + "|Thank you For Playing|".center(50,"="))
input()


