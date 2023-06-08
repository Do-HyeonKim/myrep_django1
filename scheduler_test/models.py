from django.db import models

# Create your models here.
class AppInfoModel(models.Model) :
    app_name = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    save_dir = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    start_date =  models.TextField(null=True, blank=True)

    
    class Meta:
        db_table = 'app_info'

class AppDownloadLogModel(models.Model) :
    app_name = models.TextField(null=True, blank=True)
    start_date = models.TextField(null=True, blank=True)
    end_date = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    reg_dtm = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'app_download_log'