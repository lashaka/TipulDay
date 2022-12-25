import constants as const


class user_settings_util(object):
    def clear_command_line(self: object) -> None:
        """Clear the command line.

        Args:
            self: Main class instance.

        Returns:
            None.
        """
        __import__(const.LIBRARIES_TEXT[0]).system(
            const.CLEAR_COMMAND_TEXT[0]
            if __import__(const.LIBRARIES_TEXT[0]).name == const.WINDOWS_OS_NAME_TEXT
            else const.CLEAR_COMMAND_TEXT[1]
        )

    def get_google_search_value(self: object) -> str:
        """
        Get the value of the search string from the user.
        :param self: The object.
        :return: The search string.
        """
        SEARCH_STRING = input(const.SEARCH_STRING_INPUT_TEXT)
        return str(SEARCH_STRING)

    def get_amount_of_websites_to_send_forms_to(self: object) -> int:
        """
        Get the amount of websites to send forms to.
        :param self:
        :param const:
        :return:
        """
        AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO = input(
            const.AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO_INPUT_TEXT
        )
        return int(AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO)

    def get_add_specific_search_website(self: object) -> bool:
        """
        Ask the user if they want to add a specific search website.
        :return: True if the user wants to add a specific search website, False otherwise.
        """
        ADD_SPECIFIC_SEARCH_WEBSITE = input(const.ADD_SPECIFIC_SEARCH_WEBSITE_TEXT)
        if (
            ADD_SPECIFIC_SEARCH_WEBSITE.lower()
            == const.ADD_SPECIFIC_SEARCH_WEBSITE_YES_NO_TEXT[0]
        ):
            return True
        elif (
            ADD_SPECIFIC_SEARCH_WEBSITE.lower()
            == const.ADD_SPECIFIC_SEARCH_WEBSITE_YES_NO_TEXT[1]
        ):
            return False
        else:
            print(const.ADD_SPECIFIC_SEARCH_WEBSITE_INVALID_INPUT_TEXT)
            exit()

    def get_form_name(self: object) -> str:
        """
        Get form name from user
        :param self:
        :param const:
        :return:
        """
        FORM_NAME = input(const.FORM_NAME_TEXT)
        return str(FORM_NAME)

    def get_form_email(self: object) -> str:
        """
        Get form email from user.
        :param self: object
        :return: str
        """
        FORM_EMAIL = input(const.FORM_EMAIL_TEXT)
        return str(FORM_EMAIL)

    def get_form_phone(self: object) -> int:
        """
        Get phone number from user
        :return: int
        """
        FORM_PHONE = input(const.FORM_PHONE_TEXT)
        return int(FORM_PHONE)

    def get_form_comment(self: object) -> str:
        """
        Get comment from user
        :return: str
        """
        FORM_COMMENT = input(const.FORM_COMMENT_TEXT)
        if FORM_COMMENT == None:
            FORM_COMMENT = ""
        return str(FORM_COMMENT)

    def get_all_data(self: object) -> list:
        """
        Get all data from the user.

        :return: list
        """
        SEARCH_STRING = self.get_google_search_value()
        self.clear_command_line()
        AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO = (
            self.get_amount_of_websites_to_send_forms_to()
        )
        self.clear_command_line()
        FORM_NAME = self.get_form_name()
        self.clear_command_line()
        FORM_EMAIL = self.get_form_email()
        self.clear_command_line()
        FORM_PHONE = self.get_form_phone()
        self.clear_command_line()
        FORM_COMMENT = self.get_form_comment()
        self.clear_command_line()
        ADD_SPECIFIC_WEBSITES = self.get_add_specific_search_website()
        self.clear_command_line()
        return [
            SEARCH_STRING,
            AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO,
            FORM_NAME,
            FORM_EMAIL,
            FORM_PHONE,
            FORM_COMMENT,
            ADD_SPECIFIC_WEBSITES,
        ]


if __name__ == "__main__":
    constants = user_settings_util().get_all_data()
    print(constants)
