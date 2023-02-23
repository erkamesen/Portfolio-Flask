from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class AdminForm(FlaskForm):

    username = StringField("Username",
                           validators=[DataRequired()],
                           render_kw={"placeholder": "Your Username.."}
                           )
    password = PasswordField("Password",
                             validators=[DataRequired()],
                             render_kw={"placeholder": "**********"}
                             )
    submit = SubmitField("Send")
