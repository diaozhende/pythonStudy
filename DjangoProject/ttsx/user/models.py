from django.db import models


# Create your models here.

class User(models.Model):
    uid = models.CharField(max_length=100, db_column='uid',primary_key=True)
    username = models.CharField(max_length=20, db_column='username')
    password = models.CharField(max_length=100, db_column='password')
    name = models.CharField(max_length=20, db_column='name')
    email = models.CharField(max_length=30, db_column='email')
    telephone = models.CharField(max_length=20, db_column='telephone')
    # birthday = models.DateTimeField()
    sex = models.CharField(max_length=10, db_column='sex')
    state = models.IntegerField(max_length=11, db_column='state')
    code = models.CharField(max_length=64, db_column='code')

    class Meta:
        db_table = 'user'
