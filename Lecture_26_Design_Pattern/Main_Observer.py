class YoutubeChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def upload_video(self, title):
        print(f"Video '{title}' uploaded")

        for user in self.subscribers:
            user.notify(f"New video '{title}' uploaded.")


class User:
    def __init__(self, name):
        self.name = name

    def notify(self, video_title):
        print(f"{self.name} received notification:"
              f"{video_title}")


channel = YoutubeChannel()
user1 = User("George")
user2 = User("David")

channel.subscribe(user1)
channel.subscribe(user2)

channel.upload_video("Titanic")