def calculate_total(food_type, quantity, discount_code=None):
    
    prices = {
        "پیتزا": 150000,
        "برگر": 120000,
        "سالاد": 80000
    }

    
    if food_type not in prices:
        return "خطا: نوع غذای وارد شده معتبر نیست"

    
    total_price = prices[food_type] * quantity

    
    if discount_code == "OFF20":
        discount = 0.20  
    elif total_price > 300000:
        discount = 0.15  
    else:
        discount = 0  

    
    final_price = total_price * (1 - discount)

    return f"قیمت نهایی سفارش: {int(final_price)} تومان"


food = input("نوع غذا (پیتزا، برگر، سالاد): ")
count = int(input("تعداد سفارش: "))
discount_code = input("کد تخفیف (در صورت وجود، در غیر این صورت خالی بگذارید): ")


print(calculate_total(food, count, discount_code))
