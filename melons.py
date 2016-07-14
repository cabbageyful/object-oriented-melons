"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """   creates default melon order  """


    def __init__(self, species, qty, shipped, order_type, tax):
        """ creates default melon order attributes    """

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
    
    def get_total(self):
        """Calculate price."""

        base_price = 5
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
        super(DomesticMelonOrder, self).__init__(species, qty, False, 'domestic', .08)

    # def get_total(self):
    #     return super(DomesticMelonOrder, self).get_total
    #     """Calculate price."""

      

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        self.country_code = country_code
        super(InternationalMelonOrder, self).__init__(species, qty, False,
            'international', .17)
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
