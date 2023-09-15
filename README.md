# Readme

---

### Activate environment

``` bash
$ cd venv/
$ source bin/activate
```

### isort
Sort your imports alphabetically and break them up into appropriate sections.
Here, the `.` applies the command to all python files in current directory.

``` bash
$ isort .
```

### black
Linter that reformats code in place.
Here, the `.` applies the command to all python files in current directory.

``` bash
$ black .
```

### Build `requirements.txt`

``` bash
$ pip freeze > requirements.txt
```
### Test Suite
``` bash
$ pip install pytest
```

