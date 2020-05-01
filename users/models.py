from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from boofilsic.settings import REPORT_MEDIA_PATH_ROOT, DEFAULT_PASSWORD


def report_image_path(instance, filename):
    raise NotImplementedError("UUID!!!!!!!!!!!")
    root = ''
    if REPORT_MEDIA_PATH_ROOT.endswith('/'):
        root = REPORT_MEDIA_PATH_ROOT
    else:
        root = REPORT_MEDIA_PATH_ROOT + '/'
    return root + datetime.now().strftime('%Y/%m/%d') + f'{filename}'


class User(AbstractUser):
    mastodon_id = models.IntegerField()

    def save(self, *args, **kwargs):
        """ Automatically populate password field with DEFAULT_PASSWORD before saving."""
        self.set_password(DEFAULT_PASSWORD)
        return super().save(*args, **kwargs)


class Report(models.Model):
    submit_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='sumbitted_reports', null=True)
    reported_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='accused_reports', null=True)
    image = models.ImageField(upload_to=report_image_path, height_field=None, width_field=None, max_length=None, blank=True, default='')
    is_read = models.BooleanField(default=False)
    submitted_time = models.DateTimeField(auto_now_add=True)



