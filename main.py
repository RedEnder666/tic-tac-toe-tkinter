import tkinter


window = tkinter.Tk()
bord = tkinter.Canvas(window, bg='white', height=900, width=900)
d = {0: (150, 150),
     1: (450, 150),
     2: (750, 150),
     3: (150, 450),
     4: (450, 450),
     5: (750, 450),
     6: (150, 750),
     7: (450, 750),
     8: (750, 750)}



bord.grid()
def draw_board():
    bord.delete("all")
    bord.create_line(300,900, 300, 0)
    bord.create_line(600, 900, 600, 0)
    bord.create_line(0,300, 900, 300)
    bord.create_line(0, 600, 900, 600)
    for i in range(9):
        bord.create_text(d[i][0] + 50, d[i][1] - 50, text = str(i + 1))
    for j in range(9):
            if board[j] == "X":
                p = "X"
                c = "red"
            elif board[j] == "O":
                p = "O"
                c = "green"
            else:
                p = ""
                c = "black"
            bord.create_text(d[j][0], d[j][1], text = p, font='Times 30', fill=c)
board = []
def winner():
    global board
    board = list(range(1,10))
    

winner()
draw_board()

xop = "X"

def click(event):
    xy = 0, 0
    xy1 = 300, 300
    if event.x_root > xy[0] and event.x_root < xy1[0]:
        if event.y_root > xy[1] and event.y_root < xy1[1]:
            board[0] = xop

def take_input(player_token):
    draw_board()
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer[:1])
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print (f"Клеточка {player_answer} уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    draw_board()
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    draw_board()
    counter = 0
    win = False
    while not win:
        if counter % 2 == 0:
            xop = "X"
            take_input(xop)
        else:
            xop = "O"
            take_input(xop)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (f"{tmp}, вы выиграли!")
                win = True
                winner()
                break
        if counter == 9:
            print ("Ничья!")
            break
    


    


draw_board()
main(board)





window.mainloop()
print("Вы закрыли окно")
# Доделай это!!!
