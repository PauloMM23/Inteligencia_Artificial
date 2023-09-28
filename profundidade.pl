naesquerda(luiz,paulo).
naesquerda(paulo,leo).
nadireita(A,P):- naesquerda(P,A).
naponta(P):- naesquerda(_,P), not(naesquerda(P,_)).
naponta(P):- nadireita(_,P), not(nadireita(P,_)).
nomeio(P):- naesquerda(_,P), nadireita(_,P).




%gremio, inter, interzinho, saoluiz, brasil, pelotas

chave(a,gremio).
chave(a,interzinho).
chave(a,pelotas).
chave(b,inter).
chave(b,saoluiz).
chave(b,brasil).

jogo(gremio,3,2,interzinho).
jogo(gremio,2,2,pelotas).
jogo(interzinho,1,0,gremio).
jogo(interzinho,0,0,pelotas).
jogo(pelotas,1,3,gremio).
jogo(pelotas,0,0,interzinho).

quemVenceuCasa(T):- jogo(T,GolsT,GolsA,_),
    				GolsT > GolsA.

saldoGolsTime(T,Saldo):- jogo(T,GolsT,GolsA,_),
						 Saldo is GolsT - GolsA.

saldoGolsTime(T,Saldo):- jogo(_,GolsA,GolsT,T),
    					 Saldo is GolsT - GolsA.







regiao(terra_media,norte).
regiao(terra_media,sul).
regiao(terra_media,centro-oeste).
regiao(terra_media,leste).
regiao(terra_media,oeste).

raca(orc,110).
raca(anao,500).
raca(humano,90).
raca(hobbit,100).
raca(elfo,1000).

papel(mago).
papel(guerreiro).
papel(rei).
papel(ladrao).

ficaNo(condado,leste,hobbit).
ficaNo(valfenda,centro-oeste,elfo).
ficaNo(rohan,oeste,humano).
ficaNo(mordo,norte,orc).

lingua(orc,orces).
lingua(elfo,elfico).
lingua(elfo,portugues).
lingua(anao,portugues).
lingua(humano,portugues).
lingua(hobbit,portugues).

aliados(A,B):- lingua(A,LinguaA),
   	      	   lingua(B,LinguaB),
    		   LinguaA == LinguaB.

personagem(gandalf,humano,mago,valfenda).
personagem(bilbo,hobbit,ladrao,condado).
personagem(frodo,hobbit,_,condado).
personagem(legolas,elfo,guerreiro,valfenda).
personagem(galadriel,elfo,mago,valfenda).
personagem(gimly,anao,_,_).
personagem(boromir,humano,_,rohan).

quantoVive(P,T):- personagem(P,Raca,Categoria,_),
    			  raca(Raca,T),
				  Categoria \== mago, !.

quantoVive(P,T):- personagem(P,Raca,_,_),
    			  raca(Raca,Tempo),
				  T is Tempo + 100.

nasceu(P,lugar):- personagem(P,_,_,lugar).
nasceu(P,lugar):- personagem(P,_,_,I),
    			  ficaNo(I,lugar,_).
