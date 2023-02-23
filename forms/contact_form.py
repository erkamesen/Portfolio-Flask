from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):

    name = StringField("Name",
                       validators=[DataRequired()],
                       render_kw={"placeholder": "Name..."}
                       )
    email = StringField("Email",
                        validators=[DataRequired()],
                        render_kw={"placeholder": "Email..."}
                        )
    subject = StringField("Subject",
                          validators=[DataRequired()],
                          render_kw={
                              "placeholder": "Subject..."}
                          )
    text = TextAreaField("Message",
                         validators=[DataRequired()],
                         render_kw={"rows": 10,
                                    "cols": 40,
                                    "placeholder": "Your text here..."})

    submit = SubmitField("Submit")
