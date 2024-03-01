from django.db import models


class Message(models.Model):

    from_number = models.CharField(max_length=20)
    to_number = models.CharField(max_length=20)
    message_body = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.from_number}, To: {self.to_number}, Body: {self.message_body}"


class Number(models.Model):
    number = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)


class HomePageDesign(models.Model):
    introduction_header = models.CharField(max_length=100)
    introduction_body = models.CharField(max_length=1000)
