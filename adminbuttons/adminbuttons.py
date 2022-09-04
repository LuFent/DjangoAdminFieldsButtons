from django.utils.html import format_html
from  django.template.loader import get_template, render_to_string

class TextAdminFieldButton:
    def __init__(self, buttons, desc):
        self.buttons = []
        for button in buttons:
            if len(button) == 1:
                self.buttons.append({'label': button[0], 'data': button[0]})

            if len(button) == 2:
                self.buttons.append({'label': button[0], 'data': button[1]})

        self.short_description = desc
        self.allow_tags = True

    def __call__(self, *args, **kwargs):
        context = {'buttons': self.buttons}
        html_button = render_to_string('textarea_admin_buttons_field.html', context)
        return format_html(html_button)


class AdminFieldButton:
    def __init__(self, buttons, desc):
        self.buttons = []
        for button in buttons:
            if len(button) == 1:
                self.buttons.append({'label': button[0], 'data': button[0]})

            if len(button) == 2:
                self.buttons.append({'label': button[0], 'data': button[1]})

        self.short_description = desc
        self.allow_tags = True

    def __call__(self, *args, **kwargs):
        context = {'buttons': self.buttons}
        html_button = render_to_string('admin_buttons_field.html', context)
        print(html_button)
        return format_html(html_button)