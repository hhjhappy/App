from django.db import models

# Create your models here.

class Other(models.Model):
    Numbering = models.BigIntegerField('编号')
    applicationTime = models.DateField('申请时间',auto_now_add=True)
    theTerm = models.DateField('使用期限')
    finish = models.BooleanField('订单状态',default=False)
    Remarks = models.TextField('备注')
    companyName = models.CharField('所在单位',max_length=20)
    departmentName = models.CharField('所在部门',max_length=30)
    name = models.CharField('姓名',max_length=20)
    telephoneNumber = models.BigIntegerField('电话号码',null=True)
    phoneNumber = models.BigIntegerField('手机号码',null=True)
    mail = models.EmailField('邮箱地址',null=False)
    Type = models.CharField('资源类型', max_length=2)
    otherDevices = models.CharField('其他设备',max_length=2)
    typeRemark = models.CharField('资源类型备注',max_length=50,null=True)
    DevicesRemark = models.CharField('网络设备备注',max_length=50,null=True)


class backstage(models.Model):
    filesname = models.FileField('文件上传',upload_to='')
    link = models.OneToOneField(Other,on_delete=models.DO_NOTHING,null=True)

