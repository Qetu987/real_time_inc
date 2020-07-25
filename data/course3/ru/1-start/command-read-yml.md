# Команда чтения yml.

    pip install pyyaml
     
Пример чтения.

    import yaml

    def get_meta(self,path):
        if isfile(path):
            f = open(path,'r')
            str = f.read()
            f.close()
            yml = yaml.load(str)
            return yml
        else:
            return False
