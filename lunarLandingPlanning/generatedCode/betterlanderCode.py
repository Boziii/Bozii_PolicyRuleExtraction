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
	if(lander_y <= 0.004):
		if(angle_velocity <= 0.393):
			if(y_velocity <= -0.176):
				if(right_leg_contact == True):
					return True
			else:
				return True
	else:
		if(y_velocity > -0.241):
			if(lander_y > 0.372):
				if(y_velocity > -0.143):
					if(x_velocity <= 0.262):
						if(x_velocity <= -0.161):
							if(angle <= -0.115):
								return True
						else:
							if(angle <= 0.073):
								if(lander_y > 1.409):
									return True
	return False

def weShould_left_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(lander_y > 0.004):
		if(y_velocity <= -0.241):
			if(angle_velocity <= -0.024):
				if(angle <= 0.009):
					if(x_velocity <= -0.057):
						if(angle_velocity <= -0.06):
							if(lander_y <= 1.367):
								if(y_velocity <= -0.272):
									if(y_velocity > -0.444):
										if(lander_x <= -0.013):
											return True
										else:
											if(y_velocity > -0.322):
												return True
								else:
									return True
							else:
								return True
						else:
							if(angle <= -0.034):
								if(y_velocity > -0.268):
									return True
					else:
						if(lander_y <= 0.471):
							if(angle_velocity <= -0.073):
								return True
						else:
							return True
				else:
					if(y_velocity > -0.294):
						if(angle <= 0.105):
							if(lander_y > 0.901):
								if(x_velocity <= 0.017):
									if(angle_velocity <= -0.052):
										if(angle <= 0.047):
											return True
									else:
										if(y_velocity > -0.279):
											if(angle <= 0.026):
												return True
								else:
									return True
			else:
				if(y_velocity <= -0.265):
					if(x_velocity > 0.571):
						return True
				else:
					if(lander_y <= 0.66):
						if(x_velocity > -0.112):
							if(y_velocity > -0.256):
								if(angle_velocity <= 0.008):
									if(x_velocity > -0.073):
										if(angle <= -0.03):
											if(lander_y > 0.193):
												return True
					else:
						if(x_velocity <= 0.063):
							if(lander_y <= 0.801):
								if(angle > -0.003):
									if(angle_velocity <= 0.009):
										return True
		else:
			if(lander_y <= 0.372):
				if(y_velocity <= -0.187):
					if(x_velocity <= -0.044):
						if(y_velocity <= -0.226):
							if(x_velocity > -0.09):
								if(angle_velocity <= -0.01):
									return True
					else:
						if(angle_velocity <= -0.001):
							if(angle <= -0.018):
								return True
							else:
								if(y_velocity > -0.211):
									if(angle <= 0.033):
										if(lander_y > 0.028):
											return True
									else:
										if(angle_velocity <= -0.05):
											return True
						else:
							if(y_velocity <= -0.214):
								if(angle <= -0.046):
									return True
				else:
					if(angle_velocity <= -0.007):
						return True
			else:
				if(y_velocity <= -0.143):
					if(angle_velocity <= 0.002):
						if(angle <= 0.128):
							if(y_velocity <= -0.236):
								return True
							else:
								if(angle_velocity <= -0.029):
									if(lander_x <= -0.045):
										return True
						else:
							if(y_velocity <= -0.196):
								if(x_velocity <= 0.146):
									if(angle_velocity <= -0.083):
										if(angle <= 0.224):
											return True
					else:
						if(x_velocity <= 0.239):
							if(y_velocity <= -0.228):
								if(x_velocity > -0.022):
									if(lander_y <= 0.703):
										if(angle <= -0.015):
											return True
				else:
					if(x_velocity <= 0.262):
						if(x_velocity > -0.161):
							if(angle <= 0.073):
								if(lander_y <= 1.409):
									return True
					else:
						return True
	return False

def weShould_main_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(lander_y <= 0.004):
		if(angle_velocity <= 0.393):
			if(y_velocity <= -0.176):
				if(right_leg_contact != True):
					return True
	else:
		if(y_velocity <= -0.241):
			if(angle_velocity <= -0.024):
				if(angle <= 0.009):
					if(x_velocity <= -0.057):
						if(angle_velocity <= -0.06):
							if(lander_y <= 1.367):
								if(y_velocity <= -0.272):
									if(y_velocity <= -0.444):
										return True
									else:
										if(lander_x > -0.013):
											if(y_velocity <= -0.322):
												return True
						else:
							if(angle <= -0.034):
								if(y_velocity <= -0.268):
									return True
							else:
								return True
					else:
						if(lander_y <= 0.471):
							if(angle_velocity > -0.073):
								return True
				else:
					if(y_velocity <= -0.294):
						return True
					else:
						if(angle <= 0.105):
							if(lander_y <= 0.901):
								if(y_velocity <= -0.264):
									return True
								else:
									return True
							else:
								if(x_velocity <= 0.017):
									if(angle_velocity <= -0.052):
										if(angle > 0.047):
											return True
									else:
										if(y_velocity <= -0.279):
											return True
						else:
							return True
			else:
				if(y_velocity <= -0.265):
					if(x_velocity <= 0.571):
						if(angle <= -0.075):
							if(y_velocity <= -0.288):
								if(angle_velocity <= 0.076):
									if(angle_velocity <= 0.053):
										if(lander_x <= -0.098):
											return True
										else:
											if(y_velocity <= -0.357):
												return True
											else:
												if(lander_y <= 1.169):
													return True
								else:
									return True
						else:
							if(lander_y <= 1.361):
								if(y_velocity <= -0.276):
									return True
								else:
									if(lander_y <= 0.742):
										return True
									else:
										if(lander_x > 0.015):
											return True
							else:
								return True
				else:
					if(lander_y <= 0.66):
						if(x_velocity > -0.112):
							if(y_velocity <= -0.256):
								return True
							else:
								if(angle_velocity <= 0.008):
									if(x_velocity <= -0.073):
										if(lander_y <= 0.333):
											return True
									else:
										if(angle <= -0.03):
											if(lander_y <= 0.193):
												return True
										else:
											return True
								else:
									return True
					else:
						if(x_velocity <= 0.063):
							if(lander_y <= 0.801):
								if(angle > -0.003):
									if(angle_velocity > 0.009):
										return True
							else:
								if(angle > 0.08):
									return True
						else:
							return True
		else:
			if(lander_y <= 0.372):
				if(y_velocity <= -0.187):
					if(x_velocity <= -0.044):
						if(y_velocity <= -0.226):
							if(x_velocity > -0.09):
								if(angle_velocity > -0.01):
									return True
					else:
						if(angle_velocity <= -0.001):
							if(angle > -0.018):
								if(y_velocity <= -0.211):
									return True
								else:
									if(angle <= 0.033):
										if(lander_y <= 0.028):
											return True
									else:
										if(angle_velocity > -0.05):
											return True
						else:
							if(y_velocity <= -0.214):
								if(angle > -0.046):
									return True
							else:
								if(angle <= 0.02):
									if(x_velocity > -0.003):
										if(lander_x > -0.11):
											return True
								else:
									return True
				else:
					if(angle_velocity > -0.007):
						if(y_velocity <= -0.176):
							if(angle > 0.044):
								return True
			else:
				if(y_velocity <= -0.143):
					if(angle_velocity <= 0.002):
						if(angle <= 0.128):
							if(y_velocity > -0.236):
								if(angle_velocity > -0.029):
									if(x_velocity > -0.014):
										if(y_velocity <= -0.222):
											return True
						else:
							if(y_velocity <= -0.196):
								if(x_velocity > 0.146):
									return True
					else:
						if(x_velocity <= 0.239):
							if(y_velocity <= -0.228):
								if(x_velocity > -0.022):
									if(lander_y <= 0.703):
										if(angle > -0.015):
											return True
						else:
							if(y_velocity <= -0.213):
								return True
							else:
								if(angle_velocity <= 0.098):
									return True
	return False

def weShould_right_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(lander_y <= 0.004):
		if(angle_velocity > 0.393):
			return True
	else:
		if(y_velocity <= -0.241):
			if(angle_velocity <= -0.024):
				if(angle > 0.009):
					if(y_velocity > -0.294):
						if(angle <= 0.105):
							if(lander_y > 0.901):
								if(x_velocity <= 0.017):
									if(angle_velocity > -0.052):
										if(y_velocity > -0.279):
											if(angle > 0.026):
												return True
			else:
				if(y_velocity <= -0.265):
					if(x_velocity <= 0.571):
						if(angle <= -0.075):
							if(y_velocity <= -0.288):
								if(angle_velocity <= 0.076):
									if(angle_velocity <= 0.053):
										if(lander_x > -0.098):
											if(y_velocity > -0.357):
												if(lander_y > 1.169):
													return True
									else:
										return True
							else:
								return True
						else:
							if(lander_y <= 1.361):
								if(y_velocity > -0.276):
									if(lander_y > 0.742):
										if(lander_x <= 0.015):
											return True
				else:
					if(lander_y <= 0.66):
						if(x_velocity <= -0.112):
							return True
						else:
							if(y_velocity > -0.256):
								if(angle_velocity <= 0.008):
									if(x_velocity <= -0.073):
										if(lander_y > 0.333):
											return True
					else:
						if(x_velocity <= 0.063):
							if(lander_y <= 0.801):
								if(angle <= -0.003):
									return True
							else:
								if(angle <= 0.08):
									return True
		else:
			if(lander_y <= 0.372):
				if(y_velocity <= -0.187):
					if(x_velocity <= -0.044):
						if(y_velocity <= -0.226):
							if(x_velocity <= -0.09):
								return True
						else:
							return True
					else:
						if(angle_velocity > -0.001):
							if(y_velocity > -0.214):
								if(angle <= 0.02):
									if(x_velocity <= -0.003):
										return True
									else:
										if(lander_x <= -0.11):
											return True
				else:
					if(angle_velocity > -0.007):
						if(y_velocity <= -0.176):
							if(angle <= 0.044):
								return True
						else:
							return True
			else:
				if(y_velocity <= -0.143):
					if(angle_velocity <= 0.002):
						if(angle <= 0.128):
							if(y_velocity > -0.236):
								if(angle_velocity <= -0.029):
									if(lander_x > -0.045):
										return True
								else:
									if(x_velocity <= -0.014):
										return True
									else:
										if(y_velocity > -0.222):
											return True
						else:
							if(y_velocity <= -0.196):
								if(x_velocity <= 0.146):
									if(angle_velocity <= -0.083):
										if(angle > 0.224):
											return True
									else:
										return True
							else:
								return True
					else:
						if(x_velocity <= 0.239):
							if(y_velocity <= -0.228):
								if(x_velocity <= -0.022):
									return True
								else:
									if(lander_y > 0.703):
										return True
							else:
								return True
						else:
							if(y_velocity > -0.213):
								if(angle_velocity > 0.098):
									return True
				else:
					if(x_velocity <= 0.262):
						if(x_velocity <= -0.161):
							if(angle > -0.115):
								return True
						else:
							if(angle > 0.073):
								return True
	return False

