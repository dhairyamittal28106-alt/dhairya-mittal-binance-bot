# Binance Futures Trading Bot

A Python command-line application for placing market and limit orders on the Binance USDT-M Futures Testnet. It separates API access, order logic, input validation, and logging, and includes OCO and TWAP helper modules.

## Setup

Use Python 3.10 or newer:

    cd dhairya_mittal_binance_bot
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # macOS/Linux: source .venv/bin/activate
    pip install -r requirements.txt

Create a local `.env` file with testnet API credentials expected by the client. Do not commit keys. Keep the bot on testnet while checking order parameters.

## Run

    python src/main.py

## Modules

- `src/main.py`: command-line entry point
- `src/bot/client.py`: Binance client setup
- `src/bot/orders.py`: market and limit order operations
- `src/bot/validators.py`: request/input validation
- `src/advanced/`: OCO and TWAP helpers

This software can place financial orders. Review all settings and test with a testnet account before considering any live use.
