import re
from typing import Any
from django.db import models
from ..common.util import convert_date_string_to_datetime
from .order_model import SupplierOrder
from django.forms import ValidationError

from datetime import datetime

class PaymentCard(models.Model):
    # FUNCTIONS VALIDATION
    def number_is_valid(number: str) -> bool:
        """Determines whether the CC number is valid based on Luhn's algorithm."""
        number = re.sub(r'\D', '', number)
        print(number) # 5369485886562088
        if len(number) < 16: 
            raise ValidationError("Invalid credit card number.")
        reverse =  str(number)[::-1]
        odd_digits = reverse[::2]
        odd_sum = sum(int(i) for i in odd_digits)

        even_digits = reverse[1::2]
        doubled_even_digits = [int(i) * 2 for i in even_digits]
        summed_digits_for_even_doubles = [i // 10 + i % 10 for i in doubled_even_digits]
        sum_of_even_digit_sums = sum(summed_digits_for_even_doubles)

        if (sum_of_even_digit_sums + odd_sum) % 10 != 0:
            raise ValidationError("Invalid credit card number.")
    
    def expirate_date(value :str):  
        # Just check MM/YY Pattern
        r = re.compile('^([0-9][0-9])/([0-9][0-9])$')
        m = r.match(value)
        if m == None: return False        
        # Check that the month is 1-12
        month = int(m.groups()[0])
        print('month', month)
        if month < 1 or month > 12: 
            raise ValidationError("Invalid expiration date.")  
        
        # Check that the year is not too far into the future
        year = int(m.groups()[1])
        curr_year = int(datetime.now().strftime('%y'))
        print('year', year)
        print('curr year', curr_year)
        if year == curr_year:
            curr_month = datetime.now().month
            if month < curr_month: 
                raise ValidationError("Invalid expiration date.")
        
        max_year = curr_year + 10
        if year > max_year or year < curr_year: 
            raise ValidationError("Invalid expiration date.")
    
    # FIELDS
    card_number = models.CharField(max_length=19, validators=[number_is_valid])
    card_holder_name = models.CharField(max_length=150)
    expiration_date = models.CharField(max_length=5, validators=[expirate_date])
    security_code = models.CharField(max_length=4)
    order = models.ForeignKey('SupplierOrder', on_delete=models.CASCADE, related_name='payment_card')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = '_web'
        db_table = 'payment_card'
        
    # FUNCTIONS
    
                
    def get_cc_type(number:str):
        """
        Gets credit card type given number. Based on values from Wikipedia page
        "Credit card number".
        http://en.wikipedia.org/w/index.php?title=Credit_card_number
        """
        number = re.sub(r'\D', '', number)
        #group checking by ascending length of number
        
        if number[:2] in ("34", "37"): return "American Express"
        elif number[:4] == "6011": return "Discover"
        elif number[:2] in ("51", "52", "53", "54", "55"): return "mastercard"
        elif number[0] == "4": return "visa"
        
        return "Unknown"