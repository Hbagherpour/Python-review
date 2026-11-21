#write get_rate(base, target) -> float | None. Use requests with a timeout, raise_for_status(), and catch requests.exceptions.RequestException. On any failure, log an error and return None.
#It should:
#call https://api.frankfurter.dev/v1/latest with params={"base": base, "symbols": target} and timeout=10
#call raise_for_status()
#return data["rates"][target]
#on any requests.exceptions.RequestException, log an error with the reason and return None
#handle a missing rate in the response (KeyError) the same way
#Use logger = logging.getLogger(__name__) and no basicConfig.

import logging
import requests

logger = logging.getLogger(__name__)

def get_rate(base: str, target: str) -> float | None:
    url = "https://api.frankfurter.dev/v1/latest"
    params = {"base": base, "symbols": target}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["rates"][target]
    except requests.exceptions.RequestException as e:
        logger.error("Request failed for %s/%s: %s", base, target, e)
        return None
    except KeyError:
        logger.error("Rate for %s/%s not found in response.", base, target)
        return None

