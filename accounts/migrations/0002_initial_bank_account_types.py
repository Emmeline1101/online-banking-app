from django.db import migrations
from accounts.constants import INTEREST_CALCULATION_CHOICES

def create_bank_account_types(apps, schema_editor):
    BankAccountType = apps.get_model('accounts', 'BankAccountType')
    BankAccountType.objects.create(
        name='Savings Account',
        maximum_withdrawal_amount=50000,
        annual_interest_rate=0.05,
        interest_calculation_per_year=INTEREST_CALCULATION_CHOICES[0][0]  
    )
    BankAccountType.objects.create(
        name='Current Account',
        maximum_withdrawal_amount=100000,
        annual_interest_rate=0.05,
        interest_calculation_per_year=INTEREST_CALCULATION_CHOICES[0][0]  
    )

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_bank_account_types),
    ]