def check_bank_card(card_number):
    
    if not (card_number.isdigit() and len(card_number) == 16):
        return "شماره کارت نامعتبر است."

    if card_number.startswith("6037"):
        return "این کارت متعلق به بانک ملت است"
    elif card_number.startswith("5892"):
        return "این کارت متعلق به بانک صادرات است"
    elif card_number.startswith("6274"):
        return "این کارت متعلق به بانک سامان است"
    else:
        return "بانک نامشخص است."

card_number = input("شماره کارت 16 رقمی را وارد کنید: ")
print(check_bank_card(card_number))
