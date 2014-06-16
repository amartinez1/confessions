from django.db import models
from django.core.urlresolvers import reverse
from uuslug import uuslug


# Create your models here.
CATEGORIES=(('PO','popular'),('NE','new'))

class Post(models.Model):
	title = models.CharField( max_length=50,unique = False)
	text= models.TextField(default='')
	posted = models.DateTimeField(auto_now_add = True, editable= False)
	slug= models.SlugField(max_length=255,blank=True,default='')
	image = models.ImageField(upload_to="uploads", blank=True)
	total_likes=models.IntegerField( blank=True, default='0')
	category = models.CharField(blank = True, choices=CATEGORIES, max_length=2)

	def get_absolute_url(self):
		return reverse('detail',None, {'post_id':self.id})
	def save(self, *args, **kwargs):
		self.slug = uuslug(self.title, instance=self)
		super(Post, self).save(*args, **kwargs)
	def __unicode__(self):
		return unicode(self.title)
	class Meta:
		ordering = ["-posted", "title"]


