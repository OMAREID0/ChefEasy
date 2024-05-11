from django.db import models

# Create your models here.
class Meal(models.Model):
    meal_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    cholesterol = models.IntegerField()
    ready_in_minutes = models.IntegerField()
    servings = models.IntegerField()
    ingredient = models.JSONField()
    image = models.ImageField(upload_to='images/')

