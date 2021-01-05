def get_max(n):
    max_return = n[0]
    for i in range(1, len(n)):
        if n[i] > max_return:
            max_return = n[i]
        return max_return      