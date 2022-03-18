nn(gta_net1, [Picture], Y, [left,mid,right]) :: lane(Picture,Y).
nn(gta_net2, [Speedometer], Z, [nospeed, slow, medium, fast]) :: speed(Speedometer,Z).
nn(gta_net3, [Trafficlight], X, [red, nolight]) :: trafficlight(Trafficlight, X).




%w
drivedirection(Picture, Speedometer, Trafficlight, 0) :- lane(Picture,mid), \+ speed(Speedometer,fast), \+trafficlight(red,Trafficlight).
%a
drivedirection(Picture, Speedometer, Trafficlight, 2) :- lane(Picture,right), \+ speed(Speedometer,slow).
%d
drivedirection(Picture, Speedometer, Trafficlight, 3) :- lane(Picture,left), \+ speed(Speedometer,slow).
%wa
drivedirection(Picture, Speedometer, Trafficlight, 4) :- lane(Picture,right) , \+ speed(Speedometer,fast).
%wd
drivedirection(Picture, Speedometer, Trafficlight, 5) :- lane(Picture,left), \+ speed(Speedometer,fast).
%nk
drivedirection(Picture, Speedometer, Trafficlight, 8) :- lane(Picture,mid), speed(Speedometer, fast).


%s
%drivedirection(Picture, Speedometer, Trafficlight, 1) :- lane(Picture,mid), speed(Speedometer, fast).
%sa
%drivedirection(Picture, Speedometer, Trafficlight, 6) :- lane(Picture,right), speed(Picture, fast).
%sd
%drivedirection(Picture, Speedometer, Trafficlight, 7) :- lane(Picture,left), speed(Picture,fast).


drivinginput(Picture, Speedometer, Trafficlight, Input) :- drivedirection(Picture, Speedometer, Trafficlight, Input).