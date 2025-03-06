def determine_age(national_id):
  
    if not (national_id.isdigit() and len(national_id) == 10):
        return "کد ملی نامعتبر است. لطفاً یک کد ۱۰ رقمی وارد کنید."

    birth_year = int(national_id[:2])

    if 0 <= birth_year <= 10:
        return "فرد زیر ۲۵ سال است."
    elif 60 <= birth_year <= 90:
        return "فرد بالای ۳۰ سال است."
    else:
        return "فرد بین ۲۵ تا ۳۰ سال دارد."

national_id = input("کد ملی ۱۰ رقمی را وارد کنید: ")
print(determine_age(national_id))
