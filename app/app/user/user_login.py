from shared.database import cursor

from fastapi import Depends
from .forms.user_login import UserLoginForm
from .route import user
from ..common_functions import resultset


@user.post("/user/user_login", tags=["User"])
async def user_login(
        form_data: UserLoginForm = Depends()
):
    """Login User"""
    try:
        exestr = f"select * from user_demo.dbo.user_master where email = '{form_data.email}'"

        cursor.execute(exestr)
        data = resultset(cursor)
        if data[0][0]['password'] == form_data.password:

            return {
                f"{form_data.email}": "logged in sucessfullyyyy"
            }

        else:
            return {
                "logged in fails"
            }
    except Exception as e:
        print("exception============================", e)
