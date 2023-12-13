class Family:
    def __init__(self):
        self.facts = set()

    def add_fact(self, predicate, *args):
        self.facts.add((predicate, *args))

    def query(self, predicate, *args):
        return (predicate, *args) in self.facts

def main():
    family = Family()

    # Define family relations
    family.add_fact('male', 'John')
    family.add_fact('female', 'Alice')
    family.add_fact('parent', 'John', 'Alice')
    family.add_fact('parent', 'John', 'Bob')
    family.add_fact('parent', 'Alice', 'Charlie')
    family.add_fact('parent', 'Bob', 'David')

    # Define rules for family relations
    def father(x, y):
        return family.query('male', x) and family.query('parent', x, y)

    def mother(x, y):
        return family.query('female', x) and family.query('parent', x, y)

    def grandfather(x, y):
        return father(x, 'temp') and father('temp', y)

    def grandmother(x, y):
        return mother(x, 'temp') and mother('temp', y)

    def brother(x, y):
        return family.query('male', x) and family.query('parent', 'temp', x) and family.query('parent', 'temp', y) and x != y

    def sister(x, y):
        return family.query('female', x) and family.query('parent', 'temp', x) and family.query('parent', 'temp', y) and x != y

    def uncle(x, y):
        return brother(x, 'temp') and father('temp', y)

    def aunt(x, y):
        return sister(x, 'temp') and mother('temp', y)

    def nephew(x, y):
        return family.query('male', x) and (uncle('temp', y) or aunt('temp', y))

    def niece(x, y):
        return family.query('female', x) and (uncle('temp', y) or aunt('temp', y))

    def cousin(x, y):
        return (uncle('temp', x) or aunt('temp', x)) and (uncle('temp', y) or aunt('temp', y)) and x != y

    # Example queries
    print("Is Alice a mother of Charlie?", mother('Alice', 'Charlie'))
    print("Is John a grandfather of David?", grandfather('John', 'David'))
    print("Is Bob a brother of Alice?", brother('Bob', 'Alice'))
    print("Is Alice an aunt of David?", aunt('Alice', 'David'))
    print("Is David a nephew of Bob?", nephew('David', 'Bob'))
    print("Is David a cousin of Charlie?", cousin('David', 'Charlie'))

if __name__ == "__main__":
    main()
