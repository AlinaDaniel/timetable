from project3 import Load,TimeTable
Load.load_data('classes.txt')
my_table = TimeTable(Load.data, '19704.2')
print(my_table)
