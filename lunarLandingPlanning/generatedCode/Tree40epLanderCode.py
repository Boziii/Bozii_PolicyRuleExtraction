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
	if(y_velocity <= -0.137):
		if(y_velocity <= -0.22):
			if(angle_velocity <= -0.03):
				if(angle <= 0.195):
					if(lander_y <= 1.341):
						if(y_velocity > -0.271):
							if(lander_y <= 0.289):
								if(angle_velocity <= -0.062):
									if(y_velocity > -0.245):
										if(angle <= 0.017):
											if(lander_y <= 0.015):
												return True
		else:
			if(angle_velocity <= -0.011):
				if(right_leg_contact != True):
					if(angle <= 0.062):
						if(angle_velocity <= -0.036):
							if(x_velocity <= -0.049):
								if(angle <= -0.018):
									if(x_velocity <= -0.312):
										return True
									else:
										if(x_velocity <= -0.051):
											if(x_velocity <= -0.097):
												if(angle_velocity <= -0.061):
													if(x_velocity <= -0.223):
														if(angle_velocity <= -0.163):
															if(lander_x > -0.055):
																if(angle_velocity > -0.213):
																	return True
				else:
					if(x_velocity <= 0.091):
						if(lander_y <= 0.015):
							return True
						else:
							if(angle_velocity > -0.428):
								return True
					else:
						if(angle_velocity > -0.514):
							if(angle > -0.098):
								return True
			else:
				if(lander_y <= 0.246):
					if(y_velocity <= -0.186):
						if(x_velocity <= 0.019):
							if(y_velocity <= -0.204):
								if(x_velocity > -0.027):
									if(lander_y <= 0.187):
										if(lander_x > -0.131):
											if(lander_y <= 0.002):
												return True
							else:
								if(angle_velocity > -0.005):
									if(lander_y <= 0.004):
										if(y_velocity <= -0.199):
											return True
						else:
							if(angle > 0.011):
								if(right_leg_contact == True):
									if(x_velocity > 0.044):
										return True
					else:
						if(x_velocity <= 0.079):
							if(left_leg_contact == True):
								if(angle_velocity <= 0.453):
									if(angle > -0.007):
										if(angle <= 0.095):
											return True
	else:
		if(y_velocity <= -0.0):
			if(angle <= 0.102):
				if(lander_y <= 0.046):
					if(angle_velocity <= 0.481):
						if(right_leg_contact != True):
							if(angle_velocity <= 0.145):
								if(y_velocity <= -0.0):
									if(lander_x <= -0.169):
										if(lander_x > -0.17):
											if(y_velocity > -0.001):
												return True
									else:
										if(x_velocity <= 0.113):
											if(lander_x <= -0.137):
												if(angle_velocity <= 0.024):
													if(angle_velocity <= 0.002):
														return True
													else:
														if(angle <= 0.098):
															if(angle_velocity <= 0.003):
																return True
															else:
																if(angle <= 0.096):
																	if(y_velocity <= -0.001):
																		if(lander_x > -0.165):
																			if(y_velocity <= -0.002):
																				if(angle <= 0.089):
																					if(y_velocity <= -0.003):
																						if(lander_y > -0.011):
																							if(y_velocity <= -0.003):
																								if(angle <= 0.077):
																									if(x_velocity <= -0.038):
																										if(lander_x > -0.152):
																											if(y_velocity <= -0.005):
																												if(lander_y > -0.008):
																													if(lander_y <= -0.007):
																														if(y_velocity > -0.006):
																															return True
																													else:
																														return True
																											else:
																												return True
																									else:
																										return True
																							else:
																								return True
																					else:
																						if(lander_y <= -0.012):
																							if(x_velocity > -0.021):
																								return True
																						else:
																							return True
																			else:
																				return True
																	else:
																		return True
											else:
												return True
								else:
									return True
						else:
							return True
				else:
					if(x_velocity <= 0.224):
						if(angle <= 0.001):
							if(y_velocity <= -0.1):
								if(angle <= -0.001):
									if(lander_y > 1.451):
										if(lander_x > -0.061):
											return True
							else:
								if(x_velocity <= 0.047):
									return True
								else:
									if(angle > -0.001):
										return True
						else:
							if(lander_x > 0.001):
								if(angle_velocity > 0.166):
									if(y_velocity > -0.032):
										return True
			else:
				if(x_velocity <= -0.005):
					if(lander_y <= -0.041):
						if(lander_y > -0.043):
							if(x_velocity <= -0.006):
								if(lander_x > -0.229):
									if(angle_velocity <= 0.005):
										return True
									else:
										if(lander_y > -0.042):
											if(y_velocity > -0.003):
												if(lander_y <= -0.042):
													if(angle_velocity <= 0.007):
														if(x_velocity <= -0.014):
															return True
														else:
															if(lander_y <= -0.042):
																return True
												else:
													return True
							else:
								if(lander_x > -0.292):
									return True
					else:
						if(angle_velocity <= 0.032):
							if(lander_y <= -0.03):
								if(lander_x <= -0.247):
									if(angle_velocity <= 0.003):
										return True
									else:
										if(lander_y <= -0.04):
											if(lander_x > -0.29):
												if(angle_velocity <= 0.003):
													if(lander_x <= -0.29):
														return True
													else:
														if(lander_x > -0.29):
															return True
										else:
											if(y_velocity <= -0.001):
												if(lander_y > -0.04):
													if(y_velocity > -0.009):
														if(y_velocity <= -0.002):
															if(angle <= 0.275):
																if(x_velocity <= -0.024):
																	if(angle <= 0.272):
																		if(lander_y <= -0.032):
																			if(angle_velocity <= 0.025):
																				if(lander_y <= -0.033):
																					if(x_velocity > -0.068):
																						if(angle_velocity <= 0.009):
																							return True
																						else:
																							if(lander_y > -0.038):
																								if(x_velocity <= -0.034):
																									if(lander_x > -0.276):
																										if(y_velocity <= -0.004):
																											if(lander_x > -0.272):
																												if(y_velocity <= -0.005):
																													if(lander_x > -0.268):
																														if(angle_velocity <= 0.019):
																															return True
																														else:
																															if(lander_y > -0.034):
																																return True
																												else:
																													return True
																										else:
																											return True
																								else:
																									return True
																				else:
																					return True
																		else:
																			return True
																else:
																	return True
														else:
															if(lander_x <= -0.286):
																if(x_velocity > -0.015):
																	return True
															else:
																return True
											else:
												return True
								else:
									if(y_velocity <= -0.004):
										if(lander_x > -0.222):
											if(x_velocity <= -0.032):
												if(angle <= 0.271):
													if(angle_velocity <= 0.021):
														return True
													else:
														if(y_velocity <= -0.01):
															return True
														else:
															if(lander_x > -0.216):
																if(x_velocity <= -0.047):
																	if(x_velocity > -0.056):
																		if(lander_x > -0.214):
																			if(lander_x <= -0.213):
																				if(lander_y <= -0.037):
																					return True
																			else:
																				return True
																else:
																	return True
											else:
												return True
									else:
										return True
							else:
								return True
						else:
							if(angle <= 0.125):
								return True
							else:
								if(y_velocity <= -0.017):
									if(angle <= 0.168):
										if(angle <= 0.164):
											if(lander_y > -0.021):
												if(lander_y <= -0.02):
													return True
										else:
											return True
								else:
									if(lander_x <= -0.197):
										if(lander_x > -0.205):
											if(x_velocity <= -0.078):
												if(lander_y > -0.032):
													if(lander_y <= -0.031):
														return True
											else:
												return True
									else:
										return True
				else:
					if(x_velocity <= -0.001):
						if(x_velocity <= -0.002):
							if(lander_y <= -0.041):
								if(lander_x > -0.231):
									if(y_velocity <= -0.001):
										if(angle_velocity > 0.002):
											return True
									else:
										return True
							else:
								if(right_leg_contact != True):
									if(lander_y > -0.014):
										if(angle_velocity <= 0.001):
											return True
								else:
									if(lander_x <= -0.292):
										if(angle_velocity <= 0.001):
											return True
									else:
										if(x_velocity > -0.005):
											return True
						else:
							if(angle <= 0.102):
								return True
							else:
								if(x_velocity <= -0.002):
									if(angle_velocity <= 0.001):
										if(x_velocity > -0.002):
											if(x_velocity <= -0.002):
												return True
									else:
										return True
								else:
									if(angle_velocity <= 0.0):
										if(angle <= 0.103):
											return True
									else:
										if(lander_x > -0.293):
											return True
					else:
						if(angle_velocity <= 0.182):
							if(angle <= 0.291):
								if(lander_y <= -0.025):
									return True
								else:
									if(lander_x > -0.172):
										return True
							else:
								if(lander_x > -0.232):
									return True
						else:
							if(lander_y <= 1.442):
								if(angle_velocity <= 0.236):
									if(x_velocity > 0.039):
										return True
		else:
			if(x_velocity <= 0.187):
				if(lander_y <= -0.044):
					if(angle_velocity <= -0.0):
						if(angle <= 0.305):
							return True
				else:
					if(x_velocity > -0.296):
						if(x_velocity <= -0.136):
							if(angle_velocity <= -0.191):
								if(angle_velocity <= -0.232):
									if(y_velocity <= 0.036):
										return True
								else:
									return True
						else:
							if(angle <= 0.305):
								if(lander_y <= 1.455):
									if(x_velocity <= 0.178):
										if(y_velocity <= -0.0):
											if(y_velocity <= -0.0):
												if(angle <= 0.103):
													return True
												else:
													if(x_velocity > -0.001):
														return True
										else:
											return True
									else:
										if(lander_y <= 0.706):
											return True
								else:
									if(lander_y > 1.457):
										if(y_velocity > 0.011):
											return True
							else:
								if(angle_velocity <= -0.0):
									return True
			else:
				if(x_velocity <= 0.444):
					if(lander_y <= 1.477):
						if(x_velocity > 0.23):
							if(x_velocity <= 0.271):
								if(angle_velocity <= 0.093):
									if(angle <= -0.0):
										if(x_velocity <= 0.262):
											if(y_velocity <= 0.262):
												return True
										else:
											return True
								else:
									return True
					else:
						if(angle <= 0.142):
							return True
	return False

def weShould_left_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.137):
		if(y_velocity <= -0.22):
			if(angle_velocity <= -0.03):
				if(angle <= 0.195):
					if(lander_y <= 1.341):
						if(y_velocity <= -0.271):
							if(angle <= 0.061):
								if(y_velocity <= -0.474):
									if(x_velocity > -0.594):
										if(angle <= -0.289):
											if(y_velocity <= -0.501):
												if(y_velocity > -0.541):
													if(lander_y <= 1.073):
														if(angle_velocity <= -0.05):
															if(lander_y <= 1.036):
																return True
															else:
																if(angle_velocity <= -0.195):
																	return True
											else:
												if(y_velocity <= -0.478):
													return True
										else:
											if(angle <= -0.031):
												if(lander_x <= -0.15):
													if(lander_x <= -0.153):
														if(angle_velocity <= -0.27):
															if(x_velocity > -0.526):
																return True
													else:
														return True
								else:
									if(angle_velocity <= -0.087):
										if(y_velocity <= -0.343):
											if(angle <= -0.183):
												if(x_velocity > -0.533):
													if(lander_y <= 1.077):
														if(x_velocity <= -0.406):
															if(y_velocity <= -0.439):
																if(lander_x <= -0.16):
																	if(y_velocity <= -0.461):
																		return True
															else:
																return True
														else:
															if(angle_velocity <= -0.106):
																return True
													else:
														return True
											else:
												if(x_velocity > -0.49):
													if(angle_velocity <= -0.33):
														if(angle <= 0.018):
															if(x_velocity > -0.486):
																if(angle_velocity <= -0.334):
																	if(lander_y <= 0.96):
																		if(angle_velocity > -0.392):
																			return True
																	else:
																		return True
																else:
																	if(angle_velocity > -0.333):
																		return True
														else:
															if(lander_x > 0.235):
																if(y_velocity > -0.373):
																	return True
													else:
														if(y_velocity <= -0.422):
															if(lander_y <= 0.898):
																if(angle_velocity <= -0.229):
																	return True
															else:
																if(x_velocity > -0.305):
																	if(lander_y <= 1.272):
																		if(angle_velocity <= -0.12):
																			return True
														else:
															if(angle <= -0.093):
																if(lander_y > 0.896):
																	if(x_velocity > -0.414):
																		if(angle <= -0.113):
																			if(x_velocity <= -0.38):
																				if(lander_x > 0.189):
																					return True
																			else:
																				return True
																		else:
																			if(angle_velocity <= -0.126):
																				if(lander_x > -0.053):
																					if(lander_y <= 1.308):
																						return True
																					else:
																						if(y_velocity > -0.376):
																							return True
															else:
																if(x_velocity <= -0.149):
																	if(angle_velocity <= -0.253):
																		if(y_velocity <= -0.395):
																			if(lander_x <= -0.051):
																				return True
																		else:
																			if(angle <= 0.014):
																				return True
																	else:
																		if(x_velocity <= -0.253):
																			if(y_velocity > -0.371):
																				if(lander_x <= 0.195):
																					return True
																				else:
																					if(y_velocity > -0.345):
																						return True
																		else:
																			if(lander_y > 1.323):
																				if(lander_y <= 1.325):
																					return True
																else:
																	return True
										else:
											if(y_velocity <= -0.289):
												if(angle <= 0.006):
													if(lander_y <= 1.317):
														if(lander_y <= 0.847):
															if(lander_y <= 0.793):
																return True
															else:
																if(x_velocity <= -0.217):
																	if(x_velocity <= -0.229):
																		if(y_velocity <= -0.316):
																			return True
																else:
																	return True
														else:
															if(angle_velocity <= -0.095):
																return True
															else:
																if(angle_velocity > -0.093):
																	if(lander_x <= 0.199):
																		return True
												else:
													if(angle_velocity <= -0.119):
														if(angle <= 0.05):
															if(lander_y > 0.791):
																return True
														else:
															if(lander_y > 1.065):
																return True
													else:
														if(lander_x <= 0.042):
															return True
														else:
															if(y_velocity > -0.293):
																if(lander_y > 1.026):
																	return True
											else:
												if(angle_velocity <= -0.093):
													return True
									else:
										if(y_velocity <= -0.295):
											if(angle <= -0.072):
												if(y_velocity <= -0.349):
													if(y_velocity <= -0.442):
														if(y_velocity <= -0.47):
															return True
													else:
														if(angle <= -0.226):
															return True
														else:
															if(x_velocity <= -0.158):
																if(angle <= -0.121):
																	if(y_velocity <= -0.403):
																		if(y_velocity <= -0.426):
																			if(y_velocity > -0.431):
																				return True
																	else:
																		if(y_velocity <= -0.384):
																			if(y_velocity <= -0.397):
																				if(y_velocity <= -0.402):
																					return True
																			else:
																				return True
																		else:
																			if(angle <= -0.159):
																				if(angle > -0.199):
																					if(angle <= -0.165):
																						return True
																					else:
																						if(angle > -0.162):
																							return True
															else:
																if(y_velocity > -0.369):
																	return True
												else:
													if(lander_x <= 0.147):
														return True
													else:
														if(x_velocity <= -0.206):
															if(lander_x > 0.154):
																if(angle_velocity <= -0.044):
																	return True
											else:
												if(lander_x <= -0.007):
													if(y_velocity > -0.321):
														if(lander_y > 0.86):
															if(angle <= -0.006):
																if(x_velocity <= -0.085):
																	if(angle_velocity <= -0.059):
																		return True
																else:
																	return True
															else:
																if(x_velocity <= -0.043):
																	if(lander_y > 1.166):
																		return True
												else:
													if(lander_y <= 1.295):
														if(angle <= -0.036):
															if(y_velocity <= -0.31):
																if(angle_velocity <= -0.076):
																	if(angle_velocity > -0.086):
																		return True
															else:
																if(x_velocity > -0.18):
																	if(lander_y <= 0.74):
																		if(angle_velocity <= -0.064):
																			return True
																	else:
																		return True
														else:
															if(x_velocity > -0.151):
																if(lander_y <= 0.854):
																	if(lander_y > 0.842):
																		return True
																else:
																	if(y_velocity > -0.298):
																		if(y_velocity <= -0.298):
																			return True
													else:
														if(y_velocity > -0.32):
															return True
										else:
											if(lander_y <= 0.656):
												if(angle <= -0.024):
													if(lander_y > 0.439):
														if(lander_y <= 0.639):
															return True
												else:
													if(angle_velocity <= -0.064):
														if(lander_x <= -0.006):
															return True
											else:
												if(angle <= 0.005):
													if(x_velocity <= -0.102):
														if(lander_y <= 0.895):
															if(lander_x > 0.045):
																return True
													else:
														if(angle_velocity <= -0.038):
															if(y_velocity <= -0.292):
																if(angle_velocity <= -0.06):
																	return True
															else:
																if(angle <= 0.003):
																	if(lander_x <= -0.034):
																		if(angle <= -0.011):
																			return True
																	else:
																		return True
																else:
																	if(lander_y > 0.787):
																		return True
														else:
															if(lander_y > 0.752):
																if(angle <= -0.012):
																	return True
																else:
																	if(x_velocity <= -0.03):
																		if(lander_y <= 0.839):
																			if(y_velocity <= -0.284):
																				return True
																	else:
																		if(x_velocity <= -0.024):
																			return True
												else:
													if(lander_y <= 0.925):
														if(x_velocity <= 0.017):
															if(x_velocity > -0.003):
																if(lander_x > -0.022):
																	return True
														else:
															return True
													else:
														if(x_velocity <= -0.082):
															if(y_velocity <= -0.292):
																return True
														else:
															if(lander_y <= 1.099):
																if(angle_velocity <= -0.047):
																	if(x_velocity <= -0.034):
																		if(angle_velocity <= -0.054):
																			if(y_velocity > -0.285):
																				if(angle <= 0.025):
																					return True
																				else:
																					if(angle_velocity <= -0.075):
																						if(lander_y > 1.052):
																							return True
																		else:
																			return True
																	else:
																		return True
																else:
																	if(lander_x > 0.126):
																		return True
															else:
																return True
							else:
								if(angle_velocity <= -0.093):
									if(angle_velocity <= -0.424):
										if(y_velocity > -0.339):
											if(lander_x <= 0.254):
												return True
									else:
										if(angle <= 0.114):
											if(lander_y <= 1.162):
												if(angle <= 0.079):
													if(angle <= 0.078):
														if(lander_x <= 0.127):
															if(y_velocity <= -0.281):
																return True
														else:
															if(x_velocity <= -0.23):
																if(y_velocity > -0.344):
																	return True
													else:
														return True
												else:
													if(angle > 0.108):
														return True
											else:
												if(y_velocity > -0.297):
													return True
										else:
											if(lander_x > 0.242):
												if(x_velocity > -0.078):
													return True
								else:
									if(x_velocity > -0.081):
										if(lander_x <= 0.049):
											if(lander_x > 0.048):
												return True
						else:
							if(lander_y <= 0.289):
								if(angle_velocity <= -0.062):
									if(y_velocity <= -0.245):
										if(lander_y > 0.146):
											if(x_velocity <= -0.029):
												return True
									else:
										if(angle <= 0.017):
											if(lander_y > 0.015):
												if(y_velocity <= -0.221):
													return True
								else:
									if(y_velocity <= -0.229):
										if(y_velocity > -0.249):
											if(angle <= -0.051):
												if(lander_x <= -0.156):
													if(lander_y <= 0.042):
														return True
												else:
													if(angle <= -0.054):
														return True
											else:
												if(lander_y <= 0.215):
													if(angle <= -0.019):
														if(x_velocity <= -0.041):
															if(lander_x > 0.097):
																if(angle <= -0.023):
																	if(lander_y > 0.115):
																		return True
														else:
															if(y_velocity <= -0.234):
																if(angle_velocity <= -0.051):
																	return True
															else:
																return True
												else:
													if(angle <= 0.008):
														if(angle_velocity <= -0.037):
															if(y_velocity <= -0.238):
																return True
															else:
																if(y_velocity > -0.235):
																	return True
														else:
															if(x_velocity > -0.008):
																return True
									else:
										if(angle <= -0.019):
											if(lander_x > -0.192):
												if(lander_y <= 0.225):
													if(lander_y <= 0.033):
														if(x_velocity <= -0.096):
															return True
													else:
														return True
										else:
											if(angle <= 0.008):
												if(lander_y <= 0.126):
													if(angle_velocity > -0.037):
														if(angle <= -0.015):
															return True
												else:
													if(x_velocity <= -0.016):
														if(lander_x > 0.045):
															return True
													else:
														return True
							else:
								if(angle <= -0.004):
									if(angle_velocity <= -0.041):
										if(y_velocity <= -0.258):
											if(y_velocity <= -0.26):
												if(x_velocity <= -0.078):
													if(lander_y <= 0.577):
														if(angle <= -0.036):
															return True
													else:
														return True
												else:
													if(lander_y <= 0.704):
														return True
											else:
												if(x_velocity <= -0.055):
													return True
										else:
											if(y_velocity <= -0.225):
												return True
											else:
												if(lander_y > 0.347):
													return True
									else:
										if(x_velocity > -0.095):
											if(lander_y <= 0.428):
												if(y_velocity <= -0.235):
													if(angle <= -0.011):
														if(x_velocity <= -0.015):
															if(x_velocity <= -0.085):
																return True
															else:
																if(y_velocity <= -0.238):
																	if(lander_y <= 0.345):
																		return True
																	else:
																		if(lander_x > 0.113):
																			return True
														else:
															return True
												else:
													return True
											else:
												if(angle_velocity > -0.041):
													if(lander_x > -0.263):
														if(y_velocity <= -0.265):
															if(y_velocity <= -0.266):
																return True
														else:
															return True
								else:
									if(lander_y <= 0.552):
										if(y_velocity <= -0.249):
											if(angle <= 0.0):
												if(x_velocity <= -0.027):
													return True
										else:
											if(angle_velocity <= -0.057):
												if(lander_x > -0.204):
													if(x_velocity <= -0.033):
														if(angle_velocity <= -0.092):
															return True
													else:
														if(lander_x <= -0.107):
															if(x_velocity > -0.003):
																return True
														else:
															return True
											else:
												if(y_velocity <= -0.233):
													if(angle <= 0.003):
														if(lander_y <= 0.461):
															return True
													else:
														if(angle_velocity <= -0.038):
															if(angle_velocity <= -0.039):
																if(x_velocity <= 0.07):
																	if(y_velocity > -0.239):
																		if(x_velocity <= 0.034):
																			if(y_velocity <= -0.238):
																				return True
																		else:
																			return True
																else:
																	return True
															else:
																return True
												else:
													if(x_velocity > -0.025):
														if(x_velocity <= 0.034):
															if(y_velocity <= -0.228):
																if(y_velocity > -0.232):
																	return True
														else:
															if(lander_x > -0.2):
																return True
									else:
										if(x_velocity <= -0.043):
											if(lander_x <= 0.126):
												if(lander_y > 0.699):
													if(angle <= 0.013):
														if(angle_velocity <= -0.054):
															if(x_velocity > -0.087):
																return True
											else:
												if(y_velocity <= -0.247):
													if(x_velocity <= -0.063):
														if(angle <= 0.174):
															if(angle_velocity <= -0.043):
																if(x_velocity > -0.249):
																	return True
												else:
													if(lander_x <= 0.13):
														return True
										else:
											if(angle <= 0.051):
												if(angle_velocity <= -0.036):
													if(x_velocity <= 0.002):
														if(angle_velocity <= -0.057):
															if(angle > -0.002):
																return True
														else:
															if(lander_y <= 0.705):
																if(angle <= 0.014):
																	if(angle_velocity <= -0.042):
																		return True
															else:
																if(lander_y <= 0.876):
																	return True
																else:
																	if(x_velocity > -0.004):
																		return True
													else:
														return True
												else:
													if(y_velocity <= -0.257):
														if(x_velocity > 0.006):
															if(x_velocity <= 0.024):
																return True
													else:
														if(lander_x <= 0.03):
															if(angle <= 0.032):
																if(x_velocity > -0.012):
																	return True
															else:
																if(angle > 0.04):
																	return True
											else:
												if(y_velocity <= -0.254):
													if(angle <= 0.104):
														if(angle_velocity <= -0.088):
															return True
														else:
															if(x_velocity > 0.003):
																if(y_velocity > -0.267):
																	if(angle <= 0.085):
																		if(x_velocity <= 0.009):
																			if(y_velocity <= -0.265):
																				return True
																		else:
																			return True
																	else:
																		if(lander_y > 1.241):
																			return True
													else:
														if(lander_x <= 0.1):
															if(angle_velocity <= -0.06):
																return True
														else:
															if(angle_velocity <= -0.12):
																if(angle <= 0.163):
																	return True
												else:
													if(angle_velocity <= -0.096):
														if(y_velocity <= -0.229):
															if(angle_velocity <= -0.138):
																return True
															else:
																if(angle <= 0.113):
																	return True
																else:
																	if(x_velocity > 0.018):
																		if(y_velocity <= -0.245):
																			if(angle <= 0.137):
																				if(lander_y > 0.98):
																					return True
																		else:
																			if(angle_velocity > -0.132):
																				return True
														else:
															if(x_velocity > 0.039):
																return True
													else:
														if(x_velocity <= 0.025):
															if(lander_y <= 0.896):
																return True
															else:
																if(lander_y > 0.925):
																	if(angle_velocity <= -0.085):
																		if(angle_velocity > -0.09):
																			return True
														else:
															if(angle <= 0.122):
																if(lander_x > -0.014):
																	if(y_velocity <= -0.253):
																		if(angle_velocity <= -0.067):
																			return True
																	else:
																		return True
															else:
																if(x_velocity > 0.084):
																	if(lander_y > 1.211):
																		if(y_velocity > -0.248):
																			return True
					else:
						if(x_velocity > -0.327):
							if(angle <= -0.004):
								if(y_velocity <= -0.351):
									if(lander_y <= 1.373):
										if(lander_x <= -0.02):
											if(lander_y <= 1.366):
												return True
											else:
												if(x_velocity <= -0.319):
													return True
									else:
										if(x_velocity <= -0.314):
											if(lander_y > 1.406):
												return True
										else:
											return True
								else:
									if(lander_y > 1.365):
										if(x_velocity <= -0.183):
											if(angle <= -0.033):
												if(angle_velocity <= -0.112):
													return True
												else:
													if(x_velocity <= -0.322):
														return True
													else:
														if(y_velocity <= -0.3):
															if(angle_velocity <= -0.064):
																return True
										else:
											return True
							else:
								if(y_velocity > -0.241):
									if(lander_x > 0.088):
										return True
				else:
					if(angle <= 0.263):
						if(lander_y > 0.785):
							if(lander_x <= 0.116):
								if(x_velocity <= 0.175):
									return True
							else:
								if(x_velocity > -0.187):
									if(y_velocity > -0.238):
										if(angle_velocity <= -0.171):
											if(y_velocity <= -0.229):
												return True
			else:
				if(lander_y <= 0.399):
					if(angle_velocity <= -0.006):
						if(y_velocity <= -0.237):
							if(angle <= -0.04):
								if(lander_y <= 0.175):
									if(y_velocity > -0.245):
										if(lander_x <= 0.025):
											if(lander_y <= 0.059):
												return True
								else:
									if(y_velocity <= -0.256):
										if(angle_velocity <= -0.018):
											if(lander_x > -0.05):
												return True
									else:
										if(x_velocity <= -0.079):
											if(angle <= -0.081):
												return True
										else:
											if(lander_y <= 0.377):
												return True
							else:
								if(lander_y <= 0.397):
									if(lander_y > 0.295):
										if(lander_y <= 0.297):
											return True
										else:
											if(lander_x > -0.033):
												if(lander_x <= -0.003):
													if(angle_velocity <= -0.014):
														return True
								else:
									return True
						else:
							if(angle <= -0.025):
								if(x_velocity <= -0.086):
									if(angle <= -0.049):
										return True
								else:
									if(angle_velocity > -0.028):
										if(x_velocity <= -0.038):
											if(lander_y <= 0.296):
												if(y_velocity <= -0.226):
													if(lander_y <= 0.027):
														if(x_velocity > -0.061):
															return True
													else:
														return True
										else:
											return True
							else:
								if(lander_y <= 0.206):
									if(x_velocity > -0.067):
										if(angle <= -0.02):
											if(lander_y > 0.081):
												return True
								else:
									if(lander_x <= -0.11):
										if(angle <= -0.011):
											if(lander_y > 0.33):
												return True
									else:
										if(angle <= 0.014):
											if(angle_velocity <= -0.008):
												if(angle <= -0.004):
													if(angle_velocity > -0.026):
														if(x_velocity > -0.063):
															return True
												else:
													if(x_velocity <= 0.003):
														if(x_velocity <= -0.027):
															return True
													else:
														if(angle_velocity <= -0.01):
															if(lander_y > 0.221):
																return True
											else:
												if(y_velocity <= -0.23):
													return True
										else:
											if(x_velocity <= 0.042):
												if(lander_y > 0.363):
													if(lander_x > 0.038):
														return True
											else:
												return True
					else:
						if(angle_velocity <= 0.107):
							if(angle <= -0.007):
								if(y_velocity <= -0.238):
									if(x_velocity > -0.137):
										if(angle <= -0.065):
											if(y_velocity > -0.262):
												if(angle_velocity <= 0.04):
													if(lander_y <= 0.308):
														if(x_velocity <= -0.058):
															if(lander_y > 0.246):
																if(lander_y <= 0.266):
																	return True
														else:
															return True
													else:
														return True
										else:
											if(y_velocity > -0.245):
												if(lander_y > 0.28):
													if(x_velocity <= -0.021):
														if(x_velocity <= -0.031):
															if(lander_y <= 0.298):
																if(angle > -0.038):
																	return True
														else:
															return True
													else:
														if(x_velocity > 0.033):
															return True
								else:
									if(lander_y <= 0.267):
										if(x_velocity > -0.063):
											if(angle_velocity <= 0.006):
												if(angle_velocity <= 0.004):
													if(x_velocity <= 0.027):
														if(angle_velocity <= -0.004):
															if(angle_velocity > -0.005):
																return True
													else:
														return True
												else:
													if(angle > -0.044):
														return True
									else:
										if(lander_x <= -0.085):
											if(x_velocity > 0.025):
												return True
										else:
											if(angle_velocity <= 0.001):
												return True
											else:
												if(x_velocity <= -0.01):
													if(y_velocity > -0.231):
														if(angle_velocity <= 0.05):
															if(angle <= -0.082):
																return True
														else:
															return True
												else:
													if(lander_x <= -0.01):
														if(x_velocity > 0.023):
															if(angle_velocity <= 0.057):
																return True
													else:
														if(angle_velocity <= 0.058):
															return True
							else:
								if(x_velocity > -0.054):
									if(y_velocity <= -0.221):
										if(y_velocity > -0.226):
											if(y_velocity <= -0.226):
												return True
				else:
					if(y_velocity <= -0.259):
						if(x_velocity > -0.468):
							if(angle <= -0.053):
								if(y_velocity <= -0.29):
									if(y_velocity <= -0.324):
										if(lander_y <= 1.061):
											if(angle <= -0.202):
												if(y_velocity <= -0.357):
													if(angle_velocity <= 0.039):
														if(y_velocity <= -0.405):
															if(lander_x <= -0.243):
																if(angle_velocity <= 0.033):
																	return True
															else:
																if(y_velocity > -0.424):
																	if(angle > -0.289):
																		if(angle <= -0.244):
																			return True
														else:
															return True
													else:
														if(y_velocity <= -0.387):
															if(angle <= -0.315):
																if(y_velocity <= -0.462):
																	if(angle_velocity <= 0.056):
																		return True
																	else:
																		if(x_velocity > -0.285):
																			if(angle_velocity <= 0.103):
																				return True
																else:
																	return True
															else:
																if(lander_y <= 1.037):
																	if(x_velocity > -0.319):
																		if(x_velocity > -0.093):
																			if(x_velocity <= -0.08):
																				return True
																else:
																	if(angle > -0.301):
																		return True
														else:
															if(angle <= -0.234):
																if(lander_x <= -0.234):
																	if(y_velocity <= -0.369):
																		if(angle_velocity <= 0.079):
																			return True
																	else:
																		return True
																else:
																	if(y_velocity <= -0.378):
																		return True
															else:
																if(lander_y > 0.983):
																	return True
												else:
													if(angle <= -0.205):
														if(angle_velocity <= 0.111):
															return True
														else:
															if(y_velocity > -0.341):
																return True
											else:
												if(y_velocity <= -0.336):
													if(x_velocity > -0.352):
														if(angle_velocity <= 0.218):
															if(lander_y > 1.0):
																if(lander_y <= 1.002):
																	return True
																else:
																	if(angle_velocity <= -0.006):
																		if(lander_x <= -0.08):
																			return True
																	else:
																		if(angle <= -0.152):
																			if(lander_x <= -0.187):
																				return True
																		else:
																			if(angle_velocity <= 0.025):
																				if(angle_velocity > 0.02):
																					return True
												else:
													if(angle <= -0.163):
														if(angle_velocity > 0.039):
															if(angle_velocity <= 0.137):
																if(lander_y > 0.705):
																	return True
													else:
														if(angle_velocity <= 0.048):
															if(lander_x <= -0.105):
																return True
															else:
																if(angle <= -0.1):
																	if(lander_y > 0.681):
																		if(angle > -0.107):
																			return True
										else:
											if(y_velocity <= -0.345):
												if(angle <= -0.145):
													if(y_velocity <= -0.399):
														if(lander_y <= 1.064):
															return True
														else:
															if(angle_velocity <= -0.018):
																if(x_velocity <= -0.299):
																	if(x_velocity <= -0.345):
																		return True
																else:
																	return True
															else:
																if(lander_y <= 1.317):
																	if(lander_x <= -0.194):
																		return True
																	else:
																		if(lander_y > 1.27):
																			if(lander_y <= 1.279):
																				if(y_velocity <= -0.407):
																					return True
																else:
																	if(angle_velocity <= 0.001):
																		return True
													else:
														if(angle <= -0.183):
															if(angle_velocity <= 0.048):
																if(lander_x <= -0.162):
																	if(lander_x <= -0.171):
																		return True
																else:
																	return True
															else:
																if(lander_y <= 1.142):
																	return True
														else:
															if(y_velocity <= -0.364):
																if(angle_velocity <= 0.005):
																	if(y_velocity > -0.382):
																		return True
																else:
																	if(y_velocity <= -0.397):
																		return True
																	else:
																		if(angle <= -0.179):
																			if(angle > -0.181):
																				return True
															else:
																if(angle_velocity <= 0.048):
																	return True
																else:
																	if(x_velocity > -0.14):
																		if(lander_y <= 1.117):
																			return True
												else:
													if(y_velocity > -0.36):
														if(y_velocity <= -0.357):
															if(y_velocity <= -0.357):
																return True
														else:
															if(lander_y <= 1.321):
																if(y_velocity <= -0.353):
																	if(lander_x <= -0.058):
																		return True
															else:
																return True
											else:
												if(angle <= -0.07):
													if(y_velocity <= -0.333):
														if(x_velocity <= -0.158):
															if(lander_y <= 1.144):
																return True
														else:
															if(lander_y <= 1.078):
																return True
															else:
																if(angle <= -0.075):
																	if(y_velocity <= -0.343):
																		if(angle > -0.134):
																			return True
																else:
																	return True
													else:
														if(angle_velocity <= -0.011):
															return True
												else:
													if(y_velocity <= -0.334):
														return True
									else:
										if(lander_y <= 0.972):
											if(angle <= -0.139):
												if(y_velocity <= -0.313):
													if(angle <= -0.167):
														if(lander_x <= -0.283):
															return True
													else:
														if(angle_velocity <= 0.052):
															return True
												else:
													if(angle_velocity <= 0.151):
														if(lander_x > -0.286):
															if(lander_y <= 0.654):
																if(y_velocity <= -0.311):
																	return True
																else:
																	if(x_velocity > -0.16):
																		if(lander_y <= 0.645):
																			return True
															else:
																return True
											else:
												if(lander_x <= 0.171):
													if(angle_velocity <= -0.005):
														if(x_velocity > -0.132):
															if(angle <= -0.073):
																return True
															else:
																if(x_velocity <= -0.124):
																	return True
													else:
														if(angle <= -0.118):
															if(angle_velocity <= 0.035):
																return True
															else:
																if(angle <= -0.121):
																	if(lander_y <= 0.506):
																		return True
																else:
																	if(y_velocity <= -0.303):
																		return True
														else:
															if(angle <= -0.054):
																if(lander_y <= 0.947):
																	if(y_velocity <= -0.303):
																		if(angle <= -0.059):
																			if(angle <= -0.111):
																				if(lander_y > 0.726):
																					return True
																		else:
																			if(angle <= -0.058):
																				return True
																	else:
																		if(y_velocity > -0.303):
																			if(angle_velocity <= 0.002):
																				if(lander_y <= 0.675):
																					return True
																			else:
																				if(x_velocity > -0.145):
																					if(lander_y <= 0.891):
																						if(angle_velocity <= 0.017):
																							if(x_velocity > -0.103):
																								return True
																						else:
																							if(angle <= -0.108):
																								if(x_velocity <= -0.106):
																									return True
																					else:
																						if(y_velocity <= -0.298):
																							return True
																else:
																	if(angle_velocity <= 0.032):
																		return True
															else:
																return True
												else:
													if(angle <= -0.112):
														return True
										else:
											if(x_velocity <= -0.075):
												if(angle_velocity <= 0.028):
													if(lander_x <= -0.082):
														if(angle <= -0.09):
															return True
													else:
														if(y_velocity > -0.312):
															if(lander_y > 1.083):
																return True
												else:
													if(angle <= -0.131):
														if(lander_x > -0.165):
															return True
													else:
														if(lander_x <= -0.123):
															if(lander_y > 1.071):
																return True
											else:
												if(y_velocity <= -0.297):
													if(x_velocity > -0.067):
														if(lander_x <= -0.155):
															if(angle_velocity > 0.104):
																return True
														else:
															if(angle_velocity <= 0.087):
																return True
								else:
									if(angle_velocity <= 0.055):
										if(lander_y <= 0.573):
											if(angle <= -0.071):
												if(y_velocity <= -0.283):
													return True
												else:
													if(x_velocity > -0.12):
														if(lander_x > -0.309):
															if(y_velocity <= -0.262):
																return True
											else:
												if(y_velocity > -0.272):
													if(angle_velocity <= 0.008):
														return True
										else:
											if(x_velocity <= -0.066):
												if(lander_y <= 0.69):
													if(angle_velocity <= 0.034):
														return True
													else:
														if(lander_y > 0.636):
															if(angle <= -0.084):
																return True
												else:
													if(y_velocity <= -0.271):
														if(lander_y <= 1.013):
															if(x_velocity > -0.068):
																if(lander_y <= 0.921):
																	return True
														else:
															return True
													else:
														return True
											else:
												if(y_velocity <= -0.288):
													if(x_velocity > -0.026):
														return True
												else:
													return True
									else:
										if(lander_y <= 0.766):
											if(angle <= -0.107):
												if(y_velocity > -0.283):
													if(y_velocity <= -0.274):
														if(lander_x <= -0.27):
															return True
											else:
												if(x_velocity > -0.144):
													if(y_velocity <= -0.271):
														if(angle <= -0.103):
															if(angle > -0.105):
																return True
													else:
														if(lander_y <= 0.583):
															if(lander_y <= 0.442):
																if(x_velocity > -0.079):
																	return True
										else:
											if(x_velocity <= 0.017):
												if(y_velocity > -0.267):
													if(y_velocity <= -0.263):
														return True
											else:
												if(y_velocity > -0.28):
													if(angle_velocity <= 0.111):
														return True
							else:
								if(lander_y <= 0.786):
									if(y_velocity <= -0.265):
										if(lander_y <= 0.727):
											if(x_velocity > -0.116):
												if(angle_velocity <= 0.082):
													if(y_velocity <= -0.266):
														if(y_velocity > -0.278):
															if(y_velocity <= -0.278):
																return True
															else:
																if(x_velocity > -0.093):
																	if(angle_velocity <= 0.004):
																		if(angle_velocity <= 0.003):
																			if(lander_y > 0.648):
																				if(angle <= -0.035):
																					return True
																				else:
																					if(x_velocity > 0.026):
																						if(angle_velocity <= -0.007):
																							return True
																		else:
																			return True
													else:
														if(y_velocity <= -0.266):
															return True
														else:
															if(lander_x > 0.098):
																if(x_velocity > -0.039):
																	return True
										else:
											if(lander_y <= 0.728):
												if(lander_x <= -0.015):
													return True
											else:
												if(y_velocity <= -0.27):
													if(angle <= -0.037):
														if(y_velocity <= -0.282):
															if(y_velocity > -0.291):
																if(lander_x > 0.069):
																	return True
														else:
															if(angle_velocity <= -0.005):
																return True
													else:
														if(y_velocity > -0.275):
															if(y_velocity <= -0.275):
																return True
												else:
													if(angle_velocity <= -0.004):
														if(y_velocity <= -0.268):
															return True
									else:
										if(angle <= -0.018):
											if(lander_y <= 0.672):
												if(angle <= -0.02):
													if(angle_velocity <= -0.016):
														if(angle_velocity > -0.025):
															return True
													else:
														if(lander_x <= 0.099):
															if(lander_y > 0.569):
																if(x_velocity <= -0.044):
																	return True
												else:
													return True
											else:
												if(angle_velocity <= 0.031):
													if(y_velocity > -0.264):
														return True
												else:
													if(x_velocity > 0.023):
														if(angle_velocity > 0.041):
															return True
										else:
											if(lander_x <= 0.156):
												if(angle <= -0.013):
													if(x_velocity > 0.042):
														return True
												else:
													if(lander_x <= -0.171):
														if(y_velocity > -0.26):
															return True
											else:
												if(x_velocity > -0.061):
													if(angle <= 0.003):
														return True
								else:
									if(y_velocity <= -0.281):
										if(lander_y <= 1.322):
											if(x_velocity <= 0.689):
												if(y_velocity <= -0.292):
													if(lander_y <= 1.13):
														if(lander_y <= 0.793):
															if(lander_x > 0.046):
																return True
													else:
														if(x_velocity > -0.068):
															if(angle <= 0.033):
																if(y_velocity <= -0.297):
																	if(lander_x <= 0.055):
																		if(y_velocity <= -0.31):
																			if(lander_y <= 1.131):
																				return True
																			else:
																				if(angle_velocity <= -0.029):
																					return True
																		else:
																			if(x_velocity > -0.025):
																				if(angle_velocity <= 0.02):
																					return True
																	else:
																		return True
												else:
													if(angle <= -0.032):
														if(angle_velocity <= 0.032):
															if(lander_y > 0.825):
																return True
													else:
														if(angle_velocity <= -0.014):
															if(angle <= -0.0):
																return True
														else:
															if(lander_y <= 1.098):
																if(angle <= -0.023):
																	if(angle_velocity <= 0.003):
																		return True
																else:
																	if(lander_x <= -0.067):
																		if(lander_y > 0.938):
																			if(lander_x > -0.069):
																				return True
															else:
																if(lander_x <= -0.014):
																	if(lander_x <= -0.047):
																		return True
																else:
																	if(lander_y <= 1.133):
																		if(y_velocity <= -0.286):
																			return True
																	else:
																		if(angle <= 0.055):
																			if(x_velocity > 0.069):
																				return True
											else:
												return True
										else:
											if(x_velocity <= 0.337):
												if(angle_velocity <= 0.028):
													if(y_velocity <= -0.309):
														if(lander_x > 0.0):
															if(angle_velocity <= 0.014):
																return True
													else:
														if(x_velocity <= -0.025):
															if(angle <= -0.007):
																return True
														else:
															return True
												else:
													if(x_velocity <= 0.264):
														if(lander_x > -0.008):
															if(y_velocity > -0.284):
																if(lander_x <= 0.016):
																	return True
													else:
														if(angle_velocity <= 0.225):
															return True
											else:
												if(lander_x <= 0.086):
													return True
									else:
										if(angle <= 0.009):
											if(x_velocity <= 0.03):
												if(angle_velocity <= -0.004):
													if(x_velocity <= -0.073):
														if(angle <= -0.039):
															return True
													else:
														if(y_velocity <= -0.277):
															if(lander_x <= 0.125):
																if(lander_y <= 1.083):
																	if(lander_x > 0.051):
																		if(lander_x <= 0.069):
																			return True
																else:
																	return True
															else:
																return True
														else:
															if(y_velocity <= -0.262):
																if(angle_velocity > -0.029):
																	if(x_velocity <= -0.008):
																		return True
																	else:
																		if(x_velocity > -0.004):
																			return True
												else:
													if(lander_y > 0.837):
														if(x_velocity <= 0.002):
															if(lander_x > -0.148):
																if(lander_x > 0.034):
																	if(lander_x <= 0.035):
																		return True
														else:
															if(angle_velocity <= 0.07):
																if(x_velocity <= 0.019):
																	return True
											else:
												if(lander_y <= 0.884):
													if(angle > 0.002):
														if(lander_y <= 0.825):
															return True
												else:
													if(x_velocity > 0.044):
														return True
										else:
											if(x_velocity > -0.025):
												if(lander_y <= 1.104):
													if(angle_velocity <= -0.008):
														if(lander_x <= -0.007):
															if(lander_y <= 0.883):
																if(lander_x > -0.025):
																	return True
															else:
																return True
														else:
															if(angle_velocity > -0.01):
																return True
													else:
														if(x_velocity > 0.064):
															if(angle_velocity <= 0.012):
																return True
												else:
													if(angle <= 0.06):
														if(x_velocity <= 0.077):
															if(angle_velocity <= 0.049):
																if(y_velocity > -0.277):
																	return True
														else:
															if(angle <= 0.045):
																return True
													else:
														if(x_velocity > 0.016):
															if(angle <= 0.594):
																if(angle <= 0.092):
																	if(angle <= 0.089):
																		if(angle_velocity <= -0.022):
																			return True
																		else:
																			if(x_velocity > 0.102):
																				if(angle_velocity <= 0.041):
																					return True
																	else:
																		if(angle_velocity <= -0.008):
																			return True
					else:
						if(x_velocity <= 0.035):
							if(lander_y <= 0.672):
								if(y_velocity <= -0.242):
									if(angle <= -0.03):
										if(angle_velocity <= 0.012):
											if(y_velocity > -0.257):
												if(x_velocity > -0.096):
													if(lander_y <= 0.634):
														if(lander_x > -0.264):
															if(angle_velocity <= -0.0):
																return True
															else:
																if(angle <= -0.038):
																	return True
																else:
																	if(lander_y > 0.441):
																		if(angle_velocity > 0.011):
																			return True
										else:
											if(x_velocity <= -0.041):
												if(x_velocity > -0.07):
													if(x_velocity <= -0.06):
														return True
											else:
												if(angle_velocity <= 0.063):
													if(lander_y > 0.581):
														return True
												else:
													if(x_velocity <= -0.025):
														return True
									else:
										if(x_velocity <= -0.023):
											if(y_velocity <= -0.251):
												if(x_velocity <= -0.034):
													if(x_velocity > -0.093):
														if(y_velocity <= -0.259):
															if(angle > -0.023):
																return True
														else:
															if(angle <= -0.027):
																if(x_velocity > -0.049):
																	return True
												else:
													if(y_velocity <= -0.255):
														return True
											else:
												if(lander_y <= 0.549):
													if(angle_velocity <= 0.029):
														if(angle <= -0.009):
															if(lander_x <= 0.094):
																if(angle <= -0.021):
																	if(angle_velocity <= -0.012):
																		if(x_velocity <= -0.032):
																			return True
															else:
																if(angle <= -0.01):
																	return True
												else:
													if(angle > -0.001):
														if(angle_velocity <= -0.017):
															return True
										else:
											if(angle <= 0.003):
												if(angle_velocity <= -0.006):
													if(lander_x <= -0.077):
														if(x_velocity > 0.004):
															if(angle_velocity <= -0.021):
																if(y_velocity > -0.257):
																	return True
													else:
														if(y_velocity <= -0.252):
															if(lander_y > 0.516):
																return True
														else:
															return True
												else:
													if(y_velocity > -0.248):
														if(lander_x > -0.19):
															if(lander_x <= 0.055):
																if(lander_y <= 0.646):
																	if(angle_velocity <= 0.013):
																		if(x_velocity <= 0.007):
																			return True
															else:
																return True
								else:
									if(angle <= 0.027):
										if(angle_velocity <= 0.015):
											if(x_velocity <= -0.051):
												if(angle_velocity <= -0.02):
													if(angle_velocity > -0.023):
														return True
											else:
												if(lander_y <= 0.519):
													if(lander_x <= -0.062):
														if(angle <= -0.012):
															if(x_velocity > 0.006):
																if(lander_x > -0.177):
																	return True
														else:
															if(y_velocity > -0.233):
																if(angle <= -0.008):
																	return True
													else:
														if(angle <= 0.002):
															if(y_velocity <= -0.239):
																if(angle_velocity <= -0.01):
																	return True
															else:
																if(angle_velocity <= 0.012):
																	return True
																else:
																	if(x_velocity > -0.014):
																		return True
														else:
															if(x_velocity > -0.002):
																if(x_velocity <= 0.007):
																	return True
												else:
													if(x_velocity <= 0.014):
														if(lander_x <= 0.059):
															if(angle <= -0.024):
																return True
															else:
																if(x_velocity > 0.005):
																	if(x_velocity <= 0.01):
																		return True
														else:
															if(y_velocity <= -0.222):
																return True
													else:
														if(y_velocity > -0.238):
															if(lander_y <= 0.611):
																return True
															else:
																if(x_velocity <= 0.026):
																	return True
										else:
											if(y_velocity <= -0.23):
												if(x_velocity <= -0.011):
													if(angle <= -0.059):
														if(angle > -0.065):
															return True
													else:
														if(lander_y > 0.401):
															if(y_velocity <= -0.239):
																if(y_velocity > -0.239):
																	return True
												else:
													if(lander_x <= -0.028):
														if(angle_velocity > 0.059):
															return True
											else:
												if(angle <= -0.047):
													if(angle > -0.057):
														return True
												else:
													if(lander_y > 0.585):
														if(lander_x > 0.01):
															return True
									else:
										if(lander_y > 0.551):
											if(lander_y <= 0.592):
												if(lander_x <= 0.029):
													return True
							else:
								if(y_velocity <= -0.254):
									if(lander_y <= 0.805):
										if(x_velocity <= -0.02):
											if(y_velocity <= -0.257):
												if(y_velocity <= -0.257):
													if(angle <= -0.06):
														return True
												else:
													return True
										else:
											if(y_velocity <= -0.259):
												if(lander_y > 0.709):
													return True
									else:
										if(y_velocity <= -0.256):
											if(angle_velocity <= -0.015):
												if(lander_y <= 0.825):
													return True
										else:
											if(lander_x <= 0.034):
												if(lander_x <= 0.028):
													if(x_velocity <= 0.023):
														return True
													else:
														if(angle_velocity <= 0.003):
															return True
								else:
									if(angle <= -0.028):
										if(lander_y <= 0.722):
											return True
										else:
											if(lander_y > 0.774):
												if(angle > -0.041):
													return True
									else:
										if(angle <= 0.01):
											if(angle <= 0.008):
												if(angle_velocity <= 0.019):
													if(x_velocity > -0.053):
														if(lander_x <= -0.008):
															if(x_velocity <= 0.0):
																if(lander_x > -0.023):
																	if(lander_y <= 1.034):
																		return True
															else:
																if(lander_x > -0.129):
																	if(lander_y > 0.723):
																		return True
														else:
															return True
											else:
												return True
										else:
											if(lander_y > 0.698):
												if(y_velocity <= -0.25):
													if(lander_y > 0.803):
														if(y_velocity > -0.251):
															return True
												else:
													if(angle <= 0.015):
														if(angle > 0.014):
															return True
						else:
							if(lander_y <= 0.649):
								if(angle_velocity <= -0.007):
									if(x_velocity <= 0.055):
										if(angle <= -0.012):
											return True
										else:
											if(lander_x > 0.036):
												return True
									else:
										if(angle <= 0.021):
											return True
										else:
											if(y_velocity <= -0.229):
												if(lander_x > -0.09):
													if(angle <= 0.046):
														return True
											else:
												if(angle_velocity > -0.029):
													return True
								else:
									if(angle <= 0.013):
										if(y_velocity <= -0.233):
											if(angle_velocity <= 0.009):
												if(x_velocity > 0.042):
													if(y_velocity <= -0.246):
														if(angle <= -0.005):
															return True
													else:
														return True
											else:
												if(lander_x <= -0.302):
													if(lander_y > 0.509):
														return True
												else:
													if(lander_y > 0.64):
														if(lander_x <= -0.134):
															return True
										else:
											if(lander_y <= 0.542):
												if(x_velocity <= 0.092):
													if(x_velocity <= 0.048):
														return True
													else:
														if(angle_velocity <= 0.016):
															return True
												else:
													return True
											else:
												if(angle_velocity <= 0.023):
													return True
									else:
										if(y_velocity <= -0.23):
											if(angle_velocity <= -0.001):
												if(lander_x > -0.011):
													return True
							else:
								if(angle <= 0.131):
									if(lander_y <= 0.774):
										if(y_velocity <= -0.228):
											if(angle_velocity <= -0.009):
												if(angle <= 0.039):
													return True
											else:
												if(angle <= 0.015):
													if(angle_velocity <= 0.075):
														if(y_velocity <= -0.246):
															if(angle_velocity > 0.054):
																return True
														else:
															if(lander_x <= -0.18):
																if(lander_x <= -0.21):
																	return True
															else:
																if(angle_velocity <= 0.05):
																	return True
																else:
																	if(lander_y > 0.713):
																		return True
												else:
													if(x_velocity > 0.047):
														if(y_velocity <= -0.229):
															if(angle_velocity <= 0.004):
																if(angle <= 0.037):
																	if(y_velocity > -0.247):
																		return True
														else:
															return True
										else:
											if(angle_velocity <= 0.026):
												if(lander_y <= 0.682):
													return True
									else:
										if(y_velocity <= -0.248):
											if(angle <= 0.027):
												if(angle_velocity <= 0.045):
													if(lander_y > 0.78):
														return True
												else:
													if(lander_y > 0.847):
														if(x_velocity > 0.043):
															if(angle_velocity <= 0.085):
																return True
											else:
												if(x_velocity > 0.069):
													if(angle_velocity <= 0.014):
														return True
													else:
														if(lander_y > 1.385):
															return True
										else:
											if(lander_y <= 1.382):
												if(angle_velocity <= 0.034):
													if(lander_y <= 0.848):
														if(angle_velocity <= 0.015):
															return True
													else:
														if(lander_x <= -0.044):
															return True
														else:
															if(x_velocity > 0.064):
																if(x_velocity > 0.068):
																	if(lander_x <= 0.031):
																		return True
												else:
													if(x_velocity <= 0.041):
														if(angle <= -0.007):
															return True
											else:
												if(x_velocity > 0.12):
													return True
		else:
			if(angle_velocity <= -0.011):
				if(right_leg_contact != True):
					if(angle <= 0.062):
						if(angle_velocity <= -0.036):
							if(x_velocity <= -0.049):
								if(angle <= -0.018):
									if(x_velocity > -0.312):
										if(x_velocity <= -0.051):
											if(x_velocity <= -0.097):
												if(angle_velocity <= -0.061):
													if(x_velocity <= -0.223):
														if(angle_velocity <= -0.163):
															if(lander_x <= -0.055):
																return True
															else:
																if(angle_velocity <= -0.213):
																	return True
														else:
															if(x_velocity <= -0.312):
																return True
													else:
														return True
											else:
												if(y_velocity <= -0.218):
													if(y_velocity <= -0.219):
														return True
												else:
													return True
								else:
									if(y_velocity > -0.216):
										if(lander_x <= 0.106):
											if(lander_y <= 0.076):
												if(x_velocity > -0.064):
													return True
										else:
											if(lander_y > 0.012):
												if(y_velocity <= -0.187):
													return True
							else:
								if(angle_velocity <= -0.052):
									if(angle <= 0.036):
										if(lander_y <= 0.657):
											if(lander_x <= 0.046):
												return True
											else:
												if(lander_x > 0.046):
													return True
										else:
											if(angle <= 0.01):
												return True
									else:
										if(angle_velocity <= -0.07):
											return True
										else:
											if(angle_velocity > -0.062):
												if(x_velocity > 0.044):
													if(angle <= 0.05):
														return True
								else:
									if(lander_x <= -0.175):
										if(y_velocity <= -0.207):
											if(angle <= -0.002):
												if(lander_x > -0.194):
													return True
										else:
											if(lander_y <= 0.319):
												if(angle_velocity > -0.046):
													return True
									else:
										if(x_velocity <= 0.029):
											if(angle <= 0.025):
												if(lander_x <= -0.072):
													if(angle <= -0.015):
														return True
													else:
														if(x_velocity > 0.008):
															if(angle <= 0.012):
																return True
												else:
													if(left_leg_contact != True):
														if(angle <= 0.018):
															if(x_velocity <= -0.034):
																if(angle_velocity > -0.045):
																	if(lander_x <= 0.016):
																		if(lander_y <= 0.086):
																			return True
																	else:
																		return True
															else:
																return True
														else:
															if(lander_x > 0.055):
																return True
											else:
												if(lander_y > 0.175):
													if(lander_y <= 0.275):
														return True
										else:
											if(angle <= 0.059):
												if(lander_y <= 0.558):
													if(y_velocity <= -0.164):
														return True
						else:
							if(x_velocity <= 0.002):
								if(lander_y <= 0.172):
									if(y_velocity <= -0.197):
										if(angle <= -0.004):
											if(lander_x > -0.161):
												if(x_velocity > -0.078):
													if(angle <= -0.022):
														if(x_velocity > -0.074):
															return True
													else:
														if(angle > -0.01):
															return True
										else:
											if(lander_y > 0.091):
												if(lander_x <= 0.025):
													if(y_velocity > -0.204):
														return True
												else:
													if(angle_velocity <= -0.02):
														return True
									else:
										if(angle <= -0.001):
											if(x_velocity <= -0.042):
												if(y_velocity > -0.187):
													return True
											else:
												return True
								else:
									if(lander_x <= 0.072):
										if(y_velocity <= -0.219):
											return True
										else:
											if(angle_velocity <= -0.011):
												if(y_velocity > -0.206):
													if(y_velocity <= -0.202):
														if(angle > -0.011):
															if(x_velocity > -0.02):
																return True
									else:
										if(x_velocity > -0.068):
											return True
							else:
								if(lander_y <= 0.216):
									if(y_velocity <= -0.189):
										if(angle <= 0.005):
											if(angle <= -0.01):
												return True
											else:
												if(x_velocity <= 0.028):
													if(lander_x > -0.049):
														return True
												else:
													return True
										else:
											if(x_velocity <= 0.079):
												if(lander_y <= 0.144):
													if(angle <= 0.016):
														if(angle <= 0.015):
															if(lander_x > -0.022):
																if(lander_x <= 0.003):
																	return True
														else:
															return True
												else:
													if(lander_x <= -0.027):
														if(lander_y > 0.16):
															if(y_velocity <= -0.218):
																return True
													else:
														if(angle_velocity > -0.031):
															return True
											else:
												return True
									else:
										if(lander_x <= -0.086):
											if(x_velocity <= 0.057):
												if(angle <= -0.004):
													if(y_velocity <= -0.175):
														return True
											else:
												if(angle_velocity > -0.023):
													return True
										else:
											if(angle <= 0.046):
												if(y_velocity <= -0.186):
													if(lander_y > 0.111):
														if(y_velocity <= -0.188):
															return True
												else:
													if(lander_y <= 0.043):
														if(lander_y <= 0.035):
															return True
													else:
														return True
											else:
												if(y_velocity > -0.17):
													if(x_velocity > 0.082):
														return True
								else:
									if(lander_x <= -0.044):
										if(x_velocity <= 0.062):
											if(y_velocity <= -0.21):
												if(angle <= 0.003):
													return True
												else:
													if(lander_y > 0.439):
														if(angle_velocity <= -0.025):
															return True
											else:
												if(angle_velocity <= -0.012):
													if(angle_velocity <= -0.023):
														if(y_velocity <= -0.189):
															if(angle_velocity > -0.032):
																return True
												else:
													return True
										else:
											if(lander_x <= -0.189):
												if(angle_velocity > -0.024):
													return True
											else:
												return True
									else:
										if(x_velocity <= 0.01):
											if(x_velocity <= 0.009):
												if(y_velocity > -0.184):
													return True
										else:
											if(lander_y <= 0.627):
												if(y_velocity <= -0.212):
													if(y_velocity <= -0.214):
														return True
												else:
													return True
											else:
												if(angle <= 0.017):
													return True
					else:
						if(y_velocity <= -0.174):
							if(angle <= 0.082):
								if(angle_velocity <= -0.041):
									if(lander_x <= 0.111):
										return True
								else:
									if(lander_x > -0.061):
										if(x_velocity > 0.067):
											return True
							else:
								if(x_velocity <= 0.157):
									if(angle_velocity <= -0.113):
										if(lander_y <= 1.119):
											return True
										else:
											if(y_velocity <= -0.213):
												if(lander_x > 0.169):
													return True
									else:
										if(lander_y > 1.054):
											if(lander_x <= 0.079):
												if(y_velocity > -0.217):
													return True
								else:
									if(angle_velocity <= -0.136):
										if(angle <= 0.323):
											if(y_velocity <= -0.186):
												if(x_velocity <= 0.172):
													if(lander_x > 0.216):
														return True
												else:
													return True
						else:
							if(lander_y <= 0.324):
								if(x_velocity <= 0.133):
									if(y_velocity <= -0.164):
										if(y_velocity > -0.171):
											return True
								else:
									if(angle_velocity <= -0.033):
										return True
									else:
										if(lander_y > 0.104):
											return True
							else:
								if(angle_velocity <= -0.135):
									if(x_velocity > 0.221):
										return True
				else:
					if(x_velocity <= 0.091):
						if(lander_y > 0.015):
							if(angle_velocity <= -0.428):
								return True
					else:
						if(angle_velocity <= -0.514):
							return True
						else:
							if(angle <= -0.098):
								return True
			else:
				if(lander_y <= 0.246):
					if(y_velocity <= -0.186):
						if(x_velocity <= 0.019):
							if(y_velocity <= -0.204):
								if(x_velocity <= -0.027):
									if(left_leg_contact != True):
										if(angle_velocity <= 0.004):
											if(lander_x <= 0.063):
												if(angle <= -0.054):
													if(angle > -0.073):
														return True
											else:
												if(y_velocity > -0.212):
													return True
								else:
									if(lander_y <= 0.187):
										if(lander_x > -0.131):
											if(lander_y > 0.002):
												if(angle_velocity <= -0.005):
													if(lander_y > 0.124):
														if(y_velocity <= -0.205):
															return True
									else:
										if(lander_x > -0.04):
											if(y_velocity > -0.211):
												if(x_velocity <= 0.009):
													if(angle_velocity <= 0.004):
														return True
							else:
								if(angle_velocity <= -0.005):
									if(angle <= -0.001):
										return True
									else:
										if(angle_velocity <= -0.009):
											if(angle_velocity > -0.01):
												return True
								else:
									if(lander_y > 0.004):
										if(angle <= 0.019):
											if(x_velocity <= 0.019):
												if(x_velocity > -0.001):
													if(angle_velocity <= 0.014):
														if(y_velocity <= -0.197):
															if(angle <= -0.002):
																return True
													else:
														if(lander_y > 0.011):
															if(lander_x > 0.069):
																if(angle <= 0.01):
																	return True
											else:
												return True
						else:
							if(angle <= 0.011):
								if(y_velocity <= -0.201):
									if(angle <= -0.031):
										if(angle_velocity <= 0.029):
											return True
									else:
										if(angle_velocity <= -0.001):
											if(y_velocity <= -0.21):
												if(angle_velocity > -0.006):
													return True
											else:
												return True
										else:
											if(angle <= -0.015):
												if(lander_x <= -0.114):
													if(x_velocity > 0.083):
														return True
												else:
													if(angle > -0.02):
														return True
											else:
												if(x_velocity > 0.059):
													if(x_velocity <= 0.061):
														return True
								else:
									if(lander_y <= 0.138):
										if(angle <= -0.01):
											if(angle_velocity <= 0.03):
												return True
										else:
											if(angle_velocity <= -0.005):
												if(lander_x > -0.081):
													return True
									else:
										if(y_velocity > -0.196):
											if(lander_x <= -0.035):
												if(x_velocity > 0.045):
													return True
											else:
												return True
							else:
								if(right_leg_contact != True):
									if(lander_y <= 0.148):
										if(lander_x <= -0.244):
											if(y_velocity > -0.199):
												return True
										else:
											if(lander_x > 0.069):
												if(lander_x <= 0.075):
													return True
									else:
										if(angle_velocity <= -0.004):
											if(lander_x > -0.148):
												return True
										else:
											if(y_velocity > -0.2):
												if(angle <= 0.034):
													if(angle_velocity <= 0.031):
														if(y_velocity > -0.2):
															return True
					else:
						if(x_velocity <= 0.079):
							if(left_leg_contact != True):
								if(x_velocity <= 0.053):
									if(angle <= -0.01):
										if(angle_velocity <= 0.028):
											if(x_velocity > -0.004):
												return True
									else:
										if(lander_y <= 0.011):
											if(lander_y > 0.004):
												return True
										else:
											if(lander_x <= 0.122):
												if(angle <= 0.049):
													if(angle <= 0.007):
														if(angle > 0.006):
															return True
											else:
												if(x_velocity > -0.016):
													return True
								else:
									if(y_velocity <= -0.171):
										if(lander_x <= -0.036):
											if(angle_velocity <= 0.018):
												if(angle <= 0.034):
													return True
											else:
												if(angle <= -0.011):
													return True
										else:
											if(lander_y <= 0.165):
												if(y_velocity > -0.172):
													return True
											else:
												return True
									else:
										if(angle_velocity <= -0.004):
											if(y_velocity <= -0.16):
												if(angle <= 0.049):
													return True
						else:
							if(y_velocity <= -0.164):
								if(angle_velocity <= -0.007):
									return True
								else:
									if(angle_velocity <= 0.078):
										if(lander_y <= 0.149):
											if(lander_y > -0.005):
												if(angle <= 0.049):
													if(angle <= 0.047):
														if(x_velocity > 0.096):
															if(angle_velocity <= 0.046):
																if(lander_x <= -0.068):
																	return True
													else:
														return True
							else:
								if(x_velocity <= 0.082):
									if(lander_y > 0.09):
										return True
								else:
									if(x_velocity > 0.146):
										if(y_velocity <= -0.142):
											if(lander_y <= 0.049):
												if(y_velocity > -0.146):
													return True
											else:
												if(lander_y <= 0.077):
													return True
												else:
													if(angle_velocity <= 0.02):
														return True
				else:
					if(x_velocity <= 0.09):
						if(y_velocity <= -0.21):
							if(x_velocity <= 0.014):
								if(angle_velocity <= -0.0):
									if(lander_x > -0.002):
										if(lander_y > 0.289):
											return True
								else:
									if(y_velocity <= -0.218):
										if(lander_y <= 0.313):
											if(angle <= -0.009):
												if(lander_y > 0.279):
													return True
										else:
											if(angle_velocity <= 0.004):
												return True
											else:
												if(y_velocity > -0.218):
													return True
									else:
										if(x_velocity > -0.006):
											if(x_velocity <= -0.004):
												return True
							else:
								if(lander_y <= 0.419):
									if(angle <= -0.001):
										if(angle > -0.016):
											if(angle_velocity <= 0.046):
												return True
									else:
										if(angle_velocity <= 0.001):
											if(x_velocity > 0.051):
												return True
								else:
									if(lander_x <= 0.03):
										if(y_velocity <= -0.211):
											if(angle <= -0.012):
												return True
										else:
											if(angle_velocity <= 0.029):
												return True
											else:
												if(lander_y > 1.309):
													return True
									else:
										if(lander_y > 0.556):
											if(lander_y <= 0.702):
												return True
						else:
							if(x_velocity <= 0.071):
								if(lander_y <= 0.332):
									if(y_velocity <= -0.201):
										if(angle <= 0.018):
											if(lander_x > -0.041):
												if(x_velocity <= 0.013):
													if(angle_velocity <= 0.009):
														if(angle <= -0.0):
															return True
												else:
													if(lander_y <= 0.304):
														if(lander_x > 0.079):
															return True
													else:
														return True
									else:
										if(angle_velocity <= -0.009):
											return True
										else:
											if(lander_x <= 0.082):
												if(x_velocity <= 0.057):
													if(y_velocity <= -0.199):
														if(y_velocity > -0.199):
															return True
												else:
													if(angle_velocity <= 0.028):
														return True
								else:
									if(y_velocity <= -0.148):
										if(lander_y <= 1.41):
											if(x_velocity > 0.033):
												if(x_velocity <= 0.033):
													return True
												else:
													if(lander_y <= 1.046):
														if(lander_y > 0.586):
															if(lander_y <= 0.593):
																return True
													else:
														return True
										else:
											if(x_velocity <= 0.032):
												return True
									else:
										return True
							else:
								if(angle_velocity <= 0.007):
									if(lander_x > -0.175):
										return True
								else:
									if(lander_x > -0.087):
										if(angle <= 0.051):
											if(angle <= 0.047):
												return True
					else:
						if(y_velocity <= -0.173):
							if(x_velocity <= 0.385):
								if(angle_velocity <= 0.08):
									if(lander_y <= 0.467):
										if(angle <= 0.054):
											if(y_velocity <= -0.186):
												if(lander_x <= -0.247):
													if(angle_velocity <= 0.005):
														return True
													else:
														if(lander_y > 0.436):
															return True
												else:
													return True
											else:
												if(angle > 0.048):
													return True
										else:
											if(x_velocity > 0.175):
												if(angle_velocity <= 0.026):
													return True
									else:
										if(x_velocity <= 0.262):
											if(lander_y <= 0.677):
												if(y_velocity <= -0.202):
													if(angle <= 0.052):
														if(angle_velocity <= 0.032):
															return True
											else:
												if(x_velocity <= 0.091):
													return True
								else:
									if(lander_y <= 1.385):
										if(y_velocity > -0.215):
											if(y_velocity <= -0.209):
												if(lander_y <= 0.577):
													return True
									else:
										if(angle_velocity > 0.127):
											if(x_velocity <= 0.225):
												if(lander_x <= 0.023):
													return True
											else:
												return True
							else:
								if(angle <= 0.153):
									return True
						else:
							if(x_velocity <= 0.541):
								if(lander_y <= 1.487):
									if(angle <= 0.024):
										return True
									else:
										if(x_velocity <= 0.521):
											if(lander_y <= 1.465):
												if(lander_x <= -0.253):
													if(lander_x > -0.259):
														return True
												else:
													if(y_velocity > -0.146):
														if(angle <= 0.243):
															return True
							else:
								if(lander_x <= 0.119):
									return True
	else:
		if(y_velocity <= -0.0):
			if(angle <= 0.102):
				if(lander_y <= 0.046):
					if(angle_velocity <= 0.481):
						if(right_leg_contact != True):
							if(angle_velocity <= 0.145):
								if(y_velocity <= -0.0):
									if(lander_x > -0.169):
										if(x_velocity > 0.113):
											return True
				else:
					if(x_velocity <= 0.224):
						if(angle <= 0.001):
							if(y_velocity <= -0.1):
								if(angle <= -0.001):
									if(lander_y <= 1.451):
										return True
									else:
										if(lander_x <= -0.061):
											return True
							else:
								if(x_velocity > 0.047):
									if(angle <= -0.001):
										return True
						else:
							if(lander_x > 0.001):
								if(angle_velocity <= 0.166):
									if(x_velocity <= 0.077):
										if(lander_x <= 0.003):
											return True
									else:
										return True
					else:
						return True
			else:
				if(x_velocity > -0.005):
					if(x_velocity > -0.001):
						if(angle_velocity > 0.182):
							if(lander_y > 1.442):
								if(x_velocity > 0.407):
									if(angle <= 0.193):
										return True
									else:
										if(angle_velocity <= 0.261):
											return True
		else:
			if(x_velocity <= 0.187):
				if(lander_y > -0.044):
					if(x_velocity > -0.296):
						if(x_velocity > -0.136):
							if(angle <= 0.305):
								if(lander_y <= 1.455):
									if(x_velocity > 0.178):
										if(lander_y > 0.706):
											return True
								else:
									if(lander_y <= 1.457):
										if(x_velocity > -0.015):
											return True
									else:
										if(y_velocity <= 0.011):
											return True
			else:
				if(x_velocity <= 0.444):
					if(lander_y <= 1.477):
						if(x_velocity <= 0.23):
							return True
						else:
							if(x_velocity <= 0.271):
								if(angle_velocity <= 0.093):
									if(angle <= -0.0):
										if(x_velocity <= 0.262):
											if(y_velocity > 0.262):
												return True
									else:
										return True
							else:
								return True
				else:
					return True
	return False

def weShould_main_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.137):
		if(y_velocity <= -0.22):
			if(angle_velocity <= -0.03):
				if(angle <= 0.195):
					if(lander_y <= 1.341):
						if(y_velocity <= -0.271):
							if(angle <= 0.061):
								if(y_velocity <= -0.474):
									if(x_velocity <= -0.594):
										if(y_velocity <= -0.574):
											return True
									else:
										if(angle <= -0.289):
											if(y_velocity <= -0.501):
												if(y_velocity <= -0.541):
													return True
												else:
													if(lander_y <= 1.073):
														if(angle_velocity <= -0.05):
															if(lander_y > 1.036):
																if(angle_velocity > -0.195):
																	return True
														else:
															return True
													else:
														return True
											else:
												if(y_velocity > -0.478):
													return True
										else:
											if(angle <= -0.031):
												if(lander_x <= -0.15):
													if(lander_x <= -0.153):
														if(angle_velocity <= -0.27):
															if(x_velocity <= -0.526):
																return True
														else:
															return True
												else:
													if(angle <= -0.065):
														return True
													else:
														if(angle > -0.061):
															if(y_velocity <= -0.499):
																return True
															else:
																if(x_velocity > -0.474):
																	return True
											else:
												if(y_velocity <= -0.546):
													if(x_velocity > -0.57):
														if(x_velocity <= -0.557):
															if(lander_y > 1.301):
																return True
														else:
															return True
								else:
									if(angle_velocity <= -0.087):
										if(y_velocity <= -0.343):
											if(angle <= -0.183):
												if(x_velocity <= -0.533):
													return True
												else:
													if(lander_y <= 1.077):
														if(x_velocity <= -0.406):
															if(y_velocity <= -0.439):
																if(lander_x <= -0.16):
																	if(y_velocity > -0.461):
																		return True
																else:
																	return True
														else:
															if(angle_velocity > -0.106):
																return True
											else:
												if(x_velocity <= -0.49):
													if(angle_velocity <= -0.36):
														return True
												else:
													if(angle_velocity <= -0.33):
														if(angle <= 0.018):
															if(x_velocity <= -0.486):
																return True
															else:
																if(angle_velocity <= -0.334):
																	if(lander_y <= 0.96):
																		if(angle_velocity <= -0.392):
																			return True
														else:
															if(lander_x <= 0.235):
																return True
															else:
																if(y_velocity <= -0.373):
																	return True
													else:
														if(y_velocity <= -0.422):
															if(lander_y <= 0.898):
																if(angle_velocity > -0.229):
																	return True
															else:
																if(x_velocity <= -0.305):
																	if(x_velocity <= -0.474):
																		if(lander_y <= 1.122):
																			return True
																	else:
																		return True
																else:
																	if(lander_y <= 1.272):
																		if(angle_velocity > -0.12):
																			return True
																	else:
																		return True
														else:
															if(angle <= -0.093):
																if(lander_y <= 0.896):
																	return True
																else:
																	if(x_velocity > -0.414):
																		if(angle <= -0.113):
																			if(x_velocity <= -0.38):
																				if(lander_x <= 0.189):
																					return True
																		else:
																			if(angle_velocity > -0.126):
																				return True
															else:
																if(x_velocity <= -0.149):
																	if(angle_velocity <= -0.253):
																		if(y_velocity <= -0.395):
																			if(lander_x > -0.051):
																				return True
																		else:
																			if(angle > 0.014):
																				return True
																	else:
																		if(x_velocity <= -0.253):
																			if(y_velocity <= -0.371):
																				if(x_velocity <= -0.327):
																					if(angle_velocity <= -0.24):
																						return True
																				else:
																					return True
																			else:
																				if(lander_x > 0.195):
																					if(y_velocity <= -0.345):
																						return True
																		else:
																			if(lander_y <= 1.323):
																				return True
																			else:
																				if(lander_y > 1.325):
																					return True
										else:
											if(y_velocity <= -0.289):
												if(angle <= 0.006):
													if(lander_y <= 1.317):
														if(lander_y <= 0.847):
															if(lander_y > 0.793):
																if(x_velocity <= -0.217):
																	if(x_velocity <= -0.229):
																		if(y_velocity > -0.316):
																			if(lander_y > 0.804):
																				return True
																	else:
																		return True
														else:
															if(angle_velocity > -0.095):
																if(angle_velocity <= -0.093):
																	return True
												else:
													if(angle_velocity <= -0.119):
														if(angle <= 0.05):
															if(lander_y <= 0.791):
																return True
														else:
															if(lander_y <= 1.065):
																return True
													else:
														if(lander_x > 0.042):
															if(y_velocity <= -0.293):
																return True
															else:
																if(lander_y <= 1.026):
																	return True
									else:
										if(y_velocity <= -0.295):
											if(angle <= -0.072):
												if(y_velocity <= -0.349):
													if(y_velocity <= -0.442):
														if(y_velocity > -0.47):
															return True
													else:
														if(angle > -0.226):
															if(x_velocity <= -0.158):
																if(angle <= -0.121):
																	if(y_velocity <= -0.403):
																		if(y_velocity <= -0.426):
																			if(y_velocity <= -0.431):
																				return True
																		else:
																			return True
																	else:
																		if(y_velocity <= -0.384):
																			if(y_velocity <= -0.397):
																				if(y_velocity > -0.402):
																					return True
																		else:
																			if(angle <= -0.159):
																				if(angle <= -0.199):
																					if(y_velocity <= -0.38):
																						return True
																				else:
																					if(angle > -0.165):
																						if(angle <= -0.162):
																							return True
																			else:
																				if(y_velocity <= -0.375):
																					return True
																				else:
																					if(lander_x > 0.134):
																						return True
																else:
																	return True
															else:
																if(y_velocity <= -0.369):
																	return True
												else:
													if(lander_x > 0.147):
														if(x_velocity <= -0.206):
															if(lander_x <= 0.154):
																if(angle > -0.11):
																	return True
														else:
															return True
											else:
												if(lander_x <= -0.007):
													if(y_velocity <= -0.321):
														if(lander_x <= -0.031):
															if(angle_velocity <= -0.054):
																if(y_velocity <= -0.422):
																	return True
															else:
																return True
														else:
															if(x_velocity > -0.288):
																if(y_velocity <= -0.334):
																	return True
																else:
																	if(lander_x > -0.021):
																		return True
													else:
														if(lander_y <= 0.86):
															return True
														else:
															if(angle <= -0.006):
																if(x_velocity <= -0.085):
																	if(angle_velocity > -0.059):
																		return True
															else:
																if(x_velocity <= -0.043):
																	if(lander_y <= 1.166):
																		return True
																else:
																	return True
												else:
													if(lander_y <= 1.295):
														if(angle <= -0.036):
															if(y_velocity <= -0.31):
																if(angle_velocity <= -0.076):
																	if(angle_velocity <= -0.086):
																		return True
																else:
																	return True
															else:
																if(x_velocity > -0.18):
																	if(lander_y <= 0.74):
																		if(angle_velocity > -0.064):
																			return True
														else:
															if(x_velocity <= -0.151):
																if(y_velocity <= -0.311):
																	return True
															else:
																if(lander_y <= 0.854):
																	if(lander_y <= 0.842):
																		return True
																else:
																	if(y_velocity <= -0.298):
																		return True
																	else:
																		if(y_velocity > -0.298):
																			return True
													else:
														if(y_velocity <= -0.32):
															return True
										else:
											if(lander_y <= 0.656):
												if(angle <= -0.024):
													if(lander_y <= 0.439):
														return True
													else:
														if(lander_y > 0.639):
															return True
												else:
													if(angle_velocity <= -0.064):
														if(lander_x > -0.006):
															return True
													else:
														return True
											else:
												if(angle <= 0.005):
													if(x_velocity > -0.102):
														if(angle_velocity <= -0.038):
															if(y_velocity <= -0.292):
																if(angle_velocity > -0.06):
																	return True
															else:
																if(angle <= 0.003):
																	if(lander_x <= -0.034):
																		if(angle > -0.011):
																			return True
																else:
																	if(lander_y <= 0.787):
																		return True
														else:
															if(lander_y <= 0.752):
																return True
															else:
																if(angle > -0.012):
																	if(x_velocity <= -0.03):
																		if(lander_y <= 0.839):
																			if(y_velocity > -0.284):
																				return True
																		else:
																			return True
																	else:
																		if(x_velocity > -0.024):
																			return True
												else:
													if(lander_y <= 0.925):
														if(x_velocity <= 0.017):
															if(x_velocity <= -0.003):
																return True
															else:
																if(lander_x <= -0.022):
																	return True
													else:
														if(x_velocity > -0.082):
															if(lander_y <= 1.099):
																if(angle_velocity <= -0.047):
																	if(x_velocity <= -0.034):
																		if(angle_velocity <= -0.054):
																			if(y_velocity <= -0.285):
																				return True
																			else:
																				if(angle > 0.025):
																					if(angle_velocity > -0.075):
																						return True
																else:
																	if(lander_x <= 0.126):
																		return True
							else:
								if(angle_velocity <= -0.093):
									if(angle_velocity <= -0.424):
										if(y_velocity <= -0.339):
											return True
										else:
											if(lander_x > 0.254):
												if(angle > 0.176):
													return True
									else:
										if(angle <= 0.114):
											if(lander_y <= 1.162):
												if(angle <= 0.079):
													if(angle <= 0.078):
														if(lander_x <= 0.127):
															if(y_velocity > -0.281):
																return True
														else:
															if(x_velocity <= -0.23):
																if(y_velocity <= -0.344):
																	return True
															else:
																return True
												else:
													if(angle <= 0.108):
														return True
											else:
												if(y_velocity <= -0.297):
													return True
										else:
											if(lander_x <= 0.242):
												return True
											else:
												if(x_velocity <= -0.078):
													return True
								else:
									if(x_velocity > -0.081):
										if(lander_x <= 0.049):
											if(lander_x <= 0.048):
												return True
										else:
											return True
						else:
							if(lander_y <= 0.289):
								if(angle_velocity <= -0.062):
									if(y_velocity <= -0.245):
										if(lander_y <= 0.146):
											return True
										else:
											if(x_velocity > -0.029):
												return True
									else:
										if(angle > 0.017):
											return True
								else:
									if(y_velocity <= -0.229):
										if(y_velocity <= -0.249):
											return True
										else:
											if(angle <= -0.051):
												if(lander_x <= -0.156):
													if(lander_y > 0.042):
														return True
											else:
												if(lander_y <= 0.215):
													if(angle <= -0.019):
														if(x_velocity <= -0.041):
															if(lander_x <= 0.097):
																return True
															else:
																if(angle <= -0.023):
																	if(lander_y <= 0.115):
																		return True
																else:
																	return True
														else:
															if(y_velocity <= -0.234):
																if(angle_velocity > -0.051):
																	return True
													else:
														return True
												else:
													if(angle <= 0.008):
														if(angle_velocity <= -0.037):
															if(y_velocity > -0.238):
																if(y_velocity <= -0.235):
																	return True
														else:
															if(x_velocity <= -0.008):
																return True
													else:
														return True
									else:
										if(angle <= -0.019):
											if(lander_x > -0.192):
												if(lander_y <= 0.225):
													if(lander_y <= 0.033):
														if(x_velocity > -0.096):
															return True
										else:
											if(angle <= 0.008):
												if(lander_y <= 0.126):
													if(angle_velocity <= -0.037):
														return True
													else:
														if(angle > -0.015):
															return True
												else:
													if(x_velocity <= -0.016):
														if(lander_x <= 0.045):
															return True
											else:
												return True
							else:
								if(angle <= -0.004):
									if(angle_velocity <= -0.041):
										if(y_velocity <= -0.258):
											if(y_velocity <= -0.26):
												if(x_velocity <= -0.078):
													if(lander_y <= 0.577):
														if(angle > -0.036):
															return True
											else:
												if(x_velocity > -0.055):
													return True
									else:
										if(x_velocity > -0.095):
											if(lander_y <= 0.428):
												if(y_velocity <= -0.235):
													if(angle <= -0.011):
														if(x_velocity <= -0.015):
															if(x_velocity > -0.085):
																if(y_velocity <= -0.238):
																	if(lander_y > 0.345):
																		if(lander_x <= 0.113):
																			return True
													else:
														return True
											else:
												if(angle_velocity <= -0.041):
													if(lander_y <= 0.467):
														return True
												else:
													if(lander_x <= -0.263):
														return True
													else:
														if(y_velocity <= -0.265):
															if(y_velocity > -0.266):
																return True
								else:
									if(lander_y <= 0.552):
										if(y_velocity <= -0.249):
											if(angle <= 0.0):
												if(x_velocity > -0.027):
													return True
											else:
												return True
										else:
											if(angle_velocity <= -0.057):
												if(lander_x <= -0.204):
													return True
												else:
													if(x_velocity <= -0.033):
														if(angle_velocity > -0.092):
															return True
													else:
														if(lander_x <= -0.107):
															if(x_velocity <= -0.003):
																return True
											else:
												if(y_velocity <= -0.233):
													if(angle <= 0.003):
														if(lander_y > 0.461):
															return True
													else:
														if(angle_velocity <= -0.038):
															if(angle_velocity <= -0.039):
																if(x_velocity <= 0.07):
																	if(y_velocity <= -0.239):
																		return True
																	else:
																		if(x_velocity <= 0.034):
																			if(y_velocity > -0.238):
																				return True
														else:
															return True
												else:
													if(x_velocity > -0.025):
														if(x_velocity <= 0.034):
															if(y_velocity <= -0.228):
																if(y_velocity <= -0.232):
																	return True
															else:
																return True
														else:
															if(lander_x <= -0.2):
																return True
									else:
										if(x_velocity <= -0.043):
											if(lander_x <= 0.126):
												if(lander_y <= 0.699):
													if(angle > -0.0):
														return True
											else:
												if(y_velocity <= -0.247):
													if(x_velocity <= -0.063):
														if(angle <= 0.174):
															if(angle_velocity > -0.043):
																if(angle <= 0.015):
																	return True
														else:
															return True
													else:
														if(y_velocity <= -0.266):
															return True
										else:
											if(angle <= 0.051):
												if(angle_velocity <= -0.036):
													if(x_velocity <= 0.002):
														if(angle_velocity <= -0.057):
															if(angle <= -0.002):
																return True
														else:
															if(lander_y <= 0.705):
																if(angle > 0.014):
																	return True
												else:
													if(y_velocity <= -0.257):
														if(x_velocity <= 0.006):
															return True
														else:
															if(x_velocity > 0.024):
																return True
													else:
														if(lander_x <= 0.03):
															if(angle > 0.032):
																if(angle <= 0.04):
																	return True
											else:
												if(y_velocity <= -0.254):
													if(angle <= 0.104):
														if(angle_velocity > -0.088):
															if(x_velocity <= 0.003):
																if(lander_y <= 1.057):
																	if(angle > 0.074):
																		return True
															else:
																if(y_velocity <= -0.267):
																	return True
																else:
																	if(angle <= 0.085):
																		if(x_velocity <= 0.009):
																			if(y_velocity > -0.265):
																				return True
																	else:
																		if(lander_y <= 1.241):
																			return True
													else:
														if(lander_x <= 0.1):
															if(angle_velocity > -0.06):
																return True
														else:
															if(angle_velocity <= -0.12):
																if(angle > 0.163):
																	return True
															else:
																return True
												else:
													if(angle_velocity <= -0.096):
														if(y_velocity <= -0.229):
															if(angle_velocity > -0.138):
																if(angle > 0.113):
																	if(x_velocity > 0.018):
																		if(y_velocity <= -0.245):
																			if(angle <= 0.137):
																				if(lander_y <= 0.98):
																					return True
																			else:
																				return True
																		else:
																			if(angle_velocity <= -0.132):
																				return True
													else:
														if(x_velocity <= 0.025):
															if(lander_y > 0.896):
																if(lander_y <= 0.925):
																	if(lander_x > 0.145):
																		return True
														else:
															if(angle <= 0.122):
																if(lander_x <= -0.014):
																	return True
															else:
																if(x_velocity <= 0.084):
																	if(y_velocity <= -0.247):
																		if(lander_y <= 1.207):
																			return True
																	else:
																		if(lander_y <= 1.059):
																			if(lander_x <= 0.143):
																				return True
																else:
																	if(lander_y <= 1.211):
																		return True
																	else:
																		if(y_velocity <= -0.248):
																			return True
					else:
						if(x_velocity <= -0.327):
							if(y_velocity <= -0.424):
								if(angle <= 0.01):
									if(lander_y > 1.343):
										return True
						else:
							if(angle <= -0.004):
								if(y_velocity <= -0.351):
									if(lander_y <= 1.373):
										if(lander_x <= -0.02):
											if(lander_y > 1.366):
												if(x_velocity > -0.319):
													return True
										else:
											return True
							else:
								if(y_velocity <= -0.241):
									return True
				else:
					if(angle <= 0.263):
						if(lander_y > 0.785):
							if(lander_x <= 0.116):
								if(x_velocity > 0.175):
									return True
							else:
								if(x_velocity <= -0.187):
									if(y_velocity <= -0.303):
										return True
									else:
										if(lander_x <= 0.23):
											return True
								else:
									if(y_velocity <= -0.238):
										return True
									else:
										if(angle_velocity <= -0.171):
											if(y_velocity > -0.229):
												return True
										else:
											return True
					else:
						if(y_velocity <= -0.291):
							if(x_velocity <= -0.002):
								if(angle_velocity <= -0.19):
									if(lander_y <= 1.111):
										if(x_velocity > -0.253):
											if(lander_x <= 0.283):
												return True
											else:
												if(y_velocity <= -0.342):
													return True
									else:
										if(y_velocity <= -0.313):
											if(x_velocity <= -0.086):
												if(angle_velocity <= -0.313):
													if(lander_y > 1.117):
														if(y_velocity <= -0.321):
															return True
											else:
												return True
										else:
											if(x_velocity > -0.015):
												return True
							else:
								if(lander_x <= 0.298):
									return True
								else:
									if(lander_y <= 1.194):
										return True
						else:
							if(angle <= 0.332):
								if(x_velocity > -0.113):
									if(angle <= 0.285):
										if(x_velocity > 0.106):
											return True
									else:
										return True
							else:
								if(x_velocity > 0.01):
									if(lander_y <= 1.04):
										if(y_velocity <= -0.258):
											if(angle <= 0.512):
												return True
										else:
											if(x_velocity > 0.12):
												return True
									else:
										if(x_velocity > 0.185):
											return True
			else:
				if(lander_y <= 0.399):
					if(angle_velocity <= -0.006):
						if(y_velocity <= -0.237):
							if(angle <= -0.04):
								if(lander_y <= 0.175):
									if(y_velocity <= -0.245):
										return True
									else:
										if(lander_x > 0.025):
											return True
								else:
									if(y_velocity <= -0.256):
										if(angle_velocity <= -0.018):
											if(lander_x <= -0.05):
												return True
										else:
											return True
							else:
								if(lander_y <= 0.397):
									if(lander_y <= 0.295):
										return True
									else:
										if(lander_y > 0.297):
											if(lander_x <= -0.033):
												return True
											else:
												if(lander_x <= -0.003):
													if(angle_velocity > -0.014):
														return True
												else:
													return True
						else:
							if(angle <= -0.025):
								if(x_velocity > -0.086):
									if(angle_velocity <= -0.028):
										return True
									else:
										if(x_velocity <= -0.038):
											if(lander_y <= 0.296):
												if(y_velocity <= -0.226):
													if(lander_y <= 0.027):
														if(x_velocity <= -0.061):
															return True
												else:
													return True
							else:
								if(lander_y <= 0.206):
									if(x_velocity <= -0.067):
										if(angle <= -0.017):
											return True
									else:
										if(angle <= -0.02):
											if(lander_y <= 0.081):
												return True
										else:
											return True
								else:
									if(lander_x <= -0.11):
										if(angle <= -0.011):
											if(lander_y <= 0.33):
												return True
										else:
											return True
									else:
										if(angle <= 0.014):
											if(angle_velocity <= -0.008):
												if(angle <= -0.004):
													if(angle_velocity <= -0.026):
														return True
													else:
														if(x_velocity <= -0.063):
															return True
												else:
													if(x_velocity <= 0.003):
														if(x_velocity > -0.027):
															return True
													else:
														if(angle_velocity <= -0.01):
															if(lander_y <= 0.221):
																return True
														else:
															return True
										else:
											if(x_velocity <= 0.042):
												if(lander_y <= 0.363):
													return True
												else:
													if(lander_x <= 0.038):
														return True
					else:
						if(angle_velocity <= 0.107):
							if(angle <= -0.007):
								if(y_velocity <= -0.238):
									if(x_velocity <= -0.137):
										if(angle <= -0.097):
											return True
									else:
										if(angle <= -0.065):
											if(y_velocity <= -0.262):
												return True
											else:
												if(angle_velocity <= 0.04):
													if(lander_y <= 0.308):
														if(x_velocity <= -0.058):
															if(lander_y <= 0.246):
																return True
															else:
																if(lander_y > 0.266):
																	return True
										else:
											if(y_velocity <= -0.245):
												return True
											else:
												if(lander_y <= 0.28):
													return True
												else:
													if(x_velocity <= -0.021):
														if(x_velocity <= -0.031):
															if(lander_y > 0.298):
																if(x_velocity > -0.064):
																	return True
													else:
														if(x_velocity <= 0.033):
															return True
								else:
									if(lander_y <= 0.267):
										if(x_velocity <= -0.063):
											if(lander_y <= 0.141):
												if(lander_x <= -0.028):
													if(y_velocity > -0.223):
														return True
												else:
													if(angle > -0.058):
														if(angle_velocity > -0.002):
															return True
											else:
												if(lander_x > 0.119):
													return True
										else:
											if(angle_velocity <= 0.006):
												if(angle_velocity <= 0.004):
													if(x_velocity <= 0.027):
														if(angle_velocity <= -0.004):
															if(angle_velocity <= -0.005):
																return True
														else:
															return True
												else:
													if(angle <= -0.044):
														return True
											else:
												if(x_velocity <= -0.057):
													if(y_velocity > -0.232):
														return True
												else:
													return True
									else:
										if(lander_x <= -0.085):
											if(x_velocity <= 0.025):
												if(lander_y <= 0.29):
													if(lander_y > 0.275):
														return True
										else:
											if(angle_velocity > 0.001):
												if(x_velocity <= -0.01):
													if(y_velocity <= -0.231):
														if(lander_y > 0.315):
															if(angle <= -0.008):
																return True
												else:
													if(lander_x <= -0.01):
														if(x_velocity <= 0.023):
															return True
														else:
															if(angle_velocity > 0.057):
																return True
													else:
														if(angle_velocity > 0.058):
															return True
							else:
								if(x_velocity <= -0.054):
									if(lander_x > 0.058):
										return True
								else:
									if(y_velocity <= -0.221):
										if(y_velocity <= -0.226):
											return True
										else:
											if(y_velocity > -0.226):
												if(x_velocity <= -0.006):
													if(lander_x > -0.043):
														return True
												else:
													return True
									else:
										if(y_velocity > -0.221):
											return True
						else:
							if(lander_y <= 0.393):
								if(x_velocity <= -0.069):
									return True
							else:
								return True
				else:
					if(y_velocity <= -0.259):
						if(x_velocity <= -0.468):
							if(y_velocity <= -0.601):
								return True
						else:
							if(angle <= -0.053):
								if(y_velocity <= -0.29):
									if(y_velocity <= -0.324):
										if(lander_y <= 1.061):
											if(angle <= -0.202):
												if(y_velocity <= -0.357):
													if(angle_velocity <= 0.039):
														if(y_velocity <= -0.405):
															if(lander_x <= -0.243):
																if(angle_velocity > 0.033):
																	return True
															else:
																if(y_velocity <= -0.424):
																	return True
																else:
																	if(angle <= -0.289):
																		return True
																	else:
																		if(angle > -0.244):
																			return True
													else:
														if(y_velocity <= -0.387):
															if(angle <= -0.315):
																if(y_velocity <= -0.462):
																	if(angle_velocity > 0.056):
																		if(x_velocity <= -0.285):
																			return True
																		else:
																			if(angle_velocity > 0.103):
																				return True
															else:
																if(lander_y <= 1.037):
																	if(x_velocity <= -0.319):
																		if(y_velocity <= -0.414):
																			return True
																	else:
																		if(x_velocity <= -0.093):
																			return True
																		else:
																			if(x_velocity > -0.08):
																				return True
																else:
																	if(angle <= -0.301):
																		return True
														else:
															if(angle <= -0.234):
																if(lander_x <= -0.234):
																	if(y_velocity <= -0.369):
																		if(angle_velocity > 0.079):
																			return True
															else:
																if(lander_y <= 0.983):
																	return True
												else:
													if(angle <= -0.205):
														if(angle_velocity > 0.111):
															if(y_velocity <= -0.341):
																if(x_velocity > -0.16):
																	return True
											else:
												if(y_velocity <= -0.336):
													if(x_velocity <= -0.352):
														if(angle_velocity <= -0.007):
															return True
													else:
														if(angle_velocity <= 0.218):
															if(lander_y <= 1.0):
																return True
															else:
																if(lander_y > 1.002):
																	if(angle_velocity <= -0.006):
																		if(lander_x > -0.08):
																			return True
																	else:
																		if(angle <= -0.152):
																			if(lander_x > -0.187):
																				return True
																		else:
																			if(angle_velocity <= 0.025):
																				if(angle_velocity <= 0.02):
																					return True
																			else:
																				return True
														else:
															if(x_velocity > -0.054):
																return True
												else:
													if(angle <= -0.163):
														if(angle_velocity > 0.039):
															if(angle_velocity <= 0.137):
																if(lander_y <= 0.705):
																	return True
															else:
																if(angle > -0.189):
																	return True
													else:
														if(angle_velocity <= 0.048):
															if(lander_x > -0.105):
																if(angle <= -0.1):
																	if(lander_y <= 0.681):
																		return True
																	else:
																		if(angle <= -0.107):
																			if(lander_x > -0.085):
																				return True
																else:
																	return True
														else:
															return True
										else:
											if(y_velocity <= -0.345):
												if(angle <= -0.145):
													if(y_velocity <= -0.399):
														if(lander_y > 1.064):
															if(angle_velocity <= -0.018):
																if(x_velocity <= -0.299):
																	if(x_velocity > -0.345):
																		if(y_velocity <= -0.413):
																			return True
															else:
																if(lander_y <= 1.317):
																	if(lander_x > -0.194):
																		if(lander_y <= 1.27):
																			return True
																		else:
																			if(lander_y > 1.279):
																				return True
																else:
																	if(angle_velocity > 0.001):
																		if(angle <= -0.227):
																			return True
																		else:
																			if(angle > -0.218):
																				return True
													else:
														if(angle > -0.183):
															if(y_velocity <= -0.364):
																if(angle_velocity > 0.005):
																	if(y_velocity > -0.397):
																		if(angle <= -0.179):
																			if(angle <= -0.181):
																				return True
																		else:
																			return True
															else:
																if(angle_velocity > 0.048):
																	if(x_velocity > -0.14):
																		if(lander_y > 1.117):
																			return True
												else:
													if(y_velocity <= -0.36):
														return True
													else:
														if(y_velocity > -0.357):
															if(lander_y <= 1.321):
																if(y_velocity <= -0.353):
																	if(lander_x > -0.058):
																		return True
																else:
																	return True
											else:
												if(angle <= -0.07):
													if(y_velocity <= -0.333):
														if(x_velocity > -0.158):
															if(lander_y > 1.078):
																if(angle <= -0.075):
																	if(y_velocity <= -0.343):
																		if(angle <= -0.134):
																			return True
																	else:
																		return True
												else:
													if(y_velocity > -0.334):
														return True
									else:
										if(lander_y <= 0.972):
											if(angle <= -0.139):
												if(y_velocity <= -0.313):
													if(angle > -0.167):
														if(angle_velocity > 0.052):
															if(lander_y <= 0.87):
																return True
												else:
													if(angle_velocity <= 0.151):
														if(lander_x <= -0.286):
															if(angle_velocity <= 0.106):
																return True
													else:
														if(y_velocity > -0.304):
															return True
											else:
												if(lander_x <= 0.171):
													if(angle_velocity <= -0.005):
														if(x_velocity <= -0.132):
															if(lander_y <= 0.772):
																return True
														else:
															if(angle > -0.073):
																if(x_velocity > -0.124):
																	return True
													else:
														if(angle <= -0.118):
															if(angle_velocity > 0.035):
																if(angle <= -0.121):
																	if(lander_y > 0.506):
																		if(lander_x <= 0.065):
																			return True
																		else:
																			if(x_velocity > -0.145):
																				return True
														else:
															if(angle <= -0.054):
																if(lander_y <= 0.947):
																	if(y_velocity <= -0.303):
																		if(angle <= -0.059):
																			if(angle <= -0.111):
																				if(lander_y <= 0.726):
																					return True
																			else:
																				return True
																		else:
																			if(angle > -0.058):
																				return True
																	else:
																		if(y_velocity > -0.303):
																			if(angle_velocity <= 0.002):
																				if(lander_y > 0.675):
																					return True
																			else:
																				if(x_velocity <= -0.145):
																					if(angle_velocity <= 0.024):
																						return True
																					else:
																						if(angle <= -0.091):
																							if(angle_velocity > 0.025):
																								return True
																				else:
																					if(lander_y <= 0.891):
																						if(angle_velocity <= 0.017):
																							if(x_velocity <= -0.103):
																								return True
																						else:
																							if(angle <= -0.108):
																								if(x_velocity > -0.106):
																									return True
																							else:
																								return True
																					else:
																						if(y_velocity > -0.298):
																							return True
																else:
																	if(angle_velocity > 0.032):
																		if(lander_x <= -0.092):
																			if(y_velocity <= -0.296):
																				return True
																			else:
																				if(y_velocity > -0.292):
																					return True
										else:
											if(x_velocity <= -0.075):
												if(angle_velocity <= 0.028):
													if(lander_x <= -0.082):
														if(angle > -0.09):
															return True
											else:
												if(y_velocity <= -0.297):
													if(x_velocity <= -0.067):
														return True
													else:
														if(lander_x <= -0.155):
															if(angle_velocity <= 0.104):
																return True
														else:
															if(angle_velocity > 0.087):
																return True
								else:
									if(angle_velocity <= 0.055):
										if(lander_y <= 0.573):
											if(angle <= -0.071):
												if(y_velocity > -0.283):
													if(x_velocity > -0.12):
														if(lander_x <= -0.309):
															return True
											else:
												if(y_velocity <= -0.272):
													return True
												else:
													if(angle_velocity > 0.008):
														if(x_velocity > -0.082):
															return True
										else:
											if(x_velocity <= -0.066):
												if(lander_y <= 0.69):
													if(angle_velocity > 0.034):
														if(lander_y > 0.636):
															if(angle > -0.084):
																return True
									else:
										if(lander_y <= 0.766):
											if(angle <= -0.107):
												if(y_velocity <= -0.283):
													return True
											else:
												if(x_velocity > -0.144):
													if(y_velocity <= -0.271):
														if(angle <= -0.103):
															if(angle <= -0.105):
																return True
														else:
															return True
													else:
														if(lander_y <= 0.583):
															if(lander_y > 0.442):
																return True
										else:
											if(x_velocity > 0.017):
												if(y_velocity <= -0.28):
													return True
							else:
								if(lander_y <= 0.786):
									if(y_velocity <= -0.265):
										if(lander_y <= 0.727):
											if(x_velocity <= -0.116):
												if(x_velocity <= -0.125):
													return True
											else:
												if(angle_velocity <= 0.082):
													if(y_velocity <= -0.266):
														if(y_velocity <= -0.278):
															return True
														else:
															if(y_velocity > -0.278):
																if(x_velocity <= -0.093):
																	if(y_velocity <= -0.27):
																		return True
																else:
																	if(angle_velocity <= 0.004):
																		if(angle_velocity <= 0.003):
																			if(lander_y <= 0.648):
																				return True
																			else:
																				if(angle > -0.035):
																					if(x_velocity <= 0.026):
																						return True
																					else:
																						if(angle_velocity > -0.007):
																							return True
																	else:
																		return True
													else:
														if(y_velocity > -0.266):
															if(lander_x <= 0.098):
																return True
															else:
																if(x_velocity <= -0.039):
																	return True
												else:
													if(angle_velocity > 0.087):
														return True
										else:
											if(lander_y > 0.728):
												if(y_velocity <= -0.27):
													if(angle <= -0.037):
														if(y_velocity <= -0.282):
															if(y_velocity <= -0.291):
																return True
															else:
																if(lander_x <= 0.069):
																	return True
													else:
														if(y_velocity <= -0.275):
															return True
														else:
															if(y_velocity > -0.275):
																return True
												else:
													if(angle_velocity <= -0.004):
														if(y_velocity > -0.268):
															if(y_velocity > -0.268):
																return True
													else:
														if(y_velocity <= -0.269):
															if(lander_y > 0.752):
																return True
														else:
															return True
									else:
										if(angle <= -0.018):
											if(lander_y <= 0.672):
												if(angle <= -0.02):
													if(angle_velocity <= -0.016):
														if(angle_velocity <= -0.025):
															return True
													else:
														if(lander_x <= 0.099):
															if(lander_y <= 0.569):
																return True
															else:
																if(x_velocity > -0.044):
																	return True
														else:
															if(angle_velocity <= 0.024):
																return True
											else:
												if(angle_velocity > 0.031):
													if(x_velocity <= 0.023):
														if(y_velocity > -0.26):
															if(lander_x <= 0.01):
																return True
													else:
														if(angle_velocity <= 0.041):
															return True
										else:
											if(lander_x <= 0.156):
												if(angle <= -0.013):
													if(x_velocity <= 0.042):
														return True
												else:
													if(lander_x <= -0.171):
														if(y_velocity <= -0.26):
															return True
													else:
														return True
											else:
												if(x_velocity > -0.061):
													if(angle > 0.003):
														return True
								else:
									if(y_velocity <= -0.281):
										if(lander_y <= 1.322):
											if(x_velocity <= 0.689):
												if(y_velocity <= -0.292):
													if(lander_y <= 1.13):
														if(lander_y <= 0.793):
															if(lander_x <= 0.046):
																return True
														else:
															if(x_velocity <= -0.11):
																if(y_velocity <= -0.296):
																	return True
															else:
																if(x_velocity <= -0.079):
																	if(x_velocity <= -0.079):
																		return True
																else:
																	return True
													else:
														if(x_velocity <= -0.068):
															if(y_velocity <= -0.336):
																return True
														else:
															if(angle <= 0.033):
																if(y_velocity <= -0.297):
																	if(lander_x <= 0.055):
																		if(y_velocity <= -0.31):
																			if(lander_y > 1.131):
																				if(angle_velocity > -0.029):
																					return True
																		else:
																			if(x_velocity <= -0.025):
																				if(x_velocity <= -0.037):
																					if(y_velocity <= -0.307):
																						return True
																					else:
																						if(lander_y <= 1.162):
																							return True
																				else:
																					return True
																			else:
																				if(angle_velocity > 0.02):
																					return True
															else:
																return True
												else:
													if(angle <= -0.032):
														if(angle_velocity <= 0.032):
															if(lander_y <= 0.825):
																if(lander_y > 0.815):
																	return True
														else:
															if(lander_x <= -0.081):
																return True
													else:
														if(angle_velocity <= -0.014):
															if(angle > -0.0):
																if(lander_x > -0.005):
																	if(x_velocity > -0.103):
																		if(angle <= 0.317):
																			if(angle_velocity > -0.03):
																				return True
														else:
															if(lander_y <= 1.098):
																if(angle <= -0.023):
																	if(angle_velocity > 0.003):
																		return True
																else:
																	if(lander_x <= -0.067):
																		if(lander_y <= 0.938):
																			return True
																	else:
																		return True
															else:
																if(lander_x > -0.014):
																	if(lander_y <= 1.133):
																		if(y_velocity > -0.286):
																			return True
																	else:
																		if(angle <= 0.055):
																			if(x_velocity <= 0.069):
																				return True
																		else:
																			return True
										else:
											if(x_velocity <= 0.337):
												if(angle_velocity <= 0.028):
													if(y_velocity <= -0.309):
														if(lander_x <= 0.0):
															if(angle_velocity <= -0.004):
																return True
															else:
																if(x_velocity > -0.118):
																	if(y_velocity <= -0.326):
																		return True
														else:
															if(angle_velocity > 0.014):
																return True
												else:
													if(x_velocity <= 0.264):
														if(lander_x <= -0.008):
															if(y_velocity <= -0.383):
																return True
														else:
															if(y_velocity <= -0.284):
																if(angle <= 0.002):
																	if(lander_x > -0.002):
																		return True
																else:
																	return True
															else:
																if(lander_x > 0.016):
																	return True
													else:
														if(angle_velocity > 0.225):
															return True
											else:
												if(lander_x > 0.086):
													return True
									else:
										if(angle <= 0.009):
											if(x_velocity <= 0.03):
												if(angle_velocity <= -0.004):
													if(x_velocity > -0.073):
														if(y_velocity <= -0.277):
															if(lander_x <= 0.125):
																if(lander_y <= 1.083):
																	if(lander_x <= 0.051):
																		return True
																	else:
																		if(lander_x > 0.069):
																			return True
														else:
															if(y_velocity <= -0.262):
																if(angle_velocity <= -0.029):
																	return True
																else:
																	if(x_velocity > -0.008):
																		if(x_velocity <= -0.004):
																			return True
															else:
																if(angle > -0.005):
																	return True
												else:
													if(lander_y <= 0.837):
														if(angle > -0.036):
															if(y_velocity <= -0.272):
																return True
															else:
																if(lander_y <= 0.802):
																	return True
													else:
														if(x_velocity <= 0.002):
															if(lander_x <= -0.148):
																if(y_velocity <= -0.272):
																	return True
														else:
															if(angle_velocity <= 0.07):
																if(x_velocity > 0.019):
																	return True
															else:
																if(lander_y > 0.885):
																	if(x_velocity <= 0.023):
																		return True
											else:
												if(lander_y <= 0.884):
													if(angle <= 0.002):
														return True
													else:
														if(lander_y > 0.825):
															return True
										else:
											if(x_velocity <= -0.025):
												if(lander_y <= 0.898):
													return True
												else:
													if(y_velocity <= -0.274):
														if(lander_y <= 1.126):
															return True
											else:
												if(lander_y <= 1.104):
													if(angle_velocity <= -0.008):
														if(lander_x <= -0.007):
															if(lander_y <= 0.883):
																if(lander_x <= -0.025):
																	return True
														else:
															if(angle_velocity <= -0.01):
																return True
													else:
														if(x_velocity <= 0.064):
															return True
														else:
															if(angle_velocity > 0.012):
																return True
												else:
													if(angle <= 0.06):
														if(x_velocity <= 0.077):
															if(angle_velocity <= 0.049):
																if(y_velocity <= -0.277):
																	return True
														else:
															if(angle > 0.045):
																return True
													else:
														if(x_velocity > 0.016):
															if(angle <= 0.594):
																if(angle <= 0.092):
																	if(angle <= 0.089):
																		if(angle_velocity > -0.022):
																			if(x_velocity <= 0.102):
																				if(angle_velocity <= 0.073):
																					return True
																			else:
																				if(angle_velocity > 0.041):
																					return True
																else:
																	if(lander_y <= 1.147):
																		if(lander_x <= 0.174):
																			return True
																	else:
																		return True
															else:
																if(x_velocity > 0.221):
																	return True
					else:
						if(x_velocity <= 0.035):
							if(lander_y <= 0.672):
								if(y_velocity <= -0.242):
									if(angle <= -0.03):
										if(angle_velocity <= 0.012):
											if(y_velocity <= -0.257):
												return True
											else:
												if(x_velocity > -0.096):
													if(lander_y <= 0.634):
														if(lander_x > -0.264):
															if(angle_velocity > -0.0):
																if(angle > -0.038):
																	if(lander_y <= 0.441):
																		return True
										else:
											if(x_velocity > -0.041):
												if(angle_velocity <= 0.063):
													if(lander_y <= 0.581):
														return True
												else:
													if(x_velocity > -0.025):
														if(y_velocity <= -0.255):
															if(lander_x > -0.269):
																return True
									else:
										if(x_velocity <= -0.023):
											if(y_velocity <= -0.251):
												if(x_velocity <= -0.034):
													if(x_velocity > -0.093):
														if(y_velocity <= -0.259):
															if(angle <= -0.023):
																return True
														else:
															if(angle <= -0.027):
																if(x_velocity <= -0.049):
																	return True
															else:
																return True
												else:
													if(y_velocity > -0.255):
														return True
											else:
												if(lander_y <= 0.549):
													if(angle_velocity <= 0.029):
														if(angle <= -0.009):
															if(lander_x <= 0.094):
																if(angle <= -0.021):
																	if(angle_velocity <= -0.012):
																		if(x_velocity > -0.032):
																			return True
																	else:
																		return True
																else:
																	if(lander_y <= 0.44):
																		return True
															else:
																if(angle > -0.01):
																	return True
														else:
															return True
													else:
														if(y_velocity <= -0.248):
															return True
												else:
													if(angle <= -0.001):
														if(y_velocity <= -0.25):
															if(lander_x <= 0.071):
																return True
													else:
														if(angle_velocity > -0.017):
															if(angle <= 0.01):
																return True
										else:
											if(angle <= 0.003):
												if(angle_velocity <= -0.006):
													if(lander_x <= -0.077):
														if(x_velocity <= 0.004):
															return True
														else:
															if(angle_velocity <= -0.021):
																if(y_velocity <= -0.257):
																	return True
															else:
																return True
													else:
														if(y_velocity <= -0.252):
															if(lander_y <= 0.516):
																return True
												else:
													if(y_velocity <= -0.248):
														return True
													else:
														if(lander_x > -0.19):
															if(lander_x <= 0.055):
																if(lander_y <= 0.646):
																	if(angle_velocity <= 0.013):
																		if(x_velocity > 0.007):
																			return True
																	else:
																		return True
											else:
												if(angle_velocity <= 0.051):
													return True
												else:
													if(angle_velocity > 0.052):
														return True
								else:
									if(angle <= 0.027):
										if(angle_velocity <= 0.015):
											if(x_velocity > -0.051):
												if(lander_y <= 0.519):
													if(lander_x <= -0.062):
														if(angle > -0.012):
															if(y_velocity <= -0.233):
																return True
															else:
																if(angle > -0.008):
																	if(angle <= 0.004):
																		if(x_velocity <= 0.01):
																			return True
													else:
														if(angle <= 0.002):
															if(y_velocity <= -0.239):
																if(angle_velocity > -0.01):
																	return True
															else:
																if(angle_velocity > 0.012):
																	if(x_velocity <= -0.014):
																		return True
														else:
															if(x_velocity <= -0.002):
																return True
															else:
																if(x_velocity > 0.007):
																	return True
										else:
											if(y_velocity <= -0.23):
												if(x_velocity <= -0.011):
													if(angle > -0.059):
														if(lander_y <= 0.401):
															return True
												else:
													if(lander_x <= -0.028):
														if(angle_velocity <= 0.059):
															if(lander_y <= 0.434):
																return True
															else:
																if(angle > 0.009):
																	return True
													else:
														if(y_velocity <= -0.237):
															if(lander_x <= 0.039):
																return True
														else:
															return True
									else:
										if(lander_y <= 0.551):
											return True
										else:
											if(lander_y > 0.592):
												return True
							else:
								if(y_velocity <= -0.254):
									if(lander_y <= 0.805):
										if(x_velocity > -0.02):
											if(y_velocity <= -0.259):
												if(lander_y <= 0.709):
													if(angle <= -0.027):
														return True
											else:
												if(angle > -0.035):
													return True
									else:
										if(y_velocity > -0.256):
											if(lander_x <= 0.034):
												if(lander_x > 0.028):
													return True
								else:
									if(angle > -0.028):
										if(angle <= 0.01):
											if(angle <= 0.008):
												if(angle_velocity <= 0.019):
													if(x_velocity > -0.053):
														if(lander_x <= -0.008):
															if(x_velocity > 0.0):
																if(lander_x > -0.129):
																	if(lander_y <= 0.723):
																		return True
												else:
													if(angle_velocity > 0.067):
														if(angle_velocity <= 0.071):
															return True
										else:
											if(lander_y <= 0.698):
												if(y_velocity <= -0.242):
													return True
											else:
												if(y_velocity <= -0.25):
													if(lander_y <= 0.803):
														return True
						else:
							if(lander_y <= 0.649):
								if(angle_velocity <= -0.007):
									if(x_velocity <= 0.055):
										if(angle > -0.012):
											if(lander_x <= 0.036):
												return True
									else:
										if(angle > 0.021):
											if(y_velocity <= -0.229):
												if(lander_x <= -0.09):
													return True
												else:
													if(angle > 0.046):
														return True
											else:
												if(angle_velocity <= -0.029):
													return True
								else:
									if(angle <= 0.013):
										if(y_velocity <= -0.233):
											if(angle_velocity <= 0.009):
												if(x_velocity <= 0.042):
													return True
												else:
													if(y_velocity <= -0.246):
														if(angle > -0.005):
															return True
											else:
												if(lander_x > -0.302):
													if(lander_y <= 0.64):
														return True
													else:
														if(lander_x > -0.134):
															return True
										else:
											if(lander_y <= 0.542):
												if(x_velocity <= 0.092):
													if(x_velocity > 0.048):
														if(angle_velocity > 0.016):
															if(y_velocity <= -0.225):
																return True
									else:
										if(y_velocity <= -0.23):
											if(angle_velocity <= -0.001):
												if(lander_x <= -0.011):
													return True
											else:
												return True
										else:
											if(lander_y <= 0.623):
												if(lander_y <= 0.542):
													return True
												else:
													if(angle > 0.035):
														return True
							else:
								if(angle <= 0.131):
									if(lander_y <= 0.774):
										if(y_velocity <= -0.228):
											if(angle_velocity <= -0.009):
												if(angle > 0.039):
													return True
											else:
												if(angle <= 0.015):
													if(angle_velocity <= 0.075):
														if(y_velocity <= -0.246):
															if(angle_velocity <= 0.054):
																return True
														else:
															if(lander_x > -0.18):
																if(angle_velocity > 0.05):
																	if(lander_y <= 0.713):
																		return True
												else:
													if(x_velocity <= 0.047):
														if(x_velocity <= 0.038):
															return True
													else:
														if(y_velocity <= -0.229):
															if(angle_velocity <= 0.004):
																if(angle <= 0.037):
																	if(y_velocity <= -0.247):
																		return True
																else:
																	return True
															else:
																if(angle_velocity <= 0.06):
																	return True
																else:
																	if(lander_x <= -0.149):
																		return True
										else:
											if(angle_velocity <= 0.026):
												if(lander_y > 0.682):
													if(y_velocity <= -0.224):
														return True
									else:
										if(y_velocity <= -0.248):
											if(angle <= 0.027):
												if(angle_velocity <= 0.045):
													if(lander_y <= 0.78):
														return True
												else:
													if(lander_y <= 0.847):
														if(y_velocity <= -0.251):
															return True
													else:
														if(x_velocity <= 0.043):
															if(lander_y <= 0.972):
																return True
											else:
												if(x_velocity <= 0.069):
													if(lander_y <= 1.081):
														return True
												else:
													if(angle_velocity > 0.014):
														if(lander_y <= 1.385):
															if(angle <= 0.116):
																return True
															else:
																if(lander_y <= 1.356):
																	return True
										else:
											if(lander_y <= 1.382):
												if(angle_velocity <= 0.034):
													if(lander_y <= 0.848):
														if(angle_velocity > 0.015):
															return True
													else:
														if(lander_x > -0.044):
															if(x_velocity > 0.064):
																if(x_velocity <= 0.068):
																	return True
								else:
									if(x_velocity <= 0.294):
										if(angle <= 0.425):
											if(y_velocity <= -0.24):
												if(lander_x > 0.041):
													return True
											else:
												if(x_velocity <= 0.222):
													if(lander_y <= 1.13):
														return True
													else:
														if(angle <= 0.162):
															if(angle > 0.151):
																return True
												else:
													return True
										else:
											if(y_velocity <= -0.254):
												return True
											else:
												if(angle_velocity <= 0.01):
													return True
												else:
													if(x_velocity <= 0.276):
														if(angle_velocity > 0.195):
															if(lander_x > 0.208):
																return True
													else:
														if(y_velocity <= -0.227):
															return True
									else:
										return True
		else:
			if(angle_velocity <= -0.011):
				if(right_leg_contact != True):
					if(angle <= 0.062):
						if(angle_velocity <= -0.036):
							if(x_velocity <= -0.049):
								if(angle <= -0.018):
									if(x_velocity > -0.312):
										if(x_velocity <= -0.051):
											if(x_velocity > -0.097):
												if(y_velocity <= -0.218):
													if(y_velocity > -0.219):
														return True
								else:
									if(y_velocity <= -0.216):
										return True
									else:
										if(lander_x > 0.106):
											if(lander_y <= 0.012):
												return True
							else:
								if(angle_velocity <= -0.052):
									if(angle <= 0.036):
										if(lander_y <= 0.657):
											if(lander_x > 0.046):
												if(lander_x <= 0.046):
													return True
									else:
										if(angle_velocity > -0.07):
											if(angle_velocity <= -0.062):
												return True
											else:
												if(x_velocity > 0.044):
													if(angle > 0.05):
														return True
								else:
									if(lander_x <= -0.175):
										if(y_velocity <= -0.207):
											if(angle > -0.002):
												return True
									else:
										if(x_velocity <= 0.029):
											if(angle <= 0.025):
												if(lander_x <= -0.072):
													if(angle > -0.015):
														if(x_velocity <= 0.008):
															if(lander_y <= 0.132):
																return True
												else:
													if(left_leg_contact != True):
														if(angle <= 0.018):
															if(x_velocity <= -0.034):
																if(angle_velocity > -0.045):
																	if(lander_x <= 0.016):
																		if(lander_y > 0.086):
																			return True
														else:
															if(lander_x <= 0.055):
																if(x_velocity <= -0.004):
																	return True
													else:
														return True
											else:
												if(lander_y <= 0.175):
													if(y_velocity <= -0.186):
														return True
										else:
											if(angle > 0.059):
												return True
						else:
							if(x_velocity <= 0.002):
								if(lander_y <= 0.172):
									if(y_velocity <= -0.197):
										if(angle <= -0.004):
											if(lander_x > -0.161):
												if(x_velocity > -0.078):
													if(angle <= -0.022):
														if(x_velocity <= -0.074):
															return True
													else:
														if(angle <= -0.01):
															if(y_velocity <= -0.212):
																return True
										else:
											if(lander_y <= 0.091):
												return True
											else:
												if(lander_x <= 0.025):
													if(y_velocity <= -0.204):
														return True
												else:
													if(angle_velocity > -0.02):
														return True
								else:
									if(lander_x <= 0.072):
										if(y_velocity > -0.219):
											if(angle_velocity > -0.011):
												return True
							else:
								if(lander_y <= 0.216):
									if(y_velocity <= -0.189):
										if(angle <= 0.005):
											if(angle > -0.01):
												if(x_velocity <= 0.028):
													if(lander_x <= -0.049):
														if(x_velocity > 0.006):
															return True
										else:
											if(x_velocity <= 0.079):
												if(lander_y <= 0.144):
													if(angle <= 0.016):
														if(angle <= 0.015):
															if(lander_x <= -0.022):
																return True
															else:
																if(lander_x > 0.003):
																	return True
													else:
														return True
												else:
													if(lander_x <= -0.027):
														if(lander_y > 0.16):
															if(y_velocity > -0.218):
																return True
													else:
														if(angle_velocity <= -0.031):
															return True
									else:
										if(lander_x <= -0.086):
											if(x_velocity > 0.057):
												if(angle_velocity <= -0.023):
													return True
										else:
											if(angle <= 0.046):
												if(y_velocity <= -0.186):
													if(lander_y <= 0.111):
														return True
											else:
												if(y_velocity <= -0.17):
													if(lander_x <= 0.007):
														return True
								else:
									if(lander_x <= -0.044):
										if(x_velocity <= 0.062):
											if(y_velocity <= -0.21):
												if(angle > 0.003):
													if(lander_y <= 0.439):
														if(lander_x > -0.196):
															if(x_velocity > 0.014):
																return True
										else:
											if(lander_x <= -0.189):
												if(angle_velocity <= -0.024):
													return True
									else:
										if(x_velocity <= 0.01):
											if(x_velocity <= 0.009):
												if(y_velocity <= -0.184):
													return True
										else:
											if(lander_y <= 0.627):
												if(y_velocity <= -0.212):
													if(y_velocity > -0.214):
														return True
					else:
						if(y_velocity <= -0.174):
							if(angle <= 0.082):
								if(angle_velocity <= -0.041):
									if(lander_x > 0.111):
										return True
								else:
									if(lander_x <= -0.061):
										return True
									else:
										if(x_velocity <= 0.067):
											return True
							else:
								if(x_velocity <= 0.157):
									if(angle_velocity <= -0.113):
										if(lander_y > 1.119):
											if(y_velocity <= -0.213):
												if(lander_x <= 0.169):
													return True
											else:
												if(x_velocity > 0.134):
													return True
									else:
										if(lander_y <= 1.054):
											if(y_velocity <= -0.216):
												return True
								else:
									if(angle_velocity <= -0.136):
										if(angle <= 0.323):
											if(y_velocity <= -0.186):
												if(x_velocity <= 0.172):
													if(lander_x <= 0.216):
														return True
											else:
												return True
										else:
											return True
									else:
										if(y_velocity <= -0.192):
											return True
										else:
											if(lander_y <= 1.386):
												if(x_velocity > 0.256):
													if(lander_x > 0.182):
														return True
											else:
												if(angle <= 0.353):
													return True
						else:
							if(lander_y <= 0.324):
								if(x_velocity > 0.133):
									if(angle_velocity > -0.033):
										if(lander_y <= 0.104):
											return True
			else:
				if(lander_y <= 0.246):
					if(y_velocity <= -0.186):
						if(x_velocity <= 0.019):
							if(y_velocity <= -0.204):
								if(x_velocity <= -0.027):
									if(left_leg_contact != True):
										if(angle_velocity <= 0.004):
											if(lander_x > 0.063):
												if(y_velocity <= -0.212):
													return True
									else:
										return True
								else:
									if(lander_y <= 0.187):
										if(lander_x <= -0.131):
											if(y_velocity <= -0.214):
												return True
											else:
												if(left_leg_contact == True):
													return True
										else:
											if(lander_y > 0.002):
												if(angle_velocity <= -0.005):
													if(lander_y <= 0.124):
														return True
												else:
													if(x_velocity <= -0.015):
														if(angle_velocity <= 0.057):
															if(y_velocity <= -0.207):
																return True
													else:
														return True
									else:
										if(lander_x > -0.04):
											if(y_velocity <= -0.211):
												return True
											else:
												if(x_velocity > 0.009):
													return True
							else:
								if(angle_velocity <= -0.005):
									if(angle > -0.001):
										if(angle_velocity > -0.009):
											return True
								else:
									if(lander_y <= 0.004):
										if(y_velocity > -0.199):
											return True
									else:
										if(angle <= 0.019):
											if(x_velocity <= 0.019):
												if(x_velocity > -0.001):
													if(angle_velocity <= 0.014):
														if(y_velocity <= -0.197):
															if(angle > -0.002):
																return True
													else:
														if(lander_y <= 0.011):
															return True
										else:
											if(y_velocity <= -0.192):
												if(lander_x > 0.04):
													return True
						else:
							if(angle <= 0.011):
								if(y_velocity <= -0.201):
									if(angle > -0.031):
										if(angle_velocity <= -0.001):
											if(y_velocity <= -0.21):
												if(angle_velocity <= -0.006):
													return True
										else:
											if(angle <= -0.015):
												if(lander_x <= -0.114):
													if(x_velocity <= 0.083):
														return True
											else:
												if(x_velocity <= 0.059):
													return True
												else:
													if(x_velocity > 0.061):
														return True
								else:
									if(lander_y <= 0.138):
										if(angle > -0.01):
											if(angle_velocity <= -0.005):
												if(lander_x <= -0.081):
													return True
											else:
												if(angle <= -0.004):
													if(angle_velocity <= 0.066):
														if(angle <= -0.009):
															return True
													else:
														return True
												else:
													if(angle_velocity <= 0.069):
														return True
													else:
														if(angle_velocity > 0.243):
															return True
									else:
										if(y_velocity <= -0.196):
											if(x_velocity > 0.059):
												return True
							else:
								if(right_leg_contact != True):
									if(lander_y <= 0.148):
										if(lander_x <= -0.244):
											if(y_velocity <= -0.199):
												return True
										else:
											if(lander_x <= 0.069):
												return True
											else:
												if(lander_x > 0.075):
													return True
									else:
										if(angle_velocity <= -0.004):
											if(lander_x <= -0.148):
												return True
										else:
											if(y_velocity <= -0.2):
												if(angle <= 0.017):
													if(angle <= 0.016):
														return True
												else:
													return True
											else:
												if(angle <= 0.034):
													if(angle_velocity > 0.031):
														if(angle_velocity <= 0.07):
															if(angle_velocity <= 0.046):
																if(angle_velocity <= 0.043):
																	return True
																else:
																	if(y_velocity > -0.188):
																		return True
															else:
																return True
												else:
													if(x_velocity <= 0.055):
														if(x_velocity <= 0.046):
															return True
													else:
														return True
					else:
						if(x_velocity <= 0.079):
							if(left_leg_contact != True):
								if(x_velocity <= 0.053):
									if(angle > -0.01):
										if(lander_y > 0.011):
											if(lander_x <= 0.122):
												if(angle > 0.049):
													if(angle <= 0.05):
														return True
								else:
									if(y_velocity <= -0.171):
										if(lander_x <= -0.036):
											if(angle_velocity <= 0.018):
												if(angle > 0.034):
													return True
										else:
											if(lander_y <= 0.165):
												if(y_velocity <= -0.172):
													if(angle_velocity <= 0.041):
														return True
									else:
										if(angle_velocity <= -0.004):
											if(y_velocity <= -0.16):
												if(angle > 0.049):
													return True
							else:
								if(angle_velocity <= 0.453):
									if(angle <= -0.007):
										return True
						else:
							if(y_velocity <= -0.164):
								if(angle_velocity > -0.007):
									if(angle_velocity <= 0.078):
										if(lander_y <= 0.149):
											if(lander_y > -0.005):
												if(angle <= 0.049):
													if(angle <= 0.047):
														if(x_velocity <= 0.096):
															return True
														else:
															if(angle_velocity <= 0.046):
																if(lander_x > -0.068):
																	return True
															else:
																if(angle_velocity > 0.049):
																	if(y_velocity <= -0.172):
																		return True
																	else:
																		if(lander_x > -0.237):
																			return True
												else:
													return True
										else:
											if(y_velocity <= -0.172):
												if(angle > 0.039):
													return True
							else:
								if(x_velocity > 0.082):
									if(x_velocity > 0.146):
										if(y_velocity <= -0.142):
											if(lander_y <= 0.049):
												if(y_velocity <= -0.146):
													return True
				else:
					if(x_velocity <= 0.09):
						if(y_velocity <= -0.21):
							if(x_velocity <= 0.014):
								if(angle_velocity <= -0.0):
									if(lander_x <= -0.002):
										if(angle > 0.001):
											return True
								else:
									if(y_velocity <= -0.218):
										if(lander_y <= 0.313):
											if(angle > -0.009):
												return True
									else:
										if(x_velocity > -0.006):
											if(x_velocity > -0.004):
												if(lander_y <= 0.301):
													if(y_velocity > -0.215):
														return True
							else:
								if(lander_y <= 0.419):
									if(angle <= -0.001):
										if(angle > -0.016):
											if(angle_velocity > 0.046):
												if(lander_y <= 0.307):
													return True
									else:
										if(angle_velocity <= 0.001):
											if(x_velocity <= 0.051):
												if(lander_y <= 0.374):
													return True
										else:
											if(y_velocity <= -0.211):
												return True
											else:
												if(angle_velocity > 0.027):
													return True
								else:
									if(lander_x <= 0.03):
										if(y_velocity <= -0.211):
											if(angle > -0.012):
												if(y_velocity <= -0.216):
													if(lander_y <= 0.495):
														return True
													else:
														if(x_velocity > 0.078):
															if(lander_x > -0.167):
																return True
									else:
										if(lander_y <= 0.556):
											return True
						else:
							if(x_velocity <= 0.071):
								if(lander_y <= 0.332):
									if(y_velocity <= -0.201):
										if(angle <= 0.018):
											if(lander_x > -0.041):
												if(x_velocity > 0.013):
													if(lander_y <= 0.304):
														if(lander_x <= 0.079):
															return True
										else:
											if(angle <= 0.024):
												if(angle <= 0.021):
													return True
											else:
												return True
									else:
										if(angle_velocity > -0.009):
											if(lander_x > 0.082):
												if(lander_x <= 0.082):
													return True
							else:
								if(angle_velocity > 0.007):
									if(lander_x > -0.087):
										if(angle <= 0.051):
											if(angle > 0.047):
												return True
					else:
						if(y_velocity <= -0.173):
							if(x_velocity <= 0.385):
								if(angle_velocity <= 0.08):
									if(lander_y <= 0.467):
										if(angle <= 0.054):
											if(y_velocity <= -0.186):
												if(lander_x <= -0.247):
													if(angle_velocity > 0.005):
														if(lander_y <= 0.436):
															if(angle_velocity <= 0.049):
																return True
															else:
																if(angle > 0.026):
																	return True
										else:
											if(x_velocity <= 0.175):
												return True
											else:
												if(angle_velocity > 0.026):
													return True
									else:
										if(x_velocity <= 0.262):
											if(lander_y <= 0.677):
												if(y_velocity <= -0.202):
													if(angle > 0.052):
														return True
										else:
											if(y_velocity <= -0.182):
												return True
											else:
												if(x_velocity > 0.338):
													return True
								else:
									if(lander_y <= 1.385):
										if(y_velocity <= -0.215):
											if(angle_velocity <= 0.234):
												if(x_velocity > 0.142):
													if(angle <= 0.271):
														if(x_velocity <= 0.166):
															if(lander_x <= -0.098):
																return True
														else:
															return True
													else:
														if(lander_y <= 1.162):
															return True
										else:
											if(y_velocity <= -0.209):
												if(lander_y > 0.577):
													if(y_velocity <= -0.21):
														if(angle_velocity > 0.283):
															if(x_velocity > 0.307):
																return True
													else:
														return True
											else:
												if(lander_y <= 0.464):
													if(lander_y > 0.448):
														return True
									else:
										if(angle_velocity <= 0.127):
											return True
							else:
								if(angle > 0.153):
									if(angle <= 0.387):
										return True
									else:
										if(x_velocity <= 0.427):
											if(y_velocity <= -0.206):
												return True
										else:
											if(angle_velocity <= 0.382):
												return True
						else:
							if(x_velocity <= 0.541):
								if(lander_y <= 1.487):
									if(angle > 0.024):
										if(x_velocity <= 0.521):
											if(lander_y > 1.465):
												if(y_velocity <= -0.163):
													return True
										else:
											if(y_velocity <= -0.154):
												return True
								else:
									if(x_velocity > 0.446):
										return True
							else:
								if(lander_x > 0.119):
									return True
	else:
		if(y_velocity <= -0.0):
			if(angle <= 0.102):
				if(lander_y <= 0.046):
					if(angle_velocity <= 0.481):
						if(right_leg_contact != True):
							if(angle_velocity > 0.145):
								if(lander_y <= -0.013):
									return True
	return False

def weShould_right_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.137):
		if(y_velocity <= -0.22):
			if(angle_velocity <= -0.03):
				if(angle <= 0.195):
					if(lander_y <= 1.341):
						if(y_velocity <= -0.271):
							if(angle <= 0.061):
								if(y_velocity <= -0.474):
									if(x_velocity <= -0.594):
										if(y_velocity > -0.574):
											return True
									else:
										if(angle > -0.289):
											if(angle <= -0.031):
												if(lander_x > -0.15):
													if(angle > -0.065):
														if(angle <= -0.061):
															return True
														else:
															if(y_velocity > -0.499):
																if(x_velocity <= -0.474):
																	return True
											else:
												if(y_velocity <= -0.546):
													if(x_velocity <= -0.57):
														return True
													else:
														if(x_velocity <= -0.557):
															if(lander_y <= 1.301):
																return True
												else:
													return True
								else:
									if(angle_velocity <= -0.087):
										if(y_velocity <= -0.343):
											if(angle > -0.183):
												if(x_velocity <= -0.49):
													if(angle_velocity > -0.36):
														return True
												else:
													if(angle_velocity <= -0.33):
														if(angle <= 0.018):
															if(x_velocity > -0.486):
																if(angle_velocity > -0.334):
																	if(angle_velocity <= -0.333):
																		return True
													else:
														if(y_velocity <= -0.422):
															if(lander_y > 0.898):
																if(x_velocity <= -0.305):
																	if(x_velocity <= -0.474):
																		if(lander_y > 1.122):
																			return True
														else:
															if(angle <= -0.093):
																if(lander_y > 0.896):
																	if(x_velocity <= -0.414):
																		return True
																	else:
																		if(angle > -0.113):
																			if(angle_velocity <= -0.126):
																				if(lander_x <= -0.053):
																					return True
																				else:
																					if(lander_y > 1.308):
																						if(y_velocity <= -0.376):
																							return True
															else:
																if(x_velocity <= -0.149):
																	if(angle_velocity > -0.253):
																		if(x_velocity <= -0.253):
																			if(y_velocity <= -0.371):
																				if(x_velocity <= -0.327):
																					if(angle_velocity > -0.24):
																						return True
										else:
											if(y_velocity <= -0.289):
												if(angle <= 0.006):
													if(lander_y <= 1.317):
														if(lander_y <= 0.847):
															if(lander_y > 0.793):
																if(x_velocity <= -0.217):
																	if(x_velocity <= -0.229):
																		if(y_velocity > -0.316):
																			if(lander_y <= 0.804):
																				return True
														else:
															if(angle_velocity > -0.095):
																if(angle_velocity > -0.093):
																	if(lander_x > 0.199):
																		return True
													else:
														return True
											else:
												if(angle_velocity > -0.093):
													return True
									else:
										if(y_velocity <= -0.295):
											if(angle <= -0.072):
												if(y_velocity <= -0.349):
													if(y_velocity > -0.442):
														if(angle > -0.226):
															if(x_velocity <= -0.158):
																if(angle <= -0.121):
																	if(y_velocity > -0.403):
																		if(y_velocity > -0.384):
																			if(angle <= -0.159):
																				if(angle <= -0.199):
																					if(y_velocity > -0.38):
																						return True
																			else:
																				if(y_velocity > -0.375):
																					if(lander_x <= 0.134):
																						return True
												else:
													if(lander_x > 0.147):
														if(x_velocity <= -0.206):
															if(lander_x <= 0.154):
																if(angle <= -0.11):
																	return True
															else:
																if(angle_velocity > -0.044):
																	return True
											else:
												if(lander_x <= -0.007):
													if(y_velocity <= -0.321):
														if(lander_x <= -0.031):
															if(angle_velocity <= -0.054):
																if(y_velocity > -0.422):
																	return True
														else:
															if(x_velocity <= -0.288):
																return True
															else:
																if(y_velocity > -0.334):
																	if(lander_x <= -0.021):
																		return True
												else:
													if(lander_y <= 1.295):
														if(angle <= -0.036):
															if(y_velocity > -0.31):
																if(x_velocity <= -0.18):
																	return True
														else:
															if(x_velocity <= -0.151):
																if(y_velocity > -0.311):
																	return True
										else:
											if(lander_y > 0.656):
												if(angle <= 0.005):
													if(x_velocity <= -0.102):
														if(lander_y <= 0.895):
															if(lander_x <= 0.045):
																return True
														else:
															return True
												else:
													if(lander_y > 0.925):
														if(x_velocity <= -0.082):
															if(y_velocity > -0.292):
																return True
														else:
															if(lander_y <= 1.099):
																if(angle_velocity <= -0.047):
																	if(x_velocity <= -0.034):
																		if(angle_velocity <= -0.054):
																			if(y_velocity > -0.285):
																				if(angle > 0.025):
																					if(angle_velocity <= -0.075):
																						if(lander_y <= 1.052):
																							return True
							else:
								if(angle_velocity <= -0.093):
									if(angle_velocity <= -0.424):
										if(y_velocity > -0.339):
											if(lander_x > 0.254):
												if(angle <= 0.176):
													return True
								else:
									if(x_velocity <= -0.081):
										return True
						else:
							if(lander_y <= 0.289):
								if(angle_velocity <= -0.062):
									if(y_velocity > -0.245):
										if(angle <= 0.017):
											if(lander_y > 0.015):
												if(y_velocity > -0.221):
													return True
								else:
									if(y_velocity <= -0.229):
										if(y_velocity > -0.249):
											if(angle <= -0.051):
												if(lander_x > -0.156):
													if(angle > -0.054):
														return True
									else:
										if(angle <= -0.019):
											if(lander_x <= -0.192):
												return True
											else:
												if(lander_y > 0.225):
													return True
							else:
								if(angle <= -0.004):
									if(angle_velocity <= -0.041):
										if(y_velocity <= -0.258):
											if(y_velocity <= -0.26):
												if(x_velocity > -0.078):
													if(lander_y > 0.704):
														return True
										else:
											if(y_velocity > -0.225):
												if(lander_y <= 0.347):
													return True
									else:
										if(x_velocity <= -0.095):
											return True
										else:
											if(lander_y <= 0.428):
												if(y_velocity <= -0.235):
													if(angle <= -0.011):
														if(x_velocity <= -0.015):
															if(x_velocity > -0.085):
																if(y_velocity > -0.238):
																	return True
											else:
												if(angle_velocity <= -0.041):
													if(lander_y > 0.467):
														return True
								else:
									if(lander_y <= 0.552):
										if(y_velocity > -0.249):
											if(angle_velocity > -0.057):
												if(y_velocity > -0.233):
													if(x_velocity <= -0.025):
														return True
									else:
										if(x_velocity <= -0.043):
											if(lander_x <= 0.126):
												if(lander_y <= 0.699):
													if(angle <= -0.0):
														return True
												else:
													if(angle <= 0.013):
														if(angle_velocity <= -0.054):
															if(x_velocity <= -0.087):
																return True
														else:
															return True
													else:
														return True
											else:
												if(y_velocity <= -0.247):
													if(x_velocity <= -0.063):
														if(angle <= 0.174):
															if(angle_velocity <= -0.043):
																if(x_velocity <= -0.249):
																	return True
															else:
																if(angle > 0.015):
																	return True
													else:
														if(y_velocity > -0.266):
															return True
												else:
													if(lander_x > 0.13):
														return True
										else:
											if(angle <= 0.051):
												if(angle_velocity <= -0.036):
													if(x_velocity <= 0.002):
														if(angle_velocity > -0.057):
															if(lander_y <= 0.705):
																if(angle <= 0.014):
																	if(angle_velocity > -0.042):
																		return True
															else:
																if(lander_y > 0.876):
																	if(x_velocity <= -0.004):
																		return True
												else:
													if(y_velocity > -0.257):
														if(lander_x <= 0.03):
															if(angle <= 0.032):
																if(x_velocity <= -0.012):
																	return True
														else:
															return True
											else:
												if(y_velocity <= -0.254):
													if(angle <= 0.104):
														if(angle_velocity > -0.088):
															if(x_velocity <= 0.003):
																if(lander_y <= 1.057):
																	if(angle <= 0.074):
																		return True
																else:
																	return True
												else:
													if(angle_velocity <= -0.096):
														if(y_velocity <= -0.229):
															if(angle_velocity > -0.138):
																if(angle > 0.113):
																	if(x_velocity <= 0.018):
																		return True
														else:
															if(x_velocity <= 0.039):
																return True
													else:
														if(x_velocity <= 0.025):
															if(lander_y > 0.896):
																if(lander_y <= 0.925):
																	if(lander_x <= 0.145):
																		return True
																else:
																	if(angle_velocity <= -0.085):
																		if(angle_velocity <= -0.09):
																			return True
																	else:
																		return True
														else:
															if(angle <= 0.122):
																if(lander_x > -0.014):
																	if(y_velocity <= -0.253):
																		if(angle_velocity > -0.067):
																			return True
															else:
																if(x_velocity <= 0.084):
																	if(y_velocity <= -0.247):
																		if(lander_y > 1.207):
																			return True
																	else:
																		if(lander_y <= 1.059):
																			if(lander_x > 0.143):
																				return True
																		else:
																			return True
					else:
						if(x_velocity <= -0.327):
							if(y_velocity <= -0.424):
								if(angle <= 0.01):
									if(lander_y <= 1.343):
										return True
								else:
									return True
							else:
								return True
						else:
							if(angle <= -0.004):
								if(y_velocity <= -0.351):
									if(lander_y > 1.373):
										if(x_velocity <= -0.314):
											if(lander_y <= 1.406):
												return True
								else:
									if(lander_y <= 1.365):
										return True
									else:
										if(x_velocity <= -0.183):
											if(angle <= -0.033):
												if(angle_velocity > -0.112):
													if(x_velocity > -0.322):
														if(y_velocity <= -0.3):
															if(angle_velocity > -0.064):
																return True
														else:
															return True
											else:
												return True
							else:
								if(y_velocity > -0.241):
									if(lander_x <= 0.088):
										return True
				else:
					if(angle <= 0.263):
						if(lander_y <= 0.785):
							return True
						else:
							if(lander_x > 0.116):
								if(x_velocity <= -0.187):
									if(y_velocity > -0.303):
										if(lander_x > 0.23):
											return True
					else:
						if(y_velocity <= -0.291):
							if(x_velocity <= -0.002):
								if(angle_velocity <= -0.19):
									if(lander_y <= 1.111):
										if(x_velocity <= -0.253):
											return True
										else:
											if(lander_x > 0.283):
												if(y_velocity > -0.342):
													return True
									else:
										if(y_velocity <= -0.313):
											if(x_velocity <= -0.086):
												if(angle_velocity <= -0.313):
													if(lander_y <= 1.117):
														return True
													else:
														if(y_velocity > -0.321):
															return True
												else:
													return True
										else:
											if(x_velocity <= -0.015):
												return True
								else:
									return True
							else:
								if(lander_x > 0.298):
									if(lander_y > 1.194):
										return True
						else:
							if(angle <= 0.332):
								if(x_velocity <= -0.113):
									return True
								else:
									if(angle <= 0.285):
										if(x_velocity <= 0.106):
											return True
							else:
								if(x_velocity <= 0.01):
									return True
								else:
									if(lander_y <= 1.04):
										if(y_velocity <= -0.258):
											if(angle > 0.512):
												return True
										else:
											if(x_velocity <= 0.12):
												return True
									else:
										if(x_velocity <= 0.185):
											return True
			else:
				if(lander_y <= 0.399):
					if(angle_velocity <= -0.006):
						if(y_velocity <= -0.237):
							if(angle <= -0.04):
								if(lander_y <= 0.175):
									if(y_velocity > -0.245):
										if(lander_x <= 0.025):
											if(lander_y > 0.059):
												return True
								else:
									if(y_velocity > -0.256):
										if(x_velocity <= -0.079):
											if(angle > -0.081):
												return True
										else:
											if(lander_y > 0.377):
												return True
						else:
							if(angle <= -0.025):
								if(x_velocity <= -0.086):
									if(angle > -0.049):
										return True
								else:
									if(angle_velocity > -0.028):
										if(x_velocity <= -0.038):
											if(lander_y > 0.296):
												return True
							else:
								if(lander_y <= 0.206):
									if(x_velocity <= -0.067):
										if(angle > -0.017):
											return True
								else:
									if(lander_x > -0.11):
										if(angle <= 0.014):
											if(angle_velocity > -0.008):
												if(y_velocity > -0.23):
													return True
					else:
						if(angle_velocity <= 0.107):
							if(angle <= -0.007):
								if(y_velocity <= -0.238):
									if(x_velocity <= -0.137):
										if(angle > -0.097):
											return True
									else:
										if(angle <= -0.065):
											if(y_velocity > -0.262):
												if(angle_velocity > 0.04):
													return True
										else:
											if(y_velocity > -0.245):
												if(lander_y > 0.28):
													if(x_velocity <= -0.021):
														if(x_velocity <= -0.031):
															if(lander_y <= 0.298):
																if(angle <= -0.038):
																	return True
															else:
																if(x_velocity <= -0.064):
																	return True
								else:
									if(lander_y <= 0.267):
										if(x_velocity <= -0.063):
											if(lander_y <= 0.141):
												if(lander_x <= -0.028):
													if(y_velocity <= -0.223):
														return True
												else:
													if(angle <= -0.058):
														return True
													else:
														if(angle_velocity <= -0.002):
															return True
											else:
												if(lander_x <= 0.119):
													return True
										else:
											if(angle_velocity > 0.006):
												if(x_velocity <= -0.057):
													if(y_velocity <= -0.232):
														return True
									else:
										if(lander_x <= -0.085):
											if(x_velocity <= 0.025):
												if(lander_y <= 0.29):
													if(lander_y <= 0.275):
														return True
												else:
													return True
										else:
											if(angle_velocity > 0.001):
												if(x_velocity <= -0.01):
													if(y_velocity <= -0.231):
														if(lander_y <= 0.315):
															return True
														else:
															if(angle > -0.008):
																return True
													else:
														if(angle_velocity <= 0.05):
															if(angle > -0.082):
																return True
							else:
								if(x_velocity <= -0.054):
									if(lander_x <= 0.058):
										return True
								else:
									if(y_velocity <= -0.221):
										if(y_velocity > -0.226):
											if(y_velocity > -0.226):
												if(x_velocity <= -0.006):
													if(lander_x <= -0.043):
														return True
									else:
										if(y_velocity <= -0.221):
											return True
						else:
							if(lander_y <= 0.393):
								if(x_velocity > -0.069):
									return True
				else:
					if(y_velocity <= -0.259):
						if(x_velocity <= -0.468):
							if(y_velocity > -0.601):
								return True
						else:
							if(angle <= -0.053):
								if(y_velocity <= -0.29):
									if(y_velocity <= -0.324):
										if(lander_y <= 1.061):
											if(angle <= -0.202):
												if(y_velocity <= -0.357):
													if(angle_velocity > 0.039):
														if(y_velocity <= -0.387):
															if(angle > -0.315):
																if(lander_y <= 1.037):
																	if(x_velocity <= -0.319):
																		if(y_velocity > -0.414):
																			return True
														else:
															if(angle <= -0.234):
																if(lander_x > -0.234):
																	if(y_velocity > -0.378):
																		return True
												else:
													if(angle <= -0.205):
														if(angle_velocity > 0.111):
															if(y_velocity <= -0.341):
																if(x_velocity <= -0.16):
																	return True
													else:
														return True
											else:
												if(y_velocity <= -0.336):
													if(x_velocity <= -0.352):
														if(angle_velocity > -0.007):
															return True
													else:
														if(angle_velocity > 0.218):
															if(x_velocity <= -0.054):
																return True
												else:
													if(angle <= -0.163):
														if(angle_velocity <= 0.039):
															return True
														else:
															if(angle_velocity > 0.137):
																if(angle <= -0.189):
																	return True
													else:
														if(angle_velocity <= 0.048):
															if(lander_x > -0.105):
																if(angle <= -0.1):
																	if(lander_y > 0.681):
																		if(angle <= -0.107):
																			if(lander_x <= -0.085):
																				return True
										else:
											if(y_velocity <= -0.345):
												if(angle <= -0.145):
													if(y_velocity <= -0.399):
														if(lander_y > 1.064):
															if(angle_velocity <= -0.018):
																if(x_velocity <= -0.299):
																	if(x_velocity > -0.345):
																		if(y_velocity > -0.413):
																			return True
															else:
																if(lander_y <= 1.317):
																	if(lander_x > -0.194):
																		if(lander_y > 1.27):
																			if(lander_y <= 1.279):
																				if(y_velocity > -0.407):
																					return True
																else:
																	if(angle_velocity > 0.001):
																		if(angle > -0.227):
																			if(angle <= -0.218):
																				return True
													else:
														if(angle <= -0.183):
															if(angle_velocity <= 0.048):
																if(lander_x <= -0.162):
																	if(lander_x > -0.171):
																		return True
															else:
																if(lander_y > 1.142):
																	return True
														else:
															if(y_velocity <= -0.364):
																if(angle_velocity <= 0.005):
																	if(y_velocity <= -0.382):
																		return True
															else:
																if(angle_velocity > 0.048):
																	if(x_velocity <= -0.14):
																		return True
												else:
													if(y_velocity > -0.36):
														if(y_velocity <= -0.357):
															if(y_velocity > -0.357):
																return True
											else:
												if(angle <= -0.07):
													if(y_velocity <= -0.333):
														if(x_velocity <= -0.158):
															if(lander_y > 1.144):
																return True
													else:
														if(angle_velocity > -0.011):
															return True
									else:
										if(lander_y <= 0.972):
											if(angle <= -0.139):
												if(y_velocity <= -0.313):
													if(angle <= -0.167):
														if(lander_x > -0.283):
															return True
													else:
														if(angle_velocity > 0.052):
															if(lander_y > 0.87):
																return True
												else:
													if(angle_velocity <= 0.151):
														if(lander_x <= -0.286):
															if(angle_velocity > 0.106):
																return True
														else:
															if(lander_y <= 0.654):
																if(y_velocity > -0.311):
																	if(x_velocity <= -0.16):
																		return True
																	else:
																		if(lander_y > 0.645):
																			return True
													else:
														if(y_velocity <= -0.304):
															return True
											else:
												if(lander_x <= 0.171):
													if(angle_velocity <= -0.005):
														if(x_velocity <= -0.132):
															if(lander_y > 0.772):
																return True
													else:
														if(angle <= -0.118):
															if(angle_velocity > 0.035):
																if(angle <= -0.121):
																	if(lander_y > 0.506):
																		if(lander_x > 0.065):
																			if(x_velocity <= -0.145):
																				return True
																else:
																	if(y_velocity > -0.303):
																		return True
														else:
															if(angle <= -0.054):
																if(lander_y <= 0.947):
																	if(y_velocity > -0.303):
																		if(y_velocity <= -0.303):
																			return True
																		else:
																			if(angle_velocity > 0.002):
																				if(x_velocity <= -0.145):
																					if(angle_velocity > 0.024):
																						if(angle <= -0.091):
																							if(angle_velocity <= 0.025):
																								return True
																						else:
																							return True
																else:
																	if(angle_velocity > 0.032):
																		if(lander_x <= -0.092):
																			if(y_velocity > -0.296):
																				if(y_velocity <= -0.292):
																					return True
																		else:
																			return True
												else:
													if(angle > -0.112):
														return True
										else:
											if(x_velocity <= -0.075):
												if(angle_velocity <= 0.028):
													if(lander_x > -0.082):
														if(y_velocity <= -0.312):
															return True
														else:
															if(lander_y <= 1.083):
																return True
												else:
													if(angle <= -0.131):
														if(lander_x <= -0.165):
															return True
													else:
														if(lander_x <= -0.123):
															if(lander_y <= 1.071):
																return True
														else:
															return True
											else:
												if(y_velocity > -0.297):
													return True
								else:
									if(angle_velocity <= 0.055):
										if(lander_y <= 0.573):
											if(angle <= -0.071):
												if(y_velocity > -0.283):
													if(x_velocity <= -0.12):
														return True
													else:
														if(lander_x > -0.309):
															if(y_velocity > -0.262):
																return True
											else:
												if(y_velocity > -0.272):
													if(angle_velocity > 0.008):
														if(x_velocity <= -0.082):
															return True
										else:
											if(x_velocity <= -0.066):
												if(lander_y <= 0.69):
													if(angle_velocity > 0.034):
														if(lander_y <= 0.636):
															return True
												else:
													if(y_velocity <= -0.271):
														if(lander_y <= 1.013):
															if(x_velocity <= -0.068):
																return True
															else:
																if(lander_y > 0.921):
																	return True
											else:
												if(y_velocity <= -0.288):
													if(x_velocity <= -0.026):
														return True
									else:
										if(lander_y <= 0.766):
											if(angle <= -0.107):
												if(y_velocity > -0.283):
													if(y_velocity <= -0.274):
														if(lander_x > -0.27):
															return True
													else:
														return True
											else:
												if(x_velocity <= -0.144):
													return True
												else:
													if(y_velocity > -0.271):
														if(lander_y <= 0.583):
															if(lander_y <= 0.442):
																if(x_velocity <= -0.079):
																	return True
														else:
															return True
										else:
											if(x_velocity <= 0.017):
												if(y_velocity <= -0.267):
													return True
												else:
													if(y_velocity > -0.263):
														return True
											else:
												if(y_velocity > -0.28):
													if(angle_velocity > 0.111):
														return True
							else:
								if(lander_y <= 0.786):
									if(y_velocity <= -0.265):
										if(lander_y <= 0.727):
											if(x_velocity <= -0.116):
												if(x_velocity > -0.125):
													return True
											else:
												if(angle_velocity <= 0.082):
													if(y_velocity <= -0.266):
														if(y_velocity > -0.278):
															if(y_velocity > -0.278):
																if(x_velocity <= -0.093):
																	if(y_velocity > -0.27):
																		return True
												else:
													if(angle_velocity <= 0.087):
														return True
										else:
											if(lander_y <= 0.728):
												if(lander_x > -0.015):
													return True
											else:
												if(y_velocity <= -0.27):
													if(angle <= -0.037):
														if(y_velocity > -0.282):
															if(angle_velocity > -0.005):
																return True
												else:
													if(angle_velocity <= -0.004):
														if(y_velocity > -0.268):
															if(y_velocity <= -0.268):
																return True
													else:
														if(y_velocity <= -0.269):
															if(lander_y <= 0.752):
																return True
									else:
										if(angle <= -0.018):
											if(lander_y <= 0.672):
												if(angle <= -0.02):
													if(angle_velocity > -0.016):
														if(lander_x > 0.099):
															if(angle_velocity > 0.024):
																return True
											else:
												if(angle_velocity <= 0.031):
													if(y_velocity <= -0.264):
														return True
												else:
													if(x_velocity <= 0.023):
														if(y_velocity <= -0.26):
															return True
														else:
															if(lander_x > 0.01):
																return True
										else:
											if(lander_x > 0.156):
												if(x_velocity <= -0.061):
													return True
								else:
									if(y_velocity <= -0.281):
										if(lander_y <= 1.322):
											if(x_velocity <= 0.689):
												if(y_velocity <= -0.292):
													if(lander_y <= 1.13):
														if(lander_y > 0.793):
															if(x_velocity <= -0.11):
																if(y_velocity > -0.296):
																	return True
															else:
																if(x_velocity <= -0.079):
																	if(x_velocity > -0.079):
																		return True
													else:
														if(x_velocity <= -0.068):
															if(y_velocity > -0.336):
																return True
														else:
															if(angle <= 0.033):
																if(y_velocity <= -0.297):
																	if(lander_x <= 0.055):
																		if(y_velocity > -0.31):
																			if(x_velocity <= -0.025):
																				if(x_velocity <= -0.037):
																					if(y_velocity > -0.307):
																						if(lander_y > 1.162):
																							return True
																else:
																	return True
												else:
													if(angle <= -0.032):
														if(angle_velocity <= 0.032):
															if(lander_y <= 0.825):
																if(lander_y <= 0.815):
																	return True
														else:
															if(lander_x > -0.081):
																return True
													else:
														if(angle_velocity <= -0.014):
															if(angle > -0.0):
																if(lander_x <= -0.005):
																	return True
																else:
																	if(x_velocity <= -0.103):
																		return True
																	else:
																		if(angle <= 0.317):
																			if(angle_velocity <= -0.03):
																				return True
																		else:
																			return True
														else:
															if(lander_y <= 1.098):
																if(angle > -0.023):
																	if(lander_x <= -0.067):
																		if(lander_y > 0.938):
																			if(lander_x <= -0.069):
																				return True
															else:
																if(lander_x <= -0.014):
																	if(lander_x > -0.047):
																		return True
										else:
											if(x_velocity <= 0.337):
												if(angle_velocity <= 0.028):
													if(y_velocity <= -0.309):
														if(lander_x <= 0.0):
															if(angle_velocity > -0.004):
																if(x_velocity <= -0.118):
																	return True
																else:
																	if(y_velocity > -0.326):
																		return True
													else:
														if(x_velocity <= -0.025):
															if(angle > -0.007):
																return True
												else:
													if(x_velocity <= 0.264):
														if(lander_x <= -0.008):
															if(y_velocity > -0.383):
																return True
														else:
															if(y_velocity <= -0.284):
																if(angle <= 0.002):
																	if(lander_x <= -0.002):
																		return True
									else:
										if(angle <= 0.009):
											if(x_velocity <= 0.03):
												if(angle_velocity <= -0.004):
													if(x_velocity <= -0.073):
														if(angle > -0.039):
															return True
													else:
														if(y_velocity > -0.277):
															if(y_velocity > -0.262):
																if(angle <= -0.005):
																	return True
												else:
													if(lander_y <= 0.837):
														if(angle <= -0.036):
															return True
														else:
															if(y_velocity > -0.272):
																if(lander_y > 0.802):
																	return True
													else:
														if(x_velocity <= 0.002):
															if(lander_x <= -0.148):
																if(y_velocity > -0.272):
																	return True
															else:
																if(lander_x <= 0.034):
																	return True
																else:
																	if(lander_x > 0.035):
																		return True
														else:
															if(angle_velocity > 0.07):
																if(lander_y <= 0.885):
																	return True
																else:
																	if(x_velocity > 0.023):
																		return True
											else:
												if(lander_y > 0.884):
													if(x_velocity <= 0.044):
														return True
										else:
											if(x_velocity <= -0.025):
												if(lander_y > 0.898):
													if(y_velocity <= -0.274):
														if(lander_y > 1.126):
															return True
													else:
														return True
											else:
												if(lander_y > 1.104):
													if(angle <= 0.06):
														if(x_velocity <= 0.077):
															if(angle_velocity > 0.049):
																return True
													else:
														if(x_velocity <= 0.016):
															return True
														else:
															if(angle <= 0.594):
																if(angle <= 0.092):
																	if(angle <= 0.089):
																		if(angle_velocity > -0.022):
																			if(x_velocity <= 0.102):
																				if(angle_velocity > 0.073):
																					return True
																	else:
																		if(angle_velocity > -0.008):
																			return True
																else:
																	if(lander_y <= 1.147):
																		if(lander_x > 0.174):
																			return True
															else:
																if(x_velocity <= 0.221):
																	return True
					else:
						if(x_velocity <= 0.035):
							if(lander_y <= 0.672):
								if(y_velocity <= -0.242):
									if(angle <= -0.03):
										if(angle_velocity <= 0.012):
											if(y_velocity > -0.257):
												if(x_velocity <= -0.096):
													return True
												else:
													if(lander_y <= 0.634):
														if(lander_x <= -0.264):
															return True
														else:
															if(angle_velocity > -0.0):
																if(angle > -0.038):
																	if(lander_y > 0.441):
																		if(angle_velocity <= 0.011):
																			return True
													else:
														return True
										else:
											if(x_velocity <= -0.041):
												if(x_velocity <= -0.07):
													return True
												else:
													if(x_velocity > -0.06):
														return True
											else:
												if(angle_velocity > 0.063):
													if(x_velocity > -0.025):
														if(y_velocity <= -0.255):
															if(lander_x <= -0.269):
																return True
														else:
															return True
									else:
										if(x_velocity <= -0.023):
											if(y_velocity <= -0.251):
												if(x_velocity <= -0.034):
													if(x_velocity <= -0.093):
														return True
											else:
												if(lander_y <= 0.549):
													if(angle_velocity <= 0.029):
														if(angle <= -0.009):
															if(lander_x <= 0.094):
																if(angle > -0.021):
																	if(lander_y > 0.44):
																		return True
													else:
														if(y_velocity > -0.248):
															return True
												else:
													if(angle <= -0.001):
														if(y_velocity <= -0.25):
															if(lander_x > 0.071):
																return True
														else:
															return True
													else:
														if(angle_velocity > -0.017):
															if(angle > 0.01):
																return True
										else:
											if(angle <= 0.003):
												if(angle_velocity > -0.006):
													if(y_velocity > -0.248):
														if(lander_x <= -0.19):
															return True
														else:
															if(lander_x <= 0.055):
																if(lander_y > 0.646):
																	return True
											else:
												if(angle_velocity > 0.051):
													if(angle_velocity <= 0.052):
														return True
								else:
									if(angle <= 0.027):
										if(angle_velocity <= 0.015):
											if(x_velocity <= -0.051):
												if(angle_velocity <= -0.02):
													if(angle_velocity <= -0.023):
														return True
												else:
													return True
											else:
												if(lander_y <= 0.519):
													if(lander_x <= -0.062):
														if(angle <= -0.012):
															if(x_velocity <= 0.006):
																return True
															else:
																if(lander_x <= -0.177):
																	return True
														else:
															if(y_velocity > -0.233):
																if(angle > -0.008):
																	if(angle <= 0.004):
																		if(x_velocity > 0.01):
																			return True
																	else:
																		return True
												else:
													if(x_velocity <= 0.014):
														if(lander_x <= 0.059):
															if(angle > -0.024):
																if(x_velocity <= 0.005):
																	return True
																else:
																	if(x_velocity > 0.01):
																		return True
														else:
															if(y_velocity > -0.222):
																return True
													else:
														if(y_velocity <= -0.238):
															return True
														else:
															if(lander_y > 0.611):
																if(x_velocity > 0.026):
																	return True
										else:
											if(y_velocity <= -0.23):
												if(x_velocity <= -0.011):
													if(angle <= -0.059):
														if(angle <= -0.065):
															return True
													else:
														if(lander_y > 0.401):
															if(y_velocity <= -0.239):
																if(y_velocity <= -0.239):
																	return True
															else:
																return True
												else:
													if(lander_x <= -0.028):
														if(angle_velocity <= 0.059):
															if(lander_y > 0.434):
																if(angle <= 0.009):
																	return True
													else:
														if(y_velocity <= -0.237):
															if(lander_x > 0.039):
																return True
											else:
												if(angle <= -0.047):
													if(angle <= -0.057):
														return True
												else:
													if(lander_y <= 0.585):
														return True
													else:
														if(lander_x <= 0.01):
															return True
									else:
										if(lander_y > 0.551):
											if(lander_y <= 0.592):
												if(lander_x > 0.029):
													return True
							else:
								if(y_velocity <= -0.254):
									if(lander_y <= 0.805):
										if(x_velocity <= -0.02):
											if(y_velocity <= -0.257):
												if(y_velocity <= -0.257):
													if(angle > -0.06):
														return True
											else:
												return True
										else:
											if(y_velocity <= -0.259):
												if(lander_y <= 0.709):
													if(angle > -0.027):
														return True
											else:
												if(angle <= -0.035):
													return True
									else:
										if(y_velocity <= -0.256):
											if(angle_velocity <= -0.015):
												if(lander_y > 0.825):
													return True
											else:
												return True
										else:
											if(lander_x <= 0.034):
												if(lander_x <= 0.028):
													if(x_velocity > 0.023):
														if(angle_velocity > 0.003):
															return True
											else:
												return True
								else:
									if(angle <= -0.028):
										if(lander_y > 0.722):
											if(lander_y <= 0.774):
												return True
											else:
												if(angle <= -0.041):
													return True
									else:
										if(angle <= 0.01):
											if(angle <= 0.008):
												if(angle_velocity <= 0.019):
													if(x_velocity <= -0.053):
														return True
													else:
														if(lander_x <= -0.008):
															if(x_velocity <= 0.0):
																if(lander_x <= -0.023):
																	return True
																else:
																	if(lander_y > 1.034):
																		return True
															else:
																if(lander_x <= -0.129):
																	return True
												else:
													if(angle_velocity <= 0.067):
														return True
													else:
														if(angle_velocity > 0.071):
															return True
										else:
											if(lander_y <= 0.698):
												if(y_velocity > -0.242):
													return True
											else:
												if(y_velocity <= -0.25):
													if(lander_y > 0.803):
														if(y_velocity <= -0.251):
															return True
												else:
													if(angle <= 0.015):
														if(angle <= 0.014):
															return True
													else:
														return True
						else:
							if(lander_y <= 0.649):
								if(angle_velocity > -0.007):
									if(angle <= 0.013):
										if(y_velocity <= -0.233):
											if(angle_velocity > 0.009):
												if(lander_x <= -0.302):
													if(lander_y <= 0.509):
														return True
										else:
											if(lander_y <= 0.542):
												if(x_velocity <= 0.092):
													if(x_velocity > 0.048):
														if(angle_velocity > 0.016):
															if(y_velocity > -0.225):
																return True
											else:
												if(angle_velocity > 0.023):
													return True
									else:
										if(y_velocity > -0.23):
											if(lander_y <= 0.623):
												if(lander_y > 0.542):
													if(angle <= 0.035):
														return True
											else:
												return True
							else:
								if(angle <= 0.131):
									if(lander_y <= 0.774):
										if(y_velocity <= -0.228):
											if(angle_velocity > -0.009):
												if(angle <= 0.015):
													if(angle_velocity <= 0.075):
														if(y_velocity > -0.246):
															if(lander_x <= -0.18):
																if(lander_x > -0.21):
																	return True
													else:
														return True
												else:
													if(x_velocity <= 0.047):
														if(x_velocity > 0.038):
															return True
													else:
														if(y_velocity <= -0.229):
															if(angle_velocity > 0.004):
																if(angle_velocity > 0.06):
																	if(lander_x > -0.149):
																		return True
										else:
											if(angle_velocity <= 0.026):
												if(lander_y > 0.682):
													if(y_velocity > -0.224):
														return True
											else:
												return True
									else:
										if(y_velocity <= -0.248):
											if(angle <= 0.027):
												if(angle_velocity > 0.045):
													if(lander_y <= 0.847):
														if(y_velocity > -0.251):
															return True
													else:
														if(x_velocity <= 0.043):
															if(lander_y > 0.972):
																return True
														else:
															if(angle_velocity > 0.085):
																return True
											else:
												if(x_velocity <= 0.069):
													if(lander_y > 1.081):
														return True
												else:
													if(angle_velocity > 0.014):
														if(lander_y <= 1.385):
															if(angle > 0.116):
																if(lander_y > 1.356):
																	return True
										else:
											if(lander_y <= 1.382):
												if(angle_velocity <= 0.034):
													if(lander_y > 0.848):
														if(lander_x > -0.044):
															if(x_velocity <= 0.064):
																return True
															else:
																if(x_velocity > 0.068):
																	if(lander_x > 0.031):
																		return True
												else:
													if(x_velocity <= 0.041):
														if(angle > -0.007):
															return True
													else:
														return True
											else:
												if(x_velocity <= 0.12):
													return True
								else:
									if(x_velocity <= 0.294):
										if(angle <= 0.425):
											if(y_velocity <= -0.24):
												if(lander_x <= 0.041):
													return True
											else:
												if(x_velocity <= 0.222):
													if(lander_y > 1.13):
														if(angle <= 0.162):
															if(angle <= 0.151):
																return True
														else:
															return True
										else:
											if(y_velocity > -0.254):
												if(angle_velocity > 0.01):
													if(x_velocity <= 0.276):
														if(angle_velocity <= 0.195):
															return True
														else:
															if(lander_x <= 0.208):
																return True
													else:
														if(y_velocity > -0.227):
															return True
		else:
			if(angle_velocity <= -0.011):
				if(right_leg_contact != True):
					if(angle <= 0.062):
						if(angle_velocity <= -0.036):
							if(x_velocity <= -0.049):
								if(angle <= -0.018):
									if(x_velocity > -0.312):
										if(x_velocity <= -0.051):
											if(x_velocity <= -0.097):
												if(angle_velocity <= -0.061):
													if(x_velocity <= -0.223):
														if(angle_velocity > -0.163):
															if(x_velocity > -0.312):
																return True
												else:
													return True
										else:
											return True
								else:
									if(y_velocity > -0.216):
										if(lander_x <= 0.106):
											if(lander_y <= 0.076):
												if(x_velocity <= -0.064):
													return True
											else:
												return True
										else:
											if(lander_y > 0.012):
												if(y_velocity > -0.187):
													return True
							else:
								if(angle_velocity <= -0.052):
									if(angle <= 0.036):
										if(lander_y > 0.657):
											if(angle > 0.01):
												return True
									else:
										if(angle_velocity > -0.07):
											if(angle_velocity > -0.062):
												if(x_velocity <= 0.044):
													return True
								else:
									if(lander_x <= -0.175):
										if(y_velocity <= -0.207):
											if(angle <= -0.002):
												if(lander_x <= -0.194):
													return True
										else:
											if(lander_y <= 0.319):
												if(angle_velocity <= -0.046):
													return True
											else:
												return True
									else:
										if(x_velocity <= 0.029):
											if(angle <= 0.025):
												if(lander_x <= -0.072):
													if(angle > -0.015):
														if(x_velocity <= 0.008):
															if(lander_y > 0.132):
																return True
														else:
															if(angle > 0.012):
																return True
												else:
													if(left_leg_contact != True):
														if(angle <= 0.018):
															if(x_velocity <= -0.034):
																if(angle_velocity <= -0.045):
																	return True
														else:
															if(lander_x <= 0.055):
																if(x_velocity > -0.004):
																	return True
											else:
												if(lander_y <= 0.175):
													if(y_velocity > -0.186):
														return True
												else:
													if(lander_y > 0.275):
														return True
										else:
											if(angle <= 0.059):
												if(lander_y <= 0.558):
													if(y_velocity > -0.164):
														return True
												else:
													return True
						else:
							if(x_velocity <= 0.002):
								if(lander_y <= 0.172):
									if(y_velocity <= -0.197):
										if(angle <= -0.004):
											if(lander_x <= -0.161):
												return True
											else:
												if(x_velocity <= -0.078):
													return True
												else:
													if(angle > -0.022):
														if(angle <= -0.01):
															if(y_velocity > -0.212):
																return True
									else:
										if(angle <= -0.001):
											if(x_velocity <= -0.042):
												if(y_velocity <= -0.187):
													return True
										else:
											return True
								else:
									if(lander_x <= 0.072):
										if(y_velocity > -0.219):
											if(angle_velocity <= -0.011):
												if(y_velocity <= -0.206):
													return True
												else:
													if(y_velocity <= -0.202):
														if(angle <= -0.011):
															return True
														else:
															if(x_velocity <= -0.02):
																return True
													else:
														return True
									else:
										if(x_velocity <= -0.068):
											return True
							else:
								if(lander_y <= 0.216):
									if(y_velocity <= -0.189):
										if(angle <= 0.005):
											if(angle > -0.01):
												if(x_velocity <= 0.028):
													if(lander_x <= -0.049):
														if(x_velocity <= 0.006):
															return True
										else:
											if(x_velocity <= 0.079):
												if(lander_y > 0.144):
													if(lander_x <= -0.027):
														if(lander_y <= 0.16):
															return True
									else:
										if(lander_x <= -0.086):
											if(x_velocity <= 0.057):
												if(angle <= -0.004):
													if(y_velocity > -0.175):
														return True
												else:
													return True
										else:
											if(angle <= 0.046):
												if(y_velocity <= -0.186):
													if(lander_y > 0.111):
														if(y_velocity > -0.188):
															return True
												else:
													if(lander_y <= 0.043):
														if(lander_y > 0.035):
															return True
											else:
												if(y_velocity <= -0.17):
													if(lander_x > 0.007):
														return True
												else:
													if(x_velocity <= 0.082):
														return True
								else:
									if(lander_x <= -0.044):
										if(x_velocity <= 0.062):
											if(y_velocity <= -0.21):
												if(angle > 0.003):
													if(lander_y <= 0.439):
														if(lander_x <= -0.196):
															return True
														else:
															if(x_velocity <= 0.014):
																return True
													else:
														if(angle_velocity > -0.025):
															return True
											else:
												if(angle_velocity <= -0.012):
													if(angle_velocity <= -0.023):
														if(y_velocity <= -0.189):
															if(angle_velocity <= -0.032):
																return True
														else:
															return True
													else:
														return True
									else:
										if(x_velocity <= 0.01):
											if(x_velocity > 0.009):
												return True
										else:
											if(lander_y > 0.627):
												if(angle > 0.017):
													return True
					else:
						if(y_velocity <= -0.174):
							if(angle > 0.082):
								if(x_velocity <= 0.157):
									if(angle_velocity <= -0.113):
										if(lander_y > 1.119):
											if(y_velocity > -0.213):
												if(x_velocity <= 0.134):
													return True
									else:
										if(lander_y <= 1.054):
											if(y_velocity > -0.216):
												return True
										else:
											if(lander_x <= 0.079):
												if(y_velocity <= -0.217):
													return True
											else:
												return True
								else:
									if(angle_velocity > -0.136):
										if(y_velocity > -0.192):
											if(lander_y <= 1.386):
												if(x_velocity <= 0.256):
													return True
												else:
													if(lander_x <= 0.182):
														return True
											else:
												if(angle > 0.353):
													return True
						else:
							if(lander_y <= 0.324):
								if(x_velocity <= 0.133):
									if(y_velocity <= -0.164):
										if(y_velocity <= -0.171):
											return True
									else:
										return True
							else:
								if(angle_velocity <= -0.135):
									if(x_velocity <= 0.221):
										return True
								else:
									return True
			else:
				if(lander_y <= 0.246):
					if(y_velocity <= -0.186):
						if(x_velocity <= 0.019):
							if(y_velocity <= -0.204):
								if(x_velocity <= -0.027):
									if(left_leg_contact != True):
										if(angle_velocity <= 0.004):
											if(lander_x <= 0.063):
												if(angle <= -0.054):
													if(angle <= -0.073):
														return True
												else:
													return True
										else:
											return True
								else:
									if(lander_y <= 0.187):
										if(lander_x <= -0.131):
											if(y_velocity > -0.214):
												if(left_leg_contact != True):
													return True
										else:
											if(lander_y > 0.002):
												if(angle_velocity <= -0.005):
													if(lander_y > 0.124):
														if(y_velocity > -0.205):
															return True
												else:
													if(x_velocity <= -0.015):
														if(angle_velocity <= 0.057):
															if(y_velocity > -0.207):
																return True
														else:
															return True
									else:
										if(lander_x <= -0.04):
											return True
										else:
											if(y_velocity > -0.211):
												if(x_velocity <= 0.009):
													if(angle_velocity > 0.004):
														return True
							else:
								if(angle_velocity <= -0.005):
									if(angle > -0.001):
										if(angle_velocity <= -0.009):
											if(angle_velocity <= -0.01):
												return True
								else:
									if(lander_y > 0.004):
										if(angle <= 0.019):
											if(x_velocity <= 0.019):
												if(x_velocity <= -0.001):
													return True
												else:
													if(angle_velocity <= 0.014):
														if(y_velocity > -0.197):
															return True
													else:
														if(lander_y > 0.011):
															if(lander_x <= 0.069):
																return True
															else:
																if(angle > 0.01):
																	return True
										else:
											if(y_velocity <= -0.192):
												if(lander_x <= 0.04):
													return True
											else:
												return True
						else:
							if(angle <= 0.011):
								if(y_velocity <= -0.201):
									if(angle <= -0.031):
										if(angle_velocity > 0.029):
											return True
									else:
										if(angle_velocity > -0.001):
											if(angle <= -0.015):
												if(lander_x > -0.114):
													if(angle <= -0.02):
														return True
								else:
									if(lander_y <= 0.138):
										if(angle <= -0.01):
											if(angle_velocity > 0.03):
												return True
										else:
											if(angle_velocity > -0.005):
												if(angle <= -0.004):
													if(angle_velocity <= 0.066):
														if(angle > -0.009):
															return True
												else:
													if(angle_velocity > 0.069):
														if(angle_velocity <= 0.243):
															return True
									else:
										if(y_velocity <= -0.196):
											if(x_velocity <= 0.059):
												return True
										else:
											if(lander_x <= -0.035):
												if(x_velocity <= 0.045):
													return True
							else:
								if(right_leg_contact != True):
									if(lander_y > 0.148):
										if(angle_velocity > -0.004):
											if(y_velocity <= -0.2):
												if(angle <= 0.017):
													if(angle > 0.016):
														return True
											else:
												if(angle <= 0.034):
													if(angle_velocity <= 0.031):
														if(y_velocity <= -0.2):
															return True
													else:
														if(angle_velocity <= 0.07):
															if(angle_velocity <= 0.046):
																if(angle_velocity > 0.043):
																	if(y_velocity <= -0.188):
																		return True
														else:
															return True
												else:
													if(x_velocity <= 0.055):
														if(x_velocity > 0.046):
															return True
								else:
									if(x_velocity <= 0.044):
										return True
					else:
						if(x_velocity <= 0.079):
							if(left_leg_contact != True):
								if(x_velocity <= 0.053):
									if(angle <= -0.01):
										if(angle_velocity <= 0.028):
											if(x_velocity <= -0.004):
												return True
										else:
											return True
									else:
										if(lander_y <= 0.011):
											if(lander_y <= 0.004):
												return True
										else:
											if(lander_x <= 0.122):
												if(angle <= 0.049):
													if(angle <= 0.007):
														if(angle <= 0.006):
															return True
													else:
														return True
												else:
													if(angle > 0.05):
														return True
											else:
												if(x_velocity <= -0.016):
													return True
								else:
									if(y_velocity <= -0.171):
										if(lander_x <= -0.036):
											if(angle_velocity > 0.018):
												if(angle > -0.011):
													return True
										else:
											if(lander_y <= 0.165):
												if(y_velocity <= -0.172):
													if(angle_velocity > 0.041):
														return True
									else:
										if(angle_velocity <= -0.004):
											if(y_velocity > -0.16):
												return True
										else:
											return True
							else:
								if(angle_velocity <= 0.453):
									if(angle > -0.007):
										if(angle > 0.095):
											return True
								else:
									return True
						else:
							if(y_velocity <= -0.164):
								if(angle_velocity > -0.007):
									if(angle_velocity <= 0.078):
										if(lander_y <= 0.149):
											if(lander_y <= -0.005):
												return True
											else:
												if(angle <= 0.049):
													if(angle <= 0.047):
														if(x_velocity > 0.096):
															if(angle_velocity > 0.046):
																if(angle_velocity <= 0.049):
																	return True
																else:
																	if(y_velocity > -0.172):
																		if(lander_x <= -0.237):
																			return True
										else:
											if(y_velocity <= -0.172):
												if(angle <= 0.039):
													return True
											else:
												return True
									else:
										return True
							else:
								if(x_velocity <= 0.082):
									if(lander_y <= 0.09):
										return True
								else:
									if(x_velocity <= 0.146):
										return True
									else:
										if(y_velocity <= -0.142):
											if(lander_y > 0.049):
												if(lander_y > 0.077):
													if(angle_velocity > 0.02):
														return True
										else:
											return True
				else:
					if(x_velocity <= 0.09):
						if(y_velocity <= -0.21):
							if(x_velocity <= 0.014):
								if(angle_velocity <= -0.0):
									if(lander_x <= -0.002):
										if(angle <= 0.001):
											return True
									else:
										if(lander_y <= 0.289):
											return True
								else:
									if(y_velocity <= -0.218):
										if(lander_y <= 0.313):
											if(angle <= -0.009):
												if(lander_y <= 0.279):
													return True
										else:
											if(angle_velocity > 0.004):
												if(y_velocity <= -0.218):
													return True
									else:
										if(x_velocity <= -0.006):
											return True
										else:
											if(x_velocity > -0.004):
												if(lander_y <= 0.301):
													if(y_velocity <= -0.215):
														return True
												else:
													return True
							else:
								if(lander_y <= 0.419):
									if(angle <= -0.001):
										if(angle <= -0.016):
											return True
										else:
											if(angle_velocity > 0.046):
												if(lander_y > 0.307):
													return True
									else:
										if(angle_velocity <= 0.001):
											if(x_velocity <= 0.051):
												if(lander_y > 0.374):
													return True
										else:
											if(y_velocity > -0.211):
												if(angle_velocity <= 0.027):
													return True
								else:
									if(lander_x <= 0.03):
										if(y_velocity <= -0.211):
											if(angle > -0.012):
												if(y_velocity <= -0.216):
													if(lander_y > 0.495):
														if(x_velocity <= 0.078):
															return True
														else:
															if(lander_x <= -0.167):
																return True
												else:
													return True
										else:
											if(angle_velocity > 0.029):
												if(lander_y <= 1.309):
													return True
									else:
										if(lander_y > 0.556):
											if(lander_y > 0.702):
												return True
						else:
							if(x_velocity <= 0.071):
								if(lander_y <= 0.332):
									if(y_velocity <= -0.201):
										if(angle <= 0.018):
											if(lander_x <= -0.041):
												return True
											else:
												if(x_velocity <= 0.013):
													if(angle_velocity <= 0.009):
														if(angle > -0.0):
															return True
													else:
														return True
										else:
											if(angle <= 0.024):
												if(angle > 0.021):
													return True
									else:
										if(angle_velocity > -0.009):
											if(lander_x <= 0.082):
												if(x_velocity <= 0.057):
													if(y_velocity <= -0.199):
														if(y_velocity <= -0.199):
															return True
													else:
														return True
												else:
													if(angle_velocity > 0.028):
														return True
											else:
												if(lander_x > 0.082):
													return True
								else:
									if(y_velocity <= -0.148):
										if(lander_y <= 1.41):
											if(x_velocity <= 0.033):
												return True
											else:
												if(x_velocity > 0.033):
													if(lander_y <= 1.046):
														if(lander_y <= 0.586):
															return True
														else:
															if(lander_y > 0.593):
																return True
										else:
											if(x_velocity > 0.032):
												return True
							else:
								if(angle_velocity <= 0.007):
									if(lander_x <= -0.175):
										return True
								else:
									if(lander_x <= -0.087):
										return True
									else:
										if(angle > 0.051):
											return True
					else:
						if(y_velocity <= -0.173):
							if(x_velocity <= 0.385):
								if(angle_velocity <= 0.08):
									if(lander_y <= 0.467):
										if(angle <= 0.054):
											if(y_velocity <= -0.186):
												if(lander_x <= -0.247):
													if(angle_velocity > 0.005):
														if(lander_y <= 0.436):
															if(angle_velocity > 0.049):
																if(angle <= 0.026):
																	return True
											else:
												if(angle <= 0.048):
													return True
									else:
										if(x_velocity <= 0.262):
											if(lander_y <= 0.677):
												if(y_velocity <= -0.202):
													if(angle <= 0.052):
														if(angle_velocity > 0.032):
															return True
												else:
													return True
											else:
												if(x_velocity > 0.091):
													return True
										else:
											if(y_velocity > -0.182):
												if(x_velocity <= 0.338):
													return True
								else:
									if(lander_y <= 1.385):
										if(y_velocity <= -0.215):
											if(angle_velocity <= 0.234):
												if(x_velocity <= 0.142):
													return True
												else:
													if(angle <= 0.271):
														if(x_velocity <= 0.166):
															if(lander_x > -0.098):
																return True
													else:
														if(lander_y > 1.162):
															return True
											else:
												return True
										else:
											if(y_velocity <= -0.209):
												if(lander_y > 0.577):
													if(y_velocity <= -0.21):
														if(angle_velocity <= 0.283):
															return True
														else:
															if(x_velocity <= 0.307):
																return True
											else:
												if(lander_y <= 0.464):
													if(lander_y <= 0.448):
														return True
												else:
													return True
									else:
										if(angle_velocity > 0.127):
											if(x_velocity <= 0.225):
												if(lander_x > 0.023):
													return True
							else:
								if(angle > 0.153):
									if(angle > 0.387):
										if(x_velocity <= 0.427):
											if(y_velocity > -0.206):
												return True
										else:
											if(angle_velocity > 0.382):
												return True
						else:
							if(x_velocity <= 0.541):
								if(lander_y <= 1.487):
									if(angle > 0.024):
										if(x_velocity <= 0.521):
											if(lander_y <= 1.465):
												if(lander_x <= -0.253):
													if(lander_x <= -0.259):
														return True
												else:
													if(y_velocity <= -0.146):
														return True
													else:
														if(angle > 0.243):
															return True
											else:
												if(y_velocity > -0.163):
													return True
										else:
											if(y_velocity > -0.154):
												return True
								else:
									if(x_velocity <= 0.446):
										return True
	else:
		if(y_velocity <= -0.0):
			if(angle <= 0.102):
				if(lander_y <= 0.046):
					if(angle_velocity <= 0.481):
						if(right_leg_contact != True):
							if(angle_velocity <= 0.145):
								if(y_velocity <= -0.0):
									if(lander_x <= -0.169):
										if(lander_x <= -0.17):
											return True
										else:
											if(y_velocity <= -0.001):
												return True
									else:
										if(x_velocity <= 0.113):
											if(lander_x <= -0.137):
												if(angle_velocity <= 0.024):
													if(angle_velocity > 0.002):
														if(angle <= 0.098):
															if(angle_velocity > 0.003):
																if(angle <= 0.096):
																	if(y_velocity <= -0.001):
																		if(lander_x <= -0.165):
																			return True
																		else:
																			if(y_velocity <= -0.002):
																				if(angle <= 0.089):
																					if(y_velocity <= -0.003):
																						if(lander_y <= -0.011):
																							return True
																						else:
																							if(y_velocity <= -0.003):
																								if(angle <= 0.077):
																									if(x_velocity <= -0.038):
																										if(lander_x <= -0.152):
																											return True
																										else:
																											if(y_velocity <= -0.005):
																												if(lander_y <= -0.008):
																													return True
																												else:
																													if(lander_y <= -0.007):
																														if(y_velocity <= -0.006):
																															return True
																								else:
																									return True
																					else:
																						if(lander_y <= -0.012):
																							if(x_velocity <= -0.021):
																								return True
																				else:
																					return True
																else:
																	return True
														else:
															return True
												else:
													return True
							else:
								if(lander_y > -0.013):
									return True
					else:
						return True
				else:
					if(x_velocity <= 0.224):
						if(angle <= 0.001):
							if(y_velocity <= -0.1):
								if(angle > -0.001):
									return True
						else:
							if(lander_x <= 0.001):
								return True
							else:
								if(angle_velocity <= 0.166):
									if(x_velocity <= 0.077):
										if(lander_x > 0.003):
											return True
								else:
									if(y_velocity <= -0.032):
										return True
			else:
				if(x_velocity <= -0.005):
					if(lander_y <= -0.041):
						if(lander_y <= -0.043):
							return True
						else:
							if(x_velocity <= -0.006):
								if(lander_x <= -0.229):
									return True
								else:
									if(angle_velocity > 0.005):
										if(lander_y <= -0.042):
											return True
										else:
											if(y_velocity <= -0.003):
												return True
											else:
												if(lander_y <= -0.042):
													if(angle_velocity <= 0.007):
														if(x_velocity > -0.014):
															if(lander_y > -0.042):
																return True
													else:
														return True
							else:
								if(lander_x <= -0.292):
									return True
					else:
						if(angle_velocity <= 0.032):
							if(lander_y <= -0.03):
								if(lander_x <= -0.247):
									if(angle_velocity > 0.003):
										if(lander_y <= -0.04):
											if(lander_x <= -0.29):
												return True
											else:
												if(angle_velocity <= 0.003):
													if(lander_x > -0.29):
														if(lander_x <= -0.29):
															return True
												else:
													return True
										else:
											if(y_velocity <= -0.001):
												if(lander_y <= -0.04):
													return True
												else:
													if(y_velocity <= -0.009):
														return True
													else:
														if(y_velocity <= -0.002):
															if(angle <= 0.275):
																if(x_velocity <= -0.024):
																	if(angle <= 0.272):
																		if(lander_y <= -0.032):
																			if(angle_velocity <= 0.025):
																				if(lander_y <= -0.033):
																					if(x_velocity <= -0.068):
																						return True
																					else:
																						if(angle_velocity > 0.009):
																							if(lander_y <= -0.038):
																								return True
																							else:
																								if(x_velocity <= -0.034):
																									if(lander_x <= -0.276):
																										return True
																									else:
																										if(y_velocity <= -0.004):
																											if(lander_x <= -0.272):
																												return True
																											else:
																												if(y_velocity <= -0.005):
																													if(lander_x <= -0.268):
																														return True
																													else:
																														if(angle_velocity > 0.019):
																															if(lander_y <= -0.034):
																																return True
																			else:
																				return True
																	else:
																		return True
															else:
																return True
														else:
															if(lander_x <= -0.286):
																if(x_velocity <= -0.015):
																	return True
								else:
									if(y_velocity <= -0.004):
										if(lander_x <= -0.222):
											return True
										else:
											if(x_velocity <= -0.032):
												if(angle <= 0.271):
													if(angle_velocity > 0.021):
														if(y_velocity > -0.01):
															if(lander_x <= -0.216):
																return True
															else:
																if(x_velocity <= -0.047):
																	if(x_velocity <= -0.056):
																		return True
																	else:
																		if(lander_x <= -0.214):
																			return True
																		else:
																			if(lander_x <= -0.213):
																				if(lander_y > -0.037):
																					return True
												else:
													return True
						else:
							if(angle > 0.125):
								if(y_velocity <= -0.017):
									if(angle <= 0.168):
										if(angle <= 0.164):
											if(lander_y <= -0.021):
												return True
											else:
												if(lander_y > -0.02):
													return True
									else:
										return True
								else:
									if(lander_x <= -0.197):
										if(lander_x <= -0.205):
											return True
										else:
											if(x_velocity <= -0.078):
												if(lander_y <= -0.032):
													return True
												else:
													if(lander_y > -0.031):
														return True
				else:
					if(x_velocity <= -0.001):
						if(x_velocity <= -0.002):
							if(lander_y <= -0.041):
								if(lander_x <= -0.231):
									return True
								else:
									if(y_velocity <= -0.001):
										if(angle_velocity <= 0.002):
											return True
							else:
								if(right_leg_contact != True):
									if(lander_y <= -0.014):
										return True
									else:
										if(angle_velocity > 0.001):
											return True
								else:
									if(lander_x <= -0.292):
										if(angle_velocity > 0.001):
											return True
									else:
										if(x_velocity <= -0.005):
											return True
						else:
							if(angle > 0.102):
								if(x_velocity <= -0.002):
									if(angle_velocity <= 0.001):
										if(x_velocity <= -0.002):
											return True
										else:
											if(x_velocity > -0.002):
												return True
								else:
									if(angle_velocity <= 0.0):
										if(angle > 0.103):
											return True
									else:
										if(lander_x <= -0.293):
											return True
					else:
						if(angle_velocity <= 0.182):
							if(angle <= 0.291):
								if(lander_y > -0.025):
									if(lander_x <= -0.172):
										return True
							else:
								if(lander_x <= -0.232):
									return True
						else:
							if(lander_y <= 1.442):
								if(angle_velocity <= 0.236):
									if(x_velocity <= 0.039):
										return True
								else:
									return True
							else:
								if(x_velocity <= 0.407):
									return True
								else:
									if(angle > 0.193):
										if(angle_velocity > 0.261):
											return True
		else:
			if(x_velocity <= 0.187):
				if(lander_y <= -0.044):
					if(angle_velocity <= -0.0):
						if(angle > 0.305):
							return True
					else:
						return True
				else:
					if(x_velocity <= -0.296):
						return True
					else:
						if(x_velocity <= -0.136):
							if(angle_velocity <= -0.191):
								if(angle_velocity <= -0.232):
									if(y_velocity > 0.036):
										return True
							else:
								return True
						else:
							if(angle <= 0.305):
								if(lander_y <= 1.455):
									if(x_velocity <= 0.178):
										if(y_velocity <= -0.0):
											if(y_velocity <= -0.0):
												if(angle > 0.103):
													if(x_velocity <= -0.001):
														return True
											else:
												return True
								else:
									if(lander_y <= 1.457):
										if(x_velocity <= -0.015):
											return True
							else:
								if(angle_velocity > -0.0):
									return True
			else:
				if(x_velocity <= 0.444):
					if(lander_y > 1.477):
						if(angle > 0.142):
							return True
	return False

