import re

from ._builtin import Page


############### Functions
def special_characters(s, pat=re.compile('[@_!#$%^&*()<>?/\|}{~:]')):
    """
    Detects special characters in string

    Input: string, regex pattern
    Output: boolean
    """

    print("---into specials---")
    print("string: ", s)
    specials_in_s = pat.search(s)
    output = specials_in_s is not None  # if true, there are specials, else no
    print("output: ", output)
    return output


def alpha_in_string(s):
    """
    Detects if string has at least one alphabetic character

    Input: string
    Output: boolean
    """

    validator = False
    counter = 0
    while validator is False and counter < len(s):
        if s[counter].isalpha():
            validator = True
        else:
            counter += 1

    return validator


############### Classes

class Login(Page):
    form_model = "player"
    form_fields = ["user", "password"]

    # def error_message(self, values):
    # # user validation
    # if "@" not in values["user"] or "." not in values["user"]:
    #     return "Ingresar un correo válido"

    # pass validation
    # print("----------------")
    # print("pass: ", values["password"])
    # nums = len(re.findall('\.[0-9.]+', values["password"])) != 0 # checking if nums in pass
    # print("v nums: ", nums)
    # specials = special_characters(values["password"]) # checking if special in pass
    # print("v specials: ", specials)
    # alphabs = alpha_in_string(values["password"]) # validating if alphabetics in pass
    # print("v alphabs: ", alphabs)
    # if not specials:
    #     return "La contraseña debe incluir caracteres especiales."
    # if not nums:
    #     print("raaaaaaa")
    #     return "La contraseña debe incluir números."
    # if not alphabs:
    #     return "La contraseña debe incluir caracteres alfabéticos."


class Dashboard(Page):
    form_model = "player"
    form_fields = ["updated_password", "validate_updated_password"]

    def vars_for_template(self):
        return {"username": "John Doe"}


page_sequence = [Login, Dashboard]
