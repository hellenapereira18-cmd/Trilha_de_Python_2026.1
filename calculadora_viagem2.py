#Orçamento
orcamento = float(input("Digite o orçamento total disponível em reais {R$}"))
#Destino 
destino = input("Digite o destino escolhido")
#Passagem 
custo_da_passagem_em_reais_= float(input("Digite o o custo da passagem em reais {R$}"))
#Custo diário em euro 
custo_diario_em_euro = float(input("Digite o custo da hospedagem em euro {E}"))
#Dias de viagem
dias = int(input("Digite a quantidade de dias da viagem"))

#RESTRIÇÃO IMPORTANTE
#SE OS VALORES FOREM NEGATIVOS
if custo_da_passagem_em_reais_<= 0 or custo_diario_em_euro <= 0 or custo_da_passagem_em_reais_ <=  0 :
    print("O programa não poderá ser executado, pois o valor inserido é negativo")
    print ("ValueError")

#COTAÇÃO EM EURO = 6.10 reais
custo_diario_em_reais = custo_diario_em_euro * custo_da_passagem_em_reais_
total_da_hospedagem_em_reais = custo_diario_em_reais * dias
custo_diario_em_reais = custo_da_passagem_em_reais_ + total_da_hospedagem_em_reais
custo_total_da_viagem = custo_da_passagem_em_reais_ + total_da_hospedagem_em_reais
#Orçamento possível 
if custo_total_da_viagem <= orcamento and dias > 0 :
    print("Orçamento possível")
    print("Status viável")

#Orçamento não possível 
else: 
    print("Orçamento não possível")
    print("Status inviável")
    
#Status final da viagem (caso o orçamento final seja igual ou inferior ao custo total)
print(f" --- Resumo da viagem: {destino} --- ")
print(f"custo total da hospedagem R$ : {total_da_hospedagem_em_reais}")
print(f"o custo total da viagem R$ : {custo_total_da_viagem}")

