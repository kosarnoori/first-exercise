def validate_login(username, password):
    if not username or not password:
        return "خطا: نام کاربری یا رمز عبور خالی است."
    
    if len(password) < 8:
        return "خطا: رمز عبور باید حداقل ۸ کاراکتر باشد."
    
    if not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
        return "خطا: رمز عبور باید شامل حداقل یک عدد و یک حرف بزرگ باشد."
    
    if username.lower() == "admin":
        return "پیغام: ورود مدیر"
    
    return "ورود موفق"

# دریافت ورودی از کاربر
username = input("نام کاربری: ")
password = input("رمز عبور: ")

# بررسی و نمایش نتیجه
print(validate_login(username, password))
