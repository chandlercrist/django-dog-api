from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Breed(models.Model):
    class Size(models.TextChoices):
        TINY = "Tiny"
        SMALL = "Small"
        MEDIUM = "Medium"
        LARGE = "Large"

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=6, choices=Size.choices)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['id']
        constraints = [models.CheckConstraint(condition=models.Q(**{f'{field}__gte': 1, f'{field}__lte': 5}), name=f'breed_{field}_range') for field in ['friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']]
        constraints += [models.CheckConstraint(condition=models.Q(size__in=['Tiny', 'Small', 'Medium', 'Large']), name='breed_valid_size')]

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT, related_name='dogs')
    gender = models.CharField(max_length=30)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']
        constraints = [models.CheckConstraint(condition=models.Q(age__gte=0), name='dog_nonnegative_age')]

    def __str__(self):
        return self.name
