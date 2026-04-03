from django.shortcuts import render
from .models import FinancialRecord
from .serializers import FinanceSerializer
from rest_framework.viewsets import ModelViewSet
from core.permissions import RecordPermission
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
import django_filters
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class DashboardView(APIView):
    def get(self, request):
        data = FinancialRecord.objects.all()
        income = data.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
        expense = data.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
        # serializer = FinanceSerializer(data, many=True)
        return Response({
            # "data": str(serializer.data)
            "total_income": income,
            "total_expense": expense,
            "net_balance": income - expense
        })


class FinancialRecordFilter(filters.FilterSet):
    class Meta:
        model = FinancialRecord
        fields = {
            'type': ['exact'],
            'category': ['exact', 'icontains'],
            'date': ['exact', 'gte', 'lte'],
            'amount': ['gte', 'lte'],
        }

class FinancialRecordViewSet(ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinanceSerializer
    permission_classes = [RecordPermission]
    filterset_class = FinancialRecordFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return FinancialRecord.objects.all()

        return FinancialRecord.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    @swagger_auto_schema(
        operation_description="List financial records with filters",
        manual_parameters=[
            openapi.Parameter('type', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('category', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('date_gte', openapi.IN_QUERY, type=openapi.FORMAT_DATE),
            openapi.Parameter('date_lte', openapi.IN_QUERY, type=openapi.FORMAT_DATE),
            openapi.Parameter('amount_gte', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
            openapi.Parameter('amount_lte', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

