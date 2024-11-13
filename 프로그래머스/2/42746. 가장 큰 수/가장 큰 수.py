def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_list = sorted(str_numbers, key=lambda x: x * 3, reverse=True)
    answer = ''
    for s in str_list:
        answer += s
    return answer if answer[0] != '0' else '0'