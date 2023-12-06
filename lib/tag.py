class Tag:

    def __init__(self, id, name, posts = []):
        self.id = id
        self.name = name
        self.posts = posts

    def __eq__(self, other):
        return self.__dict__ == other

    def __repr__(self):
        return f"Tag({self.id}, {self.name})"