def calculate_final_price(device_price, weight_kg):
    # Constants
    INSURANCE_RATE       = 0.03  # 3% insurance
    SHIPPING_COST_PER_KG = 15  # $15 per kg
    DELIVERY_CHARGE      = 3.5  # Fixed delivery charge
    COMMISSION_FLAT      = 30  # Flat commission if price < $500
    COMMISSION_RATE      = 0.10  # 10% commission if price >= $500
    EXCHANGE_RATE        = 135  # USD to KES

    # Calculating insurance
    insurance_cost = device_price * INSURANCE_RATE

    # Calculating shipping cost
    shipping_cost = weight_kg * SHIPPING_COST_PER_KG

    # Calculating commission
    if device_price < 500:
        commission = COMMISSION_FLAT
    else:
        commission = device_price * COMMISSION_RATE

    # Total cost (supplier price + insurance + shipping + delivery + commission)
    total_cost_usd = device_price + insurance_cost + shipping_cost + DELIVERY_CHARGE + commission

    # Convert to KES
    total_cost_kes = total_cost_usd * EXCHANGE_RATE

    return round(total_cost_kes, 2)


# Example usage
if __name__ == "__main__":
    while True:
        price       = float(input("Enter the device price from the supplier: $"))
        weight      = float(input("Enter the device weight in kg: "))
        final_price = calculate_final_price(price, weight)
        print(f"The final price of the device is: KES {final_price}\n")
