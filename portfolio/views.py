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

# from myapp.forms import ContactForm
# from django.views.generic.edit import FormView

# class ContactView(FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
#     success_url = ''

#     def form_valid(self, form):
#         form.send_email()
#         return super().form_valid(form)