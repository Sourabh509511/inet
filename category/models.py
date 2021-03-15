from django.db import models

# Create your models here.

class category(models.Model):
    id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=255)
    parent=models.ForeignKey("self", on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.category_name
    