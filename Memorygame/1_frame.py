import pygame

# 초기화
pygame.init()
screen_width = 1280 # 가로
screen_height = 720 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Carrot Memory game')

# 게임 루프
running = True

while running:
    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False # 게임 끝

# 게임 종료
pygame.quit()