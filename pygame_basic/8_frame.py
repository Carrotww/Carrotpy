import pygame

############################################
pygame.init() # pygame 초기화 반드시 필요

# 화면 크기 설정 부분
screen_width = 480 # 가로
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 표시 부분
pygame.display.set_caption("carrot game")

# FPS
clock = pygame.time.Clock()
##############################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# Event loop

running = True # 게임 진행 여부 확인
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 부분(키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 특정 이벤트가 발생하면 종료하게 설정
            running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트

    # 5. 화면에 그리기
    pygame.display.update() # pygame은 게임 화면을 계속 그려주어야 함 이게 없으면 배경이 보이지 않음
    
# pygame 종료되는 부분
pygame.quit()