"""
Module defining Pizza class and its subclasses for making an order.

See module app for an ordering mechanism.

Classes:

    PizzaInterface
    PizzaSizes
    Pizza
    Margherita
    Pepperoni
    Hawaiian
"""


from enum import Enum
from abc import abstractmethod
from abc import ABC


class PizzaInterface(ABC):
    """
    Pizza Interface class

    Properties:
        ingredients - pizza ingredients display

    Methods:
        dict - pizza recipe dictionary display
    """

    @property
    @abstractmethod
    def ingredients(self):
        pass

    @abstractmethod
    def dict(self):
        pass


class PizzaSizes(Enum):
    """
    Enumeration class for pizza sizes

    Set of available sizes for pizza orders
    is limited to Large and Extra Large
    """
    L = 'Large'
    XL = 'Extra Large'
    Large = 'Large'
    ExtraLarge = 'Extra Large'


class Pizza(PizzaInterface):
    """
    A class to represent a pizza.

    Attributes
    ----------
        name : str
            name of the pizza
        size : PizzaSize
            size of the pizza
        _ingredients : list
            ingredients of the pizza

    Methods
    -------
    ingredients(self):
        Property for recipe string representation

    __str__(self):
        Returns string of Pizza object string representation

    dict(self):
        Returns pizza recipe dictionary representation

    __eq__(self, other):
        Returns boolean of ingredients sets
        comparison of self and other Pizza objects
    """

    def __init__(self, name: str = '', size: str = 'L', ingredients=None):
        """
        Constructs all the necessary attributes for the Pizza object.

        Parameters
        ----------
            name : str
                name of the pizza
            size : PizzaSize = Large
                size of the pizza
            ingredients : list = []
                ingredients of the pizza
        """

        if not isinstance(name, str) or name == '':
            self.name = 'default_pizza_name'
        else:
            self.name = name

        if ingredients is None or not isinstance(ingredients, list):
            self._ingredients = []
        else:
            self._ingredients = ingredients

        try:
            self.size = getattr(PizzaSizes, size).value
        except AttributeError:
            print('It is either L or XL sizes, '
                  'pizza size will be set to Large')
            self.size = 'Large'

    @property
    def ingredients(self):
        """
        Property for recipe string representation

        Returns
        -------
        Pizza recipe string representation
        """

        return ", ".join(self._ingredients)

    def __str__(self):
        """
        Method for Pizza object string representation

        Returns
        -------
        Pizza string representation
        """

        return f'{self.name} pizza, {self.size} size'

    def dict(self):
        """
        Method for pizza recipe dictionary representation

        Returns
        -------
        Pizza recipe dictionary representation
        """

        return {self.name: self.ingredients}

    def __eq__(self, other):
        """
        Ingredients sets comparison of
        self and other Pizza objects

        Parameters
        -------
            other : Pizza object

        Returns
        -------
        True in case of equality of ingredients sets,
        otherwise - False
        """

        return set(self.ingredients) == set(other.ingredients)


class Margherita(Pizza):
    """
    A Pizza subclass to represent a margherita pizza.

    Attributes
    ----------
        name : str
            name of the pizza
        size : PizzaSize
            size of the pizza
        _ingredients : list
            ingredients of the pizza
    """

    def __init__(self, size: str = 'L'):
        """
        Constructs all the necessary attributes for the Margherita object.

        Parameters
        ----------
            size : PizzaSize = Large
                size of the pizza

        Attributes
        ----------
            name : str = Margherita
            _ingredients : list = [
            'Tomato Sauce',
            'Mozzarella',
            'Tomatoes'
            ]
        """

        super().__init__(size=size)
        self.name = 'Margherita'
        self._ingredients = [
            'Tomato Sauce',
            'Mozzarella',
            'Tomatoes'
        ]


class Pepperoni(Pizza):
    """
    A Pizza subclass to represent a pepperoni pizza.

    Attributes
    ----------
        name : str
            name of the pizza
        size : PizzaSize
            size of the pizza
        _ingredients : list
            ingredients of the pizza
    """

    def __init__(self, size: str = 'L'):
        """
        Constructs all the necessary attributes for the Pepperoni object.

        Parameters
        ----------
            size : PizzaSize = Large
                size of the pizza

        Attributes
        ----------
            name : str = Pepperoni
            _ingredients : list = [
            'Tomato Sauce',
            'Mozzarella',
            'Pepperoni'
            ]
        """

        super().__init__(size=size)
        self.name = 'Pepperoni'
        self._ingredients = [
            'Tomato Sauce',
            'Mozzarella',
            'Pepperoni'
        ]


class Hawaiian(Pizza):
    """
    A Pizza subclass to represent a hawaiian pizza.

    Attributes
    ----------
        name : str
            name of the pizza
        size : PizzaSize
            size of the pizza
        _ingredients : list
            ingredients of the pizza
    """

    def __init__(self, size: str = 'L'):
        """
        Constructs all the necessary attributes for the Hawaiian object.

        Parameters
        ----------
            size : PizzaSize = Large
                size of the pizza

        Attributes
        ----------
            name : str = Hawaiian
                name of the pizza
            _ingredients : list = [
            'Tomato Sauce',
            'Mozzarella',
            'Pepperoni'
            ]
        """

        super().__init__(size=size)
        self.name = 'Hawaiian'
        self._ingredients = [
            'Tomato Sauce',
            'Mozzarella',
            'Chicken',
            'Pineapples'
        ]


if __name__ == '__main__':
    pass  # pragma: no cover
