from django.db import models


# Create your models here.

class Goods(models.Model):
    name = models.CharField(max_length=30, verbose_name="商品名称")
    image = models.ImageField(upload_to="image/%Y/%m", default='image/default.png', max_length=100, verbose_name="商品图片")
    price = models.IntegerField(default=10, verbose_name="商品价格")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name
