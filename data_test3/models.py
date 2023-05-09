from django.db import models

# Create your models here.
class ColumnTable(models.Model):
    table_name = models.CharField(max_length=100 , null=True)
    column_en = models.CharField(max_length=100 ,  null=True)
    column_kr = models.CharField(max_length=100 ,  null=True)

    class Meta:
        db_table = 'column_table'