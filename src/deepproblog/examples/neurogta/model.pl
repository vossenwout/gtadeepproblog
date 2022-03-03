nn(gta_net1, [Picture], Y, [y,n]) :: car(Picture,Y).

drivinginput(Picture, [0, 0, 0, 0, 0, 0, 0, 0, 1]) :- car(Picture,y).