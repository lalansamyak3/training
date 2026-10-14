from typing import Optional, Union

from pydantic import BaseModel
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.core.exceptions import AppError
from app.core.pagination import PageParams
from app.core.validators import calculate_age
from app.users.enums import Gender, Occupation
from app.users.models import User
from app.users.schemas import UserCreate


def get_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.get(User, user_id)


def get_by_email(db: Session, email: str) -> Optional[User]:
    return db.scalar(select(User).where(User.email == email.lower()))


def get_by_phone(db: Session, phone_no: str) -> Optional[User]:
    return db.scalar(select(User).where(User.phone_no == phone_no))


def get_by_aadhaar(db: Session, aadhaar_no: str) -> Optional[User]:
    return db.scalar(select(User).where(User.aadhaar_no == aadhaar_no))


def create_user(db: Session, data: UserCreate, hashed_password: str) -> User:
    user = User(
        **data.model_dump(exclude={"password", "confirm_password"}),
        hashed_password=hashed_password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user: User, data: BaseModel) -> User:
    changes = data.model_dump(exclude_unset=True)

    new_age = changes.get("age", user.age)
    new_dob = changes.get("dob", user.dob)
    if calculate_age(new_dob) != new_age:
        raise AppError("Age does not match the date of birth", 422)

    new_phone = changes.get("phone_no")
    if new_phone and new_phone != user.phone_no and get_by_phone(db, new_phone):
        raise AppError("Phone number already registered", 409)

    for field, value in changes.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()


def list_users(
    db: Session,
    params: PageParams,
    search: Union[str, None] = None,
    gender: Optional[Gender] = None,
    occupation: Optional[Occupation] = None,
    city: Union[str, None] = None,
) -> tuple[list[User], int]:
    stmt = select(User)
    if search:
        like = f"%{search}%"
        stmt = stmt.where(
            or_(
                User.name.ilike(like), User.email.ilike(like), User.phone_no.ilike(like)
            )
        )
    if gender:
        stmt = stmt.where(User.gender == gender)
    if occupation:
        stmt = stmt.where(User.occupation == occupation)
    if city:
        stmt = stmt.where(User.city.ilike(city))

    total = db.scalar(select(func.count()).select_from(stmt.subquery())) or 0
    items = db.scalars(
        stmt.order_by(User.id.desc()).offset(params.offset).limit(params.size)
    ).all()
    return list(items), total


"""1. Get user by ID
Finds a user using their unique ID. If a matching user exists, it returns that user; otherwise, it returns None.
2. Get user by email
Searches the database for a user with the given email address. It converts the supplied email to lowercase before searching, helping with consistent email lookup.
3. Get user by phone number
Searches the database for a user whose phone number matches the provided number. If no match exists, it returns None.
4. Get user by Aadhaar number
Searches for a user with the specified Aadhaar number. This helps check whether a record associated with that number already exists.
5. Create a user
Creates and saves a new user in the database.
- Takes the validated user data and the already-hashed password.
- Excludes the plain password and confirmation password from the user data.
- Stores the hashed password instead of the original password.
- Adds the new user to the database session.
- Commits the transaction to save the user permanently.
- Refreshes the user object to retrieve database-generated values, such as the ID.
- Returns the newly created user.
6. Update a user
Updates an existing user's information.
- Reads only the fields provided in the update request.
- Uses the existing age or date of birth when either field is not supplied.
- Checks whether the age matches the date of birth. If they do not match, it raises an error with status code 422, meaning the supplied data is invalid.
- Checks whether a newly supplied phone number already belongs to another user. If it does, it raises 409 Conflict.
- Applies the requested changes to the user.
- Commits the changes to the database, refreshes the user object, and returns the updated user.
7. Delete a user
Deletes an existing user from the database.
It marks the user for deletion and commits the transaction so that the deletion is saved.
8. List users
Retrieves a list of users and supports searching, filtering, and pagination.
It accepts the database session, pagination settings, and optional filters for search text, gender, occupation, and city.
Search: Searches for matching text in the user's name, email, or phone number. The search is case-insensitive.
Gender filter: Returns only users whose gender matches the requested value.
Occupation filter: Returns only users whose occupation matches the requested value.
City filter: Returns users whose city matches the supplied city, ignoring case. In the current implementation, it checks for a match against the whole city value rather than searching for a partial city name.
These filters can be combined, allowing the application to narrow the results.
Total count: Counts all users matching the filters before pagination is applied. This lets the frontend know how many matching records exist overall.
Sorting: Orders users by ID in descending order, so higher IDs appear first.
Pagination: Skips records according to the requested offset and returns no more than the requested page size. This prevents the application from loading every matching user at once.
Finally, it returns two things:
- The list of users for the requested page.
- The total number of users matching the filters, before pagination."""
