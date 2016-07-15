"""This file should have our order classes in it."""

import random
from datetime import datetime, date

class AbstractMelonOrder(object):
    """   creates default melon order  """


    def __init__(self, species, qty, tax, order_type):
        """ creates default melon order attributes    """

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_base_price(self):
        """Return base price for melon order based on splurge pricing."""

        # base_price = random.randint(5, 9)
        base_price = 5
        if self.species == 'Christmas melon':
            base_price *= 1.5

        order_time = datetime.now()
        if (date.time in range(8,15)) and (datetime.weekday in range(0,5)): # need to change due to adding a time check
            base_price += 4

        return base_price


    def get_total(self):
        """Calculate price."""

       
        total = (1 + self.tax) * self.qty * self.get_base_price() 
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, 0.08, "Domestic")
      

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, 0.17, "International")

        self.country_code = country_code


    def get_total(self):
        """Calculate price, add $3 fee for orders less than 10."""
        
        
        intl_total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10: 
            intl_total += 3
            return intl_total

        else:
            return intl_total
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """ For US Government Melon orders """ 

    def __init__(self, species, qty):
        super(GovernmentMelonOrder,self).__init__(species, qty, 0, "Domestic")

        self.passed_inspection = False 

    def mark_inspection(self, passed):
        """Takes boolean input if govt order passed inspection."""
        
        self.passed_inspection = passed
