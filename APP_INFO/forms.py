
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
        
        form = self.__class__(self.__filter_from_POST_data(POSTdata))
        
        if form.is_valid():
            try:
                form.save()
                status_code = 200
            except:
                status_code = 504
        else:
            status_code = 400
        return status_code
            

    def __filter_from_POST_data(self, request_post:dict):
        post_dict = dict()
        post_dict['user_name'] = request_post.get('user_name', None)
        post_dict['user_contact_info'] = request_post.get('user_contact_info', None)
        post_dict['title'] = request_post.get('title', None)
        post_dict['message'] = request_post.get('message', None)
        post_dict['csrfmiddlewaretoke'] = request_post.get('csrfmiddlewaretoke', None)
        return post_dict