import pygame
from game_object import *
from data import *
from random import choice
pygame.init()


window = pygame.display.set_mode((set_win["WIDTH"], 
                                  set_win["HEIGHT"]))
pygame.display.set_caption("Ping-Pong")

def run():
    game = True
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)
    
    player_left = Board(start_game["LEFT_PLAYER"][0], 
                        start_game["LEFT_PLAYER"][1], 
                        set_board["WIDTH"], 
                        set_board["HEIGHT"],
                        None, 5)
    player_right = Board(start_game["RIGHT_PLAYER"][0], 
                        start_game["RIGHT_PLAYER"][1], 
                        set_board["WIDTH"],
                        set_board["HEIGHT"],
                        None, 5)
    
    ball = Ball(start_game["BALL"]["START"][0], 
                start_game["BALL"]["START"][1],
                set_ball["RADIUS"], 
                (0,255,0), None, 
                set_ball["SPEED"])


    while game:
        window.fill((0,0,0))
        pygame.draw.line(window, (255,255,255),
                          (set_win["WIDTH"]//2, 0), 
                          (set_win["WIDTH"]//2, set_win["HEIGHT"]))
        pygame.draw.rect(window, (255,0,0), player_left)
        pygame.draw.rect(window, (255,0,0), player_right)
        pygame.draw.circle(window, ball.COLOR, (ball.X, ball.Y), ball.RADIUS)
        win_lose_score(window, ball, player_left, player_right, font)
        player_left.move()
        player_right.move()
        if ball.DIRECTION:
            ball.move(player_left)
        else:
            ball.move(player_right)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_left.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    player_left.MOVE["DOWN"] = True
                ##
                if event.key == pygame.K_UP:
                    player_right.MOVE["UP"] = True
                if event.key == pygame.K_DOWN:
                    player_right.MOVE["DOWN"] = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player_left.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    player_left.MOVE["DOWN"] = False
                ##
                if event.key == pygame.K_UP:
                    player_right.MOVE["UP"] = False
                if event.key == pygame.K_DOWN:
                    player_right.MOVE["DOWN"] = False

        
        clock.tick(60)
        pygame.display.flip()

run()
