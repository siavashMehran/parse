
from .models import ContactUs
from django.forms import ModelForm, TextInput, Textarea, EmailInput


class ContactUsModelForm(ModelForm):

    



    class Meta:
        
        
        model = ContactUs
        fields = '__all__'

        CSS_CLASSES = {
            'TextInput' : 'txt-s-101 cl3 plh1 size-a-46 bo-all-1 bocl15 focus1 p-rl-20',
            'TextArea' : 'txt-s-120 cl3 plh1 size-a-26 bo-all-1 bocl15 focus1 p-rl-20 p-tb-10',
        }
        widgets = {
            'user_name'     : TextInput (attrs={'class': CSS_CLASSES['TextInput'], 'placeholder':'*نام'    , 'required':''}),
            'user_contact_info'    : EmailInput(attrs={'class': CSS_CLASSES['TextInput'], 'placeholder':'اطلاعات تماس : (تلفن یا ایمیل)'}),
            'title'         : TextInput (attrs={'class': CSS_CLASSES['TextInput'], 'placeholder':'موضوع'}),
            'message'       : Textarea  (attrs={'class': CSS_CLASSES['TextArea']}),
        }



    def validate_and_save_POST_data(self, POSTdata:dict):
        """
        this method returns the co-responding HTTPResponse
        `status_code` of the operation `save()`
        """
        self.data = POSTdata
        if self.is_valid():
            try:
                self.save()
                status_code = 200
            except:
                status_code = 504

        else:
            status_code = 400
        return status_code
            
        