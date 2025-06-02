from Produtos import ProdutoNacional, ProdutoImportado
from Func import FuncionarioCLT, FuncionarioPJ

def main():
    # Cadastro de produtos
    produtos = [
        ProdutoNacional("Teclado", 100.0, 50),
        ProdutoImportado("iPhone 15", 8000.0, 10, 0.6),
        ProdutoNacional("Mouse Gamer", 150.0, 30)
    ]

    # Cadastro de funcionários
    funcionarios = [
        FuncionarioCLT("João Silva", 3000.0),
        FuncionarioPJ("Maria Souza", 160, 50.0)
    ]

    # Relatório de produtos
    print("\n=== RELATÓRIO DE PRODUTOS ===")
    for produto in produtos:
        produto.exibir_detalhes()
        produto.emitir_nota()
        print("-" * 40)

    # Controle de estoque
    produtos[0].vender(5)  # Vende teclados
    produtos[1].repor(3)   # Repõe iPhones

    # Folha de pagamento
    print("\n=== FOLHA DE PAGAMENTO ===")
    for func in funcionarios:
        print(f"{func.nome}: R${func.calcular_pagamento():.2f}")

if __name__ == "__main__":
    main()