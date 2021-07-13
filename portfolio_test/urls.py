from django.urls import path
from portfolio_test.views import *

urlpatterns = [
    path('show', show_stock, name="show_stock"),
    path('show_all', show_all, name="show_all"),
    path('get_stocks', populate_stock_history, name='populate_stock_history')
]