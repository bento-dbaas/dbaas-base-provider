from recordclass import recordclass

MONGO_ENDPOINT = "fake_endpoint"
MONGODB_DB = "fake_db"
MONGODB_HOST = "fake_host"
MONGODB_PORT = "fake_port"
MONGODB_USER = "fake_user"
MONGODB_PWD = "fake_pass"


FAKE_CREDENTIAL = {'abc': 123}

FAKE_PROVIDER = "fake"

FAKE_SAVE_ID = "IDFAKE"


class CredentialAddFake(object):

    def __init__(self, provider, environment, content):
        pass

    def delete(self):
        pass
