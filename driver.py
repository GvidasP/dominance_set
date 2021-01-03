from queens import Queens
from bishops import Bishops
import testing

print('Pasirinkite paleidimo buda:\n0 - Variantu radimas NxN lentoje;\n1 - Greicio analize')

global case
case = int(input(''))

print('\n')

if(case == 0):
    n = int(input('Iveskite lentos dydi: '))

    queens_class = Queens(n, output=True)
    bishops_class = Bishops(n, output=True)

    queens_class.solve()
    bishops_class.solve()

    print('Rezultatai isvesti failuose solution_bishops ir solution_queens.')

elif(case == 1):
    print('Iveskite lentos NxN dydi:')
    n_from = int(input('Pradinis N = '))
    n_to = int(input('Paskutinis N = '))

    testing.do_testing(n_from, n_to)
