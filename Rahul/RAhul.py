class Patient:
    def init(self,v1,v2,v3,v4,v5):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3 
        self.v4 = v4 
        self.v5 = v5 

class Doctor:
    def init(self,hName,patientList):
        self.hName = hName
        self.patientList = patientList
    
    def findPatientWithMaximumAge(self):
        if len(self.patientList) == 0:
            return None 
        ans = sorted(self.patientList, key = lambda p : p.v3)
        return ans[-1]
    
    def sortPatientByBillAmount(self):
        if len(self.patientList) == 0:
            return None 
        return sorted(self.patientList, key = lambda p : p.v5)
        
    
patientList = []
n = int(input())
for _ in range(n):
    v1 = input()
    v2 = input()
    v3 = int(input())
    v4 = input()
    v5 = float(input())
    patientList.append(Patient(v1,v2,v3,v4,v5))

d = Doctor("XYZ",patientList)

a = d.findPatientWithMaximumAge()

if a == None:
    print("No Data Found.")
else:
    print(a.v1,a.v2,a.v3,a.v4,a.v5,sep="\n")

b = d.sortPatientByBillAmount()

if b == None:
    print("No Data Found.")
else:
    for x in b:
        print(x.v5)