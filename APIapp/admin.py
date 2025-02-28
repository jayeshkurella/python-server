from django.contrib import admin
from .models import ServerInfo 

class ServerInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'server_role', 'server_name', 'ip', 'os', 'ram', 'datasource', 'job', 'diskdevices')  # Removed is_deleted from list_display
    list_filter = ('server_role', 'os')  
    search_fields = ('server_name', 'ip', 'os')
    

admin.site.register(ServerInfo, ServerInfoAdmin)
