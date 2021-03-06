import random
from util import Feature,Feature_pool,Note
import mido
from copycat import midi_read



def containsPattern(feature_pool,notes,tick,low=3,up=5):
  '''
  
  :param feature_pool:  a pool to store all features extracted
  :param note: source note list
  :param time: source time list
  :param low: min length of a pattern
  :param up:  max length of a pattern

  :return: none
  '''
  print('++++++++Feature Extraction+++++++++++')
  for m in range (low,up+1):
    i = 0
    while i < len(notes)-m+1:
        p = tuple(notes[i:i+m])
        # new_feature = feature(note[i:i+m],time[i:i+m])
        feature_pool.new_feature(notes[i:i+m],tick)
        # features_list.append(new_feature)
        # if p * k == arr[i:i+m*k]:
        #     return features
        i += 1
    
    # feature_pool.show_pool()
    # return dict(result)

def compose(length, pool):
  '''
  generate a individual by picking from the pool, add up features 
  entill duration is stafisted( could be a bit longer)
  
  :param duraiton: 
  :param pool: 
  :return: 
  '''
  cur = 0
  individual =[] # a list of features
  while cur< length:
    
    x = random.choice(pool.feature_pool) #choice of feature
    individual.append(x.notes)
    
    cur += len(x.notes)
    
  return individual

def play(track):
  '''
  print out a individual
  :param track: 
  :return: 
  '''
  note = []
  time = []
  for item in track.feature_pool:
    note+=item.note
    time+=random.choice(item.time)
  print (note)
  print(time)
  
def read_to_notes(filename):
  '''
  
  :param input: a sequence
  :param output: 
  :return: 
  '''
  input,tick = midi_read(filename)
  print('Tick_per_beat=',tick)
  output = []
  velocity = 0
  time = 0
  channel =0
  for i in range(len(input[0])):
    
    duration = input[1][i]
    output.append(Note(channel, input[0][i], velocity, time, duration))
    time += duration
  return output,tick
    
#   
#   
# smk_note = [5, 7, 8,-1, 5, 7, 9, 8,-1, 5, 7, 8,-1, 7, 5]
# smk_time = [1, 1, 2,1, 1, 1, 1, 2,1, 1, 1, 2,1, 1, 4]
# smk_note = [5, 7, 8,-1, 5, 7, 9, 8,-1, 5, 7, 8,-1, 7, 5]+[5, 7, 8,-1, 5, 7, 9, 8,-1, 5, 7, 8,-1, 7, 5]
# smk_time = [1, 1, 2,1, 1, 1, 1, 2,1, 1, 1, 2,1, 1, 4]+[1, 1, 2,1, 1, 1, 1, 2,1, 1, 1, 2,1, 1, 4]
# feature_p = feature_pool()
# containsPattern(feature_p,smk_note,smk_time,3,5)
# min3_pool = feature_pool(feature_p.give_pool(3))
# # min3_pool.show_pool()
# # pool = make_pool(x)
# 
# x1 = compose(12,min3_pool)
# x2 =compose(12,min3_pool)
# x1.show_pool()
# x2.show_pool()
# play(x2)
# print(compose(12,min3_pool))

# star_note = [1,1,5,5,6,6,5,-1,4,4,3,3,2,2,1,-1,5,5,4,4,3,3,2,-1,5,5,4,4,3,3,2,-1]+[1,1,5,5,6,6,5,-1,4,4,3,3,2,2,1,-1,5,5,4,4,3,3,2,-1,5,5,4,4,3,3,2,-1]
# star_time = [1,1,1,1,1,1,2,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1]+[1,1,1,1,1,1,2,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1]
# feature_p = feature_pool()
# containsPattern(feature_p,star_note,star_time,3,5)
# min3_pool = feature_pool(feature_p.give_pool(3))
# # min3_pool.show_pool()
# # pool = make_pool(x)
# 
# x1 = compose(12,min3_pool)
# x2 =compose(12,min3_pool)
# x1.show_pool()
# x2.show_pool()
# play(x2)



# some generated star
# star_note = [1,1,5,5,6,6,5,-1,4,4,3,3,2,2,1,-1,5,5,4,4,3,3,2,-1,5,5,4,4,3,3,2,-1]
# star_time = [1,1,1,1,1,1,2,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1]
# [4, 4, 3, 3, 4, 3, 3, 2, -1, 4, 4, 3, 3, 2]
# [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1]
# [-1, 5, 5, 4, 4, 3, 3, 4, 3, 3, 2, -1]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]


