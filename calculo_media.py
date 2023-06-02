nota_final_cp_primeiro_ano = 6.5 
nota_final_gp_primeiro_ano  = 7.5 
nota_final_challenge_primeiro_ano  = 6.0 

nota_final_cp_segundo_ano = 8.0
nota_final_gp_segundo_ano  = 10.0
nota_final_challenge_segundo_ano  = 8.0 

peso_20 = 0.2
peso_60 = 0.6
peso_40 = 0.4
   
media_primeiro_ano = nota_final_cp_primeiro_ano * peso_20 + nota_final_gp_primeiro_ano * peso_20 + nota_final_challenge_primeiro_ano * peso_60

print ("Média final primeiro ano", media_primeiro_ano)

media_segundo_ano = nota_final_cp_segundo_ano * peso_20 + nota_final_gp_segundo_ano * peso_60 + nota_final_challenge_segundo_ano * peso_20
print ("Média final segundo ano", media_segundo_ano)

resultado_final= media_primeiro_ano * peso_40 + media_segundo_ano * peso_60
print ("Média final ", resultado_final)



