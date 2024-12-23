from db_models.candidate_post_model import CandidatePost_DB
from db_models.election_post_model import ElectionPost_DB
from .base_model import BaseModel_DB
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy


if TYPE_CHECKING:
    from .user_model import User_DB
    from .election_model import Election_DB


class Candidate_DB(BaseModel_DB):
    __tablename__ = "candidate_table"

    candidate_id: Mapped[int] = mapped_column(primary_key=True, init=False)

    election_id: Mapped[int] = mapped_column(ForeignKey("election_table.election_id"))

    election: Mapped["Election_DB"] = relationship("Election_DB", back_populates="candidates", init=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))

    user: Mapped["User_DB"] = relationship("User_DB", back_populates="candidates", init=False)

    candidate_posts: Mapped[list["CandidatePost_DB"]] = relationship(
        back_populates="candidate", cascade="all, delete-orphan", init=False
    )

    posts: AssociationProxy[list["ElectionPost_DB"]] = association_proxy(
        target_collection="candidate_posts", attr="election_post", init=False
    )

    pass