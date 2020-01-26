import endpoints
import json
import requests


class Charts:
    def __init__(self):
        self.session = requests.Session()

    def get_top_artist(self, format_json=True, artists=None):
        """
        Get a list of top artists
        :param format_json: bool: response will be returned by default in Json format, if False it'll be XML
        :param artists: int: limit of artists per page, boundary 1-1000
        :return: code and text of response
        """
        endpoint = endpoints.top_artist
        if format_json:
            endpoint += endpoints.json

        if artists:
            endpoint += f'{endpoints.limit}{artists}'

        response = self.session.get(endpoint)
        return response.status_code, json.loads(response.text)
