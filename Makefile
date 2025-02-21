
clean:
	rm -rf .venv

venv:
	python3 -m venv .venv

requirements: venv
	.venv/bin/pip install -r requirements.txt

test: check
	PYTHONPATH=src .venv/bin/python -m unittest tests/*/test_*.py

run:
	.venv/bin/python src/main.py 10

check: format
	.venv/bin/mypy . --install-types --strict --ignore-missing-imports --disable-error-code misc

format:
	.venv/bin/black .