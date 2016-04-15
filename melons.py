"""This file should have our order classes in it."""
from random import randint

class AbstractMelonOrder(object):
    """Parent class for all melon orders"""

    def __init__(self, 
                 species, 
                 qty, 
                 country_code
                 ):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False

    def get_base_price(self):
        """Activates Splurge Pricing by setting the base price randomly"""
        
        base_price = randint(5, 9)
        return base_price

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        # print base_price

        if self.species == "Christmas melon":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08    

    def __init__(self, species, qty, country_code='US'):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species,
                                                 qty,
                                                 country_code)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species,
                                                      qty,
                                                      country_code)

    def get_total(self):
        """Calculate price."""

        total = super(InternationalMelonOrder,self).get_total()

        flat_fee = 3

        if self.qty < 10:
            total += flat_fee

        return total

class USGovernmentOrderMixin(object):
    """A melon order from the US Government"""

    tax = 0
    passed_inspection = False

    def mark_inspection(self):
        """Mark order as inspected"""

        self.passed_inspection = True

class USGDomestic(USGovernmentOrderMixin, DomesticMelonOrder):
    """US Government order to a domestic address"""

    pass

class USGInternational(USGovernmentOrderMixin, InternationalMelonOrder):
    """US Government order to an international address (APO, FPO, Embassy)"""

    pass
