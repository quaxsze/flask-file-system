import mimetypes
import os.path

__all__ = (
    'TEXT', 'DOCUMENTS', 'IMAGES', 'AUDIO', 'DATA', 'SCRIPTS', 'ARCHIVES', 'EXECUTABLES',
    'DEFAULTS', 'ALL', 'NONE', 'All', 'AllExcept', 'DisallowAll'
)

# Plain text files format.
TEXT = ['txt']

# Various office document formats
# Macro-enabled versions of Microsoft Office 2007 files are not included.
DOCUMENTS = 'rtf odf ods gnumeric abw doc docx xls xlsx'.split()

# Basic image types, viewable from most browsers.
IMAGES = 'jpg jpe jpeg png gif svg bmp'.split()

# Audio file types.
AUDIO = 'wav mp3 aac ogg oga flac'.split()

# Structured data files types.
DATA = 'csv ini json plist xml yaml yml'.split()

# Various types of scripts.
# If your Web server has PHP installed and set to auto-run,
# you might want to add ``php`` to the DENY setting.
SCRIPTS = 'js php pl py rb sh bat'.split()

# Archive and compression types.
ARCHIVES = 'gz bz2 zip tar tgz txz 7z'.split()

# Shared libraries and executable files.
# Most of the time, you will not want to allow this - it's better suited for use with `AllExcept`.
EXECUTABLES = 'so exe dll'.split()

# Default allowed extensions - `TEXT`, `DOCUMENTS`, `DATA`, and `IMAGES`.
DEFAULTS = TEXT + DOCUMENTS + IMAGES + DATA


def extension(filename):
    ext = os.path.splitext(filename)[1]
    if ext.startswith('.'):
        # os.path.splitext retains . separator
        ext = ext[1:]
    return ext.lower()


def lower_extension(filename):
    """
    A helper used by :meth:`Storage.save` to provide lowercase extensions for
    all processed files, to compare with configured extensions in the same
    case.
    :param str filename: The filename to ensure has a lowercase extension.
    """
    if '.' in filename:
        main, ext = os.path.splitext(filename)
        return main + ext.lower()
    # For consistency with os.path.splitext,
    # do not treat a filename without an extension as an extension.
    # That is, do not return filename.lower().
    return filename


def mime(filename, default=None):
    """
    Helper to guess mime type from a filename or url
    """
    return mimetypes.guess_type(filename)[0] or default


class All:
    """
    Can be used to allow all extensions.
    There is a predefined instance named `ALL`.
    """

    def __contains__(self, item):
        return True


class DisallowAll:
    """
    This type can be used to disallow all extensions.
    There is a predefined instance named `NONE`.
    """

    def __contains__(self, item):
        return False


# "Contains" all items. Can be used to allow all extensions to be uploaded.
ALL = All()

# "Contains" no items. Can used to force an whitelist by configuration.
NONE = DisallowAll()


class AllExcept:
    """
    This can be used to allow all file types except certain ones.
    For example, to exclude .exe and .iso files, pass::
        AllExcept(('exe', 'iso'))
    to the :class:`~flask_file_system.Storage` constructor as `extensions` parameter.
    You can use any container, for example::
        AllExcept(SCRIPTS + EXECUTABLES)
    """

    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item not in self.items
