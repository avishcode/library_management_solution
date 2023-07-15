from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class StudyRoom(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=100)
    room_description = models.CharField(max_length=200,blank=True, null=True)
    total_no_of_seats = models.IntegerField(blank=True, null=True)
    seat_occupied = models.IntegerField(blank=True, null=True)
    seat_vacant = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_name
    
    def seat_vacant(self):
        pass


PLAN_TYPE = (
    ('FOUR_HOURS', 'Four_Hours'),
    ('HALF_DAY', 'Half_Day'),
    ('FULL_DAY', 'Full_Day'),
)


class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    plan = models.CharField(choices=PLAN_TYPE, max_length=100)
    membership_name = models.CharField(max_length=100)
    membership_description = models.CharField(max_length=200)
    membership_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.membership_name


PAYMENT_MODE = (
    ('CASH', 'Cash'),
    ('UPI', 'upi'),
)



class EnrollStudent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    room = models.ForeignKey(StudyRoom, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name