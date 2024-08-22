from django.shortcuts import render
from django.http import HttpResponse
from .models import My

# Create your views here.
def home(request):
    return render(request,'index.html')

def home2(request):
    if 'name' in request.POST and 'contact_no' in request.POST and 'address' in request.POST and 'books' in request.POST and 'amount' in request.POST and 'noofbooks' in request.POST:
        name = request.POST['name']
        contact_no = request.POST['contact_no']
        address = request.POST['address']
        books = request.POST['books']
        amount = request.POST['amount']
        noofbook = request.POST['noofbook']

        var = My(name=name, contact_no=contact_no, address=address, books=books, amount=amount, noofbook=noofbook)
        var.save()

        return render(request, 'result.html', {
            "name": name,
            "contact_no": contact_no,
            "address": address,
            "books": books,
            "amount": amount,
            "noofbook": noofbook
        })
    else:
        # Handle the case where one or more keys are missing in the request.POST
        return HttpResponse("One or more required fields are missing.")
