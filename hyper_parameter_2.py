import numpy as np


class hp(object):

    # env
    d_y_max = 392.5
    d_y_min = -32.5
    d_margin = 0.2 * 0.05 * (d_y_max - d_y_min)#Geometric mean w-space
    joint_wrist_max = 90 * np.pi / 180.0
    joint_wrist_min = -120 * np.pi / 180.0
    joint_max = np.array([140.0, -45.0, 150.0, 140.0, -45.0, 150.0]) * np.pi / 180.0
    joint_min = np.array([-140.0, -180.0, 45.0, -140.0, -180.0, 45.0]) * np.pi / 180.0
    step_size = 0.05 * (np.prod(joint_max - joint_min)**(1.0/6.0))#Geometric mean c-space
    goal_bound = 0.2 * step_size
    margin = goal_bound #makes max value lower and min value higher and also increase node check boundary
    env_noise = 0.002 #noise in step fuction
    c_check_acc = 0.2 #accuracy of path collision(step check)
    state_dim = 13 #delta joint and goal(12 = 6D x 2) with features of obstacle location(number of features = 1)
    action_dim = 6

    # agent
    lr_actor = 0.001
    lr_critic = 0.001
    tau = 0.005
    actor_l2 = 1.0
    her_k = 4
    max_time_step = 50

    target_noise_std = 0.2
    target_noise_clip = 0.5
    policy_delay = 2
    discount_factor = 0.98
    batch_size = 512
    memory_size = 1000000
    random_action_prob = 0.1
    action_noise_std = 0.1

