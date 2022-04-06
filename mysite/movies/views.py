from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Movie,Theater,City
from .forms import BookingForm
from django.contrib.auth import authenticate

class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('Myadmin')
    template_name = 'movies/create_movie.html'


class MovieDetail(DetailView):
    model = Movie
    fields = '_all_'
    context_object_name = 'movie'
    template_name = 'movies/movie_detail.html'

class MovieUpdate(UpdateView):
    model = Movie
    fields = '__all__'
    # slug_field = 'slug'
    # slug_url_kwarg = 'slug'
    exclude = ['slug']
    success_url = reverse_lazy('Myadmin')
    template_name = 'movies/update_movie.html'

class MovieDelete(DeleteView):
    model = Movie
    fields = '__all__'
    exclude = 'slug'
    success_url = reverse_lazy('Myadmin')
    template_name = 'movies/delete_movie.html'

################################################### City Views ##########################################################
# class CityList(ListView):
#     model = City
#     fields = '__all__'
#     context_object_name = 'cities'
#     success_url = reverse_lazy('home')
#     template_name = 'app_users/index.html'


class CityCreate(CreateView):
    model = City
    fields = ['name']
    success_url = reverse_lazy('Myadmin')
    template_name = 'movies/create_city.html'


class CityDetail(DetailView):
    model = City
    fields = '_all_'
    context_object_name = 'city'
    template_name = 'movies/city_details.html'


class CityUpdate(UpdateView):
    model = City
    fields = '__all__'
    exclude = ['slug']
    success_url = reverse_lazy('Myadmin')
    template_name = 'movies/update_city.html'


class CityDelete(DeleteView):
    model = City
    fields = '__all__'
    exclude = 'slug'
    success_url = reverse_lazy('Myadmin')
    template_name = 'movies/delete_city.html'


#############################################################For theaters###############################################

# class TheaterList(ListView):
#     model = Theater
#     fields = '__all__'
#     context_object_name = 'theater'
#     success_url = reverse_lazy('home')
#     template_name = 'app_users/index.html'


class TheaterCreate(CreateView):
    model = Theater
    fields = '__all__'
    success_url = reverse_lazy('Myadmin')
    template_name = 'movies/create_theater.html'


class TheatherDetail(DetailView):
    model = Theater
    fields = '_all_'
    context_object_name = 'theater'
    template_name = 'movies/theater_detail.html'


class TheaterUpdate(UpdateView):
    model = Theater
    fields = '__all__'
    success_url = reverse_lazy('Myadmin')
    template_name = 'movies/update_theater.html'

class TheaterDelete(DeleteView):
    model = Theater
    fields = '__all__'
    exclude = 'slug'
    success_url = reverse_lazy('Myadmin')
    template_name = 'movies/delete_theater.html'

#Book Movie

def bookmovie(request,slug):
    if request.user.is_authenticated:
        form = BookingForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect('home')
        context = {'form':form}
        return render(request,'movies/book_movie.html',context)
    else:
        return redirect('login')

# def bookmovie(request,slug):
#     form = BookingForm(request.POST)
#     if request.method == "POST" and form.is_valid():
#         print("Saved2")
#         form.save()     
#         return redirect('home')
#     context = {'form':form}
#     return render(request,'movies/book_movie.html',context)


# def bookmovie(request,slug):
#     form = BookingForm()
#     if request.method == 'POST':
#         bookform = BookingForm(request.POST)
#         if bookform.is_valid():
#             print("Saved2")
#             form.save()            
#             return redirect('home')
#     context = {'form':form}
#     return render(request,'movies/book_movie.html',context)
    


# class BookingView(CreateView):
#     form = BookingForm()
#     model = Theater
#     fields = '__all__'
#     success_url = reverse_lazy('HomeView')
#     template_name = 'movies/book_movie.html'
