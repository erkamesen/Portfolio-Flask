from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired, URL


class ProjectForm(FlaskForm):
    title = StringField("Proje Adı",
                        validators=[DataRequired()],
                        render_kw={
                            "placeholder": "Projenin isminizi giriniz..."}
                        )
    subtitle = StringField("Açıklama",
                           validators=[DataRequired()],
                           render_kw={
                               "placeholder": "Projeye dair bir açıklama giriniz..."}
                           )
    img_url = StringField("Resim",
                          validators=[DataRequired(), URL()],
                          render_kw={
                              "placeholder": "Bir resim URL si giriniz..."}
                          )
    body = CKEditorField("İçerik", validators=[DataRequired()],
                         render_kw={"placeholder": "Projenizin detaylarını giriniz..."})
    submit = SubmitField("Proje Oluştur.")
