# Open Bank
A Mobile Bank

![mobile bank](openbank/wall.png)

Build with django, this app will basically do in-house transactions.
Within time and contributions, external payment platforms should be linked so this
can be a financial tool.

## Setup
you need a python environment and then close this repository

### Linux
#### Python
`python -v` or `python3 -v` to comfirl python is installed. <br>
The command should show a version of python installed. Otherwise if you get an error saying 
`-bash: python: command not found` it means python is not installed. Install it since it is required

#### Git
* [Fork](https://github.com/rootech-inc/Open-Bank/fork) this repository
* Move to forked repository
* Clone your repository (checkout branches `view` for testing and `main` for live deployment)

#### Local Setup
* cd to your cloned directory
* Checkout the branch you need, cd to openbank
* create a virtual environment
* install requirement (`pip install -r requirements.txt`)
* run server (`python3 manage.py runserver ip_address:port_number`)



