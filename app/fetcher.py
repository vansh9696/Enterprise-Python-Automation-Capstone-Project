import pandas as pd
import requests

def fetch_telemetry_data() -> pd.DataFrame:
    """Simulates or fetches enterprise operational telemetry logs."""
    data = {
        "Service": ["Auth-Service", "Payment-Gateway", "User-Microservice", "Telemetry-Worker", "Database-Proxy"],
        "Requests": [14200, 9800, 22100, 5400, 31000],
        "Uptime_Pct": [99.98, 99.91, 100.00, 98.45, 99.99],
        "Avg_Latency_ms": [42.1, 120.4, 18.2, 210.0, 8.5]
    }
    return pd.DataFrame(data)