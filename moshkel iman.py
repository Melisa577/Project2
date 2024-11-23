grade_to_points = {
    'A': 5,
    'B': 4,
    'C': 3,
    'E': 1,
    'F': 0
}

# ورودی تعداد امتحانات را از کاربر میگیریم.
n = int(input("تعداد امتحانات: "))  # تعداد امتحانات را ورودی میگیریم.

total_weighted_score = 0  # مجموع نمرات وزنی را صفر اولیه میگذاریم.
total_weight = 0  # مجموع وزنها را نیز صفر اولیه میگذاریم.

# حال، برای هر امتحان، ورودیهای مربوطه را دریافت میکنیم.
for _ in range(n):  # به تعداد n بار تکرار میکنیم.
    line = input().strip()  # ورودی را میخوانیم و فضاهای اضافی را حذف میکنیم.
    weight_str, grade = line.split()  # ورودی را به وزن و نمره تقسیم میکنیم.
    weight = int(weight_str)  # وزن را به عدد صحیح تبدیل میکنیم.

    # نمره وزنی را محاسبه میکنیم و آن را به مجموع اضافه میکنیم.
    total_weighted_score += grade_to_points[grade] * weight  # نمره وزنی را محاسبه کرده و به مجموع اضافه میکند.
    total_weight += weight  # وزن را به مجموع وزنها اضافه میکنیم.

    # اگر مجموع وزنها صفر باشد، میانگین محاسبه نمیکنیم.
    if total_weight == 0:
        average_grade = 'F'  # اگر وزنی نداریم، میتوانیم 'F' را برگردانیم.
    else:
        average_score = total_weighted_score / total_weight  # میانگین نمرات وزنی را محاسبه میکنیم.

        # حال میانگین را به نمره توصیفی تبدیل میکنیم.
        if average_score >= 4:
            average_grade = 'A'
        elif average_score >= 3:
            average_grade = 'B'
        elif average_score >= 2:
            average_grade = 'C'
        elif average_score >= 1:
            average_grade = 'E'
        else:
            average_grade = 'F'

    # در انتها، نمره میانگین را چاپ میکنیم.
    print(average_grade)  # نمره میانگین را چاپ میکنیم.