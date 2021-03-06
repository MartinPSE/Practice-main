# <문제> 모험가 길드: 문제 설명
# 한 마을에 모험가 N 명이 있다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도' 를 측정했는데
# '공포도' 가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어진다.
#  모험가 길드장인 형석이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 X명 이상으로 구성한 모험가 그룹에 참여
#  형석이는 최대 몇개의 모험가 그룹을 만들 수 있는지 궁금하다. N 명의 모험가에 대한 정보가 주어졌을 때,
#  여행을 떠날 수 있는 그릅 수의 최댓값을 구하자.

#  예를 들어 N = 5  X(공포도) - > [2, 3, 1, 2, 2]
#  몇 명의 모험가는 마을에 그대로 남아 있어도 된다, 모든 모험가를 특정한 그룹에 넣을 필요는 없다.

"""
idea 1. 공포도를 오름차순
idea 2. 공포도를 보고, 그룹을 만든다.
idea 3. 바로바로 내보내는 거야 !!
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 결과 값
count = 0  # 그룹에 모험가 수

for i in data:  # 공포도를 낮은 것 부터 하나씩 확인
    count += 1  # 현재 그룹에 해당 모험가를 포함시키고
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹의 수 증가시키기
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력