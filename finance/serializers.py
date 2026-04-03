from rest_framework import serializers
from .models import FinancialRecord
from django.utils import timezone

class FinanceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = FinancialRecord
        fields = '__all__'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('Amount must be Positive.')
        return value
    def validate_type(self, value):
        if value not in ['income', 'expense']:
            raise serializers.ValidationError("Type must be either 'income' or 'expense'.")
        return value

    def validate_category(self, value):
        if not value.strip():
            raise serializers.ValidationError("Category cannot be empty.")
        return value

    def validate_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Date cannot be in the future.")
        return value

    # Object-level validation (optional)
    def validate(self, data):
        if data['type'] == 'expense' and data['amount'] > 100000:
            raise serializers.ValidationError(
                "Expense amount seems too large. Please verify."
            )
        return data