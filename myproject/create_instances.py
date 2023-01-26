import os
import random

import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()
from core.models import ProcessChain, ProcessStep

# Create process chain
process_chain = ProcessChain.objects.create()

# Create 5 random process steps
for i in range(5):
    process_step = ProcessStep(
        process_chain = process_chain,
        cost = random.uniform(0.00, 10.00)
    )
    process_step.save()
    print(f"{i+1}ProcessStep created. Cost: {process_step.cost:.2f}")
print(f"\nProcessChain created. Total Cost: {process_chain.total_cost:.2f}")

# Change cost value of last process step
last_process_step = process_chain.process_steps.last()
print(f"Changing last ProcessStep cost from {last_process_step.cost:.2f} to 100.")
last_process_step.cost = 100
last_process_step.save()

print(f"ProcessChain updated. Total Cost: {process_chain.total_cost:.2f}")
