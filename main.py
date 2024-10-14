# Backgammon

import random, pygame

pygame.init()
display = pygame.display.set_mode((1500, 600))
font = pygame.font.Font(None,40)

board_1 = [0,0,0,0,0,5,0,3,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,2] #goes left
board_2 = [2,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0] #goes right
boards = [board_1,board_2]
#jails = [jail_1,jail_2]

def show_board():
    for i in range(12):
        text = font.render(str(board_1[i]),None,(255,0,0))
        display.blit(text, (30+30*i,20))
    for i in range(12):
        text = font.render(str(board_1[23-i]),None,(255,0,0))
        display.blit(text, (30+30*i,60))
    

def roll_dice():
    global dice
    dice = [random.randint(1,6),random.randint(1,6)]
    if dice[0] == dice[1]:
        dice.append(dice[0]); dice.append(dice[0])
    return dice

def player_move(player):
    roll_dice()
    finished = False
    while not finished:
        try:
            from_space = int(input("Enter which board place you want to move the piece FROM."))
        except:
            print("Invalid input. Enter which board place you want to move the piece FROM.")
        if not (from_space >= 1 and from_space <= 24 and boards[player][from_space] != 0): #and jails[player] == 0:
            player_move(player)
        try:
            to_space = int(input("Enter which board place you want to move the piece TO."))
        except:
            print("Invalid input. Enter which board place you want to move the piece TO.")
        if not (to_space >= 1 and to_space <= 24 and boards[(player+1)%2][23-to_space] == 0): #and jails[player] == 0:
            player_move(player)
            
run = True
while run:
    display.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
    show_board()
    pygame.display.flip()
    
pygame.quit()
            


