# Strategies used in this project

## List of strategies
- Unconditional cooperator: Cooperates unconditionally.
- Unconditional defector: Defects unconditionally
- Random: Cooperates or defects with p = 0.5
- Probability p Cooperator: Cooperates or defects with probability p
- Tit for tat: Cooperates on the first round and imitates its opponent's previous move thereafter.
- Suspicious Tit for Tat: Defects on the first round and imitates its opponent's previous move thereafter.
- Generous Tit for Tat: Cooperates on the first round and after its opponent cooperates. Following a defection,it cooperates with probability $g(R,P,T,S)=min \{{1-\frac{T-R}{R-S},\frac{R-P}{T-P}}\}$ where R, P, T and S are the reward, punishment, temptation and sucker payoffs.
- Tit for Two Tats: Cooperates unless defected against twice in a row.
- Two tits for tat: Defects twice after being defected against, otherwise cooperates.
- GRIM: Cooperates until its opponent has defected once, and then defects for the rest of the game.
- Pavlov (or Win-stay, Lose-shift): Cooperates if it and its opponent moved alike in previous move and defects if they moved differently.
- Reactive (with parameters y,p,q): Cooperates with probability y in first round and with probabilities p or q after opponent cooperates or defects 
- Memory-one: Cooperates with probabilities probabilities p,q,r or s after outcomes (C,C), (C,D), (D,C) or (C,D).