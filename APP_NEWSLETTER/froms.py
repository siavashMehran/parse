import imp
from django import forms
from django.utils.translation import gettext_lazy as _
from APP_NEWSLETTER.models import NewsletterClient

class NewsletterModelForm(forms.ModelForm):
    class Meta:
        model = NewsletterClient
        fields = ['email']

    def is_validated_and_saved(self):
        if self.is_valid():
            self.save()
            return True
        else:
            self.add_error('email', _('لطفا یک ایمیل معتبر وارد کنید'))
            return False