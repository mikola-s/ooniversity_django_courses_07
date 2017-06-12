from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'
#def detail(request, pk):
#    course = get_object_or_404(Course, pk=pk)
#    context = {'course': course}
#    return render (request, 'courses/detail.html', context)

def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print(instance)
            messages.success(request, "Lesson %s has been successfully added."%instance.subject)
            return redirect ('courses:detail', course.id)       
    else:
        form = LessonModelForm(initial = {'course': course})   
    context = {'form': form}
    return render (request, 'courses/add_lesson.html', context)

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'
    context_object_name = 'course'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,"Course {} has been successfully added.".format(self.object.name))
        return response
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title':"Course creation",})
        return context
#def add(request):
#    if request.method == "POST":
#        form = CourseModelForm(request.POST)
#        if form.is_valid():
#            instance = form.save()
#            print(instance)
#            messages.success(request, "Course %s has been successfully added."%instance.name)
#            return redirect ('index')       
#    else:
#        form = CourseModelForm()   
#    context = {'form': form}
#    return render (request, 'courses/add.html', context)


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'
    context_object_name = 'course'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "The changes have been saved.")
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title':"Course update",})
        return context

    def get_success_url(self):
        success_url = reverse_lazy('courses:edit',
                                   kwargs={"pk":self.object.id})
        return success_url
#def edit(request, pk):
#    course = Course.objects.get(id=pk)
#    if request.method == "POST":
#        form = CourseModelForm(request.POST, instance=course)
#        if form.is_valid():
#            course = form.save()
#            messages.success(request, "The changes have been saved.")
#            return redirect ('courses:edit', course.id)       
#    else:
#        form = CourseModelForm(instance=course)   
#    context = {'form': form}
#    return render (request, 'courses/edit.html', context)

class CourseDeleteView(DeleteView):
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    def delete(self, request, *args, **kwargs):
        response = super().delete( request, *args, **kwargs)
        messages.success(self.request,
                         "Course {} has been deleted.".format(self.object.name))
        return response
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context
#def remove(request, pk):
#    course = Course.objects.get(id=pk)
#    if request.method == "POST":
#        course.delete()
#        messages.success(request, "Course %s has been deleted."%course.name)
#        return redirect ('index')
#    print(redirect ('index'))
#    context = {'course': course}
#    return render (request, 'courses/remove.html', context)


# Create your views here.
