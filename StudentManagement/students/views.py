from django.shortcuts import render
from .models import Student
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'home.html')


def student_list(request):
    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'student_list.html', context)

def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form})
def add_student(request):
    return render(request, 'add_student.html')