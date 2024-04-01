def line():
   print('-' * 40)

def sides():
   for i in range(3):
      print('|' + ' ' * 38 + '|')

def box():
   line()
   sides()
   line()

box()
