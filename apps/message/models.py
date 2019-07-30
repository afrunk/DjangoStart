from django.db import models

class UserMessage(models.Model):
    object_id = models.CharField(max_length=50,default="",primary_key=True,verbose_name=u"主键")
    name=models.CharField(max_length=50,verbose_name=u"用户名")
# max_length 最大长度 verbose_name   注释 u Unicode编码
    email=models.EmailField(verbose_name=u"邮箱")
    address=models.CharField(max_length=100,verbose_name=u"联系地址")
    message=models.CharField(max_length=500,verbose_name=u"留言信息")

    class Meta:
        verbose_name=u"用户留言信息"
    '''
    通过一个内嵌类 class Meta 给你的model 定义元数据
    他下面还会有许多的选项可供我们选择，
    如果我们不对其进行修改的话就是默认的继承
    '''
