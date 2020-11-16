my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
# 1
my_sample_list[1] = 'Steven'
print('primer paso: ', my_sample_list)
# 2
my_sample_list.append('Pepe')
print('segundo paso: ', my_sample_list)
# 3
my_sample_list[2] = my_sample_list[0] + my_sample_list[4]
print('tercer paso: ', my_sample_list)

#4

for i in reversed(range(len(my_sample_list))):
    print('cuarto paso: ', my_sample_list[i])

