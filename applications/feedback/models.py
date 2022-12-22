from django.db import models
from django.contrib.auth import get_user_model
from applications.product.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.owner
    


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    test = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.owner


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], blank=True, null=True
    )

    def __str__(self) -> str:
        return self.owner

class Favourite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favourites')
    like = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.owner
    
