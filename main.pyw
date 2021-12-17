import random
import copy
import time
import pygame

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        x, y = find

    for i in range(1,10):
        if valid(bo, i, (x, y)):
            bo[y][x] = i

            if solve(bo):
                return True

            bo[y][x] = 0

    return False


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[1]][i] == num and pos[0] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[0]] == num and pos[1] != i:
            return False

    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and pos != [j,i]:
                return False

    return True

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (j,i)

    return None

def sudoku_maker():
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    solved = copy.deepcopy(board)

    while True:
        new = copy.deepcopy(board)

        counter = 0

        for i in range(100):
            pos = [random.randint(0,8),random.randint(0,8)]
            num = random.randint(1,9)
            if valid(new,num,pos):
                new[pos[1]][pos[0]] = num
                counter += 1

            if counter == 15:
                break
            

        if solve(new):
            solved = copy.deepcopy(new)
            board = copy.deepcopy(new)
            break

    for i in range(60):
        x = random.randint(0,8)
        y = random.randint(0,8)

        board[y][x] = 0

    return board, solved

board, solved = sudoku_maker()
cur = copy.deepcopy(board)
check = copy.deepcopy(board)
pos = [0,0]

pygame.init()

width,height = 540,540
win = pygame.display.set_mode((width,height+40))
pygame.display.set_caption("Sudoku")
pygame.font.init()

font = pygame.font.Font(pygame.font.get_default_font(), 36)
finished = False
timemins = 0
timesecs = 0
timecount = 0
clock = pygame.time.Clock()
size = width//9
run = True
while run:
    if not find_empty(check):
        finished = True

    if not finished:
        timecount += 1
    if timecount == 30:
        timecount = 0
        timesecs += 1
        if timesecs == 60:
            timesecs = 0
            timemins += 1
    clock.tick(30)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0] // size
            y = mouse_pos[1] // size
            if not (mouse_pos[1] > height):
                pos = [x,y]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                finished = True
                check = copy.deepcopy(solved)
            if event.key == pygame.K_SPACE:
                board, solved = sudoku_maker()
                cur = copy.deepcopy(board)
                check = copy.deepcopy(board)
                pos = [0,0]
                finished = False
                timesecs = 0
                timecount = 0
                timemins = 0
            if event.key == pygame.K_LEFT:
                if pos[0] != 0:
                    pos[0] -= 1
            if event.key == pygame.K_RIGHT:
                if pos[0] != 8:
                    pos[0] += 1
            if event.key == pygame.K_UP:
                if pos[1] != 0:
                    pos[1] -= 1
            if event.key == pygame.K_DOWN:
                if pos[1] != 8:
                    pos[1] += 1

            if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                if board[pos[1]][pos[0]] == 0:
                    cur[pos[1]][pos[0]] = 0
                    check[pos[1]][pos[0]] = 0

            if event.key == pygame.K_1:
                if board[pos[1]][pos[0]] == 0:
                    if valid(check,1,pos):
                        cur[pos[1]][pos[0]] = [1,1]
                        check[pos[1]][pos[0]] = 1
                    else:
                        cur[pos[1]][pos[0]] = [1,0]

            if event.key == pygame.K_2:
                if board[pos[1]][pos[0]] == 0:
                    if valid(check,2,pos):
                        cur[pos[1]][pos[0]] = [2,1]
                        check[pos[1]][pos[0]] = 2
                    else:
                        cur[pos[1]][pos[0]] = [2,0]

            if event.key == pygame.K_3:
                if board[pos[1]][pos[0]] == 0:
                    if valid(check,3,pos):
                        cur[pos[1]][pos[0]] = [3,1]
                        check[pos[1]][pos[0]] = 3
                    else:
                        cur[pos[1]][pos[0]] = [3,0]

            if event.key == pygame.K_4:
                if board[pos[1]][pos[0]] == 0:
                    if valid(check,4,pos):
                        cur[pos[1]][pos[0]] = [4,1]
                        check[pos[1]][pos[0]] = 4
                    else:
                        cur[pos[1]][pos[0]] = [4,0]

            if event.key == pygame.K_5:
                if board[pos[1]][pos[0]] == 0:
                    if valid(check,5,pos):
                        cur[pos[1]][pos[0]] = [5,1]
                        check[pos[1]][pos[0]] = 5
                    else:
                        cur[pos[1]][pos[0]] = [5,0]

            if event.key == pygame.K_6:
                if board[pos[1]][pos[0]] == 0:
                    if valid(check,6,pos):
                        cur[pos[1]][pos[0]] = [6,1]
                        check[pos[1]][pos[0]] = 6
                    else:
                        cur[pos[1]][pos[0]] = [6,0]

            if event.key == pygame.K_7:
                if board[pos[1]][pos[0]] == 0:
                    if valid(check,7,pos):
                        cur[pos[1]][pos[0]] = [7,1]
                        check[pos[1]][pos[0]] = 7
                    else:
                        cur[pos[1]][pos[0]] = [7,0]

            if event.key == pygame.K_8:
                if board[pos[1]][pos[0]] == 0:
                    if valid(check,8,pos):
                        cur[pos[1]][pos[0]] = [8,1]
                        check[pos[1]][pos[0]] = 8
                    else:
                        cur[pos[1]][pos[0]] = [8,0]

            if event.key == pygame.K_9:
                if board[pos[1]][pos[0]] == 0:
                    if valid(check,9,pos):
                        cur[pos[1]][pos[0]] = [9,1]
                        check[pos[1]][pos[0]] = 9
                    else:
                        cur[pos[1]][pos[0]] = [9,0]

    win.fill('white')

    for i in range(9):
        for j in range(9):
            if not finished:
                if (i == pos[0]) or (j == pos[1]) or ((i//3 == pos[0]//3) and (j//3 == pos[1]//3)):
                    pygame.draw.rect(win,(222,222,222),(i*size,j*size,size,size))

                if ((check[j][i] == check[pos[1]][pos[0]]) and check[j][i] != 0):
                    pygame.draw.rect(win,(150,150,150),(i*size,j*size,size,size))


            if finished:
                if board[j][i] != 0:
                    text = font.render(str(check[j][i]),True,(0,0,0))
                    win.blit(text,(i*size+size/3,j*size+size/3))
                else:
                    text = font.render(str(check[j][i]),True,(0,200,0))
                    win.blit(text,(i*size+size/3,j*size+size/3))
            elif cur[j][i] != 0:
                if board[j][i] != 0:
                    text = font.render(str(cur[j][i]),True,(0,0,0))
                    win.blit(text,(i*size+size/3,j*size+size/3))
                else:
                    if cur[j][i][1]:
                        text = font.render(str(cur[j][i][0]),True,(0,200,0))
                        win.blit(text,(i*size+size/3,j*size+size/3))
                    else:
                        text = font.render(str(cur[j][i][0]),True,(150,0,0))
                        win.blit(text,(i*size+size/3,j*size+size/3))

    pygame.draw.rect(win,(0,0,0),(0,0,width,height),5)

    d = pygame.Surface((width,40))
    d.set_alpha(100)
    d.fill((0,0,0))
    win.blit(d,(0,height))

    for i in range(9):
        pygame.draw.line(win,(0,0,0),(i*size-1,0),(i*size-1,height),2)
        pygame.draw.line(win,(0,0,0),(0,i*size-1),(width,i*size-1),2)

        if i % 3 == 0:
            pygame.draw.line(win,(0,0,0),(i*size-1,0),(i*size-1,height),4)
            pygame.draw.line(win,(0,0,0),(0,i*size-1),(width,i*size-1),4)

    if not finished:
        pygame.draw.rect(win,(0,0,255),(pos[0]*size,pos[1]*size,size,size),4)

    if timesecs == 0:
        textsecs = "00"
    elif timesecs < 10:
        textsecs = "0" + str(timesecs)
    else:
        textsecs = str(timesecs)
    
    if timemins == 0:
        textmins = "00"
    elif timemins < 10:
        textmins = "0" + str(timemins)
    else:
        textmins = str(timemins)

    time = font.render(textmins + ":" + textsecs,True,(0,0,0))
    win.blit(time,(2,height+2))

    if finished:
        text = font.render("Solved!" , True, (0,0,0))
        win.blit(text,(width-text.get_width()-2, height+2))

    pygame.display.update()

pygame.quit()
exit()  
