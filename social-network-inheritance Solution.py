# Define the Post class
class Post:
    def __init__(self, text):
        self.text = text
        self.user = None  # Initially, the post has no user

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}: "{self.text}"'

# Define the TextPost class
class TextPost(Post):
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}: "{self.text}"'

# Define the PicturePost class
class PicturePost(Post):
    def __init__(self, text, image_url):
        super().__init__(text)
        self.image_url = image_url

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}: "{self.text}"\n  Pic URL: {self.image_url}'

# Define the CheckInPost class
class CheckInPost(Post):
    def __init__(self, text, latitude, longitude):
        super().__init__(text)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f'{self.user.first_name} Checked In: "{self.text}"\n  {self.latitude}, {self.longitude}'

# Define the User class
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []  # List to hold posts
        self.following = []  # List of users this user follows

    def add_post(self, post):
        post.user = self  # Set the user of the post
        self.posts.append(post)  # Add post to user's posts

    def follow(self, user):
        self.following.append(user)  # Add user to following list

    def get_timeline(self):
        # Combine posts from users this user is following
        timeline = []
        for user in self.following:
            timeline.extend(user.posts)
        return sorted(timeline, key=lambda post: post.created_at, reverse=True)  # Sort by date

# Example usage
if __name__ == "__main__":
    # Create users
    john = User("John", "Lennon", "john@rmotr.com")
    paul = User("Paul", "McCartney", "paul@rmotr.com")
    george = User("George", "Harrison", "george@rmotr.com")

    # John creates a text post
    text_post = TextPost("All you need is love!")
    john.add_post(text_post)

    # Paul and George create their posts
    paul.add_post(TextPost("Post 1"))
    george.add_post(TextPost("Post 2"))
    paul.add_post(TextPost("Post 3"))

    # John follows Paul and George
    john.follow(paul)
    john.follow(george)

    # Print John's timeline
    print("John's Timeline:")
    for post in john.get_timeline():
        print(post)
