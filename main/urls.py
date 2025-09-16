from django.urls import path
from .views import (
    show_main,
    create_product,
    show_product,
    show_json, show_json_by_id,
    show_xml, show_xml_by_id,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('json/', show_json, name='show_json'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
]
