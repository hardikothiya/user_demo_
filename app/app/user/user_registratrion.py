from shared.database import cursor

from fastapi import Depends
from .forms.user_registratrion import UserRegistratrionForm
from .route import user
from ..common_functions import resultset


@user.post("/user/user_registration", tags=["User"])
async def user_registration(
        form_data: UserRegistratrionForm = Depends()
):
    """ Register new user"""
    try:
        if form_data.password == form_data.confirm_password:
            try:
                exestr = f"insert into user_demo.dbo.user_master(username, email, password, confirm_password, address,city, mobile_no) values('{form_data.username}', '{form_data.email}', '{form_data.password}', '{form_data.confirm_password}', '{form_data.address}', '{form_data.city}', '{form_data.mobile_no}')"

                cursor.execute(exestr)

                return {
                    "message": "success",
                    "user added": f"{form_data.username}"

                }
            except Exception as e:
                print(e)
                return {" Error occurred": e}
        else:
            return {"Password doesnt match"}
    except Exception as e:
        print("exception============================", e)
        return {"Error occurred": e}
