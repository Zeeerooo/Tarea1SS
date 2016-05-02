from wtforms import Form, StringField, validators


class ValidateForm(Form):
    user_name = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    text = StringField('Text', [validators.Length(min=16, max=160), validators.DataRequired()])
    tag = StringField('Tag', [validators.Length(min=16, max=64), validators.DataRequired()])
