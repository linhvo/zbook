from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    pv_id = models.IntegerField()
    tag_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)


class Review(models.Model):
    created_timestamp = models.BigIntegerField()
    created_by = models.ForeignKey(User)
    review_by = models.ForeignKey(User, related_name='assigned_reviews')
    pv_link = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    story_type = models.CharField(max_length=20)
    story_id = models.IntegerField()


