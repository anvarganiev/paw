from django.db import models
from customers.models import Customer
from chats.models import Chat
from programers.models import Skill
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def inrange_validator(a: int, b: int):
    def validator(value):
        if value < a or value >= b:
            raise ValidationError(
                _('%(value)s is not valid'), params={'value': value},)
    return validator


def min_validator(a: int):
    def validator(value):
        if value < a:
            raise ValidationError(
                _('%(value)s is not valid'), params={'value': value},)
    return validator


class Project(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.IntegerField(null=True, blank=True)

    title = models.CharField(max_length=128)

    sal_low = models.FloatField(validators=[min_validator(0)])
    sal_high = models.FloatField(validators=[min_validator(0)])

    status = models.IntegerField(default=0)
    
    auction_date = models.DateField()
    files = models.FileField()
    chat_id = models.ForeignKey(Chat, on_delete=models.PROTECT, null=True)
    customer_review = models.TextField(null=True, blank=True)
    rating = models.IntegerField(
        validators=[inrange_validator(1, 6)], 
        blank=True, 
        null=True
    )
    result_files = models.FileField(null=True, blank=True)
    additional_fixes_finances = models.BinaryField(default=False)
    skills = models.ManyToManyField(
        Skill,
        through='ProjectSkills',
        through_fields=('project', 'skill')
    )
    is_team = models.BooleanField(default=False)

    def required_skills(self):
        return list(self.skills.all())


class ProjectSkills(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
