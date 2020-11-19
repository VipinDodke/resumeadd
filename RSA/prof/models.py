from django.db import models

# Create your models here.
class profile(models.Model):
    profile_id = models.AutoField
    name = models.CharField(max_length=50)
    ct_date= models.DateField()
    pro_img= models.ImageField(upload_to="prof/images",default="")
    def __str__(self):
        return self.name