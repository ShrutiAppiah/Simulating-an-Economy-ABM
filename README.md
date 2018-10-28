# Simulating an Organizational Economy

Research
------------
This is a multi-agent simulator for token mechanisms in decentralized organizations. Use this to simulate your own token-based societies!

Built out of a project for scientifically evaluating an organizational incentive schemes, this simulation demonstrates the behaviour of a decentralized autonmous economy over time. The system is akin to those occuring in statistical mechanics and is modelled as a discrete-time Markov chain. 

Read my paper on [Decentralized Organizations as Multi-Agent Systems](https://www.researchgate.net/publication/319875145_Decentralized_Organizations_as_Multi-Agent_Systems_-_A_Complex_Systems_Perspective "Decentralized Organizations as Multi-Agent Systems") (Mar 2017)


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

#### :rocket: Objective :rocket:
----
Define the goal of your token economy. Think long-term.

A simple token economy aims to either maximize or minimize one parameter or function. The objective funtion is also known as the fitness function or utility function. 

<i> In this example, </i> I want my token to incentivize human agents to contribute in projects. 
So, I could define my objective function as:

>  <b> Maximize </b> f(x) = Total number of human agents participating in a project in each iteration  

#### :globe_with_meridians: Domain :globe_with_meridians:
----
<i> In this example, </i> the domain is a single organization/company with a fixed number of agents.

> <b> Domain: </b> A single DAO with 10x10 participants

#### :couple: System agents/players :couple:
----
The agents of the system constitute of all the parties that can transact with one another. 

<i> In this example, </i> the agents of this economy are members of the DAO.

> <b> Agents: </b> Members of the DAO

The agents certainly have some properties associated with them. At this point, you may have uncovered some of them. 

<i> In this example, </i> the agents have the following known properties -

> <b> Properties: </b>
> <br> Altruistic
> <br> Fair 
> <br> Truthful
> <br> Rational

#### :clock2: System clock :clock2:
----
The clock is defined as the smallest period in which the objective function/parameter changes.  The period should be repeatable.

<i> In this example, </i> the period is the granular unit in which a full project cycle can be completed i.e. the project can be posted, agents can opt in to it, complete it, and get rewarded. 

#### :ok_hand: Assumptions :ok_hand:
----
There are always some unknowns in any system. Although not measured or verified, we may have a rough idea of what these unknowns could be. These will be defined as assumptions. 

<i> In this example, </i> we make the following assumptions -
> Quality of all the projects completed are similar
> <br> Agents aren't able to evaluate difficulty of projects
> <br> All token transactions are tracked


#### :anchor: Constraints :anchor:
----
Constraints bound the system. An optimally constrained system is easy to find solutions for. 

<b> System constraints </b>
- Bounded rationality of agents

<b> Technical constraints </b>
- Scalability
- Gas price

#### :arrow_right: Input parameters :arrow_right:
----
Can be obtained from prior statistical studies
- User or design research
- Behavioural economics
- Surveys

<i> In this example, </i> one of the input parameters are the altruism coefficients.

#### :beginner: Starting mechanism :beginner:
----

In most cases, you may be able to define some of these in your starting mechanism -
- Incentives/tokens
- Token supply
- Is there a cap?
- Value 
-- Is the value pegged to fiat or a stablecoin?
- Mobility
- Tradability
-- What can the token be exchanged for?
- Any identified equilibria

This example started with the mechanism of a simple <i> Boltzmann Wealth Model. </i> 

## Run
Navigate into the cloned repo folder 
```
$ cd Simulating-an-Economy-ABM
```
And run
```
$ python3 VisualizeEconomy.py
```

## Docker

```
docker build -t simulating-an-economy-abm .
docker run -it -p 8521:8521 -v `pwd`:/usr/local/models simulating-an-economy-abm
```

### View
The server should host it on http://127.0.0.1:8521/

:checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: :checkered_flag: 

## Support
Join TokenWork on <b> [Telegram](https://t.me/joinchat/Hwj46xFpeQdiPXvUUfG7Dw) </b>
Read my paper on [Decentralized Organizations as Multi-Agent Systems](https://www.researchgate.net/publication/319875145_Decentralized_Organizations_as_Multi-Agent_Systems_-_A_Complex_Systems_Perspective "Decentralized Organizations as Multi-Agent Systems") (Mar 2017)
<br> Star this repo if you found this model useful. Reach out to me if you'd like to collaborate.

