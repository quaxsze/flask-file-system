import codecs
import io
import logging
import re

from contextlib import contextmanager

from flask import send_file
from gridfs import GridFS
from pymongo import MongoClient

from . import BaseBackend

log = logging.getLogger(__name__)


class GridFsBackend(BaseBackend):
    """
    A Mongo GridFS backend

    Expects the following settings:

    - `mongo_url`: The Mongo access URL
    - `mongo_db`: The database to store the file in.
    """
    def __init__(self, name, config):
        super().__init__(name, config)

        self.client = MongoClient(config.mongo_url)
        self.db = self.client[config.mongo_db]
        self.fs = GridFS(self.db, self.name)

    def exists(self, filename):
        return self.fs.exists(filename=filename)

    @contextmanager
    def open(self, filename, mode='r', encoding='utf8'):
        if 'r' in mode:
            f = self.fs.get_last_version(filename)
            yield f if 'b' in mode else codecs.getreader(encoding)(f)
        else:  # mode == 'w'
            f = io.BytesIO() if 'b' in mode else io.StringIO()
            yield f
            params = {'filename': filename}
            if 'b' not in mode:
                params['encoding'] = encoding
            self.fs.put(f.getvalue(), **params)

    def read(self, filename):
        f = self.fs.get_last_version(filename)
        return f.read()

    def write(self, filename, content):
        kwargs = {
            'filename': filename
        }

        if hasattr(content, 'content_type') and content.content_type is not None:
            kwargs['content_type'] = content.content_type

        return self.fs.put(self.as_binary(content), **kwargs)

    def delete(self, filename):
        regex = '^{0}'.format(re.escape(filename))
        for version in self.fs.find({'filename': {'$regex': regex}}):
            self.fs.delete(version._id)

    def copy(self, filename, target):
        src = self.fs.get_last_version(filename)
        self.fs.put(src, filename=target, content_type=src.content_type)

    def list_files(self):
        for f in self.fs.list():
            yield f

    def serve(self, filename):
        file = self.fs.get_last_version(filename)
        return send_file(file, mimetype=file.content_type)

    def get_metadata(self, filename):
        f = self.fs.get_last_version(filename)
        return {
            'checksum': 'md5:{0}'.format(f.md5),
            'size': f.length,
            'mime': f.content_type,
            'modified': f.upload_date,
        }
