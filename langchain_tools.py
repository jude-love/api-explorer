import requests
from langchain.agents import tool

@tool
def get_users():
    """Fetches all users from the API."""
    response = requests.get("http://127.0.0.1:5000/users")
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()

@tool
def get_products():
    """Fetches all products from the API."""
    response = requests.get("http://127.0.0.1:5000/products")
    response.raise_for_status()
    return response.json()

@tool
def get_purchases():
    """Fetches all purchases from the API."""
    response = requests.get("http://127.0.0.1:5000/purchases")
    response.raise_for_status()
    return response.json()

@tool
def get_complaints():
    """Fetches all complaints from the API."""
    response = requests.get("http://127.0.0.1:5000/complaints")
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    # Example usage:
    users = get_users()
    print("Users:", users)

    products = get_products()
    print("Products:", products)

    purchases = get_purchases()
    print("Purchases:", purchases)

    complaints = get_complaints()
    print("Complaints:", complaints)