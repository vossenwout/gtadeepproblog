nn(gta_net1, [Picture], Y, [left,mid,right]) :: lane(Picture,Y).


presskey(Picture, d) :- lane(Picture,left); lane(Picture,mid) , \+lane(Picture,right).
presskey(Picture, a) :- lane(Picture,right); lane(Picture,mid) , \+lane(Picture,left).
presskey(Picture, w) :- lane(Picture,right) ; lane(Picture,left); lane(Picture,mid).
presskey(Picture, s):- \+lane(Picture,right), \+lane(Picture,mid) , \+lane(Picture,left).



drivedirection(Picture, 0) :-  presskey(Picture,w), \+presskey(Picture,s), \+ presskey(Picture,d), \+ presskey(Picture, a).
drivedirection(Picture, 1) :- presskey(Picture,s), \+presskey(Picture,d), \+ presskey(Picture,w), \+ presskey(Picture, a).
drivedirection(Picture, 2) :- presskey(Picture,a), \+presskey(Picture,d), \+ presskey(Picture,w), \+ presskey(Picture, d).
drivedirection(Picture, 3) :- presskey(Picture,d), \+presskey(Picture,s), \+ presskey(Picture,w), \+ presskey(Picture, a).
drivedirection(Picture, 4) :- presskey(Picture,w), \+presskey(Picture,s), \+ presskey(Picture,d), presskey(Picture, a).
drivedirection(Picture, 5) :- presskey(Picture,d), \+presskey(Picture,s), presskey(Picture,w), \+ presskey(Picture, a).
drivedirection(Picture, 6) :- \+presskey(Picture,d), presskey(Picture,s), \+ presskey(Picture,w), presskey(Picture, a).
drivedirection(Picture, 7) :- presskey(Picture,d), presskey(Picture,s), \+ presskey(Picture,w), \+ presskey(Picture, a).
drivedirection(Picture, 8) :- \+presskey(Picture,d), \+presskey(Picture,s), \+ presskey(Picture,w), \+ presskey(Picture, a).




%drivedirection(Picture, 3) :- lane(Picture,left).
%drivedirection(Picture, 5) :- lane(Picture,left).
%drivedirection(Picture, 7) :- lane(Picture,left).
%drivedirection(Picture, 2) :- lane(Picture,n).
drivinginput(Picture, Input) :- drivedirection(Picture,Input).