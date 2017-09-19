from django.db import models

# Create your models here.

class host(models.Model):
    hostname=models.CharField(max_length=32,unique=True)
    key=models.TextField()
    status_choices=(
        (0, 'Waiting Approval'),
        (1, 'Accepted'),
        (2, 'Rejected'))
    os_type_choices=(
        ('redhat', 'Redhat\CentOS'),
        ('ubuntu', 'Ubuntu'),
        ('suse', 'Suse'),
        ('windows', 'Windows'),
    )
    os_type=models.CharField(choices=os_type_choices,max_length=64,default='Centos')
    status=models.SmallIntegerField(choices=status_choices,default=0)

    def __str__(self):
        return self.hostname
    class Meta:
        verbose_name="主机"
        verbose_name_plural="主机"

class hostGroup(models.Model):
    name=models.CharField(max_length=64,unique=True)
    hosts=models.ManyToManyField(host,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="主机组"
        verbose_name_plural="主机组"

























