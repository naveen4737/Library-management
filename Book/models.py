from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=122)
  ISBN = models.CharField(max_length=122)
  publication_date = models.DateField()

  def __str__(self):
    return self.title
