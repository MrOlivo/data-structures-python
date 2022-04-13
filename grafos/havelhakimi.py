class HavelHakimi(object):
    def algorithm(self, arreglo):
        try:
            while arreglo:
                arreglo.sort(reverse=True)
                print(arreglo)
                d = arreglo.pop(0)
                if d > len(arreglo):
                    print('Value (%s) is greater than array length (%s) itselft' % (
                        d, len(arreglo)))
                    break
                if d == 0:
                    break
                for i in range(d):
                    arreglo[i] -= 1
        except:
            print('Error')
