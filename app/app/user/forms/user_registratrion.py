from fastapi.param_functions import Body


class UserRegistratrionForm:
    def __init__(
            self,
            username: str = Body(...),
            email: str = Body(...),
            mobile_no: int = Body(0),
            address: str = Body(...),
            city: str = Body(...),
            password: str = Body(...),
            confirm_password: str = Body(...),
            state_id : int = Body(0)
    ):
        self.username = username
        self.email = email
        self.mobile_no = mobile_no
        self.address = address
        self.city = city
        self.password = password
        self.confirm_password = confirm_password
        self.state_id = state_id






