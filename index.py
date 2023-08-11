file = open("text.txt", "r")

line = file.readlines()

n = int(line[0].split(" ")[2])
m = int(line[0].split(" ")[3])
form = list()

for i in range(1, m + 1):
  clauses = set()
  for l in line[i].split(" "):
    if int(l) != 0:
      clauses.add(int(l))
  form.append(clauses)

def simplifica(F: list) -> list:
  for clause in F:
    if len(clause) == 1:
      var = clause.pop()
      for disjunction in F:
        if var in disjunction:
         F.remove(disjunction)
         if set() in F:
            F.remove(set())
        elif -var in disjunction:
            disjunction.remove(-var)
  print(F)


def dpll(F: list) -> int:

    return 0

simplifica(form)

file.close()
