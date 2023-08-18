def dpll(simbolos, clausulas, valoracao):
    
    if all(len(c) == 0 for c in clausulas):
        return True
    if any(len(c) == 0 for c in clausulas):
        return False

    for simbolo in simbolos:
        if simbolo not in valoracao:
            break

    aux_valoracao_true = valoracao.copy()
    aux_valoracao_true[simbolo] = True
    aux_clausulas_true = [[c for c in clausula if c != -simbolo] for clausula in clausulas]

    if dpll(simbolos, aux_clausulas_true, aux_valoracao_true):
        return True

    aux_valoracao_false = valoracao.copy()
    aux_valoracao_false[simbolo] = False
    aux_clausulas_false = [clausula for clausula in clausulas if -simbolo not in clausula]
    return dpll(simbolos, aux_clausulas_false, aux_valoracao_false)

def satisfativel(F):
    simbolos = set(abs(literal) for clausula in F for literal in clausula)
    valoracao = {}
    return dpll(simbolos, F, valoracao)

def simplifica(F: list) -> list:
    clausulas_unitaria = set()
    clausulas_var_negada = set()

    for clausula in F:
        if len(clausula) == 1:
            clausulas_unitaria.add(clausula.pop())
        else:
            clausulas_var_negada.update(clausula)

    F = [clausula for clausula in F if not any(-var in clausula for var in clausulas_unitaria)]

    for clausula in F:
        clausula.difference_update(-var for var in clausulas_var_negada)

    return F

with open("text.txt", "r", encoding="utf-8") as file:
    line = file.read().split("\n")

for linha in line:
    if linha.startswith('p'):
        n = int(linha.split(" ")[2])
        m = int(linha.split(" ")[3])

line = [s for s in line if not (s.startswith("p") or s.startswith("c"))]

form = []

for i in range(0, m):
    clausulas = set()
    for l in line[i].split(" "):
        if int(l) != 0:
            clausulas.add(int(l))
    form.append(clausulas)

print(form)

if satisfativel(simplifica(form)):
    print("Satisfatível")
else:
    print("Insatisfatível")