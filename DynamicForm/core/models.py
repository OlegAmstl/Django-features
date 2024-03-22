from django.db import models


class Contact(models.Model):
    """"
    Модель контакта.
    """

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name
