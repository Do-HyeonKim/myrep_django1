from django.db import models

# total_query 모델 정의
class QueryModel(models.Model):
    id = models.IntegerField(primary_key=True)
    query = models.CharField(max_length=255)

    class Meta : 
        db_table = 'query'
