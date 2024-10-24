import sys

vowels = ["a", "e", "i", "o", "u"]
consonants = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in vowels]

while True:
    word = sys.stdin.readline().strip()
    if word == 'end':
        break

    word_lst = list(word)

    if all(w not in vowels for w in word_lst):
        print(f"<{word}> is not acceptable.")
    else:
        is_acceptable = True
        for i in range(len(word_lst) - 1):
            if word_lst[i + 1] == word_lst[i] and word_lst[i] not in ["e", "o"]:
                is_acceptable = False
                print(f"<{word}> is not acceptable.")
                break
        if is_acceptable:
            for i in range(len(word_lst) - 2):
                if (word_lst[i] in vowels and word_lst[i + 1] in vowels and word_lst[i + 2] in vowels) or (
                        word_lst[i] in consonants and word_lst[i + 1] in consonants and word_lst[i + 2] in consonants):
                    is_acceptable = False
                    print(f"<{word}> is not acceptable.")
                    continue
        if is_acceptable:
            print(f"<{word}> is acceptable.")