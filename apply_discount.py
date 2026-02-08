def apply_discount(price, discount):
    """
    Calculate the final price after applying a percentage discount.

    Args:
        price (float): Original price (must be > 0)
        discount (float): Discount percentage (0–100)

    Returns:
        float: Final discounted price
    """

    if not isinstance(price, (int, float)):
        return "The price should be a number"

    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    return round(final_price, 2)
