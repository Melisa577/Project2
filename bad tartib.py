def sort_string(input_string):
    # حروف، اعداد و کاراکترهای خاص را در لیستهای جداگانه قرار میدهیم
    special_chars = []
    letters = []
    digits = []

    # حلقه برای بررسی هر کاراکتر در رشته ورودی
    for char in input_string:
        if char.isalpha():  # اگر کاراکتر حرف باشد
            letters.append(char)
        elif char.isdigit():  # اگر کاراکتر عدد باشد
            digits.append(char)
        elif not char.isspace():  # اگر کاراکتر فضای خالی نباشد
            special_chars.append(char)

    # حروف را به ترتیب الفبایی مرتب میکنیم
    letters.sort()
    # اعداد را به ترتیب مرتب میکنیم
    digits.sort()

    # بازگشت لیستی با ترتیب مشخص (علامتهای خاص، اعداد، حروف)
    # برای حفظ ترتیب، ابتدا کاراکترهای خاص، سپس اعداد و سپس حروف را به هم میچسبانیم
    sorted_string = ''.join(special_chars) + ''.join(digits) + ''.join(letters)

    return sorted_string


# دریافت ورودی از کاربر
input_string = input("لطفا رشته ورودی را وارد کنید: ")
# نمایش خروجی مرتبشده
print(sort_string(input_string))