from django.shortcuts import render

# Create your views here.
def index(request,user_id):
	return render(request,'owner.html')
