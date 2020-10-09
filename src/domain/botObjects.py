class User:

    def __init__(self, id: str, name: str, ) -> None:
        self.id = id
        self.name = name
        super().__init__()


class Teacher(User):
    def __init__(self, id: str, name: str) -> None:
        super().__init__(id, name)


class Hometask:
    def __init__(self, id: int, group_id: str, ) -> None:
        self.id = id
        self.group_id = group_id
        super().__init__()


class Group:
    def __init__(self, id: str, ) -> None:
        self.id = id
        super().__init__()
