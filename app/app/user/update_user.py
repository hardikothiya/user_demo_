from shared.database import cursor

from fastapi import Depends
from .forms.update_user import UpdateUSerForm
from .route import user
from ..common_functions import resultset


@user.post("/user/update_user", tags=["User"])
async def update_user(
        form_data: UpdateUSerForm = Depends()
):
    try:
        exestr = f" update user_master set username = '{form_data.username}', city = '{form_data.city}', mobile_no = '{form_data.mobile_no}', address = '{form_data.address}' where email = '{form_data.email}'"

        cursor.execute(exestr)
        print("=================================")
        print("=++++++++++++++")
        return {f"{form_data.email} has been updated"}
    except Exception as e:
        print("exception============================", e)
