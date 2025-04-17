class ProfileService():

    def __init__(self, user):
        self.user = user

    def get_profile(self):
        return {"name": self.user.name}
