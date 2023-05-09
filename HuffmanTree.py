class HuffTree:

    def __init__ (self,left,right,mid):

        self.left=left
        self.right=right
        self.mid=mid
 #defining getters and setters to get and set left, right, and mid nodes
    def get_mid(self):
        return self.mid
    
    def set_mid(self,val):
        self.mid = val

    def get_right(self):
        return self.right

    def set_right(self,val):
        self.right=val

    def get_left(self):
        return self.left

    def set_left(self,val):
        self.left = val
