from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s: %s" % (self.date_added, self.title)


