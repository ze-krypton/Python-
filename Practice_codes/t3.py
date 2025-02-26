# This is the scoring criteria: 
# - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# - Scores 71 - 80: Grade = "Acceptable" 
# - Scores 70 or lower: Grade = "Fail" 
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


student_grades={}
for student , scores in student_scores.items():
    if 91<=scores<=100:
        student_grades[student]="Outstanding"
    elif 81<=scores<=91:
        student_grades[student]="Exceeds Expectations"
    elif 71<=scores<=81:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"
    print(student_scores,": ",student_grades[student])
