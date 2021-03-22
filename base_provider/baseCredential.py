from .base import BaseProviderObject
from .base import MongoClient

class BaseCredential(BaseProviderObject):

    MONGODB_PARAMS = None
    MONGODB_DB = None
    provider_type = None

    def __init__(self, provider_type, provider, environment):
        self.provider_type = provider_type
        self.provider = provider
        self.environment = environment
        self._db = None
        self._collection_credential = None
        self._content = None

    @property
    def db(self):
        if not self._db:
            client = MongoClient(**self.MONGODB_PARAMS)
            self._db = client[self.MONGODB_DB]
        return self._db

    @property
    def credential(self):
        if not self._collection_credential:
            self._collection_credential = self.db["credentials"]
        return self._collection_credential

    @property
    def content(self):
        return self._content
