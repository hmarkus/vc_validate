# Validator for vertex covers
The library allows to validate a given vertex cover for a given graph.


## Download:
```bash
git clone --recurse-submodules  git@github.com:hmarkus/vc_validate.git
````


## External Requirements (requirements.txt)
```bash
pip install -r requirements.txt
```

## Manpage
```bash
bin/vc_validate --help
```

## Validate Vertex Cover
```bash
bin/vc_validate -g graphfile.gr -vc vertexcoverfile.vc
```

## Compile with PyInstaller
```bash
pyinstaller -p $PWD:$PWD/lib/htd_validate --clean --onefile bin/vc_validate
```
Executable will be in `dist`