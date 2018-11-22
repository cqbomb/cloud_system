from django.db import models


class Vmdb(models.Model):
    vm_name = models.CharField(max_length=100, blank=False)
    vm_summary = models.CharField(max_length=10000, blank=True)
    vm_owner = models.CharField(max_length=100, blank=False)
    vm_ip = models.CharField(max_length=100, blank=True)
    vm_global_ip = models.CharField(max_length=100, blank=True)
    vm_status = models.CharField(max_length=100, blank=True)
    vm_webconsole_url = models.CharField(max_length=10000, blank=True)


