def josephus(n, k):
    """محاسبهی موقعیت آخرین نفر باقیمانده"""
    if n == 1:
        return 0  # تنها یک نفر که باقی مانده است
    else:
        # بازگشت به حل مسئله با n-1 نفر
        return (josephus(n - 1, k) + k) % n


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # تعداد آزمون ها
    x = int(data[0])
    results = []

    for i in range(1, x + 1):
        line = data[i].strip()
        if line == "*":
            break

        # اطلاعات آزمایش
        numbers = list(map(int, line.split()))
        n = 100  # مقدار پیشفرض n
        k = 2  # مقدار پیشفرض k

        if len(numbers)
            >= 1:
n = numbers[0]  # اگر n داده شده باشد از آن استفاده کن
if len(numbers)
    >= 2:
    k = numbers[1]  # اگر k داده شده باشد از آن استفاده کن

    # محاسبهی شخصیت آزاد شده
safe_position = josephus(n, k) + 1  # +1 برای نمایش موقعیت در نمای نهایی
results.append(safe_position)  # ذخیره نتیجه در لیست

# چاپ نتایج
for result in results:
    print(result)

if _name_ == "__main__":
    main()