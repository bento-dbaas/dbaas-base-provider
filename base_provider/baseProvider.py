from .base import BaseProviderObject
from .base import MongoClient


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

    def wait_zone_operation(self, zone, operation):
        op = self.client.zoneOperations().wait(
            project=self.credential.project,
            zone=zone,
            operation=operation
        ).execute()
        return self._check_operation_status(op)

    def wait_global_operation(self, operation):
        op = self.client.globalOperations().wait(
            project=self.credential.project,
            operation=operation
        ).execute()
        self._check_operation_status(op)

    def _check_operation_status(self, operation):
        if operation.get('error'):
            error = 'Error in {} operation: {}'.format(
                operation.get('operationType'),
                operation.get('error')
            )
            raise Exception(error)

        if operation.get('status') != 'DONE':
            error = 'Operation {} is not Done. Status: {}'.format(
                operation.get('operationType'),
                operation.get('status')
            )
            raise Exception(error)

        return True
