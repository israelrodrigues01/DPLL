with open("text.txt", "r", encoding="utf-8") as file:
  line = file.read().split("\n")

#guarda variaveis e clausulas em n e m, respectivamente
for linha in line:
  if linha.startswith('p'):
    n = int(linha.split(" ")[2])
    m = int(linha.split(" ")[3])

#remove linhas que não são cláusulas
line = [s for s in line if not (s.startswith("p") or s.startswith("c"))]

form = list()

for i in range(0, m):
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