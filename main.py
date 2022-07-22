import application.db.people
from application.salary import get_salary
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    application.db.people.get_info()
    get_salary()