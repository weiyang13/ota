Directories
===========

4 directories:

* ./src for source code (and some tests, but unstructured)
* ./data for real-world dataset obtained, including sql script
* ./expt for and scripts ran and results for experiments
* ./doc for reports (incl. LaTeX files), presentations and papers

Real world dataset
===========

Data obtained from NYC TLC, at https://bigquery.cloud.google.com/table/nyc-tlc:green.trips_2015
Can obtain more datasets by modifying the SQL queries.

So far, the datasets are obtained from the Brooklyn region in NYC. To change location, modify the appropriate coordinates in the SQL queries. 
Note that yellow taxis are more suited for the Manhattan region.

Running experiments
===========
It is inadvisable to run experiments on your terminal. For NUS SoC students, you can use the xcna/xcnb (etc.) servers 
to run experiments. Look up https://dochub.comp.nus.edu.sg/cf/guides/compute-cluster/hardware for more information.

Note that to run python on the SoC Compute Cluster, you need to create a virtual environment using venv and install the required
dependencies (mainly scipy). You have to transfer the code, manually or via git.

The scripts (e.g. in ./exp/exp_060420/task) for the first 3 experiments are ran across multiple servers in the SoC Compute Cluster. 
Note that the commands differ depending on how you set up your project files in the server. For the first three experiments,
the files were transferred manually, and organised differently, so changes have to be made to the file locations for the scripts.

Furthermore, changes to the codebase have been made between experiments, so earlier experiments may not contain the required
arguments in the command to properly run. It is recommended to base new scripts from the latest experiments, and make the
necessary changes.