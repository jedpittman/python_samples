


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        students = []
        for i in range(int(f.readline().strip())):
            name = f.readline().strip()
            score = float(f.readline().strip())
            #print(name, score)
            students.append([name, score])
    max_score = max([s[1] for s in students])
    second_max = max(s[1] for s in students if s[1] != max_score)
    second_names = sorted([s[0] for s in students if s[1] == second_max])
    for n in second_names:
        print(n)    