import collections
import sys

n, w, l = map(int, sys.stdin.readline().split())  # 트럭수, 다리 길이, 최대 하중
trucks = collections.deque(list(map(int, sys.stdin.readline().split())))

bridge = collections.deque([0] * w)
cnt = 0
current_sum = 0

while bridge:
    cnt += 1
    current_sum -= bridge.popleft()
    if trucks:
        if current_sum + trucks[0] <= l:
            new_truck = trucks.popleft()
            bridge.append(new_truck)
            current_sum += new_truck
        else:
            bridge.append(0)
print(cnt)