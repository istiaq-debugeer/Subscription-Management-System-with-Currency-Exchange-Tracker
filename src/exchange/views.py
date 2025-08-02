from rest_framework.viewsets import ModelViewSet

from .models import ExchangeRate
from .serializers import ExchangeRateSerializer
from .helpers import get_exchange_rates
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime


class ExchangeRateViewSet(ModelViewSet):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer


class ExchangeRateApiview(APIView):
    def get(self, request):
        base = request.GET.get("base", "USD")
        target = request.GET.get("target", "BDT")

        try:
            data = get_exchange_rates(base, target)
            if "error" in data:
                return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
            rate = data.get("rate")

            if rate:
                ExchangeRate.objects.create(
                    base_currency=base,
                    target_currency=target,
                    rate=rate,
                    fetched_at=datetime.now(),
                )
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
