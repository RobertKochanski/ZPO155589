from abc import ABC, abstractmethod


class User(ABC):
    permission:bool

    def __init__(self, permission:bool = True):
        self.permission = permission

    @abstractmethod
    def GET(self) -> None:
        pass

    @abstractmethod
    def POST(self) -> None:
        pass

class CurrentUser(User):
    def GET(self) -> None:
        print("User used: GET")

    def POST(self) -> None:
        print("User used: POST")

class CurrentUserProxy(User):
    currentUser: User

    def __init__(self, currentUser:User):
        super().__init__(currentUser.permission)
        self.currentUser = currentUser

    def GET(self) -> None:
        self.currentUser.GET()

    def POST(self) -> None:
        if self.currentUser.permission:
            self.currentUser.POST()
        else:
            print("User has no permission")


currentUser = CurrentUser()

proxy_user = CurrentUserProxy(currentUser)

proxy_user.GET()
proxy_user.POST()

blocked_user = CurrentUser(False)
proxy_blocked = CurrentUserProxy(blocked_user)

proxy_blocked.GET()
proxy_blocked.POST()
