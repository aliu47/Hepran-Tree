import oddSugar
import evenSugar

class Tree:
    def __init__(self):
        self.evenSugars = ["GlcNAc", "GlcNAc6S","GlcNS","GlcNS6S"]
        self.oddSugars = ["GlcA","GlcA2S","IdoA","IdoA2S"]

    def tree(self):
        # Send an even parent sugar in to see what odd sugar children can connect
        def oddLoop(self, parent, n):
            # end function under these conditions
            if parent.position == n:
                return
            # for each sugar in the odd sugar list
            for name in self.oddSugars:
                # set the child sugar's parent and position
                sugar = oddSugar.oddSugar(
                    str(name), "odd", int(parent.position+1), parent)
                # check if the child can link with the parent
                if(sugar.canLink()):
                    # link child to parent
                    parent.children.append(sugar)
                    # if this parent has children check each child to see if it has grand children
                    evenLoop(self, sugar, n)

        # Send an odd sugar parent in to see what even sugar children can connect
        def evenLoop(self, parent, n):
            # end function under these conditions
            if parent.position == n:
                return
            for name in self.evenSugars:
                # set the child sugar's parent and position
                sugar = evenSugar.evenSugar(
                    str(name), "even", int(parent.position+1), parent)
                # check if the child can link with the parent
                if(sugar.canLink()):
                    # link child to parent
                    parent.children.append(sugar)
                    # if this parent has children check each child to see if it has grand children
                    oddLoop(self, sugar, n)

        #This display is used to view children, depth, etc.
        def display(sugar):
            result = ""
            result = "parent: "+sugar.name+"\nchildren: "
            print("depth: "+str(sugar.position))
            for child in sugar.children:
                # append the child to the result
                result = result + child.name+' | '
                # call the function again for each child
            print(result)
            for child in sugar.children:
                display(child)

        #This display is suppose to be used to view the structure *Not fully working
        def display2(sugar,result):
            # result = ""
            # result = "parent: "+sugar.name+"\nchildren: "
            # print("depth: "+str(sugar.position))
            if(len(sugar.children) == 0):
                print(result)

            for child in sugar.children:
                # append the child to the result
                result = result + child.name+' | '
                # call the function again for each child
                display2(child,result)

        a = oddSugar.oddSugar("GlcA", "odd", 1, None)
        evenLoop(self, a, 6)
        display2(a,a.name)
        # b = evenSugar.evenSugar("GlcNAc6S", "even", 0, None)
        # oddLoop(self, b, 5)
        # display(b)


a = Tree()
a.tree()
