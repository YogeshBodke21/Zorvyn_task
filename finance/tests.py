from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import FinancialRecord
from decimal import Decimal
from datetime import date

User = get_user_model()

class FinancialRecordModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_create_income_record(self):
        record = FinancialRecord.objects.create(
            user=self.user,
            amount=Decimal('100.50'),
            type='income',
            category='Salary',
            date=date.today(),
            notes='Monthly salary'
        )
        self.assertEqual(record.amount, Decimal('100.50'))
        self.assertEqual(record.type, 'income')
        self.assertEqual(record.category, 'Salary')
        self.assertEqual(record.notes, 'Monthly salary')
        self.assertEqual(record.user, self.user)

    def test_create_expense_record(self):
        record = FinancialRecord.objects.create(
            user=self.user,
            amount=Decimal('45.75'),
            type='expense',
            category='Groceries',
            date=date.today(),
            notes=''
        )
        self.assertEqual(record.type, 'expense')
        self.assertEqual(record.notes, '')  

    def test_type_choice_validation(self):
        # Trying to assign an invalid type should raise an error on full_clean
        record = FinancialRecord(
            user=self.user,
            amount=Decimal('20.00'),
            type='invalid_type', #this shd raise an exception as this is not valid
            category='Misc',
            date=date.today()
        )
        with self.assertRaises(Exception):
            record.full_clean()  

    def test_amount_max_digits_and_decimal_places(self):
        # max_digits=10, decimal_places=2
        record = FinancialRecord(
            user=self.user,
            amount=Decimal('12345678.90'),  # valid
            type='income',
            category='Bonus',
            date=date.today()
        )
        record.full_clean()  

        # Too many digits
        record.amount = Decimal('1234567890.12')  # 12 digits total
        with self.assertRaises(Exception):
            record.full_clean()

    def test_string_representation(self):
        record = FinancialRecord.objects.create(
            user=self.user,
            amount=Decimal('200.00'),
            type='income',
            category='Freelance',
            date=date.today()
        )
        expected_str = f"{record.user} - {record.type} - {record.amount}"
        print(expected_str)
        
        self.assertEqual(str(record), expected_str) # it checks whether you have defined __str__ in the model
