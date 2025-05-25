import pandas as pd
from django.core.management.base import BaseCommand
from main_page.models import Item  # Make sure this points to your actual app

class Command(BaseCommand):
    help = 'Import unique item names from Excel'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str)

    def handle(self, *args, **kwargs):
        filepath = kwargs['filepath']

        df = pd.read_excel(filepath, header=1)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df.columns = df.columns.str.strip().str.upper()

        required_columns = ['NAME OF THE PRODUCT', 'CATEGORY', 'QUANTITY', 'REMARKS']
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            self.stdout.write(self.style.ERROR(f"Missing columns: {missing}"))
            return

        for _, row in df.iterrows():
            name = str(row['NAME OF THE PRODUCT']).strip()
            category = str(row['CATEGORY']).strip()
            quantity = int(row['QUANTITY']) if not pd.isna(row['QUANTITY']) else 0
            remarks = str(row['REMARKS']).strip()

            item, created = Item.objects.update_or_create(
                name=name,
                defaults={
                    'category': category,
                    'quantity': quantity,
                    'remarks': remarks
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Created: {name}"))
            else:
                self.stdout.write(self.style.WARNING(f"🌀 Updated: {name}"))

