'''
Program to display student percentage scores
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    selected_scores=student_marks[query_name]
    print(selected_scores)
    size=len(selected_scores)
    sum_of_scores=sum(selected_scores)
    print(sum_of_scores)
    average=(sum_of_scores/size)
    final_output="{:.2f}".format(average)
    print(final_output)
