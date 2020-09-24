# from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Portfolio
from .serializers import PortfolioSerializer


# Create your views here.
class PortfolioView(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_classs = PortfolioSerializer

class ContactCreate(CreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
