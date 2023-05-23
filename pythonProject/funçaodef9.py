def converte_em_minuto(horas, minutos):
    horas_p_minutos = horas * 60
    return horas_p_minutos

if __name__ == '__main__':
    horas= int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    v_horas = converte_em_minuto(horas, minutos) + minutos

    print("a hora em minutos é: ",v_horas)