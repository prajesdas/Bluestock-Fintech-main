from django.forms.widgets import ClearableFileInput

class CustomClearableFileInput(ClearableFileInput):
    template_name = 'custom_clearable_file_input.html'

    def __init__(self, ipo_instance=None, *args, **kwargs):
        self.ipo_instance = ipo_instance
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['ipo_instance'] = self.ipo_instance
        return context
    
    # widgets.py
