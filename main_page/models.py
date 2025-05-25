from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Info(models.Model):
    name = models.CharField('Student Name', max_length=100)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, blank=False, null=True)


    deadline = models.DateField('Return Before', null=True, blank=True)
    borrow = models.DateField('Borrowed on', null=True, blank=True)
    status = models.CharField("Current Status", max_length=20, blank=True)

    def __str__(self):
        return self.name
