
from tkinter import *
from variaveis import *



class Processador(object):
    def __init__(self,inst):

        # Imagem
        imagem = PhotoImage(file='cpu.gif')
        self.imagemIcon = Label(inst, image=imagem, bg = 'white')
        self.imagemIcon.image = imagem
        self.imagemIcon.pack()

        #Rótulos
        self.lbProcessador = Label(inst, text = 'Processador: ', bg= 'white')
        self.lbArquitectura = Label(inst, text = 'Arquitectura: ', bg= 'white')
        self.lbBits = Label(inst, text = 'Bits: ', bg= 'white')
        self.lbFrequencia_disponivel = Label(inst, text = 'Frequência disponível: ', bg= 'white')
        self.lbFrequencia_usada = Label(inst, text = 'Frequência usada: ', bg= 'white')
        self.lbNr_Nucleos = Label(inst, text = 'Número de núcleos (Processador): ', bg= 'white')
        self.lbBateria = Label(inst, text = 'Bateria: ', bg= 'white')
        self.lbKernel = Label(inst, text = 'Sistema: ', bg= 'white')
        self.lbVersao_Kernel = Label(inst, text = 'Versão do Kernel: ', bg= 'white')
        self.lbUtilizador = Label(inst, text = 'Utilizador: ', bg= 'white')
        #self.lbUso_CPU = Label(inst, text = 'Uso do Processador: ')

        self.infoProcessador = Label(inst,text = processador, bg= 'white')
        self.infoArquitectura = Label(inst, text = arquitectura, bg= 'white')
        self.infoBits = Label(inst,text = bits, bg= 'white')
        self.infoFrequencia_disponivel = Label(inst, text = frequencia_disponivel, bg= 'white')
        self.infoFrequencia_usada = Label(inst, text = frequencia_usada, bg= 'white')
        self.infoNr_Nucleos = Label(inst, text = nr_nucleos, bg= 'white')
        self.infoBateria = Label(inst, text = str(bateria)+str('%'), bg= 'white')
        self.infoKernel = Label(inst, text = kernel, bg= 'white')
        self.infoVersao_Kernel = Label(inst, text = kernel_versao, bg= 'white')
        self.infoUtilizador = Label(inst, text = utilizador, bg= 'white')
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

        self.lbProcessador.place(x = 40, y = 170)
        self.lbArquitectura.place(x = 40, y = 200)
        self.lbBits.place(x = 40, y = 230)
        self.lbFrequencia_disponivel.place(x = 40, y = 270)
        self.lbFrequencia_usada.place(x = 40, y = 300)
        self.lbNr_Nucleos.place(x = 40, y = 330)
        self.lbBateria.place(x = 40, y = 360)
        self.lbKernel.place(x = 40, y = 390)
        self.lbVersao_Kernel.place(x = 40, y = 420)
        self.lbUtilizador.place(x = 40, y = 450)
        #self.lbUso_CPU.place(x = 40, y = 450 )


        #Place informação

        self.infoProcessador.place(x =250, y = 170)
        self.infoArquitectura.place(x =250, y = 200)
        self.infoBits.place(x =250, y = 230)
        self.infoFrequencia_disponivel.place(x =250, y = 270)
        self.infoFrequencia_usada.place(x =250, y = 300)
        self.infoNr_Nucleos.place(x =250, y = 330)
        self.infoBateria.place(x =250, y = 360)
        self.infoKernel.place(x =250, y = 390)
        self.infoVersao_Kernel.place(x =250, y = 420)
        self.infoUtilizador.place(x =250, y = 450)
        #self.infoUso_CPU.place(x = 250, y = 450)


'''
    def uso_cpu(self):
        while True:
            self.infoUso_CPU['text'] = psutil.cpu_percent(interval=1)
'''

inst = Tk()										#Instanciando a classe Tk
inst['bg'] = 'white'#inst['bg'] = 'gray'								#Alterando a cor do fundo
#ícone
#inst.wm_iconbitmap('~/Documentos/Python/logo.ico')

inst.title('Informação do Computador')						#Nome/título da janela
Processador(inst)										#Assossiando a classe Login ao mestre(instância)
inst.geometry('550x650')						#Definindo o tamanho da janela
inst.resizable('False','False')					#Impedindo o redimensionamento da tela
inst.mainloop()									#Iniciando o programa