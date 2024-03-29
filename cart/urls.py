from django.urls import path
from .views import cart_detail_view, add_to_cart_view, remove_from_cart,\
    clear_cart, add_to_favorites, favorites_list

app_name = 'cart'

urlpatterns = [
    path('cart_detail/', cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cart_view, name='add_to_cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('clear/', clear_cart, name='clear_cart'),
    path('favoriteAdd/<int:product_id>', add_to_favorites, name='add_to_favorites'),
    path('favoritelist/', favorites_list, name='favorites_list'),

]
