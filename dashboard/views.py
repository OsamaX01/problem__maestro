from django.shortcuts import render

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "dashboard/guest.html")
    
    return render(request, "dashboard/user_dashboard.html")