from django.db import models


# Create your models here.
class BookModel(models.Model):
    bookName = models.CharField(max_length=20)
    startDate = models.DateTimeField()

    def __str__(self):
        return self.bookName


class BookRole(models.Model):
    roleName = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    book = models.ForeignKey('BookModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.roleName
