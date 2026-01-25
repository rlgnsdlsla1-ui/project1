import sys  # 표준 입력을 읽기 위한 모듈 사용

data = sys.stdin.read().split()  # 입력 전체를 공백 기준으로 분리
caps = [int(data[0]), int(data[2]), int(data[4])]  # 각 양동이의 용량 저장
milk = [int(data[1]), int(data[3]), int(data[5])]  # 각 양동이의 현재 우유량 저장

for i in range(100):  # 총 100번 붓기 동작 반복
    a = i % 3  # 붓는 양동이 인덱스 계산
    b = (i + 1) % 3  # 받는 양동이 인덱스 계산
    space = caps[b] - milk[b]  # 받는 양동이의 남은 공간 계산
    poured = milk[a] if milk[a] < space else space  # 실제로 부을 수 있는 양 계산
    milk[a] -= poured  # 붓는 양동이에서 우유 감소
    milk[b] += poured  # 받는 양동이에 우유 증가

sys.stdout.write(f"{milk[0]}\n{milk[1]}\n{milk[2]}\n")  # 최종 우유량 출력
