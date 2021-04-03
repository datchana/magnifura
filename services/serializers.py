from rest_framework import serializers

from .models import Subscribermail, ContactUsForm, JoinUsForm

class SubscriberMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribermail
        fields = [
            'email'
        ]

class ContactUsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsForm
        fields = ['firstname', 'lastname', 'email',
                  'phone_number',
                  'domain', 'message',
                  'created_at'
        ]

class JoinUsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinUsForm
        fields = ['firstname', 'lastname', 'email',
                  'phone_number',
                  'domain','experience','message','url',
                  'created_at'
        ]
