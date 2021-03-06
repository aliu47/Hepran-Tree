class evenSugar:
    def __init__(self, name, parity, position, parent):
        self.name = name
        self.parity = parity
        self.parent = parent
        self.children = []
        self.position = position

    def canLink(self):
        if(self.parent):
            return getattr(self, str(self.name))()
        return False

    def GlcNAc(self):
        if(self.parent.name == "GlcA"):
            if(self.parent.parent):
                if("6S" in self.parent.parent.name):
                    return False
            return True
        else:
            return False

    def GlcNAc6S(self):
        if(self.parent.name == "GlcA"):
            if(self.parent.parent):
                if(self.parent.parent == "GlcNS"):
                    return False
            return True
        else:
            return False

    def GlcNS(self):
        if(self.parent.name == "GlcA" or self.parent.name == "GlcA2S" or self.parent.name == "IdoA" or self.parent.name == "IdoA2S"):
            if(self.parent.parent):
                if(self.parent.parent == "GlcNS"):
                    return False
            return True
        else:
            return False

    def GlcNS6S(self):
        if(self.parent.name == "GlcA" or self.parent.name == "GlcA2S" or self.parent.name == "IdoA" or self.parent.name == "IdoA2S"):
            if(self.parent.parent):
                if(self.parent.parent == "GlcNS"):
                    return False
            return True
        else:
            return False

    def GlcNS6S3S(self):
        if(self.parent.name == "IdoA2S"):
            if(self.parent.parent):
                if(self.parent.parent == "GlcNS"):
                    return False
            return True
        else:
            return False
