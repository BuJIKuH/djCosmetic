from django.db import models


class PartOfBodyModel(models.Model):
    """Таблица Части Тела"""
    name = models.CharField('Часть тела', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Часть тела"
        verbose_name_plural = "Части тела"


class ProblemsModel(models.Model):
    """Таблица проблемные моменты клиента с кожей, наименование "болезней" """
    name = models.CharField('Проблема', max_length=150)
    part_of_the_body = models.ForeignKey(PartOfBodyModel, verbose_name='Части тела', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проблема с кожей"
        verbose_name_plural = "Проблемы с кожей"


class MastersModel(models.Model):
    """Таблица Мастеров """
    second_name = models.CharField('Фамилия', max_length=20)
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Отчество', max_length=20)
    photo = models.ImageField('Картинка', upload_to='masters/%Y/%m/%d')
    speciality = models.CharField("Специальность", max_length=50)
    experience = models.DateField('Когда начало карьеры')
    slug = models.SlugField('Слаг', max_length=150)

    def __str__(self):
        return f"{self.second_name}-{self.first_name}-{self.first_name}"

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"


class ProceduresModels(models.Model):
    """Таблица Процедуры"""
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', max_length=5000)
    indications_for = models.TextField('Для кого подходит', max_length=1000)
    contraindications = models.TextField('Для кого не подходит', max_length=1000)
    problems = models.ForeignKey(ProblemsModel, verbose_name='Проблемы', on_delete=models.CASCADE)
    soviet_of_expert = models.TextField('Совет эксперта', max_length=1500)
    protocol = models.TextField('Протокол', max_length=3000)
    result = models.TextField('Результат', max_length=1000)
    price = models.PositiveIntegerField("Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"

