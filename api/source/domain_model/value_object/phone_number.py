import re


class PhoneNumber:
    def phone_number(self, phone_number) -> None:
        pattern = "^0\d{9,10}$"
        if re.match(pattern, phone_number) is None:
            raise ValueError("Invalid phone number format")

        self.phone_number = phone_number
