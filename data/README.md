# Kaggle: Student Performances
```bash
!wget -O student_performance.csv https://raw.githubusercontent.com/bhishanpdl/Shared/master/data/students_performance.csv
```
```python
ifile = 'student_performance.csv'
df = pd.read_csv(ifile)
print(df.shape)
df.head()

 gender race/ethnicity parental level of education         lunch  \
0  female        group B           bachelor's degree      standard   
1  female        group C                some college      standard   
2  female        group B             master's degree      standard   
3    male        group A          associate's degree  free/reduced   
4    male        group C                some college      standard   

  test preparation course  math score  reading score  writing score  
0                    none          72             72             74  
1               completed          69             90             88  
2                    none          90             95             93  
3                    none          47             57             44  
4                    none          76             78             75
```
- https://pub.towardsai.net/3-best-often-better-alternatives-to-histograms-b588f3850ce8
