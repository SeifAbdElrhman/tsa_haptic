from time import perf_counter,sleep
from lcm_interface import commands_message, publish

commands_message.mode = 0 
# commands_message.desired_position = np.array([0, 0, 0, 0])

for i in range(200):
    
    commands_message.arm = True
    commands_message.mode = 11
    commands_message.desired_position[:3] = [200, 200, 200]
    commands_message.desired_speed[:3] = 3*[0]
    publish("commands")
    sleep(0.01)



try:
    t_upd = 0 
    t0 = perf_counter()
    while True:
        t = perf_counter() - t0

        if t - t_upd >= 1E-2:
            commands_message.arm = True
            commands_message.timestamp = int(t*1000)
            commands_message.mode = 21
            commands_message.desired_position[:3] = [0, 0, 80]
            
            publish("commands")
            t_upd = t


except KeyboardInterrupt:
    print('Exit by interrupt')
except Exception as e:
    print(e)
finally:
    print('Controller is turning off...')
    commands_message.arm = True    
    commands_message.mode = 12
    commands_message.desired_position = 4*[0]
    commands_message.desired_speed = 4*[0]
    publish("commands")

