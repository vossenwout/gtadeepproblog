nn(gta_net1, [Picture], Y, [left,mid,right]) :: lane(Picture,Y).
nn(gta_net2, [Speedometer], Z, [slow, medium, fast]) :: speed(Speedometer,Z).


%w
drivedirection(Picture, Speedometer, 0) :- lane(Picture,mid), \+ speed(Speedometer,fast).
%a
drivedirection(Picture, Speedometer, 2) :- lane(Picture,right), \+ speed(Speedometer,slow).
%d
drivedirection(Picture, Speedometer, 3) :- lane(Picture,left), \+ speed(Speedometer,slow).
%wa
drivedirection(Picture, Speedometer, 4) :- lane(Picture,right) , \+ speed(Speedometer,fast).
%wd
drivedirection(Picture, Speedometer, 5) :- lane(Picture,left), \+ speed(Speedometer,fast).
%nk
drivedirection(Picture, Speedometer, 8) :- lane(Picture,mid), speed(Speedometer, fast).

%s
%drivedirection(Picture, Speedometer, 1) :- lane(Picture,mid), speed(Speedometer, fast).
%sa
%drivedirection(Picture, Speedometer, 6) :- lane(Picture,right), speed(Picture, fast).
%sd
%drivedirection(Picture, Speedometer, 7) :- lane(Picture,left), speed(Picture,fast).


drivinginput(Picture, Speedometer, Input) :- drivedirection(Picture, Speedometer,Input).