nn(gta_net1, [Picture], Y, [left,mid,right]) :: lane(Picture,Y).

%w
drivedirection(Picture, 0) :- lane(Picture,mid).
%s
%drivedirection(Picture, 1) :- lane(Picture,left).
%a
%drivedirection(Picture, 2) :- lane(Picture,right).
%d
%drivedirection(Picture, 3) :- lane(Picture,left).
%wa
drivedirection(Picture, 4) :- lane(Picture,right).
%wd
drivedirection(Picture, 5) :- lane(Picture,left).
%sa
%drivedirection(Picture, 6) :- lane(Picture,left).
%sd
%drivedirection(Picture, 7) :- lane(Picture,left).
%nk
%drivedirection(Picture, 8) :- lane(Picture,left).


drivinginput(Picture, Input) :- drivedirection(Picture,Input).