
# class GFG:
#     def __init__(self, val):
#         self.left = None
#         self.right = None
#         self.data = val
# class Pagoda:
#     def __init__(self):
#         self.root = None
#     def is_empty(self):
#         return self.root is None
#     def clear(self):
#         self.root = None
#     def insert(self, val_list):
#         val = val_list[1]
#         node = GFG(val)
#         self.root = self._insert(node, self.root)

#     def _insert(self, node, queue):
#         node.left = node
#         node.right = node
#         return self._merge(queue, node)

#     def delete(self):
#         if self.root is None:
#             print("empty heap")
#         else:
#             self.root = self._delete(self.root)

#     def _delete(self, queue):
#         if queue is None:
#             print("Empty")
#             return None
#         l = r = None
#         if queue.left == queue:
#             l = None
#         else:
#             l = queue.left
#             while l.left != queue:
#                 l = l.left
#             l.left = queue.left
#         if queue.right == queue:
#             r = None
#         else:
#             r = queue.right
#             while r.right != queue:
#                 r = r.right
#             r.right = queue.right
#         return self._merge(l, r)

#     def _merge(self, root, newnode):
#         if root is None:
#             return newnode
#         elif newnode is None:
#             return root
#         else:
#             botroot = root.right
#             root.right = None
#             botnew = newnode.left
#             newnode.left = None
#             r = None
#             while botroot is not None and botnew is not None:
#                 if botroot.data > botnew.data:
#                     temp = botroot.right
#                     if r is None:
#                         botroot.right = botroot
#                     else:
#                         botroot.right = r.right
#                         r.right = botroot
#                     r = botroot
#                     botroot = temp
#                 else:
#                     temp = botnew.left
#                     if r is None:
#                         botnew.left = botnew
#                     else:
#                         botnew.left = r.left
#                         r.left = botnew
#                     r = botnew
#                     botnew = temp

#             if botnew is None:
#                 root.right = r.right
#                 r.right = botroot
#                 return root
#             else:
#                 newnode.left = r.left
#                 r.left = botnew
#                 return newnode
            
#     def find_min(self):
#         if self.root:
#             return self.root.data
#         else:
#             print ("empty tree")
class GFG:
    def __init__(self, val, letter):
        self.left = None
        self.right = None
        self.data = val
        self.char = letter
class Pagoda:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root is None
    def clear(self):
        self.root = None
    def insert(self, val_list):
        val = val_list[1]
        letter=val_list[0]
        node = GFG(val, letter)
        self.root = self._insert(node, self.root)
    def _insert(self, node, queue):
        node.left = node
        node.right = node
        return self._merge(queue, node)
    def delete(self):
        self.root = self._delete(self.root)
    def _delete(self, queue):
        if queue is None:
            return None
        l = r = None
        if queue.left == queue:
            l = None
        else:
            l = queue.left
            while l.left != queue:
                l = l.left
            l.left = queue.left
        if queue.right == queue:
            r = None
        else:
            r = queue.right
            while r.right != queue:
                r = r.right
            r.right = queue.right
        return self._merge(l, r)
    def _merge(self, root, newnode):
        if root is None:
            return newnode
        elif newnode is None:
            return root
        else:
            botroot = root.right
            root.right = None
            botnew = newnode.left
            newnode.left = None
            r = None
            while botroot is not None and botnew is not None:
                if botroot.data > botnew.data:
                    temp = botroot.right
                    if r is None:
                        botroot.right = botroot
                    else:
                        botroot.right = r.right
                        r.right = botroot
                    r = botroot
                    botroot = temp
                else:
                    temp = botnew.left
                    if r is None:
                        botnew.left = botnew
                    else:
                        botnew.left = r.left
                        r.left = botnew
                    r = botnew
                    botnew = temp
            if botnew is None:
                root.right = r.right
                r.right = botroot
                return root
            else:
                newnode.left = r.left
                r.left = botnew
                return newnode
    def find_min(self):
        if self.root:
            return [self.root.char, self.root.data]

# p = Pagoda()
# p.insert(['A', 3])
# p.insert(['B', 4])
# p.insert(['C', 1])
# p.insert(['D', 10])
# p.insert(['E', 15])
# p.insert(['F', 6])
# p.insert(['G', 8])
# p.delete()
# p.delete()
# # p.delete()
# # # p.delete()
# # # p.delete()
# # # p.delete()
# print(p.find_min())



#assert p.root.val == 1