def main():
    clientes = []

    while True:
        nome = input("DIGITE O NOME DO CLIENTE: ")

        while True:
            vgastoinput = input("DIGITE O VALOR GASTO EM REAIS: R$ ")
            if vgastoinput.strip().isdigit():
                vgasto = int(vgastoinput)
                break
            else:
                print("VALOR INVÁLIDO, DIGITE APENAS NÚMEROS INTEIROS.")

        clientes.append([nome, vgasto])

        cont = input("VOCÊ DESEJA CONTINUAR? (S/N): ").strip().upper()
        while cont not in ['S', 'N']:
            cont = input("OPÇÃO INVÁLIDA, DIGITE APENAS 'S' OU 'N': ").strip().upper()
        if cont == 'N':
            break

    total = len(clientes)
    if total > 0:
        soma = sum(p[1] for p in clientes)
        clientemaismais = max(clientes, key=lambda p: p[1])

        print("\nRESULTADOS FINAIS:")
        print(f"Total de clientes cadastrados: {total}")
        print(f"Total gasto: R$ {soma}")
        print(f"O cliente que mais comprou é: {clientemaismais}")


if __name__ == "__Main__":
    main()