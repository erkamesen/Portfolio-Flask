from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):

    name = StringField("Name",
                       validators=[DataRequired()],
                       render_kw={"placeholder": "İsminizi giriniz..."}
                       )
    email = StringField("Email",
                        validators=[DataRequired()],
                        render_kw={"placeholder": "Mail adresinizi yazınız..."}
                        )
    subject = StringField("Email",
                          validators=[DataRequired()],
                          render_kw={
                              "placeholder": "Konu başlığını giriniz..."}
                          )
    text = TextAreaField("Message",
                         validators=[DataRequired()],
                         render_kw={"rows": 10,
                                    "cols": 40,
                                    "placeholder": "Mesajınızı buraya yazınız..."})

    submit = SubmitField("Gönder")
