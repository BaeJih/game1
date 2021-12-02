from os import closerange
import pygame
from pygame.constants import DOUBLEBUF, K_LEFT, KEYDOWN
from pygame.event import event_name, get
from pygame.math import enable_swizzling
import random
# #############################################################################################
# # 기본 초기화 (반드시 해야 하는 것들)
pygame.init()
# # 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# # 화면 타이틀 설정
pygame.display.set_caption("QUIZ")

# # FPS
clock = pygame.time.Clock()
# #############################################################################################

# # 1.사용자 게임 초기화(배경화면, 게임 이미지, 좌표,속도 , 폰트 등)
# 배경 만들기
background = pygame.image.load(
    "C:/Users/ICNIT/Desktop/코딩/새 폴더 (3)/pygame_basic/background.png")

# 캐릭터 만들기
character = pygame.image.load(
    "C:/Users/ICNIT/Desktop/코딩/새 폴더 (3)/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0
character_speed = 10

# 똥 만들기
ddong = pygame.image.load(
    "C:/Users/ICNIT/Desktop/코딩/새 폴더 (3)/pygame_basic/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10

# # 2.이벤트 처리(키보드,마우스 등)
running = True  # 게임이 진행중인가
while running:
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed
    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width-ddong_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running: False

    # 5. 화면 그리기

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    pygame.display.update()  # 게임 화면을 다시 그리기!


# pygame 종료
pygame.quit()
