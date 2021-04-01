from pymongo import MongoClient, ReturnDocument


class BaseProviderObject(object):
    _provider_type = None

    def __init__(self, *args, **kwargs):
        if not self.provider_type:
            raise EnvironmentError('Invalid provider type')

    @property
    def provider_type(self):
        if self._provider_type:
            return self._provider_type
        raise NotImplementedError

    @provider_type.setter
    def provider_type(self, prov_type):
        self._provider_type = prov_type
