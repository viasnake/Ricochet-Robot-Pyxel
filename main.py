def board_render():
    border = []
    i = 0
    board_raw = open("boards/0.txt", "r")
    lines = board_raw.readlines()
    for line in lines:
        print(line)
        border.append(line)
    board_raw.close()
    print(border)
    return

if __name__ == "__main__":
    board_render()