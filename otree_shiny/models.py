from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Marco Gutierrez'

doc = """
Shiny dashboard replication
using oTree
"""


class Constants(BaseConstants):
    name_in_url = 'otree_shiny'
    players_per_group = None
    num_rounds = 1

    # templates incluibles
    acerca = "otree_shiny/Acerca.html"
    noticias = "otree_shiny/Noticias.html"
    inicio = "otree_shiny/Inicio.html"
    indicadores = "otree_shiny/Indicadores.html"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user = models.StringField(label="Nombre de usuario/email")
    new_user = models.StringField(label="Nombre de usuario/email")
    password = models.StringField(label="Contraseña")
    updated_password = models.StringField(label="Ingrese su nueva contraseña")
    validate_updated_password = models.StringField(label="Vuelva a ingresar su nueva contraseña")
