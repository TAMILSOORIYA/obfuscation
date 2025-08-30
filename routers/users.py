from fastapi import APIRouter
from services.user_service import get_users
from models.user import User
from testdirectory.test_dir import test_dir

router = APIRouter(prefix="/obfuscation_sample", tags=["users"])

@router.get("/users", response_model=list[User])
def list_users():
    return get_users()

@router.get("/")
def root():
    return {"message": "Hello from FastAPI CSR example"}

@router.get("/external_directory")
def testdir():
    return test_dir()
