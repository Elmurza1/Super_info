from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122, null=True)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()


class Category(models.Model):
    title = models.CharField(max_length=111)

    def __str__(self):

        return self.title



class Hashtag(models.Model):
    title = models.CharField(max_length=111)

    def __str__(self):

        return self.title


class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category',null=True)
    hashtags = models.ManyToManyField(Hashtag,  null=True)
    short_description = models.TextField()
    description = models.TextField()
    title = models.CharField(max_length=111)
    img = models.ImageField()
    data = models.DateField(null=True)
    is_activ = models.BooleanField(null=True)


class PublicationComment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    name = models.CharField(max_length=111)
    created_at = models.DateField(auto_now=True)











































































































































