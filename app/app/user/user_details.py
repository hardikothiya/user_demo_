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

        exestr2 = f"select user_demo.dbo.user_master.email, user_demo.dbo.state_list.states from " \
                  f"user_demo.dbo.user_master, user_demo.dbo.state_list where user_demo.dbo.user_master.state_id = " \
                  f"user_demo.dbo.state_list.id and user_demo.dbo.user_master.email = '{form_data.email}' "

        cursor.execute(exestr2)

        print(cursor)
        y = resultset(cursor)



        return {
            "code": "success",
            "data": y

        }

    except Exception as e:
        print("exception============================", e)
        return {"Error occurred": e}
