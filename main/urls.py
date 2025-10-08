from django.urls import path
from .views import (
    show_main,
    create_product,
    show_product,
    show_json, show_json_by_id,
    show_xml, show_xml_by_id,
    register, login_user, logout_user,
    edit_product, delete_product,
    add_product_entry_ajax
)

app_name = 'main'

urlpatterns = [
    # Main Page
    path('', show_main, name='show_main'),

    # CRUD Product
    path('create-product/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('product/<uuid:id>/edit/', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete/', delete_product, name='delete_product'),

    # AJAX
    path("create-product-ajax/", add_product_entry_ajax, name="add_product_entry_ajax"),
    

    # Data Endpoints
    path('json/', show_json, name='show_json'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),

    # Auth
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
