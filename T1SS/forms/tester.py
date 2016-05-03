from wtforms import Form, StringField, validators


class TestForm(Form):
    user_name = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()],
                            render_kw={"placeholder": "Username"})
    text = StringField('Text', [validators.Length(min=16, max=160), validators.DataRequired()],
                       render_kw={"placeholder": "Text"})
