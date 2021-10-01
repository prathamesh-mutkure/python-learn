import requests

api_url = "https://api.npoint.io/4af156202f984d3464c3"


class Post:

    all_posts = []

    def __init__(self, _id, body, title, subtitle):
        self.id = _id
        self.body = body
        self.title = title
        self.subtitle = subtitle

    @staticmethod
    def get_all_post():
        all_posts = []
        response = requests.get(url=api_url)
        response.raise_for_status()

        data = response.json()

        for item in data:
            post = Post(_id=item["id"], body=item["body"], title=item["title"], subtitle=item["subtitle"])
            all_posts.append(post)

        return all_posts

    @staticmethod
    def get_post_by_id(all_post: [], _id):
        for post in all_post:
            if post.id == _id:
                return post

