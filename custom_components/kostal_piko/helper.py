from numbers import Number
import requests
import logging

_LOGGER = logging.getLogger('KostalPikoClient')


class KostalPikoClient:
    def __init__(self, host: str, username: str, password: str):
        self._host = host
        self._url = "http://" + self._host + "/api/dxs.json?dxsEntries="
        self.session = requests.Session()
        self.session.auth = (username, password)

    def get_data(self, dxs_id: Number):
        response = self.session.get(url=self._url + str(dxs_id), timeout=10)
        _LOGGER.info(f'Got response {response.text}...')

        try:
            data = response.json()

            for entry in data['dxsEntries']:
                if entry['dxsId'] == dxs_id:
                    return entry['value']
        except KeyError as e:
            raise Exception(
                f'Kostal response does not match expected format for dxsId {dxs_id}. Got error {repr(e)} for response {response.text}'
            )
        except requests.exceptions.JSONDecodeError as e:
            raise Exception(
                f'Kostal response has invalid format. Response was {response.text}: {repr(e)}'
            )

        raise Exception(
            f'Kostal response did not contain dxs_id {dxs_id}: {response.text}')
