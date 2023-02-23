from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):

    name = StringField("Name",
                       validators=[DataRequired()],
                       render_kw={"placeholder": "Name..."}
                       )
    text = TextAreaField("Message",
                         validators=[DataRequired()],
                         render_kw={"rows": 10,
                                    "cols": 40,
                                    "placeholder": "Comment..."})

    submit = SubmitField("Submit")
