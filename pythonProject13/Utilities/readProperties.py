import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\Madhuri.Jasti\\PycharmProjects\\pythonProject13\\Configurations\\config.ini")

class Read_login_details:

    @staticmethod
    def get_url():
        return config.get("login_details","url")

    @staticmethod
    def get_username():
        return config.get("login_details", "username")

    @staticmethod
    def get_password():
        return config.get("login_details", "password")

    @staticmethod
    def get_otp():
        return config.get("login_details", "otp")