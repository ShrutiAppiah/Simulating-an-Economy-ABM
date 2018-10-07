# Simulating an Organizational Economy

Research
------------
This is a multi-agent simulator for token mechanisms in decentralized organizations. Use this to simulate your own token-based societies!

Built out of a project for scientifically evaluating an organizational incentive schemes, this simulation demonstrates the behaviour of a decentralized autonmous economy over time. The system is akin to those occuring in statistical mechanics and is modelled as a discrete-time Markov chain. 

Read my paper on [Decentralized Organizations as Multi-Agent Systems](https://www.researchgate.net/publication/319875145_Decentralized_Organizations_as_Multi-Agent_Systems_-_A_Complex_Systems_Perspective "Decentralized Organizations as Multi-Agent Systems")


## Cryptosystems Simulation Workshop
Ahoj Ethereum developers! 

### Python
Make sure you have Python 3. You can download the latest version here - https://www.python.org/

### Install Mesa
Install Mesa on Python 3:

    $ pip3 install mesa

### Dependencies
Install all dependencies either manually or by using
```
$ pip3 install -r requirements.txt
```

### Clone
Clone this repository.
```
$ git clone https://github.com/ShrutiAppiah/Simulating-an-Economy-ABM
```
On Terminal or Command Prompt, cd into the main directory for this repository.

If you want to follow the workshop, see Token Engineering. If you want to skip ahead and run the code, go to Run/

## Token Engineering 
In the token enginerring design process, you will define your token economy as an optimization problem, mathematically model it, and then validate it using this multi-agent simulation.

### Objective :rocket:
Define the goal of your token economy. Think long-term.

A simple token economy aims to either maximize or minimize one parameter or function. The objective funtion is also known as the fitness function or utility function. 

<i> In this example, </i> I want my token to incentivize human agents to contribute in projects. 
So, I could define my objective function as:
Maximize f(x) = Total number of human agents participating in a project in each iteration  

### Domain
### System agents/players
### System clock
### Assumptions
### Constraints 
### Input parameters
### Starting mechanism

## Run
Navigate into the cloned repo folder 
```
$ cd Simulating-an-Economy-ABM
```
And run
```
$ python3 VisualizeEconomy.py
```

### View
The server should host it on http://127.0.0.1:8521/

### Support
Star this repo if you found this model useful. Reach out to me if you'd like to collaborate.

