# Smart Contact CTF Platform

## Services

### chain0
*Port: 8545*
Ganache blockchain node, will run with a minimal dataset initialized with the base contract and challenge contract factories.
Data is stored in a shared volume on `data/chain/`

### explorer
*Port: 8000*
A lightweight blockchain explorer.

### flags
*Port: 3001*
The flag server has 2 functions:
 - proxies requests to provide players with starting Ether
 - validates completion of challenges to return flags

Flags can be managed in `flag-server/config/flags.json`

### webapp
*Port: 8080*
Serves the web frontend.

## Getting Started

The services can be started with a simple `docker-compose up`.
