import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Madhuri.Jasti\\PycharmProjects\\RobatFramework\\Configurations\\config.ini")


def get_browser():
    return config.get("basic_info", "browser")


def get_url():
    return config.get("basic_info", "url")
