# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.data import JsonLexer


def admin_field_json_formatted(field):
    data = json.dumps(field, indent=2)

    formatter = HtmlFormatter(style='colorful')
    response = highlight(data, JsonLexer(), formatter)
    style = "<style>" + formatter.get_style_defs() + "</style><br/>"

    return mark_safe(style + response)