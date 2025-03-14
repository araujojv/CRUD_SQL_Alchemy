from pathlib import Path
from sqlalchemy import create_engine, String, Boolean,select
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column,Session



pasta_atual = Path(__file__).parent
PATH_TO_BD = pasta_atual/'bd_usuarios.sqlite'

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean(),default=False)
    
    def __repr__(self):
        return f"Usuario({self.id=},{self.nome=})"
    
    
engine = create_engine(f"sqlite:///{PATH_TO_BD}")
Base.metadata.create_all(bind=engine)



##CRUD


def cria_usuarios(
    nome,
    senha,
    email,
    acesso_gestor=False
        
):
    with Session(bind=engine) as session:
        usuario = Usuario(
            nome=nome,
            senha=senha,
            email=email,
            acesso_gestor=acesso_gestor
        )
        session.add(usuario)
        session.commit()
        
        
def le_toods_usuarios():
    with Session(bind=engine) as session:
        select_sql= select(Usuario)
        usuarios = session.execute(select_sql).fetchall()
        return usuarios 

def le_usuario_por_id(id):
    with Session(bind=engine) as session:
        select_sql =select(Usuario).filter_by(id=id)
        usuarios = session.execute(select_sql).fetchall()
        return usuarios
        
def modifica_usuario(
    id,
    nome=None,
    senha=None,
    email=None,
    acesso_gestor=None      
    ):
    with Session(bind=engine) as session:
        Select_sql=select(Usuario).filter_by(id=id)
        usuarios=session.execute(Select_sql).fetchall    
        for usuario in usuarios:
            if nome:
                usuario[0].nome = nome 
            if senha:
                usuario[0].senha = senha 
            if email:
                usuario[0].email = email 
            if not acesso_gestor is None:
                usuario[0].acesso_gestor = acesso_gestor     
        session.commit()
        
def deleta_usuario(id):
    with Session(bind=engine) as session: 
        comando_sql=select(Usuario).filter_by(id=id)
        usuarios= session.execute(comando_sql).fetchall()
        for usuario in usuarios:
            session.delete(usuario[0])
        session.commit()
        
        
if __name__ =='__main__':
    cria_usuarios(
        "rafael araujo",
        senha="minha_senha",
        email="pedroaraujo.com",
        acesso_gestor=True
    )
    
print(le_toods_usuarios())