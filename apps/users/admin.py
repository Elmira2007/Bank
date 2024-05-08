from django.contrib import admin

from apps.users.models import User, HistoryTransfer

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'age')
    list_filter = ('id', )
    
    
@admin.register(HistoryTransfer)
class HistoryTransferAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user')
    list_filter = ('id',)