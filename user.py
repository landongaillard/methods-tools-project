class User:
    def __init__(self, id: str, username: str, password: str, email: str, address_line_1: str, address_line_2: str, contact_num: str) -> None:
        self.__id: str = id
        self.__username: str = username
        self.__password: str = password
        self.__email: str = email
        self.__address_line_1: str = address_line_1
        self.__address_line_2: str = address_line_2
        self.__contact_num: str = contact_num

    def login(self, email: str, password: str) -> None:
        pass

    def createAccount(self) -> None:
        pass

    def exitProgram(self) -> None:
        pass
    