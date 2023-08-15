with open("text.txt", "r", encoding="utf-8") as file:
    line = file.read().split("\n")

# guarda variaveis e clausulas em n e m, respectivamente
for linha in line:
    if linha.startswith('p'):
        n = int(linha.split(" ")[2])
        m = int(linha.split(" ")[3])

# remove linhas que não são cláusulas
line = [s for s in line if not (s.startswith("p") or s.startswith("c"))]

form = []

for i in range(0, m):
    clauses = set()
    for l in line[i].split(" "):
        if int(l) != 0:
            clauses.add(int(l))
    form.append(clauses)


def dpll(symbols, clauses, model):
    
    if all(len(c) == 0 for c in clauses):
        return True
    if any(len(c) == 0 for c in clauses):
        return False

    for symbol in symbols:
        if symbol not in model:
            break

    aux_model_true = model.copy()
    aux_model_true[symbol] = True
    aux_clauses_true = [[c for c in clause if c != -symbol]
                        for clause in clauses]
    result_true = dpll(symbols, aux_clauses_true, aux_model_true)

    if result_true:
        return True

    aux_model_false = model.copy()
    aux_model_false[symbol] = False
    aux_clauses_false = [clause for clause in clauses if -symbol not in clause]
    return dpll(symbols, aux_clauses_false, aux_model_false)

def satisfativel(F):
    symbols = set(abs(literal) for clause in F for literal in clause)
    model = {}
    return dpll(symbols, F, model)


def simplifica(F: list) -> list:
    clauses_unitaria = set()
    clauses_var_negada = set()

    for clause in F:
        if len(clause) == 1:
            clauses_unitaria.add(clause.pop())
        else:
            clauses_var_negada.update(clause)

    F = [clause for clause in F if not any(-var in clause for var in clauses_unitaria)]

    for clause in F:
        clause.difference_update(-var for var in clauses_var_negada)

    return F

print(form)

satisfatibilidade = satisfativel(simplifica(form))

if satisfatibilidade:
    print("Satisfatível")
else:
    print("Insatisfatível")