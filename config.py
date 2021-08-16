import configparser
import os

class config:
    path = ""
    config = None
    def __init__(self,path="settings.ini") -> None:
        self.path=path
        self.config = configparser.ConfigParser()
        if not os.path.exists(self.path):
            self.__write_config()
        else:
             with open(self.path) as config_file:
                self.config.read_file(config_file) 

    def __write_config(self):
            with open(self.path, "w") as config_file:
                self.config.write(config_file)

    def set_section(self,section='Common'):
        self.config.add_section(section)
        self.__write_config()

    def set_option(self,section,option,value):
        self.config.set(section,option,value)
        self.__write_config()

    def get_config(self):
        self.config.read(self.path)
        return self.config
    
    def get_option(self,section,option):
    #    self.get_config(self)
        return self.config.get(section,option)
    def options(self,section):
        return self.config.options(section)    

if __name__ == "__main__":
    
    con = config()
    print(con.config['ZZ']['ip'])
