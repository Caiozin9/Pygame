import time
import numpy


# ndarray1 = numpy.zeros(100000)
# print(' 1- Conteúdo de Lista:', ndarray1, f', o tamanho: {len(ndarray1)}')
#
# ndarray1 = numpy.ones(100000)
# print(' 2- Conteúdo de Lista:', ndarray1, f', o tamanho: {len(ndarray1)}')
#
# ndarray1 = numpy.linspace(10, 1000, 1000)
# print(' 3- Conteúdo de Lista:', ndarray1, f', o tamanho: {len(ndarray1)}')

# start_time = time.time()
# lista = [0] * 1000000000
# end_time = time.time()
# elapsed_time = end_time - start_time
# print (f'A criação da lista de 1 bilhão de elementos levou {elapsed_time}')
#
# start_time = time.time()
# ndarray = numpy.zeros(1000000000)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print (f'A criação de um ndarray de 1 bilão de elementos levou {elapsed_time}')

# start_time = time.time()
# ndarray_uint8 = numpy.zeros(1000000000, dtype='uint8')
# end_time = time.time()
# elapsed_time = end_time - start_time
# print (f'A criação de um ndarray de 1 bilhão de elementos em int de 8 não sinalizado levou {elapsed_time} segundos')

# vetor_a = numpy.linspace(10, 1000, 100)
# vetor_b = numpy.linspace(10, 3000, 100)
# vetor_c = numpy.linspace(10, 8000, 100)
#
# print(vetor_a)
# print(vetor_b)
# print(vetor_c)
#
# numpy.savetxt('vetor_a.txt', vetor_a, fmt='%f', delimiter=';')
# numpy.savetxt('vetor_b.txt', vetor_b, fmt='%f', delimiter=';')
# numpy.savetxt('vetor_c.txt', vetor_c, fmt='%f', delimiter=';')

import plotly.express

array_a = numpy.loadtxt('vetor_a.txt', dtype=numpy.float64, delimiter=';')
array_b = numpy.loadtxt('vetor_b.txt', dtype=numpy.float64, delimiter=';')
array_c = numpy.loadtxt('vetor_c.txt', dtype=numpy.float64, delimiter=';')
print(array_a)

array_abc = numpy.vstack([array_a, array_b, array_c])
print(array_abc)
array_abc = array_abc.transpose()
print(array_abc)
fig = plotly.express.line(array_abc)
fig.show()



