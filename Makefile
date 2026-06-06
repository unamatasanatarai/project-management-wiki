VENV := ./venv

all:
	$(VENV)/bin/python build.py
	ggicp -y