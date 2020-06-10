from django.db import models
import random
# Create your models here.

class SlabDetails(models.Model):
    slab = models.CharField(max_length=22)
    slab_amount = models.FloatField(default=0.0)

    class Meta:
        db_table = "slab_details"

    def __str__(self):
        return self.slab

class Commission(models.Model):
    commission = models.CharField(max_length=35)

    class Meta:
        db_table = "commission"

    def __str__(self):
        return self.commission

class SetCommission(models.Model):
    slab = models.ForeignKey("SlabDetails", on_delete=models.CASCADE)
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    share = models.FloatField(default=0.0)

    class Meta:
        db_table = "set_commission"
    def __str__(self):
        return self.slab.slab

class Distributers(models.Model):
    dist_id = models.IntegerField(default=random.randrange(999,99999))
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "distributers"
    def __str__(self):
        return self.dist_name

class MakeCommission(models.Model):
    dist_id = models.IntegerField(unique=True, default=random.randrange(999,99999))
    slab = models.ForeignKey(SlabDetails, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    marchent_comm = models.ForeignKey(SetCommission, on_delete=models.SET_NULL, null=True, related_name="marchent_comm")
    distributer_comm = models.ForeignKey(SetCommission, on_delete=models.SET_NULL, null=True, related_name="distributer_comm")
    zrupee_comm = models.ForeignKey(SetCommission, on_delete=models.SET_NULL, null=True, related_name="zrupee_comm")
    tr_amount = models.FloatField(default=0.0)

    gst = models.CharField(max_length=55, default="0")
    tds = models.CharField(max_length=22, null=True, blank=True)
    cust_fee = models.FloatField(default=0.0)

    class Meta:
        db_table = "make_commission"

    def __str__(self):
        return str(self.dist_id)
