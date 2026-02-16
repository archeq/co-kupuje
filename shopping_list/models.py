from django.db import models

# Create your models here.
class ShoppingList(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ShoppingItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_bought = models.BooleanField(default=False)