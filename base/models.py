from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

BRANCH_CHOICES= [
    ('COMPUTER SCIENCE AND ENGINEERING','Computer Science and Engineering'),
    ('ELECTRONICS ENGINEERING','Electronics Engineering'),
    ('ELECTRICAL ENGINEERING','Electrical Engineering'),
    ('MATHEMATICS AND COMPUTING','Mathematics and Computing'),
    ('MECHANICAL ENGINEERING','Mechanical Engineering'),
    ('CIVIL ENGINEERING','Civil Engineering'),
    ('CHEMICAL ENGINEERING','Chemical Engineering'),
    ('MINING ENGINEERING','Mining Engineering'),
    ('CEREMIC ENGINEERING','Ceremic Engineering'),
    ('ARCHITECTURE ENGINEERING','Architecture Engineering'),
    ('BIOCHEMICAL ENGINEERING','Biochemical Engineering'),
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

GENDER_CHOICES= [
    ('FEMALE','Female'),
    ('MALE','Male'),
    ('PREFER NOT TO SAY','Prefer Not To Say')
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=15, blank=True)
    branch = models.CharField(max_length=50, blank=True, choices= BRANCH_CHOICES)
    program = models.CharField(max_length=30, blank=True, choices= PROGRAM_CHOICES, default= 'B.Tech')
    year = models.PositiveIntegerField(null=True, blank=True, choices= YEAR_CHOICES, default= '1')
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=15, blank=True, choices= GENDER_CHOICES, default= 'Female')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()