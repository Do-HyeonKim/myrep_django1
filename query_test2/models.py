from django.db import models

# total_query 모델 정의
class TotalQuery(models.Model):
    id = models.IntegerField(primary_key=True)
    query = models.CharField(max_length=255)

    class Meta : 
        # 테이블 이름을 mypost로 변경 
        db_table = 'queryTest'
