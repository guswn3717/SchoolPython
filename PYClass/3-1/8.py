import datetime

# 현재 날짜/시간을 구한다.
now = datetime.datetime.now()

# 봄 (3~5월)
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

# 여름 (6~8월)
elif 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

# 가을 (9~11월)
elif 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

# 겨울 (12, 1, 2월)
else:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))
