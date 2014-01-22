from django.db import models

class Group(models.Model):
	name = models.CharField(max_length = 50)
	captain = models.ForeignKey('Stud',verbose_name = 'Starosta')

	def __unicode__(self):
		return u"%s. %s" % (self.id,self.name)


	def get_absolute_url(self):
		return "/group/%i" % self.id

	def get_edit_url(self):
		return "group/edit/%i/" % self.id

class StudManager(models.Manager):
	def all(self):
		return super(StudManager,self).get_query_set().filter(is_removed = False)

class Stud(models.Model):
	Group = models.ForeignKey('Group',verbose_name = 'Gruppa',null = True,blank = True)
	name = models.CharField(max_length = 50)
	surname = models.CharField(verbose_name = 'Otchestvo',max_length = 50)
	name2 = models.CharField(verbose_name = 'Familia',max_length = 50)
	birth_date = models.DateField(('Birth_date'),
		help_text = "Please use the following format: <em>DD.MM.YYYY</em>.")
	ticket = models.CharField(verbose_name = 'number_bilet',max_length = 50)
	is_removed = models.BooleanField(verbose_name = 'is removed', default=False,)
	objects = StudManager()

	def __unicode__(self):
		return u"%s. %s %s, %s" % (self.id,self.name,self.surname,self.ticket)

	def get_absolute_url(self):
		return "student/%i/" % self.id

	def get_edit_url(self):
		return "student/edit/%i/" % self.id

	class Meta:
		verbose_name = 'Student'
		verbose_name_plural = 'Students'


# Create your models here.
