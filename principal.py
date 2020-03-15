
from tkinter import *
from variaveis import *



class Processador(object):
    def __init__(self,inst):

        # Imagem
        imagem = PhotoImage(file='cpu.gif')
        self.imagemUser = Label(inst, image=imagem)#, bg='#4B0082')
        self.imagemUser.image = imagem
        self.imagemUser.pack()

        #Rótulos
        self.lbProcessador = Label(inst, text = 'Processador: ')
        self.lbArquitectura = Label(inst, text = 'Arquitectura: ')
        self.lbBits = Label(inst, text = 'Bits: ')
        self.lbFrequencia_disponivel = Label(inst, text = 'Frequência disponível: ')
        self.lbFrequencia_usada = Label(inst, text = 'Frequência usada: ')
        self.lbNr_Nucleos = Label(inst, text = 'Número de núcleos (Processador): ')
        self.lbBateria = Label(inst, text = 'Bateria: ')
        self.lbKernel = Label(inst, text = 'Sistema: ')
        self.lbVersao_Kernel = Label(inst, text = 'Versão do Kernel: ')
        self.lbUtilizador = Label(inst, text = 'Utilizador: ')
        #self.lbUso_CPU = Label(inst, text = 'Uso do Processador: ')

        self.infoProcessador = Label(inst,text = processador)
        self.infoArquitectura = Label(inst, text = arquitectura)
        self.infoBits = Label(inst,text = bits)
        self.infoFrequencia_disponivel = Label(inst, text = frequencia_disponivel)
        self.infoFrequencia_usada = Label(inst, text = frequencia_usada)
        self.infoNr_Nucleos = Label(inst, text = nr_nucleos)
        self.infoBateria = Label(inst, text = str(bateria)+str('%'))
        self.infoKernel = Label(inst, text = kernel)
        self.infoVersao_Kernel = Label(inst, text = kernel_versao)
        self.infoUtilizador = Label(inst, text = utilizador)
        #self.infoUso_CPU = Label(inst, text='')


        #pack rótulos
        self.lbProcessador.pack()
        self.lbArquitectura.pack()
        self.lbBits.pack()
        self.lbFrequencia_disponivel.pack()
        self.lbFrequencia_usada.pack()
        self.lbNr_Nucleos.pack()
        self.lbBateria.pack()
        self.lbKernel.pack()
        self.lbVersao_Kernel.pack()
        self.lbUtilizador.pack()
        #self.lbUso_CPU.pack()

        # pack informação
        self.infoProcessador.pack()
        self.infoArquitectura.pack()
        self.infoBits.pack()
        self.infoFrequencia_disponivel.pack()
        self.infoFrequencia_usada.pack()
        self.infoNr_Nucleos.pack()
        self.infoBateria.pack()
        self.infoKernel.pack()
        self.infoVersao_Kernel.pack()
        self.infoUtilizador.pack()
        #self.infoUso_CPU.pack()

        #Place rótulos

        self.lbProcessador.place(x = 40, y = 150)
        self.lbArquitectura.place(x = 40, y = 180)
        self.lbBits.place(x = 40, y = 210)
        self.lbFrequencia_disponivel.place(x = 40, y = 240)
        self.lbFrequencia_usada.place(x = 40, y = 270)
        self.lbNr_Nucleos.place(x = 40, y = 300)
        self.lbBateria.place(x = 40, y = 330)
        self.lbKernel.place(x = 40, y = 360)
        self.lbVersao_Kernel.place(x = 40, y = 390)
        self.lbUtilizador.place(x = 40, y = 420)
        #self.lbUso_CPU.place(x = 40, y = 450 )


        #Place informação

        self.infoProcessador.place(x =250, y = 150)
        self.infoArquitectura.place(x =250, y = 180)
        self.infoBits.place(x =250, y = 210)
        self.infoFrequencia_disponivel.place(x =250, y = 240)
        self.infoFrequencia_usada.place(x =250, y = 270)
        self.infoNr_Nucleos.place(x =250, y = 300)
        self.infoBateria.place(x =250, y = 330)
        self.infoKernel.place(x =250, y = 360)
        self.infoVersao_Kernel.place(x =250, y = 390)
        self.infoUtilizador.place(x =250, y = 420)
        #self.infoUso_CPU.place(x = 250, y = 450)


'''
    def uso_cpu(self):
        while True:
            self.infoUso_CPU['text'] = psutil.cpu_percent(interval=1)
'''

inst = Tk()										#Instanciando a classe Tk
#inst['bg'] = 'gray'								#Alterando a cor do fundo
#ícone
#inst.wm_iconbitmap('~/Documentos/Python/logo.ico')

inst.title('Informação do Computador')						#Nome/título da janela
Processador(inst)										#Assossiando a classe Login ao mestre(instância)
inst.geometry('550x650')						#Definindo o tamanho da janela
inst.resizable('False','False')					#Impedindo o redimensionamento da tela
inst.mainloop()									#Iniciando o programa