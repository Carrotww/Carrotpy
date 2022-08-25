import pygame

pygame.init() # pygame 초기화 반드시 필요

# 화면 크기 설정 부분
screen_width = 480 # 가로
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 표시 부분
pygame.display.set_caption("carrot game")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\유형석\\PycharmProjects\\pythonProject\\Carrotpy\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\유형석\\PycharmProjects\\pythonProject\\Carrotpy\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해 올 수 있음
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치함
character_y_pos = screen_height - character_height

# Event loop
running = True # 게임 진행 여부 확인

while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 특정 이벤트가 발생하면 종료하게 설정
            running = False

    # screen.fill((0, 0, 255)) # 이런 식으로 RGB를 주어서 배경이 가능
    screen.blit(background, (0, 0)) # 배경 그리기 왼쪽 위 끝에서 부터 사진을 채우는 것

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # pygame은 게임 화면을 계속 그려주어야 함 이게 없으면 배경이 보이지 않음

# pygame 종료되는 부분
pygame.quit()