from django.contrib import admin
from .models import Movie,Wishlist
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=[
        "userid",
        "title",
        "description",
        "category",
        "image",
        "video",
        "age_limit",

    ]

class WishlistAdmin(admin.ModelAdmin):
    list_display=[
        "userid",
        "movieid",
    ]


admin.site.register(Movie,MovieAdmin)
admin.site.register(Wishlist,WishlistAdmin)
