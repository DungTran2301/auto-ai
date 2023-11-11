from django.urls import path, include, re_path
from . import views
urlpatterns = [
  #   'ecomstore.catalog.views',
  # path(r'^$', 'index', { 'template_name':'catalog/index.html'}, 'catalog_home'),
  # path(r'^category/(?P<category_slug>[-\w]+)/$', 
  # 'show_category', {
  # 'template_name':'catalog/category.html'},'catalog_category'),
  # path(r'^product/(?P<product_slug>[-\w]+)/$', 
  # 'show_product', {
  # 'template_name':'catalog/product.html'},'catalog_product'),
  path("", views.classify, name='set'),
  # re_path(r'^setcard/detail/(?P<id>\d+)/$', views.show_card_by_set_id, name="detail"),
]