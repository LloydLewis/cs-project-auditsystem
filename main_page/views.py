from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Info, Item
from .forms import InfoForm, ItemForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from main_page.models import Item
from django.forms import modelformset_factory

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



def item_search(request):
    term = request.GET.get('term', '')
    items = Item.objects.filter(name__icontains=term)[:10]
    results = [{'id': item.id, 'text': item.name} for item in items]
    return JsonResponse({'results': results})

def manage_items(request):
    items = Item.objects.all()
    return render(request, 'main_page/manage_items.html', {'items': items})

@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity') or 0
        remarks = request.POST.get('remarks') or ''
        item = Item.objects.create(name=name, category=category, quantity=quantity, remarks=remarks)
        return JsonResponse({'id': item.id, 'name': item.name})

@csrf_exempt
def edit_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        item.name = request.POST.get('name')
        item.category = request.POST.get('category')
        item.quantity = request.POST.get('quantity') or 0
        item.remarks = request.POST.get('remarks') or ''
        item.save()
        return JsonResponse({'success': True})

@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        item.delete()
        return JsonResponse({'success': True})