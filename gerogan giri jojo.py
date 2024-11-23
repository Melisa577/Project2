def is_prime(num):
    """چک میکند که آیا عدد ورودی اول است یا خیر."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    # ورودی n: بزرگترین عدد موجود در غربال
    n = int(input())
    # ورودی m: عددی که باید بررسی شود
    m = int(input())

    # اگر m عددی اول باشد
    if is_prime(m):
        print(-1)
        return

    # غربال اراتوستن تا عدد n
    is_composite = [False] * (n + 1)

    for p in range(2, n + 1):
        if not is_composite[p]:  # اگر p اول باشد
            for multiple in range(p * p, n + 1, p):
                is_composite[multiple] = True  # عدد را خط بزنید

    # حالا بررسی میکنیم که m در چه زمان خط میخورد
    count = 0
    for num in range(2, n + 1):
        if not is_composite[num]:  # اگر عدد اول باشد
            count += 1
            if count == m:  # اگر به m رسیدیم
                print(num)
                return


# فراخوانی تابع اصلی
main()