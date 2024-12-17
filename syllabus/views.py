# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import FileResponse
from .models import Syllabus, SyllabusCategory
from .forms import SyllabusUploadForm
from django.contrib import messages

def syllabus_list(request):
    syllabi = Syllabus.objects.filter(is_active=True)  # Only active syllabi
    return render(request, 'syllabus/syllabus_list.html', {'syllabi': syllabi})


def syllabus_by_category(request, category_id):
    category = get_object_or_404(SyllabusCategory, id=category_id)
    syllabi = category.syllabuses.filter(is_active=True)
    return render(request, 'syllabus/category.html', {
        'category': category,
        'syllabi': syllabi,
    })


def syllabus_view(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, id=syllabus_id, is_active=True)
    return render(request, 'syllabus/view.html', {
        'syllabus': syllabus
    })

def download_syllabus(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, id=syllabus_id, is_active=True)
    syllabus.download_count += 1
    syllabus.save(update_fields=['download_count'])  # Update the count
    response = FileResponse(syllabus.file, as_attachment=True)
    return response


@staff_member_required
def upload_syllabus(request):
    if request.method == 'POST':
        form = SyllabusUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Syllabus uploaded successfully!')
            return redirect('syllabus_list')
    else:
        form = SyllabusUploadForm()
    
    return render(request, 'syllabus/upload.html', {'form': form})