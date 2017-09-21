# -*- coding: utf8 -*-
from webodt.conf import WEBODT_DEFAULT_ext, WEBODT_TMP_DIR
import mimetypes
import tempfile
import os


def get_mimetype(ext):
    extend = '.%s' % ext
    map = mimetypes.types_map.copy()
    map['.odt'] = 'application/vnd.oasis.opendocument.text'
    map['.rtf'] = 'text/richtext'
    mimetype = map[extend]
    return mimetype


def guess_extend_and_filename(filename, ext):
    """ guess ext and filename of the output document

    Either ext and filename or both can be undefined (None) variables.
    Function determines undefined variables on basis of file extension or
    default values. If needed, temporary file will be created and returned.

    @return: tuple of strings (filename, ext)
    """
    # filename is defined, ext is undefined
    if filename and '.' in filename and not ext:
        ext = filename.split('.')[-1]
    # ext is undefined
    if not ext:
        ext = WEBODT_DEFAULT_ext
    # filename is undefined
    if not filename:
        lowlevel_fd, filename = tempfile.mkstemp(suffix='.' + ext, dir=WEBODT_TMP_DIR)
        os.close(lowlevel_fd)
    return filename, ext
