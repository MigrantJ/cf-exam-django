from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return " ".join([self.first_name, self.last_name])
