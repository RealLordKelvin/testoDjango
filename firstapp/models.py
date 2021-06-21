from django.db import models


class FlowFile(models.Model):
    mpan = models.CharField(max_length=13)
    meter_id = models.CharField(max_length=20)
    meter_registration_id = models.CharField(max_length=3)
    reading_date_time = models.CharField(max_length=20)
    reading_register = models.CharField(max_length=20)
    file_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ["mpan", "meter_id", "file_name"]
    
