class flashcard:
    def __init__ (self,word,meaning):
        self.word=word
        self.meaning=meaning
    def getword(self):
        return self.word
    def getmean(self):
        return self.meaning

    def __str__(self):
        return self.getword() + ":" + self.getmean()
l=[]
def dic(x,y):
    l.append(obj)
    return l
x="y"
while x=="y":
    w=input("Add word in your flashcard::")
    m=input("Meaning of the word in flashcard:")
    obj=flashcard(w,m)
    d=dic(w,m)
    x=input("want to add flashcard: y/n")
n=1
for i in d:
    print(n,".",i)
