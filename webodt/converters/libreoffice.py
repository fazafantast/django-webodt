# -*- coding: utf-8 -*-
import os
from webodt import Document
from webodt.conf import WEBODT_LIBREOFFICE_COMMAND, WEBODT_TMP_DIR
from webodt.converters import ODFConverter
from webodt.helpers import get_mimetype
import subprocess


class LibreofficeODFConverter(ODFConverter):

    def convert(self, document, extend=None, output_filename=None, delete_on_close=True):
        extend = extend or self._get_extend()
        output_file_path, _ = os.path.splitext(document.name)

        args = [extend, document.name, '--outdir', WEBODT_TMP_DIR]
        my_env = os.environ.copy()
        my_env['HOME'] = WEBODT_TMP_DIR
        process = subprocess.Popen(WEBODT_LIBREOFFICE_COMMAND + args, env=my_env, stdin=subprocess.PIPE)  # stdout=subprocess.PIPE, stderr=subprocess.PIPE
        process.communicate('\n')

        if process.returncode != 0:
            return document

        document_name = '.'.join([output_file_path, extend])
        fd = Document(document_name, delete_on_close=delete_on_close)
        fd.content_type = get_mimetype(extend)
        return fd
