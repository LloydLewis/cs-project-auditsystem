from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Info
from .forms import InfoForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'main_page/home.html')

def all_info(request): #Extracts information from database
    binfo = Info.objects.all() 
    return render(request, 'main_page/borrow_info.html',
                  {'binfo': binfo})

def add_info(request): #View to add info
    submitted = False # Used to keep track of whether the user has submitted a form or not
    if request.method == 'POST':
        form = InfoForm(request.POST) # Pass the value into the form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/home/add_info?submitted =True') # Submits the form, saves into databse, redirects user back
    else:
        form = InfoForm
        if 'submitted' in request.GET:
            submitted = True #If form submitted, sets to True
            messages.success(request, ('Details have been submitted'))

    
    return render(request, 'main_page/add_info.html', {'form': form, 'submitted': submitted})

def search(request):
    if request.method == 'POST':
         searched = request.POST['searched']
         records = Info.objects.filter(name__contains = searched)
         return render(request, 'main_page/search.html', {'searched': searched, 'records': records})
    else:
        return render(request, 'main_page/search.html', {})
    
def info_list(request):
    records = Info.objects.all()
    return render(request, 'info_list.html', {'records': records})

@csrf_exempt
def delete_record(request, record_id):
    if request.method == 'DELETE':
        try:
            record = Info.objects.get(pk=record_id)
            record.delete()
            return JsonResponse({'success': True})
        except Info.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Record not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)

