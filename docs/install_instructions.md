Windows
=======

If given the option you will want to add python and mysql to your path. Both the installers may give you an option while installing.

Download python (3.6.x):

    https://www.python.org/downloads/

Install MySQL Community Server and MySQL Workbench when installing MySQL make sure the password is set as 'root'.

    https://dev.mysql.com/downloads/mysql/
    https://dev.mysql.com/downloads/workbench/

Download the source code from https://github.com/AnthonyBrunasso/crypto_db you can clone it with git or download the zipped file from the link.

    Direct download:

        1. Click 'Clone or download' 
        2. Click 'Download ZIP'

Extract the zipped file somewhere on your machine and open up that directory in your command line console. If you've never done that before search for the program 'cmd' my pressing the windows key and typing cmd. Assuming you extracted the zipped file from above to C:\Users\You\crytpo_db type:

    cd C:\Users\You\crypto_db

Now run the following commands from your command line:

    pip install mysqlclient
    mysql -u root -p < create_database.sql
    python update_tables.py

The result of this should the database created with all the tables and some inital data from the api. You should be able to connect to this using MySQL Workbench or you can run the following commands from command line:

    mysql -u root -p
    <type your password>
    use cryptics;
    show tables;
    SELECT * FROM USDT_BTC;

You can view data using SQL from any of the tables show from the show tables query.
