nota_media_cp_primeiro_semestre = int(input("Media do CP: "))
nota_media_gs_primeiro_semestre  = int(input("Media do GS: "))
nota_media_challenge_primeiro_semestre  = int(input("Media do Challenge: "))

media_primeiro_semestre = ( nota_media_cp_primeiro_semestre*20/100 + nota_media_gs_primeiro_semestre *60/100 + nota_media_challenge_primeiro_semestre *20/100)/3
print(media_primeiro_semestre)

nota_media_cp_segundo_semestre = int(input("Media do CP: "))
nota_media_gs_segundo_semestre  = int(input("Media do GS: "))
nota_media_challenge_segundo_semestre  = int(input("Media do Challenge: "))
   
media_segundo_semestre = ( nota_media_cp_segundo_semestre*20/100 + nota_media_gs_segundo_semestre *60/100 + nota_media_challenge_segundo_semestre *20/100)/3
print (media_segundo_semestre)

media_final= media_primeiro_semestre*10/100 + media_segundo_semestre*60/100
print (media_final)

if media_final < 4:
    print ("você está retido")
elif media_final > 6:
    print ("você foi aprovado") 
elif media_final >=4 and media_final >6:
    print ("Você esta de exame")    
