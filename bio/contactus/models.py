from django.db import migrations, models

class ContactUs(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=45)
    message = models.TextField()

    def __str__(self):
        return self.first_name