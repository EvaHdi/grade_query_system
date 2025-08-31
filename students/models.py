from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)  # 学号
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  # 初始密码设为学号本身

    def __str__(self):
        return f"{self.student_id} - {self.name}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    score = models.FloatField()

    def __str__(self):
        return f"{self.student.name} - {self.course}: {self.score}"