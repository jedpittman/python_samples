# python_samples
Sample Bits of Python Code

# Diagrams

Diagrams allows for generation of architecture diagrams with python for slick documentation.

Diagrams uses the code from here:
https://diagrams.mingrammer.com/docs/getting-started/installation


For windows users, you'll need to install graphviz.
Open up an administrative-level powershell.
Install chocolatey if you haven't done that:
https://chocolatey.org/install

Then install graphviz:
`
choco install graphviz
`
https://chocolatey.org/packages/Graphviz

Setup a virtual environment to run the samples:
`
python -m venv diagramvenv
`

Navigate to the environment and activate it. 
Do a pip install to get the dependencies. 

`
pip install -r requirements.txt
`

Then do a standard run of the samples and the pngs are in the folder.

`
python sample1.py
`