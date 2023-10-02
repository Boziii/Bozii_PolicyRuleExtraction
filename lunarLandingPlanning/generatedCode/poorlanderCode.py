def predict(observation):
	action = 0
	lander_x= observation[0]
	lander_y= observation[1]
	x_velocity= observation[2]
	y_velocity= observation[3]
	angle= observation[4]
	angle_velocity= observation[5]
	left_leg_contact= observation[6]
	right_leg_contact= observation[7]

	if weShould_nothing(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
		action = 0
	if weShould_left_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
		action = 1
	if weShould_main_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
		action = 2
	if weShould_right_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
		action = 3

	return action
def weShould_nothing(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(right_leg_contact == True):
		return True
	return False

def weShould_left_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):

	return False

def weShould_main_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(right_leg_contact != True):
		if(y_velocity <= -0.21934568881988525):
			if(angle_velocity <= -0.02332074288278818):
				return True
			else:
				return True
	return False

def weShould_right_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(right_leg_contact != True):
		if(y_velocity > -0.21934568881988525):
			return True
	return False

