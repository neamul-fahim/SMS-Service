from django.db import models


class Number(models.Model):
    number = models.CharField(max_length=30)
    country = models.CharField(max_length=100, null=True, blank=True)
    country_flag_image = models.ImageField(
        upload_to='number_images/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number


class Message(models.Model):

    from_number = models.CharField(max_length=20)
    to_number = models.ForeignKey(
        Number, on_delete=models.CASCADE, related_name='received_messages')
    message_body = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.from_number}, To: {self.to_number}, Body: {self.message_body}"


class HomePageDesign(models.Model):
    introduction_header = models.CharField(max_length=100)
    introduction_body = models.CharField(max_length=1000)
