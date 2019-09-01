import json

class User(object):
    def __init__(self, name, owes=dict(), owed_by=dict(), balance=0 ):
        self.name = name
        self.owes = owes
        self.owed_by = owed_by
        self.balance = balance

    def lend(self, borrower, amount):
        if self.name == borrower:
            return
        if borrower not in self.owed_by:
            self.owed_by[borrower] = 0
        self.owed_by[borrower] += amount
        self.balance += amount
        self.balance_books()

    def borrow(self, lender, amount):
        if self.name == lender:
            return
        if lender not in self.owes:
            self.owes[lender] = 0
        self.owes[lender] += amount
        self.balance -= amount
        self.balance_books()

    def balance_books(self):
        common = [ name for name in self.owes if name in self.owed_by ]  # find users that both owe us and we owe to
        for name in common:
            if self.owed_by[name] == self.owes[name]:
                del self.owed_by[name]
                del self.owes[name]
            elif self.owed_by[name] > self.owes[name]:
                self.owed_by[name] -= self.owes[name]
                del self.owes[name]
            else:
                self.owes[name] -= self.owed_by[name]
                del self.owed_by[name]


class Database(object):
    def __init__(self, database=None):
        self._database = dict()
        if database is not None:
            for user in database['users']:
                self.add_user(user["name"], user["owes"], user["owed_by"], user["balance"])

    def add_user(self, name, owes=dict(), owed_by=dict(), balance=0):
        if not name in self._database:
            self._database[name] = User(name, owes, owed_by, balance)
        return self.get_user(name)

    def get_user_list(self, payload=None):
        if payload is None:
            payload = sorted(self._database.keys())
        else:
            payload.sort()
        return [ self.get_user(name) for name in payload ]

    def get_user(self, name):
        return self._database[name].__dict__

    def transaction(self, lender, borrower, amount):
        if amount < 0:
            raise ValueError("Amount borrowed cannot be negative - thats a lend")
        #self.add_user(lender)
        #self.add_user(borrower)
        self._database[lender].lend(borrower, amount)
        self._database[borrower].borrow(lender, amount)

        names = sorted([borrower, lender])

        return self.get_user_list(names)



class RestAPI(object):
    def __init__(self, database=None):
        self.database = Database(database)

    def get(self, url, payload=None):
        if url == '/users':
            if payload is not None:
                payload = json.loads(payload)["users"]
            return json.dumps( { "users": self.database.get_user_list(payload) } )

    def post(self, url, payload=None):
        if url == '/add':
            if payload is not None:
                payload = json.loads(payload)
            return json.dumps(self.database.add_user(payload['user']))
        elif url == '/iou':
            if payload is not None:
                payload = json.loads(payload)
            return json.dumps({ "users": self.database.transaction(payload["lender"], payload["borrower"], payload["amount"]) })
