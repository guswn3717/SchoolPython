import datetime

# 현재 날짜/시간을 구한다.
now = datetime.datetime.now()

# 현재 시간이 오전인지 오후인지에 따라 출력
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))
else:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))