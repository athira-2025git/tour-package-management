from django.shortcuts import render
from .models import TourPackage

def package_list(request):
    packages = TourPackage.objects.filter(approved=True)
    return render(request, 'packages/package_list.html', {'packages': packages})
