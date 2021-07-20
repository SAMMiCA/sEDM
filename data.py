# import json
# import torch
# import numpy as np
# import transformers
#
#
# tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
# model = transformers.BertModel.from_pretrained('bert-base-uncased')
#
# f = open("recipe_data/layer_temp.json")
#
# data = json.load(f)
# for i in range(len(data)):
#     ingredients = data[i]['ingredients']
#     title = data[i]['title']
#     instructions = data[i]['instructions']
#     input_ids_title = torch.unsqueeze(torch.Tensor(tokenizer.encode(title)), 0).long()
#     embed_t = model(input_ids_title)
#     menu = embed_t[0][0]
#     for ing in range(len(ingredients)):
#         input_ids_ing = torch.unsqueeze(torch.Tensor(tokenizer.encode(ingredients[ing]['text'])), 0).long()
#         embed_ing = model(input_ids_ing)
#         ingre = embed_ing[0][0]
#     for ins in range(len(instructions)):
#         input_ids_ins = torch.unsqueeze(torch.Tensor(tokenizer.encode(instructions[ins]['text'])), 0).long()
#         embed_ins = model(input_ids_ins)
#         recipe = embed_ins[0][0]
#     if i == 0:
#         break

import torch
from transformers import BertTokenizer, BertModel
from torch.nn.utils.rnn import pack_padded_sequence
from recipe import recipe_dict

tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

# print(len(recipe_dict))
def dataload_train(v):
    input_ids_title = []
    input_ids_recipe = []
    input_ids_ingre = []
    # print(k)
    # print(v)
    title = v["food_type"][0]
    ingre = v["ingredient"][:]
    recipe = v["recipe"][:]
    # print(title)
    # print(ingre)
    # print(recipe)

    encoded_title = tokenizer.encode_plus(text=title,  # the sentence to be encoded
                                    add_special_tokens=True,  # Add [CLS] and [SEP]
                                    max_length = 16,  # maximum length of a sentence
                                    pad_to_max_length=True,  # Add [PAD]s
                                    return_attention_mask=True,  # Generate the attention mask
                                    return_tensors='pt')  # ask the function to return PyTorch tensors)
    input_ids_title.append(encoded_title['input_ids'])
    input_ids_title = torch.cat(input_ids_title, dim=0)

    length_ingre = []
    for ing in ingre:
        encoded_ingre = tokenizer.encode_plus(text=ing,  # the sentence to be encoded
                                          add_special_tokens=True,  # Add [CLS] and [SEP]
                                          max_length=16,  # maximum length of a sentence
                                          pad_to_max_length=True,  # Add [PAD]s
                                          return_attention_mask=True,  # Generate the attention mask
                                          return_tensors='pt')  # ask the function to return PyTorch tensors)
        input_ids_ingre.append(encoded_ingre['input_ids'])
    input_ids_ingre = torch.cat(input_ids_ingre, dim=0)

    for re in recipe:
        encoded_recipe = tokenizer.encode_plus(text=re,  # the sentence to be encoded
                                          add_special_tokens=True,  # Add [CLS] and [SEP]
                                          max_length=64,  # maximum length of a sentence
                                          pad_to_max_length=True,  # Add [PAD]s
                                          return_attention_mask=True,  # Generate the attention mask
                                          return_tensors='pt')  # ask the function to return PyTorch tensors)
        input_ids_recipe.append(encoded_recipe['input_ids'])
    input_ids_recipe = torch.cat(input_ids_recipe, dim=0)

    model = BertModel.from_pretrained('bert-base-cased',
                                      output_hidden_states=True,  # Whether the model returns all hidden-states.
                                      )
    model.eval()
    with torch.no_grad():

        title_emb = model(input_ids_title)[0]
        recipe_emb = model(input_ids_recipe)[0]
        ingre_emb = model(input_ids_ingre)[0]

    return title_emb, ingre_emb, recipe_emb


def dataload_test(ingre):
    input_ids_ingre = []
    for ing in ingre:
        encoded_ingre = tokenizer.encode_plus(text=ing,  # the sentence to be encoded
                                          add_special_tokens=True,  # Add [CLS] and [SEP]
                                          max_length=16,  # maximum length of a sentence
                                          pad_to_max_length=True,  # Add [PAD]s
                                          return_attention_mask=True,  # Generate the attention mask
                                          return_tensors='pt')  # ask the function to return PyTorch tensors)
        input_ids_ingre.append(encoded_ingre['input_ids'])
    input_ids_ingre = torch.cat(input_ids_ingre, dim=0)

    model = BertModel.from_pretrained('bert-base-cased',
                                      output_hidden_states=True,  # Whether the model returns all hidden-states.
                                      )
    model.eval()
    with torch.no_grad():
        ingre_emb = model(input_ids_ingre)[0]

    return ingre_emb
