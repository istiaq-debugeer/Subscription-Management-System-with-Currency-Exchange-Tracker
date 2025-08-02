from rest_framework import serializers
from .models import exchangeRate


class exchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = exchangeRate
        fields = ["id", "base_currency", "target_currency", "rate", "fetched_at"]
