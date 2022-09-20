from django.db import models
from datetime import datetime
# Create your models here.
from ckeditor.fields import RichTextField


class Cover_Photo(models.Model):
    class Meta:
        verbose_name_plural = 'Cover Photo'
    Title1 = models.CharField(max_length=255)
    Title2 = models.CharField(max_length=255)
    cover_photo = models.ImageField(upload_to='cover_photo/')

    def __str__(self):
        return self.Title1


class About(models.Model):
    class Meta:
        verbose_name_plural = 'About'
    Name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    Description = RichTextField(blank=True, null=True)
    Happy_Clients = models.IntegerField()
    Projects = models.IntegerField()
    Years_of_experience = models.IntegerField()
    Awards = models.IntegerField()
    def __str__(self):
        return self.Name


class Skills(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
    Title = models.CharField(max_length=255)
    expertise_percentage = models.IntegerField()
    def __str__(self):
        return self.Title



class Resume(models.Model):
    class Meta:
        verbose_name_plural = 'Resume'
    Text = RichTextField(blank=True, null=True)



class Services(models.Model):
    class Meta:
        verbose_name_plural = 'Services'
    Name = models.CharField(max_length=255)
    Short_Description = models.CharField(max_length=255)
    def __str__(self):
        return self.Name



class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio'
    Name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    Protfolio_Link = models.TextField()
    def __str__(self):
        return self.Name




class Testimonials(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials'
    Name = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    Feedback = models.TextField()
    def __str__(self):
        return self.Name



class Contact_Us_Form(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Us'
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Message = models.TextField()
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.Name