from django.db import models
from django.contrib.auth.models import User
# from django.conf import settings
# import uuid

# def contact_default():
    # return {"email": "to1@example.com"}
# contact_info = JSONField("ContactInfo", default=contact_default)


class Skill(models.Model):
    value = models.CharField(max_length=90, unique=True)

    def __str__(self):
        return self.value


# https: //docs.djangoproject.com/en/3.1/ref/contrib/auth/ read this
class SoloProgramer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    skills = models.ManyToManyField(
        Skill,
        through='SoloProgSkill',
        through_fields=('programer', 'skill'),
    )

    contact_info = models.CharField(max_length=200, blank=True, null=True)  # TODO autoinit

    def first_name(self):
        return self.user.first_name

    def full_name(self):
        return self.user.get_full_name()

    def skill_list(self):
        return list(self.skills.all())

    def __str__(self):
        return f'{self.user.id} : {self.full_name()}'


class SoloProgSkill(models.Model):
    programer = models.ForeignKey(
        SoloProgramer,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'[{self.programer} {self.skill}]'


class Team(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        SoloProgramer,
        through='Membership',
        through_fields=('team', 'programer'),
    )

    def __str__(self):
        return f"{self.id} {self.name}"

    def member_list(self):
        return list(self.members.all())  #


class TeamSkill(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'[{self.team} {self.skill}]'


class Membership(models.Model):
    programer = models.ForeignKey(SoloProgramer, on_delete=models.CASCADE)
    access = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

