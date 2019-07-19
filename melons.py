"""Classes for melon orders."""

from random import randrange
import datetime

class TooManyMelonsError(ValueError):
    pass

class AbstractMelonOrder():

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        if qty > 100:
            raise TooManyMelonsError
            
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        """Dynamic pricing algorithm."""

        base_price = randrange(5,10)

        # Monday is 0, Sunday is 6.
        # 24-hour integer hour.
        day = datetime.datetime.weekday(datetime.datetime.now())
        hour = datetime.datetime.now().hour

        if day in range(5) and hour in range(8, 12):
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price *= 1.5

        if self.qty < 10:
            base_price += 3

        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped =  True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize international melon order attributes."""
        
        self.country_code = country_code

        super().__init__(species, qty)
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """US Government melon order."""

    order_type = "government"
    tax = 0.00

    def __init__(self, species, qty):
        """Initialize US Government melon order attributes."""

        self.passed_inspection = False
        super().__init__(species, qty)

    def mark_inspection(passed):
        """Updates whether or not the melon has passed inspection."""

        self.passed_inspection = passed