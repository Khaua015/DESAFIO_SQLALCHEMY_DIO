

import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Integer, String, Column, ForeignKey, DECIMAL

#Conectando com o banco de dados
engine = sqlalchemy.create_engine('sqlite://', echo=True)

#Declarando o mapeamento
Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))



    def __repr__(self):
        return f'<Cliente(nome= {self.nome}, cpf= {self.cpf}, endereco= {self.endereco}'

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num= Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(DECIMAL)



    def __repr__(self):
        return f'<Conta(tipo= {self.tipo}, agencia= {self.agencia}, num= {self.num}, saldo= {self.saldo}'



#Criar a tabela no banco de dados

Base.metadata.create_all(engine)


#Criar uma sessão no banco de dados

Session = sessionmaker(bind=engine)

session = Session()


# Adicionar Objetos(Equivalente ao INSERT)
session.add(Cliente(nome='Serafino', cpf='12345678', endereco='Rua Santo Antonio De Pádua'))
session.add(Cliente(nome='Josefina', cpf='87654321', endereco='Rua Das Amélias'))
session.add(Conta(tipo='Corrente', agencia='001', num=1234, saldo=1200))
session.add(Conta(tipo='Corrente', agencia='011', num=4321, saldo=5000))
session.commit()

#Consultar Objetos(SELECT)

query_cliente = session.query(Cliente).filter_by(nome='Serafino').first()
query_conta = session.query(Conta).filter_by(num='1234').first()
print(query_cliente)
print(query_conta)

# Modificar Objetos(UPDATE)
print(Cliente.nome)
Cliente.nome = 'Serafin'
print(Cliente)

session.dirty

session.commit()

# Deletar Objetos(DELETE)

cliente= session.query(Cliente).filter_by(nome='Serafin').first()
conta= session.query(Conta).filter_by(num=1234).first()
session.delete(cliente)
session.delete(conta)

session.commit()