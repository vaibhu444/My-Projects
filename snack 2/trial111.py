import pygame
import random
import os
pygame.mixer.init()
pygame.init()
screen_width=1200
screen_height=600
compwindo=pygame.display.set_mode((screen_width,screen_height))
bgimg=pygame.image.load('snake.jpg')
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

white= (255 , 255 , 255)
red= (255,0,0)
black=(0,0,0)
clock=pygame.time.Clock()

def plot_snack(compwindo, color, snk_list, snack_size):
    for x, y in snk_list:
        pygame.draw.rect(compwindo, color, [x, y, snack_size, snack_size])


font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text= font.render(text,True,color)
    compwindo.blit(screen_text,[x,y])
def welcome():
    exit_game=False
    while not exit_game:
        compwindo.fill((229,220,244))
        text_screen("Welcome To SnakeByVaibhav ",black,screen_width/4,screen_height/4)
        text_screen("Press Space To Play ", black, 400,250 )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('play_date.mp3.mp3')
                    pygame.mixer.music.play()
                    snk_game()

        pygame.display.update()
        clock.tick(30)


    pygame.quit()
    quit()



def snk_game():
    snack_x=10
    snack_y=10
    score=0
    velocity_x=10
    velocity_y=10
    snack_size=25
    init_velocity=10
    food_x=random.randint(0,screen_width)
    food_y=random.randint(0,screen_height)
    fps=30
    pygame.display.set_caption("My First Game")
    pygame.display.update()
    exit_game=False
    game_over=False
    snk_list=[]
    snk_length=1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt","rt") as f:
        highscore=f.read()
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            text_screen("Game Over! Enter To Continue",(150,150,150),screen_width/4,screen_height/4)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x= -init_velocity
                        velocity_y=0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x=0
                    if event.key == pygame.K_DOWN:
                        velocity_y =init_velocity
                        velocity_x=0
            snack_x=snack_x+velocity_x
            snack_y=snack_y+velocity_y
            if snack_x<0 or snack_x>screen_width or snack_y<0 or snack_y>screen_height:
                game_over=True
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
            if abs(food_x - snack_x)<6 and abs(food_y-snack_y)<6:
                score+=10
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snk_length+=5
                if score>int(highscore):
                    highscore =score
            compwindo.fill(white)
            compwindo.blit(bgimg,(0,0))
            text_screen("score:"+ str(score)+" Highscore:"+ str(highscore),red,5,5)
            pygame.draw.rect(compwindo, red, [food_x, food_y, snack_size, snack_size])
            head=[]
            head.append(snack_x)
            head.append(snack_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
            plot_snack(compwindo,black,snk_list,snack_size)
        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
welcome()
