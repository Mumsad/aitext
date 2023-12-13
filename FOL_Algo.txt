class Predicate:
    def __init__(self, subject, relation, object):
        self.subject = subject
        self.relation = relation
        self.object = object

    def __str__(self):
        return f"{self.subject} is {self.relation} {self.object}."


def derive_predicate(relationships, subject):
    derived_predicates = []
    for relation in relationships:
        if relation[0] == subject:
            derived_predicates.append(Predicate(subject, relation[1], relation[2]))
    return derived_predicates


# Relationships: (subject, relation, object)
relationships = [("Sachin", "batsman", "cricketer"), ("batsman", "is", "cricketer")]

# Subject for which we want to derive predicates
subject_to_derive = "Sachin"

derived_predicates = derive_predicate(relationships, subject_to_derive)

for predicate in derived_predicates:
    print(predicate)
