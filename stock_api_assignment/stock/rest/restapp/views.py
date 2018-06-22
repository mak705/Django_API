from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StockSerializer,UserSerializer
from .models import Stock
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
# Create your views here.
class StockViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Stock.objects.all().order_by('stock_gain')
    serializer_class = StockSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter)
    filter_fields = ('market_name',)
    search_fields = ('stock_name',)
    ordering = ('stock_gain',)


class Createuserview(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer
