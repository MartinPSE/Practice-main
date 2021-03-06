# <문제> 시각
# 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각중에서 3이 하나라도 포함되는
# 모든 경우의 수를 구하는 프로그램을 작성해라.
# EX) 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
# 00 시 00 분 03 초
# 00시 13분 30 초

# BUT) 3이 하나도 포함 안되어 있는 것들
# 00시 02분 55초
# 01시 27분 45초

# 완전 탐색
"""
idea 1. 가능한 모든 시각의 경우를 하나씩 모두 세서 푸 는 문제
idea 2. 하루는 86,400초 --> 그냥 컴퓨터한테 식은 죽 먹기
idea 3 . Brute Forcing (완전 탐색) --> 1초에 2,000만 번 이란거 잊지마세요 )
"""

N = int(input())
count = 0
for i in range(N+1): # 0 -> index + 1
    for j in range(60): # 0 ~ 59 분
        for k in range(60): # 0 ~ 59 초
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
