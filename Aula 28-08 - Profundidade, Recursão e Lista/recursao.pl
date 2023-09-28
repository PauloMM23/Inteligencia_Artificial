imprimeD(N) :- N == 0, !.
imprimeD(N) :- writeln(N),
    		   R is N - 1,
    		   imprimeD(R).

imprimeC(N) :- N == 0, !.
imprimeC(N) :- R is N - 1,
    		   imprimeC(R),
    		   writeln(N).

fatorial(N,F) :- N == 1, 
    			 F is 1,!.
fatorial(N,F) :- N1 is N - 1,
    			 fatorial(N1,F1), %ponto de recursão
    			 F is N * F1.

conecta(a,b,10).
conecta(a,d,60).
conecta(b,c,50).
conecta(d,e,20).
conecta(e,b,10).
conecta(e,c,40).

caminho(O,D,Custo) :- conecta(O,D,Custo).
caminho(O,D,Custo) :- conecta(O,I,Custo1),
    				  caminho(I,D,Custo2),
    				  writeln(I),
    				  Custo is Custo1 + Custo2.

progenitor(claro,pedro).
progenitor(pedro,paulo).
progenitor(paulo,alex).
progenitor(alex,dante).

ascendente(A,D):- progenitor(A,D).
ascendente(A,D):- progenitor(A,I),
    			  ascendente(I,D).



