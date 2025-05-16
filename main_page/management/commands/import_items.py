import pandas as pd
from django.core.management.base import BaseCommand
from main_page.models import Item  # Make sure this points to your actual app

class Command(BaseCommand):
    help = 'Import unique item names from Excel'

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str)

    def handle(self, *args, **kwargs):
        filepath = kwargs['filepath']

        # Read from second row (row index 1) and drop unnamed columns
        df = pd.read_excel(filepath, header=1)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        column = 'NAME OF THE PRODUCT'
        if column not in df.columns:
            self.stdout.write(self.style.ERROR(f"Column '{column}' not found. Available columns: {df.columns.tolist()}"))
            return

        for name in df[column].dropna().unique():
            item, created = Item.objects.get_or_create(name=name.strip())
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added: {name}"))
            else:
                self.stdout.write(f"Already exists: {name}")
