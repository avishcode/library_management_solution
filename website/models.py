from django.db import models
from membership.models import Membership, StudyRoom
# Create your models here.

class Lead(models.Model):
    lead_id = models.AutoField(primary_key=True)
    lead_name = models.CharField(max_length=100)
    lead_phone = models.CharField(max_length=15)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lead_name
    



