from llproj import LinkedList
from lqproj import LinkedQueue

class Worker:
    def __init__(self,id,name):
        self._name=name
        self._id=id
        self._works=LinkedQueue()

    def __str__(self):
        strg="Name:"+str(self._name)+"\nID  :"+str(self._id)
        return strg

w1=Worker("W01","Ram")
w2=Worker("W02","Krish")
w3=Worker("W03","Shiv")
w4=Worker("W04","Balaji")
w5=Worker("W05","Vicky")

WorkersList=LinkedList()
WorkersList.insert(w1)
WorkersList.insert(w2)
WorkersList.insert(w3)
WorkersList.insert(w4)
WorkersList.insert(w5)

class Admin:
    def __init__(self):
        self.custlist=LinkedList()
        self.totalservices=LinkedList()
        self.pendingservices=LinkedQueue()

    '''def assignworks(self,service):
        if self.totalservices.length()%5==1:
            w1._works.enqueue(service)
        elif self.totalservices.length()%5==2:
            w2._works.enqueue(service)
        elif self.totalservices.length()%5==3:
            w3._works.enqueue(service)
        elif self.totalservices.length()%5==4:
            w4._works.enqueue(service)
        elif self.totalservices.length()%5==0:
            w5._works.enqueue(service)'''