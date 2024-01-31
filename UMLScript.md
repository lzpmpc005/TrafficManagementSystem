## PlantUML
Copy and paste the script to the web below to see and modify
https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000
## Use Case Diagram
```
@startuml

left to right direction

actor "Driver" << human >> as D
actor "Detection Monitor" << device >> as DM

rectangle "Automated Traffic\nManagement System" {
  
  rectangle "User Service" << application>>{
    usecase (Register Vehicle) as UC1
  }
  
  usecase (Recognize Plate\nLog Vehicle) as UC2

  rectangle "Database Server"{
    usecase (Store Data) as UC3
    usecase (Return Data) as UC6
  }
  
  rectangle "Email Server"{
    usecase (Notify Driver) as UC4
  }
  
  usecase (Detect Violation\nGenerate Fine) as UC5

}

rectangle "Outer System"{
  usecase (Purchase Plate) as PP1
}

D --> PP1
D --> UC1
DM --> UC2
UC1 --> UC3: << include >>
UC2 --> UC3: << include >>
DM --> UC5
UC5 --> UC3: << include >>
UC6 --> UC4
UC4 --> D

@enduml

```
## Sequential Diagram
```
@startuml

== Violation Detection ==
actor "Driver" as D
actor "Detection Monitor" as DM

participant "Violation Detection System" as VDS
participant "Fine Generation\nand\nNotificationSystem" as FGNS
participant "Email Server" as ES
participant "Database Server" as DB

DM -> VDS : Detect Violation
activate VDS
VDS -> VDS : Make Judgement
VDS -> DB : Store Violation Record
deactivate VDS
activate DB

== Email Notification ==
actor "Driver" as D
actor "Detection Monitor" as DM

participant "Violation Detection System" as VDS
participant "Fine Generation\nand\nNotificationSystem" as FGNS
participant "Email Server" as ES
participant "Database Server" as DB

FGNS -> DB : Request Record\n(once every day)
activate FGNS
DB -> FGNS : Return Violation Record and Driver Info
FGNS -> FGNS : Generate Context of Fine
FGNS -> ES : Trigger and Pass Information\n(once every day)
deactivate FGNS
activate ES
ES -> D : Send Notification of Violation and Fine
ES -> DB : Archive the Email Sent Record\n(y/n)
deactivate ES
deactivate DB

@enduml

```
## Class Diagram
```
@startuml
left to right direction

class Vehicle {
    - «PK» numberPlate: String
    - «FK» ownerID: String
    - vehicleType: String
}

class Driver {
    - «PK» driverID: int
    - driverName: String
    - driverEmail: String
    - driverPhone: int
}

class Plate {
    - «PK» numberPlate: String
    - region: String
    - postal_area: String
    - age_identifier: List<String>
    - random_latters: String
}

class JunctionsLog {
    - «PK» logID: int

    - «FK» numberPlate: String
    - dateTime: String
    - location: String

    - speed: int
    - hitSuspicion: Boolean
    - redlightSuspicion: Boolean
    - beltStatus: Boolean
    - phoneStatus: Boolean

    - registerStatus: Boolean
}

class Violation {
    - «PK» logID: int
    - violationType: String
    - fineAmount: int
}

class ViolationLog {
    - «PK» logID: int

    - «FK» numberPlate: String
    - «FK» dateTime: String
    - «FK» location: String

    - «FK» violationType: String
}

class FineLog {
    - «PK» logID: int

    - «FK» numberPlate: String
    - «FK» driverID: int
    - «FK» driverName: String
    - «FK» dateTime: String
    - «FK» location: String

    - «FK» violationType: String
    - «FK» fineAmount: int

    - «FK» closedStatus: Boolean
}

class EmailLog {
    - «PK» logID: int
    - «FK» driverEmail: String
    - «FK» fineLogID: int
    - dateTime: String

    - sentStatus: Boolean
}

Driver "1" -- "0..*" Vehicle : has
Driver "1" -- "0..*" Plate : has
Vehicle "1" -- "1" Plate : has
Plate "1" -- "0..*" JunctionsLog : has
JunctionsLog "1" -- "1" ViolationLog : has
Violation "1" -- "0..*" ViolationLog : has
ViolationLog "1" -- "1" FineLog : has
Violation "1" -- "0..*" FineLog : has
FineLog "1" -- "1" EmailLog : has
Driver "1" -- "0..*" FineLog : has
Vehicle "1" -- "0..*" FineLog : has
Driver "1" -- "0..*" EmailLog : has

@enduml

```
