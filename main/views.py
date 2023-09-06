from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Kevin Gilbert Sinaga',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
