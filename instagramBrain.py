class Commentator:
    def __init__(self, value):
        self.head = {
            "value" : value,
            "next" : None
        }
        self.tail = self.head
        pass

    def newComment(self, value):
        newNode = {
            "value": value,
            "next" : None
        }
        self.tail["next"] = newNode
        self.tail = newNode



    def deleteComment(self): pass



    def oldComment(self):
        first = self.head
        second = first["next"]

        while(second):
            temp = second["next"]
            second["next"] = first
            first = second
            second  = temp
        
        self.head["next"] = None
        self.head = first
        return self.head

    def recentlyComment(self):
        return self.head["value"]


