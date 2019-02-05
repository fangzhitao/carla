import scipy.misc

import carla

from agents.navigation.autonomous_agent import AutonomousAgent

class MyAgent(AutonomousAgent):
    def setup(self):
        pass

    def sensors_setup(self):
        """
        Define the sensor suite required by the agent

        :return: a list containing the required sensors in the following format:

        [
            ['sensor.camera.rgb', {'x':x_rel, 'y': y_rel, 'z': z_rel,
                                   'yaw': yaw, 'pitch': pitch, 'roll': roll,
                                   'width': width, 'height': height, 'fov': fov}, 'Sensor01'],
            ['sensor.camera.rgb', {'x':x_rel, 'y': y_rel, 'z': z_rel,
                                   'yaw': yaw, 'pitch': pitch, 'roll': roll,
                                   'width': width, 'height': height, 'fov': fov}, 'Sensor02'],

            ['sensor.lidar.ray_cast', {'x':x_rel, 'y': y_rel, 'z': z_rel,
                                       'yaw': yaw, 'pitch': pitch, 'roll': roll}, 'Sensor03']
        ]

        """
        sensors = [['sensor.camera.rgb',
                   {'x':0.7, 'y':0.0, 'z':1.60, 'roll':0.0, 'pitch':0.0, 'yaw':0.0, 'width':800, 'height':600, 'fov':100},
                   'Center'],

                   ['sensor.camera.rgb',
                    {'x':0.7, 'y':-0.4, 'z': 1.60, 'roll': 0.0, 'pitch': 0.0, 'yaw': -45.0, 'width': 800, 'height': 600,
                     'fov': 100},
                    'Left'],

                   ['sensor.camera.rgb',
                    {'x':0.7, 'y':0.4, 'z':1.60, 'roll':0.0, 'pitch':0.0, 'yaw':45.0, 'width':800, 'height':600,
                     'fov':100},
                    'Right']]


        return sensors

    def run_step(self):
        """
        Execute one step of navigation.
        :return: control
        """

        print('Saving images...')
        scipy.misc.imsave('outfile.png', self.data_buffers['Left'])


        control = carla.VehicleControl()
        control.steer = 0.0
        control.throttle = 1.0
        control.brake = 0.0
        control.hand_brake = False
        control.manual_gear_shift = False

        return control