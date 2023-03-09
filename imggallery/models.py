from django.db import models

# Create your models here.
def uplode_path(instance,filename):
    print(filename)
    return '/'.join(['images',str(instance.title),filename])
class Gallery(models.Model):
    title = models.CharField(max_length=250,blank=False)
    img = models.ImageField(blank=True,null=True,upload_to=uplode_path)

    class Meta:
        db_table = 'gallery'