from fastapi.param_functions import Body


class DeleteUserForm:
    def __init__(
            self,
            email: str = Body(...),
    ):
        self.email = email
