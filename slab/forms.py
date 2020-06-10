from django import forms
from . import models
import sys

class SlabDetailForm(forms.ModelForm):
    class Meta:
        model = models.SlabDetails
        fields = ("__all__")

class CommissionForm(forms.Form):
    class Meta:
        model = models.Commission
        fields = ("__all__")

class MakeCommissionForm(forms.ModelForm):
    class Meta:
        model = models.MakeCommission
        fields = ('dist_id', 'slab')

    def save(self):
        try:
            print("cleaned_data.....",self.cleaned_data)
            slab = self.cleaned_data['slab']
            dist_id = self.cleaned_data['dist_id']
            print(slab.id)

            di_comm = models.SetCommission.objects.get(slab_id = slab.id, commission_id = 2) ## Distributer
            mr_comm = models.SetCommission.objects.get(slab_id = slab.id, commission_id = 3) ## Marchent
            zr_comm = models.SetCommission.objects.get(slab_id = slab.id, commission_id = 1) ## Zrupee
            comm, is_created = models.MakeCommission.objects.get_or_create(slab=slab, dist_id=dist_id)
            if is_created:
                comm.marchent_comm = mr_comm
                comm.distributer_comm = di_comm
                comm.zrupee_comm = zr_comm
            print("Saving data...")
            comm.save()
            return comm
        except Exception as e:
            print("Error is saving data : ",e)
            print("Error at : {}".format(sys.exc_info()[-1].tb_lineno))
