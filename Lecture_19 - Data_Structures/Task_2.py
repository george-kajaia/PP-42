from collections import Counter

class Users:
    user_list = ["gio", "ნინო", "gio", "ანა", "ნიკა", "ანა"]

    @staticmethod
    def get_unique_users():
        suer_set = set(Users.user_list)
        print(f"The site was visited by {len(suer_set)} unique users: {suer_set}", "\n")

    @staticmethod
    def get_user_visit_count():
        name_counts = Counter(Users.user_list)

        for name, count in name_counts.items():
            print(f"{name} visited the site {count} times")

Users.get_unique_users()
Users.get_user_visit_count()