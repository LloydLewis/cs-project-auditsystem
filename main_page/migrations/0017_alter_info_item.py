from django.db import migrations, models

def link_items(apps, schema_editor):
    Info = apps.get_model('main_page', 'Info')
    Item = apps.get_model('main_page', 'Item')
    for info in Info.objects.all():
        item_obj = Item.objects.get(name=info.item)
        info.item = item_obj
        info.save()

class Migration(migrations.Migration):

    dependencies = [
    ('main_page', '0016_alter_info_item')
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='item_new',
            field=models.ForeignKey(null=True, to='main_page.item', on_delete=models.CASCADE),
        ),
        migrations.RunPython(link_items),
        migrations.RemoveField(
            model_name='info',
            name='item',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='item_new',
            new_name='item',
        ),
    ]
