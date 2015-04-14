from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    bio = models.TextField(default="")

    @property
    def name_abbrev(self):
        name = str(self)
        return name[:25] + "..." if len(name) > 28 else name

    @property
    def bio_abbrev(self):
        if self.bio:
            return self.bio[:30] + "..." if len(self.bio) > 33 else self.bio
        else:
            return "..."

    def __str__(self):
        return " ".join([self.first_name, self.last_name])
