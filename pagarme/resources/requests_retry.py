import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from pagarme import sdk

def headers():
    _headers = {
        'User-Agent': 'pagarme-python/{}'.format(sdk.VERSION),
        'X-PagarMe-User-Agent': 'pagarme-python/{}'.format(sdk.VERSION)
    }
    return _headers

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    session.headers.update(headers())

    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    return session
