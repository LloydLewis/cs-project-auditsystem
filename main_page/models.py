from django.db import models
from django.contrib.auth.models import User

class Info(models.Model):
    
    name = models.CharField('Student Name', max_length = 100, blank = False)
    item = models.CharField('Item Name', max_length = 100, blank = False)
    deadline = models.DateField('Return Before', null= True, blank= True)
    borrow = models.DateField('Borrowed on', null= True, blank= True)
    status = models.CharField("Current Status", max_length = 20, blank = True )

    

    
    def __str__(self):
        return self.name

