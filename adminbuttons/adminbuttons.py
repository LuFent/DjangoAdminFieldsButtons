from django.utils.html import format_html
from  django.template.loader import get_template, render_to_string


class AdminFieldButton:
    def __init__(self, label, callback_data=None, distinct_color=None, distinct_url=None):
        self.label = label
        self.callback_data = callback_data
        self.color = distinct_color
        self.url = distinct_url


    def serialize(self, common_url, common_color):
        serialized_button =  {
            'callback_data': self.callback_data,
            'label': self.label,
            'color': self.color if self.color else common_color,
            'url': self.url if self.url else common_url
        }
        return serialized_button


class AdminFieldTextButtonsSet:
    def __init__(self, buttons, description, url, color='var(--primary)'):
        self.buttons_set = []
        self.url = url
        self.short_description = description
        self.allow_tags = True

        for buttons_row in buttons:
            buttons_row = [button.serialize(url, color) for button in buttons_row]
            self.buttons_set.append(buttons_row)


    def __call__(self, *args, **kwargs):
        context = {'buttons_set': self.buttons_set}
        html_button = render_to_string('textarea_admin_buttons_field.html', context)
        return format_html(html_button)


class AdminFieldButtonsSet:
    def __init__(self, buttons, description, url, color='var(--primary)'):
        self.buttons_set = []
        self.short_description = description
        self.allow_tags = True

        for buttons_row in buttons:
            buttons_row = [button.serialize(url, color) for button in buttons_row]
            self.buttons_set.append(buttons_row)


    def __call__(self, *args, **kwargs):
        context = {'buttons_set': self.buttons_set}
        html_button = render_to_string('admin_buttons_field.html', context)
        return format_html(html_button)