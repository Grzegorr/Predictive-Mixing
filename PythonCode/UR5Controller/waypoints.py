from math import pi

# home position - right angle between shouder and forearm
robot_homej = [-1.7626080116, -1.5486306453, -1.6470672151, -1.5008086238, 1.5735888536, -0.031415926536]
robot_home_l = [-0.19931, -0.448052, 0.452649, 0, 3.13094, -0.0228049]

#For mixing and sampling
mixing_home_l = [0.129577, -0.550784, 0.454364, 0.228642, 3.1262, -0.0216748]
mixing_sensor_down_home_l = [0.128516, -0.548173, 0.619766, 0, 0, 0]
sensing_above_the_eggs = [0.130781, -0.555521, 0.205379, 0, 0, 0]

sensing_above_the_eggs_high = [0.130713, -0.555018, 0.236909, 0, 0, 0] # this is for the mode when the probe moves upwards more


#Chewing
chewing_home_l = [0.0487648, -0.394838, 0.439984, 0.228667, 3.12616, -0.0217348]



























######NOT USED IN CURRENT PROJECT YET #####

#### Cooking waypoints ######
cooking_home_l = [-0.0313337, -0.591629, 0.288477, 1.19586, 2.88875, -0.0144897]
scrambling_home_l = [0.129567, -0.337269, 0.454375, 0.228624, 3.12624, -0.0217565]

#### Callibration waypoints ######
callibrate_left = [0.562206, -0.399603, 0.0281787, 1.19577, 2.88868, -0.0142948]
callibrate_right = [-0.599309, -0.34802, 0.0303375, 1.72242, 2.60719, -0.0102147]

#### midle of the pan waypoints
pan_middle_left = [0.116336, -0.656514, 0.458775, -0.0149256, -0.0147912, -0.391588]
pan_middle_right = [-0.0524189, -0.656498, 0.458775, -0.0149218, -0.0147087, -0.391585]

#TCPs
pincher_tcp = [0,0,0.01,0,0,0]