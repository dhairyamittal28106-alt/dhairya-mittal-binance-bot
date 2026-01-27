from binance.enums import *
from .logging_config import logger

def place_futures_order(client, symbol, side, order_type, quantity, price=None):
    try:
        # Construct the basic order payload
        payload = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity,
            # 'RESULT' returns the full filled data for Market orders
            # and the final status (Filled/Expired) for Limit orders
            'newOrderRespType': 'RESULT'
        }
        
        # Add limit-specific parameters
        if order_type.upper() == 'LIMIT':
            payload['price'] = str(price)
            payload['timeInForce'] = TIME_IN_FORCE_GTC

        logger.info(f"Request: {payload}")
        
        # Execute the order on Binance Futures (testnet is handled by the client)
        response = client.futures_create_order(**payload)
        
        logger.info(f"Response: {response}")
        return response

    except Exception as e:
        logger.error(f"Order Error: {str(e)}")
        raise