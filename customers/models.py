from django.db import models
from django.contrib.auth.models import User
from programers.models import Skill

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_info = models.CharField(max_length=100, default="customer_info")
    skills = models.ManyToManyField(
        Skill,
        through='CustomerSkill',
        through_fields=('customer', 'skill'),
    )
    def full_name(self):
        return self.user.get_full_name()
    def skill_list(self):
        return list(self.skills.all())
    def __str__(self):
        return str(self.user)

class CustomerSkill(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'[{self.customer} {self.skill}]'
