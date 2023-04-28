import logging

import requests

log = logging.getLogger('trevorspray.sprayers.base')

def send_slack_message(message: str, slack_url: str):
    log.info('Sending slack message: %s' % message)
    data = {'Message': message}
    response = requests.post(url=slack_url, json=data)
    if response.status_code != 200:
        raise ValueError(f'Slack returned non-200 status code. Response: "{response.text}" URL: "{slack_url}"')