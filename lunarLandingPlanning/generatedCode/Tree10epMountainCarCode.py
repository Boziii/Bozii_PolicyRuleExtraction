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
	if(car_velocity <= -0.0007429399411194026):
		if(car_position <= -0.9177583456039429):
			if(car_velocity <= -0.023546687327325344):
				if(car_position > -0.9492785632610321):
					return True
		else:
			if(car_position <= -0.8889897763729095):
				if(car_velocity <= -0.016514434944838285):
					return True
			else:
				if(car_position <= -0.879206657409668):
					if(car_position <= -0.8803532421588898):
						return True
				else:
					return True
	else:
		if(car_velocity <= 0.011293863877654076):
			if(car_position <= -0.36911800503730774):
				if(car_position <= -0.3872663378715515):
					if(car_velocity <= 0.0001295892579946667):
						if(car_position > -0.41892318427562714):
							return True
				else:
					if(car_velocity <= 0.0038730697706341743):
						return True
			else:
				if(car_position <= -0.32232697308063507):
					if(car_velocity <= 0.005594694288447499):
						return True
					else:
						if(car_position > -0.3468054533004761):
							if(car_velocity <= 0.008963249158114195):
								return True
				else:
					return True
		else:
			if(car_velocity <= 0.01517109153792262):
				if(car_position > -0.31513597071170807):
					return True
	return False

def weShould_nothing(car_position, car_velocity):

	return False

def weShould_accelerate_right(car_position, car_velocity):
	if(car_velocity <= -0.0007429399411194026):
		if(car_position <= -0.9177583456039429):
			if(car_velocity <= -0.023546687327325344):
				if(car_position <= -0.9492785632610321):
					return True
			else:
				return True
		else:
			if(car_position <= -0.8889897763729095):
				if(car_velocity > -0.016514434944838285):
					return True
			else:
				if(car_position <= -0.879206657409668):
					if(car_position > -0.8803532421588898):
						return True
	else:
		if(car_velocity <= 0.011293863877654076):
			if(car_position <= -0.36911800503730774):
				if(car_position <= -0.3872663378715515):
					if(car_velocity <= 0.0001295892579946667):
						if(car_position <= -0.41892318427562714):
							return True
					else:
						return True
				else:
					if(car_velocity > 0.0038730697706341743):
						return True
			else:
				if(car_position <= -0.32232697308063507):
					if(car_velocity > 0.005594694288447499):
						if(car_position <= -0.3468054533004761):
							return True
						else:
							if(car_velocity > 0.008963249158114195):
								return True
		else:
			if(car_velocity <= 0.01517109153792262):
				if(car_position <= -0.31513597071170807):
					return True
			else:
				return True
	return False

