# Atividade8_CC8550

## Execucao

Na pasta `lab08`, com as dependencias do PDF instaladas:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
pytest -q --cov=senha --cov=embarque --cov=preco --cov-branch --cov-report=term-missing
```

A suite funcional criada nesta entrega passa com **19 testes**.
