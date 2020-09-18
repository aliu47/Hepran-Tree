class oddSugar:
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

    def GlcA(self):
        if(self.parent.parity == "even"):
            return True
        else:
            return False

    def GlcA2S(self):
        if(self.parent.name == "GlcNS" and self.position == 3):
            return True
        else:
            return False

    def IdoA(self):
        if(self.parent.name == "GlcNS" or self.parent.name == "glcNS6S" and self.position == 3):
            return True
        else:
            return False

    def IdoA2S(self):
        if(self.parent.name == "GlcNS" or self.parent.name == "glcNS6S"):
            return True
        else:
            return False
