# Prisoner's dilemma

## Introduction

The prisoner's dilemma is a game theory thought experiment involving two rational agents, each of whom can either cooperate for mutual benefit or betray their partner ("defect") for individual gain.
The original dilemma goes as following: 
Two members of a criminal gang are arrested and imprisoned. Each prisoner is in solitary confinement with no means of speaking to or exchanging messages with the other. The police admit they don't have enough evidence to convict the pair on the principal charge. They plan to sentence both to a year in prison on a lesser charge. Simultaneously, the police offer each prisoner a Faustian bargain. If he testifies against his partner, he will go free while the partner will get three years in prison on the main charge. Oh, yes, there is a catch ... If both prisoners testify against each other, both will be sentenced to two years in jail. The prisoners are given a little time to think this over, but in no case may either learn what the other has decided until he has irrevocably made his decision. Each is informed that the other prisoner is being offered the very same deal. Each prisoner is concerned only with his own welfare—with minimizing his own prison sentence (source: Prisoner's dilemma by William Poundstone)

This repository covers another problem similar to the one described before but with slight changes, extracted from [Veritasium video](https://www.youtube.com/watch?v=mScpHTIi-kM&list=WL&index=31). 

In this case the situation is the following:

There is a rich person who gives money for two people to work for him, but with a slight inconvenience: you can decide if you want to cooperate between the two of you, or if you want to defect. Each day that you work together for him and cooperate, you will earn $3 each (3 coins in the video). If one of you chooses not to cooperate and the other one chooses to cooperate, the first one will receive $5 and the other one will receive $0. If both of you decide not to cooperate, you will only win $1 each. 

The idea of this repository is to discuss different strategies for playing this two-sided game and how they compare to each other. The strategies are described in the strategies folder, with two main types of strategies: nasty and nice. The first one indicates that the first move in this game will be to not cooperate. The second indicates that the first move will always be to cooperate. The following moves in each strategy are determined by the previous moves of the opposing player. 
