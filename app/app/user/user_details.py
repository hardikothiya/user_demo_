from shared.database import cursor

from fastapi import Depends
from .forms.user_details import UserDetailsForm
from .route import user
from ..common_functions import resultset


@user.post("/user/user_details", tags=["User"])
async def user_details(
        form_data: UserDetailsForm = Depends()
):
    try:
        exestr = f" select * from user_master where email = '{form_data.email}'"

        cursor.execute(exestr)
        print(cursor)
        y = resultset(cursor)
        print(y)
        return {
            "code": "success",
            "data": y

        }

    except Exception as e:
        print("exception============================", e)
        return {"Error occurred": e}
