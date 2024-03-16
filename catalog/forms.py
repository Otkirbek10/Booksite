from .models import Comments,BookInstance
from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['body']

class BookOrderForm(ModelForm):
    class Meta:
        model = BookInstance
        fields = ('book','imprint')