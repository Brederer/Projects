from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class AD(models.Model):
    title = models.CharField('Название',max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг',help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='ads/', null=True, blank=True)
    
    
    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="font-weight: bold; color:green;">Сегодня в {} </span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')
    
    
    @admin.display(description='Дата последнего обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="font-weight: italic; color:blue;">Сегодня в {} </span>', created_time
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')
    
    
    @admin.display(description='Изображение')
    def picture(self):
        picture_url = self.image
        return format_html('<span>  </span>')
    
    @admin.display(description='Фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height= 80px;">',url=self.image.url
            )
    
    
    def __str__(self):
        return f"AD(id={self.id}, title={self.title}, price={self.price})"
    
    class Meta:
        db_table = "advertisements"    