nn(gta_net1, [Picture], Y, [y,n]) :: car(Picture,Y).

drivedirection(Picture, 1) :- car(Picture,y).
drivinginput(Picture, Input) :- drivedirection(Picture,Input).