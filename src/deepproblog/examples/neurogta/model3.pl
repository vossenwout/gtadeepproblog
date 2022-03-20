nn(gta_net1, [Picture], Y, [left,mid,right]) :: lane(Picture,Y).
nn(gta_net2, [Speedometer], Z, [slow, fast]) :: speed(Speedometer,Z).
nn(gta_net3, [Obstacle], X, [noobst, closeobst, farobst]) :: obstacle(Obstacle,X).


presskey(Picture, Speedometer, Obstacle, d) :- lane(Picture,right).
presskey(Picture,Speedometer, Obstacle, a) :- lane(Picture,left).
presskey(Picture,Speedometer, Obstacle, w) :- obstacle(Obstacle, noobst), speed(Speedometer,slow) .
presskey(Picture,Speedometer, Obstacle, s) :- obstacle(Obstacle, closeobst).
presskey(Picture,Speedometer, Obstacle, nk) :- lane(Picture,mid), (obstacle(Obstacle, farobst) ; speed(Speedometer, fast)).

drivedirection(Picture, Speedometer, Obstacle, 0) :-  presskey(Picture,Speedometer, Obstacle,w), \+presskey(Picture,Speedometer, Obstacle,s), \+ presskey(Picture,Speedometer, Obstacle,d), \+ presskey(Picture,Speedometer, Obstacle, a).

drivedirection(Picture,Speedometer, Obstacle, 1) :- presskey(Picture,Speedometer, Obstacle,s), \+presskey(Picture,Speedometer, Obstacle,d), \+ presskey(Picture,Speedometer, Obstacle,w), \+ presskey(Picture,Speedometer, Obstacle, a).
drivedirection(Picture, Speedometer, Obstacle,2) :- presskey(Picture,Speedometer, Obstacle,a), \+presskey(Picture,Speedometer, Obstacle,d), \+ presskey(Picture,Speedometer, Obstacle,w), \+ presskey(Picture,Speedometer, Obstacle, d).
drivedirection(Picture, Speedometer, Obstacle,3) :- presskey(Picture,Speedometer, Obstacle,d), \+presskey(Picture,Speedometer, Obstacle,s), \+ presskey(Picture,Speedometer, Obstacle,w), \+ presskey(Picture,Speedometer, Obstacle, a).
drivedirection(Picture,Speedometer, Obstacle, 4) :- presskey(Picture,Speedometer, Obstacle,w), \+presskey(Picture,Speedometer, Obstacle,s), \+ presskey(Picture,Speedometer, Obstacle,d), presskey(Picture,Speedometer, Obstacle, a).
drivedirection(Picture,Speedometer, Obstacle, 5) :- presskey(Picture,Speedometer, Obstacle,d), \+presskey(Picture,Speedometer, Obstacle,s), presskey(Picture,Speedometer, Obstacle,w), \+ presskey(Picture, Speedometer, Obstacle,a).
drivedirection(Picture,Speedometer, Obstacle, 8) :- \+presskey(Picture,Speedometer, Obstacle,d), \+presskey(Picture,Speedometer, Obstacle,s), \+ presskey(Picture,Speedometer, Obstacle,w), \+ presskey(Picture, Speedometer, Obstacle,a), presskey(Picture,Speedometer, Obstacle, nk).




drivinginput(Picture, Speedometer, Obstacle, Input) :- drivedirection(Picture, Speedometer, Obstacle, Input).