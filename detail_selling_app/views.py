from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from allauth.account.views import LoginView, LogoutView
from .models import Cars, Categories, Seller
from .forms import AddYourCar
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.db import transaction
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SellerSignUpForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# @login_required
def home(request):
    all_categories = Categories.objects.all()
    return render(request, 'home.html', {
        'categories':all_categories
    })

def categories(request, id):
    selected_category = get_object_or_404(Categories, id=id)
    cars_in_category = Cars.objects.filter(category=selected_category)
    
    return render(request, 'category.html', {
        "category": selected_category,
        "cars": cars_in_category  
    })

class AddCarView(LoginRequiredMixin, CreateView):
    model = Cars
    form_class = AddYourCar
    template_name = 'sell.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_seller_profile'] = hasattr(self.request.user, 'seller')
        return context

    def form_valid(self, form):
        if not hasattr(self.request.user, 'seller'):
            seller, created = Seller.objects.get_or_create(
                user=self.request.user,
                defaults={  
                    'name': self.request.user.username,
                    'phonenumber': 'Not provided',
                    'address': 'Not provided'
                }
            )
        
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)



class Login(LoginView):
    template_name = 'account/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class SellerSignUpView(FormView):
    template_name = 'account/signup.html'
    form_class = SellerSignUpForm
    success_url = reverse_lazy('home')

    @transaction.atomic
    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
        )

        Seller.objects.create(
            user=user,
            phonenumber=form.cleaned_data['phonenumber'],
            address=form.cleaned_data.get('address', ''),
        )

        login(
            self.request,
            user,
            backend="django.contrib.auth.backends.ModelBackend"
        )

        return redirect(self.success_url)


class Logout(LogoutView):
    template_name = 'account/logout.html'
    success_url = '/home/'

def search(request):
    searched = request.POST.get('searched')
    results = Cars.objects.filter(name__icontains=searched)
    return render(request, 'search_results.html', {
        'results': results
    })

def profile(request):
    return render(request, "profile.html")

def cars(request):
    cars = Cars.objects.all()
    categories = Categories.objects.all()
    return render(request, "products.html",{
        'all_cars': cars,
        'categories': categories,
        })

def car_details(request, slug):
    # selected = next(car for car in Cars.objects.all() if car.slug ==slug)
    selected = get_object_or_404(Cars, slug=slug)
    return render(request, "car_details.html",{
        'car': selected,
    })

@require_POST
def add_to_cart(request, car_id):
    car = get_object_or_404(Cars, id=car_id)
    cart = request.session.get('cart', {})
    car_id_str = str(car.id)

    if car_id_str in cart:
        cart[car_id_str]['qty'] += 1
    else:
        cart[car_id_str] = {
            'name': car.name,
            'price': car.price,
            'qty': 1,
            'image': car.image.url if car.image else '',
        }

    request.session['cart'] = cart
    request.session.modified = True

    messages.success(request, f"{car.name} added to cart")
    return redirect(request.META.get('HTTP_REFERER', 'products'))


def cart_view(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['qty'] for item in cart.values())

    return render(request, 'cart.html', {
        'cart': cart,
        'total': total
    })

@login_required
@require_POST
def toggle_like(request, car_id):
    car = get_object_or_404(Cars, id=car_id)
    seller = request.user.seller

    if car in seller.liked_cars.all():
        seller.liked_cars.remove(car)
        messages.info(request, f"{car.name} removed from liked")
    else:
        seller.liked_cars.add(car)
        messages.success(request, f"{car.name} added to liked")

    return redirect(request.META.get('HTTP_REFERER', 'products'))

@login_required
def liked_cars_view(request):
    liked_cars = request.user.seller.liked_cars.all()
    return render(request, 'liked_cars.html', {
        'liked_cars': liked_cars
    })

class CustomPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_email.html' 
    success_url = '/account/password-reset-done/'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = '/account/password-reset-complete/'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'