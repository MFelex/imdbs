import os

from django import forms

from .models import MovieComment, MovieCrew, MovieRate, Rate


class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ['comment_text']

    def clean(self):
        disallow = ['rahbar', 'nezam', 'fuck']
        data = super().clean()
        for word in disallow:
            if word in data['comment_text']:
                raise forms.ValidationError(f"No {word} allowed!!")


class MovieRateForm(forms.Form):
    rate = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)],
                             widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}), )
