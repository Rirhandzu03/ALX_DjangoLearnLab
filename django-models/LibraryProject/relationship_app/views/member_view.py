from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_member(user):
    return user.userprofilr.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_page.html')