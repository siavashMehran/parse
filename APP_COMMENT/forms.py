from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea
from django.http.response import JsonResponse
from .models import PostComment




# for shared behavior among comment models
class CommentModelFormMixin:


    def save_and_return_JSON_response(self):
        status_code   = self._validate_and_save() # this method returns the status_code of the final response
        response_data = self._make_response_data_from_status_code(status_code)
        response      = self._create_json_response(response_data, response_data['status'])
        return response

    def _validate_and_save(self) -> int:
        """
        returns the `status_code` of the response that client recieves\n
        status_code could be: [504, 200, 400]
        """
        status_code = 0
        if self.is_valid():
            try: 
                self.save()
                status_code = 200
            except: 
                status_code = 504
                raise Exception('Server Error 504')
        else:
            status_code = 400
        return status_code

    def _make_response_data_from_status_code(self, status_code:int):
        """ retruns a python `<dict>` that contains the\n
        `status_code` and `message` associated with the response
        """
        response_messages = {
            200 : ' با موفقیت انجام شد',
            400 : 'اطلاعات وارد شده صحیح نیست',
            504 : 'در انجام درخواست شما خطایی رخ داده است',
        }
        response_data = {}
        response_data['status']  = status_code
        response_data['message'] = response_messages[status_code]
        return response_data

    def _create_json_response(self, response_data, status_code):
        """create `JSONResponse` from a response_data dict that,\n
        contains a status code => { 'status': 404 }
        """
        return JsonResponse(data=response_data, status=status_code, json_dumps_params={'ensure_ascii':False})





class PostCommentModelForm(ModelForm, CommentModelFormMixin):
    
    class Meta:
        fields  = ['user_name', 'body']
        model   = PostComment
        widgets = {
            'user_name'       : TextInput (attrs={'class':'txt-s-120 cl3 plh1 size-a-21 bo-all-1 bocl15 focus1 p-rl-20',         'placeholder':'*نام'    }),
            'body'       : Textarea  (attrs={'class':'txt-s-120 cl3 plh1 size-a-26 bo-all-1 bocl15 focus1 p-rl-20 p-tb-10', 'placeholder':'*نظر شما'}),
        }

    @classmethod
    def get_comment_form_with_initial_or_blank(cls, user):
        try:
            form = cls()
            form.initial = {
                'user'       : user.first_name,
            }
        except:
            form = cls()
        return form