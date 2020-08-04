from django.db import models
from django.utils import timezone
import datetime


class Comment(models.Model):
    Owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, null=True)
    Title = models.CharField(max_length=200)
    Pub_date = models.DateTimeField('date published', auto_now_add=True)
    Emb_html = models.CharField(max_length=2024, null=True, blank=True)
    Content = models.TextField(default='Empty')
    File = models.FileField(upload_to='media/uploads/', default='media/None/', null=True, blank=True)
    Image = models.ImageField(upload_to='media/pic_folder', default='media/None/no-img.jpg')
    Ip_log = models.GenericIPAddressField(null=True)
    User_agent = models.CharField(max_length=200,null=True)

    def image_tag(self):
        return mark_safe('<img src="/polls/pic_folder/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.Title

    def was_published_recently(self):
        return self.Pub_date >= timezone.now() - datetime.timedelta(days=1)



