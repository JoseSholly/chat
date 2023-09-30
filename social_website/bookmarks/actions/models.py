from django.db import models

# Create your models here.


class Actions(models.Model):
    user= models.ForeignKey('auth.user',
                            related_name='actions',
                            on_delete=models.CASCADE,)
    verb= models.CharField(max_length=225)
    created= models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes= [
            models.Index(fields=['-created'])
        ]

        ordering= ['-created']
