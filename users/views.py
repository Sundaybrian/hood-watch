from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('login')
    else:

        form=UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})    

@login_required
def profile(request):
    '''
    view function for a user profile
    '''

    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,f'Account has been updated')

            return redirect('profile')

    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'usr_form':user_form,
        'prof_form':profile_form
    }    



    return render(request,'users/profile.html',context)



