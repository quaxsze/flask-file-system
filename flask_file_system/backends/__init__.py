from flask_file_system import files

__all__ = [i.encode('ascii') for i in ('BaseBackend', 'DEFAULT_BACKEND')]


DEFAULT_BACKEND = 'local'


class BaseBackend:
    """
    Abstract class to implement backend.
    """
    root = None
    DEFAULT_MIME = 'application/octet-stream'

    def __init__(self, name, config):
        self.name = name
        self.config = config

    def exists(self, filename):
        """Tests wether a file exists or not given its filename in the storage"""
        raise NotImplementedError()

    def open(self, filename, *args, **kwargs):
        """Opens a file given its filename relative to the storage root"""
        raise NotImplementedError()

    def read(self, filename):
        """Reads a file content given its filename in the storage"""
        raise NotImplementedError()

    def write(self, filename, content):
        """Writes content into a file given its filename in the storage"""
        raise NotImplementedError()

    def delete(self, filename):
        """Deletes a file given its filename in the storage"""
        raise NotImplementedError()

    def copy(self, filename, target):
        """Copies a file given its filename to another path in the storage"""
        raise NotImplementedError()

    def move(self, filename, target):
        """
        Moves a file given its filename to another path in the storage

        Default implementation performs a copy then a delete.
        Backends should overwrite it if there is a better way.
        """
        self.copy(filename, target)
        self.delete(filename)

    def save(self, file_or_wfs, filename, overwrite=False):
        """
        Saves a file-like object or a `werkzeug.FileStorage` with the specified filename.

        :param storage: The file or the storage to be saved.
        :param filename: The destination in the storage.
        :param overwrite: if `False`, raises an exception if file exists in storage

        :raises FileExists: when file exists and overwrite is set to `False`
        """
        self.write(filename, file_or_wfs.read())
        return filename

    def metadata(self, filename):
        """
        Fetches all available metadata for a given file
        """
        meta = self.get_metadata(filename)
        # Fixes backend mime misdetection
        meta['mime'] = meta.get('mime') or files.mime(filename, self.DEFAULT_MIME)
        return meta

    def get_metadata(self, filename):
        """
        Backend specific method to retrieve metadata for a given file
        """
        raise NotImplementedError()

    def serve(self, filename):
        """Serves a file given its filename"""
        raise NotImplementedError()

    def as_binary(self, content, encoding='utf8'):
        """Performs content encoding for binary write"""
        if hasattr(content, 'read'):
            return content.read()
        elif isinstance(content, str):
            return content.encode(encoding)
        else:
            return content
