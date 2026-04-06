class APIClient:
    def __init__(self, request_context):
        self.request = request_context
        # New base URL: No Auth required!
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_post(self, post_id):
        return self.request.get(f"{self.base_url}/posts/{post_id}")

    def create_post(self, title, body, user_id):
        payload = {"title": title, "body": body, "userId": user_id}
        return self.request.post(f"{self.base_url}/posts", data=payload)
