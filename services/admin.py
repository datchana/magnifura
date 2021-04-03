from django.contrib import admin
from .models import Subscribermail, ContactUsForm, JoinUsForm
from root.admin import CustomModelAdmin
# Register your models here.

class SubscribermailAdmin(admin.ModelAdmin):
    list_display = ['id','email']

    class Meta:
        model = Subscribermail

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email',
                  'phone_number',
                  'domain', 'message',
                  'created_at'
        ]
    class Meta:
        model = ContactUsForm

class JoinUsAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email',
                  'phone_number',
                  'domain','experience','message','url',
                  'created_at'
        ]
    class Meta:
        model = JoinUsForm


admin.site.register(Subscribermail, SubscribermailAdmin)
admin.site.register(ContactUsForm, ContactUsAdmin)
admin.site.register(JoinUsForm, JoinUsAdmin)

