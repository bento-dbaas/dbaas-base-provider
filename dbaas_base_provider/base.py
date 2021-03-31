from pymongo import MongoClient, ReturnDocument


class BaseProviderObject(object):
    def __init__(self, *args, **kwargs):
        pass

    @property
    def provider_type(self):
        raise NotImplementedError
