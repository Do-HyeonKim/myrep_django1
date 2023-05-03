from django.db import models

# Create your models here.
class StatusModel(models.Model) :
    run_date = models.DateField(auto_now_add=True)
    reg_dtm = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0, null=True)
    last_timestamp = models.CharField(max_length=255,null=True)
    last_value = models.CharField(max_length = 255, null=True)
    last_file_name = models.CharField(max_length=255,null=True)

    class Meta:
        db_table = 'status'