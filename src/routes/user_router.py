from fastapi import APIRouter


router = APIRouter()



@router.get("/user/{id}")
def get_user_by_id(id: int):
    pass

