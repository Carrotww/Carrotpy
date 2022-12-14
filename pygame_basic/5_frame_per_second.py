import pygame

pygame.init() # pygame 초기화 반드시 필요

# 화면 크기 설정 부분
screen_width = 480 # 가로
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 표시 부분
pygame.display.set_caption("carrot game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\유형석\\PycharmProjects\\pythonProject\\Carrotpy\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\유형석\\PycharmProjects\\pythonProject\\Carrotpy\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해 올 수 있음
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치함
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# Event loop
running = True # 게임 진행 여부 확인

while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 특정 이벤트가 발생하면 종료하게 설정
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # screen.fill((0, 0, 255)) # 이런 식으로 RGB를 주어서 배경이 가능
    screen.blit(background, (0, 0)) # 배경 그리기 왼쪽 위 끝에서 부터 사진을 채우는 것

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # pygame은 게임 화면을 계속 그려주어야 함 이게 없으면 배경이 보이지 않음

# pygame 종료되는 부분
pygame.quit()