def predict(observation):
	action = 0
	car_position= observation[0]
	car_velocity= observation[1]

	if weShould_accelerate_left(car_position, car_velocity):
		action = 0
	if weShould_nothing(car_position, car_velocity):
		action = 1
	if weShould_accelerate_right(car_position, car_velocity):
		action = 2

	return action
def weShould_accelerate_left(car_position, car_velocity):
	if(car_velocity <= -0.0007326875056605786):
		if(car_position > -0.9431617856025696):
			if(car_position <= -0.884903073310852):
				if(car_velocity <= -0.019993042573332787):
					return True
				else:
					if(car_velocity <= -0.016577613539993763):
						if(car_position > -0.9122465550899506):
							return True
			else:
				return True
	else:
		if(car_velocity <= 0.013955564238131046):
			if(car_position <= -0.34686462581157684):
				if(car_position <= -0.374004527926445):
					if(car_velocity <= 0.00012927717762067914):
						if(car_position > -0.4246840476989746):
							return True
				else:
					if(car_velocity <= 0.006931324256584048):
						return True
			else:
				if(car_velocity <= 0.01053376728668809):
					return True
				else:
					if(car_position > -0.31659844517707825):
						return True
		else:
			if(car_velocity <= 0.01614677906036377):
				if(car_position > -0.3126959800720215):
					return True
	return False

def weShould_nothing(car_position, car_velocity):

	return False

def weShould_accelerate_right(car_position, car_velocity):
	if(car_velocity <= -0.0007326875056605786):
		if(car_position <= -0.9431617856025696):
			return True
		else:
			if(car_position <= -0.884903073310852):
				if(car_velocity > -0.019993042573332787):
					if(car_velocity <= -0.016577613539993763):
						if(car_position <= -0.9122465550899506):
							return True
					else:
						return True
	else:
		if(car_velocity <= 0.013955564238131046):
			if(car_position <= -0.34686462581157684):
				if(car_position <= -0.374004527926445):
					if(car_velocity <= 0.00012927717762067914):
						if(car_position <= -0.4246840476989746):
							if(car_position <= -0.5271211266517639):
								return True
							else:
								if(car_position <= -0.5027747005224228):
									return True
								else:
									return True
					else:
						return True
				else:
					if(car_velocity > 0.006931324256584048):
						return True
			else:
				if(car_velocity > 0.01053376728668809):
					if(car_position <= -0.31659844517707825):
						return True
		else:
			if(car_velocity <= 0.01614677906036377):
				if(car_position <= -0.3126959800720215):
					return True
			else:
				return True
	return False

