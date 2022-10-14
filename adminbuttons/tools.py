from .adminbuttons import *

def admin_model_with_buttons_decorator(original_class):
    admin_buttons_field_css = 'admin_custom/mycss.css'
    admin_buttons_field_js = 'admin_custom/myjs.js'
    buttons_types = [AdminFieldTextButtonsSet, AdminFieldButtonsSet]

    try:
        orig_media = getattr(original_class, 'Media')

        try:
            orig_js = list(getattr(orig_media, 'js'))
            orig_js.append(admin_buttons_field_js)
            orig_media.js = orig_js
        except Exception:
            orig_media.js = [admin_buttons_field_js]

        try:
            orig_css = list(getattr(orig_media, 'css')['all'])
            orig_css.append(admin_buttons_field_css)
            orig_media.css['all'] = orig_css
        except Exception:
            orig_media.css = {'css': [admin_buttons_field_css]}

    except AttributeError:
        class Media:
            js = [admin_buttons_field_js]
            css = {'all': [admin_buttons_field_css]}

        orig_media = Media

    original_class.Media = orig_media

    buttons_fields = list(
        filter(lambda field_name: type(getattr(original_class, field_name)) in buttons_types, dir(original_class)))

    try:
        orig_readonly_fields = list(getattr(original_class, 'readonly_fields'))
        orig_readonly_fields.extend(buttons_fields)

    except AttributeError:
        orig_readonly_fields = buttons_fields

    original_class.readonly_fields = orig_readonly_fields

    return original_class