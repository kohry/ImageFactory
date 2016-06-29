from __future__ import unicode_literals

from django.db import models

# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

# class ImageExample(models.Model):
#     image = ProcessedImageField(
#         upload_to=('d:\imfactory\image'),
#         processors=[ResizeToFill(100, 50)],
#         format='JPEG',
#         options={'quality': 60}
#     )



# @python_2_unicode_compatible  # only if you need to support Python 2
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     
#     def __str__(self):
#         return self.question_text
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# 
# @python_2_unicode_compatible  # only if you need to support Python 2
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
# 
#     def __str__(self):
#     return self.choice_text
