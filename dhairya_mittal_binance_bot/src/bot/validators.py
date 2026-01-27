def validate_order_input(symbol, side, order_type, quantity, price):
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if not symbol.endswith('USDT'):
        raise ValueError("Symbol must be a USDT pair")
    
    if side not in ['BUY', 'SELL']:
        raise ValueError("Side must be BUY or SELL")
    
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError("Type must be MARKET or LIMIT")
    
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    
    if order_type == 'LIMIT' and (price is None or price <= 0):
        raise ValueError("Valid price is required for LIMIT orders")

    return symbol, side, order_type