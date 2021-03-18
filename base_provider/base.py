class BaseProviderObject(object):
    def __init__(self, *args, **kwargs):
        pass


class BaseProvider(BaseProviderObject):
    def __init__(self, *args, **kwargs):
        print('Initializing base provider...')


class BaseCredential(BaseProviderObject):
    def __init__(self, *args, **kwargs):
        print('Initializing base credential...')
