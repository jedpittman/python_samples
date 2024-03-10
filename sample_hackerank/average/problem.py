"""Working with dictionaries and lists to calculate the average of a student's scores."""

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        n = int(f.readline().strip()
            
        student_marks = {}
        for _ in range(n):
            name, *line = f.readline().strip().split()
            scores = list(map(float, line))
            student_marks[name] = scores
            #print(name, scores)
        query_name = f.readline().strip()
        #print(query_name)
        print(f"{sum(student_marks[query_name])/len(student_marks[query_name]):.2f}")