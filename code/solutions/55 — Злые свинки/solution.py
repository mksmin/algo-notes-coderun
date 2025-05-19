def main():
    n = int(input())
    result = set()
    for _ in range(n):
        x, y = list(map(int, input().split()))
        result.add(x)

    print(len(result))


if __name__ == '__main__':
    main()