from django.db import models


class AD(models.Model):
    title = models.CharField('Название',max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг',help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"AD(id={self.id}, title={self.title}, price={self.price})"
    
    class Meta:
        db_table = "advertisements"    