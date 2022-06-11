init: # for window
	python -m venv venv && ./venv/Scripts/pip.exe install -r requirements.txt
update:
	./venv/Scripts/pip.exe install -r requirements.txt
run:
	venv/Scripts/python.exe .\index.py