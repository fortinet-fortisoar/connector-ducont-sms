"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import json
import requests
from connectors.core.connector import get_logger, ConnectorError
from connectors.core.connector import Connector
import ast
from .constants import PRIORITY
logger = get_logger('ducont-sms')

class Ducont(object):

    def __init__(self, config):
        self.server_url = config.get('server_url').strip()
        self.headers = {'Content-Type': 'application/json'}
        if not self.server_url.startswith('http://'):
            self.server_url = 'http://{0}'.format(self.server_url)

    def make_api_call(self, endpoint=None, method='GET', headers=None, data=None):
        url = self.server_url + endpoint
        logger.debug('API Endpoint URL: %s', url)
        if headers:
            self.headers.update(headers)
        logger.debug('Making a %s request with headers: %s', method, self.headers)
        try:
            response = requests.request(method, url, headers=self.headers, data=data)
            logger.debug('Received response with status code: %d', response.status_code)
            if response.ok:
                try:
                    response_data = response.json()
                    status = response_data.get('status', 'Success')
                    return {'status': status, 'data': response_data}
                except ValueError as e:
                    response_data = response.content
                    logger.error('JSON decoding failed: %s. Response content: %s', e, response_data)
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Request failed with status code: %d, response: %s', response.status_code, response.text)
                return {'status': 'Failure', 'status_code': response.status_code, 'response': response.text}
        except requests.RequestException as e:
            logger.exception('Request failed: %s', e)
            return {'status': 'Failure', 'error': str(e)}


def push_sms(config, params, *args, **kwargs):
    template_variables = params.get('template_variables')
    if not template_variables: 
        template_variables_value = {}
    else:
        template_variables_value = ast.literal_eval(template_variables)
    payload = {
        "userId": str(config.get('user_id')),
        "password": str(config.get('password')),
        "channelId": str(params.get('channel_id', "")),
        "senderId": str(params.get('sender_id')),
        "messageId": str(params.get('message_id')),
        "priority": PRIORITY.get(params.get('priority')),
        "recipients": str(params.get('recipients', "")).split(','),
        "templateId": str(params.get('template_id', "")),
        "templateVariables": template_variables_value,
        "statusCallbackURL": str(params.get('status_callback_url', "")),
        "confirmDelivery": params.get('confirm_delivery'),
        "validityPeriod": str(params.get('validity_period')),
        "body": str(params.get('body')),
    }
    obj = Ducont(config)
    endpoint = '/RESTAPISMS/api/Service/PushSMS'
    response = obj.make_api_call(endpoint=endpoint, method='POST', data=json.dumps(payload))
    return response


def push_sms_sub(config, params, *args, **kwargs):
    template_variables = params.get('template_variables')
    if not template_variables: 
        template_variables_value = {}
    else:
        template_variables_value = ast.literal_eval(template_variables)
    payload = {
        "userId": str(config.get('user_id')),
        "password": str(config.get('password')),
        "channelId": str(params.get('channel_id', "")),
        "senderId": str(params.get('sender_id')),
        "messageId": str(params.get('message_id')),
        "priority": PRIORITY.get(params.get('priority')),
        "recipients": str(params.get('recipients', "")).split(','),
        "templateId": str(params.get('template_id', "")),
        "templateVariables":template_variables_value,
        "statusCallbackURL": str(params.get('status_callback_url', "")),
        "confirmDelivery": params.get('confirm_delivery'),
        "validityPeriod": str(params.get('validity_period')),
        "body": str(params.get('body')),
        "languageId": str(params.get('language_id'))
    }
    obj = Ducont(config)
    endpoint = '/RESTAPISMS/api/Service/PushSMSSub'
    response = obj.make_api_call(endpoint=endpoint, method='POST', data=json.dumps(payload))
    return response 


operations = {
    'push_sms': push_sms,
    'push_sms_sub': push_sms_sub
}

