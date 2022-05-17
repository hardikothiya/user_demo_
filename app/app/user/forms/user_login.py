from fastapi.param_functions import Body


class UserLoginForm:
    def __init__(
            self,
            email: str = Body(...),
            password: str = Body(...)
    ):
        self.email = email
        self.password = password
