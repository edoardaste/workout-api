from typing import Annotated

from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema


class CentroDeTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do CT (Centro de Treinamento)', example='CT São Paulo', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do CT (Centro de Treinamento)', example='Avenida Brasil, n 40', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do CT ', example='Calleri', max_length=30)]


class CentroDeTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do CT (Centro de Treinamento)', example='CT São Paulo', max_length=20)]


class CentroDeTreinamentoOut(CentroDeTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador CT (Centro de Treinamento)o')]    