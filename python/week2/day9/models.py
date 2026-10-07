from datetime import UTC, datetime

from __future__ import annotations

from python.week2.day10.database import Base
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "users"

    '''tells sqlalchemy the name of
    s"'''

    """Mpapped[int] is a type hint that indicates that the id attribute is mapped to an integer column in the database. It helps with type checking and code readability."""

    """mapped_column specifies the properties of the column in the database, such as its data type, constraints, and indexing. In this case, it defines the id column as an integer primary key with an index."""

    """nullable false means a required field and unique true means no two users can have same username or email"""

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False,
    )

    image_file: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
        default=None,
    )

    """if user has uploaded image we willreturn it 
    usiong first return and if doesnt have it we will
    return it using the second return now we will use this 
    image file to display the profile picture of the user in 
    the frontend"""

    """we are seprating the statc file that re shipped with the file 
    it make deployemnets easier whenever you commiyt the code you dont want to commit user gentrete d content 
    you dont want to include the default pictures 
    or tings like that """

    posts: Mapped[list["Post"]] = relationship(back_populates="author")

    """back_populates help us in that to see user,post to get all the user post """

    """it is creating one-m,anyt relationship one user can have many posts but one post can have only one user"""

    """relationship is used to define the relationship between the User and Post models. It allows you to access the related posts of a user using the posts attribute."""

    """back_populates is used to specify the corresponding attribute in the related model (Post) that defines the reverse relationship. In this case, it indicates that the author attribute in the Post model corresponds to the posts attribute in the User model."""

    """cascade="all, delete-orphan" specifies that when a user is deleted, all their associated posts should also be deleted. It ensures that there are no orphaned posts left in the database when a user is removed."""

    @property
    def image_path(self) -> str:
        if self.image_file:
            return f"/media/profile_pics/{self.image_file}"
        return "/statics/profile_pics/default.jpg"


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    """ForeignKey("users.id") establishes a foreign key relationship between the user_id column in the Post model and the id column in the User model. It ensures that each post is associated with a valid user."""

    """index=True creates an index on the user_id column, which improves query performance when filtering"""

    """primary key gets index by default but for foreign key we have to create index manually"""

    """nullable false means a required field and unique true means no two users can have same username"""

    date_posted: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    author: Mapped["User"] = relationship(back_populates="posts")

    """default=lambda: datetime.now(UTC) sets the default value of the date_posted column to the current UTC datetime when a new post is created. It ensures that each post has a timestamp indicating when it was posted."""

    """it allows post.author to access the user who created the post and user.posts to access all the posts created by a specific user."""
