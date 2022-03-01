from django.shortcuts import render,redirect
from . models import Movie
from . models import Review 
from . forms import ReviewForm



def home(request):
    items = Movie.objects.all()
    context = {
        'items':items
    }
    return render(request, "movie/home.html",context)


def rate(request, id):
    post = Movie.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        author = request.POST.get('author')
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(author=author, stars = stars,  comment=comment , movie=post)
        review.save()
        return redirect('success')

    form = ReviewForm()
    context = {
        "form":form

    }
    return render(request, 'movie/rate.html',context)


def success(request):
    return render(request, "movie/success.html")
