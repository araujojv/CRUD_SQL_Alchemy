from pathlib import Path
from sqlalchemy import create_engine, String, Boolean
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