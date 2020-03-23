from math import floor
import cpuinfo
import platform
import psutil




processador = cpuinfo.get_cpu_info()['brand']
arquitectura = cpuinfo.get_cpu_info()['arch']
bits = cpuinfo.get_cpu_info()['bits']
frequencia_disponivel = cpuinfo.get_cpu_info()['hz_advertised']
frequencia_usada = cpuinfo.get_cpu_info()['hz_actual']

#platform
kernel = platform.system()
kernel_versao = platform.release()
utilizador = platform.node()

#psutil
nr_nucleos = psutil.cpu_count()
bateria = floor(psutil.sensors_battery().percent)




