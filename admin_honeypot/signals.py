from django.dispatch import Signal

honeypot = Signal()

# Signal sender
def send_honeypot_signal(instance, request):
    honeypot.send(sender=None, instance=instance, request=request)

# Signal receiver
def handle_honeypot_signal(sender, instance, request, **kwargs):
    # Handle the signal here
    pass

# Connect the signal receiver
honeypot.connect(handle_honeypot_signal)
