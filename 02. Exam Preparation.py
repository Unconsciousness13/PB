failed_treshold = int(input())
failed_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ""
has_failed = True
while failed_times < failed_treshold:
    problems_name = input()
    if problems_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems_count += 1
    last_problem = problems_name
if has_failed:
    print(f"You need a break, {failed_treshold} poor grades.")
else:
    print(f"Average score: {grades_sum / solved_problems_count:.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_problem}")
