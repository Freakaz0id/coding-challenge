from django.db.models import Model, FloatField, ForeignKey, CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from .process_chain import ProcessChain


class ProcessStep(Model):
    process_chain = ForeignKey(ProcessChain, on_delete=CASCADE, verbose_name="Process Chain", related_name="process_steps")  # The process chain can query all process steps using the related_name
    cost = FloatField(verbose_name="Cost", null=True, blank=True, default=0)

# Call this function after a process chain is saved
@receiver(post_save, sender=ProcessStep)
def update_total_cost(sender, instance, **kwargs):
    instance.process_chain.calculate_total_cost()
