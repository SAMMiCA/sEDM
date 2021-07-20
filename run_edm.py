import random
import numpy as np
from sedm import EDM, sEDM
from recipe import recipe_dict
from data import dataload_train, dataload_test
from old_recipe_data import data_load

# model = EDM()
model = sEDM()
total_ingre_list = []
for i in range(12):
    menu, ingre, recipe = data_load(i)
    total_ingre_list.append(ingre)
    print(i)
    model.train(menu, ingre, recipe)
total_ingre_list = np.array(total_ingre_list)

unique_ingre_list = []
for ingre in total_ingre_list:
    for ing in ingre:
        if ing not in unique_ingre_list:
            unique_ingre_list.append(ing)

num_sample = 10
total = 0
for i in range(100):
    sample_ingre = random.sample(unique_ingre_list, k=num_sample)
    ct = model.test(np.array([sample_ingre]))
    if ct == 0:
        ct=1
    total += ct
    print(total)

# for i, (k, v) in enumerate(recipe_dict.items()):
#     total_ingre_list.extend(v['ingredient'])
#     menu, ingre, recipe = dataload_train(v)
#     model.train(menu, ingre, recipe)
#     print(i)
# total_ingre_list = list(set(total_ingre_list))
#
# num_sample = 10
# total = 0
# for i in range(100):
#     sample_ingre = random.sample(total_ingre_list, k=num_sample)
#     sample_ingre = dataload_test(sample_ingre)
#     ct = model.test(sample_ingre.numpy())
#     if ct == 0:
#         ct=1
#     total += ct
#     print(total)




# menu, ingre, recipe = data_load(11)
# cue = np.array([ingre])
# model.test(cue)










# if __name__ == '__main__':
    # model = EDM()
    # total_ingre_list = []
    # menu, ingre, recipe = data_load(1)
    # total_ingre_list.append(ingre)
    # model.train(menu, ingre, recipe)

"""
i = 0: pass
i = 1: pass 
i = 2: pass
i = 3: pass
i = 4: pass
i = 5: 
i = 6: 
i = 7: 
i = 8: 
i = 9:
i = 10:
i = 11:   
"""

"""
food_type :  fried rice 
 
recipe :  beat 2 eggs thoroughly bowl 
recipe :  stir cooked rice bowl 
recipe :  slice 1/2 pieces spring onion 
recipe :  heat wok over high heat pour oil 
recipe :  stir-fry spring onion with oil 
recipe :  stir cooked rice into wok 
recipe :  season taste with pepper 
recipe :  pour one spoon oyster sauce stir mixture 


food_type :  fried rice 

recipe :  beat two eggs thoroughly bowl 
recipe :  stir cooked rice bowl 
recipe :  slice half pieces spring onion 
recipe :  heat wok over high heat pour oil 
recipe :  stir-fry spring onion with oil 
recipe :  stir cooked rice into wok 
recipe :  pour three spoons soy sauce 
recipe :  when soy sauce boils, stir mixture 


food_type :  fried rice 

recipe :  slice 1 piece spring onion 
recipe :  chop kimchi 
recipe :  heat wok over high heat pour oil 
recipe :  stir-fry spring onion with oil 
recipe :  stir-fry chopped kimchi with mixture 
recipe :  when kimchi is cooked, put one spoon chili powder 
recipe :  pour one spoon soy sauce 
recipe :  when soy sauce boils, stir cooked rice 
recipe :  drizzle 1/2 spoons sesame oil over rice mixture 


food_type :  fried rice 
when shrimp is cooked


food_type :  rolled omlet
roll omelet



food_type :  curry 
 
recipe :  dice 1/2 pieces onion 
recipe :  dice can ham 
recipe :  heat wok over high heat pour oil 
recipe :  stir-fry ham onion 
recipe :  pour 500ml milk 
recipe :  stir 100g curry powder simmer mixture 
recipe :  beat 2 eggs wok stir mixture 


japanese curry
cubed beef stew meat
carrot zucchini
"""