import pandas as pd

students_information=pd.read_csv('students.txt' )

class_students=students_information.groupby('class')

mean_score=class_students['score'].mean()
print(mean_score)

gender_students=students_information.groupby('gender')

boy_highest_score=gender_students.get_group('남')['score'].max()
girl_highest_score=gender_students.get_group('여')['score'].max()

print(boy_highest_score)
print(girl_highest_score)

print(class_students.size())
