set -e

echo "==> Executando migrations..."
alembic upgrade head

echo "==> Executando seeds..."
python -m app.seeds.run_seeds

echo "==> Executando testes..."
pytest -v

echo "==> Testes finalizados com sucesso!"
