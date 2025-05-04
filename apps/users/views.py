# apps/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        # گرفتن داده‌ها از فرم
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # احراز هویت کاربر
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # ورود موفقیت‌آمیز
            login(request, user)
            next_url = request.POST.get('next', '/')
            return JsonResponse({'status': 'success', 'redirect_url': '/admin/'})

        else:
            # ورود ناموفق
            return JsonResponse({'status': 'error', 'message': 'نام کاربری یا رمز عبور اشتباه است.'})
    else:
        # نمایش صفحه ورود
        return render(request, 'users/log.html')


def user_logout(request):
    logout(request)
    return redirect('login')  # برگرده به صفحه لاگین
