import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 31, 1), 'tip')

quality.automf(3)
service.automf(3)
quality.view()
service.view()

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 15])
tip['medium'] = fuzz.trimf(tip.universe, [0, 15, 30])
tip['high'] = fuzz.trimf(tip.universe, [15, 30, 30])
tip.view()

rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

tipping = ctrl.ControlSystemSimulation(ctrl.ControlSystem([rule1, rule2, rule3]))

tipping.input['quality'] = 4
tipping.input['service'] = 4
tipping.compute()
print(tipping.output['tip'])
tip.view(sim=tipping)

tipping.input['quality'] = 7
tipping.input['service'] = 4
tipping.compute()
print(tipping.output['tip'])
tip.view(sim=tipping)

tipping.input['quality'] = 4
tipping.input['service'] = 9
tipping.compute()
print(tipping.output['tip'])
tip.view(sim=tipping)

tipping.input['quality'] = 10
tipping.input['service'] = 10
tipping.compute()
print(tipping.output['tip'])

tip.view(sim=tipping)

# zad2


# a


distance = ctrl.Antecedent(np.arange(0, 141, 1), 'distance')
speed = ctrl.Antecedent(np.arange(0, 121, 1), 'speed')
acceleration = ctrl.Consequent(np.arange(-1, 1.1, 0.1), 'acceleration')

distance['low'] = fuzz.trapmf(np.arange(0, 141, 1), [0, 0, 20, 45])
distance['medium'] = fuzz.trapmf(np.arange(0, 141, 1), [20, 45, 110, 130])
distance['high'] = fuzz.trapmf(np.arange(0, 141, 1), [105, 130, 140, 140])

speed['low'] = fuzz.trapmf(np.arange(0, 121, 1), [0, 0, 15, 65])
speed['medium'] = fuzz.trimf(np.arange(0, 121, 1), [15, 65, 115])
speed['high'] = fuzz.trapmf(np.arange(0, 121, 1), [65, 115, 120, 120])

acceleration['low-'] = fuzz.trimf(acceleration.universe, [-0.4, 0, 0.1])
acceleration['low+'] = fuzz.trimf(acceleration.universe, [-0.1, 0, 0.4])
acceleration['high-'] = fuzz.trapmf(acceleration.universe, [-1, -1, -0.4, 0])
acceleration['high+'] = fuzz.trapmf(acceleration.universe, [0, 0.4, 1, 1])

distance.view()
speed.view()
acceleration.view()


# b


rule1 = ctrl.Rule(distance['low'] | speed['low'], acceleration['high-'])
rule2 = ctrl.Rule(distance['medium'] | speed['low'], acceleration['low-'])
rule3 = ctrl.Rule(distance['high'] | speed['low'], acceleration['low-'])
rule4 = ctrl.Rule(distance['low'] | speed['medium'], acceleration['high+'])
rule5 = ctrl.Rule(distance['medium'] | speed['medium'], acceleration['low-'])
rule6 = ctrl.Rule(distance['high'] | speed['medium'], acceleration['low-'])
rule7 = ctrl.Rule(distance['low'] | speed['high'], acceleration['low+'])
rule8 = ctrl.Rule(distance['medium'] | speed['high'], acceleration['high-'])
rule9 = ctrl.Rule(distance['high'] | speed['high'], acceleration['low-'])

driving = ctrl.ControlSystemSimulation(ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9]))

# c


driving.input['distance'] = 30
driving.input['speed'] = 50
driving.compute()
print(driving.output['acceleration'])
acceleration.view(sim=driving)

driving.input['distance'] = 100
driving.input['speed'] = 50
driving.compute()
print(driving.output['acceleration'])
acceleration.view(sim=driving)

driving.input['distance'] = 30
driving.input['speed'] = 65
driving.compute()
print(driving.output['acceleration'])
acceleration.view(sim=driving)
