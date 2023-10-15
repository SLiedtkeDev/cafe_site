from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.CharField(max_length=100, verbose_name='Descripcion')
    order = models.IntegerField(verbose_name='Orden de presentacion')
    active = models.BooleanField(verbose_name='Activo', default=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
        ordering = ['order']

    def __str__(self) -> str:
        return self.title


class Food(models.Model):
    menu = models.ForeignKey(Menu, verbose_name='Menu',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Alimento')
    description = models.CharField(max_length=100, verbose_name='Description')
    cost = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name='Costo')
    previous_cost = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name='Costo Previo', null=True, blank=True)
    recommended = models.BooleanField(
        verbose_name="Recomendado", default=False)
    order = models.IntegerField(verbose_name='Orden de presentacion')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimento'
        ordering = ['order']

    def __str__(self) -> str:
        return self.name
