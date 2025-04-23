# while 반복문을 사용합니다.
while True:
    # 기본 출력
    print(".", end="\n")
    
    # 문자열 입력을 받아 반복을 끝낼지 확인합니다.
    input_text = input("종료하려면 'exit'을 입력하세요: ")
    if input_text == "exit":
        break
