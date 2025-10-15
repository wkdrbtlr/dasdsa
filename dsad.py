import random

def guess_the_number():
    """
    1부터 100 사이의 숫자를 맞추는 게임 함수
    """
    # 1부터 100 사이의 임의의 숫자를 선택합니다.
    secret_number = random.randint(1, 100)
    guess = 0
    attempts = 0

    print("🎉 숫자 맞추기 게임에 오신 것을 환영합니다! 🎉")
    print("제가 1부터 100 사이의 숫자 중 하나를 생각했습니다. 맞춰보세요!")

    # 사용자가 정답을 맞출 때까지 반복합니다.
    while guess != secret_number:
        try:
            # 사용자로부터 입력을 받습니다.
            guess_input = input("추측한 숫자를 입력하세요: ")
            guess = int(guess_input)
            attempts += 1

            # 사용자의 추측과 비밀 숫자를 비교합니다.
            if guess < secret_number:
                print("너무 작아요! 더 큰 숫자를 시도해보세요. 🤔")
            elif guess > secret_number:
                print("너무 커요! 더 작은 숫자를 시도해보세요. 🤔")
            else:
                print(f"🎉 축하합니다! {attempts}번 만에 숫자를 맞추셨습니다! 정답은 {secret_number}입니다.")

        except ValueError:
            # 사용자가 숫자가 아닌 값을 입력했을 경우 처리합니다.
            print("⚠️ 잘못된 입력입니다. 숫자만 입력해주세요.")

# 게임 시작
if __name__ == "__main__":
    guess_the_number()
