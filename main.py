import sys  # 표준 입력을 빠르게 읽기 위한 모듈 사용

tokens = sys.stdin.buffer.read().split()  # 입력을 공백 기준으로 모두 분리
caps = [0, 0, 0]  # 각 양동이의 용량을 담을 리스트 준비
milk = [0, 0, 0]  # 각 양동이의 현재 우유량을 담을 리스트 준비

idx = 0  # 토큰 인덱스 초기화
for i in range(3):  # 3개의 양동이 정보를 순서대로 읽기
    caps[i] = int(tokens[idx])  # i번째 양동이의 용량 저장
    milk[i] = int(tokens[idx + 1])  # i번째 양동이의 우유량 저장
    idx += 2  # 다음 양동이 입력으로 이동

for step in range(100):  # 총 100번 붓기 동작 수행
    src = step % 3  # 붓는 양동이 인덱스 계산
    dst = (step + 1) % 3  # 받는 양동이 인덱스 계산
    space = caps[dst] - milk[dst]  # 받는 양동이의 남은 공간 계산
    move = milk[src] if milk[src] < space else space  # 실제로 옮길 수 있는 양 계산
    milk[src] -= move  # 붓는 양동이의 우유 감소
    milk[dst] += move  # 받는 양동이의 우유 증가

sys.stdout.write(f"{milk[0]}\n{milk[1]}\n{milk[2]}\n")  # 최종 우유량을 3줄로 출력
