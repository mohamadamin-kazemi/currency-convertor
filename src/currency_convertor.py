"""
Currency Converter Module
=========================

This script provides a command-line interface to convert amounts between 
different currencies using the ExchangeRate-API.
"""

import requests
from requests.exceptions import RequestException
from typing import Optional

API_BASE_URL = "https://api.exchangerate-api.com/v4/latest/"


def get_exchange_rate(base_currency: str, target_currency: str) -> Optional[float]:
    """
    Fetch the live exchange rate for a given currency pair.

    :param base_currency: The 3-letter currency code to convert from (e.g., 'USD').
    :param target_currency: The 3-letter currency code to convert to (e.g., 'EUR').
    :return: The exchange rate if successful, otherwise ``None``.
    """
    base = base_currency.strip().upper()
    target = target_currency.strip().upper()
    url = f"{API_BASE_URL}{base}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        rate = data.get("rates", {}).get(target)
        
        if rate is None:
            print(f"Error: Target currency '{target}' not found in the API response.")
            return None
            
        return float(rate)

    except RequestException as e:
        print(f"Error: Failed to retrieve data from the network. Details: {e}")
        return None
    except ValueError:
        print("Error: Received an invalid JSON response from the API.")
        return None


def convert_currency(amount: float, exchange_rate: float) -> float:
    """
    Calculate the converted currency amount.

    :param amount: The original monetary amount to convert.
    :param exchange_rate: The current conversion rate.
    :return: The calculated final amount.
    """
    return amount * exchange_rate


def main() -> None:
    """
    Main controller for parsing user input and orchestrating the conversion.
    """
    print("--- Currency Converter ---")
    
    while True:
        try:
            amount_input = input("Enter the amount to convert: ").strip()
            amount = float(amount_input)
            if amount < 0:
                print("Error: Please enter a positive amount.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value (e.g., 100.50).")

    base_currency = input("Enter the base currency (e.g., USD): ").strip()
    target_currency = input("Enter the target currency (e.g., EUR): ").strip()

    print(f"\nFetching exchange rate for {base_currency.upper()} to {target_currency.upper()}...")
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is not None:
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"Success: {amount:.2f} {base_currency.upper()} is equal to "
              f"{converted_amount:.2f} {target_currency.upper()}")
    else:
        print("Conversion failed due to the errors above.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram cancelled by user. Exiting.")
