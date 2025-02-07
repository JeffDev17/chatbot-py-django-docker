from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # 🔥 Renderiza a página "home.html"