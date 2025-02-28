from django.db import models

class ServerInfo(models.Model):
    server_role = models.CharField(max_length=255)
    server_name = models.CharField(max_length=255)
    ip = models.CharField(max_length=50) 
    os = models.CharField(max_length=255)
    ram = models.PositiveIntegerField()  
    datasource = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    diskdevices = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.server_name} ({self.server_role})"