from django.db import models
from django.contrib.auth import get_user_model

class Item(models.Model):
    CATEGORY = (
      ('Foundation', 'Foundation'),
      ('Concealer', 'Concealer'),
      ('Blush', 'Blush'),
      ('Eyeshadow', 'Eyeshadow'),
      ('Eyeliner', 'Eyeliner'),
      ('Lipstick', 'Lipstick'),
      ('Lipgloss', 'Lipgloss'),
      ('Other', 'Other')
    )
    name = models.CharField(max_length=50)
    photo = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    review = models.TextField(max_length=300)
    author = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE, null=True
  )
    created_or_updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name