from django.db import models


class exchangeRate(models.Model):
    base_currency = models.CharField(max_length=10)
    target_currency = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=20, decimal_places=6)
    fetched_at = models.DateTimeField()

    class Meta:
        unique_together = ("base_currency", "target_currency", "fetched_at")
        ordering = ["-fetched_at"]

    def __str__(self):
        return f"{self.base_currency} → {self.target_currency} @ {self.rate} on {self.fetched_at}"
