# Currency Converter

A simple and user-friendly currency conversion application built with Python and Streamlit. This project retrieves live exchange rates from the ExchangeRate-API and allows users to convert between hundreds of international currencies in real time.

## Features

- 🌍 Supports a wide range of global currencies
- 📈 Retrieves live exchange rates from ExchangeRate-API
- ⚡ Fast performance with cached exchange rates
- 🖥️ Interactive Streamlit web interface
- 💱 Accurate currency conversion calculations
- 🔄 Automatic exchange rate updates
- 🛡️ Error handling for network and API issues

## Project Structure

```text
CURRENCY-CONVERTOR/
├── src/
│   ├── app.py
│   ├── constants.py
│   ├── currency_convertor.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## How It Works

1. The user selects a base currency.
2. The user selects a target currency.
3. The user enters the amount to convert.
4. The application fetches the latest exchange rate from ExchangeRate-API.
5. The converted value is calculated and displayed instantly.
6. Exchange rates are cached for one hour to reduce API requests and improve performance.

## Technologies Used

- Python 3
- Streamlit
- Requests
- Cachetools
- ExchangeRate-API

## Installation

### Clone the Repository

```bash
git clone https://github.com/mohamadamin-kazemi/currency-convertor.git
cd currency-convertor
```

### Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

#### Activate on Windows

```bash
venv\Scripts\activate
```

#### Activate on macOS/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the Streamlit Application

From the project root directory:

```bash
streamlit run src/app.py
```

After launching, Streamlit will provide a local URL similar to:

```text
http://localhost:8501
```

Open the URL in your browser and start converting currencies.

### Command-Line Interface

The project also includes a CLI version of the converter.

Run:

```bash
python src/currency_convertor.py
```

Example:

```text
--- Currency Converter ---
Enter the amount to convert: 100
Enter the base currency (e.g., USD): USD
Enter the target currency (e.g., EUR): EUR

Fetching exchange rate for USD to EUR...
Success: 100.00 USD is equal to 85.00 EUR
```

## Supported Currencies

The application supports hundreds of international currencies, including:

- USD — United States Dollar
- EUR — Euro
- GBP — British Pound Sterling
- CAD — Canadian Dollar
- AUD — Australian Dollar
- JPY — Japanese Yen
- CHF — Swiss Franc
- CNY — Chinese Yuan
- INR — Indian Rupee
- AED — UAE Dirham

And many more.

## Caching

To improve performance and reduce unnecessary API requests, exchange rates are cached using `cachetools.TTLCache`.

Cache configuration:

```python
TTLCache(maxsize=100, ttl=60*60)
```

- Maximum cache entries: 100
- Cache duration: 1 hour

## Error Handling

The application gracefully handles:

- Network connection failures
- API request errors
- Invalid JSON responses
- Unsupported currency codes
- Invalid user input

## Requirements

```text
cachetools==7.1.4
Requests==2.34.2
streamlit==1.58.0
```

## API Source

Exchange rates are retrieved from:

https://api.exchangerate-api.com

## Repository

GitHub Repository:

https://github.com/mohamadamin-kazemi/currency-convertor

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more information.
