import random

def play_game():
    options = ["가위", "바위", "보"]
    
    # 사용자 입력
    user_choice = input("가위, 바위, 보 중 하나를 입력하세요: ")
    if user_choice not in options:
        print("잘못된 입력입니다.")
        return

    # 컴퓨터 랜덤 선택
    computer_choice = random.choice(options)
    print(f"컴퓨터: {computer_choice}")

    # 승패 판정
    if user_choice == computer_choice:
        print("비겼습니다!")
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        print("이겼습니다!")
    else:
        print("졌습니다!")

# 게임 실행
play_game()
