
clean:
	rm -rf .venv

venv:
	python3 -m venv .venv

requirements: venv
	.venv/bin/pip install -r requirements.txt

test: check
	.venv/bin/python -m unittest tests/test_*.py

run:
	.venv/bin/python src/main.py 10

check: format
	.venv/bin/python -m mypy src/*.py --install-types

format:
	.venv/bin/black src/*.py tests/*.py