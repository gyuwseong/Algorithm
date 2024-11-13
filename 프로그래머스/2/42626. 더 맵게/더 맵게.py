import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while scoville[0] < K:
        if len(scoville) >= 2:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, (first + (second * 2)))
            answer += 1
        else:
            return -1

    return answer