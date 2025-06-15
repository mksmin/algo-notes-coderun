def main():
    print(*sorted(set(input().split()) & set(input().split()), key=int))


if __name__ == '__main__':
    main()