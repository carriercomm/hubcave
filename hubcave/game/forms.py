import re

from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from hubcave.game.models import Game

# TODO add point system based on commits and item collection

class GameCreateForm(ModelForm):
    button_prefix = "Create"

    class Meta:
        model = Game
        fields = [
            'repository',
            'map_type'
        ]
        widgets = {'map_type': forms.Select(choices=(('maze', 'Maze'),
                                                     ('cave', 'Cave')))}

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'repository',
            'map_type',
            ButtonHolder(
                Submit('submit', "%s Game".format(self.button_prefix,
                                                  css_class='button'))
            )
        )

        super(ProjectCreateForm, self).__init__(*args, **kwargs)


class GameUpdateForm(GameCreateForm):
    button_prefix = "Update"
