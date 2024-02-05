
## Prerequisites
- Installed python on you computer
- Path to Python interpreter in environmental variable (mostly done automatically)
- Installed `PIP` library

## Recommendation
- put this note into the Obsidian, all code blocks will be dispelled in special block with **copy** button in the right-top corner 
- install plugin **Editor Syntax Highlight
- installed git (otional)

*Depends on your installation, sometime run command for python is not `python` but `python3`. Try at the beginning what is a correct command on you PC and change the following commands. Similar is for `pip` or `pip3` 
## Steps:
1) upgrade `PIP`
```SHELL
python.exe -m pip install --upgrade pip
```
2) Clone or download repository into the directory of choice
   - clonig (require git)
```SHELL
git clone https://github.com/czeos/geo_analysis.git <path to folder>
```
- Download repository https://github.com/czeos/geo_analysis/archive/refs/heads/master.zip and extract in folder of choice 

 3) In folder of your choice (the best ne empty) create virtual environment It is good practice to keep project and production environments separated to avoid any version conflicts
```SHELL
python -m venv <path to folder>\<name of the venv>
```
e.g.
```SHELL
python -m venv <path>\geo_analysis\geopy_venv
```
4) Activate virtual environment. **If you use download, folder geo_analysis should be named diferently e.g.** <font color="#2DC26B">geo_analysis-master</font>  same for name of venv
```SHELL
.\geo_analysis\geopy_venv\Scripts\activate
```
 5) Installation of requirements (libraries)
```SHELL
pip install -r .\geo_anlysis\requirements.txt
```
6) If everything goes right you can start Jupytern Lab
```SHELL
jupyter lab
```