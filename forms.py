from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, SelectMultipleField

from wtforms.widgets import ListWidget, CheckboxInput
from Foodfix import dishes

#classes set for each form needed for the app, allows for better organisation
class SelectForm(FlaskForm):
    dishes = RadioField(
    choices = [('soup', 'Soup'), ('sauces', 'Sauces'), ('meats', 'Meats'), ('grains', 'Grains'), ('baked_goods', 'Baked Goods')],
    widget = ListWidget(prefix_label = False),
    option_widget = CheckboxInput())
    submit = SubmitField('Submit')



class FixForm(FlaskForm):
    dishes = (SelectMultipleField(
    choices = [('texture', 'Texture'), ('flavour', 'Flavour'), ('burnt', 'Burnt')],
    widget = ListWidget(prefix_label = False),
    option_widget = CheckboxInput(),
    submit = SubmitField('Submit'),
    ))
