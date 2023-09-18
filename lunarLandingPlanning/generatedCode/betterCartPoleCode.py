def predict(observation):
	action = 0
	cart_position= observation[0]
	cart_velocity= observation[1]
	pole_angle= observation[2]
	pole_angular_velocity= observation[3]

	if weShould_move_left(cart_position, cart_velocity, pole_angle, pole_angular_velocity):
		action = 0
	if weShould_move_right(cart_position, cart_velocity, pole_angle, pole_angular_velocity):
		action = 1

	return action
def weShould_move_left(cart_position, cart_velocity, pole_angle, pole_angular_velocity):
	if(pole_angular_velocity <= -0.017):
		if(pole_angular_velocity <= -0.115):
			return True
		else:
			if(pole_angle <= 0.001):
				return True
	else:
		if(pole_angular_velocity <= 0.071):
			if(pole_angle <= -0.001):
				return True
	return False

def weShould_move_right(cart_position, cart_velocity, pole_angle, pole_angular_velocity):
	if(pole_angular_velocity <= -0.017):
		if(pole_angular_velocity > -0.115):
			if(pole_angle > 0.001):
				return True
	else:
		if(pole_angular_velocity <= 0.071):
			if(pole_angle > -0.001):
				return True
		else:
			return True
	return False

