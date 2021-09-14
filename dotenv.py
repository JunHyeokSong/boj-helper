class dotEnv :
    def __init__(self) :
        with open('.env', 'r') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines if line[0]!='#']
        self.attributes = {}
        for line in lines : 
            attribute = line.split('=')
            self.attributes[attribute[0].strip()] = attribute[1].strip()

    def getAttributes(self) :
        return self.attributes

    def getAttribute(self, name) :
        return self.attributes[name]

if __name__ == '__main__' :
    dotenv = dotEnv()
    print(dotenv.getAttributes())
    

         