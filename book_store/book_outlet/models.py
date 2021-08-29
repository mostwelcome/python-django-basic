from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="book")
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, blank=True)  # Harry Potter 1 -> harry-potter-1

    def __str__(self):
        return f'{self.title} {self.rating}'

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
