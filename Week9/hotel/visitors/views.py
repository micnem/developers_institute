from django.shortcuts import render, redirect
from django.views.generic import ListView
from hotel.models import Review
from .forms import AddReview, MakeBooking

# Create your views here.
class ReviewList(ListView):
    model =  Review
    context_object_name = 'review_list'
    template_name = 'reviews.html'


def home(request):
    return render(request, 'homepage.html')

def book(request):
    form = MakeBooking()
    if request.method == "POST":
        form = MakeBooking(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'book.html', {'form':form})

def add_review(request):
    form = AddReview()
    if request.method == "POST":
        form = AddReview(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reviews')
    return render(request, 'addreview.html', {'form':form})


def review(request, id):
    review = Review.objects.get(id=id)

    return render(request, 'review.html', {'review':review})