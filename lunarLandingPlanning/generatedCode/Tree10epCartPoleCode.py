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
	if(pole_angular_velocity <= -0.016515093855559826):
		if(pole_angular_velocity <= -0.11481225490570068):
			return True
		else:
			if(pole_angle <= 0.0013758284621872008):
				return True
	else:
		if(pole_angular_velocity <= 0.07106633484363556):
			if(pole_angle <= -0.000866586749907583):
				return True
	return False

def weShould_move_right(cart_position, cart_velocity, pole_angle, pole_angular_velocity):
	if(pole_angular_velocity <= -0.016515093855559826):
		if(pole_angular_velocity > -0.11481225490570068):
			if(pole_angle > 0.0013758284621872008):
				return True
	else:
		if(pole_angular_velocity <= 0.07106633484363556):
			if(pole_angle > -0.000866586749907583):
				return True
		else:
			return True
	return False

