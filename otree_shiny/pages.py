from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Login(Page):
    form_model = "player"
    form_fields = ["user", "password"]


class Dashboard(Page):
    form_model = "player"
    form_fields = ["updated_password", "validate_updated_password"]

    def vars_for_template(self):
        return {"username": "John Doe"}


page_sequence = [Login, Dashboard]
