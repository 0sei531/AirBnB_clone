#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review for a place.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new Review instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")

    def __str__(self):
        """Returns a string representation of the Review instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary representation of the Review instance."""
        review_dict = super().to_dict()
        review_dict.update({
            "place_id": self.place_id,
            "user_id": self.user_id,
            "text": self.text
        })
        return review_dict

