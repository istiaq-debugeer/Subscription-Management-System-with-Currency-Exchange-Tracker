from rest_framework import serializers
from .models import Plan, Subscription


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()

    class Meta:
        model = Subscription
        fields = "__all__"

    def create(self, validated_data):
        plan_data = validated_data.pop("plan")
        plan = Plan.objects.create(**plan_data)
        subscription = Subscription.objects.create(plan=plan, **validated_data)
        return subscription
