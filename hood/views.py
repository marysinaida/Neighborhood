from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Neighborhood, Business
from django.contrib.auth.decorators import login_required
from .forms import NewNeighborhoodForm
import datetime as dt

# Create your views here.


def index(request):
    neighbor = Neighborhood.objects.all()
    return render(request, 'index.html', {'neighbor': neighbor})


@login_required(login_url='/accounts/login/')
def neighborhood(request, neighborhood_id):
    try:
        neighborhood = Neighborhood.objects.get(id=neighborhood_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "neighborhood.html", {"neighborhood": neighborhood})


@login_required(login_url='/accounts/login/')
def new_neighbor(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.name = current_user
            neighborhood.save()
        return redirect('index')


def hood(request, id):
    hoods = Neighborhood.objects.get(id=id)
    bus = hoods.business_set.all
    posts = hoods.post_set.all
    return render(request, 'hood.html', {'hoods': hoods, 'bus': bus, 'posts': posts})

    
def news_of_day(request):
    date = dt.date.today()

    return render(request, 'all-news/today-news.html', {"date": date, })


def past_days_news(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html', {"date": date})


def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_bName(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def add_post(request, id):
    current_user = request.user
    hoods = Neighborhood.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            addpost = form.save(commit=False)
            post.hood = hoods
            addpost.user = current_user
            addpost.save()
        return redirect('hood', hoods.id)
    else:
        form = PostForm()
        return render(request, 'new_post.html', {"form": form, 'hood': hoods})
