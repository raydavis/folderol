The rails_api branch requires Ruby 1.9.*. Even with "--old-style-hash", generators will produce the new hash syntax.

----

Ruby + Oracle is still a nightmare.

* Download everything you can think of from <http://www.oracle.com/technetwork/topics/intel-macsoft-096467.html> and consolidate to one directory.
* Add a "tnsnames.ora" file to the consolidated directory.
* Add the directory to your .profile in a lot of ways:
```
DYLD_LIBRARY_PATH="/Users/ray/Code/oracle-instantclient_10_2"
export DYLD_LIBRARY_PATH
SQLPATH=$DYLD_LIBRARY_PATH
export SQLPATH
TNS_ADMIN=$DYLD_LIBRARY_PATH
export TNS_ADMIN
NLS_LANG="AMERICAN_AMERICA.UTF8"
export NLS_LANG
PATH=$PATH:$DYLD_LIBRARY_PATH
```
* Install Ruby stuff:
```
gem install ruby-oci8
gem install activerecord-oracle_enhanced-adapter
```
* Before connecting to campusdb_development, set the secret variables:
```
export ORACLE_USER=yer_username
export ORACLE_PASSWORD=yer_password
export ORACLE_DATABASE=//yer_host:yer_port/yer_sid.berkeley.edu
```
* And test:
```
ray_api> rails dbconsole campusdb_development -p
```
