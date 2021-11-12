from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.student.id, filename)

BRANCH_CHOICES= [
    ('ARCHITECTURE ENGINEERING','Architecture Engineering'),
    ('BIOCHEMICAL ENGINEERING','Biochemical Engineering'),
    ('CEREMIC ENGINEERING','Ceremic Engineering'),
    ('CHEMICAL ENGINEERING','Chemical Engineering'),
    ('CIVIL ENGINEERING','Civil Engineering'),
    ('COMPUTER SCIENCE AND ENGINEERING','Computer Science and Engineering'),
    ('ELECTRICAL ENGINEERING','Electrical Engineering'),
    ('ELECTRONICS ENGINEERING','Electronics Engineering'),
    ('ENGINEERING PHYSICS','Engineering Physics'),
    ('INDUSTRIAL CHEMISTRY ENGINEERING','Industry Chemistry Engineering'),
    ('MATERIAL SCIENCE AND ENGINEERING','Material Science and Engineering'),
    ('MATHEMATICS AND COMPUTING','Mathematics and Computing'),
    ('MECHANICAL ENGINEERING','Mechanical Engineering'),
    ('METALLURGY ENGINEERING','Metallurgy Engineering'),
    ('MINING ENGINEERING','Mining Engineering'),
    ('PHARMACEUTICAL ENGINEERING','Pharmaceutical Engineering'),
    ]

PROGRAM_CHOICES= [
    ('B.TECH','B.Tech'),
    ('IDD','IDD'),
    ('M.TECH','M.Tech'),
    ('PhD','PhD'),
]


YEAR_CHOICES= [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
]

DOSE_TAKEN= [
    (1,1),
    (2,2),
]

VACCINE_NAME= [
    ('COVAXIN','Covaxin'),
    ('COVISHIELD','Covishield'),
    ('SPUTNIK','Sputnik')
]

GENDER_CHOICES= [
    ('FEMALE','Female'),
    ('MALE','Male'),
    ('PREFER NOT TO SAY','Prefer Not To Say')
]

NOTIF_CHOICES= [
    ('info','info'),
    ('success','success'),
    ('error','error')
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=15, blank=True)
    branch = models.CharField(max_length=50, blank=True, choices= BRANCH_CHOICES)
    program = models.CharField(max_length=30, blank=True, choices= PROGRAM_CHOICES, default= 'B.Tech')
    year = models.PositiveIntegerField(null=True, blank=True, choices= YEAR_CHOICES, default= 1)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=15, blank=True, choices= GENDER_CHOICES, default= 'Female')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        VaccDetails.objects.create(student=instance)
        CovidHistory.objects.create(student1=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()      

class VaccDetails(models.Model):
    student = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    reference_id = models.CharField(max_length=30, blank=True)
    vaccine_name = models.CharField(max_length=15, blank=True, choices= VACCINE_NAME)
    dose_taken = models.PositiveIntegerField(null=True, blank=True, choices= DOSE_TAKEN)
    date1 = models.DateField(null=True, blank=True)
    date2 = models.DateField(null=True, blank=True) 
    certificate = models.FileField(null=True, blank=True, upload_to=user_directory_path)  

class CovidHistory(models.Model):
    student1 = models.ForeignKey(User, related_name='student1', on_delete=models.CASCADE)
    infected = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)

class Notifications(models.Model):
    student2 = models.ForeignKey(User, related_name='student2', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    option = models.CharField(max_length=15, blank=True, choices= NOTIF_CHOICES)
    date_notif = models.DateTimeField(null=True, blank=True)
