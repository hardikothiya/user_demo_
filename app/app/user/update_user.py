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
        if 1 <= form_data.state_id <= 36:
            exestr = f" update user_master set username = '{form_data.username}', city = '{form_data.city}', mobile_no = '{form_data.mobile_no}', address = '{form_data.address}', state_id = '{form_data.state_id}' where email = '{form_data.email}'"

            cursor.execute(exestr)
            print("=================================")
            return {f"{form_data.username} has been updated"}
        else:
            return {"Invalid state id"}

    except Exception as e:
        print("exception============================", e)
