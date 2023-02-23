from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL


class ServiceForm(FlaskForm):

    title = StringField("Title",
                       validators=[DataRequired()],
                       render_kw={"placeholder": "Service Title..."}
                       )
    img_url = StringField("Image",
                          validators=[DataRequired(), URL()],
                          render_kw={
                              "placeholder": "Image URL..."})
    description = TextAreaField("Açıklama",
                         validators=[DataRequired()],
                         render_kw={"rows": 15,
                                    "cols": 40,
                                    "placeholder": "Details..."})

    submit = SubmitField("Create Service")
