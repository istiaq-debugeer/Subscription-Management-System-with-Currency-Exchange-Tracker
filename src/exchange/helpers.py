import requests


def get_exchange_rates(base: str, target: str):
    url = f"https://v6.exchangerate-api.com/v6/2c4750bcb38a08424d1f44ef/latest/{base}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data.get("conversion_rates", {}).get(target)
        if rate:
            return {"base": base, "target": target, "rate": rate}
        else:
            return {"error": f"Target currency '{target}' not found in exchange data"}
    else:
        return {"error": f"Failed to fetch data. Status: {response.status_code}"}
