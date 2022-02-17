import sys

num = int(sys.stdin.readline())
profiles = []
for n in range(num):
    enroll = sys.stdin.readline().split()
    profile = (int(enroll[0]), enroll[1], n+1)    # 등록 나이, 이름, 순서 순으로 튜플 생성
    profiles.append(profile)    # 생성한 튜플을 리스트에 저장

profiles.sort(key=lambda profile: (profile[0], profile[2]))    # 튜플의 나이, 순서 순으로 정렬

for i in range(len(profiles)):
    print(profiles[i][0], profiles[i][1])


# 등록하는 나이를 int형으로 바꿔주지 않으면 정렬 시 에러 발생