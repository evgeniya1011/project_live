from django.db import models

NULLABLE = {"blank": True, "null": True}

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="порода")
    description = models.TextField(verbose_name="Описание", **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "порода"
        verbose_name_plural = "породы"

class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name="Кличка")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Порода")
    image = models.ImageField(upload_to="dogs/", verbose_name="Изображение", **NULLABLE)
    birthday = models.DateField(verbose_name="Дата рождения", **NULLABLE)

    def __str__(self):
        return f"{self.name} {self.category}"

    class Meta:
        verbose_name = "собака"
        verbose_name_plural = "собаки"

