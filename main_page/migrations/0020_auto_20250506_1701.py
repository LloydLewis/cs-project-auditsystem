from django.db import migrations

def migrate_items_to_fk(apps, schema_editor):
    Info = apps.get_model('main_page', 'Info')
    Item = apps.get_model('main_page', 'Item')

    for info in Info.objects.all():
        if isinstance(info.item, str):
            item_name = info.item.strip()
            if item_name:
                item_obj, _ = Item.objects.get_or_create(name=item_name)
                info.item = item_obj
                info.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0019_alter_info_item'),  # adjust as needed
    ]

    operations = [
        migrations.RunPython(migrate_items_to_fk),
    ]
