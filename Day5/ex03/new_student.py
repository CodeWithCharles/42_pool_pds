import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a 15-character random student ID.

    The ID consists of lowercase letters from 'a' to 'z'.

    Returns:
        str: The generated 15-character student ID.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class representing a student with basic personal information.

    Attributes:
        name (str): First name of the student.
        surname (str): Last name of the student.
        active (bool): Whether the student is currently active.
        login (str): Generated login name, created from first initial\
and surname.
        id (str): Unique student ID generated automatically.
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Initialize fields that depend on other fields after dataclass\
__init__.

        - `login` is set as the capitalized first letter of `name`
          followed by the lowercase `surname`.
        """
        self.login = self.name[0].capitalize() + self.surname.lower()
