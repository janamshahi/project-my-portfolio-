# from django.db import models

# class TestModel(models.Model):
#     name = models.CharField(max_length=50)
# email Testmodel(models.Model):
#     name = models.CharField(max_length=50)
    
from django.db import models

class Testmodel(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)  # store hashed password ideally
    

    def __str__(self):
        return self.username