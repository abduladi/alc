# alc
ALCDevops Challenge

## Prerequisites

* Docker
* Python 2.7
* Terminal

Install docker community edition from this link https://www.docker.com/community-edition  
This code has only been tested on a macOS computer.  
  
  
Test docker installation by typing this command into terminal  
```
$ docker -v
```  
  
You should get an output similar to this:  
```
Docker version 17.12.0-ce, build c97c6d6
```


### Deployment
clone this repo  
Navigate into the the clone folder with  
```
$ cd alc  
```  

Run the `dockapp.py` file with this  
```$ python dockapp.py```  

### Installation
* Start up your terminal (or Command Prompt on Windows OS).
* Ensure that you've `node` installed on your PC.
* Clone the repository by entering the command `git clone https://github.com/andela-bolajide/UserManager` in the terminal.
* Navigate to the project folder using `cd UserManager` on your terminal (or command prompt)
* After cloning, install the application's dependencies with the command `npm install`.
* Create a `.env` file in your root directory as described in `.env.sample` file. Variables such as DB_URL (which must be a mongoDB URL) and PORT are defined in the .env file and it is essential you create this file before running the application.
```
PORT=3000
