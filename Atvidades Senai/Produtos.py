from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque} unidades")
    
    def preco_final(self):
        return self.preco
    
    def emitir_nota(self):
        print(f"Nota gerada para {self.nome}.")
    
    def repor(self, quantidade):
        self.estoque += quantidade
        print(f"Estoque de {self.nome} reposto. Novo estoque: {self.estoque}")
    
    def vender(self, quantidade):
        if quantidade > self.estoque:
            print(f"Erro: Estoque insuficiente de {self.nome} (disponível: {self.estoque})")
        else:
            self.estoque -= quantidade
            print(f"Venda de {quantidade} {self.nome}(s) realizada. Estoque restante: {self.estoque}")

class ProdutoNacional(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)
    
    def emitir_nota(self):
        print(f"Nota fiscal nacional para {self.nome}.")

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_importacao = taxa_importacao
    
    def preco_final(self):
        return self.preco * (1 + self.taxa_importacao)
    
    def emitir_nota(self):
        print(f"Nota de importação para {self.nome} com taxa de {self.taxa_importacao*100}% aplicada.")
    
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Taxa de importação: {self.taxa_importacao*100}% | Preço final: R${self.preco_final():.2f}")