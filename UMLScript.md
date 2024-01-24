## PlantUML
Copy and paste the script to the web below to see and modify
https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000
## Use Case Diagram
```
@startuml
left to right direction
actor "Driver" as D
actor "Traffic Police" as TP
actor "Administration Staff" as AS
actor "Detection Monitor" as DM

rectangle "Automated Traffic\nManagement System" {
  
  usecase (Vehicle Registration) as UC1
  usecase (Vehicle\nRecognization and Log) as UC2

  rectangle "Database Server"{
  
  usecase (Data Storage) as UC3

 }
  
  rectangle "Email Server"{

  usecase (Email Notification) as UC4

 }

}
```
## Sequential Diagram
```
@startuml

== Vehicle Registration ==
actor "Driver" as D
actor "Administration Staff" as AS
actor "Detection Monitor" as DM

participant "Registration and Recognation System" as RRS
participant "Database Server" as DB

D -> RRS: Register Vehicle
activate RRS
RRS -> DB: Store Vehicle and Owner Information
activate DB
RRS -> AS: Retrieve Information
deactivate RRS
deactivate DB

== Vehicle Recognation ==
DM -> RRS: Detect vehicle plates
activate RRS
RRS -> RRS: Recognise plates and create logs per unit period
RRS -> DB: Store traffic logs per unit period
activate DB
RRS -> AS: Retrieve Information
deactivate RRS
deactivate DB
@enduml

D --> UC1
DM --> UC2
UC1 --> UC3: << include >>
UC2 --> UC3: << include >>

@enduml
```
## Class Diagram
```
@startuml

left to right direction

class "Vehicle" {

- «PK» numberPlate: String
- «FK» ownerID: String
- vehicleType: String

}

class "Driver"{

- «PK» driverID: String
- driverName: String
- driverEmail: String
- driverPhone: int
}

Driver "1" -- "0..*" Vehicle : has

@enduml
```
