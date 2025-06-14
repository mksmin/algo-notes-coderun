import sys


def main():

    words = []
    count = {}

    for line in sys.stdin:
        word = line.strip().split()
        words.extend(word)

    lines = ''.join(words)
    for char in lines:
        if not count.get(char):
            count[char] = 0
        count[char] += 1

    chars = sorted(list(count.keys()))
    max_ = max(count.values())
    result = []


    for _ in range(max_):
        sub_result = []
        for i in chars:
            if count.get(i) <= 0:
                sub_result.append(" ")
            else:
                sub_result.append("#")
            count[i] -= 1

        result.append(sub_result)
    result_list = sorted(result)
    result_list.append(chars)
    for i in result_list:
        print(''.join(i))



if __name__ == '__main__':
    main()