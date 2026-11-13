pacientes = []
medicamentos = []
pacientes_postos = []

ativo = True
while ativo:
    print("\n===== SISTEMA INTEGRADO DE SAÚDE DO UÍGE =====")
    print("1. Hospital Provincial")
    print("2. Postos de Saúde")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    # HOSPITAL PROVINCIAL
    if opcao == "1":
        hospital_ativo = True
        while hospital_ativo:
            print("\n--- HOSPITAL PROVINCIAL ---")
            print("1. Cadastrar pacientes")
            print("2. Listar pacientes")
            print("3. Registar consulta")
            print("4. Ver histórico de um paciente")
            print("5. Cadastrar medicamentos")
            print("6. Listar medicamentos")
            print("7. Voltar")
            opcao_h = input("Escolha uma opção: ")

            if opcao_h == "1":
                quantidade = int(input("Quantos pacientes deseja cadastrar? "))
                for i in range(quantidade):
                    print("\nPaciente", i + 1)
                    nome = input("Nome: ")
                    idade = input("Idade: ")
                    genero = input("Género (M/F): ")
                    pacientes.append({"nome": nome, "idade": idade, "genero": genero, "historico": []})
                print("Pacientes cadastrados com sucesso!")

            elif opcao_h == "2":
                if len(pacientes) == 0:
                    print("Não há pacientes registados.")
                else:
                    for i, p in enumerate(pacientes):
                        print(i + 1, "-", p["nome"], "| Idade:", p["idade"], "| Género:", p["genero"])

            elif opcao_h == "3":
                posicao = int(input("Posição do paciente: "))
                indice = posicao - 1
                if 0 <= indice < len(pacientes):
                    diagnostico = input("Diagnóstico: ")
                    medico = input("Médico responsável: ")
                    pacientes[indice]["historico"].append({"diagnostico": diagnostico, "medico": medico})
                    print("Consulta registada!")
                else:
                    print("Posição inválida.")

            elif opcao_h == "4":
                posicao = int(input("Posição do paciente: "))
                indice = posicao - 1
                if 0 <= indice < len(pacientes):
                    historico = pacientes[indice]["historico"]
                    if len(historico) == 0:
                        print("Sem consultas registadas.")
                    else:
                        for consulta in historico:
                            print("Diagnóstico:", consulta["diagnostico"], "| Médico:", consulta["medico"])
                else:
                    print("Posição inválida.")

            elif opcao_h == "5":
                quantidade = int(input("Quantos medicamentos deseja cadastrar? "))
                for i in range(quantidade):
                    print("\nMedicamento", i + 1)
                    nome = input("Nome: ")
                    estoque = int(input("Quantidade: "))
                    medicamentos.append({"nome": nome, "quantidade": estoque})
                print("Medicamentos cadastrados com sucesso!")

            elif opcao_h == "6":
                if len(medicamentos) == 0:
                    print("Estoque vazio.")
                else:
                    for i, m in enumerate(medicamentos):
                        print(i + 1, "-", m["nome"], "| Quantidade:", m["quantidade"])

            elif opcao_h == "7":
                hospital_ativo = False

            else:
                print("Opção inválida.")

    # POSTOS DE SAÚDE
    elif opcao == "2":
        posto_ativo = True
        while posto_ativo:
            print("\n--- POSTOS DE SAÚDE ---")
            print("1. Cadastrar pacientes")
            print("2. Listar pacientes")
            print("3. Encaminhar paciente para o Hospital Provincial")
            print("4. Voltar")
            opcao_p = input("Escolha uma opção: ")

            if opcao_p == "1":
                quantidade = int(input("Quantos pacientes deseja cadastrar? "))
                for i in range(quantidade):
                    print("\nPaciente", i + 1)
                    nome = input("Nome: ")
                    idade = input("Idade: ")
                    genero = input("Género (M/F): ")
                    pacientes_postos.append({"nome": nome, "idade": idade, "genero": genero})
                print("Pacientes registados com sucesso!")

            elif opcao_p == "2":
                if len(pacientes_postos) == 0:
                    print("Não há pacientes registados.")
                else:
                    for i, p in enumerate(pacientes_postos):
                        print(i + 1, "-", p["nome"], "| Idade:", p["idade"], "| Género:", p["genero"])

            elif opcao_p == "3":
                posicao = int(input("Posição do paciente no posto: "))
                indice = posicao - 1
                if 0 <= indice < len(pacientes_postos):
                    p = pacientes_postos[indice]
                    pacientes.append({"nome": p["nome"], "idade": p["idade"], "genero": p["genero"], "historico": []})
                    print("Paciente encaminhado para o Hospital Provincial, posição:", len(pacientes))
                else:
                    print("Posição inválida.")

            elif opcao_p == "4":
                posto_ativo = False

            else:
                print("Opção inválida.")

    elif opcao == "3":
        print("A sair do sistema!")
        ativo = False

    else:
        print("Opção inválida.")
