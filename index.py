def dpll(simbolos, clausulas, valoracao):
    
    #verificações triviais
    if all(len(c) == 0 for c in clausulas):
        return True
    if any(len(c) == 0 for c in clausulas):
        return False

    #um símbolo sem valor atribuído é escolhido
    for simbolo in simbolos:
        if simbolo not in valoracao:
            break

    #bcp para símbolo=True
    aux_valoracao_true = valoracao.copy()
    aux_valoracao_true[simbolo] = True
    aux_clausulas_true = simplifica([[c for c in clausula if c != -simbolo] for clausula in clausulas])

    if dpll(simbolos, aux_clausulas_true, aux_valoracao_true):
        return True

    #bcp para símbolo=False
    aux_valoracao_false = valoracao.copy()
    aux_valoracao_false[simbolo] = False
    aux_clausulas_false = simplifica([clausula for clausula in clausulas if -simbolo not in clausula])
    return dpll(simbolos, aux_clausulas_false, aux_valoracao_false)

def satisfativel(F):
    simbolos = set(abs(literal) for clausula in F for literal in clausula)
    valoracao = {}
    return dpll(simbolos, F, valoracao)

#"simplifica" tratando apenas de cláusulas unitárias
def simplifica(F: list) -> list:
    new_F = []
    
    for clause in F:
        if len(clause) == 1:
            var = clause.pop()
            remove_disjunction = False
            for disjunction in F:
                if disjunction != clause:
                    if var in disjunction:
                        remove_disjunction = True
                        break
                    elif -var in disjunction:
                        disjunction.remove(-var)
            
            if not remove_disjunction:
                new_F.append(clause)
    
    return new_F

#main
with open("text.txt", "r", encoding="utf-8") as file:
    line = file.read().split("\n")

#guardamos número de clausulas e simbolos
for linha in line:
    if linha.startswith('p'):
        n = int(linha.split(" ")[2])
        m = int(linha.split(" ")[3])

#remoção de linhas de comentários ou linhas desnecessárias
line = [s for s in line if not (s.startswith("p") or s.startswith("c"))]

form = []

#a fórmula em si, como uma lista de sets
for i in range(0, m):
    clausulas = set()
    for l in line[i].split(" "):
        if int(l) != 0:
            clausulas.add(int(l))
    form.append(clausulas)

print(form)

#decisão de satisfatibilidade
if satisfativel(simplifica(form)):
    print("Satisfatível")
else:
    print("Insatisfatível")