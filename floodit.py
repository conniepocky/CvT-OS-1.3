from guizero import App, Waffle, Text, PushButton, info, warn, info
import random

#VARS

colours = ["peru", "olive", "PeachPuff", "plum", "DarkOrange", "DeepPink"]
board_size = 14

moves_limit = 25

moves_taken = 0

def flood(x, y, target, replacement):
   
    if target == replacement:
        return False
    if board.get_pixel(x, y) != target:
        return False
    board.set_pixel(x, y, replacement)
    if y+1 <= board_size-1:   # South
        flood(x, y+1, target, replacement)
    if y-1 >= 0:            # North
        flood(x, y-1, target, replacement)
    if x+1 <= board_size-1:    # East
        flood(x+1, y, target, replacement)
    if x-1 >= 0:            # West
        flood(x-1, y, target, replacement)

def all_squares_are_the_same():
    squares = board.get_all()
    if all(colour == squares[0] for colour in squares):
        return True
    else:
        return False

def win_check():
    print("ayyayayay checkedddddddd!")
    global moves_taken
    moves_taken += 1
    if moves_taken <= moves_limit:
        if all_squares_are_the_same():
            win_text.value = "You Win!!!"
            print("yayayayayyaya")
    else:
        win_text.value = "You lose!"
        palette.disable()

def fill_board():
    for x in range(board_size):
        for y in range(board_size):
            board.set_pixel(x,y, random.choice(colours))

def init_palette():
    column = 0
    for colour in colours:
        palette.set_pixel(column,0,colour)
        column +=1


def start_flood(x,y):
    flood_colour = palette.get_pixel(x,y)
    target = board.get_pixel(0,0) 

    flood(0,0 ,target, flood_colour)

    win_check()

    move_text.value = moves_taken

    
        
#Main

app = App("Flood it!")

board = Waffle(app, width=board_size, height=board_size, pad=0)

palette = Waffle(app, width=6, height=1, dotty=True, command=start_flood)

win_text = Text(app)

move_text = Text(app)

warn("Flood it!", "You only have 25 moves! ")

fill_board()

init_palette()

app.display()

