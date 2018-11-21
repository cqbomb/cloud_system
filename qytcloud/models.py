from django.db import models


class Vmdb(models.Model):
    vm_name = models.CharField(max_length=100, blank=False)
    vm_summary = models.CharField(max_length=10000, blank=False)
    vm_owner = models.CharField(max_length=100, blank=False)
    vm_webconsole_url = models.CharField(max_length=10000, blank=False)


