for attempt in range(3):  # Retry up to 3 times
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            text = "Ok"
            break
    except requests.exceptions.RequestException:
        time.sleep(2)  # Wait 2 seconds before retrying
        text = "Request failed after 3 attempts."

