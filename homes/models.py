from django.db import models


class Sido(models.Model):
    sido_name = models.CharField(max_length=20)
    sido_code = models.CharField(max_length=20)

    class Meta:
        verbose_name = '시도 코드'
        verbose_name_plural = '시도 코드'
        ordering = ['sido_code', ]

    def __str__(self):
        return self.sido_code + ' ' + self.sido_name


class Sigungu(models.Model):
    sido_code = models.ForeignKey(Sido, on_delete=models.CASCADE)
    sigungu_name = models.CharField(max_length=20)
    sigungu_code = models.CharField(max_length=20)

    class Meta:
        verbose_name = '시군구 코드'
        verbose_name_plural = '시군구 코드'
        ordering = ['sigungu_code', ]

    def __str__(self):
        return self.sigungu_code + ' ' + self.sigungu_name


class Home(models.Model):
    home_name = models.CharField(max_length=500)
    sido_code = models.ForeignKey(Sido, on_delete=models.CASCADE)
    sigungu_code = models.ForeignKey(Sigungu, on_delete=models.CASCADE)
    pttn_code = models.CharField(max_length=100)
    lt_sym_code = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    geo_lat = models.CharField(max_length=500)
    geo_lng = models.CharField(max_length=500)
    max_capacity = models.IntegerField(default=0)
    current_person = models.IntegerField(default=0)
    is_address_find_done = models.BooleanField(default=False)
    is_latlng_find_done = models.BooleanField(default=False)
    is_detail_find_done = models.BooleanField(default=False)
    created_date = models.DateTimeField('date created')
    updated_date = models.DateTimeField('date updated')

    class Meta:
        verbose_name = '양로원 정보'
        verbose_name_plural = '양로원 정보'
        ordering = ['created_date', ]

    def __str__(self):
        return self.home_name
