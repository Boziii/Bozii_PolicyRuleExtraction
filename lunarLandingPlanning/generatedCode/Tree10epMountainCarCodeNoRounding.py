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
	if(car_velocity <= -0.00016046120435930789):
		if(car_position <= -0.9124211668968201):
			if(car_velocity <= -0.023629012517631054):
				if(car_position > -0.9544557332992554):
					return True
			else:
				if(car_velocity <= -0.02059745602309704):
					if(car_position > -0.9437641501426697):
						return True
		else:
			if(car_position <= -0.8937625586986542):
				if(car_velocity <= -0.017688910476863384):
					return True
			else:
				return True
	else:
		if(car_velocity <= 0.011687043122947216):
			if(car_position <= -0.34210288524627686):
				if(car_position > -0.39060287177562714):
					if(car_velocity <= 0.003789988812059164):
						return True
					else:
						if(car_velocity <= 0.005817488534376025):
							if(car_position > -0.3703962415456772):
								return True
			else:
				if(car_velocity <= 0.009335705079138279):
					return True
				else:
					if(car_position > -0.32073603570461273):
						return True
		else:
			if(car_velocity <= 0.015482913237065077):
				if(car_position > -0.318467453122139):
					return True
	return False

def weShould_nothing(car_position, car_velocity):

	return False

def weShould_accelerate_right(car_position, car_velocity):
	if(car_velocity <= -0.00016046120435930789):
		if(car_position <= -0.9124211668968201):
			if(car_velocity <= -0.023629012517631054):
				if(car_position <= -0.9544557332992554):
					return True
			else:
				if(car_velocity <= -0.02059745602309704):
					if(car_position <= -0.9437641501426697):
						return True
				else:
					return True
		else:
			if(car_position <= -0.8937625586986542):
				if(car_velocity > -0.017688910476863384):
					return True
	else:
		if(car_velocity <= 0.011687043122947216):
			if(car_position <= -0.34210288524627686):
				if(car_position <= -0.39060287177562714):
					return True
				else:
					if(car_velocity > 0.003789988812059164):
						if(car_velocity <= 0.005817488534376025):
							if(car_position <= -0.3703962415456772):
								return True
						else:
							return True
			else:
				if(car_velocity > 0.009335705079138279):
					if(car_position <= -0.32073603570461273):
						return True
		else:
			if(car_velocity <= 0.015482913237065077):
				if(car_position <= -0.318467453122139):
					return True
			else:
				return True
	return False

