"""Imports"""
from django.forms.widgets import ClearableFileInput
# Using "as _" means we can now call gettext_lazy() using _().
# It's effectively an alias.
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """Generate clearable file imput"""
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/custom_clearable_file_input.html')
