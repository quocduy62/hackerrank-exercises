avg_score = 0
student_marks = {}
for _ in range(int(input())):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for score in student_marks[query_name]:
    avg_score += score
avg_score /= 3
print("{:.2f}".format(avg_score))