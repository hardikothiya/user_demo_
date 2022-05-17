from fastapi.param_functions import Body


class UserDetailsForm:
    def __init__(
            self,
            email: str = Body(...),

    ):
        self.email = email

