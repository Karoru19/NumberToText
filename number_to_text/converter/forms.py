from django import forms
from django.utils.translation import pgettext_lazy
from number_to_text.converter.utils import number_to_words


class ConverterForm(forms.Form):
    number = forms.IntegerField(
        max_value=1000000, min_value=0, label=pgettext_lazy("Form", "Number")
    )

    def convert(self):
        number = self.cleaned_data["number"]
        return number_to_words(number)
