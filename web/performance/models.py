# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Performance(models.Model):
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
    genre = models.CharField(max_length=255)
    state = models.CharField(max_length=20)
    price = models.CharField(max_length=255)
    crew = models.CharField(max_length=255)
    cast = models.CharField(max_length=255)
    story = models.TextField()
    enterprise_p = models.CharField(max_length=255)
    enterprise_a = models.CharField(max_length=255)
    enterprise_h = models.CharField(max_length=255)
    enterprise_s = models.CharField(max_length=255)
    seats = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'performance'


class PerformanceDatetime(models.Model):
    id = models.BigAutoField(primary_key=True)
    performance_id = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'performance_datetime'


class PerformancePerson(models.Model):
    id = models.BigAutoField(primary_key=True)
    performance_id = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'performance_person'


class PerformancePrice(models.Model):
    id = models.BigAutoField(primary_key=True)
    performance_id = models.CharField(max_length=20)
    price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'performance_price'
