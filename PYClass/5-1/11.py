# 함수 선언
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

# 함수 호출
print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0, 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))
