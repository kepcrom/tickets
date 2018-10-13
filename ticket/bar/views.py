from django.shortcuts import render
from bar.forms import BarForm
from bar.models import Bar
from member.models import MemberProfile

# Create your views here.
def create(request):
    edit_form = BarForm()
    return render(request, 'bar/edit.html',{'edit_form':edit_form})

def save(request):
    number = request.POST.get("Number")
    summary = request.POST.get("Summary")
    creator = MemberProfile.objects.filter(user=request.user)[0]

    bar_form = BarForm(data={'Number':number,'Summary':summary,'Creator':creator})

    if bar_form.is_valid():
        bar_form.save()

    return render(request, 'bar/edit.html',{'edit_form':bar_form})
