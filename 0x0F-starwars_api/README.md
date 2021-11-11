# 0x0F. Star Wars API

## Install Node 10
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs

## Install semi-standard
$ sudo npm install semistandard --global

## Install request module and use it
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules

## 0. Star Wars Characters
Write a script that prints all characters of a Star Wars movie:

* The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
* Display one character name per line in the same order as the “characters” list in the /films/ endpoint
* You must use the [Star wars API](https://swapi-api.hbtn.io/)
* You must use the request module