adiciona(N, Lista) :- adiciona(N,[],Lista).

adiciona(0,Acumulador,Acumulador).
adiciona(N,Acumulador,Resultado) :-
    	N > 0,
    	N1 is N - 1,
    	adiciona(N1,[N|Acumulador],Resultado).


idades([ [andre,25], [jose,30] ]).
casas([casa(1, azul), casa(2, verde)]).

alunos([luiz,paulo,leo,alex]).
distancias([120,34,100,67,12]).

primeiro([P | _], P).

ultimo([U], U).
ultimo([_ | R], U) :- ultimo(R,U).

disciplinas([ia,ed,po,redes,so,modelagem]).

percorre([U]) :- writeln(U).
percorre([P | R]) :-	  
    				  writeln(P),
    				  percorre(R).
    				  