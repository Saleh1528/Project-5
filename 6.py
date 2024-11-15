import time

FILE_NAME = "survey.txt"  # نام فایل ذخیره نظرات


def save_vote(vote):
    """ذخیره نظر در فایل"""
    with open(FILE_NAME, "a") as file:
        file.write(f"{vote}\n")


def get_votes():
    """خواندن تمامی نظرات از فایل"""
    try:
        with open(FILE_NAME, "r") as file:
            votes = [int(line.strip()) for line in file]
        return votes
    except FileNotFoundError:
        return []


def calculate_satisfaction(votes):
    """محاسبه درصد رضایت"""
    if not votes:
        return 0  # اگر نظری وجود ندارد
    satisfied = votes.count(1)
    return (satisfied / len(votes)) * 100


def main():
    print("به نظرسنجی ما خوش آمدید! لطفاً نظر خود را ثبت کنید:")
    while True:
        print("\n1. ثبت نظر (0 = ناراضی، 1 = راضی)")
        print("2. نمایش درصد رضایت")
        print("3. خروج")
        choice = input("لطفاً یک گزینه را وارد کنید (1/2/3): ")

        if choice == "1":
            try:
                vote = int(input("نظر خود را وارد کنید (0 یا 1): "))
                if vote in [0, 1]:
                    save_vote(vote)
                    print("نظر شما با موفقیت ثبت شد.")
                else:
                    print("لطفاً فقط عدد 0 یا 1 وارد کنید.")
            except ValueError:
                print("ورودی نامعتبر است! فقط عدد وارد کنید.")
        elif choice == "2":
            votes = get_votes()
            satisfaction = calculate_satisfaction(votes)
            print(f"\nتعداد کل نظرات: {len(votes)}")
            print(f"درصد رضایت: {satisfaction:.2f}%")
        elif choice == "3":
            print("خروج از برنامه...")
            time.sleep(1)
            break
        else:
            print("گزینه نامعتبر است. لطفاً دوباره تلاش کنید.")


main()
