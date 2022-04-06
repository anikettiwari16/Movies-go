from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from .forms import CreateUserForm, UserProfileForm
from django.contrib import messages
from movies.models import Movie,City,Theater
from django.contrib.auth import authenticate, login, logout
# Create your views here.

#Register Function
# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         user_form = CreateUserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)
#     if request.method =='POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid:
#             form.save()
#             user = form.cleaned_data['username']
#             messages.success(request,'Account was created for ' + user)

#             return redirect('login')
#     context = {'form' : form}
#     return render (request, 'app_users/register.html',context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        registered = False
    if request.method == "POST":
        user_form = CreateUserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return redirect('login')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = CreateUserForm()
        profile_form = UserProfileForm()
    return render(request, 'app_users/register.html',
                  {'registered': registered,
                   'user_form': user_form,
                   'profile_form': profile_form})

#logout Function
def logoutUser(request):
    logout(request)
    return redirect('home')


#Login Function
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Invalid Username Or Password')

        context = {}
        return render (request, 'app_users/login.html',context)

#Homepage Function
# def home(request):
#     return render (request, 'app_users/index.html')

class HomeView(TemplateView):
    template_name = 'app_users/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = Movie.objects.all()
        context['movies'] = movies 
        return context

class AdminView(TemplateView):
    template_name = 'app_users/admin_panel.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # getting all the models form movies app to show in admin panel for admin edit
        movies = Movie.objects.all()
        cities = City.objects.all()
        theaters = Theater.objects.all()
        context['movies'] = movies
        context['cities'] = cities
        context['theaters'] = theaters
        return context