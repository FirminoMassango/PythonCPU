from variaveis import *
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Informações do computador")
        self.imagem = Gtk.Image.new_from_file('imagem/cpu.png')

        #Rótulos
        self.lbProcessador = Gtk.Label(label=processador)

        self.lbProcessador = Gtk.Label(label='Processador: ', xalign=0)
        self.lbArquitectura = Gtk.Label(label='Arquitectura: ', xalign=0)
        self.lbBits = Gtk.Label(label='Bits: ', xalign=0)
        self.lbFrequencia_disponivel = Gtk.Label(label='Frequência disponível: ', xalign=0)
        self.lbFrequencia_usada = Gtk.Label(label='Frequência usada: ', xalign=0)
        self.lbNr_Nucleos = Gtk.Label(label='Número de núcleos (Processador): ', xalign=0)
        self.lbBateria = Gtk.Label(label='Bateria: ', xalign=0)
        self.lbKernel = Gtk.Label(label='Sistema: ', xalign=0)
        self.lbVersao_Kernel = Gtk.Label(label='Versão do Kernel: ', xalign=0)
        self.lbUtilizador = Gtk.Label(label='Utilizador: ', xalign=0)
        # self.lbUso_CPU = Label(inst, text = 'Uso do Processador: ')

        # Info
        self.infoProcessador = Gtk.Label(label=processador, xalign=3)
        self.infoArquitectura = Gtk.Label(label=arquitectura, xalign=3)
        self.infoBits = Gtk.Label(label=bits, xalign=2)
        self.infoFrequencia_disponivel = Gtk.Label(label=frequencia_disponivel, xalign=2)
        self.infoFrequencia_usada = Gtk.Label(label=frequencia_usada, xalign=2)
        self.infoNr_Nucleos = Gtk.Label(label=nr_nucleos, xalign=2)
        self.infoBateria = Gtk.Label(label=str(bateria) + str('%'), xalign=2)
        self.infoKernel = Gtk.Label(label=kernel, xalign=2)
        self.infoVersao_Kernel = Gtk.Label(label=kernel_versao, xalign=2)
        self.infoUtilizador = Gtk.Label(label=utilizador, xalign=2)







        #Button
        self.button1 = Gtk.Button(label="Botão 1")
        self.button2 = Gtk.Button(label="Botão 2")
        self.button3 = Gtk.Button(label="Botão 3")
        self.button1.connect("clicked", self.on_button_clicked)

       #Boxes
        # self.hbox= Gtk.HBox(spacing  = 50)
        self.vbox = Gtk.VBox(spacing = 50)

        # self.add(self.button)
        # self.add(self.hbox)
        self.add(self.vbox)

        # self.vbox.pack_start(self.lbProcessador,False, False, 0)
        # self.vbox.pack_start(self.button1,True, True, 0)
        # self.vbox.pack_start(self.button2, True, True, 0)

        # self.vbox.pack_start(self.hbox, False, False, 0)
        # self.vbox.pack_start(self.button3, True, True, 1)

        # Grid
        self.grid = Gtk.Grid()
        self.add(self.grid)


        self.vbox.pack_start(self.imagem, True, False, 0)
        self.vbox.pack_start(self.grid, True, True, 0)

                #Imagem
        self.grid.add(self.imagem)

                #Processador
        self.grid.attach(self.lbProcessador, 0, 1, 1, 1)
        self.grid.attach_next_to(self.infoProcessador, self.lbProcessador, Gtk.PositionType.RIGHT, 1, 1)

                #Arquitectura
        self.grid.attach(self.lbArquitectura, 0, 2, 1, 1)
        self.grid.attach_next_to(self.infoArquitectura, self.lbArquitectura, Gtk.PositionType.RIGHT, 1, 1)

                # Bits
        self.grid.attach(self.lbBits, 0, 3, 1, 1)
        self.grid.attach_next_to(self.infoBits, self.lbBits, Gtk.PositionType.RIGHT, 1, 1)

                # Frequência Disponível
        self.grid.attach(self.lbFrequencia_disponivel, 0, 4, 1, 1)
        self.grid.attach_next_to(self.infoFrequencia_disponivel, self.lbFrequencia_disponivel, Gtk.PositionType.RIGHT, 1, 1)

                # Frequência Usada
        self.grid.attach(self.lbFrequencia_usada, 0, 5, 1, 1)
        self.grid.attach_next_to(self.infoFrequencia_usada, self.lbFrequencia_usada, Gtk.PositionType.RIGHT, 1, 1)

                # Nr Núcleos
        self.grid.attach(self.lbNr_Nucleos, 0, 6, 1, 1)
        self.grid.attach_next_to(self.infoNr_Nucleos, self.lbNr_Nucleos, Gtk.PositionType.RIGHT, 1, 1)

                # Bateria
        self.grid.attach(self.lbBateria, 0, 7, 1, 1)
        self.grid.attach_next_to(self.infoBateria, self.lbBateria, Gtk.PositionType.RIGHT, 1, 1)

                # Sistema
        self.grid.attach(self.lbKernel, 0, 8, 1, 1)
        self.grid.attach_next_to(self.infoKernel, self.lbKernel, Gtk.PositionType.RIGHT, 1, 1)

                # Versão do Kernel
        self.grid.attach(self.lbVersao_Kernel, 0, 9, 1, 1)
        self.grid.attach_next_to(self.infoVersao_Kernel, self.lbVersao_Kernel, Gtk.PositionType.RIGHT, 1, 1)

                # Utilizador
        self.grid.attach(self.lbUtilizador, 0, 10, 1, 1)
        self.grid.attach_next_to(self.infoUtilizador, self.lbUtilizador, Gtk.PositionType.RIGHT, 1, 1)



    def on_button_clicked(self, widget):
        print("Hello World")
    # button = Gtk.Box()
    # print(dir(button.props))


win = MyWindow()
win.set_position(Gtk.WindowPosition.CENTER)
win.set_default_size(550,600)
win.set_resizable(False)
win.connect("destroy", Gtk.main_quit)
win.show_all()

if __name__ == "__main__":
    Gtk.main()

