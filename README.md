#Alien EMS

Backend api for a fictional company employee management system that manage employees in seperate teams. The system 
enable an accountant to retrieve list of employees in the system with their respective pays.
## Business rules
Each team is lead by one team leader who can also leads more teams at the same time. An employee must be in at least one team. The alien
allows two types of work arrangement:- full time and part time. Unlike full time employees can work for 40 hours a week.
Part time employee can multiple work arrangements as long an employee does not exceed 40 hours limit, and in different
teams.

The system design uses [a Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) 
proposed by Robert C. Martin aka Uncle Bob. I stumbled upon his book, Clean Architecture : A Craftsman's Guide to Software Structure and Design,
online while search for software design books for my Software Design and Architecture class and I never look at the 
software development the same way again. Alien EMS became the best use case to try clean architecture.

Although the clean architecture can be a hustle and and a lot of work, it is really worth the hustle as confirming to 
its rules can make the system easily maintainable and  scalable in the long run without a lot of headache.
It also allows development of system that is more testable evidenced in the is Alien EMS use case. I was able to write
a lot of unit tests for core  business rules and without depending on django framework.


## installation

1. Clone the repository:- `git clone https://github.com/JoeMabor/alienems.git`
2. Create virtual environment inside the repository folder and activate it:- [a Virtual environment in python](https://docs.python.org/3.7/tutorial/venv.html)
3. Install dependencies:- `pip install -r requirements.txt`
3. Open the web server:- `python manage.py runserver`


##Available routes 

1. Teams: Add , view, update and delete teams
    - /teams/
    - /teams/pk/
2. Employees: Add, view, update and  delete employees. Can also add team leader/employee
     - /Employees/
     - /Employees/pk/
3. Team leaders: Assign, view, change and remove remove team leaders
    - /team-leaders/
     - /team-leaders/pk/
4. Team employees: Add, view, update and delete team employees
    - /team-employees/
     - /team-employees/pk/
5. work arrangements: Add, view, update and delete employees work arrangements
    - /work-arrangements/
     - /work-arrangements/pk/
6. work times: View employees work time
    - /work-times/
     - /work-times/pk/
     

    
