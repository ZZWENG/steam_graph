import numpy as np

def extract_feat_from_review(review):
    feat = []
    if len(review['funny']) > 0:
        funny = int(review['funny'].split()[0].replace(',', ''))
        feat.append(funny)
    else:
        feat.append(0)
    feat.append(int(review['recommend']))
    if 'fun' in review['review']:
        feat.append(1)
    else:
        feat.append(0)
    return np.array(feat)

###########################################
### Save graph for Gephi visualizations ###
###########################################
def save_graph(bundle_item_map):
    with open('steam_edge_list.csv', 'w') as f:
        for bundle, items in bundle_item_map.iteritems():
            for item in items:
                f.write(str(bundle+3000)+','+str(item)+'\n')  # bundle id to game id
    with open('steam_node_list.csv', 'w') as g:
        for item_i in items_set:
            item_id = item_id_lookup[item_i]
            item_name = item_name_map[item_id]
            g.write(str(item_i)+';'+item_name.encode('ascii','ignore').replace(';',',')+';'+'g\n')
        for bundle_i in bundle_item_map.keys():
            g.write(str(bundle_i+3000)+';bundle;b\n')
            
            
def save_user_graph(user_item_map, user_bundle_map):
    with open('steam_user_edge_list.csv', 'w') as f:
        f.write('Source,Target\n')
        for user, bundles in user_bundle_map.iteritems():
            for bundle in bundles:
                f.write(str(user+6000)+','+str(bundle+3000)+'\n')  # user id to bundle id
        for user, items in user_item_map.iteritems():
            for item in items:
                f.write(str(user+6000)+','+str(item)+'\n')  # user id to game id
                
    with open('steam_user_node_list.csv', 'w') as g:
        g.write('id;name;type\n')
        for item_i in items_set:
            item_id = item_id_lookup[item_i]
            item_name = item_name_map[item_id]
            g.write(str(item_i)+';'+item_name.encode('ascii','ignore').replace(';',',')+';'+'g\n')
        for bundle_i in bundle_item_map.keys():
            g.write(str(bundle_i+3000)+';bundle;b\n')
        for user in user_item_map.keys():
            g.write(str(user+6000)+';user;u\n')