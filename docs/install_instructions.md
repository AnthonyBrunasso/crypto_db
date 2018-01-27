Windows
=======

If given the option you will want to add python and mysql to your path. Both the installers may give you an option while installing.

Download python (3.6.x):

    https://www.python.org/downloads/

Install MySQL Community Server and MySQL Workbench when installing MySQL make sure the password is set as 'root'.

    https://dev.mysql.com/downloads/

Download the source code from https://github.com/AnthonyBrunasso/crypto_db you can clone it with git or download the zipped file from the link.

    Direct download:

        1. Click 'Clone or download' 
        2. Click 'Download ZIP'

Extract the zipped file somewhere on your machine and open it up that directory in your command line console. Run the following commands:

    pip install mysqlclient
    mysql -u root -p < create_database.sql
    python update_tables.py

The result of this should the database created with all the tables and some inital data from the api.
