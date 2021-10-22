from django.contrib import admin
from .models import Product
from .models import Category
from .models import ContactForm
from .models import Offers
from .models import NewArrivals
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ContactForm)
admin.site.register(NewArrivals)
admin.site.register(Offers)