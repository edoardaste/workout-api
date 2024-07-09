from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from workout_api.centro_de_treinamento.schemas import CentroDeTreinamentoIn, CentroDeTreinamentoOut
from workout_api.centro_de_treinamento.models import CentroDeTreinamentoModel

from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()

@router.post(
    '/', 
    summary='Criar um novo CT (Centro de Treinamento)',
    status_code=status.HTTP_201_CREATED,
    response_model=CentroDeTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency, 
    centro_de_treinamento_in: CentroDeTreinamentoIn = Body(...)
) -> CentroDeTreinamentoOut:
    centro_treinamento_out = CentroDeTreinamentoOut(id=uuid4(), **centro_de_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_de_treinamento_out.model_dump())
    
    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_out
    
    
@router.get(
    '/', 
    summary='Consultar todos os CTs (Centro de Treinamento)',
    status_code=status.HTTP_200_OK,
    response_model=list[CentroDeTreinamentoOut],
)
async def query(db_session: DatabaseDependency) -> list[CentroDeTreinamentoOut]:
    centros_de_treinamento_out: list[CentroDeTreinamentoOut] = (
        await db_session.execute(select(CentroDeTreinamentoModel))
    ).scalars().all()
    
    return centros_de_treinamento_out


@router.get(
    '/{id}', 
    summary='Consulta um centro de treinamento pelo id',
    status_code=status.HTTP_200_OK,
    response_model=CentroDeTreinamentoOut,
)
async def get(id: UUID4, db_session: DatabaseDependency) -> CentroDeTreinamentoOut:
    centro_de_treinamento_out: CentroDeTreinamentoOut = (
        await db_session.execute(select(CentroDeTreinamentoModel).filter_by(id=id))
    ).scalars().first()

    if not centro_de_treinamento_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Centro de treinamento não encontrado no id: {id}'
        )
    
    return centro_de_treinamento_out