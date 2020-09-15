from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Ebook (models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=60)
    description = models.TextField()
    publication_date = models.DateField()

    #Metadata
    class Meta :
        ordering = ['id']

    #Methods
    def __str__(self):
        return self.title



class Review (models.Model):
    review_author = models.CharField(max_length=20, help_text='Enter field documentation')
    review = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name='reviews')

    #Metadata
    class Meta :
        ordering = ['id']

    #Methods
    def __str__(self):
        return f"{self.rating}"
