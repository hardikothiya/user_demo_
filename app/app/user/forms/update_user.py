from fastapi.param_functions import Body
from typing import Optional


class UpdateUSerForm:
    def __init__(
            self,
            email : str = Body(...),
            username: str = Body(...),
            address: str = Body(...),
            city: str = Body(...),
            mobile_no: int = Body(0)

    ):
        self.email = email
        self.username = username
        self.address = address
        self.city = city
        self.mobile_no = mobile_no
