nome = input("digite seu nome")

peso = float(input("digite seu peso"))

altura = float(input("digite sua altura"))

imc =peso/(altura*altura)

msg_padrão= "você está no peso adequado para sua altura, caso queira almentar seu peso terá que seguir uma dieta regrada com mais cairboidratos e mais proteina"
msg_para_pessoas_abaixo_do_peso= "você esta abaixo do peso, precisa faazer uma dieta para aumentar seu peso"
msg_para_pessoas_acima_do_peso= "você esta acima do seu peso para sua altura você tera que comer menos comida"
msg_para_pessoas_com_obesidade_grau_1 = "você esta com obesidade do 1° grau, é tratavel mais se não tratar pode ser mortal"
msg_para_pessoas_com_obesidade_grau_2= "sua obesidade esta no grau 2 se o senhor não tratar isso rapido pode vir a Óbito"
msg_para_pessoas_com_obesidade_grau_3= "sua obesidade atinjiu o terceiro grau isso não pode ser mais tratado, você infelizmente pode vir a Óbito "

if imc<18.5:
    print(nome,msg_para_pessoas_abaixo_do_peso)
elif 18.5<= imc <25:
    print(nome,msg_padrão)
elif 25<= imc <30:
    print(nome,msg_para_pessoas_acima_do_peso) 
elif 30<= imc <34.9:
    print(nome,msg_para_pessoas_com_obesidade_grau_1)
elif 35<= imc <39.9:
    print(nome,msg_para_pessoas_com_obesidade_grau_2)
elif imc <=40:
    print(nome,msg_para_pessoas_com_obesidade_grau_3)       