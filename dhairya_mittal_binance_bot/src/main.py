import click
import time
from bot.client import get_binance_client
from bot.validators import validate_order_input
from bot.orders import place_futures_order
from bot.logging_config import logger

@click.command()
@click.option('--symbol', required=True)
@click.option('--side', required=True, type=click.Choice(['BUY', 'SELL'], case_sensitive=False))
@click.option('--type', 'order_type', required=True, type=click.Choice(['MARKET', 'LIMIT'], case_sensitive=False))
@click.option('--qty', required=True, type=float)
@click.option('--price', type=float)
def main(symbol, side, order_type, qty, price):
    try:
        symbol, side, order_type = validate_order_input(symbol, side, order_type, qty, price)
        
        client = get_binance_client()

        # Fix for the -1021 Timestamp Error
        server_time = client.get_server_time()['serverTime']
        local_time = int(time.time() * 1000)
        client.timestamp_offset = server_time - local_time
        
        order_data = place_futures_order(client, symbol, side, order_type, qty, price)
        
        print("\n--- Order Summary ---")
        print(f"Order ID: {order_data.get('orderId')}")
        print(f"Status:   {order_data.get('status')}")
        print(f"Quantity: {order_data.get('executedQty')}")
        print(f"Price:    {order_data.get('avgPrice', price)}")
        print("Successfully placed order.")
        
    except Exception as e:
        print(f"\nExecution failed: {e}")

if __name__ == '__main__':
    main()