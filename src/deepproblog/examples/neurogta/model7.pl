nn(gta_net1, [Picture], Y, [left,mid,right]) :: lane(Picture,Y).
nn(gta_net2, [Speedometer], Z, [nospeed, slow, medium, fast]) :: speed(Speedometer,Z).
nn(gta_net3, [Obstacle], X, [noobst, closeobst, farobst]) :: obstacle(Obstacle,X).

%w forward
drivedirection(Picture, Speedometer, Obstacle , 0) :- lane(Picture,mid), \+ speed(Speedometer,fast).
%a left
drivedirection(Picture, Speedometer,Obstacle ,  2) :- lane(Picture,right), \+ speed(Speedometer,slow).
%d right
drivedirection(Picture, Speedometer, Obstacle , 3) :- lane(Picture,left), \+ speed(Speedometer,slow).
%wa forward to the left
drivedirection(Picture, Speedometer, Obstacle , 4) :- lane(Picture,right) , \+ speed(Speedometer,fast).
%wd forward to the right
drivedirection(Picture, Speedometer, Obstacle , 5) :- lane(Picture,left), \+ speed(Speedometer,fast).
%nk nokey
drivedirection(Picture, Speedometer, Obstacle , 8) :- (lane(Picture,mid), speed(Speedometer, fast) ).
drivedirection(Picture, Speedometer, Obstacle , 8) :- obstacle(Obstacle, farobst).
%s brake
drivedirection(Picture, Speedometer, Obstacle, 1) :- lane(Picture,mid), speed(Speedometer, fast).
drivedirection(Picture, Speedometer, Obstacle, 1) :-  \+ speed(Speedometer, nospeed) , obstacle(Obstacle,closeobst).

% press on the w key IF we are standing still
drivedirection(Picture, Speedometer, Obstacle ,  0) :- speed(Speedometer, nospeed), \+ obstacle(Obstacle, closeobst).
drivedirection(Picture, Speedometer, Obstacle ,  4) :- speed(Speedometer, nospeed), \+ obstacle(Obstacle, closeobst).
drivedirection(Picture, Speedometer, Obstacle ,  5) :- speed(Speedometer, nospeed), \+ obstacle(Obstacle, closeobst).


%sa
%drivedirection(Picture, Speedometer, 6) :- lane(Picture,right), speed(Picture, fast).
%sd
%drivedirection(Picture, Speedometer, 7) :- lane(Picture,left), speed(Picture,fast).


drivinginput(Picture, Speedometer, Obstacle , Input) :- drivedirection(Picture, Speedometer, Obstacle, Input).