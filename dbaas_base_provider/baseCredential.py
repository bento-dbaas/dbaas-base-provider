from collections import OrderedDict

from .base import BaseProviderObject
from .base import MongoClient


class BaseCredential(BaseProviderObject):

    MONGODB_PARAMS = None
    MONGODB_DB = None
    MONGO_ENDPOINT = None
    MONGODB_HOST = None
    MONGODB_USER = None
    MONGODB_PORT = None
    MONGODB_PWD = None
    MONGODB_DB = None
    provider_type = None

    def __init__(self, provider, environment):
        super(BaseCredential, self).__init__()
        self.provider = provider
        self.environment = environment
        self._db = None
        self._collection_credential = None
        self._content = None

    @property
    def db(self):
        if not self._db:
            if self.provider_type == "host_provider":
                params = {'document_class': OrderedDict}
                if self.MONGO_ENDPOINT is None:
                    params.update({
                        'host': self.MONGODB_HOST,
                        'port': self.MONGODB_PORT,
                        'username': self.MONGODB_USER,
                        'password': self.MONGODB_PWD
                    })
                    client = MongoClient(**params)
                else:
                    client = MongoClient(self.MONGO_ENDPOINT, **params)
                self._db = client[self.MONGODB_DB]
            elif self.provider_type == "volume_provider":
                client = MongoClient(**self.MONGODB_PARAMS)
                self._db = client[self.MONGODB_DB]
            else:
                # new provider needs implementation
                raise NotImplementedError
        return self._db

    @property
    def credential(self):
        if not self._collection_credential:
            self._collection_credential = self.db[self._credential_idx]
        return self._collection_credential

    @property
    def _credential_idx(self):
        return ("credentials"
                if self.provider_type == "volume_provider"
                else "credential")

    @property
    def content(self):
        if not self._content:
            raise NotImplementedError
        return self._content
