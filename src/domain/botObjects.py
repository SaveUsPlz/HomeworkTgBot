class User:

    def __init__(self, id: str, name: str,) -> None:
        self.id = id
        self.name = name
        super().__init__()


class Teacher(User):
    def __init__(self, id: str, name: str,) -> None:
        super().__init__(id, name)