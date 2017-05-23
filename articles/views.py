# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Articles

# Create your views here.
def index(request):
	total = Articles.objects.all().count()
	articles = Articles.objects.all()
	paginator = Paginator(articles, 2) # Show 25 contacts per page
	
	page = request.GET.get('page')
	try:
		latest_articles = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		latest_articles = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		latest_articles = paginator.page(paginator.num_pages)

	context = {'latest_articles': latest_articles, 'total': total, 'latest_articles': latest_articles}
	return render(request, 'index.html', context)


def capacitorsizing(request):
	context = {'path': capacitorsizing}
	return render(request, 'capacitor.html', context)

def systemstudy(request):
	context = {'path': capacitorsizing}
	return render(request, 'capacitor.html', context)

def transformersizing(request):
	context = {'path': capacitorsizing}
	return render(request, 'transformer.html', context)		