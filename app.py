"""
Module defining ordering functions and
command line interface for it.

See module pizza for a pizza definition.

Functions:

    log
    bake
    delivery_func
    pickup
    cli
    menu
    order
"""


from pizza import Pizza
from random import randint
import click


def log(pattern: str = ''):
    """
    Decorator for ordering functions to log the duration
    of the wrapped function imitated by
    randomint generation of the seconds spent

    Parameters
    ----------
        pattern (str = '' ) : A pattern for
            logged function string display

    Returns
    -------
        Log message string display
    """

    def inner_log(func):
        def wrapper(*args):
            if not pattern:
                result = f'{func.__name__.capitalize()} {args[0].name} ' \
                         f'- {randint(1, 11)}c!'
            else:
                result = pattern.replace('{}', str(randint(1, 11)))
                result = result.replace('pizzaname', args[0].name)
            print(result)
            return result
        return wrapper
    return inner_log


@log('👨‍🍳 Приготовили pizzaname за {}c!')
def bake(pizza: Pizza):
    """Baking pizza command"""
    pass  # pragma: no cover


@log('🛵 Доставили pizzaname за {}c!')
def delivery_func(pizza: Pizza):
    """Delivery pizza command"""
    pass  # pragma: no cover


@log('🏠 Забрали pizzaname за {}c!')
def pickup(pizza: Pizza):
    """Pickup pizza command"""
    pass  # pragma: no cover


@click.group()
def cli():
    """Click Command Line Interface command"""
    pass  # pragma: no cover


@cli.command()
def menu():
    """Menu display command"""
    emodji_dict = {
        'Margherita': '🧀',
        'Pepperoni': '🍕',
        'Hawaiian': '🍍'
    }
    for cls in Pizza.__subclasses__():
        click.echo(
            f'- {cls().name} {emodji_dict[cls().name]}: \
{cls().ingredients}'
        )


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default='L')
@click.argument('pizza_name', nargs=1)
def order(pizza_name: str, delivery: bool,  size: str):
    """
    Order making command.
    Creates a Pizza object, passes it to bake and
    delivery or pickup function,
    displays all messages of the order info and logs.

    Parameters
    ----------
        pizza_name (str) : A pizza name for order
        delivery (bool) : CLI flag for delivery
        size (str) : Pizza size

    Returns
    -------
        None
    """

    pizza_name = pizza_name.lower().capitalize()
    pizza = None

    for cls in Pizza.__subclasses__():
        name = cls().name
        if pizza_name == name:
            pizza = cls(size=size)
            break

    if not pizza:
        pizza = Pizza(name=pizza_name, size=size)

    click.echo(f'🧾 Сделан заказ на: {pizza}')

    bake(pizza)

    if delivery:
        delivery_func(pizza)
    else:
        pickup(pizza)


if __name__ == '__main__':
    cli()  # pragma: no cover
