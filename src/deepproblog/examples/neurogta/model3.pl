nn(gta_net1, [Picture], Y, [left,mid,right]) :: lane(Picture,Y).
nn(gta_net2, [Speedometer], Z, [slow, fast]) :: speed(Speedometer,Z).
nn(gta_net3, [Obstacle], X, [noobst, closeobst, farobst]) :: obstacle(Obstacle,X).


presskey(Picture, d) :- lane(Picture,right).
presskey(Picture, a) :- lane(Picture,left).
presskey(Picture, w) :- obstacle(Obstacle, noobst), speed(Speedometer,slow) .
presskey(Picture, s) :- obstacle(Obstacle, closeobst).
presskey(Picture, nk) :- lane(Picture,mid), (obstacle(Obstacle, farobst) ; speed(Speedometer, fast))


drivedirection(Picture, 0) :-  presskey(Picture,w), \+presskey(Picture,s), \+ presskey(Picture,d), \+ presskey(Picture, a).
drivedirection(Picture, 1) :- presskey(Picture,s), \+presskey(Picture,d), \+ presskey(Picture,w), \+ presskey(Picture, a).
drivedirection(Picture, 2) :- presskey(Picture,a), \+presskey(Picture,d), \+ presskey(Picture,w), \+ presskey(Picture, d).
drivedirection(Picture, 3) :- presskey(Picture,d), \+presskey(Picture,s), \+ presskey(Picture,w), \+ presskey(Picture, a).
drivedirection(Picture, 4) :- presskey(Picture,w), \+presskey(Picture,s), \+ presskey(Picture,d), presskey(Picture, a).
drivedirection(Picture, 5) :- presskey(Picture,d), \+presskey(Picture,s), presskey(Picture,w), \+ presskey(Picture, a).
drivedirection(Picture, 8) :- \+presskey(Picture,d), \+presskey(Picture,s), \+ presskey(Picture,w), \+ presskey(Picture, a), presskey(Picture, nk).




drivinginput(Picture, Input) :- drivedirection(Picture,Input).