from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired, URL


class ProjectForm(FlaskForm):
    title = StringField("Project Name",
                        validators=[DataRequired()],
                        render_kw={
                            "placeholder": "Projects Title..."}
                        )
    subtitle = StringField("Subtitle",
                           validators=[DataRequired()],
                           render_kw={
                               "placeholder": "Subtitle..."}
                           )
    img_url = StringField("Image",
                          validators=[DataRequired(), URL()],
                          render_kw={
                              "placeholder": "Image URL..."}
                          )
    body = CKEditorField("Content", validators=[DataRequired()],
                         render_kw={"placeholder": "Details..."})
    submit = SubmitField("Create Project.")
