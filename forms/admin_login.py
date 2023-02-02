from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class AdminForm(FlaskForm):
    
    username = StringField("Kullanıcı Adı",
                       validators=[DataRequired()],
                       render_kw={"placeholder": "Kullanıcı Adı.."}
                       )
    password = PasswordField("Şifre",
                         validators=[DataRequired()],
                         render_kw={"placeholder": "Şifre"}
                         )
    submit = SubmitField("Gönder")