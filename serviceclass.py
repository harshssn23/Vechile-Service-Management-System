from datetime import *
import json

class service():
    
    __slots__=['cust','model','regnon','stype','bodate','rddate','worker']
    
    def __init__(self,cust,model,regnon,stype,bodate ,rddate ,worker):
        self.model=model
        self.regnon=regnon
        self.cust=cust
        self.stype=stype
        self.worker=worker
        self.bodate=bodate
        self.rddate=rddate
    
    def addServicetype(self,type):
        self.stype=type.split(',')
    
    # general service,oil maintenance,clutch repair,engine maintenace,break system maintenace
    
    def price(self):
        price=0
        for i in self.servicetype:
            if i=='general service':
                price+=1000
            elif i=='oil service':
                price+=500
            elif i=='clutch repair':
                price+=700
            elif i=='engine maintenace':
                price+=900
            else:
                price+=500
        return price
    
    def writefile(self,file,phone):
        servicedict=self.servicedetails(phone)
        with open(file,'r') as servicefile:
            servicedata=json.load(servicefile)
            servicedata.append(servicedict)
        with open(file,'w') as servicefile:
            json.dump(servicedata,servicefile)
    
    def assignworker(self,worker=None):
        self.worker=worker
    
    def servicedetails(self,phone):
        #retdate=self.regdate+timedelta(2)
        return {"cust":phone,
                'model':self.model,
                'regno':self.regnon,
                'type':self.stype,
                'bdate':str(self.bodate),
                'rdate':str(self.rddate),
                'worker':self.worker}
    
    def getservicedetails(self):
        details=self.servicedetails()
        info=''
        for data in details:
            info+=str(data)+'\n'
        return info

# s=service('Yamaha RX100','TN55AD1555')
# s.addServicetype('general service,oil maintenance,clutch repair,engine maintenace,break system maintenace')
# print(type(s.regdate))
# print(s.getservicedetails())

