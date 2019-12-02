from django.views.generic import FormView
from number_to_text.converter.forms import ConverterForm

# Create your views here.


class ConverterFormView(FormView):
    form_class = ConverterForm
    template_name = "converter.html"

    def form_valid(self, form):
        self.extra_context = {"text": form.convert()}
        return self.render_to_response(self.get_context_data(form=form))
