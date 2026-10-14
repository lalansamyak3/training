from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Occupation(str, Enum):
    STUDENT = "student"
    SALARIED = "salaried"
    SELF_EMPLOYED = "self_employed"
    BUSINESS = "business"
    HOMEMAKER = "homemaker"
    RETIRED = "retired"
    UNEMPLOYED = "unemployed"
    OTHER = "other"


class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"
