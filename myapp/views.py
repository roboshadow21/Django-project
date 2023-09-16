import logging
import datetime
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import EditProductForm, ImageForm
from .models import User, Product, Order

logger = logging.getLogger(__name__)

html = """<h1>Hello!</h1>
<br>
<h2>This is the page about the my first django project</h2>
<br>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolores eum expedita itaque laudantium mollitia, 
sit suscipit tempore. Neque obcaecati repudiandae vero! Ab alias aperiam atque blanditiis cupiditate, et fuga 
harum inventore, ipsam ipsum iste magni maiores nam necessitatibus nulla perferendis praesentium quibusdam quos 
repudiandae similique sit tenetur voluptas voluptate voluptates.</p>
"""

html2 = """<h1>This is the page about me</h1>
<br>
<h2>My name is Alex and i am the developer of this website</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolores eum expedita itaque laudantium mollitia, 
sit suscipit tempore. Neque obcaecati repudiandae vero! Ab alias aperiam atque blanditiis cupiditate, et fuga 
harum inventore, ipsam ipsum iste magni maiores nam necessitatibus nulla perferendis praesentium quibusdam quos 
repudiandae similique sit tenetur voluptas voluptate voluptates.</p>
"""


def index(request):
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')
    return HttpResponse(html2)


def get_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.all()
    my_dict = {}
    for i in range(len(orders)):
        my_dict[orders[i]] = orders[i].products.all()
    return render(request, 'myapp/orders.html', {'user': user, 'my_dict': my_dict})


def get_sorted_orders(request, user_id, days):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.all()
    my_dict = {}
    date_now = datetime.datetime.today()
    date_past = date_now - datetime.timedelta(days=days)
    for i in range(len(orders)):
        date = orders[i].ordered_at
        if date_past < date.replace(tzinfo=None) < date_now:
            my_dict[orders[i]] = orders[i].products.all()
    return render(request, 'myapp/orders_sorted.html', {'user': user, 'my_dict': my_dict, 'days': days})

def upload_image(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)

    else:
        form = ImageForm()
    return render(request, 'myapp/upload_image.html', {'form': form})


def edit_product(request):
    if request.method == 'POST':
        form = EditProductForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            prod_id = form.cleaned_data['prod_id']
            price = form.cleaned_data['price']
            logger.info(f'Getting {name=}, {prod_id=}, {price=}.')
            product = Product.objects.filter(pk=prod_id).first()
            product.name = name
            product.price = price
            product.save()
            message = f'Товар {name}, цена: {price}'
    else:
        form = EditProductForm()
        message = 'Заполните форму'
    return render(request, 'myapp/edit_product.html', {'form': form, 'message': message})

