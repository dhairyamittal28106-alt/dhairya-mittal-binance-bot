# Binance Futures Trading Bot (Testnet)

A lightweight Python CLI application for placing Market and Limit orders on the Binance Futures Testnet (USDT-M). Built with a modular structure for easy maintenance and testing.

## Project Structure
- `main.py`: Entry point for the CLI.
- `bot/client.py`: Binance API client initialization.
- `bot/orders.py`: Core logic for order execution.
- `bot/validators.py`: Input sanitization and validation.
- `bot/logging_config.py`: Centralized logging setup.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd trading_bot