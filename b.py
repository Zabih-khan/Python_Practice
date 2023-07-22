class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    
    def print(self):
        
        space= ' ' * self.get_level()*3
        prefix= space + "|--" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print()


def build_product_tree():
    root=TreeNode("Electronic")
    
    laptop=TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone=TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Google pixel"))
    cellphone.add_child(TreeNode("Vivo"))
    cellphone.add_child(TreeNode("Nokai"))

    Tv=TreeNode("TV")
    Tv.add_child(TreeNode("Sumsung"))
    Tv.add_child(TreeNode("LG"))
    
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(Tv)

    root.print()

    
if __name__=="__main__":
    build_product_tree()
    





    
