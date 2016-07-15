"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """   creates default melon order  """


    def __init__(self, species, qty):
        """ creates default melon order attributes    """

        self.species = species
        self.qty = qty
        self.shipped = False
    
    def get_total(self):
        """Calculate price."""

        base_price = 5
        if self.species == 'Christmas melon':
            base_price = 7.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    #entire get_total method 
    #marked_shipped method is the same

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)

        self.tax = 0.08
        self.order_type = 'Domestic'
      

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code
        self.tax = 0.17
        self.order_type = 'International'


    def get_total(self):
        """Calculate price."""
            # base_price += 3             # adds $3 for orders less than 10
        
        intl_total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10: 
            intl_total += 3
            return intl_total

        else:
            return intl_total
        
        # base_price = 5
        # if self.species == 'Christmas melon':
        #     base_price = 7.5
        
        # total = (1 + self.tax) * self.qty * base_price
        # return total



    def get_country_code(self):
        """Return the country code."""

        return self.country_code
