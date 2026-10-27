from binance.enums import *
from .logging_config import logger

def place_futures_order(client, symbol, side, order_type, quantity, price=None):
    try:
        
        payload = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity,
            
            
            'newOrderRespType': 'RESULT'
        }
        
        
        if order_type.upper() == 'LIMIT':
            payload['price'] = str(price)
            payload['timeInForce'] = TIME_IN_FORCE_GTC

        logger.info(f"Request: {payload}")
        
        
        response = client.futures_create_order(**payload)
        
        logger.info(f"Response: {response}")
        return response

    except Exception as e:
        logger.error(f"Order Error: {str(e)}")
        raise