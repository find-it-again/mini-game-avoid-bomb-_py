import pygame
import random
import sys

class Character:
    def __init__(self):
        self.character = pygame.image.load("C:/Users/dnqls/OneDrive/바탕 화면/pygame/프로젝트/character.png")
        self.character_size = self.character.get_rect().size
        self.character_width = self.character_size[0]
        self.character_height = self.character_size[1]
        self.character_x_pos = (screen_width / 2) - (self.character_width / 2)
        self.character_y_pos = screen_height - self.character_height
        self.to_x = 0
        self.to_y = 0
        self.character_speed = 0.5
        
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.to_x -= 3
                elif event.key == pygame.K_d:
                    self.to_x += 3
                elif event.key == pygame.K_LEFT:
                    self.to_x -= self.character_speed
                elif event.key == pygame.K_RIGHT:
                    self.to_x += self.character_speed
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    self.to_x = 0
                    
        self.character_x_pos += self.to_x * dt
                    
        if self.character_x_pos <= 0:
            self.character_x_pos = 0
        
        elif self.character_x_pos >= screen_width - self.character_width:
            self.character_x_pos = screen_width - self.character_width
        
class Bomb:
    def __init__(self):
        self.bomb = pygame.image.load("C:/Users/dnqls/OneDrive/바탕 화면/pygame/프로젝트/bomb.png")
        self.bomb_size = self.bomb.get_rect().size
        self.bomb_width = self.bomb_size[0]
        self.bomb_height = self.bomb_size[1]
        self.bomb_x_pos = random.randint(11, screen_width - self.bomb_width)
        self.bomb_y_pos = 10
        self.bomb_speed = random.randint(1, 10)
    
    def free_fall(self):
        global total_score
        
        self.bomb_speed += 1
        self.bomb_y_pos += self.bomb_speed
        if self.bomb_y_pos > screen_height:
            total_score += 10
            self.bomb_x_pos = random.randint(11, screen_width - self.bomb_width)
            self.bomb_y_pos = 10
            self.bomb_speed = 10

while True:
        # 초기화
    pygame.init()

    # 화면 크기 설정
    screen_width = 1200
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))

    # FPS
    clock = pygame.time.Clock()

    # 화면 타이틀 설정(게임 이름)
    pygame.display.set_caption("폭탄 피하기 게임")

    # 배경 이미지 불러오기
    background = pygame.image.load("C:/Users/dnqls/OneDrive/바탕 화면/pygame/프로젝트/background.png")

    # 폰트 정의
    big_font = pygame.font.Font(None, 60)
    small_font = pygame.font.Font(None, 30)
    # 총 점수
    total_score = 0

    gameover = "Game Over"
    game_start = True
    game = False
    game_end = False

    character = Character()
    bomb1 = Bomb()
    bomb2 = Bomb()
    bomb3 = Bomb()
    bomb4 = Bomb()
    while game_start:
        start_message = big_font.render("Press the s key to start the game", True, (0, 0, 0))
        rule1 = small_font.render("control : steer with direction key that right or left, Teleportation = a or d key", True, (0, 0, 0))
        rule2 = small_font.render("Game Rule : 10 points for every time you avoid a bomb. If you get hit by a bomb, game over", True, (0, 0, 0))
        
        screen.blit(background, (0, 0))
        screen.blit(start_message, (300,100))
        screen.blit(rule1, (200,300))
        screen.blit(rule2, (200,400))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_start = False
                    game = True
                    
    while game:
        dt = clock.tick(30)
                
        character.move()
        bomb1.free_fall()
        bomb2.free_fall()
        bomb3.free_fall()
        bomb4.free_fall()
                
        character_rect = character.character.get_rect()
        character_rect.left = character.character_x_pos
        character_rect.top = character.character_y_pos
        
        bomb1_rect = bomb1.bomb.get_rect()
        bomb1_rect.left = bomb1.bomb_x_pos
        bomb1_rect.top = bomb1.bomb_y_pos
        
        bomb2_rect = bomb2.bomb.get_rect()
        bomb2_rect.left = bomb2.bomb_x_pos
        bomb2_rect.top = bomb2.bomb_y_pos
        
        bomb3_rect = bomb3.bomb.get_rect()
        bomb3_rect.left = bomb3.bomb_x_pos
        bomb3_rect.top = bomb3.bomb_y_pos
        
        bomb4_rect = bomb4.bomb.get_rect()
        bomb4_rect.left = bomb4.bomb_x_pos
        bomb4_rect.top = bomb4.bomb_y_pos

        if character_rect.colliderect(bomb1_rect):
            pygame.time.delay(500)
            game = False
            game_end = True
        elif character_rect.colliderect(bomb2_rect):
            pygame.time.delay(500)
            game = False
            game_end = True
        elif character_rect.colliderect(bomb3_rect):
            pygame.time.delay(500)
            game = False
            game_end = True
        elif character_rect.colliderect(bomb4_rect):
            pygame.time.delay(500)
            game = False
            game_end = True
        
        score = small_font.render(str(int(total_score)), True, (255, 255, 255))
            
        screen.blit(background, (0, 0))
        screen.blit(bomb1.bomb, (bomb1.bomb_x_pos, bomb1.bomb_y_pos))
        screen.blit(bomb2.bomb, (bomb2.bomb_x_pos, bomb2.bomb_y_pos))
        screen.blit(bomb3.bomb, (bomb3.bomb_x_pos, bomb3.bomb_y_pos))
        screen.blit(bomb4.bomb, (bomb4.bomb_x_pos, bomb4.bomb_y_pos))
        screen.blit(character.character, (character.character_x_pos, character.character_y_pos))
        screen.blit(score, (10, 10))
        pygame.display.update()

    while game_end:
        re_message = small_font.render("restart : y key, end : n key", True, (0, 0, 0))
        end_msg = big_font.render(gameover, True, (255, 0, 0))
        msg_rect = end_msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
        screen.blit(background, (0, 0))
        screen.blit(end_msg, (450,100))
        screen.blit(re_message, (450, 350))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    game_start = True
                    game_end = False
                elif event.key == pygame.K_n:
                    game_end = False
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
