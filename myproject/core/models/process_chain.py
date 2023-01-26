from django.db.models import Model, FloatField, Sum


class ProcessChain(Model):
    total_cost = FloatField(verbose_name="Total Cost", null=True, blank=True, default=0)

    def calculate_total_cost(self):
        '''
        > Gets all related process steps and sums up the cost field
        '''
        process_steps = self.process_steps.all()
        self.total_cost = process_steps.aggregate(Sum('cost'))['cost__sum']
        self.save()
