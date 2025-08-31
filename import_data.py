import os
import django
import xlrd

# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grade_query_system.settings')
django.setup()

from students.models import Student, Grade

def import_data_from_excel(file_path):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)

    # 假设你的表头如下：[学号, 姓名, 科目1, 科目2, ...]
    header = sheet.row_values(0)
    course = header[2:]  # 第三列开始是各科成绩

    for row_idx in range(1, sheet.nrows):
        row = sheet.row_values(row_idx)
        student_id = str(row[0]).strip()
        name = str(row[1]).strip()

        if not student_id or not name:
            continue  # 跳过空行

        # 创建学生
        student, _ = Student.objects.get_or_create(student_id=student_id, name=name)

        # 创建成绩
        for subject_idx, subject in enumerate(course):
            score_val = row[2 + subject_idx]
            try:
                score = float(score_val)
            except:
                continue  # 跳过无法解析的分数

            Grade.objects.update_or_create(
                student=student,
                course=course,
                defaults={'score': score}
            )

    print("数据导入完成")

if __name__ == "__main__":
    import_data_from_excel("students_grade.xls")