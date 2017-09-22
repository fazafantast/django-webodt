# -*- coding: utf8 -*-
from django.conf import settings

WEBODT_TEMPLATE_PATH = getattr(settings, 'WEBODT_TEMPLATE_PATH', '')
WEBODT_DEFAULT_EXTEND = getattr(settings, 'WEBODT_DEFAULT_EXTEND', 'doc')

WEBODT_ABIWORD_COMMAND = getattr(settings, 'WEBODT_ABIWORD_COMMAND', ['/usr/bin/abiword', '--plugin', 'AbiCommand'])
WEBODT_LIBREOFFICE_COMMAND = getattr(settings, 'WEBODT_LIBREOFFICE_COMMAND', ['/usr/bin/libreoffice', '--headless', '--writer', '--convert-to'])

WEBODT_GOOGLEDOCS_EMAIL = getattr(settings, 'WEBODT_GOOGLEDOCS_EMAIL', None)
WEBODT_GOOGLEDOCS_PASSWORD = getattr(settings, 'WEBODT_GOOGLEDOCS_PASSWORD', None)
WEBODT_CONVERTER = getattr(settings, 'WEBODT_CONVERTER', 'webodt.converters.abiword.AbiwordODFConverter')
WEBODT_TMP_DIR = getattr(settings, 'WEBODT_TMP_DIR', None)
WEBODT_CACHE_DIR = getattr(settings, 'WEBODT_CACHE_DIR', '/tmp/webodt_cache')
WEBODT_ODF_TEMPLATE_PREPROCESSORS = getattr(settings, 'WEBODT_ODF_TEMPLATE_PREPROCESSORS', [
    'webodt.preprocessors.xmlfor_preprocessor',
    'webodt.preprocessors.unescape_templatetags_preprocessor',
])
