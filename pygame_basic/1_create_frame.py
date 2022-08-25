import pygame

pygame.init() # pygame 초기화 반드시 필요

# 화면 크기 설정 부분
screen_width = 480 # 가로
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 표시 부분
pygame.display.set_caption("carrot game")

# Event loop
running = True # 게임 진행 여부 확인

while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 특정 이벤트가 발생하면 종료하게 설정
            running = False

# pygame 종료되는 부분
pygame.quit()