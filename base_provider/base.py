from pymongo import MongoClient, ReturnDocument


class BaseProviderObject(object):
    credential = None
    client = None

    def __init__(self, *args, **kwargs):
        pass


class BaseProvider(BaseProviderObject):
    def __init__(self, environment, auth_info=None):
        self.environment = environment
        self._client = None
        self._credential = None
        self._commands = None
        self.auth_info = auth_info

    @property
    def client(self):
        if not self._client:
            self._client = self.build_client()
        return self._client

    @property
    def credential(self):
        if not self._credential:
            self._credential = self.build_credential()
        return self._credential

    def credential_add(self, content):
        credential_cls = self.get_credential_add()
        credential = credential_cls(self.provider, self.environment, content)
        is_valid, error = credential.is_valid()
        if not is_valid:
            return False, error

        try:
            insert = credential.save()
        except Exception as e:
            return False, str(e)
        else:
            return True, insert.get('_id')

    def build_client(self):
        raise NotImplementedError

    def build_credential(self):
        raise NotImplementedError

    def get_credential_add(self):
        raise NotImplementedError

    @classmethod
    def get_provider(cls):
        raise NotImplementedError

    @property
    def provider(self):
        return self.get_provider()


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
