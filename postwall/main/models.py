from django.db import models
# from django.contrib.auth.admin import User
from django.contrib.auth.models import User
from datetime import datetime
from jsonfield import JSONField
from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize= value.size
    if filesize > 5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value

class Post(models.Model): 
    createDate = models.DateTimeField(auto_now_add=True )
    owner      = models.ForeignKey(User,on_delete=models.CASCADE)
    pic        = models.ImageField(upload_to='post_pictures/', blank=True, verbose_name="", validators=[validate_file_size])
    content    = models.TextField(default="")
    num_like   = models.IntegerField(default=0)
    likes      = JSONField(null=True, default={})
    comments   = JSONField(null=True, default={})


