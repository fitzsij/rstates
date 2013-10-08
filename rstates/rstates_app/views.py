from django.http import HttpResponse
from django.shortcuts import render_to_response
from rstates_app.models import Package



def showPackages(request):
	pkglist = Package.objects.all()
	return render_to_response('rstates_app/packages.html', {'packages':pkglist})