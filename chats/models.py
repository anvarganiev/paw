from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    title = models.CharField(max_length=120, default="new chat")

    members = models.ManyToManyField(
        User,
        through='Membership',
        through_fields=('chat', 'member'),
    )

    def __str__(self):
        return f"{self.id} {self.title}"

    def member_list(self):
        return list(self.members.all())


class Membership(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    access = models.IntegerField(default=0)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.chat}] {self.member}"


class ChatLine(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    status = models.IntegerField(default=0)
    line = models.CharField(max_length=300)
