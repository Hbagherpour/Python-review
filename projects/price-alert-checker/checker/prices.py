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

