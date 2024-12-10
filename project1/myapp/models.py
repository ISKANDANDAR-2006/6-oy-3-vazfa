from django.db import models

# krs klasi ------------------------------------------------------------------------------------
class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Kurs tavsifi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")



    def __str__(self):
        return self.title

# student clasi ----------------------------------------------------------------------------


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Talaba ismi")
    email = models.EmailField(verbose_name="Email manzil")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro‘yxatdan o‘tgan vaqti")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students", verbose_name="Kurs")

    def __str__(self):
        return self.name

