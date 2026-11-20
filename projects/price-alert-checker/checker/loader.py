# write load_alerts(path) that reads the file, skips bad alerts with a logged warning, and returns the good ones. Also handle a missing file or broken JSON without a crash.

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def load_alerts(path: Path) -> list[dict]:
    try:
        with open(path, 'r' , encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        logger.error("Alerts file not found: %s", path)
        return []
    except json.JSONDecodeError as e:
        logger.error("Alerts file is not valid JSON: %s", e)
        return []

    alerts = []
    for alert in data.get("alerts", []):
        if not all(key in alert for key in ["base", "target", "condition", "threshold"]):
            logger.warning("Skipping incomplete alert: %s", alert)
            continue

        if alert["condition"] not in ["above", "below"]:
            logger.warning("Skipping alert with invalid condition: %s", alert)
            continue

        if not isinstance(alert["threshold"], (int, float)):
            logger.warning("Skipping alert with non-number threshold: %s", alert)
            continue

        alerts.append(alert)

    return alerts

