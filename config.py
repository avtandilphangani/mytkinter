import configparser
import os

class config:

    def __init__(self,path="settings.ini") -> None:
        if not os.path.exists(path):
            config = configparser.ConfigParser()
            config.add_section("Settings")
            with open(path, "w") as config_file:
                config.write(config_file)

if __name__ == "__main__":
    
    con = config("bla.ini")
    con2 = config("config.ini")