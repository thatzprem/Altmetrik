from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):

    identifier = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=250,null=True,blank=True)
    content = models.CharField(max_length=100, null=True, blank=True)            
    author_name  = models.CharField(max_length=100, null=True, blank=True)
    up_votes = models.PositiveIntegerField(null=True, blank=True)

    created = models.DateTimeField(null=True, blank=True, editable=False)
    modified = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Article, self).save(*args, **kwargs)
    
    def __repr__(self):
        return '<Article: ({0}, {1})>'.format(self.id, self.identifier)
    
    def __unicode__(self):
        return unicode(self.__repr__())
