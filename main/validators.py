from django.core.exceptions import ValidationError

class PhoneNumberValidator:

    def __call__(self, data:str):
        self.phone_number = data
        self.validate_phone_number()

        
    def len_not_13(self):
        return (len(self.phone_number) < 13) or (len(self.phone_number) > 13)


    def validate_phone_number(self):

        # if blank
        if len(self.phone_number) == 0:
            return self.phone_number

        elif not self.phone_number.startswith('+98'):
            raise ValidationError('تلفن باید با +98 شروع بشود')
        
        # length validation
        elif self.len_not_13():
            raise ValidationError('تلفن درست نیست')
            
        return self.phone_number