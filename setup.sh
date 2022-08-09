#!/bin/bash

# Conda: Create virtual environment
sitename=mysite
conda create --name $sitename --file requirements.txt
conda activate $sitename
# More info https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

# Pip: Create virtual environment
python -m venv myenv
# More info https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-packages-using-pip-and-virtual-environments

# Unix/MacOS: Active virtual environment
source myenv/bin/activate

# Window: Active virtual environment
myenv\Scripts\activate.bat

# Clone repository
git clone https://github.com/analyticstensor/mysite.git
cd mysite
pip install -r requirements.txt

# Initialize database
flask init-db

# Run apps
flask run