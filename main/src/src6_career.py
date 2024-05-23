def calculate_max_experience(levels):
    for i in range(len(levels) - 1, -1, -1):
        for j in range(len(levels[i])):
            current_value = levels[i][j]
            right_value = 0
            if i < len(levels) - 1:
                next_level = levels[i + 1]
                right_value = next_level[j + 1] if j + 1 < len(next_level) else 0
            levels[i][j] = current_value + max(levels[i + 1][j] if i < len(levels) - 1 else 0, right_value)
    return levels[0][0]

def main():
    with open("career.in", "r") as file:
        L = int(file.readline().strip())
        levels = []
        for _ in range(L):
            level = list(map(int, file.readline().strip().split()))
            levels.append(level)

    result = calculate_max_experience(levels)

    with open("career.out", "w") as file:
        file.write(str(result))

if __name__ == "__main__":
    main()