class calcQTA():

    def __init__(self):
        self.__numberOfCalls = 22

    def __convertToCO2__(self,kwh):
        return 0.00040972222*kwh

    def getNumberOfCalculations(self):
        return self.__numberOfCalls

    def getListOfPossibilities(self):
        str = '''
            _-_-Geladeira-_-_\ngeladeira() \nOutputs:\n     Consumo em kWh por mês\n    Massa de CO2 em kG  \n
            _-_-Lampada-_-_\nlampada(tipo 0-LED 1-Fluorescente 2-Incandescente,Horas Por Dia) \nOutputs: \n     Consumo em kWh por mês\n    Massa de CO2 em kG\n
            _-_-Televisao-_-_\ntv(tipo 0-PLASMA 1-LCD 2-LED,tamanho em polegadas, horas por dia) \nOutputs: \n     Consumo em kWh por mês\n    Massa de CO2 em kG\n
            _-_-Lava-roupa-_-_\nlavaRoupa(Horas Diarias) \n
            _-_-Secadora roupa-_-_\nsecadoraRoupas(Horas Diarias) \n
            _-_-Lava-Louca-_-_\nlavaLouca(Ciclos por dia) \n
            _-_-Computador-_-_\ncomputador(tipo 0-mesa 1-notebook,tempo diario) \n
            _-_-Celular-_-_\ncelular(tempo diario) \n
            _-_-Chuveiro-_-_\nchuveiro(potencia em WATTs, horas diarias) \n
            _-_-Ferro de Passar Roupa-_-_\nferroPassarRoupa(horas diarias) \n
            _-_-Microondas-_-_\nmicroondas(horas diarias) \n
            _-_-VideoGame-_-_\nvideoGame(horas diarias, tipo 0-XBOX360 1-PS3 2-XBOXONE 3-PS4,horas diarias) \n
            _-_-Secador de Cabelo-_-_\nsecadorCabelo(horas diarias) \n
            _-_-Chapinha-_-_\nchapinha(horas diarias) \n
            _-_-Ventilador-_-_\nventilador(horas diarias) \n
            _-_-Ar Condicionado-_-_\narCondicionado(Horas diarias) \n
            _-_-Sistema de Som-_-_\nsistemaSom(Horas Diarias) \n
            
            
            
            _-_-Veiculo-_-_\nveiculo(combustivel,tipoVeiculo,motor,kmMensal):
        Combustivel(0-Gasolina, 1-Alcool, 2-Diesel, 3-GNV)
        tipo (0-carro, 1-moto, 2-onibus,3-onibus rodoviario) \n
            _-_-Fogao-_-_\nfogao(tipo 0-butijão 1-encanado ,medido embutijoes ou em metro cubico) \n
            _-_-Aquecedor a Gas-_-_\naquecedor(Metros cubicos mensais(Encanado somente)) \n
            _-_-Avião-_-_\naviao(tipo 0-nacional 1-internacional,km Mensal) \n
            _-_-Residuos Sólidos-_-_\nresiduos(kgDiario) \n
                Outputs:\n   Emissão de CO2 por Mes \n
            \n
            '''
        return str
    
    def residuos(self,kGDiario):
        return 963.6*kGDiario

    def aviao(self,tipo,kmMensal):
        if(tipo==0):
            return 100.188*kmMensal
        else:
            return 112.4649999*kmMensal

    def geladeira(self):
        consumo = 53.1
        co = self.__convertToCO2__(consumo)
        return consumo,co

    def Lampada(self,tipo,horasDiarias):
        if tipo==0:      #LED
            consumoMensal = 4.8*10^(-3)*30*horasDiarias
        elif tipo==1:    #Fluorescente
            consumoMensal = 15*10^(-3)*30*horasDiarias
        elif tipo==2:    #Incandescente
            consumoMensal = 100*10^(-3)*30*horasDiarias
        else:
            consumoMensal = 40*10^(-3)*30*horasDiarias
        co = self.__convertToCO2__(consumoMensal)
        return consumoMensal,co

    def tv(self,tipo,tamanho,horasDiarias):
        #plasma
        if tipo==0:
            if tamanho==42:
                consumoMensal = 275*30*horasDiarias
            elif tamanho==50:
                consumoMensal = 340*30*horasDiarias
            else:
                consumoMensal = 307.5*30*horasDiarias

        #LCD
        elif tipo==1:
            if tamanho==32:
                consumoMensal = 110*30*horasDiarias
            elif tamanho==40:
                consumoMensal = 190*30*horasDiarias
            elif tamanho==42:
                consumoMensal = 225*30*horasDiarias
            elif tamanho==46:
                consumoMensal = 265*30*horasDiarias
            elif tamanho==52:
                consumoMensal = 295*30*horasDiarias
            else:
                consumoMensal = 217*30*horasDiarias

        #LED
        elif tipo==2:
            if tamanho==32:
                consumoMensal = 80*30*horasDiarias
            elif tamanho==40:
                consumoMensal = 115*30*horasDiarias
            elif tamanho==46:
                consumoMensal = 140*30*horasDiarias
            else:
                consumoMensal = 112*30*horasDiarias
        
        else:
            consumoMensal = 212*30*horasDiarias
        
        co = self.__convertToCO2__(consumoMensal)

        return consumoMensal,co

    def lavaRoupa(self,horasDiarias):
        consumo = horasDiarias*0.6*30
        co = self.__convertToCO2__(consumo)
        return consumo,co

    def secadoraRoupas(self,horasDiarias):
        consumo = horasDiarias*30*4.5
        co = self.__convertToCO2__(consumo)
        return consumo,co

    def lavaLouca(self,ciclosDiarios):
        consumo = 1.4*30*ciclosDiarios
        co = self.__convertToCO2__(consumo)
        return consumo,co

    def veiculo(self,combustivel,tipoVeiculo,motor,kmMensal):
        #Combustivel(0-Gasolina, 1-Alcool, 2-Diesel, 3-GNV)
        #tipo (0-carro, 1-moto, 2-onibus,3-onibus rodoviario)
        if(combustivel==0):
            if(tipoVeiculo==0):
                if(motor<=1.4):
                    return 2.184*kmMensal                
                elif(motor<=2.0):
                    return 2.579*kmMensal
                else:
                    return 3.571*kmMensal
            elif(tipoVeiculo==1):
                return 1.268*kmMensal
        elif(combustivel==1):
            return 0.719*kmMensal
        elif(combustivel==2):
            if(tipoVeiculo==0):
                return 3.091*kmMensal
            elif(tipoVeiculo==2):
                return 2.280*kmMensal
            elif(tipoVeiculo==3):
                return 0.6*kmMensal
        elif(combustivel==3):
            return 3.128*kmMensal
        
    def computador(self,tipo,horasDiarias):
        if tipo==0:     #mesa
            consumoMensal = 274*30*horasDiarias
        else:           #Notebook
            consumoMensal = 65*30*horasDiarias
        co = self.__convertToCO2__(consumoMensal)
        return consumoMensal,co

    def celular(self,horasDiarias):
        consumoMensal = 7*10^(-3)*30*horasDiarias 
        return consumoMensal,self.__convertToCO2__(consumoMensal)

    def chuveiro(self,watts,horasFunc):
        consumo = (watts/1000)*horasFunc
        co = self.__convertToCO2__(consumo)
        return consumo,co

    def fogao(self,tipo,butOUM3):
        if tipo==0:     #Butijao
            return 13*35.895*butOUM3
        else:           #Encanado
            return butOUM3*22.674

    def ferroPassarRoupa(self,horasDiarias):
        consumoMensal = 1.2*10^(-3)*30*horasDiarias
        co = self.__convertToCO2__(consumoMensal)
        return consumoMensal,co

    def microondas(self,horasDiarias):
        consumoMensal = 1.3*10^(-3)*30*horasDiarias
        co = self.__convertToCO2__(consumoMensal)
        return consumoMensal,co

    def videoGame(self,horasDiarias,tipo):
        # 0-xbox360   1-ps3  2-xboxONE   3-PS4
        if tipo==0:
            consumoMensal = 70*30*horasDiarias
        elif tipo==1:
            consumoMensal = 64*30*horasDiarias
        elif tipo==2:
            consumoMensal = 250*30*horasDiarias
        elif tipo==3:
            consumoMensal = 181*30*horasDiarias
        co = self.__convertToCO2__(consumoMensal)
        return consumoMensal,co

    def secadorCabelo(self,horasDiarias):
        consumoMensal = 2*10^(-3)*30*horasDiarias
        return consumoMensal,self.__convertToCO2__(consumoMensal)

    def chapinha(self,horasDiarias):
        consumoMensal = 52*10^(-3)*30*horasDiarias
        return consumoMensal,self.__convertToCO2__(consumoMensal)

    def ventilador(self,horasDiarias):
        consumoMensal = 150*10^(-3)*30*horasDiarias
        return consumoMensal,self.__convertToCO2__(consumoMensal)

    def arCondicionado(self,horasDiarias):
        consumoMensal = 0,758333*horasDiarias*30
        co = self.__convertToCO2__(consumoMensal)
        return consumoMensal,co

    def aquecedor(self,metrocubicosmes):
        return metrocubicosmes*2.2674

    def sistemaSom(self,horasDiarias):
        consumoMensal = 15*10^(-3)*30*horasDiarias
        return consumoMensal,self.__convertToCO2__(consumoMensal)

a = calcQTA()
print(a.getListOfPossibilities())