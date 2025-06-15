def main():
    t_room, t_cond = list(map(int, input().split()))
    mode = input().strip()

    if mode == "fan":
        print(t_room)

    if mode == "auto":
        print(t_cond)

    if mode == "heat":
        print(max(t_cond, t_room))

    if mode == "freeze":
        print(min(t_cond, t_room))


if __name__ == '__main__':
    main()
