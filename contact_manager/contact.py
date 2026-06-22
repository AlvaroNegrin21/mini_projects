"""
Contact class: represents a single contact with name, phone,
and email, and supports conversion to/from dict for JSON storage.
"""

class Contact:
    """Represents a contact with name, phone, and email."""

    def __init__(self, name, phone, email):
        """Initializes a new contact.

        Args:
            name (str): contact's name.
            phone (str): contact's phone number.
            email (str): contact's email address.
        """
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        """Converts the contact to a dictionary, for JSON storage.

        Returns:
            dict: dictionary with name, phone, and email.
        """
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Contact instance from a dictionary (loaded from JSON).

        Args:
            data (dict): dictionary with name, phone, and email.

        Returns:
            Contact: the reconstructed contact instance.
        """
        return cls(data["name"], data["phone"], data["email"])