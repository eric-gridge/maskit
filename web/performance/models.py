# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime

from django.db import models
# from django.db.backends.mysql.base import DatabaseWrapper
# DatabaseWrapper.data_types['DateTimeField'] = datetime


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    performance_id = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    faculty_id = models.CharField(max_length=20)
    faculty_name = models.CharField(max_length=255)
    age = models.IntegerField()
    age_detail = models.CharField(max_length=255)
    date_from = models.CharField(max_length=20)
    date_to = models.CharField(max_length=20)
    date_detail = models.CharField(max_length=255)
    time = models.TextField()
    poster = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    daehakro = models.CharField(max_length=2)
    genre = models.CharField(max_length=255)
    state = models.CharField(max_length=20)
    price = models.CharField(max_length=255)
    crew = models.CharField(max_length=255)
    cast = models.CharField(max_length=255)
    story = models.TextField()
    host = models.CharField(max_length=255)
    plan = models.CharField(max_length=255)
    seats = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    # # def save(self, *args, **kwargs):
    #     self.created_at = datetime.now()
    #     self.updated_at = datetime.now()
    #     return super(Item, self).save(*args, **kwargs)


class Datetime(models.Model):
    id = models.BigAutoField(primary_key=True)
    performance = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="performance_datetime")
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    # def save(self, *args, **kwargs):
    #     self.created_at = datetime.now()
    #     self.updated_at = datetime.now()
    #     return super(Datetime, self).save(*args, **kwargs)


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    performance = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="performance_person")
    name = models.CharField(max_length=255)
    chosung = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    # def save(self, *args, **kwargs):
    #     self.created_at = datetime.now()
    #     self.updated_at = datetime.now()
    #     return super(Person, self).save(*args, **kwargs)


class Price(models.Model):
    id = models.BigAutoField(primary_key=True)
    performance = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="performance_price")
    price = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    # def save(self, *args, **kwargs):
    #     self.created_at = datetime.now()
    #     self.updated_at = datetime.now()
    #     return super(Price, self).save(*args, **kwargs)


class Faculty(models.Model):
    id = models.BigAutoField(primary_key=True)
    faculty_id = models.CharField(max_length=20)
    faculty_name = models.CharField(max_length=255)
    area = models.CharField(max_length=20)
    seatscale = models.IntegerField()
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
