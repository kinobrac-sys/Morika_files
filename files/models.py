from django.db import models

# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=255)
    main_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)


