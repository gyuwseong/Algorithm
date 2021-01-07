def solution(arr):
  result = []
  for i in range(len(arr)):
    if arr[i] not in result:
        result.append(arr[i])
    else:
        return i - arr.index(arr[i])
    if len(result) == len(arr):
        return -1