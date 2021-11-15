import pymel.core as pm
import json
import os, sys
obj_sets = [i for i in pm.selected() if i.name() == "ControlSet" and i.nodeType()=="objectSet"]
if not obj_sets:
    raise
dict_of_items = {}
for obj_set in obj_sets:
    obj_set_children = pm.sets(obj_set, q=1)
    for item in obj_set_children:
        item_attr = pm.listAttr(item, keyable=1)
        if not item_attr:continue
        main_dict[item.name()]= {}
        for each in item_attr:
            val = item.attr(each).get()
            main_dict[item.name()][each]= val

if os.path.exists('C:/temp'):
    path = 'c:/temp/'
# else:
#     path = raw_input()

if path:
    with open('{}/out.json'.format(path), 'w') as writer:
        json.dump(main_dict, writer, indent=2)
