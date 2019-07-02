class Flight(object):
    flight_count = 0
    def __init__(self, Flight_Number, From, To, Date):
        self.Flight_Number = Flight_Number
        self.From_Loc = From
        self.To_Loc = To
        self.Date = Date
        Flight.flight_count += 1

    def getFlight(self):
        #print("Details of flight are: ", self.Flight_Number, self.From_Loc, self.To_Loc, self.Date)
        return self.Flight_Number, self.From_Loc, self.To_Loc, self.Date
    def getFlightCount(self):
        print("Total number of flights are: " , self.flight_count)


class Person(object):
    person_count = 0
    def _init_(self, Name, Age, Sex):
        self.Name = Name
        self.Age = Age
        self.Sex = Sex
        Person.person_count += 1

    def persondetails(self):
        return str((self.Name, self.Sex,self.Age))

    def getPersonCount(self):
        print("Total number of persons are: ", self.person_count)

class Employee(Person): #inheritance
    employee_count = 0
    def __init__(self, Name, Age, Sex, Emp_ID):
        super()._init_(Name, Age, Sex) #super call
        #super._init_(self,Name, Age, Sex)
        self.Emp_ID = Emp_ID
        Employee.employee_count += 1

    def employeedetails(self):
        #Person.Print_Person_Details(self)
        print("Employee Details are",self.persondetails(),self.Emp_ID)

    def getEmployeeCount(self):
        print("Total Number of employees are: ", self.employee_count)

class Passenger(Person): # inheritance
    flight_details = None
    passenger_count = 0
    def __init__(self, Name, Age, Sex, ID_No, flight):
        Person._init_(self,Name, Age,Sex)
        self.ID_No = ID_No
        self.flight_details = flight.getFlight()
        Passenger.passenger_count += 1

    def passengerdetails(self):
        #Person.Print_Person_Details(self)
        print("Passenger Details are",self.persondetails(),self.ID_No , "and Flight details are", self.flight_details )

    def getPassengerCount(self):
        print("Total Number of passengers are: ", self.passenger_count)

class Pilot(Person, Flight):
    pilot_count = 0
    assigned_flight = None
    def __init__(self, Name, Age, Sex, Pilot_ID, flight):
        Person.__init__(self,Name, Age, Sex)
        self.assigned_flight = flight.getFlight()
        self.Pilot_ID = Pilot_ID
        Pilot.pilot_count += 1

    def pilotDetails(self):
        print("Pilot Details are",Person.persondetails(self),self.Pilot_ID,"and assigned flight detils are",self.assigned_flight)

    def getPilotCount(self):
        print("Total number of pilots are: ", self.pilot_count)

if __name__ == '_main_': #creation of instances of above classes
    person1 = Person('Rahul',23,'Male')
    flight1 = Flight(9893, 'Kansas-City', 'Chicago-IL','June-25-19')
    flight2 = Flight(1235, 'Seattle', 'Virginia','June-26-19')
    passenger1 = Passenger('Dhar', 18, 'Male', 'Ab123', flight1)
    passenger2 = Passenger('Ramya', 19, 'Female', 'A6359', flight2)
    passenger3 = Passenger('Aparna', 40, 'Female', '6E235', flight1)
    Employee1 = Employee('Lohitha', 36, 'Female', 'C125')
    Employee2 = Employee('Bala', 73, 'Male', 'E876')
    pilot1 = Pilot('King', 35, 'Male', 'I435', flight1)

    Employee1.employeedetails()
    Employee2.employeedetails()
    passenger1.passengerdetails()
    passenger2.passengerdetails()
    passenger3.passengerdetails()
    pilot1.pilotDetails()
    pilot1.getPilotCount()
    person1.getPersonCount()
    flight1.getFlightCount()
    passenger1.getPersonCount()
    Employee1.getEmployeeCount()