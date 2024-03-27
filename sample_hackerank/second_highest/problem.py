"""minor bit of code that given the input should return the second to lowest score in the list of students."""


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        students = []
        for i in range(int(f.readline().strip())):
            name = f.readline().strip()
            score = float(f.readline().strip())
            #print(name, score)
            students.append([name, score])
    min_score = min([s[1] for s in students])
    second_min = min(s[1] for s in students if s[1] != min_score)
    second_names = sorted([s[0] for s in students if s[1] == second_min])
    for n in second_names:
        print(n)    