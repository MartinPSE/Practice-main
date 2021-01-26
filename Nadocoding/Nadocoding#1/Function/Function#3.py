# 지역변수 : 함수 내에서만 부를 수 있는 변수
# 전역변수 : 프로그램 내에서 전체적으로 부를 수 있는 변수 / global

gun = 10


def checkpoint(soldiers):  # 근무자들
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
#
# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# print("남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
