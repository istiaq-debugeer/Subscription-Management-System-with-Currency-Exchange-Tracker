
from rest_framework.viewsets import ModelViewSet
# from .models import ExchangeRate
# from .serializers import ExchangeRateSerializer
from .helpers import get_exchange_rates
from django.http import JsonResponse


# class ExchangeRateViewSet(ModelViewSet):
#     queryset = ExchangeRate.objects.all()
#     serializer_class = ExchangeRateSerializer


def exchange_rates_api(request):
    data = get_exchange_rates()
    return JsonResponse(data)