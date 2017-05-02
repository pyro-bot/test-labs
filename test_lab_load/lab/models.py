from django.db import models

# Create your models here.
class People(models.Model):
    fio=models.CharField(max_length=255)
    sex=models.CharField(max_length=1)
    age=models.IntegerField()

    def __str__(self):
        return 'ФИО:%s Пол:%s Возраст:%s'%(self.fio,self.sex,self.age)