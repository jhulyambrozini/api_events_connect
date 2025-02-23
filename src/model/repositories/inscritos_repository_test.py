from  .inscritos_repository import InscritosRepository
import pytest

@pytest.mark.skip('insert in db')
def test_insert():
    inscrito_infos = {
        'name': 'pessoa 1',
        'email': 'email@gmail.com',
        'evento_id': 1
    }
    inscritos_repo = InscritosRepository()
    inscritos_repo.insert(inscrito_infos)

@pytest.mark.skip('select in db')
def test_select():
    email = 'email@gmail.com'
    id = 1
    inscritos_repo = InscritosRepository()
    res = inscritos_repo.select_subscriber(email, id)
    print(res.nome)
