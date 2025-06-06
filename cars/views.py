from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import CarForm
from django.contrib.auth.decorators import login_required

# Create your views here.



def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)


def search(request):
    cars = Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html', data)


@login_required
def car_create(request):
    if request.method == "POST":
        form = CarForm(request.POST,request.FILES)
        if form.is_valid():
            car= form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect("cars")
        
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html',{'form': form})

@login_required
def car_edit(request, car_id):
    car = get_object_or_404(Car,pk=car_id, user= request.user)
    if request.method == "POST":
        form= CarForm(request.POST,request.FILES,instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect("cars")
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html',{'form': form})

@login_required
def car_delete(request, car_id):
        car=get_object_or_404(Car,pk=car_id,user=request.user)
        if request.method == 'POST':
            car.delete()
            return redirect('cars')
        return render(request, 'cars/car_confirm_delete.html', {'car': car})
