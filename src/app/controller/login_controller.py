from fastapi import APIRouter, HTTPException, Depends
from app.model.login_model import LoginCredentials
from app.business.login_business import ILoginBusiness
from app.repository.impl.dynamodb.users_auth_dynamodb_repository import UsersAuthDynamoDBRepository

router = APIRouter(prefix="/login", tags=["Login"])

def get_auth_repository() -> UsersAuthDynamoDBRepository:
    return UsersAuthDynamoDBRepository()

def get_login_business(auth_repo: UsersAuthDynamoDBRepository = Depends(get_auth_repository)) -> ILoginBusiness:
    from app.business.impl.login_business_impl import LoginBusiness
    return LoginBusiness(auth_repo)

@router.post("")
def login(
    credentials: LoginCredentials,
    business: ILoginBusiness = Depends(get_login_business)
):
    try:
        auth_result = business.authenticate(credentials)
        return auth_result
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))