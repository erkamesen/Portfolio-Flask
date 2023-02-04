from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL


class ServiceForm(FlaskForm):

    title = StringField("Başlık",
                       validators=[DataRequired()],
                       render_kw={"placeholder": "Hizmetinizin ismini giriniz..."}
                       )
    img_url = StringField("Resim",
                          validators=[DataRequired(), URL()],
                          render_kw={
                              "placeholder": "Bir resim URL si giriniz..."})
    description = TextAreaField("Açıklama",
                         validators=[DataRequired()],
                         render_kw={"rows": 15,
                                    "cols": 40,
                                    "placeholder": "İçeriğini buraya yazınız..."})

    submit = SubmitField("Yayınla")
