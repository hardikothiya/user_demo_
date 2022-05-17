from shared.database import cursor

from fastapi import Depends
from .forms.delete_user import DeleteUserForm
from .route import user
from ..common_functions import resultset


@user.post("/user/delete_user", tags=["User"])
async def delete_user(
        form_data: DeleteUserForm = Depends()
):
    try:
        exestr = f" delete from user_demo.dbo.user_master where email  = '{form_data.email}'"

        cursor.execute(exestr)


        return {
            "code": "success",
            "data": "user deleted successfully"

        }

    except Exception as e:
        print("exception============================", e)
        return {"Error occurred" : e}
