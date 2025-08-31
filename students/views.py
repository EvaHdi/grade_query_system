from django.shortcuts import render
from .models import Student, Grade

def query_view(request):
    student = None
    grades = []
    student_id = request.GET.get("student_id")

    if student_id:
        try:
            student = Student.objects.get(student_id=student_id)
            grades = Grade.objects.filter(student=student)
        except Student.DoesNotExist:
            student = None

    return render(request, "students/query.html", {
        "student": student,
        "grades": grades,
        "student_id": student_id or "",
    })