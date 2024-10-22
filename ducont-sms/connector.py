"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from .operations import operations

logger = get_logger('ducont-sms')


class Ducont(Connector):
    def execute(self, config, operation, params, *args, **kwargs):
        try:
            logger.info('In execute() Operation: {}'.format(operation))
            operation = operations.get(operation)
            return operation(config, params, *args, **kwargs)
        except Exception as err:
            logger.error('An exception occurred {}'.format(err))
            raise ConnectorError('{}'.format(err))

    # unavailability of the API documentation health check functionality not implemented
    def check_health(self, config):
        pass