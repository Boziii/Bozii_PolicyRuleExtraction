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
	if(y_velocity <= -0.13108108192682266):
		if(y_velocity <= -0.22433070093393326):
			if(angle_velocity <= -0.033176204189658165):
				if(lander_y <= 1.3444701433181763):
					if(y_velocity > -0.273845911026001):
						if(angle <= 0.034930093213915825):
							if(lander_y <= 0.5064136981964111):
								if(angle_velocity <= -0.06040847301483154):
									if(y_velocity > -0.2535327672958374):
										if(angle <= 0.019497358240187168):
											if(lander_y <= 0.151559479534626):
												if(angle <= -0.01771371066570282):
													if(angle_velocity <= -0.06213214062154293):
														if(y_velocity > -0.2358163446187973):
															if(lander_x <= -0.14672942459583282):
																if(lander_x > -0.17687151581048965):
																	return True
												else:
													if(angle_velocity <= -0.0768754780292511):
														if(lander_y <= 0.02447665180079639):
															return True
								else:
									if(y_velocity > -0.2400168478488922):
										if(lander_y <= 0.19187165051698685):
											if(angle <= -0.020316937007009983):
												if(x_velocity <= -0.029020866379141808):
													if(y_velocity <= -0.23269294202327728):
														if(angle <= -0.045829424634575844):
															if(y_velocity > -0.23651983588933945):
																if(angle > -0.06055501289665699):
																	return True
				else:
					if(x_velocity <= -0.33664602041244507):
						if(angle <= -0.11459648981690407):
							if(angle_velocity <= -0.09190931171178818):
								if(y_velocity > -0.2519789934158325):
									if(angle_velocity <= -0.152280293405056):
										if(lander_x <= -0.16842999309301376):
											return True
										else:
											if(angle <= -0.333836629986763):
												return True
			else:
				if(lander_y <= 0.4006982296705246):
					if(y_velocity > -0.23569615185260773):
						if(x_velocity > -0.04648813232779503):
							if(angle_velocity > -0.009669447783380747):
								if(lander_y <= 0.26726894080638885):
									if(lander_y <= -0.0023655378608964384):
										if(lander_x > -0.10059509612619877):
											return True
		else:
			if(angle_velocity <= -0.01109519088640809):
				if(right_leg_contact != True):
					if(lander_y > 0.5234372615814209):
						if(x_velocity <= 0.1182720772922039):
							if(lander_y > 1.4159489870071411):
								if(y_velocity <= -0.20843198895454407):
									if(y_velocity > -0.22065477073192596):
										if(x_velocity <= -0.37183597683906555):
											return True
								else:
									if(angle <= -0.04813877120614052):
										if(y_velocity <= -0.16151153296232224):
											if(lander_y > 1.508604645729065):
												if(lander_y <= 1.5100222826004028):
													return True
										else:
											if(y_velocity <= -0.15729797631502151):
												return True
											else:
												if(angle_velocity <= -0.13756970316171646):
													if(angle_velocity <= -0.48991283774375916):
														return True
												else:
													if(angle <= -0.09075165167450905):
														return True
				else:
					if(angle <= -0.06543062441051006):
						if(angle_velocity <= -0.5765689015388489):
							if(y_velocity <= -0.21171773225069046):
								if(angle_velocity > -0.6924467980861664):
									return True
						else:
							if(angle > -0.28274887800216675):
								return True
					else:
						if(x_velocity <= 0.1321985051035881):
							if(angle_velocity > -0.724619597196579):
								if(y_velocity > -0.2181570902466774):
									return True
						else:
							if(left_leg_contact == True):
								return True
			else:
				if(y_velocity <= -0.19208889454603195):
					if(lander_y <= 0.2897540479898453):
						if(angle <= -0.001974301296286285):
							if(x_velocity <= -0.01461441582068801):
								if(lander_y <= 0.00980702368542552):
									if(angle_velocity > -0.005119665991514921):
										if(right_leg_contact == True):
											return True
						else:
							if(right_leg_contact == True):
								if(lander_x > -0.12573399394750595):
									return True
				else:
					if(x_velocity <= 0.07045570015907288):
						if(right_leg_contact == True):
							if(angle_velocity <= 0.40840761363506317):
								if(lander_y <= -0.02071993052959442):
									if(angle <= 0.1901896819472313):
										if(angle > 0.18110547959804535):
											return True
								else:
									if(x_velocity > -0.09408597834408283):
										return True
							else:
								if(y_velocity > -0.13969463109970093):
									if(x_velocity > -0.04035506024956703):
										if(x_velocity <= -0.022401030641049147):
											return True
					else:
						if(y_velocity <= -0.17878469824790955):
							if(lander_y <= 0.3682808578014374):
								if(angle <= 0.033226991072297096):
									if(angle_velocity <= 0.032327210530638695):
										if(y_velocity <= -0.1822424978017807):
											if(y_velocity <= -0.18755576759576797):
												if(y_velocity <= -0.18873679637908936):
													if(angle > 0.022810661233961582):
														if(y_velocity > -0.18998104333877563):
															if(angle > 0.03160081245005131):
																return True
						else:
							if(x_velocity <= 0.45725807547569275):
								if(angle_velocity > 0.020849051885306835):
									if(lander_y <= 0.04226007126271725):
										if(left_leg_contact != True):
											if(y_velocity > -0.16917701810598373):
												if(x_velocity <= 0.15987766534090042):
													if(lander_x > -0.2338159829378128):
														if(right_leg_contact == True):
															if(lander_x > -0.19359001517295837):
																return True
	else:
		if(angle <= 0.18057335913181305):
			if(lander_y <= 0.04876668006181717):
				if(angle_velocity <= 0.459291011095047):
					if(x_velocity <= -0.138141967356205):
						if(lander_x <= -0.16982293128967285):
							if(angle <= 0.1695684865117073):
								if(x_velocity <= -0.1505345180630684):
									if(lander_y > -0.021395273506641388):
										if(y_velocity > -0.025826004333794117):
											if(lander_y <= -0.020888819359242916):
												return True
											else:
												if(angle <= 0.14696944504976273):
													return True
								else:
									return True
						else:
							if(y_velocity > -0.07581898756325245):
								if(x_velocity <= -0.1820785105228424):
									if(lander_x <= -0.16601614654064178):
										return True
								else:
									return True
					else:
						if(angle_velocity <= -0.6161576211452484):
							if(left_leg_contact == True):
								return True
						else:
							if(angle_velocity <= 0.38545961678028107):
								if(angle <= -0.3233342170715332):
									if(angle_velocity > -0.25130046159029007):
										return True
								else:
									if(x_velocity <= -0.10150237381458282):
										if(angle_velocity <= 0.19341470301151276):
											if(x_velocity <= -0.10205988958477974):
												return True
										else:
											if(lander_y > -0.013565602246671915):
												return True
									else:
										if(angle_velocity <= 0.31549812853336334):
											if(right_leg_contact != True):
												if(angle_velocity <= 0.06605993956327438):
													return True
												else:
													if(y_velocity > 0.019714023917913437):
														return True
											else:
												return True
										else:
											if(angle <= 0.13291499763727188):
												return True
							else:
								if(lander_x <= -0.1301352009177208):
									if(angle_velocity > 0.4115541875362396):
										return True
								else:
									return True
			else:
				if(x_velocity <= -0.29952582716941833):
					if(angle <= -0.0669122189283371):
						if(angle_velocity <= -0.31141039729118347):
							if(x_velocity > -0.6054616570472717):
								if(y_velocity > -0.1259635053575039):
									if(lander_y > 1.459312617778778):
										if(x_velocity <= -0.5541252493858337):
											if(angle <= -0.12758800759911537):
												return True
										else:
											return True
					else:
						if(lander_y > 1.5030698776245117):
							if(x_velocity > -0.445543497800827):
								return True
				else:
					if(x_velocity <= 0.2370886579155922):
						if(angle <= -0.00334473280236125):
							if(y_velocity > -0.1187281422317028):
								if(angle <= -0.02227552980184555):
									if(angle_velocity <= -0.0828390121459961):
										if(y_velocity <= -0.11646486073732376):
											if(x_velocity <= -0.23474515974521637):
												return True
										else:
											if(lander_y <= 1.4232779741287231):
												if(lander_y <= 1.4201720356941223):
													return True
											else:
												if(angle <= -0.15128538757562637):
													if(lander_x <= -0.062276314944028854):
														return True
												else:
													if(angle_velocity <= -0.11093137785792351):
														return True
													else:
														if(lander_x > -0.028021334670484066):
															return True
								else:
									if(x_velocity <= -0.24020950496196747):
										if(angle_velocity <= -0.174425907433033):
											return True
									else:
										if(y_velocity > -0.07852547243237495):
											if(lander_x <= 0.005284500075504184):
												if(angle_velocity <= -0.024072550237178802):
													if(angle > -0.021963967010378838):
														if(angle_velocity <= -0.07620223984122276):
															if(angle_velocity <= -0.10634908080101013):
																return True
															else:
																if(y_velocity > 0.3189091980457306):
																	return True
														else:
															if(angle_velocity <= -0.03161052614450455):
																return True
															else:
																if(angle > -0.00671025225892663):
																	return True
											else:
												if(y_velocity <= 0.27142174541950226):
													if(angle_velocity <= 0.02164728008210659):
														if(x_velocity <= 0.16837178170681):
															if(y_velocity <= 0.15363261103630066):
																if(angle_velocity > 0.007625528844073415):
																	return True
															else:
																if(angle > -0.01668528001755476):
																	return True
													else:
														if(lander_y <= 1.4907854795455933):
															return True
														else:
															if(x_velocity <= 0.123173076659441):
																return True
												else:
													return True
						else:
							if(x_velocity > -0.12136666104197502):
								if(y_velocity <= -0.03921147249639034):
									if(angle_velocity <= 0.17280402034521103):
										if(x_velocity <= 0.19898531585931778):
											if(angle_velocity <= 0.13633114844560623):
												if(lander_y > 1.404726803302765):
													if(x_velocity <= 0.11053816229104996):
														if(angle_velocity > 0.02529743779450655):
															if(lander_x <= 0.014724159613251686):
																return True
								else:
									if(lander_x <= 0.0017909050220623612):
										if(lander_y <= 1.4155747890472412):
											if(x_velocity > -0.051502836868166924):
												if(angle > -0.0009680459916125983):
													return True
										else:
											if(angle <= 0.006337355822324753):
												if(lander_x <= -0.010935783386230469):
													if(x_velocity > -0.10414125770330429):
														return True
												else:
													if(lander_y <= 1.4177979230880737):
														if(lander_y <= 1.4172518849372864):
															return True
													else:
														return True
									else:
										if(angle_velocity <= 0.10761477425694466):
											if(y_velocity <= 0.18568943440914154):
												if(angle_velocity > 0.06498461216688156):
													if(angle <= 0.0021552671678364277):
														if(lander_x <= 0.024590635672211647):
															return True
													else:
														if(y_velocity > 0.10900164768099785):
															if(angle <= 0.009164376650005579):
																return True
											else:
												return True
										else:
											if(angle_velocity <= 0.19915063679218292):
												if(lander_y > 1.4240711331367493):
													if(lander_x <= 0.0422650333493948):
														if(angle_velocity <= 0.14905401319265366):
															if(angle <= 0.02732013911008835):
																if(lander_x <= 0.020147276110947132):
																	if(angle_velocity <= 0.12353972345590591):
																		if(angle <= 0.010281411465257406):
																			return True
																	else:
																		return True
																else:
																	return True
														else:
															if(angle_velocity <= 0.17684370279312134):
																return True
															else:
																if(angle <= 0.04242449067533016):
																	return True
					else:
						if(x_velocity <= 0.46994757652282715):
							if(lander_y <= 1.4616153836250305):
								if(y_velocity > 0.2778199464082718):
									if(x_velocity <= 0.3102336823940277):
										if(y_velocity <= 0.351259708404541):
											if(y_velocity <= 0.31201910972595215):
												return True
										else:
											return True
							else:
								if(y_velocity > -0.01241840049624443):
									if(angle_velocity <= 0.1323314756155014):
										if(y_velocity > 0.3109956532716751):
											return True
									else:
										if(lander_x <= 0.09310021251440048):
											if(angle_velocity <= 0.16254669427871704):
												if(x_velocity > 0.2891625463962555):
													return True
											else:
												return True
		else:
			if(angle_velocity <= -0.0002966387401102111):
				if(angle <= 0.3039054870605469):
					if(lander_x > -0.28749994933605194):
						if(lander_y <= -0.04361077770590782):
							if(y_velocity > 0.0002322039581486024):
								return True
						else:
							return True
				else:
					if(x_velocity <= 0.0013785074697807431):
						if(lander_x <= -0.23232891410589218):
							if(x_velocity > 0.0013156583881936967):
								if(lander_y > -0.0431901179254055):
									return True
						else:
							if(lander_x <= -0.23217620700597763):
								if(lander_x <= -0.23226668685674667):
									return True
							else:
								return True
					else:
						if(lander_x > -0.24004290252923965):
							if(angle_velocity <= -0.0005263057246338576):
								return True
							else:
								if(angle <= 0.304432675242424):
									return True
			else:
				if(lander_y <= -0.04202711209654808):
					if(y_velocity <= -0.0002578590210760012):
						if(lander_x <= -0.23773784190416336):
							if(lander_x <= -0.23841527104377747):
								if(x_velocity > -0.0014504787395708263):
									if(lander_x > -0.2729504704475403):
										return True
							else:
								if(lander_y <= -0.04298262298107147):
									if(y_velocity > -0.0006346373702399433):
										return True
						else:
							if(angle <= 0.29945676028728485):
								if(y_velocity <= -0.0009148360113613307):
									if(y_velocity <= -0.0013403847115114331):
										if(angle <= 0.29289789497852325):
											if(angle_velocity <= 0.00512483436614275):
												return True
									else:
										if(angle <= 0.29685693979263306):
											return True
										else:
											if(lander_x > -0.2296057939529419):
												return True
								else:
									return True
							else:
								if(x_velocity <= -0.0028954772278666496):
									if(lander_x > -0.23037397861480713):
										if(x_velocity > -0.004811337450519204):
											return True
								else:
									if(angle <= 0.3015734851360321):
										if(lander_x > -0.23662061989307404):
											return True
					else:
						if(angle <= 0.303544357419014):
							if(lander_x > -0.27298156917095184):
								if(lander_y > -0.043588677421212196):
									if(x_velocity > -0.0015286349807865918):
										if(y_velocity <= -0.00014368049596669152):
											if(angle <= 0.3028325289487839):
												if(angle > 0.2964203506708145):
													return True
										else:
											return True
						else:
							if(lander_x > -0.2321137711405754):
								if(x_velocity > -0.00029814841036568396):
									return True
				else:
					if(left_leg_contact == True):
						if(lander_x <= -0.23503723740577698):
							if(lander_y <= -0.03342694975435734):
								if(y_velocity <= -0.00031181934173218906):
									if(angle <= 0.29256346821784973):
										if(lander_x <= -0.27979449927806854):
											if(y_velocity <= -0.005563078681007028):
												if(x_velocity > -0.03565696254372597):
													return True
											else:
												if(angle <= 0.24749747663736343):
													return True
												else:
													if(x_velocity > -0.04683324880897999):
														if(angle_velocity <= 0.008627701085060835):
															return True
														else:
															if(angle <= 0.2606273740530014):
																if(angle_velocity <= 0.011774625163525343):
																	return True
																else:
																	if(angle <= 0.2534070312976837):
																		return True
										else:
											if(y_velocity <= -0.0006552657578140497):
												if(lander_x <= -0.27048829197883606):
													if(lander_x > -0.2708262652158737):
														if(lander_y <= -0.041449401527643204):
															return True
												else:
													if(x_velocity <= -0.00947643257677555):
														if(lander_x > -0.2688800096511841):
															if(x_velocity <= -0.01223765965551138):
																if(lander_y > -0.04041311889886856):
																	if(y_velocity <= -0.0025606987765058875):
																		if(lander_x > -0.26284368336200714):
																			if(x_velocity <= -0.026978440582752228):
																				if(lander_x > -0.26045216619968414):
																					if(x_velocity > -0.06665289029479027):
																						if(y_velocity <= -0.003999263746663928):
																							if(lander_x > -0.2584616243839264):
																								if(angle <= 0.24389991164207458):
																									return True
																								else:
																									if(angle_velocity <= 0.018895636312663555):
																										if(lander_y <= -0.03638923354446888):
																											if(y_velocity > -0.005372762447223067):
																												if(angle <= 0.2633099853992462):
																													return True
																												else:
																													if(x_velocity > -0.035358116030693054):
																														return True
																										else:
																											return True
																									else:
																										if(lander_x > -0.24810293316841125):
																											if(angle_velocity <= 0.022017963230609894):
																												return True
																						else:
																							return True
																			else:
																				return True
																	else:
																		if(lander_y <= -0.04012190364301205):
																			if(y_velocity > -0.0020756263402290642):
																				return True
																		else:
																			return True
															else:
																return True
													else:
														if(lander_y <= -0.041261376813054085):
															if(y_velocity > -0.0009450570505578071):
																return True
														else:
															return True
											else:
												return True
									else:
										if(lander_x > -0.2535083740949631):
											if(angle_velocity <= 0.0032097346847876906):
												return True
								else:
									if(lander_x <= -0.27284882962703705):
										if(angle_velocity <= 0.0005846305866725743):
											return True
									else:
										return True
							else:
								if(y_velocity > -0.009919839445501566):
									if(y_velocity <= -0.009197108913213015):
										if(angle <= 0.229521743953228):
											return True
									else:
										return True
						else:
							if(y_velocity <= -0.0017634674441069365):
								if(y_velocity <= -0.014181504491716623):
									if(x_velocity <= 0.045335978269577026):
										if(angle <= 0.20899919420480728):
											if(x_velocity <= -0.11125599592924118):
												if(angle <= 0.1932438611984253):
													if(angle_velocity <= 0.06029107794165611):
														if(angle <= 0.18885479122400284):
															return True
														else:
															if(y_velocity > -0.01869307179003954):
																return True
											else:
												if(lander_x <= -0.1810481995344162):
													if(x_velocity <= -0.10662930458784103):
														if(angle_velocity > 0.05132148042321205):
															return True
													else:
														return True
									else:
										return True
								else:
									if(angle <= 0.29117703437805176):
										if(x_velocity <= -0.014963520225137472):
											if(angle <= 0.28673432767391205):
												if(x_velocity <= -0.02327061351388693):
													if(lander_y <= -0.03942263312637806):
														if(angle <= 0.27718666195869446):
															if(lander_x <= -0.22879020869731903):
																return True
													else:
														if(y_velocity <= -0.005009366665035486):
															if(lander_y > -0.03856287710368633):
																if(x_velocity <= -0.04225950874388218):
																	if(angle <= 0.25911061465740204):
																		if(lander_x <= -0.21519596874713898):
																			if(angle <= 0.20358587801456451):
																				return True
																			else:
																				if(x_velocity <= -0.052496904507279396):
																					if(angle <= 0.2514372915029526):
																						if(y_velocity > -0.012675213161855936):
																							if(lander_y <= -0.029767395928502083):
																								if(y_velocity > -0.011487866286188364):
																									if(lander_y <= -0.03101267386227846):
																										if(y_velocity > -0.010406606364995241):
																											if(angle <= 0.24915795773267746):
																												return True
																											else:
																												if(x_velocity > -0.05765606090426445):
																													return True
																									else:
																										return True
																							else:
																								return True
																				else:
																					return True
																		else:
																			if(y_velocity <= -0.013802431058138609):
																				return True
																			else:
																				if(x_velocity <= -0.07644497230648994):
																					if(y_velocity <= -0.006820400943979621):
																						if(angle_velocity > 0.03866227902472019):
																							if(y_velocity > -0.013106403406709433):
																								return True
																					else:
																						if(y_velocity <= -0.005661074770614505):
																							if(lander_x > -0.18308457732200623):
																								return True
																				else:
																					if(lander_y <= -0.03367278166115284):
																						if(y_velocity > -0.010693163145333529):
																							if(angle <= 0.2468985989689827):
																								if(x_velocity <= -0.06347637996077538):
																									if(angle_velocity > 0.030273349955677986):
																										return True
																								else:
																									return True
																							else:
																								if(x_velocity <= -0.04866452142596245):
																									if(x_velocity > -0.05291973799467087):
																										if(lander_x > -0.2128155753016472):
																											return True
																								else:
																									return True
																					else:
																						if(angle_velocity <= 0.03657999262213707):
																							return True
																						else:
																							if(lander_x > -0.20477870106697083):
																								return True
																else:
																	if(angle <= 0.2676932066679001):
																		return True
																	else:
																		if(angle_velocity <= 0.017368759959936142):
																			if(angle <= 0.27267181873321533):
																				return True
														else:
															if(angle <= 0.2776561379432678):
																return True
															else:
																if(angle > 0.27853506803512573):
																	return True
												else:
													if(lander_x <= -0.23180026561021805):
														if(angle_velocity <= 0.009558133315294981):
															return True
													else:
														if(angle <= 0.2844739258289337):
															return True
														else:
															if(y_velocity > -0.0033114090329036117):
																return True
											else:
												if(lander_x > -0.22632689028978348):
													if(angle_velocity <= 0.009472921025007963):
														return True
										else:
											return True
									else:
										if(y_velocity > -0.0017753514694049954):
											if(y_velocity <= -0.0017680999008007348):
												return True
							else:
								if(angle_velocity <= 0.10090447217226028):
									if(angle <= 0.2965114265680313):
										if(angle <= 0.295711025595665):
											return True
										else:
											if(angle_velocity <= 0.003781290724873543):
												return True
	return False

def weShould_left_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.13108108192682266):
		if(y_velocity <= -0.22433070093393326):
			if(angle_velocity <= -0.033176204189658165):
				if(lander_y <= 1.3444701433181763):
					if(y_velocity <= -0.273845911026001):
						if(angle <= 0.024799825623631477):
							if(angle_velocity <= -0.059247663244605064):
								if(y_velocity <= -0.2988070696592331):
									if(angle_velocity <= -0.37396079301834106):
										if(lander_y <= 1.3258112668991089):
											if(y_velocity > -0.5854084193706512):
												if(angle_velocity <= -0.44097302854061127):
													return True
												else:
													if(lander_y <= 1.3106675744056702):
														if(lander_x <= 0.1759875789284706):
															if(y_velocity <= -0.4950762987136841):
																if(angle <= -0.2834938168525696):
																	return True
																else:
																	if(lander_y > 1.2984379529953003):
																		return True
															else:
																return True
										else:
											if(angle <= -0.17070841044187546):
												return True
									else:
										if(angle <= -0.17935995012521744):
											if(y_velocity <= -0.4330245852470398):
												if(angle_velocity <= -0.19668453186750412):
													if(angle <= -0.20540592074394226):
														if(y_velocity <= -0.5109458863735199):
															if(angle <= -0.313695952296257):
																if(x_velocity <= -0.6070241034030914):
																	if(angle_velocity <= -0.2956071197986603):
																		if(x_velocity <= -0.6256603896617889):
																			if(lander_x <= -0.19057030230760574):
																				return True
																		else:
																			return True
																else:
																	if(lander_y <= 1.0964854955673218):
																		if(x_velocity > -0.5373500883579254):
																			if(angle <= -0.3279412090778351):
																				return True
																	else:
																		if(lander_x <= -0.2093058079481125):
																			if(x_velocity > -0.5842687487602234):
																				return True
																		else:
																			return True
															else:
																if(x_velocity <= -0.4836074560880661):
																	if(lander_y <= 1.1334953904151917):
																		if(y_velocity > -0.5321527123451233):
																			return True
																else:
																	if(lander_x > -0.14405455440282822):
																		return True
														else:
															if(x_velocity > -0.5982315242290497):
																if(angle <= -0.2599492073059082):
																	return True
																else:
																	if(y_velocity <= -0.47442156076431274):
																		if(y_velocity <= -0.48567211627960205):
																			if(x_velocity > -0.5408328175544739):
																				return True
																	else:
																		if(lander_x > -0.13941650092601776):
																			return True
													else:
														if(angle > -0.18944034725427628):
															return True
												else:
													if(angle <= -0.23576706647872925):
														if(x_velocity <= -0.5415813624858856):
															if(angle <= -0.4017997086048126):
																if(angle_velocity <= -0.14701531827449799):
																	if(x_velocity > -0.5794510841369629):
																		return True
																else:
																	if(angle <= -0.47650036215782166):
																		if(y_velocity > -0.591996043920517):
																			return True
														else:
															if(lander_x <= -0.2238810509443283):
																if(y_velocity <= -0.5997353196144104):
																	if(lander_x <= -0.24918199330568314):
																		return True
																else:
																	return True
															else:
																if(angle_velocity <= -0.11672377586364746):
																	if(angle_velocity <= -0.16923823952674866):
																		if(y_velocity <= -0.4514021724462509):
																			if(x_velocity > -0.4411177337169647):
																				if(lander_x <= -0.12251529842615128):
																					return True
																		else:
																			return True
																	else:
																		if(y_velocity > -0.5715382993221283):
																			if(angle <= -0.2806345522403717):
																				if(x_velocity > -0.5356830954551697):
																					return True
																			else:
																				if(y_velocity <= -0.4643421918153763):
																					if(angle <= -0.2704138904809952):
																						if(lander_x > -0.13970622420310974):
																							return True
																				else:
																					return True
																else:
																	if(y_velocity <= -0.5278385281562805):
																		if(x_velocity > -0.40742215514183044):
																			return True
																	else:
																		if(angle <= -0.29466553032398224):
																			if(x_velocity <= -0.4519476890563965):
																				if(angle_velocity <= -0.08787873014807701):
																					return True
																			else:
																				if(angle_velocity <= -0.08251367881894112):
																					if(angle <= -0.3342030197381973):
																						return True
																				else:
																					return True
																		else:
																			if(angle_velocity <= -0.09223894774913788):
																				if(x_velocity > -0.431535080075264):
																					if(lander_y <= 1.120452105998993):
																						if(x_velocity > -0.34248849749565125):
																							return True
																					else:
																						return True
													else:
														if(x_velocity <= -0.3409680724143982):
															if(angle_velocity <= -0.18334412574768066):
																if(y_velocity <= -0.4420445114374161):
																	return True
															else:
																if(lander_y <= 0.5386775732040405):
																	if(x_velocity > -0.3683338314294815):
																		return True
														else:
															if(lander_y <= 1.2742559313774109):
																return True
											else:
												if(y_velocity <= -0.4094104766845703):
													if(x_velocity <= -0.3373663127422333):
														if(angle_velocity <= -0.13404980301856995):
															if(lander_x <= -0.13412489742040634):
																if(lander_y <= 1.0713378190994263):
																	return True
															else:
																return True
														else:
															if(angle <= -0.22553379833698273):
																if(x_velocity > -0.3820887953042984):
																	return True
													else:
														return True
												else:
													return True
										else:
											if(y_velocity <= -0.4337708652019501):
												if(lander_y > 1.29323410987854):
													if(x_velocity > -0.5180715620517731):
														if(angle_velocity <= -0.21660000085830688):
															if(lander_y <= 1.3219497203826904):
																if(lander_y <= 1.299863576889038):
																	if(angle_velocity > -0.29600100219249725):
																		return True
											else:
												if(angle <= -0.00803579343482852):
													if(y_velocity <= -0.36119943857192993):
														if(lander_x <= -0.048978567123413086):
															if(angle_velocity <= -0.18610703945159912):
																if(angle <= -0.07978971302509308):
																	if(x_velocity <= -0.3541252464056015):
																		if(angle_velocity <= -0.22655729949474335):
																			if(y_velocity <= -0.4039473682641983):
																				if(angle_velocity <= -0.2346111163496971):
																					if(angle <= -0.11017873510718346):
																						if(angle_velocity <= -0.2751312702894211):
																							return True
																						else:
																							if(angle_velocity > -0.2598416358232498):
																								return True
																					else:
																						if(y_velocity <= -0.41161997616291046):
																							return True
																	else:
																		if(lander_y <= 1.3376284837722778):
																			if(angle <= -0.08771895989775658):
																				if(lander_y <= 1.3183715343475342):
																					return True
																				else:
																					if(lander_y > 1.3271225690841675):
																						return True
																			else:
																				if(x_velocity > -0.29317427426576614):
																					return True
															else:
																if(y_velocity <= -0.4065731167793274):
																	if(y_velocity > -0.4108072370290756):
																		if(lander_y > 1.2151699662208557):
																			return True
																else:
																	if(angle <= -0.12085811421275139):
																		if(y_velocity <= -0.36271941661834717):
																			if(x_velocity > -0.3558248430490494):
																				if(angle_velocity <= -0.09198614582419395):
																					return True
																				else:
																					if(x_velocity > -0.26327161490917206):
																						return True
																	else:
																		if(x_velocity > -0.22532016038894653):
																			return True
														else:
															if(x_velocity <= -0.36446189880371094):
																if(lander_y <= 0.6396991312503815):
																	return True
																else:
																	if(x_velocity > -0.3678661584854126):
																		if(lander_y <= 0.9843174815177917):
																			return True
															else:
																if(angle <= -0.013763591181486845):
																	if(lander_y <= 1.3147606253623962):
																		if(angle <= -0.025734934955835342):
																			if(x_velocity <= -0.34728533029556274):
																				if(y_velocity > -0.3774220198392868):
																					return True
																			else:
																				if(x_velocity > -0.19715038686990738):
																					if(lander_x <= -0.034735774621367455):
																						return True
																	else:
																		if(y_velocity > -0.4041459262371063):
																			return True
													else:
														if(angle_velocity <= -0.06438378989696503):
															if(lander_x <= 0.14272303879261017):
																if(angle_velocity <= -0.08884239196777344):
																	if(lander_y <= 1.210818886756897):
																		if(x_velocity <= -0.1250804290175438):
																			return True
																		else:
																			if(x_velocity > -0.12362043559551239):
																				return True
																	else:
																		if(x_velocity > -0.2173689603805542):
																			return True
																else:
																	if(y_velocity <= -0.3359816372394562):
																		if(x_velocity <= -0.19562559574842453):
																			if(x_velocity <= -0.20183955878019333):
																				return True
																		else:
																			if(lander_x <= -0.032077884301543236):
																				return True
																	else:
																		if(lander_x <= 0.13328395038843155):
																			if(y_velocity <= -0.30143213272094727):
																				if(lander_y <= 1.1246248483657837):
																					if(angle <= -0.014325159136205912):
																						if(angle_velocity <= -0.07771759107708931):
																							return True
																						else:
																							if(x_velocity <= -0.12454863637685776):
																								if(x_velocity <= -0.1958720162510872):
																									return True
																							else:
																								if(x_velocity <= -0.08081450685858727):
																									return True
																								else:
																									if(angle_velocity <= -0.07152122259140015):
																										return True
																				else:
																					return True
															else:
																if(lander_y <= 0.7706000208854675):
																	if(x_velocity <= -0.2208804190158844):
																		if(y_velocity > -0.337039589881897):
																			if(lander_y <= 0.48573848605155945):
																				if(angle <= -0.12391063198447227):
																					return True
																			else:
																				return True
																	else:
																		if(x_velocity > -0.18279066681861877):
																			return True
																else:
																	if(y_velocity <= -0.3521493077278137):
																		if(lander_x <= 0.19722943007946014):
																			return True
																	else:
																		if(lander_x <= 0.2635515630245209):
																			if(x_velocity <= -0.13918402791023254):
																				if(angle_velocity <= -0.06700482964515686):
																					if(x_velocity <= -0.25093626976013184):
																						if(lander_x <= 0.20511451363563538):
																							return True
																					else:
																						return True
														else:
															if(angle <= -0.05002631992101669):
																if(angle_velocity <= -0.0614648275077343):
																	return True
												else:
													if(y_velocity > -0.32478559017181396):
														if(angle_velocity <= -0.08423697203397751):
															if(x_velocity <= -0.10184061527252197):
																if(angle_velocity <= -0.19225498288869858):
																	return True
																else:
																	if(angle <= 0.0030389951425604522):
																		return True
																	else:
																		if(y_velocity > -0.301647886633873):
																			if(angle_velocity <= -0.12690065801143646):
																				return True
															else:
																return True
														else:
															if(angle_velocity <= -0.06011812388896942):
																if(angle_velocity > -0.06475789099931717):
																	if(angle_velocity <= -0.06261859461665154):
																		return True
															else:
																return True
								else:
									if(lander_y <= 0.7050610482692719):
										if(angle <= -0.016425722744315863):
											if(y_velocity <= -0.2863665968179703):
												if(angle_velocity <= -0.08904643729329109):
													return True
												else:
													if(lander_y <= 0.6451204121112823):
														if(angle <= -0.037636296823620796):
															if(lander_y > 0.43963347375392914):
																return True
													else:
														if(angle_velocity > -0.07828659936785698):
															return True
											else:
												if(lander_x > -0.20630282908678055):
													return True
										else:
											if(y_velocity <= -0.27654169499874115):
												if(angle_velocity <= -0.06510399654507637):
													if(y_velocity <= -0.2940068542957306):
														return True
													else:
														if(angle_velocity <= -0.08824694529175758):
															if(lander_y > 0.6597811579704285):
																return True
												else:
													return True
											else:
												return True
									else:
										if(angle <= 0.004968515830114484):
											if(lander_y <= 1.1829760670661926):
												if(lander_y <= 0.9118808507919312):
													return True
												else:
													if(lander_y > 0.926120936870575):
														if(angle <= -0.0050670604687184095):
															if(lander_x > 0.16263370215892792):
																return True
														else:
															return True
										else:
											if(angle_velocity <= -0.08426381647586823):
												if(angle <= 0.022597305476665497):
													return True
												else:
													if(angle > 0.024377943947911263):
														return True
											else:
												if(x_velocity <= -0.058141548186540604):
													if(lander_y <= 1.0551754832267761):
														if(lander_x > 0.1210385337471962):
															if(x_velocity > -0.10559209063649178):
																return True
												else:
													if(y_velocity > -0.2911544591188431):
														return True
							else:
								if(lander_y <= 0.8993513584136963):
									if(angle <= -0.03608830086886883):
										if(y_velocity <= -0.28350360691547394):
											if(lander_y <= 0.7270106077194214):
												if(angle_velocity > -0.05718567967414856):
													if(angle_velocity <= -0.033221347257494926):
														if(x_velocity <= -0.020858132280409336):
															if(angle <= -0.10625071451067924):
																if(y_velocity <= -0.33073922991752625):
																	if(lander_x <= 0.08706545829772949):
																		return True
																else:
																	if(y_velocity > -0.31617048382759094):
																		return True
															else:
																if(y_velocity <= -0.2871044874191284):
																	if(angle_velocity <= -0.04851607233285904):
																		if(angle_velocity > -0.04945286735892296):
																			return True
																else:
																	if(lander_y <= 0.6390789747238159):
																		if(angle_velocity <= -0.044836126267910004):
																			if(angle_velocity > -0.04730966500937939):
																				return True
																	else:
																		return True
														else:
															return True
													else:
														return True
											else:
												if(y_velocity <= -0.3133092075586319):
													if(angle <= -0.09916141256690025):
														return True
													else:
														if(angle_velocity > -0.04292111285030842):
															if(y_velocity <= -0.3179745227098465):
																if(y_velocity <= -0.34161847829818726):
																	return True
															else:
																return True
												else:
													if(y_velocity <= -0.28776492178440094):
														if(angle_velocity <= -0.03477237932384014):
															if(angle_velocity <= -0.05153496190905571):
																if(x_velocity > -0.15227125585079193):
																	return True
															else:
																if(angle <= -0.0412223432213068):
																	return True
																else:
																	if(angle > -0.039473528042435646):
																		return True
										else:
											if(lander_y <= 0.469486266374588):
												if(angle_velocity <= -0.04586024023592472):
													if(x_velocity <= -0.06577751412987709):
														return True
											else:
												if(y_velocity <= -0.2753429412841797):
													if(angle <= -0.04135387763381004):
														return True
													else:
														if(angle_velocity <= -0.04640534892678261):
															return True
												else:
													if(lander_y <= 0.6207251846790314):
														return True
									else:
										if(y_velocity <= -0.2771090269088745):
											if(y_velocity <= -0.28404779732227325):
												if(x_velocity > -0.14623917639255524):
													if(lander_y <= 0.8852115869522095):
														if(angle <= -0.03160950541496277):
															if(angle <= -0.03189449943602085):
																if(angle <= -0.03372976556420326):
																	if(lander_y > 0.6550625860691071):
																		return True
															else:
																return True
														else:
															if(lander_x <= 0.16130437701940536):
																if(angle_velocity <= -0.05151553079485893):
																	if(angle_velocity > -0.05165383778512478):
																		return True
															else:
																if(lander_y > 0.748996376991272):
																	return True
													else:
														if(angle <= -0.021644615568220615):
															return True
											else:
												if(lander_y <= 0.6336986422538757):
													if(angle <= -0.0298122838139534):
														if(x_velocity > -0.07587196305394173):
															if(y_velocity <= -0.27869923412799835):
																return True
												else:
													if(angle <= -0.002378964680247009):
														if(lander_x <= 0.04290165938436985):
															if(y_velocity <= -0.2811284810304642):
																return True
														else:
															return True
										else:
											if(lander_y > 0.5317091047763824):
												if(x_velocity > -0.07187707349658012):
													if(y_velocity <= -0.2747925966978073):
														return True
													else:
														if(lander_y > 0.7707552313804626):
															return True
								else:
									if(y_velocity <= -0.29669009149074554):
										if(lander_x <= -0.003475999808870256):
											if(y_velocity <= -0.342788428068161):
												if(lander_x <= -0.07627568393945694):
													if(y_velocity <= -0.4099150002002716):
														if(angle_velocity <= -0.05680711194872856):
															return True
														else:
															if(lander_x <= -0.2660738676786423):
																if(x_velocity > -0.6355670988559723):
																	return True
															else:
																if(x_velocity > -0.48067183792591095):
																	if(lander_x <= -0.19408683478832245):
																		if(angle_velocity <= -0.03933914750814438):
																			if(lander_x <= -0.23800327628850937):
																				return True
																		else:
																			return True
																	else:
																		if(lander_y <= 1.1852357387542725):
																			if(angle <= -0.30683842301368713):
																				if(x_velocity > -0.3961202949285507):
																					return True
																		else:
																			if(angle_velocity <= -0.0436124037951231):
																				if(angle_velocity <= -0.05217815563082695):
																					return True
																			else:
																				return True
													else:
														if(x_velocity > -0.33552083373069763):
															if(y_velocity <= -0.37997524440288544):
																return True
															else:
																if(y_velocity > -0.367921844124794):
																	return True
												else:
													if(angle_velocity <= -0.04700538143515587):
														if(y_velocity > -0.37741243839263916):
															if(lander_x <= -0.04243931919336319):
																return True
															else:
																if(y_velocity > -0.3486199826002121):
																	return True
											else:
												if(lander_x <= -0.03591289557516575):
													if(angle_velocity <= -0.036549970507621765):
														return True
													else:
														if(y_velocity > -0.312905415892601):
															return True
												else:
													if(y_velocity > -0.32739101350307465):
														if(x_velocity <= -0.08919725939631462):
															if(y_velocity > -0.31665223836898804):
																if(x_velocity <= -0.16322143375873566):
																	return True
														else:
															if(lander_y > 1.0605363249778748):
																if(lander_y <= 1.31239652633667):
																	return True
																else:
																	if(x_velocity > -0.051038533449172974):
																		return True
										else:
											if(y_velocity <= -0.3068675696849823):
												if(angle <= -0.05213010683655739):
													if(x_velocity > -0.16359515488147736):
														return True
											else:
												if(angle_velocity > -0.05088780261576176):
													if(lander_x <= 0.21108727902173996):
														if(lander_y <= 1.096395194530487):
															if(angle <= 0.008978136640507728):
																return True
									else:
										if(x_velocity <= -0.06396332010626793):
											if(x_velocity > -0.09581229835748672):
												if(angle <= 0.005803724052384496):
													if(x_velocity <= -0.08584951609373093):
														if(angle <= -0.020941817201673985):
															return True
													else:
														if(y_velocity <= -0.2916957288980484):
															if(angle <= -0.002429311629384756):
																return True
														else:
															return True
										else:
											if(angle <= 0.015422617085278034):
												if(lander_y <= 1.232492446899414):
													return True
												else:
													if(lander_y > 1.3102829456329346):
														return True
											else:
												if(y_velocity > -0.2848079204559326):
													if(y_velocity <= -0.2767981141805649):
														return True
						else:
							if(angle <= 0.23191983997821808):
								if(angle_velocity <= -0.05972559005022049):
									if(angle <= 0.0912783332169056):
										if(y_velocity <= -0.28658297657966614):
											if(lander_x <= 0.039663076400756836):
												if(y_velocity > -0.3101351112127304):
													if(angle > 0.027676471509039402):
														if(angle <= 0.0576394647359848):
															return True
														else:
															if(angle_velocity > -0.07374140247702599):
																return True
											else:
												if(angle_velocity <= -0.10369608923792839):
													if(lander_y <= 1.1294952034950256):
														if(angle_velocity <= -0.36916184425354004):
															if(angle <= 0.06587366387248039):
																return True
														else:
															if(lander_x <= 0.06910424306988716):
																return True
													else:
														if(y_velocity <= -0.30115795135498047):
															if(lander_y <= 1.1519516706466675):
																if(y_velocity > -0.36087512969970703):
																	return True
														else:
															return True
												else:
													if(angle_velocity <= -0.0598941296339035):
														if(angle <= 0.05225302837789059):
															if(angle_velocity <= -0.0939495638012886):
																return True
															else:
																if(x_velocity <= -0.030840015038847923):
																	if(lander_y <= 1.2010349035263062):
																		if(angle <= 0.02745828777551651):
																			if(y_velocity > -0.3056199252605438):
																				return True
																		else:
																			if(angle_velocity <= -0.09268640726804733):
																				if(lander_x > 0.1837688460946083):
																					return True
																else:
																	if(lander_y > 0.9904069006443024):
																		return True
										else:
											if(x_velocity <= -0.0033900575945153832):
												if(angle <= 0.05077522248029709):
													if(lander_y <= 0.8034813106060028):
														if(y_velocity > -0.27736397087574005):
															return True
													else:
														if(lander_x > 0.042511845007538795):
															if(angle > 0.026534578762948513):
																if(x_velocity <= -0.048390813171863556):
																	if(lander_y > 0.998577892780304):
																		return True
																else:
																	return True
												else:
													if(angle_velocity <= -0.09065785631537437):
														if(lander_y <= 0.9230482876300812):
															if(angle_velocity <= -0.35589443147182465):
																return True
														else:
															return True
											else:
												if(y_velocity <= -0.2744954973459244):
													return True
									else:
										if(lander_x <= 0.2587932199239731):
											if(lander_x <= 0.05486712232232094):
												return True
											else:
												if(x_velocity > -0.3030150681734085):
													if(x_velocity <= -0.1765737608075142):
														if(x_velocity <= -0.18656593561172485):
															if(angle <= 0.11395077407360077):
																return True
														else:
															return True
										else:
											if(lander_y <= 1.2129668593406677):
												if(y_velocity <= -0.32512956857681274):
													if(lander_y <= 1.168076753616333):
														return True
												else:
													return True
											else:
												if(x_velocity <= 0.047188255935907364):
													if(y_velocity > -0.2758232653141022):
														if(x_velocity <= -0.04902367852628231):
															return True
												else:
													return True
								else:
									if(lander_x <= 0.037775563076138496):
										if(y_velocity > -0.29584261775016785):
											if(angle_velocity <= -0.05103209242224693):
												return True
											else:
												if(y_velocity > -0.27884821593761444):
													if(lander_x <= 0.0034049036912620068):
														return True
									else:
										if(x_velocity > -0.073564313352108):
											if(lander_x <= 0.07187323644757271):
												if(lander_x <= 0.07159404829144478):
													if(x_velocity > -0.05135893262922764):
														if(angle <= 0.029172008857131004):
															if(angle > 0.029036596417427063):
																return True
												else:
													return True
					else:
						if(angle <= 0.034930093213915825):
							if(lander_y <= 0.5064136981964111):
								if(angle_velocity <= -0.06040847301483154):
									if(y_velocity <= -0.2535327672958374):
										if(angle <= -0.05017863027751446):
											if(x_velocity > -0.13901380449533463):
												return True
										else:
											if(lander_x <= -0.011474322993308306):
												if(lander_y > 0.305573508143425):
													if(angle_velocity <= -0.08623545616865158):
														return True
													else:
														if(lander_y <= 0.32553939521312714):
															return True
														else:
															if(angle_velocity <= -0.06177215836942196):
																if(angle_velocity <= -0.07961239293217659):
																	if(x_velocity > -0.03432629816234112):
																		return True
															else:
																return True
											else:
												if(lander_y > 0.15798208117485046):
													return True
									else:
										if(angle <= 0.019497358240187168):
											if(lander_y <= 0.151559479534626):
												if(angle <= -0.01771371066570282):
													if(angle_velocity <= -0.06213214062154293):
														if(y_velocity <= -0.2358163446187973):
															if(angle <= -0.049251850694417953):
																return True
															else:
																if(lander_y > 0.1297844871878624):
																	return True
														else:
															if(lander_x <= -0.14672942459583282):
																if(lander_x <= -0.17687151581048965):
																	return True
															else:
																return True
												else:
													if(angle_velocity <= -0.0768754780292511):
														if(lander_y > 0.02447665180079639):
															return True
													else:
														if(y_velocity > -0.22891531884670258):
															return True
											else:
												if(angle <= -0.0032971256878226995):
													if(lander_x <= 0.09063887596130371):
														if(angle <= -0.012972843833267689):
															return True
														else:
															if(angle > -0.012694571167230606):
																if(angle_velocity <= -0.06974704191088676):
																	return True
																else:
																	if(x_velocity > -0.027516911271959543):
																		return True
													else:
														if(lander_y > 0.2776852548122406):
															return True
												else:
													if(y_velocity <= -0.2518458515405655):
														if(x_velocity <= -0.03732426092028618):
															return True
													else:
														if(angle > -0.0022858771844767034):
															if(angle_velocity <= -0.06998409330844879):
																return True
															else:
																if(angle_velocity > -0.06887462735176086):
																	if(lander_y > 0.3043612092733383):
																		return True
										else:
											if(y_velocity > -0.22808357328176498):
												return True
								else:
									if(y_velocity <= -0.2400168478488922):
										if(angle <= -0.026978999376296997):
											if(lander_y <= 0.30345430970191956):
												if(y_velocity <= -0.25478316843509674):
													if(angle <= -0.05877453275024891):
														if(lander_y <= 0.1870751455426216):
															if(angle <= -0.09331268817186356):
																return True
														else:
															return True
													else:
														if(lander_y > 0.300640270113945):
															if(angle_velocity <= -0.045744482427835464):
																return True
												else:
													if(angle <= -0.04732763580977917):
														if(x_velocity > -0.09919827803969383):
															return True
													else:
														if(lander_y <= 0.21261925250291824):
															if(angle_velocity <= -0.05174741521477699):
																if(x_velocity > -0.05522949621081352):
																	return True
															else:
																if(lander_x <= -0.23906293511390686):
																	return True
																else:
																	if(lander_y <= 0.008540538605302572):
																		return True
														else:
															if(lander_x > -0.16728148609399796):
																if(x_velocity <= -0.04996753856539726):
																	if(lander_x > 0.018435811973176897):
																		return True
																else:
																	return True
											else:
												if(y_velocity <= -0.26821960508823395):
													if(angle <= -0.04693380370736122):
														return True
												else:
													if(angle_velocity <= -0.03502657637000084):
														if(lander_x <= -0.06985316053032875):
															if(x_velocity <= -0.019727726466953754):
																if(y_velocity > -0.24895920604467392):
																	return True
															else:
																return True
														else:
															if(y_velocity <= -0.24487199634313583):
																if(x_velocity <= -0.11728962883353233):
																	if(y_velocity <= -0.2559114843606949):
																		return True
																else:
																	return True
															else:
																if(angle_velocity > -0.042936887592077255):
																	return True
													else:
														if(x_velocity > -0.061256490647792816):
															return True
										else:
											if(lander_y <= 0.3868850916624069):
												if(y_velocity <= -0.24550068378448486):
													if(angle <= -0.024723769165575504):
														if(angle > -0.025082661770284176):
															return True
													else:
														if(angle_velocity <= -0.054817020893096924):
															if(angle_velocity > -0.055450962856411934):
																return True
												else:
													if(angle <= -0.012742995750159025):
														if(lander_y > 0.2760889083147049):
															return True
													else:
														if(y_velocity <= -0.24428729712963104):
															if(y_velocity > -0.24458645284175873):
																return True
											else:
												if(lander_x <= 0.0450282096862793):
													if(y_velocity <= -0.24334080517292023):
														if(angle <= -0.01838515792042017):
															if(angle_velocity > -0.04829507879912853):
																if(lander_x <= 0.03531451150774956):
																	return True
														else:
															if(x_velocity <= 0.05778321996331215):
																if(x_velocity > -0.011092393659055233):
																	if(x_velocity <= -0.00418945134151727):
																		return True
																	else:
																		if(lander_y <= 0.48397214710712433):
																			if(lander_y <= 0.4557829946279526):
																				if(lander_y > 0.4191170185804367):
																					if(angle_velocity > -0.042285582050681114):
																						return True
																		else:
																			if(angle_velocity <= -0.05122653767466545):
																				return True
															else:
																return True
													else:
														if(angle <= 0.009552558418363333):
															return True
												else:
													if(x_velocity > -0.0911533460021019):
														if(y_velocity <= -0.2600053548812866):
															if(angle_velocity <= -0.04805313982069492):
																return True
														else:
															return True
									else:
										if(lander_y <= 0.19187165051698685):
											if(angle <= -0.020316937007009983):
												if(x_velocity <= -0.029020866379141808):
													if(y_velocity <= -0.23269294202327728):
														if(angle <= -0.045829424634575844):
															if(y_velocity <= -0.23651983588933945):
																return True
														else:
															if(lander_x > 0.057770490646362305):
																return True
													else:
														if(y_velocity <= -0.2259705513715744):
															if(lander_y > 0.011627081548795104):
																return True
												else:
													if(lander_y > 0.01037331029510824):
														return True
											else:
												if(lander_x <= -0.20268094539642334):
													if(lander_y <= 0.17623337358236313):
														return True
												else:
													if(lander_x <= 0.04868140257894993):
														if(lander_y > 0.15951377153396606):
															if(lander_y <= 0.16665298491716385):
																return True
													else:
														if(angle <= -0.00803783256560564):
															return True
										else:
											if(angle <= 0.008964150212705135):
												if(lander_y <= 0.295793741941452):
													if(angle <= -0.031182220205664635):
														if(lander_y <= 0.2916702926158905):
															return True
													else:
														if(y_velocity <= -0.2264702022075653):
															if(y_velocity <= -0.22923804819583893):
																if(x_velocity <= -0.021200704388320446):
																	if(angle <= -0.011414513923227787):
																		if(lander_x > -0.023135279770940542):
																			if(lander_x <= 0.07161402702331543):
																				return True
																			else:
																				if(y_velocity > -0.23272212594747543):
																					return True
																else:
																	if(angle <= 0.002715824404731393):
																		if(angle_velocity <= -0.038494376465678215):
																			return True
																		else:
																			if(y_velocity <= -0.23635271936655045):
																				return True
														else:
															if(angle_velocity <= -0.0400046780705452):
																return True
															else:
																if(lander_y <= 0.23086553812026978):
																	return True
												else:
													if(lander_y <= 0.4847024381160736):
														if(y_velocity <= -0.22604333609342575):
															if(angle <= -0.047422030940651894):
																if(lander_x > 0.03597393038216978):
																	return True
															else:
																if(angle_velocity <= -0.03338231146335602):
																	if(lander_y > 0.2988537400960922):
																		if(y_velocity <= -0.2378656566143036):
																			if(lander_y <= 0.3742271065711975):
																				if(lander_y <= 0.3361288011074066):
																					return True
																				else:
																					if(lander_x <= -0.208277128636837):
																						return True
																			else:
																				return True
																		else:
																			if(angle_velocity <= -0.05317089706659317):
																				if(angle_velocity <= -0.05389358475804329):
																					return True
																			else:
																				return True
														else:
															if(x_velocity <= 0.01014522387413308):
																if(lander_y <= 0.312025249004364):
																	return True
															else:
																return True
													else:
														if(angle_velocity > -0.03695204667747021):
															return True
											else:
												if(lander_y <= 0.39980554580688477):
													if(angle_velocity <= -0.0341972541064024):
														if(angle_velocity <= -0.05086044780910015):
															if(angle > 0.014690518844872713):
																return True
													else:
														return True
												else:
													if(lander_y <= 0.42888352274894714):
														return True
													else:
														if(angle > 0.015268184244632721):
															if(lander_x > -0.17105422168970108):
																if(angle > 0.019403917714953423):
																	return True
							else:
								if(angle_velocity <= -0.05284256301820278):
									if(x_velocity <= -0.10827244073152542):
										if(y_velocity <= -0.26872535049915314):
											if(angle <= -0.0041271538939327):
												return True
										else:
											if(lander_x <= 0.06066169869154692):
												return True
											else:
												if(lander_x > 0.21067585796117783):
													if(x_velocity > -0.12532290443778038):
														return True
									else:
										if(angle <= -0.00010752363596111536):
											if(lander_x <= -0.06001458130776882):
												if(lander_x <= -0.06097531318664551):
													return True
											else:
												return True
										else:
											if(x_velocity <= -0.07380442321300507):
												if(angle_velocity <= -0.08547554910182953):
													return True
												else:
													if(x_velocity <= -0.0753205195069313):
														if(angle <= 0.0007209324394352734):
															if(y_velocity > -0.26561057567596436):
																return True
														else:
															if(lander_x > 0.14763760566711426):
																return True
											else:
												if(lander_y <= 0.7227818071842194):
													if(y_velocity <= -0.25040990114212036):
														if(angle <= 0.021464388817548752):
															if(x_velocity > -0.053918564692139626):
																if(angle_velocity <= -0.06892808526754379):
																	if(angle_velocity <= -0.07234077528119087):
																		return True
																else:
																	return True
														else:
															if(x_velocity > 0.02297267783433199):
																if(angle_velocity <= -0.06391268596053123):
																	return True
													else:
														if(lander_y > 0.5163798630237579):
															if(y_velocity <= -0.24693111330270767):
																if(angle_velocity <= -0.060279881581664085):
																	return True
															else:
																return True
												else:
													if(angle <= 0.002522009424865246):
														if(angle <= 0.0014628705102950335):
															return True
													else:
														if(y_velocity <= -0.23857375979423523):
															return True
														else:
															if(x_velocity > -0.029036267660558224):
																return True
								else:
									if(x_velocity <= -0.03969418443739414):
										if(angle <= -0.004477277863770723):
											if(angle_velocity <= -0.04905989393591881):
												if(angle > -0.020632019266486168):
													if(lander_x <= 0.04906487464904785):
														if(x_velocity > -0.062626201659441):
															return True
													else:
														return True
											else:
												if(x_velocity <= -0.08537657558917999):
													if(angle_velocity <= -0.03913089446723461):
														if(x_velocity <= -0.08689343929290771):
															return True
													else:
														if(y_velocity <= -0.2715301811695099):
															if(x_velocity > -0.10004038363695145):
																return True
														else:
															if(lander_x <= -0.028950500302016735):
																return True
												else:
													if(angle <= -0.006619237828999758):
														if(angle <= -0.0167265422642231):
															if(lander_y <= 0.5122690498828888):
																if(y_velocity > -0.26554323732852936):
																	return True
															else:
																return True
														else:
															if(lander_x <= 0.06441674008965492):
																if(y_velocity <= -0.25397640466690063):
																	if(lander_y > 0.7686985731124878):
																		return True
															else:
																if(angle > -0.015261868480592966):
																	return True
										else:
											if(y_velocity <= -0.2564547210931778):
												if(x_velocity > -0.06182005628943443):
													if(angle <= 0.003093022503890097):
														return True
													else:
														if(lander_y <= 0.95409095287323):
															if(angle <= 0.007898449199274182):
																if(y_velocity <= -0.2625900208950043):
																	if(lander_x > 0.059391019865870476):
																		return True
											else:
												if(lander_x <= 0.14655842632055283):
													if(angle <= 0.008637923747301102):
														if(x_velocity > -0.045624028891325):
															if(lander_y > 0.6419882774353027):
																return True
												else:
													return True
									else:
										if(lander_y <= 0.5522063076496124):
											if(lander_y <= 0.5241343975067139):
												if(angle <= 0.029883023351430893):
													return True
											else:
												if(y_velocity <= -0.23848091810941696):
													if(lander_x <= -0.025369883282110095):
														if(lander_y > 0.548709362745285):
															if(angle <= 0.01152773480862379):
																return True
													else:
														if(x_velocity > -0.022533725015819073):
															return True
												else:
													if(x_velocity > -0.016883855685591698):
														if(lander_y > 0.5267400443553925):
															return True
										else:
											if(y_velocity <= -0.2282232791185379):
												if(angle <= 0.016525248996913433):
													if(angle_velocity <= -0.033497318625450134):
														if(y_velocity <= -0.23080382496118546):
															if(y_velocity <= -0.27197331190109253):
																if(y_velocity <= -0.27213045954704285):
																	return True
															else:
																if(angle_velocity <= -0.034667354077100754):
																	if(angle <= 0.015077714342623949):
																		return True
																	else:
																		if(lander_x <= -0.014067841693758965):
																			return True
																else:
																	if(lander_y <= 0.7341466546058655):
																		return True
														else:
															if(y_velocity > -0.22896210849285126):
																return True
												else:
													if(y_velocity <= -0.2586463689804077):
														if(lander_y > 0.7615549564361572):
															if(lander_x <= 0.05675811693072319):
																if(x_velocity > 0.030231313779950142):
																	return True
															else:
																return True
													else:
														if(x_velocity <= -0.03337454795837402):
															if(lander_x <= 0.0971221923828125):
																return True
														else:
															if(angle_velocity > -0.04700267128646374):
																if(angle <= 0.018388327211141586):
																	if(y_velocity > -0.2452925369143486):
																		return True
																else:
																	return True
											else:
												if(lander_y > 0.7680761516094208):
													return True
						else:
							if(x_velocity <= 0.025186216458678246):
								if(angle_velocity <= -0.071587685495615):
									if(angle <= 0.1095874160528183):
										if(x_velocity <= -0.030848713591694832):
											if(lander_x <= 0.2282298132777214):
												if(y_velocity <= -0.2566540092229843):
													if(x_velocity <= -0.03515925072133541):
														if(lander_y <= 0.9161396026611328):
															if(lander_x <= 0.1795550361275673):
																if(angle <= 0.04489714466035366):
																	if(x_velocity > -0.06841016933321953):
																		return True
															else:
																if(lander_x <= 0.2239033207297325):
																	return True
														else:
															if(lander_x <= 0.1899833232164383):
																return True
												else:
													if(angle_velocity <= -0.19618981331586838):
														if(angle_velocity <= -0.2810531258583069):
															if(x_velocity <= -0.0608994010835886):
																if(x_velocity > -0.18246731162071228):
																	return True
														else:
															return True
													else:
														if(x_velocity > -0.035411085933446884):
															if(lander_y <= 1.0392673015594482):
																return True
										else:
											if(y_velocity <= -0.24221179634332657):
												if(angle <= 0.07443808019161224):
													return True
												else:
													if(x_velocity <= -0.01105482317507267):
														if(y_velocity <= -0.25863175094127655):
															if(lander_y > 1.177529513835907):
																return True
														else:
															if(lander_y <= 1.1389644742012024):
																return True
													else:
														if(y_velocity <= -0.2670303285121918):
															if(y_velocity <= -0.27025872468948364):
																return True
															else:
																if(angle > 0.0959988385438919):
																	return True
														else:
															return True
											else:
												if(lander_y <= 0.9253587424755096):
													if(angle_velocity <= -0.0964064821600914):
														return True
									else:
										if(angle <= 0.2809743285179138):
											if(x_velocity > -0.11730331182479858):
												if(y_velocity <= -0.24049507081508636):
													if(lander_y <= 1.2089558243751526):
														if(angle <= 0.15761693567037582):
															if(angle_velocity <= -0.13329292088747025):
																if(y_velocity > -0.2707895487546921):
																	if(y_velocity <= -0.2581660896539688):
																		if(angle_velocity <= -0.2602323293685913):
																			return True
																	else:
																		return True
													else:
														if(angle > 0.11862792074680328):
															if(lander_x <= 0.2416369915008545):
																return True
															else:
																if(angle_velocity <= -0.16942324489355087):
																	if(lander_y <= 1.2879590392112732):
																		if(y_velocity <= -0.25517041981220245):
																			return True
																		else:
																			if(y_velocity > -0.2500557228922844):
																				return True
												else:
													if(angle_velocity <= -0.2143898606300354):
														if(angle <= 0.19621512293815613):
															if(lander_x > -0.019423335790634155):
																return True
								else:
									if(lander_y <= 1.0452626943588257):
										if(x_velocity <= -0.020400109700858593):
											if(y_velocity <= -0.25144486129283905):
												if(lander_y <= 0.9741859138011932):
													if(angle_velocity <= -0.058106349781155586):
														if(angle_velocity > -0.06286430172622204):
															return True
										else:
											if(lander_y <= 0.8571777045726776):
												if(lander_x <= 0.16427383571863174):
													if(x_velocity <= -0.018550340086221695):
														return True
												else:
													return True
											else:
												if(lander_y <= 0.986799955368042):
													if(angle <= 0.08642616868019104):
														if(lander_x <= 0.13354911655187607):
															return True
														else:
															if(lander_x > 0.13364215195178986):
																return True
												else:
													if(y_velocity <= -0.2546733021736145):
														if(x_velocity <= -0.010123291984200478):
															if(lander_y > 1.0212674140930176):
																return True
													else:
														if(angle <= 0.07542070746421814):
															if(x_velocity > 0.0023838841589167714):
																if(y_velocity > -0.2542535215616226):
																	return True
									else:
										if(y_velocity <= -0.2708752453327179):
											if(x_velocity > 0.016764324624091387):
												return True
										else:
											if(x_velocity <= 0.013716375455260277):
												if(lander_y <= 1.1067175269126892):
													if(angle > 0.053557682782411575):
														if(lander_y > 1.0700825452804565):
															if(angle <= 0.06766245141625404):
																return True
											else:
												if(y_velocity <= -0.2602417767047882):
													if(lander_x <= 0.04520964436233044):
														return True
							else:
								if(lander_y <= 0.5665508806705475):
									if(angle <= 0.26563510298728943):
										if(y_velocity > -0.22618267685174942):
											if(y_velocity <= -0.22588810324668884):
												return True
								else:
									if(angle <= 0.08744543418288231):
										if(lander_y <= 0.6420569717884064):
											if(lander_y <= 0.6070963740348816):
												return True
										else:
											if(y_velocity > -0.2731200158596039):
												if(y_velocity <= -0.23672164976596832):
													return True
												else:
													if(x_velocity > 0.02860201057046652):
														return True
									else:
										if(y_velocity <= -0.24430807679891586):
											if(angle <= 0.35814069211483):
												if(angle <= 0.16630902886390686):
													if(angle_velocity <= -0.07869734987616539):
														if(lander_y <= 1.1464273929595947):
															if(angle <= 0.10493464395403862):
																return True
															else:
																if(angle_velocity <= -0.12545626237988472):
																	if(lander_y > 1.1010660529136658):
																		return True
														else:
															if(x_velocity <= 0.05530468001961708):
																if(angle_velocity <= -0.12411325797438622):
																	if(y_velocity <= -0.25613246858119965):
																		return True
																else:
																	if(angle <= 0.11198022589087486):
																		if(y_velocity > -0.2632356882095337):
																			return True
																	else:
																		if(lander_x > 0.17672505229711533):
																			return True
															else:
																if(y_velocity <= -0.2695635259151459):
																	if(angle <= 0.13553710281848907):
																		return True
																else:
																	if(lander_x <= 0.06755213811993599):
																		if(x_velocity <= 0.09038050100207329):
																			return True
																	else:
																		return True
													else:
														if(lander_x <= 0.14297018200159073):
															if(angle <= 0.11749140173196793):
																if(x_velocity <= 0.0647285096347332):
																	if(lander_y <= 1.210197925567627):
																		if(y_velocity <= -0.24939091503620148):
																			if(angle <= 0.09439653530716896):
																				if(angle_velocity <= -0.05749609135091305):
																					return True
																		else:
																			if(x_velocity <= 0.04607129655778408):
																				if(lander_y > 1.1609861850738525):
																					return True
																	else:
																		if(lander_y <= 1.2297842502593994):
																			if(y_velocity > -0.251080185174942):
																				return True
																else:
																	if(angle_velocity <= -0.046996111050248146):
																		return True
																	else:
																		if(angle > 0.10676972568035126):
																			return True
														else:
															return True
												else:
													if(angle_velocity <= -0.2895004451274872):
														return True
										else:
											if(angle <= 0.18603547662496567):
												if(angle_velocity <= -0.06871051341295242):
													if(x_velocity <= 0.039872072637081146):
														if(lander_y <= 0.9838990867137909):
															if(angle <= 0.12621251866221428):
																return True
													else:
														if(angle_velocity <= -0.12319521978497505):
															return True
														else:
															if(angle <= 0.13856685906648636):
																if(lander_y <= 1.2852905988693237):
																	if(lander_y <= 0.9667399525642395):
																		if(x_velocity > 0.05916708894073963):
																			return True
																	else:
																		return True
															else:
																if(lander_y > 1.1982311010360718):
																	if(x_velocity <= 0.09304017201066017):
																		if(angle_velocity <= -0.0915611982345581):
																			if(y_velocity <= -0.2395741418004036):
																				return True
																	else:
																		return True
												else:
													if(x_velocity <= 0.0782221369445324):
														if(lander_y <= 0.9920945465564728):
															if(lander_x <= 0.12876948714256287):
																return True
													else:
														if(lander_y > 1.2898206114768982):
															if(lander_x <= 0.0880582332611084):
																return True
											else:
												if(angle_velocity <= -0.15143311768770218):
													if(angle <= 0.2426048144698143):
														if(lander_x > 0.12378249317407608):
															return True
													else:
														if(lander_x > 0.16154446452856064):
															if(y_velocity <= -0.22632065415382385):
																if(angle_velocity <= -0.2848382294178009):
																	return True
				else:
					if(x_velocity <= -0.33664602041244507):
						if(angle <= -0.11459648981690407):
							if(angle_velocity <= -0.09190931171178818):
								if(y_velocity <= -0.2519789934158325):
									if(angle_velocity <= -0.4578545540571213):
										if(angle <= -0.15882235020399094):
											return True
									else:
										if(x_velocity <= -0.6710363924503326):
											if(y_velocity <= -0.47695353627204895):
												if(x_velocity > -0.6842849552631378):
													return True
										else:
											if(lander_y <= 1.3608826398849487):
												if(lander_x <= -0.0814695805311203):
													if(lander_y <= 1.3590882420539856):
														if(lander_y <= 1.3492493033409119):
															if(lander_x > -0.09263530001044273):
																return True
														else:
															return True
											else:
												if(angle_velocity <= -0.18298624455928802):
													return True
												else:
													if(angle_velocity <= -0.15240415930747986):
														if(lander_y <= 1.424329936504364):
															return True
														else:
															if(angle_velocity <= -0.16597214341163635):
																if(y_velocity <= -0.32941558957099915):
																	return True
													else:
														if(lander_x <= -0.12115335464477539):
															return True
								else:
									if(angle_velocity <= -0.152280293405056):
										if(lander_x > -0.16842999309301376):
											if(angle > -0.333836629986763):
												return True
							else:
								if(y_velocity <= -0.4107735753059387):
									if(x_velocity > -0.5631673336029053):
										if(angle_velocity <= -0.04858700558543205):
											if(angle_velocity > -0.08055906742811203):
												if(y_velocity > -0.5393632650375366):
													return True
								else:
									if(angle <= -0.31698454916477203):
										if(x_velocity > -0.5021641850471497):
											return True
						else:
							if(x_velocity <= -0.340665265917778):
								if(angle <= -0.09723096713423729):
									if(lander_x > -0.08354687690734863):
										if(angle_velocity <= -0.35685573518276215):
											return True
							else:
								return True
					else:
						if(angle <= 0.13649334758520126):
							if(x_velocity <= -0.12586691230535507):
								if(angle <= -0.04123163782060146):
									if(angle_velocity <= -0.05977979861199856):
										if(lander_x <= -0.01974854525178671):
											if(y_velocity <= -0.29226353764533997):
												if(angle_velocity <= -0.30927467346191406):
													if(angle <= -0.073415607213974):
														return True
												else:
													return True
											else:
												if(angle_velocity <= -0.08661189675331116):
													if(lander_y > 1.3895248174667358):
														return True
												else:
													if(angle_velocity > -0.07625826075673103):
														if(angle_velocity <= -0.06168362684547901):
															return True
									else:
										if(y_velocity <= -0.3848797380924225):
											if(y_velocity > -0.4178415685892105):
												if(lander_y > 1.3663490414619446):
													return True
										else:
											if(lander_x > -0.04711418226361275):
												if(y_velocity > -0.3718634694814682):
													return True
								else:
									if(lander_x > -0.028066777624189854):
										if(x_velocity > -0.21400336176156998):
											if(y_velocity > -0.31842872500419617):
												if(y_velocity <= -0.275382399559021):
													return True
							else:
								if(lander_y > 1.3478015065193176):
									if(lander_y <= 1.3526949882507324):
										if(angle_velocity <= -0.0776585042476654):
											return True
									else:
										return True
						else:
							if(lander_y <= 1.3533155918121338):
								if(y_velocity <= -0.25446075201034546):
									return True
							else:
								if(y_velocity <= -0.22856424748897552):
									if(lander_x <= 0.09026093408465385):
										if(lander_y <= 1.381516456604004):
											if(angle_velocity <= -0.08300057239830494):
												return True
								else:
									if(angle_velocity > -0.0935678705573082):
										return True
			else:
				if(lander_y <= 0.4006982296705246):
					if(y_velocity <= -0.23569615185260773):
						if(angle <= -0.058152781799435616):
							if(y_velocity <= -0.25839124619960785):
								if(x_velocity <= -0.13590740412473679):
									if(y_velocity <= -0.29675520956516266):
										if(angle <= -0.19683077186346054):
											if(angle_velocity <= 0.09490758925676346):
												return True
									else:
										if(angle_velocity > -0.01466236962005496):
											if(y_velocity <= -0.27699221670627594):
												if(angle_velocity <= 0.0550838578492403):
													return True
												else:
													if(x_velocity > -0.1734641119837761):
														if(lander_x > 0.041015053167939186):
															return True
											else:
												if(lander_x <= 0.14075402915477753):
													if(angle <= -0.16150250285863876):
														return True
								else:
									if(lander_x <= 0.14820809662342072):
										if(y_velocity <= -0.2689857631921768):
											if(angle <= -0.11797886714339256):
												if(x_velocity > -0.11671330034732819):
													return True
										else:
											if(angle <= -0.10477631539106369):
												if(y_velocity > -0.2667526602745056):
													return True
											else:
												if(y_velocity <= -0.2687617987394333):
													return True
												else:
													if(x_velocity > -0.1222674734890461):
														if(angle_velocity <= -0.009205518756061792):
															if(lander_x <= -0.23955176025629044):
																return True
															else:
																if(lander_y > 0.3038367033004761):
																	return True
														else:
															if(angle <= -0.09133792668581009):
																if(angle > -0.09316127747297287):
																	return True
									else:
										return True
							else:
								if(lander_y <= 0.1527993083000183):
									if(x_velocity <= -0.007451545679941773):
										if(angle <= -0.09280223399400711):
											return True
										else:
											if(angle_velocity <= -0.03134900890290737):
												return True
											else:
												if(angle_velocity <= -0.024035007692873478):
													if(lander_y > 0.07305090129375458):
														return True
									else:
										if(lander_y <= 0.147546648979187):
											return True
								else:
									if(x_velocity <= -0.07946266233921051):
										if(y_velocity > -0.25577312707901):
											if(x_velocity <= -0.11398253962397575):
												if(x_velocity <= -0.13120853900909424):
													if(x_velocity > -0.13429614901542664):
														return True
											else:
												if(angle_velocity <= 0.06525545194745064):
													if(angle <= -0.07024536281824112):
														return True
													else:
														if(lander_x > 0.0068527692928910255):
															return True
									else:
										if(angle <= -0.05995078384876251):
											if(x_velocity <= -0.024109167978167534):
												if(y_velocity <= -0.2559092044830322):
													if(y_velocity > -0.25742679834365845):
														return True
											else:
												return True
										else:
											if(angle > -0.059398721903562546):
												return True
						else:
							if(angle_velocity <= -0.015326505992561579):
								if(lander_y <= 0.25232017040252686):
									if(angle <= -0.03989301435649395):
										if(y_velocity > -0.24880661815404892):
											if(lander_y <= 0.1596236675977707):
												if(x_velocity > -0.011941983830183744):
													if(lander_x > -0.16848482936620712):
														return True
											else:
												if(lander_y <= 0.21536662429571152):
													return True
									else:
										if(lander_x > 0.12734685093164444):
											if(lander_y > 0.2011852115392685):
												return True
								else:
									if(angle <= -0.019317341037094593):
										if(y_velocity > -0.2652069330215454):
											if(angle_velocity <= -0.026273712515830994):
												if(angle_velocity > -0.032510457560420036):
													if(lander_x > -0.2069142386317253):
														if(lander_x <= 0.08081717416644096):
															if(angle <= -0.023284176364541054):
																return True
															else:
																if(lander_y > 0.34060676395893097):
																	return True
											else:
												if(x_velocity <= -0.050697602331638336):
													if(lander_y <= 0.27971217036247253):
														return True
													else:
														if(y_velocity <= -0.24368827044963837):
															if(angle_velocity <= -0.0188182620331645):
																if(angle > -0.04977857135236263):
																	return True
														else:
															if(angle <= -0.03225914016366005):
																return True
												else:
													if(x_velocity <= 0.01107311388477683):
														if(angle_velocity > -0.0155005375854671):
															return True
													else:
														if(angle > -0.03387994319200516):
															return True
									else:
										if(y_velocity > -0.2414861023426056):
											if(lander_x > -0.051000071689486504):
												if(angle <= 0.013151626102626324):
													if(angle_velocity <= -0.016257576644420624):
														if(angle_velocity <= -0.022562923841178417):
															if(lander_x > 0.040557241067290306):
																return True
														else:
															return True
							else:
								if(angle <= 0.1076303981244564):
									if(x_velocity <= -0.07047595828771591):
										if(y_velocity <= -0.2393423095345497):
											if(y_velocity <= -0.2515132427215576):
												if(y_velocity > -0.25362326204776764):
													if(y_velocity <= -0.2534611374139786):
														return True
											else:
												if(lander_y > 0.27551068365573883):
													if(lander_x > 0.09606976807117462):
														if(x_velocity > -0.07320167869329453):
															return True
										else:
											if(lander_y > 0.20869382470846176):
												if(lander_y > 0.3306434154510498):
													return True
									else:
										if(angle <= -0.04748993366956711):
											if(angle <= -0.0478067621588707):
												if(x_velocity <= 0.016812524758279324):
													if(lander_x <= 0.02426991518586874):
														if(y_velocity > -0.24017248302698135):
															if(y_velocity <= -0.2390705943107605):
																return True
													else:
														if(lander_x <= 0.0256518367677927):
															return True
														else:
															if(lander_y > 0.31341123580932617):
																if(x_velocity <= -0.06130965054035187):
																	return True
												else:
													if(lander_x <= -0.2577451467514038):
														return True
											else:
												return True
										else:
											if(y_velocity > -0.24577776342630386):
												if(y_velocity <= -0.24573373794555664):
													return True
												else:
													if(lander_y <= 0.34662970900535583):
														if(y_velocity <= -0.2367456704378128):
															if(angle <= -0.025782080367207527):
																if(angle <= -0.026252281852066517):
																	if(lander_x <= 0.05234885215759277):
																		if(angle > -0.029134863056242466):
																			if(angle <= -0.028867912478744984):
																				return True
																	else:
																		if(angle_velocity <= 0.019958649529144168):
																			return True
																else:
																	return True
														else:
															if(y_velocity <= -0.23673775792121887):
																return True
													else:
														if(x_velocity <= -0.0319372471421957):
															if(y_velocity > -0.24006640911102295):
																if(angle_velocity <= 0.0012883221497759223):
																	if(lander_x > 0.053998565301299095):
																		return True
														else:
															if(lander_y <= 0.3471149504184723):
																return True
															else:
																if(angle <= -0.03399592638015747):
																	return True
																else:
																	if(angle_velocity <= -0.001515519164968282):
																		if(angle_velocity > -0.0021210895502008498):
																			return True
					else:
						if(x_velocity <= -0.04648813232779503):
							if(lander_y <= 0.19113826006650925):
								if(angle <= -0.046979352831840515):
									if(angle_velocity <= 0.02028462290763855):
										if(x_velocity > -0.09238986298441887):
											if(lander_y <= 0.12361043319106102):
												if(lander_x <= 0.030186462681740522):
													if(angle <= -0.04844336397945881):
														if(x_velocity > -0.05976850725710392):
															if(angle_velocity <= 0.0025002136826515198):
																return True
													else:
														return True
												else:
													return True
											else:
												return True
									else:
										if(lander_y > 0.01318421121686697):
											if(angle <= -0.08574359491467476):
												if(angle > -0.09479870647192001):
													if(lander_y > 0.0951540544629097):
														return True
								else:
									if(x_velocity > -0.09178847447037697):
										if(x_velocity <= -0.04701359197497368):
											if(lander_x > 0.13120436668395996):
												return True
										else:
											return True
							else:
								if(angle_velocity <= -0.00023782247444614768):
									if(angle <= -0.026178336702287197):
										if(lander_x > -0.020393419545143843):
											if(angle_velocity > -0.029352606274187565):
												return True
									else:
										if(x_velocity > -0.0636415109038353):
											if(x_velocity > -0.04927167296409607):
												return True
								else:
									if(x_velocity > -0.07402462884783745):
										if(x_velocity <= -0.06454848125576973):
											if(y_velocity > -0.23083890974521637):
												if(lander_y <= 0.2897157371044159):
													if(y_velocity <= -0.227664552628994):
														return True
												else:
													return True
						else:
							if(angle_velocity <= -0.009669447783380747):
								if(angle <= -0.011002792976796627):
									if(lander_y <= 0.13093000650405884):
										if(lander_x <= -0.107452392578125):
											if(x_velocity > -0.04382038861513138):
												if(lander_x <= -0.23999667167663574):
													return True
												else:
													if(angle <= -0.06118393503129482):
														if(x_velocity > -0.037861282005906105):
															return True
										else:
											if(x_velocity <= -0.018888779915869236):
												if(lander_x > 0.04912071116268635):
													if(y_velocity > -0.22811774909496307):
														return True
											else:
												if(lander_y > 0.017065117601305246):
													if(lander_y <= 0.12869887053966522):
														if(angle <= -0.015971645712852478):
															return True
														else:
															if(angle > -0.011573934461921453):
																return True
									else:
										if(lander_x <= -0.053118277341127396):
											if(x_velocity <= -0.01717822067439556):
												if(lander_x > -0.11784172058105469):
													if(angle <= -0.03396008908748627):
														return True
											else:
												if(angle <= -0.01267700083553791):
													if(lander_x <= -0.13374271243810654):
														if(angle_velocity <= -0.025852824561297894):
															return True
														else:
															if(angle <= -0.014359915163367987):
																if(angle <= -0.030668151564896107):
																	if(lander_x > -0.23997964709997177):
																		return True
															else:
																return True
													else:
														return True
										else:
											return True
								else:
									if(angle <= 0.0026032080641016364):
										if(angle <= 0.0001600760042492766):
											if(y_velocity <= -0.2289690598845482):
												if(y_velocity <= -0.2350490614771843):
													return True
												else:
													if(lander_x > 0.04257049597799778):
														if(y_velocity <= -0.2317463606595993):
															return True
											else:
												if(lander_y <= 0.24653103202581406):
													if(lander_x > 0.004316091537475586):
														return True
												else:
													return True
										else:
											if(x_velocity > -0.016053935629315674):
												return True
									else:
										if(angle_velocity <= -0.030009222216904163):
											if(lander_y > 0.3308558464050293):
												return True
										else:
											if(lander_y <= 0.39159490168094635):
												if(angle <= 0.005531423492357135):
													if(angle > 0.005103458883240819):
														return True
											else:
												if(lander_x > 0.060754725243896246):
													return True
							else:
								if(lander_y <= 0.26726894080638885):
									if(lander_y > -0.0023655378608964384):
										if(angle <= -0.07237591594457626):
											if(angle_velocity <= 0.019305534195154905):
												return True
										else:
											if(angle <= -0.0323178693652153):
												if(y_velocity <= -0.2266954481601715):
													if(angle <= -0.03243671730160713):
														if(x_velocity > -0.0008773153240326792):
															if(x_velocity <= 0.005487707094289362):
																return True
													else:
														return True
												else:
													if(angle_velocity <= 0.0038238561246544123):
														if(x_velocity > -0.011577209457755089):
															return True
											else:
												if(x_velocity > -0.04456006549298763):
													if(x_velocity <= -0.03155418112874031):
														if(lander_y > 0.17070479691028595):
															if(lander_y <= 0.23987478762865067):
																if(y_velocity > -0.23088078945875168):
																	if(angle_velocity > -0.004556837142445147):
																		return True
								else:
									if(angle <= -0.002756904112175107):
										if(x_velocity <= 0.013403969816863537):
											if(angle <= -0.029252595268189907):
												if(angle_velocity <= 0.049676163122057915):
													if(x_velocity <= -0.03640488535165787):
														if(x_velocity <= -0.041138842701911926):
															if(angle_velocity > 0.02936954889446497):
																return True
													else:
														if(lander_y > 0.27811114490032196):
															return True
											else:
												if(angle > -0.025236784480512142):
													if(y_velocity <= -0.23320049792528152):
														if(lander_x > 0.02387318667024374):
															return True
										else:
											if(angle_velocity <= 0.05213731341063976):
												if(lander_x <= -0.06083793565630913):
													if(angle <= -0.022042084485292435):
														if(lander_x > -0.2704541087150574):
															return True
													else:
														if(x_velocity > 0.06282635405659676):
															if(angle_velocity <= 0.01550420792773366):
																return True
												else:
													return True
				else:
					if(y_velocity <= -0.2605880945920944):
						if(lander_y <= 0.7481449842453003):
							if(angle <= -0.02181170228868723):
								if(y_velocity <= -0.27377182245254517):
									if(x_velocity <= -0.12312685325741768):
										if(y_velocity <= -0.28999267518520355):
											if(angle <= -0.09409844875335693):
												if(y_velocity <= -0.3070802539587021):
													if(x_velocity <= -0.15461762249469757):
														if(angle_velocity <= 0.011445730458945036):
															if(y_velocity <= -0.33848021924495697):
																if(lander_y <= 0.43884681165218353):
																	return True
																else:
																	if(angle_velocity <= -0.028521228581666946):
																		return True
															else:
																if(angle_velocity <= -0.0010421707120258361):
																	return True
																else:
																	if(angle <= -0.1446538306772709):
																		if(x_velocity > -0.2682112604379654):
																			return True
														else:
															if(lander_y <= 0.41049598157405853):
																return True
															else:
																if(y_velocity > -0.3190077096223831):
																	if(x_velocity <= -0.20831692963838577):
																		if(x_velocity > -0.21005607396364212):
																			return True
													else:
														if(x_velocity <= -0.14397743344306946):
															if(lander_y > 0.7010950446128845):
																return True
														else:
															if(lander_y > 0.7201682031154633):
																if(x_velocity > -0.13563267141580582):
																	return True
												else:
													if(angle_velocity <= 0.057761792093515396):
														return True
											else:
												if(lander_x <= 0.03306412696838379):
													if(lander_y > 0.7044136822223663):
														return True
										else:
											if(angle_velocity <= 0.0013880389160476625):
												if(angle <= -0.0708085373044014):
													return True
									else:
										if(angle_velocity <= -0.02546069025993347):
											if(y_velocity <= -0.27917616069316864):
												if(lander_y <= 0.7350277602672577):
													if(lander_x <= 0.14085469022393227):
														if(y_velocity > -0.28723202645778656):
															if(y_velocity <= -0.28289762139320374):
																return True
													else:
														return True
												else:
													return True
											else:
												if(angle_velocity > -0.03183677792549133):
													return True
										else:
											if(lander_y <= 0.6829327642917633):
												if(angle <= -0.11299680918455124):
													if(angle_velocity <= 0.027471397072076797):
														if(x_velocity <= -0.10862397775053978):
															return True
														else:
															if(lander_y <= 0.5757111012935638):
																return True
													else:
														if(angle <= -0.1144704520702362):
															if(angle <= -0.2945413142442703):
																if(y_velocity > -0.4682534784078598):
																	return True
														else:
															return True
												else:
													if(y_velocity <= -0.2816237658262253):
														if(x_velocity > -0.001457451144233346):
															if(x_velocity <= -0.0009232910815626383):
																return True
													else:
														if(y_velocity <= -0.2815605252981186):
															return True
														else:
															if(lander_x > 0.08335079997777939):
																if(lander_x <= 0.08381500095129013):
																	return True
																else:
																	if(x_velocity > -0.0811101607978344):
																		return True
											else:
												if(angle_velocity <= 0.0030370953027158976):
													if(y_velocity <= -0.2869114726781845):
														if(angle_velocity <= -0.02223268896341324):
															if(angle_velocity > -0.024180482141673565):
																return True
														else:
															if(angle_velocity > 0.0024429350160062313):
																return True
													else:
														if(angle_velocity > -0.022267588414251804):
															return True
												else:
													if(lander_y <= 0.6835232675075531):
														return True
													else:
														if(y_velocity <= -0.2742239385843277):
															if(angle <= -0.040644459426403046):
																if(angle <= -0.04082971066236496):
																	if(y_velocity <= -0.29040004312992096):
																		if(angle <= -0.33636410534381866):
																			if(lander_x <= -0.3255809098482132):
																				return True
																		else:
																			if(angle <= -0.10107427462935448):
																				if(angle_velocity <= 0.14220482856035233):
																					return True
																				else:
																					if(lander_y <= 0.6909043788909912):
																						if(angle > -0.2481434866786003):
																							return True
																					else:
																						if(x_velocity <= -0.06813829019665718):
																							if(y_velocity > -0.3600621819496155):
																								return True
																	else:
																		if(lander_x <= -0.17059163749217987):
																			if(angle > -0.137898251414299):
																				if(y_velocity <= -0.2748130261898041):
																					if(angle > -0.04301474429666996):
																						if(lander_x <= -0.24942755699157715):
																							return True
																		else:
																			if(lander_y <= 0.7137521505355835):
																				if(x_velocity > -0.020681929774582386):
																					return True
																			else:
																				if(angle > -0.046668656170368195):
																					return True
														else:
															return True
								else:
									if(angle_velocity <= -0.01597929745912552):
										if(x_velocity <= -0.0942218005657196):
											if(angle <= -0.059978656470775604):
												return True
										else:
											if(y_velocity <= -0.26919007301330566):
												if(lander_y > 0.5307645499706268):
													if(lander_x <= -0.1637360081076622):
														if(lander_x <= -0.18021659553050995):
															return True
													else:
														return True
											else:
												return True
									else:
										if(x_velocity <= -0.11434036493301392):
											if(angle_velocity > -0.0038744015619158745):
												if(lander_x > 0.13892173767089844):
													if(lander_x <= 0.18229293823242188):
														if(y_velocity <= -0.26780669391155243):
															return True
										else:
											if(angle <= -0.054483141750097275):
												if(angle_velocity <= 0.12010367587208748):
													if(lander_y <= 0.4569232165813446):
														if(x_velocity <= -0.04819830134510994):
															if(x_velocity > -0.07681286707520485):
																if(y_velocity <= -0.2695690393447876):
																	if(x_velocity <= -0.06151467375457287):
																		return True
														else:
															if(angle_velocity <= 0.039116187021136284):
																return True
													else:
														if(y_velocity <= -0.26215559244155884):
															if(x_velocity <= -0.038297983817756176):
																if(lander_x > 0.022746515460312366):
																	if(angle_velocity <= 0.04956074431538582):
																		return True
															else:
																if(y_velocity <= -0.26380398869514465):
																	if(lander_y <= 0.7288891673088074):
																		return True
																	else:
																		if(angle <= -0.08069190010428429):
																			return True
														else:
															return True
											else:
												if(lander_y <= 0.6975981593132019):
													if(x_velocity <= -0.09737060591578484):
														if(y_velocity > -0.26768849790096283):
															if(lander_x > 0.17318911850452423):
																return True
													else:
														if(angle <= -0.022035779431462288):
															if(y_velocity <= -0.2633034735918045):
																if(angle_velocity <= -0.010728998109698296):
																	if(y_velocity > -0.2719820439815521):
																		if(lander_x <= 0.13725967705249786):
																			if(angle > -0.02529054321348667):
																				return True
																		else:
																			return True
																else:
																	if(x_velocity > -0.08750950545072556):
																		if(y_velocity <= -0.27327577769756317):
																			if(angle_velocity <= 0.0019136578775942326):
																				return True
																		else:
																			if(y_velocity > -0.26708464324474335):
																				if(y_velocity > -0.2669599801301956):
																					if(y_velocity <= -0.2661731094121933):
																						if(lander_x > 0.07894434640184045):
																							return True
																					else:
																						if(lander_y <= 0.6357315182685852):
																							if(lander_y > 0.5822017192840576):
																								if(lander_y <= 0.5902732610702515):
																									return True
															else:
																if(y_velocity <= -0.2629808038473129):
																	if(angle_velocity <= 0.005176165024749935):
																		return True
																else:
																	if(lander_x <= 0.025634002406150103):
																		if(angle <= -0.04536372795701027):
																			if(angle > -0.04816283844411373):
																				if(angle_velocity <= 0.008913603611290455):
																					return True
																		else:
																			if(y_velocity > -0.2607315331697464):
																				if(lander_y <= 0.543288841843605):
																					return True
																	else:
																		if(lander_x <= 0.09302086941897869):
																			return True
														else:
															if(y_velocity <= -0.26244987547397614):
																return True
												else:
													if(x_velocity <= -0.003156482183840126):
														if(lander_y <= 0.7053253650665283):
															return True
													else:
														if(angle_velocity <= 0.0421996358782053):
															if(x_velocity <= 0.010008121520513669):
																if(angle <= -0.036612335592508316):
																	return True
															else:
																return True
														else:
															if(angle_velocity <= 0.04846490919589996):
																if(y_velocity > -0.2639511823654175):
																	return True
							else:
								if(angle_velocity <= -0.0003560411714715883):
									if(y_velocity <= -0.27034956216812134):
										if(angle_velocity <= -0.0008982796862255782):
											if(angle <= -0.019256810657680035):
												if(x_velocity > -0.03592772223055363):
													if(x_velocity <= -0.006472905835835263):
														return True
										else:
											return True
									else:
										if(lander_x <= 0.1070275790989399):
											if(angle <= -0.0019573994795791805):
												if(x_velocity <= 0.023342729546129704):
													if(lander_x > 0.027657413855195045):
														if(x_velocity <= -0.03038112446665764):
															if(lander_x > 0.08523745462298393):
																if(lander_x <= 0.0926971435546875):
																	return True
														else:
															return True
												else:
													if(lander_y > 0.5626631677150726):
														return True
											else:
												if(angle_velocity <= -0.0014532044006045908):
													if(angle_velocity <= -0.03194776177406311):
														if(angle_velocity > -0.03241371363401413):
															return True
													else:
														if(lander_y > 0.697488933801651):
															if(lander_y <= 0.70826855301857):
																return True
												else:
													if(angle <= 0.019649216905236244):
														return True
										else:
											if(angle <= -0.0036085695028305054):
												if(x_velocity > -0.08577810600399971):
													return True
											else:
												if(lander_x > 0.1511659175157547):
													return True
								else:
									if(x_velocity > -0.09095006063580513):
										if(lander_x <= 0.15463419258594513):
											if(lander_y > 0.6874419748783112):
												if(y_velocity <= -0.26212240755558014):
													if(y_velocity <= -0.2651161700487137):
														if(angle_velocity <= 0.004804711090400815):
															if(angle_velocity > 0.004528076155111194):
																return True
													else:
														if(x_velocity > -0.04879201017320156):
															if(angle_velocity <= 0.013109767809510231):
																if(x_velocity > 0.003676973283290863):
																	return True
										else:
											if(angle_velocity <= 0.00947924517095089):
												return True
						else:
							if(angle <= 0.02187927905470133):
								if(y_velocity <= -0.2870802879333496):
									if(x_velocity <= 0.28544867038726807):
										if(lander_y <= 0.927573561668396):
											if(angle <= -0.05751131847500801):
												if(y_velocity <= -0.3031482994556427):
													if(x_velocity <= -0.07524305582046509):
														if(y_velocity <= -0.3130800426006317):
															if(angle <= -0.1344577819108963):
																if(y_velocity <= -0.35077668726444244):
																	if(angle_velocity <= 0.008511662017554045):
																		if(y_velocity > -0.5918124914169312):
																			return True
																	else:
																		if(angle_velocity <= 0.15972856432199478):
																			if(lander_x <= -0.3242046386003494):
																				if(angle_velocity <= 0.1528751254081726):
																					return True
																				else:
																					if(y_velocity <= -0.4986424446105957):
																						return True
																			else:
																				if(angle_velocity <= 0.15597213804721832):
																					if(angle <= -0.23700503259897232):
																						if(y_velocity <= -0.3955126404762268):
																							if(x_velocity <= -0.15833336859941483):
																								if(x_velocity <= -0.26440951228141785):
																									if(angle_velocity <= 0.08291301131248474):
																										if(lander_x <= -0.30285125970840454):
																											return True
																										else:
																											if(lander_y <= 0.817107230424881):
																												return True
																											else:
																												if(lander_y <= 0.8611823618412018):
																													if(angle > -0.38690371811389923):
																														return True
																								else:
																									if(angle <= -0.3712017238140106):
																										return True
																									else:
																										if(x_velocity <= -0.25631169974803925):
																											return True
																										else:
																											if(lander_y > 0.9086543321609497):
																												if(y_velocity > -0.4517647922039032):
																													return True
																							else:
																								return True
																						else:
																							return True
																					else:
																						if(angle_velocity <= 0.038537709042429924):
																							return True
																				else:
																					if(lander_x <= -0.23805096000432968):
																						return True
																		else:
																			if(angle <= -0.42627476155757904):
																				if(y_velocity > -0.602351188659668):
																					return True
																			else:
																				if(lander_y <= 0.7881056070327759):
																					if(lander_y <= 0.786048024892807):
																						if(angle_velocity <= 0.17853285372257233):
																							if(angle > -0.31298042833805084):
																								if(lander_x <= -0.2539311647415161):
																									return True
																					else:
																						return True
																else:
																	if(angle <= -0.18281710892915726):
																		if(x_velocity <= -0.15664704889059067):
																			if(angle_velocity <= 0.07859205082058907):
																				if(y_velocity <= -0.3229181617498398):
																					return True
																		else:
																			if(angle_velocity <= 0.19388870149850845):
																				if(y_velocity > -0.34917406737804413):
																					return True
																	else:
																		if(y_velocity <= -0.33404724299907684):
																			if(angle_velocity <= 0.07215861603617668):
																				if(y_velocity > -0.339968666434288):
																					return True
																		else:
																			if(y_velocity > -0.3166087418794632):
																				return True
															else:
																if(angle_velocity <= 0.13706297054886818):
																	if(angle_velocity <= -0.010039173532277346):
																		if(x_velocity > -0.12081129848957062):
																			if(angle <= -0.08164716698229313):
																				return True
														else:
															if(angle > -0.09483622759580612):
																if(angle <= -0.0794033445417881):
																	if(lander_y > 0.8506254851818085):
																		return True
													else:
														if(angle_velocity <= 0.03566866181790829):
															if(lander_x <= -0.1368904635310173):
																if(x_velocity <= -0.01631470862776041):
																	if(angle <= -0.07994751259684563):
																		if(x_velocity <= -0.05027257464826107):
																			if(angle <= -0.1067640520632267):
																				return True
																			else:
																				if(angle_velocity <= -0.004978791810572147):
																					return True
																		else:
																			return True
																else:
																	return True
															else:
																return True
														else:
															if(lander_y <= 0.7518079578876495):
																return True
															else:
																if(lander_y <= 0.773534506559372):
																	if(lander_y <= 0.7727174758911133):
																		if(lander_x > -0.2134246602654457):
																			return True
																else:
																	if(angle <= -0.19352463632822037):
																		if(angle_velocity <= 0.1966862976551056):
																			return True
																	else:
																		if(angle_velocity <= 0.24249832332134247):
																			if(angle <= -0.13196848332881927):
																				if(angle > -0.1350964531302452):
																					return True
												else:
													if(x_velocity <= -0.03121186699718237):
														if(angle_velocity <= 0.060871485620737076):
															if(lander_x <= -0.14834103733301163):
																if(y_velocity > -0.29245810210704803):
																	if(lander_y > 0.8403781354427338):
																		return True
															else:
																if(lander_x <= 0.006495429202914238):
																	if(y_velocity <= -0.2896360158920288):
																		if(angle_velocity <= 0.04137590713799):
																			return True
																		else:
																			if(lander_x <= -0.10703735053539276):
																				return True
														else:
															if(lander_y <= 0.8233723044395447):
																if(y_velocity > -0.2951791435480118):
																	if(lander_y <= 0.8095289468765259):
																		if(lander_y > 0.7858394086360931):
																			return True
															else:
																if(angle <= -0.1473691686987877):
																	return True
																else:
																	if(angle_velocity > 0.06705183163285255):
																		if(angle_velocity <= 0.07787059992551804):
																			if(lander_y > 0.8877435326576233):
																				return True
													else:
														if(angle_velocity <= 0.03155993763357401):
															return True
														else:
															if(angle <= -0.14376632124185562):
																if(y_velocity <= -0.29525814950466156):
																	return True
															else:
																if(y_velocity <= -0.3021085411310196):
																	if(angle > -0.09847354143857956):
																		return True
																else:
																	if(lander_y > 0.8006114363670349):
																		if(lander_y <= 0.8174704313278198):
																			if(angle_velocity <= 0.1395440325140953):
																				return True
																		else:
																			if(y_velocity <= -0.29175035655498505):
																				if(angle <= -0.09574378281831741):
																					if(angle > -0.09988484159111977):
																						return True
																			else:
																				if(angle_velocity > 0.07651634141802788):
																					if(lander_y <= 0.9152035415172577):
																						if(angle <= -0.07856425270438194):
																							if(y_velocity > -0.29131732881069183):
																								return True
											else:
												if(lander_x <= 0.21776456385850906):
													if(y_velocity <= -0.2921095937490463):
														if(y_velocity > -0.29952065646648407):
															if(y_velocity <= -0.29944540560245514):
																return True
															else:
																if(angle <= -0.047937532886862755):
																	if(angle <= -0.04831410199403763):
																		if(x_velocity > -0.010877876309677958):
																			if(lander_x > -0.2377481460571289):
																				return True
																	else:
																		return True
																else:
																	if(y_velocity <= -0.29815472662448883):
																		if(y_velocity > -0.2982545644044876):
																			return True
													else:
														if(x_velocity <= -0.11104102060198784):
															if(angle_velocity <= -0.013931303285062313):
																return True
														else:
															if(y_velocity > -0.2919992655515671):
																if(lander_x <= -0.13604015856981277):
																	if(angle_velocity <= 0.018082361668348312):
																		if(angle_velocity > -0.0016877823509275913):
																			return True
												else:
													if(y_velocity > -0.3133704215288162):
														if(angle <= -0.05219015292823315):
															return True
										else:
											if(y_velocity <= -0.3181559443473816):
												if(x_velocity <= -0.09489988535642624):
													if(y_velocity <= -0.3449101150035858):
														if(angle <= 0.003930528182536364):
															if(angle <= -0.1493743658065796):
																if(y_velocity <= -0.3789035230875015):
																	if(angle_velocity <= 0.027191842906177044):
																		if(y_velocity <= -0.3943863660097122):
																			if(lander_x <= -0.1216805949807167):
																				if(x_velocity <= -0.2808101028203964):
																					if(angle <= -0.263735756278038):
																						if(y_velocity <= -0.45882800221443176):
																							if(lander_y <= 1.059090793132782):
																								if(x_velocity <= -0.42039482295513153):
																									if(y_velocity <= -0.5972758829593658):
																										if(angle_velocity <= -0.027917093597352505):
																											return True
																									else:
																										if(lander_x <= -0.2559261620044708):
																											return True
																								else:
																									if(lander_x <= -0.21821627020835876):
																										return True
																									else:
																										if(angle_velocity <= -0.004105630214326084):
																											return True
																							else:
																								if(angle <= -0.3265712559223175):
																									if(y_velocity <= -0.5662457346916199):
																										if(lander_x <= -0.30618157982826233):
																											return True
																									else:
																										if(lander_x <= -0.24335196614265442):
																											return True
																										else:
																											if(y_velocity <= -0.49221718311309814):
																												if(lander_y <= 1.078147292137146):
																													if(x_velocity > -0.44973519444465637):
																														return True
																												else:
																													if(y_velocity <= -0.5497466921806335):
																														if(lander_y <= 1.247488021850586):
																															return True
																											else:
																												return True
																						else:
																							if(lander_y <= 1.3552486300468445):
																								if(lander_x <= -0.15971794724464417):
																									if(y_velocity <= -0.45118361711502075):
																										if(y_velocity <= -0.45621345937252045):
																											return True
																									else:
																										return True
																								else:
																									if(x_velocity <= -0.3526459187269211):
																										if(angle_velocity <= -0.01725156349129975):
																											return True
																					else:
																						if(y_velocity > -0.4173963814973831):
																							if(lander_x > -0.12892670929431915):
																								return True
																				else:
																					return True
																			else:
																				if(lander_y <= 1.4432497024536133):
																					if(angle_velocity <= -0.013694960623979568):
																						if(y_velocity > -0.42696885764598846):
																							if(lander_x <= -0.09979639202356339):
																								return True
																							else:
																								if(x_velocity > -0.22518950700759888):
																									return True
																					else:
																						if(x_velocity > -0.20433081686496735):
																							if(x_velocity <= -0.19579389691352844):
																								return True
																		else:
																			if(angle <= -0.16770220547914505):
																				if(lander_y <= 1.2468570470809937):
																					return True
																				else:
																					if(lander_x > -0.10054440796375275):
																						return True
																			else:
																				if(lander_y <= 1.2943825125694275):
																					if(x_velocity > -0.19877690821886063):
																						if(angle <= -0.15145599842071533):
																							return True
																				else:
																					if(y_velocity <= -0.3899398148059845):
																						return True
																	else:
																		if(angle <= -0.24870789796113968):
																			if(y_velocity <= -0.4152718335390091):
																				if(angle <= -0.2919051945209503):
																					if(angle_velocity <= 0.12940814346075058):
																						if(y_velocity <= -0.43711379170417786):
																							if(x_velocity <= -0.25607793033123016):
																								if(lander_x <= -0.29538968205451965):
																									if(y_velocity <= -0.5677783489227295):
																										if(lander_x > -0.3023550808429718):
																											if(lander_x <= -0.3002033233642578):
																												return True
																									else:
																										if(angle_velocity <= 0.06695100665092468):
																											return True
																										else:
																											if(lander_y <= 1.1772054433822632):
																												if(lander_y <= 0.9512946605682373):
																													return True
																												else:
																													if(angle <= -0.43317753076553345):
																														return True
																													else:
																														if(angle_velocity > 0.12379167601466179):
																															return True
																								else:
																									if(x_velocity <= -0.33678731322288513):
																										if(angle <= -0.39501728117465973):
																											if(y_velocity <= -0.5294573307037354):
																												if(x_velocity <= -0.34816914796829224):
																													if(x_velocity > -0.3924696743488312):
																														if(y_velocity > -0.5837084054946899):
																															return True
																												else:
																													return True
																											else:
																												return True
																									else:
																										if(angle <= -0.3540605157613754):
																											return True
																										else:
																											if(angle_velocity <= 0.07370385155081749):
																												if(x_velocity <= -0.28236123919487):
																													if(lander_y <= 1.2610137462615967):
																														if(angle <= -0.3481638729572296):
																															if(x_velocity > -0.32118093967437744):
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
																						if(y_velocity <= -0.4627908915281296):
																							if(y_velocity > -0.505884200334549):
																								if(y_velocity <= -0.5048397183418274):
																									return True
																								else:
																									if(angle <= -0.3451588451862335):
																										if(lander_x > -0.28787775337696075):
																											return True
																						else:
																							if(y_velocity <= -0.42912642657756805):
																								if(y_velocity <= -0.44839824736118317):
																									if(y_velocity <= -0.45893318951129913):
																										return True
																								else:
																									return True
																				else:
																					if(lander_y <= 1.2647876143455505):
																						if(x_velocity > -0.2129044607281685):
																							if(x_velocity <= -0.21264341473579407):
																								return True
																			else:
																				if(angle_velocity <= 0.12427567690610886):
																					if(angle_velocity > 0.03626669943332672):
																						if(angle_velocity <= 0.10418592393398285):
																							return True
																						else:
																							if(x_velocity > -0.24043092131614685):
																								return True
																				else:
																					if(y_velocity <= -0.38959696888923645):
																						if(angle <= -0.2965431958436966):
																							return True
																		else:
																			if(lander_y <= 1.3016756772994995):
																				if(y_velocity > -0.38997744023799896):
																					if(angle <= -0.2142021581530571):
																						if(y_velocity <= -0.38691025972366333):
																							return True
																			else:
																				if(lander_y <= 1.3090237379074097):
																					return True
																				else:
																					if(y_velocity > -0.40720145404338837):
																						if(lander_y > 1.3310995697975159):
																							return True
																else:
																	if(angle_velocity <= 0.08153198659420013):
																		if(x_velocity <= -0.20065878331661224):
																			if(angle_velocity <= 0.02515404112637043):
																				if(x_velocity > -0.2927251011133194):
																					if(lander_y <= 1.315960168838501):
																						if(lander_x <= -0.089191485196352):
																							return True
																						else:
																							if(x_velocity > -0.22504987567663193):
																								return True
																					else:
																						if(lander_y > 1.4129882454872131):
																							return True
																			else:
																				if(lander_x <= -0.1706898733973503):
																					if(angle_velocity <= 0.05479501187801361):
																						return True
																				else:
																					if(x_velocity > -0.2175237238407135):
																						if(lander_y <= 1.1773555278778076):
																							if(y_velocity <= -0.3669579178094864):
																								if(angle <= -0.18903785943984985):
																									return True
																		else:
																			if(angle <= -0.1647794246673584):
																				if(y_velocity > -0.37773849070072174):
																					if(y_velocity <= -0.3698619157075882):
																						if(y_velocity <= -0.37271711230278015):
																							return True
																					else:
																						return True
																			else:
																				if(lander_y <= 1.119242548942566):
																					if(angle_velocity <= 0.06505804881453514):
																						if(x_velocity > -0.14835474640130997):
																							return True
																				else:
																					if(angle_velocity <= 0.05683406628668308):
																						if(lander_y <= 1.138571321964264):
																							if(angle > -0.14969803392887115):
																								return True
																						else:
																							return True
																					else:
																						if(lander_x <= -0.16711640357971191):
																							if(y_velocity > -0.35712553560733795):
																								return True
																	else:
																		if(x_velocity <= -0.17687823623418808):
																			if(y_velocity <= -0.373647078871727):
																				if(angle <= -0.2283104658126831):
																					if(angle_velocity > 0.10583164915442467):
																						return True
																			else:
																				if(lander_y <= 0.9352032542228699):
																					return True
																		else:
																			if(angle <= -0.1857243850827217):
																				if(y_velocity > -0.36425161361694336):
																					if(lander_x <= -0.2079010233283043):
																						if(x_velocity <= -0.10532455891370773):
																							return True
																			else:
																				if(x_velocity > -0.10079789534211159):
																					if(lander_x > -0.1928778663277626):
																						return True
															else:
																if(y_velocity > -0.3684648126363754):
																	if(lander_y <= 1.1058405637741089):
																		if(angle <= -0.13921111822128296):
																			if(angle_velocity <= 0.06504715979099274):
																				return True
																	else:
																		if(angle <= -0.09695779904723167):
																			if(angle_velocity <= 0.016172837931662798):
																				if(y_velocity <= -0.35028357803821564):
																					if(x_velocity > -0.1887539029121399):
																						return True
																			else:
																				if(lander_x > -0.11046252027153969):
																					if(angle <= -0.12689248099923134):
																						return True
																		else:
																			if(x_velocity > -0.0986231192946434):
																				return True
													else:
														if(x_velocity <= -0.1294594332575798):
															if(lander_y <= 1.0964109301567078):
																if(y_velocity <= -0.33047036826610565):
																	if(angle <= -0.10855249688029289):
																		if(angle <= -0.16138630360364914):
																			if(y_velocity <= -0.3409622013568878):
																				return True
																			else:
																				if(lander_x <= -0.1911008358001709):
																					return True
																		else:
																			return True
																	else:
																		if(x_velocity <= -0.18380198627710342):
																			return True
															else:
																if(angle_velocity <= -0.010259217116981745):
																	if(angle_velocity > -0.015121657401323318):
																		return True
														else:
															if(angle_velocity <= 0.09766862168908119):
																if(lander_y <= 1.2238355875015259):
																	if(angle <= -0.10366370156407356):
																		if(y_velocity <= -0.3361032158136368):
																			if(x_velocity > -0.10726776719093323):
																				if(y_velocity <= -0.3405596613883972):
																					if(lander_x <= -0.1029202938079834):
																						return True
																		else:
																			if(lander_y <= 1.1015729904174805):
																				if(y_velocity <= -0.3212449848651886):
																					if(lander_y <= 0.9507454037666321):
																						if(lander_y <= 0.9412374198436737):
																							return True
																					else:
																						return True
																	else:
																		if(y_velocity <= -0.31983761489391327):
																			if(angle_velocity <= -0.004824674921110272):
																				if(angle <= -0.05814482271671295):
																					return True
																else:
																	if(angle <= -0.05679384432733059):
																		if(angle_velocity <= 0.03945926018059254):
																			if(lander_x <= -0.03557424433529377):
																				if(angle_velocity > 0.022860653698444366):
																					return True
																			else:
																				return True
												else:
													if(x_velocity <= 0.07830312848091125):
														if(angle <= -0.049028461799025536):
															if(angle_velocity <= -0.0056668659672141075):
																return True
															else:
																if(y_velocity <= -0.33644188940525055):
																	if(angle <= -0.16255146265029907):
																		if(angle_velocity <= 0.1187651939690113):
																			return True
																		else:
																			if(angle <= -0.27159905433654785):
																				return True
																			else:
																				if(angle_velocity <= 0.13883444666862488):
																					if(lander_y <= 1.0594414472579956):
																						return True
																	else:
																		if(angle_velocity <= 0.03516257554292679):
																			if(y_velocity > -0.3415589928627014):
																				return True
																		else:
																			if(lander_y > 1.2206677198410034):
																				if(lander_y <= 1.2255938053131104):
																					return True
																else:
																	if(angle <= -0.13604997098445892):
																		if(angle_velocity <= 0.12364072352647781):
																			return True
																	else:
																		if(lander_y <= 0.9831717312335968):
																			if(x_velocity > -0.034359756857156754):
																				if(x_velocity <= -0.03361884504556656):
																					return True
																		else:
																			if(angle <= -0.10840273648500443):
																				if(angle_velocity <= 0.09908459335565567):
																					return True
																			else:
																				if(angle_velocity <= 0.02375955879688263):
																					if(lander_x <= -0.036885930225253105):
																						if(lander_y > 0.9906821846961975):
																							if(angle_velocity <= 0.011057153693400323):
																								if(lander_y <= 1.1105560064315796):
																									return True
																							else:
																								return True
																				else:
																					if(angle <= -0.05209057219326496):
																						if(y_velocity <= -0.33621786534786224):
																							return True
																						else:
																							if(lander_x <= -0.04987168312072754):
																								if(x_velocity <= -0.07587060704827309):
																									if(lander_y > 1.104224145412445):
																										return True
														else:
															if(angle_velocity <= -0.017263861373066902):
																if(x_velocity > -0.04866043105721474):
																	if(y_velocity > -0.3245055228471756):
																		return True
															else:
																if(x_velocity > -0.08984805643558502):
																	if(angle_velocity <= 0.05487595312297344):
																		if(angle_velocity <= -0.009400253649801016):
																			if(angle_velocity > -0.009901043493300676):
																				return True
													else:
														if(y_velocity <= -0.4098746329545975):
															if(x_velocity <= 0.09423593804240227):
																return True
															else:
																if(lander_x > 0.028951263055205345):
																	if(lander_x <= 0.03138618357479572):
																		return True
														else:
															if(x_velocity <= 0.139861561357975):
																if(angle_velocity <= 0.07000225596129894):
																	return True
															else:
																return True
											else:
												if(angle <= -0.0553903765976429):
													if(angle_velocity <= 0.03671233169734478):
														if(x_velocity <= -0.10055548325181007):
															if(lander_y <= 1.0441427826881409):
																if(angle_velocity <= -0.005032745364587754):
																	return True
																else:
																	if(x_velocity > -0.1092936247587204):
																		if(x_velocity <= -0.10599024221301079):
																			return True
															else:
																if(lander_x <= -0.10713229328393936):
																	if(lander_x > -0.12103839218616486):
																		return True
														else:
															if(lander_y <= 1.2491780519485474):
																return True
													else:
														if(x_velocity <= -0.008781893644481897):
															if(x_velocity <= -0.0656152106821537):
																if(y_velocity <= -0.31772029399871826):
																	return True
																else:
																	if(angle_velocity > 0.12409865856170654):
																		if(angle_velocity <= 0.12992875277996063):
																			return True
															else:
																if(angle_velocity <= 0.06168821267783642):
																	if(angle <= -0.07233299687504768):
																		return True
																	else:
																		if(angle_velocity <= 0.049714384600520134):
																			return True
																else:
																	if(angle <= -0.10798439756035805):
																		if(angle_velocity <= 0.12526226043701172):
																			if(lander_y <= 0.9748157560825348):
																				return True
																			else:
																				if(lander_y > 1.0776776671409607):
																					return True
																	else:
																		if(x_velocity > -0.033516447991132736):
																			if(lander_x > -0.22974779456853867):
																				return True
												else:
													if(lander_y <= 1.1245160102844238):
														if(angle <= -0.015948761254549026):
															if(y_velocity <= -0.3007678985595703):
																if(angle_velocity <= -0.003789520589634776):
																	if(y_velocity > -0.3148154467344284):
																		if(lander_y <= 1.0923163890838623):
																			if(lander_y <= 1.080258846282959):
																				return True
																			else:
																				if(angle_velocity > -0.014787520281970501):
																					return True
																else:
																	if(y_velocity > -0.30417150259017944):
																		if(angle_velocity <= 0.0249061593785882):
																			if(x_velocity > -0.0213432339951396):
																				return True
															else:
																if(x_velocity <= -0.02867597248405218):
																	if(lander_y <= 1.0179275274276733):
																		if(x_velocity > -0.1044786274433136):
																			if(angle_velocity <= -0.02350452821701765):
																				return True
																	else:
																		if(angle_velocity <= -0.012505895458161831):
																			return True
																else:
																	if(angle_velocity <= 0.013016893062740564):
																		return True
														else:
															if(angle_velocity <= -0.03197268210351467):
																if(angle_velocity > -0.03258275426924229):
																	return True
															else:
																if(x_velocity > -0.09236766397953033):
																	if(y_velocity > -0.2938740998506546):
																		if(y_velocity <= -0.2932325005531311):
																			if(angle_velocity <= 0.011414687149226665):
																				return True
													else:
														if(x_velocity <= -0.05114337243139744):
															if(y_velocity <= -0.3057635873556137):
																if(x_velocity <= -0.06747142970561981):
																	if(angle_velocity <= -0.005634115310385823):
																		if(y_velocity > -0.3119460642337799):
																			return True
																else:
																	if(x_velocity > -0.05498969741165638):
																		return True
															else:
																if(angle <= -0.03042167890816927):
																	if(angle_velocity <= 0.021263832692056894):
																		if(y_velocity > -0.3027724474668503):
																			return True
														else:
															if(angle_velocity <= -0.009729324374347925):
																return True
															else:
																if(lander_x <= -0.0009590625850250944):
																	if(y_velocity <= -0.29851967096328735):
																		if(angle_velocity <= 0.008440156932920218):
																			if(angle <= -0.012899728026241064):
																				return True
																		else:
																			if(angle_velocity <= 0.05459572561085224):
																				if(angle <= -0.03455031104385853):
																					if(lander_y > 1.24310702085495):
																						return True
																	else:
																		if(lander_y > 1.2052368521690369):
																			if(lander_y <= 1.2466508150100708):
																				if(y_velocity <= -0.290356770157814):
																					return True
																else:
																	return True
									else:
										if(angle <= 0.0004229727273923345):
											return True
										else:
											if(y_velocity <= -0.5899165868759155):
												if(x_velocity > 0.5952281653881073):
													if(x_velocity <= 0.6212974190711975):
														return True
													else:
														if(x_velocity > 0.6719889342784882):
															return True
											else:
												if(x_velocity <= 0.3466893136501312):
													if(lander_y > 1.3488011956214905):
														return True
												else:
													return True
								else:
									if(x_velocity <= 0.015524227172136307):
										if(angle_velocity <= 0.04227382689714432):
											if(lander_y <= 0.9449955224990845):
												if(angle <= -0.015402767807245255):
													if(x_velocity <= -0.06508280709385872):
														if(angle_velocity <= 0.017942871898412704):
															if(y_velocity <= -0.2811204195022583):
																if(angle_velocity > -0.013506073970347643):
																	if(angle <= -0.04564303532242775):
																		return True
															else:
																if(y_velocity > -0.26141560077667236):
																	return True
														else:
															if(x_velocity > -0.101777333766222):
																if(x_velocity <= -0.07272878289222717):
																	return True
																else:
																	if(lander_y > 0.7930634021759033):
																		if(x_velocity > -0.07104366645216942):
																			return True
													else:
														if(angle_velocity <= -0.008661546278744936):
															if(lander_y <= 0.8945707976818085):
																if(y_velocity <= -0.28486965596675873):
																	if(x_velocity > -0.013673179782927036):
																		return True
																else:
																	return True
															else:
																if(y_velocity <= -0.2810187488794327):
																	return True
														else:
															if(angle <= -0.04194432869553566):
																if(lander_x > -0.25347161293029785):
																	if(x_velocity <= -0.04370899684727192):
																		if(angle <= -0.0710131861269474):
																			return True
																		else:
																			if(lander_x > -0.146842859685421):
																				if(y_velocity > -0.2832375317811966):
																					if(x_velocity > -0.061524951830506325):
																						return True
																	else:
																		if(angle <= -0.04754991829395294):
																			return True
																		else:
																			if(angle > -0.0447126105427742):
																				return True
															else:
																if(y_velocity <= -0.2726004123687744):
																	if(lander_y <= 0.9051461517810822):
																		if(angle <= -0.0164434970356524):
																			if(lander_x <= 0.038593340665102005):
																				if(lander_y > 0.844296395778656):
																					if(lander_y <= 0.8504377901554108):
																						return True
																		else:
																			return True
																	else:
																		if(x_velocity > -0.03634175006300211):
																			return True
																else:
																	if(lander_x <= -0.042421627789735794):
																		if(x_velocity > -0.024506441317498684):
																			if(angle_velocity <= 0.019499734975397587):
																				return True
																			else:
																				if(lander_y <= 0.7526534795761108):
																					return True
																	else:
																		return True
												else:
													if(y_velocity <= -0.270012304186821):
														if(x_velocity <= -0.016377419233322144):
															if(x_velocity <= -0.07929385080933571):
																if(lander_x > 0.0782318115234375):
																	if(angle_velocity <= 0.01603014604188502):
																		if(x_velocity > -0.0810648761689663):
																			return True
															else:
																if(angle_velocity <= -0.03231810964643955):
																	return True
														else:
															if(angle <= 0.0021461513824760914):
																return True
															else:
																if(angle_velocity <= -0.014884327538311481):
																	if(y_velocity <= -0.27731068432331085):
																		if(x_velocity <= -0.014287586323916912):
																			return True
																	else:
																		return True
													else:
														if(x_velocity <= -0.041608575731515884):
															if(angle > -0.014454931486397982):
																if(angle_velocity <= -0.025408386252820492):
																	if(x_velocity > -0.05687848851084709):
																		return True
														else:
															if(angle <= -0.009365124627947807):
																return True
															else:
																if(lander_x > 0.04172668419778347):
																	if(lander_y > 0.7868961989879608):
																		return True
											else:
												if(x_velocity <= -0.02750662248581648):
													if(angle_velocity <= -0.029355192556977272):
														return True
													else:
														if(angle <= -0.028561473824083805):
															if(x_velocity > -0.08187180384993553):
																if(y_velocity <= -0.2762713134288788):
																	if(angle_velocity <= 0.026599155738949776):
																		if(angle_velocity <= 0.010037757456302643):
																			return True
																		else:
																			if(angle_velocity > 0.015962203964591026):
																				return True
														else:
															if(lander_x <= -0.05922546423971653):
																return True
															else:
																if(y_velocity > -0.28388258814811707):
																	if(lander_x > 0.0641079917550087):
																		if(lander_x <= 0.0650944709777832):
																			return True
												else:
													if(angle_velocity <= 0.01791199017316103):
														if(angle <= 0.02093520388007164):
															if(lander_y <= 0.9808626770973206):
																if(angle_velocity <= 0.006866823881864548):
																	if(lander_x > -0.04376626014709473):
																		return True
															else:
																if(angle <= 0.011638423427939415):
																	return True
																else:
																	if(lander_x > 0.016232823953032494):
																		return True
													else:
														if(x_velocity <= -0.022695248015224934):
															if(lander_x <= -0.04166054632514715):
																return True
														else:
															if(angle_velocity > 0.04090994782745838):
																return True
										else:
											if(lander_y <= 0.7757551670074463):
												if(angle <= -0.08683010935783386):
													if(lander_y > 0.766150176525116):
														return True
											else:
												if(x_velocity <= -0.0007985317497514188):
													if(y_velocity <= -0.2753151059150696):
														if(angle_velocity <= 0.0611433032900095):
															if(angle <= -0.06968993693590164):
																if(lander_x > -0.14791449904441833):
																	return True
															else:
																if(lander_y <= 0.9312511086463928):
																	if(x_velocity > -0.039910824969410896):
																		if(x_velocity > -0.012965789763256907):
																			return True
														else:
															if(y_velocity > -0.28602685034275055):
																if(lander_y > 1.1093484163284302):
																	if(lander_y <= 1.2606794238090515):
																		return True
													else:
														if(angle <= -0.09860137477517128):
															if(angle > -0.12000813707709312):
																if(lander_y <= 0.9309572279453278):
																	return True
														else:
															if(lander_y <= 0.7897994220256805):
																if(lander_y > 0.786220133304596):
																	return True
												else:
													if(angle_velocity <= 0.060412293300032616):
														if(angle <= -0.06914813071489334):
															return True
									else:
										if(lander_y <= 1.027734100818634):
											if(angle_velocity <= 0.19868455827236176):
												if(angle_velocity <= 0.03819133900105953):
													if(angle <= -0.005042276810854673):
														if(lander_x <= -0.29285429418087006):
															if(y_velocity > -0.27130232751369476):
																if(lander_y > 0.7967526912689209):
																	return True
														else:
															if(y_velocity <= -0.2829112708568573):
																if(lander_x > -0.15746107697486877):
																	return True
															else:
																return True
													else:
														if(lander_y <= 0.9751328825950623):
															if(lander_x <= 0.03997826483100653):
																if(angle <= 0.002066176733933389):
																	if(angle_velocity <= 0.0063968447502702475):
																		return True
																else:
																	if(lander_y > 0.8892716765403748):
																		if(lander_y <= 0.9010481536388397):
																			return True
															else:
																return True
														else:
															if(angle_velocity <= 0.020914265885949135):
																return True
												else:
													if(y_velocity <= -0.26225630939006805):
														if(lander_y > 0.8528149425983429):
															if(angle <= -0.019997977651655674):
																if(lander_x > -0.3382154703140259):
																	if(y_velocity <= -0.2685592323541641):
																		if(x_velocity <= 0.047774912789464):
																			if(y_velocity > -0.27596136927604675):
																				return True
																		else:
																			return True
										else:
											if(y_velocity > -0.27959856390953064):
												if(angle_velocity <= 0.1332056187093258):
													if(angle <= 0.014942340552806854):
														return True
													else:
														if(y_velocity <= -0.2724715769290924):
															return True
							else:
								if(y_velocity <= -0.27584148943424225):
									if(x_velocity > -0.4281509518623352):
										if(angle <= 0.46151159703731537):
											if(lander_y <= 1.281448781490326):
												if(lander_x <= 0.07046699523925781):
													if(lander_x <= 0.07010574266314507):
														if(y_velocity <= -0.42698056995868683):
															if(y_velocity <= -0.44625256955623627):
																if(lander_x <= 0.06561880186200142):
																	if(angle_velocity <= 0.07942770421504974):
																		if(lander_y <= 1.2210199236869812):
																			return True
																else:
																	if(lander_y > 1.1946439743041992):
																		return True
															else:
																if(angle <= 0.040779996663331985):
																	return True
														else:
															if(y_velocity <= -0.28613579273223877):
																if(y_velocity <= -0.3309361934661865):
																	if(y_velocity > -0.33264076709747314):
																		return True
															else:
																if(y_velocity <= -0.2858380228281021):
																	if(x_velocity > 0.031264145189197734):
																		return True
													else:
														return True
												else:
													if(angle_velocity <= -0.02794352639466524):
														if(angle_velocity > -0.02803539764136076):
															return True
											else:
												if(x_velocity <= 0.42733925580978394):
													if(angle <= 0.04763258434832096):
														if(x_velocity <= 0.34170304238796234):
															if(y_velocity <= -0.2994955778121948):
																if(lander_y <= 1.3377133011817932):
																	if(lander_y <= 1.3345809578895569):
																		if(lander_y > 1.3234125971794128):
																			if(lander_y <= 1.3256255984306335):
																				return True
																	else:
																		return True
															else:
																if(angle_velocity <= 0.06817084550857544):
																	return True
														else:
															return True
												else:
													if(lander_y <= 1.2984944581985474):
														if(x_velocity > 0.5707046687602997):
															return True
													else:
														return True
								else:
									if(angle <= 0.4801601767539978):
										if(angle <= 0.07749898359179497):
											if(lander_y <= 0.9992907345294952):
												if(angle_velocity <= -0.03134584240615368):
													return True
												else:
													if(x_velocity > -0.04115448147058487):
														if(x_velocity <= 0.030899989418685436):
															if(y_velocity <= -0.2625493109226227):
																if(angle <= 0.024610111489892006):
																	if(angle <= 0.02446788363158703):
																		if(angle_velocity <= -0.020123986527323723):
																			return True
														else:
															if(angle_velocity <= -0.007334933150559664):
																return True
															else:
																if(x_velocity <= 0.03253500908613205):
																	return True
											else:
												if(x_velocity > -0.0016471044509671628):
													if(lander_y <= 1.1409984827041626):
														if(y_velocity <= -0.2676937133073807):
															if(lander_x <= -0.10712022706866264):
																return True
														else:
															if(x_velocity > 0.023460568860173225):
																if(x_velocity > 0.0555493850260973):
																	return True
													else:
														if(x_velocity <= 0.06683329120278358):
															if(angle_velocity <= -0.014909314457327127):
																return True
															else:
																if(angle <= 0.03697366826236248):
																	if(angle_velocity <= 0.07720512337982655):
																		return True
														else:
															if(angle_velocity <= 0.0761478841304779):
																if(x_velocity > 0.08216015994548798):
																	return True
										else:
											if(lander_x <= 0.042531490325927734):
												if(y_velocity <= -0.26233261823654175):
													if(lander_y > 1.1407285928726196):
														if(x_velocity > 0.052847832441329956):
															if(angle_velocity <= -0.0067379591055214405):
																if(angle_velocity > -0.01262631407007575):
																	return True
											else:
												if(angle <= 0.10374780744314194):
													if(angle > 0.10111378505825996):
														return True
					else:
						if(x_velocity <= -0.0031562260119244456):
							if(lander_y <= 0.6404740214347839):
								if(y_velocity <= -0.24344873428344727):
									if(x_velocity <= -0.06039332039654255):
										if(y_velocity <= -0.25149276852607727):
											if(angle <= -0.052637698128819466):
												if(x_velocity <= -0.07406633719801903):
													if(angle <= -0.07045106589794159):
														return True
													else:
														if(lander_x > 0.04302477976307273):
															if(lander_y <= 0.4100666046142578):
																return True
												else:
													return True
											else:
												if(lander_y <= 0.5075192451477051):
													if(x_velocity <= -0.09953827410936356):
														if(angle_velocity <= -0.008703956351382658):
															if(angle <= -0.04968533478677273):
																return True
													else:
														if(angle_velocity <= -0.019486697390675545):
															return True
												else:
													if(x_velocity <= -0.07289041206240654):
														if(angle_velocity > -0.031676873564720154):
															if(y_velocity > -0.2521260380744934):
																return True
													else:
														if(x_velocity > -0.0684046596288681):
															if(lander_x > 0.04579372517764568):
																if(x_velocity > -0.06336255371570587):
																	if(angle_velocity <= 0.010023372946307063):
																		return True
										else:
											if(angle_velocity <= -0.01959348376840353):
												if(lander_x > 0.1270311400294304):
													if(y_velocity > -0.2499309778213501):
														return True
									else:
										if(angle_velocity <= -0.01589978439733386):
											if(angle <= -0.012967045418918133):
												if(lander_x > -0.17397456616163254):
													return True
											else:
												if(lander_x <= 0.05797553062438965):
													if(angle <= -0.011343478690832853):
														if(y_velocity <= -0.2503780648112297):
															return True
												else:
													if(angle <= 0.015683614183217287):
														if(lander_y > 0.423337921500206):
															if(y_velocity > -0.2555522918701172):
																if(angle_velocity <= -0.025193702429533005):
																	return True
																else:
																	if(lander_x > 0.11938934028148651):
																		return True
										else:
											if(angle <= -0.01587140467017889):
												if(y_velocity <= -0.25238659977912903):
													if(angle > -0.07502445578575134):
														if(x_velocity > -0.05832513049244881):
															if(lander_y <= 0.6256686747074127):
																if(angle_velocity <= 0.0064967426005750895):
																	if(lander_x <= 0.042778730392456055):
																		if(x_velocity > -0.016078908927738667):
																			return True
																	else:
																		return True
															else:
																return True
												else:
													if(lander_y <= 0.4490576684474945):
														if(angle <= -0.0433986522257328):
															if(angle > -0.05176094174385071):
																return True
													else:
														if(angle_velocity <= 0.005488356575369835):
															if(x_velocity > -0.05075988546013832):
																if(angle_velocity > -0.00937642203643918):
																	return True
														else:
															if(lander_x > -0.06326909177005291):
																if(x_velocity > -0.02738816197961569):
																	return True
											else:
												if(lander_y <= 0.6370363831520081):
													if(y_velocity <= -0.24830061942338943):
														if(angle_velocity <= 0.0023282679030671716):
															if(lander_x <= 0.10510415956377983):
																if(angle_velocity > 0.0005936576635576785):
																	return True
															else:
																return True
													else:
														if(x_velocity > -0.04007616080343723):
															if(lander_y <= 0.6330767869949341):
																if(lander_x <= 0.17243342846632004):
																	if(x_velocity > -0.005723278969526291):
																		if(angle_velocity <= 0.014232780085876584):
																			return True
																else:
																	if(angle > -3.338768146932125e-05):
																		return True
												else:
													return True
								else:
									if(angle <= 0.02445459645241499):
										if(angle_velocity <= -0.010594240389764309):
											if(x_velocity <= -0.06686000898480415):
												if(lander_y <= 0.4584890604019165):
													if(angle <= -0.037527257576584816):
														if(x_velocity > -0.11899762600660324):
															return True
											else:
												if(lander_x <= -0.0601667407900095):
													if(angle_velocity <= -0.026763037778437138):
														if(y_velocity > -0.23292602598667145):
															return True
													else:
														if(lander_y <= 0.4152933359146118):
															return True
												else:
													if(angle <= -0.008313758298754692):
														if(angle_velocity <= -0.015609695110470057):
															return True
														else:
															if(lander_y <= 0.5234057009220123):
																return True
													else:
														if(y_velocity <= -0.23741857707500458):
															if(angle <= -0.006637597922235727):
																if(y_velocity <= -0.24024755507707596):
																	return True
														else:
															if(lander_x > -0.0330034252256155):
																if(x_velocity > -0.050365911796689034):
																	if(angle_velocity > -0.029944712296128273):
																		return True
										else:
											if(x_velocity <= -0.01786466594785452):
												if(lander_x <= 0.1260085552930832):
													if(angle <= -0.042609021067619324):
														if(angle_velocity <= 0.011550815310329199):
															if(y_velocity <= -0.2373959869146347):
																return True
															else:
																if(lander_y > 0.5282864272594452):
																	return True
														else:
															if(angle > -0.043867696076631546):
																return True
													else:
														if(y_velocity > -0.24284666776657104):
															if(lander_x <= 0.06515040248632431):
																if(angle <= -0.03354115970432758):
																	if(angle > -0.03557468019425869):
																		return True
															else:
																if(x_velocity > -0.036348216235637665):
																	if(y_velocity <= -0.2354392409324646):
																		if(y_velocity > -0.23693405836820602):
																			return True
												else:
													if(lander_y > 0.5181255340576172):
														if(angle_velocity > 0.037727318704128265):
															if(lander_x > 0.1447037234902382):
																return True
											else:
												if(lander_x <= 0.0003012180095538497):
													if(y_velocity <= -0.24066445976495743):
														if(angle <= -0.018292360240593553):
															return True
													else:
														if(angle_velocity <= 0.015264656394720078):
															if(y_velocity > -0.23373811691999435):
																if(y_velocity <= -0.22842319309711456):
																	if(lander_x > -0.09522390365600586):
																		return True
												else:
													if(lander_x <= 0.014161825180053711):
														return True
													else:
														if(angle_velocity <= 0.01480414578691125):
															if(angle_velocity > 0.003977410204242915):
																return True
							else:
								if(angle_velocity <= 0.004404015140607953):
									if(lander_y <= 0.889331191778183):
										if(y_velocity <= -0.2563770264387131):
											if(angle <= 0.00019111810252070427):
												if(lander_x <= -0.10800261422991753):
													return True
											else:
												if(angle <= 0.04863712377846241):
													if(lander_y <= 0.679532527923584):
														return True
													else:
														if(x_velocity > -0.007133440347388387):
															return True
										else:
											if(x_velocity <= -0.035182226449251175):
												if(angle <= -0.012895056512206793):
													if(lander_x <= 0.155231811106205):
														if(x_velocity <= -0.04647834226489067):
															if(angle_velocity <= -0.00507610198110342):
																if(lander_x <= -0.00315556516579818):
																	if(angle_velocity > -0.005973226157948375):
																		return True
																else:
																	if(x_velocity <= -0.056853245943784714):
																		if(lander_x <= 0.08292656019330025):
																			if(x_velocity > -0.07345131039619446):
																				if(angle <= -0.01731928624212742):
																					return True
																		else:
																			if(lander_x <= 0.1478385478258133):
																				return True
																	else:
																		return True
														else:
															if(lander_y <= 0.7306103110313416):
																return True
													else:
														return True
												else:
													if(angle_velocity <= -0.01736298482865095):
														if(angle_velocity <= -0.020350169390439987):
															if(angle <= -0.002092047070618719):
																if(angle > -0.005188233917579055):
																	return True
														else:
															return True
											else:
												if(lander_x <= -0.013243150431662798):
													if(angle_velocity > -0.03206194378435612):
														if(angle_velocity <= -0.02984893135726452):
															if(y_velocity <= -0.24922583997249603):
																return True
												else:
													if(angle <= 0.032609907910227776):
														if(angle <= 0.018990540876984596):
															if(angle_velocity <= -0.0018641488859429955):
																return True
															else:
																if(lander_y > 0.7314731478691101):
																	return True
														else:
															if(lander_x > 0.09156174957752228):
																if(lander_y > 0.8121799826622009):
																	return True
									else:
										if(x_velocity <= -0.005072366213425994):
											if(angle_velocity <= -0.02592717669904232):
												if(x_velocity <= -0.01937578897923231):
													if(lander_x > 0.1564117893576622):
														if(lander_y <= 1.0071746706962585):
															return True
												else:
													if(lander_y > 0.9797953069210052):
														return True
											else:
												if(lander_x <= -0.02310938760638237):
													if(x_velocity > -0.015252894721925259):
														return True
										else:
											return True
								else:
									if(y_velocity <= -0.25405117869377136):
										if(lander_y > 0.6789322793483734):
											if(angle <= -0.03126440942287445):
												if(angle_velocity <= 0.03554973937571049):
													if(lander_y > 0.7018381059169769):
														if(lander_x <= -0.1862165406346321):
															if(lander_x <= -0.20063187927007675):
																return True
														else:
															return True
									else:
										if(lander_x > 0.0815114974975586):
											if(lander_x <= 0.0852104164659977):
												return True
											else:
												if(y_velocity <= -0.2509196400642395):
													if(x_velocity > -0.060327403247356415):
														if(lander_y > 0.7441609501838684):
															if(lander_y <= 0.7657613754272461):
																return True
						else:
							if(lander_y <= 0.6782035827636719):
								if(y_velocity <= -0.24171631038188934):
									if(angle <= -0.007669943850487471):
										if(angle_velocity <= -0.00637316657230258):
											if(lander_y <= 0.4557790011167526):
												if(y_velocity > -0.24838769435882568):
													return True
											else:
												if(lander_x <= -0.18014349788427353):
													if(y_velocity > -0.2494477555155754):
														return True
												else:
													return True
										else:
											if(angle <= -0.07778352499008179):
												if(angle_velocity <= 0.2345825880765915):
													if(lander_y > 0.45886167883872986):
														if(angle_velocity <= 0.202462337911129):
															return True
											else:
												if(angle <= -0.008114891592413187):
													if(angle_velocity <= 0.019101232290267944):
														if(angle <= -0.03783738240599632):
															return True
														else:
															if(angle_velocity <= 0.01796173956245184):
																if(lander_y <= 0.4165329188108444):
																	return True
																else:
																	if(lander_y > 0.5537807047367096):
																		if(lander_y <= 0.6194112002849579):
																			return True
															else:
																return True
													else:
														if(x_velocity <= 0.028966717422008514):
															if(lander_y > 0.617910772562027):
																if(lander_y <= 0.6395766735076904):
																	return True
														else:
															if(y_velocity > -0.2502943277359009):
																if(y_velocity <= -0.24990147352218628):
																	return True
																else:
																	if(angle_velocity > 0.08107097074389458):
																		if(lander_x > -0.23189949989318848):
																			if(lander_y > 0.5135963261127472):
																				if(lander_x <= -0.2213435396552086):
																					return True
												else:
													return True
									else:
										if(lander_y <= 0.6139775216579437):
											if(angle_velocity <= -0.030039803124964237):
												if(lander_x > -0.07439098320901394):
													return True
											else:
												if(angle <= -0.0029058005893602967):
													if(angle <= -0.0031031006947159767):
														if(lander_y > 0.5822350084781647):
															if(x_velocity > 0.035679278895258904):
																return True
													else:
														return True
												else:
													if(lander_y > 0.5913910567760468):
														if(lander_y <= 0.5915193259716034):
															return True
										else:
											if(angle_velocity <= -0.009488389594480395):
												if(x_velocity > 0.001788595604011789):
													if(y_velocity > -0.25768475234508514):
														return True
											else:
												if(y_velocity <= -0.24195438623428345):
													if(angle <= 0.010575601365417242):
														if(angle_velocity <= 0.031161028891801834):
															if(x_velocity <= 0.07554014772176743):
																if(angle > 0.009950333274900913):
																	return True
															else:
																return True
								else:
									if(angle <= 0.013375560287386179):
										if(angle_velocity <= 0.013561869505792856):
											if(y_velocity <= -0.2267807349562645):
												if(lander_x <= -0.21681082248687744):
													if(angle <= 0.001464070926886052):
														if(x_velocity > 0.05326969921588898):
															if(lander_y > 0.4434673339128494):
																if(x_velocity <= 0.059055546298623085):
																	if(angle_velocity <= -0.019966778345406055):
																		return True
																else:
																	return True
												else:
													if(lander_y > 0.4119488000869751):
														if(x_velocity <= 0.0024043101584538817):
															if(y_velocity <= -0.23941097408533096):
																return True
														else:
															if(lander_x <= -0.1056583859026432):
																if(x_velocity <= 0.05768898129463196):
																	if(angle <= 0.0019282285938970745):
																		if(x_velocity <= 0.05442582629621029):
																			if(lander_x <= -0.18547696620225906):
																				if(x_velocity > 0.034452106803655624):
																					return True
																			else:
																				return True
																else:
																	return True
															else:
																return True
											else:
												if(x_velocity <= 0.0576079897582531):
													if(lander_x > -0.0866231918334961):
														return True
												else:
													return True
										else:
											if(y_velocity <= -0.2323838621377945):
												if(angle <= -0.017087535001337528):
													if(angle_velocity <= 0.05514552257955074):
														if(lander_y <= 0.552348256111145):
															if(angle_velocity <= 0.03485310636460781):
																return True
														else:
															return True
													else:
														if(lander_x > -0.13679399341344833):
															return True
												else:
													if(lander_y > 0.5022633373737335):
														if(angle_velocity <= 0.043021826073527336):
															if(angle_velocity <= 0.03569735586643219):
																if(lander_x > -0.22361929714679718):
																	if(x_velocity <= 0.016786151565611362):
																		if(angle_velocity <= 0.018224431201815605):
																			return True
																	else:
																		if(x_velocity <= 0.06459629163146019):
																			if(lander_y > 0.5536052584648132):
																				if(lander_y <= 0.6176618039608002):
																					return True
																		else:
																			return True
														else:
															if(lander_x <= -0.25233928859233856):
																if(lander_y > 0.6343375742435455):
																	return True
											else:
												if(y_velocity <= -0.22693373262882233):
													if(angle <= -0.001148426381405443):
														if(lander_x <= -0.05325303040444851):
															if(angle <= -0.02865183725953102):
																if(lander_x > -0.17642078548669815):
																	return True
															else:
																if(angle_velocity <= 0.015399147756397724):
																	return True
													else:
														if(x_velocity > 0.029866842553019524):
															if(lander_y <= 0.6139527559280396):
																if(lander_y <= 0.41525180637836456):
																	return True
															else:
																if(angle_velocity <= 0.07019239291548729):
																	return True
												else:
													if(angle <= -0.03398860339075327):
														return True
									else:
										if(angle_velocity <= -0.007965500000864267):
											if(lander_y <= 0.5712693631649017):
												if(angle <= 0.015446372795850039):
													return True
												else:
													if(y_velocity > -0.23750809580087662):
														if(angle <= 0.03104319889098406):
															if(lander_y <= 0.5300270020961761):
																if(angle_velocity <= -0.018493170849978924):
																	if(y_velocity <= -0.23020152002573013):
																		if(lander_x <= -0.06969141773879528):
																			if(angle > 0.027289587073028088):
																				return True
																		else:
																			return True
															else:
																return True
														else:
															if(lander_y <= 0.42854906618595123):
																if(angle_velocity > -0.025564314797520638):
																	return True
											else:
												if(lander_x > -0.23724763840436935):
													if(x_velocity <= 0.05604192614555359):
														if(lander_x > -0.0666357520967722):
															return True
													else:
														return True
										else:
											if(x_velocity <= 0.06353048235177994):
												if(lander_x <= -0.12678442150354385):
													if(lander_y > 0.49421779811382294):
														if(y_velocity <= -0.23695968091487885):
															return True
												else:
													if(y_velocity <= -0.22701957821846008):
														if(lander_y <= 0.585104376077652):
															if(angle_velocity <= 0.01406114175915718):
																if(lander_x > 0.05004258011467755):
																	return True
											else:
												if(angle_velocity <= 0.007223339751362801):
													if(angle <= 0.03302682004868984):
														if(x_velocity > 0.08436202630400658):
															if(angle_velocity > -0.0061489667277783155):
																return True
												else:
													if(angle <= 0.014735022094100714):
														if(lander_x <= -0.21026001125574112):
															return True
													else:
														if(y_velocity <= -0.2248585820198059):
															if(angle_velocity <= 0.014313715510070324):
																if(lander_x <= -0.2393665760755539):
																	return True
							else:
								if(angle <= 0.10295573249459267):
									if(angle_velocity <= 0.042507754638791084):
										if(y_velocity <= -0.24878141283988953):
											if(lander_y <= 0.8880913555622101):
												if(angle <= -0.008234894834458828):
													if(angle_velocity <= 0.033598922193050385):
														if(x_velocity <= 0.07583780214190483):
															if(x_velocity <= 0.010667488910257816):
																if(x_velocity <= 0.004334267621743493):
																	return True
															else:
																return True
													else:
														if(angle <= -0.022935448214411736):
															return True
												else:
													if(angle_velocity <= -0.009366677608340979):
														if(angle <= 0.03616303578019142):
															if(x_velocity > 0.011128692887723446):
																return True
													else:
														if(lander_x <= -0.05180711857974529):
															if(lander_y <= 0.7781370282173157):
																if(angle_velocity <= -0.0005504920845851302):
																	return True
															else:
																if(x_velocity > 0.02442897390574217):
																	if(y_velocity > -0.2541348934173584):
																		return True
											else:
												if(angle <= 0.03284945897758007):
													if(angle_velocity <= 0.0365157425403595):
														if(y_velocity <= -0.2595241367816925):
															if(lander_x <= -0.06111025810241699):
																return True
														else:
															return True
												else:
													if(x_velocity <= 0.052442971616983414):
														if(lander_x <= 0.1016031764447689):
															if(lander_y <= 1.1686013340950012):
																if(angle_velocity <= 0.014928619842976332):
																	if(x_velocity > 0.01401378819718957):
																		if(x_velocity <= 0.03209437523037195):
																			if(lander_y > 0.9470468163490295):
																				return True
														else:
															if(angle_velocity <= -0.023328247480094433):
																if(lander_x > 0.10581402853131294):
																	return True
													else:
														if(y_velocity <= -0.25468458235263824):
															if(angle_velocity > 0.0397985614836216):
																return True
														else:
															if(angle <= 0.10042272508144379):
																if(lander_x <= 0.02957077044993639):
																	return True
																else:
																	if(y_velocity > -0.2497774437069893):
																		return True
										else:
											if(lander_y <= 0.8257634937763214):
												if(angle_velocity <= -0.007427188102155924):
													if(angle_velocity <= -0.010084525682032108):
														if(x_velocity <= 3.487712820060551e-05):
															if(angle_velocity <= -0.019358133897185326):
																return True
														else:
															return True
													else:
														if(angle_velocity > -0.009553197305649519):
															return True
												else:
													if(x_velocity <= 0.043249502778053284):
														if(y_velocity <= -0.2370046228170395):
															if(x_velocity <= 0.010765003971755505):
																if(lander_y <= 0.6931203007698059):
																	return True
															else:
																if(lander_x > -0.16030530631542206):
																	if(y_velocity <= -0.23792554438114166):
																		if(lander_y <= 0.7956951260566711):
																			if(angle <= 0.0006219688802957535):
																				if(y_velocity > -0.2414242923259735):
																					return True
																		else:
																			return True
																	else:
																		if(x_velocity > 0.013965237885713577):
																			return True
														else:
															if(angle_velocity > 0.038914481177926064):
																return True
													else:
														if(angle <= 0.03740200214087963):
															if(angle_velocity <= 0.03658078983426094):
																if(lander_y > 0.6787808537483215):
																	return True
											else:
												if(angle <= 0.029133042320609093):
													if(x_velocity <= 0.02190345898270607):
														if(y_velocity > -0.24772899597883224):
															if(y_velocity > -0.24310211092233658):
																return True
													else:
														return True
												else:
													if(angle_velocity <= -0.01388505706563592):
														if(angle <= 0.04368908703327179):
															return True
														else:
															if(lander_x <= 0.04123663902282715):
																return True
															else:
																if(angle <= 0.05412131920456886):
																	if(lander_x <= 0.05120539665222168):
																		return True
													else:
														if(x_velocity > 0.08881065249443054):
															return True
									else:
										if(x_velocity <= 0.1433681845664978):
											if(lander_y <= 0.7128623425960541):
												if(y_velocity <= -0.23475246876478195):
													if(x_velocity > 0.04234972223639488):
														if(angle_velocity <= 0.13825778663158417):
															if(lander_x > -0.3019168972969055):
																if(angle_velocity <= 0.06672092899680138):
																	if(angle <= -0.00637528661172837):
																		if(y_velocity <= -0.24509673565626144):
																			return True
																		else:
																			if(angle > -0.015334553085267544):
																				return True
												else:
													if(y_velocity > -0.22491396218538284):
														return True
											else:
												if(y_velocity <= -0.24383505433797836):
													if(angle <= -0.04584505222737789):
														if(angle_velocity <= 0.06662938743829727):
															return True
														else:
															if(x_velocity <= 0.07981361076235771):
																if(y_velocity <= -0.2601442039012909):
																	return True
																else:
																	if(lander_y <= 0.7318928837776184):
																		if(angle <= -0.060628389939665794):
																			return True
															else:
																return True
													else:
														if(lander_y > 0.7992344200611115):
															if(lander_x > -0.338242769241333):
																if(lander_y <= 1.4189164638519287):
																	if(y_velocity > -0.24742591381072998):
																		if(y_velocity <= -0.24654389917850494):
																			return True
																else:
																	if(x_velocity > 0.1303340345621109):
																		if(lander_y > 1.4234117269515991):
																			return True
												else:
													if(x_velocity <= 0.13658814877271652):
														if(angle <= -0.06513085588812828):
															if(lander_y <= 0.8160543739795685):
																return True
										else:
											if(angle_velocity > 0.06932657957077026):
												return True
								else:
									if(y_velocity <= -0.23747292160987854):
										if(angle <= 0.4293469339609146):
											if(lander_x <= 0.05115861818194389):
												if(x_velocity > 0.13500040024518967):
													if(lander_y > 1.4222301244735718):
														return True
											else:
												if(angle <= 0.3634513318538666):
													if(lander_x <= 0.069710873067379):
														if(lander_x <= 0.0687967799603939):
															if(angle_velocity <= -0.027906393632292747):
																return True
															else:
																if(y_velocity <= -0.2599165290594101):
																	return True
																else:
																	if(lander_y <= 1.4051954746246338):
																		if(lander_x <= 0.05755038373172283):
																			if(lander_x <= 0.057309580966830254):
																				if(angle <= 0.13579915463924408):
																					if(x_velocity > 0.14063924551010132):
																						if(lander_y <= 1.3546212315559387):
																							return True
																	else:
																		if(angle <= 0.14150158315896988):
																			if(x_velocity > 0.21210245043039322):
																				return True
									else:
										if(x_velocity <= 0.12892448157072067):
											if(lander_x <= 0.04707613028585911):
												if(x_velocity > 0.1123315803706646):
													return True
										else:
											if(angle <= 0.3770904541015625):
												if(lander_y <= 1.356264591217041):
													if(angle <= 0.2588009312748909):
														if(lander_x <= 0.05328202247619629):
															return True
												else:
													if(y_velocity <= -0.2308005914092064):
														if(x_velocity <= 0.13182853162288666):
															return True
														else:
															if(y_velocity > -0.23138921707868576):
																return True
		else:
			if(angle_velocity <= -0.01109519088640809):
				if(right_leg_contact != True):
					if(lander_y <= 0.5234372615814209):
						if(y_velocity <= -0.1971578523516655):
							if(angle <= 0.0107335583306849):
								if(x_velocity <= -0.04500272683799267):
									if(angle_velocity <= -0.03327598422765732):
										if(angle <= -0.008505767676979303):
											if(y_velocity <= -0.20618872344493866):
												if(x_velocity <= -0.08068354055285454):
													if(lander_y <= 0.1223687157034874):
														return True
												else:
													if(lander_x > -0.16330795362591743):
														if(angle_velocity <= -0.04211241379380226):
															return True
														else:
															if(lander_y > 0.05079450458288193):
																if(lander_x <= 0.003806733526289463):
																	if(x_velocity > -0.06500869616866112):
																		return True
																else:
																	return True
											else:
												if(y_velocity > -0.2041017785668373):
													if(x_velocity > -0.09441464766860008):
														if(lander_y > 0.029630658216774464):
															return True
										else:
											if(lander_y <= 0.21201618760824203):
												if(angle_velocity <= -0.06125285662710667):
													if(lander_x > 0.07096729148179293):
														if(x_velocity > -0.08806149661540985):
															return True
											else:
												if(angle > -0.0007596094947075471):
													return True
									else:
										if(lander_x > -0.04515476152300835):
											if(lander_y <= 0.08018750697374344):
												if(y_velocity > -0.2137577161192894):
													if(x_velocity > -0.07389353215694427):
														return True
											else:
												if(y_velocity <= -0.2175784334540367):
													if(lander_y <= 0.3196537494659424):
														if(x_velocity <= -0.05980289727449417):
															if(lander_x > 0.04013786278665066):
																if(y_velocity > -0.2228735014796257):
																	return True
														else:
															if(angle_velocity <= -0.013619365636259317):
																return True
													else:
														if(x_velocity > -0.048792796209454536):
															return True
												else:
													if(angle <= -0.022246772423386574):
														if(lander_x > 0.04974265210330486):
															if(x_velocity > -0.09106046706438065):
																return True
								else:
									if(angle_velocity <= -0.03873600624501705):
										if(angle <= 0.009614271577447653):
											if(lander_y <= 0.38996393978595734):
												if(y_velocity <= -0.2237100526690483):
													if(lander_y <= 0.11958654969930649):
														return True
												else:
													if(lander_y <= 0.04265764728188515):
														if(angle_velocity <= -0.05158418416976929):
															if(angle <= -0.003320852294564247):
																return True
															else:
																if(lander_y > 0.011282346211373806):
																	return True
														else:
															if(lander_y <= 0.01953489612787962):
																return True
															else:
																if(angle <= -0.017878013662993908):
																	return True
													else:
														if(angle <= -0.0033316476037725806):
															if(angle_velocity <= -0.0416334867477417):
																if(y_velocity <= -0.2038421705365181):
																	return True
																else:
																	if(y_velocity > -0.20269667357206345):
																		return True
															else:
																if(lander_y <= 0.2587813660502434):
																	if(angle_velocity > -0.04149291478097439):
																		return True
														else:
															if(angle <= -0.0019331203075125813):
																if(lander_x > -0.11544475331902504):
																	if(angle_velocity <= -0.048041269183158875):
																		return True
															else:
																if(y_velocity <= -0.21046802401542664):
																	if(y_velocity <= -0.21110012382268906):
																		if(angle <= 0.008313753642141819):
																			if(angle_velocity <= -0.04226374626159668):
																				return True
																			else:
																				if(lander_x <= -0.03500175569206476):
																					return True
																		else:
																			if(lander_x > -0.05994052952155471):
																				return True
																else:
																	return True
											else:
												if(angle_velocity <= -0.05217112973332405):
													return True
												else:
													if(lander_y > 0.4278799444437027):
														return True
										else:
											if(lander_y <= 0.49673160910606384):
												if(x_velocity > 0.023714778944849968):
													if(angle <= 0.01028698030859232):
														return True
											else:
												return True
									else:
										if(angle <= -0.017591786570847034):
											if(lander_x <= -0.06204400025308132):
												if(x_velocity <= -0.009615412447601557):
													if(angle <= -0.022226118482649326):
														if(lander_x <= -0.17760396003723145):
															if(angle <= -0.05206279829144478):
																if(x_velocity > -0.03890976682305336):
																	return True
														else:
															if(angle <= -0.030797327868640423):
																if(y_velocity <= -0.2020140364766121):
																	return True
															else:
																if(y_velocity <= -0.20748993754386902):
																	if(lander_y > 0.16800661385059357):
																		if(angle_velocity <= -0.024481746833771467):
																			return True
																else:
																	return True
												else:
													if(angle > -0.04703420028090477):
														if(lander_y > 0.0005610740336123854):
															if(angle_velocity <= -0.011851252987980843):
																if(y_velocity <= -0.22352906316518784):
																	if(angle <= -0.02740698680281639):
																		return True
																else:
																	if(x_velocity <= -0.007450368953868747):
																		if(angle_velocity <= -0.017297599464654922):
																			return True
																	else:
																		return True
											else:
												return True
										else:
											if(lander_y <= 0.3056928813457489):
												if(y_velocity <= -0.2121613472700119):
													if(lander_y <= 0.17421792447566986):
														if(x_velocity <= 0.06556670367717743):
															if(angle <= -0.007533589843660593):
																if(y_velocity > -0.21823590248823166):
																	if(angle > -0.014045950025320053):
																		return True
															else:
																if(angle > 0.007243534550070763):
																	if(x_velocity > 0.04306749999523163):
																		return True
														else:
															return True
													else:
														if(y_velocity <= -0.21849275380373):
															if(lander_x > -0.2251472920179367):
																if(x_velocity <= 0.042945344001054764):
																	if(lander_x > -0.060500429943203926):
																		if(x_velocity > -0.010808070888742805):
																			return True
																else:
																	return True
														else:
															if(x_velocity <= 0.014525707345455885):
																if(angle > -0.003087206627242267):
																	if(angle_velocity > -0.02701878733932972):
																		return True
															else:
																if(lander_y <= 0.2945549488067627):
																	return True
												else:
													if(lander_y <= 0.02314615063369274):
														if(x_velocity > 0.03162580728530884):
															return True
													else:
														if(lander_x <= 0.014187526423484087):
															if(x_velocity > -0.001215156189573463):
																if(angle <= -0.0017017050413414836):
																	if(angle_velocity <= -0.013581103645265102):
																		if(angle_velocity <= -0.020318916998803616):
																			return True
																		else:
																			if(angle_velocity > -0.01922200620174408):
																				return True
																	else:
																		if(x_velocity > 0.04162782244384289):
																			return True
																else:
																	if(lander_y <= 0.11638302728533745):
																		if(lander_x <= -0.08995795249938965):
																			if(x_velocity > 0.08517949283123016):
																				return True
																		else:
																			return True
																	else:
																		if(angle > 0.006933571537956595):
																			if(y_velocity <= -0.20877941697835922):
																				return True
														else:
															if(angle_velocity <= -0.03484294191002846):
																if(x_velocity > -0.016145913861691952):
																	return True
															else:
																return True
											else:
												if(lander_x <= -0.02732639294117689):
													if(x_velocity <= 0.04054240509867668):
														if(lander_x > -0.20129163563251495):
															if(x_velocity <= 0.006260686321184039):
																if(angle <= -0.015639803372323513):
																	return True
																else:
																	if(angle_velocity <= -0.03039668034762144):
																		if(x_velocity > -0.011379038216546178):
																			return True
															else:
																if(angle <= 0.002376112388446927):
																	return True
																else:
																	if(lander_y <= 0.33565984666347504):
																		return True
													else:
														if(angle <= 0.009536838624626398):
															if(lander_x <= -0.21133217215538025):
																return True
												else:
													if(angle <= 0.0015949156950227916):
														return True
													else:
														if(angle > 0.004241250571794808):
															return True
							else:
								if(angle_velocity <= -0.06347468122839928):
									if(angle <= 0.11405843868851662):
										if(lander_y <= 0.1087837889790535):
											if(lander_y <= 0.06165244244039059):
												if(y_velocity > -0.21278832107782364):
													return True
										else:
											if(angle <= 0.052092377096414566):
												return True
											else:
												if(y_velocity > -0.2149878814816475):
													if(y_velocity <= -0.2003796547651291):
														if(angle <= 0.058106908574700356):
															if(y_velocity > -0.20573554933071136):
																return True
														else:
															return True
								else:
									if(lander_y <= 0.15496191382408142):
										if(y_velocity <= -0.20434628427028656):
											if(angle <= 0.02040480077266693):
												if(y_velocity <= -0.21522805094718933):
													if(angle_velocity <= -0.05080771818757057):
														if(y_velocity <= -0.22017275542020798):
															return True
												else:
													if(lander_x <= 0.059494875371456146):
														if(x_velocity > 0.01969167683273554):
															if(lander_x > -0.14242224395275116):
																return True
													else:
														return True
											else:
												if(x_velocity > 0.08594369143247604):
													if(y_velocity > -0.20771224051713943):
														return True
										else:
											if(angle_velocity <= -0.031124630942940712):
												if(angle <= 0.04484415240585804):
													if(lander_y <= 0.03519080579280853):
														if(y_velocity > -0.19916348904371262):
															return True
													else:
														if(y_velocity <= -0.19731296598911285):
															return True
											else:
												if(angle <= 0.020403779111802578):
													if(y_velocity > -0.2004377841949463):
														if(y_velocity <= -0.19963639229536057):
															return True
									else:
										if(angle <= 0.042803024873137474):
											if(y_velocity <= -0.21623970568180084):
												if(lander_y <= 0.34502965211868286):
													if(angle_velocity <= -0.036895280703902245):
														if(y_velocity > -0.22144688665866852):
															if(lander_y > 0.21191608905792236):
																if(lander_y <= 0.3218018412590027):
																	return True
													else:
														if(y_velocity > -0.21681158244609833):
															if(lander_x > 0.08846440352499485):
																return True
												else:
													if(angle <= 0.02758010569959879):
														if(x_velocity > -0.01779560884460807):
															if(x_velocity <= -0.0012674953613895923):
																if(lander_x > 0.03411898575723171):
																	return True
															else:
																return True
													else:
														if(x_velocity <= 0.09785904735326767):
															if(lander_x > -0.13933706283569336):
																if(angle_velocity <= -0.02688912022858858):
																	return True
																else:
																	if(lander_x <= -0.072903823107481):
																		if(angle <= 0.032312186434865):
																			return True
														else:
															return True
											else:
												if(x_velocity <= 0.06280925124883652):
													if(lander_y <= 0.3163684159517288):
														if(lander_x <= 0.025122356601059437):
															if(angle_velocity <= -0.04699285887181759):
																return True
															else:
																if(y_velocity <= -0.20552700757980347):
																	if(angle > 0.01394487265497446):
																		if(x_velocity > 0.056929245591163635):
																			if(lander_y <= 0.19123990833759308):
																				return True
																else:
																	if(angle <= 0.029211956076323986):
																		return True
														else:
															if(x_velocity > -0.03566419705748558):
																if(angle_velocity <= -0.01410002913326025):
																	if(y_velocity > -0.21473976969718933):
																		return True
													else:
														if(y_velocity <= -0.21319089084863663):
															return True
														else:
															if(x_velocity <= 0.05624804459512234):
																if(lander_x <= 0.10452795028686523):
																	if(lander_y > 0.4113921821117401):
																		if(y_velocity <= -0.20844776928424835):
																			return True
																else:
																	if(x_velocity > -0.03246714733541012):
																		return True
															else:
																if(y_velocity > -0.21005799621343613):
																	return True
												else:
													if(y_velocity <= -0.20755164325237274):
														if(lander_y > 0.17654933035373688):
															if(lander_x <= -0.1600053757429123):
																if(angle <= 0.02932643610984087):
																	return True
															else:
																if(angle_velocity <= -0.01821210514754057):
																	return True
																else:
																	if(angle_velocity > -0.018008616752922535):
																		return True
													else:
														return True
										else:
											if(y_velocity <= -0.19896094501018524):
												if(angle <= 0.06532834470272064):
													if(angle_velocity <= -0.03555918484926224):
														if(x_velocity <= 0.09161169081926346):
															if(lander_x > -0.08843240514397621):
																if(x_velocity > 0.02752626407891512):
																	if(x_velocity <= 0.07643027231097221):
																		return True
														else:
															if(lander_x <= -0.25998570024967194):
																if(lander_x <= -0.2754611521959305):
																	return True
															else:
																return True
													else:
														if(lander_y <= 0.4755209684371948):
															if(x_velocity <= 0.15868263691663742):
																if(y_velocity <= -0.20105457305908203):
																	if(x_velocity > 0.10151506215333939):
																		if(lander_x > -0.18458478152751923):
																			return True
																else:
																	if(y_velocity <= -0.19981536269187927):
																		return True
															else:
																return True
											else:
												if(angle_velocity <= -0.025362825952470303):
													if(x_velocity <= 0.06007133238017559):
														if(lander_x > 0.0679500075057149):
															return True
													else:
														if(angle_velocity <= -0.043294887989759445):
															if(y_velocity <= -0.19818031042814255):
																return True
														else:
															return True
						else:
							if(x_velocity <= 0.0011435417691245675):
								if(lander_x <= 0.015800190158188343):
									if(angle <= -0.055125484243035316):
										return True
									else:
										if(angle_velocity <= -0.07059032469987869):
											if(angle <= 0.01665340829640627):
												return True
										else:
											if(angle_velocity <= -0.02607179619371891):
												if(angle_velocity <= -0.02760558482259512):
													if(angle <= -0.009582070168107748):
														if(angle > -0.01621855143457651):
															if(angle <= -0.014363113790750504):
																return True
															else:
																if(y_velocity <= -0.19560135900974274):
																	return True
												else:
													if(angle > -0.035965751856565475):
														return True
								else:
									if(angle_velocity <= -0.04469680041074753):
										if(lander_y <= 0.10058356449007988):
											if(lander_y <= 0.0019821441455860622):
												if(y_velocity > -0.17780404537916183):
													return True
											else:
												if(y_velocity <= -0.16840074956417084):
													return True
										else:
											if(lander_x <= 0.016848516650497913):
												return True
									else:
										if(x_velocity <= -0.023783325217664242):
											if(angle <= -0.010971731040626764):
												if(x_velocity > -0.04097524285316467):
													return True
											else:
												if(angle <= 0.03952940180897713):
													if(lander_y > 0.3908946365118027):
														if(angle_velocity <= -0.035638272762298584):
															return True
										else:
											if(angle <= 0.025992137379944324):
												if(angle_velocity <= -0.013786638621240854):
													if(y_velocity <= -0.19353199750185013):
														if(lander_x > 0.10590395703911781):
															return True
													else:
														if(angle_velocity <= -0.022440374828875065):
															return True
														else:
															if(angle_velocity > -0.019915688782930374):
																return True
											else:
												if(lander_y <= 0.4093811511993408):
													if(y_velocity <= -0.18997720628976822):
														if(x_velocity > -0.008326976094394922):
															if(angle > 0.03605004400014877):
																return True
												else:
													return True
							else:
								if(y_velocity <= -0.15708663314580917):
									if(angle <= 0.055927980691194534):
										if(angle_velocity <= -0.029996730387210846):
											if(lander_y <= 0.22265808284282684):
												if(x_velocity <= 0.05057523027062416):
													if(lander_x <= 0.003647613455541432):
														if(angle <= 0.03232170734554529):
															if(x_velocity <= 0.01392990630120039):
																if(x_velocity <= 0.007273729424923658):
																	return True
															else:
																if(x_velocity <= 0.04961695522069931):
																	if(x_velocity <= 0.04707523062825203):
																		return True
																	else:
																		if(lander_y <= 0.0654207319021225):
																			return True
														else:
															if(angle > 0.037334516644477844):
																if(angle_velocity <= -0.0630903709679842):
																	return True
													else:
														return True
												else:
													if(lander_x <= -0.1860310062766075):
														if(lander_x <= -0.18918657302856445):
															return True
													else:
														return True
											else:
												if(y_velocity <= -0.18175316601991653):
													if(x_velocity <= 0.058019060641527176):
														if(lander_x <= -0.13314781337976456):
															if(angle_velocity <= -0.06879015266895294):
																return True
															else:
																if(y_velocity > -0.18628955632448196):
																	return True
														else:
															return True
													else:
														if(lander_x <= -0.12465257942676544):
															return True
														else:
															if(lander_y <= 0.29560112208127975):
																return True
										else:
											if(angle <= 0.0255026426166296):
												if(lander_x <= -0.04367666319012642):
													if(x_velocity <= 0.01822946034371853):
														if(angle <= -0.004283868474885821):
															if(x_velocity <= 0.015560395084321499):
																return True
													else:
														if(angle_velocity > -0.028262783773243427):
															if(angle_velocity <= -0.01770548801869154):
																if(y_velocity <= -0.1745178923010826):
																	if(lander_x <= -0.22383809089660645):
																		if(lander_x <= -0.2353208288550377):
																			return True
																	else:
																		if(angle <= 0.014435872435569763):
																			return True
																		else:
																			if(x_velocity > 0.04773258417844772):
																				return True
																else:
																	if(angle <= 0.010273960826452821):
																		return True
															else:
																if(lander_x <= -0.09532566368579865):
																	if(x_velocity <= 0.0507375281304121):
																		if(x_velocity <= 0.025258666835725307):
																			return True
																	else:
																		if(y_velocity <= -0.17010528594255447):
																			return True
																else:
																	return True
												else:
													return True
											else:
												if(y_velocity <= -0.18513454496860504):
													if(lander_y <= 0.22858544439077377):
														if(x_velocity <= 0.09050897136330605):
															if(lander_x > 0.14186649024486542):
																return True
														else:
															if(y_velocity <= -0.19011235982179642):
																return True
													else:
														if(lander_x > -0.1384853795170784):
															if(angle <= 0.048908576369285583):
																if(lander_y <= 0.28573012351989746):
																	if(angle > 0.04231484979391098):
																		return True
																else:
																	return True
												else:
													if(x_velocity <= 0.0833539068698883):
														if(angle_velocity <= -0.013280750252306461):
															if(x_velocity > 0.029910244047641754):
																if(lander_x <= -0.06425094604492188):
																	if(angle_velocity <= -0.014119629748165607):
																		if(lander_y > 0.08994792401790619):
																			if(angle <= 0.03540452942252159):
																				if(angle_velocity > -0.022842702455818653):
																					return True
																	else:
																		return True
																else:
																	return True
													else:
														if(lander_x <= -0.23215117305517197):
															if(x_velocity > 0.12539780884981155):
																return True
														else:
															return True
									else:
										if(y_velocity <= -0.18687207251787186):
											if(lander_y <= 0.3379046618938446):
												if(lander_x > -0.13328032940626144):
													if(x_velocity > 0.10170841962099075):
														if(angle <= 0.07501555234193802):
															return True
											else:
												if(angle_velocity <= -0.016473854891955853):
													if(angle_velocity <= -0.05001203343272209):
														if(lander_y <= 0.4006785899400711):
															if(angle_velocity <= -0.07887016981840134):
																return True
														else:
															if(angle_velocity <= -0.11767267063260078):
																return True
															else:
																if(y_velocity > -0.19001012295484543):
																	if(angle_velocity <= -0.05983622930943966):
																		return True
													else:
														return True
										else:
											if(lander_y <= 0.1910877674818039):
												if(angle_velocity <= -0.056722452864050865):
													return True
												else:
													if(lander_x > -0.04229102050885558):
														if(lander_x <= 0.018885421566665173):
															return True
											else:
												if(x_velocity <= 0.11261632665991783):
													if(lander_y <= 0.255778931081295):
														if(x_velocity > 0.08044421672821045):
															return True
													else:
														if(lander_x > -0.06852855533361435):
															if(x_velocity > 0.048225332982838154):
																return True
												else:
													if(x_velocity <= 0.17195049673318863):
														if(lander_y <= 0.4196188747882843):
															if(angle_velocity <= -0.06635932996869087):
																if(angle > 0.08471350744366646):
																	return True
															else:
																return True
														else:
															if(angle_velocity <= -0.08727699518203735):
																return True
															else:
																if(x_velocity <= 0.14947761595249176):
																	if(lander_x > -0.13791736960411072):
																		return True
																else:
																	if(x_velocity <= 0.169244222342968):
																		if(y_velocity > -0.18446720391511917):
																			return True
								else:
									if(lander_y <= 0.02113238349556923):
										return True
									else:
										if(angle_velocity <= -0.011243961751461029):
											if(lander_x > -0.051788236014544964):
												if(lander_y > 0.09482178464531898):
													return True
										else:
											return True
					else:
						if(x_velocity <= 0.1182720772922039):
							if(lander_y <= 1.4159489870071411):
								if(x_velocity <= -0.2558598518371582):
									if(angle <= -0.0816878229379654):
										if(lander_y <= 1.3962932229042053):
											return True
								else:
									if(angle <= 0.015097778290510178):
										if(x_velocity <= -0.034011710435152054):
											if(angle_velocity <= -0.05374739691615105):
												if(angle <= -0.009260292630642653):
													if(lander_y <= 1.4135539531707764):
														if(y_velocity <= -0.148211307823658):
															return True
														else:
															if(x_velocity <= -0.17158370465040207):
																return True
											else:
												if(lander_x <= 0.10194678045809269):
													if(angle_velocity <= -0.03231293894350529):
														if(angle <= -0.013385280966758728):
															return True
												else:
													return True
										else:
											if(lander_y <= 0.5317800343036652):
												if(lander_x > -0.009291745722293854):
													return True
											else:
												return True
									else:
										if(angle_velocity <= -0.03397380746901035):
											if(lander_y <= 0.6864185929298401):
												if(y_velocity > -0.22251423448324203):
													if(x_velocity <= 0.030961166135966778):
														if(x_velocity <= -0.016317512840032578):
															return True
														else:
															if(angle <= 0.01918367575854063):
																return True
													else:
														return True
											else:
												if(x_velocity <= 0.058617839589715004):
													if(angle_velocity <= -0.37056033313274384):
														return True
													else:
														if(x_velocity > 0.012419880833476782):
															if(angle_velocity <= -0.2228338047862053):
																if(angle_velocity <= -0.27831925451755524):
																	return True
															else:
																if(lander_y <= 0.9218689501285553):
																	if(angle <= 0.12585018947720528):
																		return True
																	else:
																		if(x_velocity > 0.046162309125065804):
																			return True
																else:
																	if(y_velocity <= -0.222663052380085):
																		if(y_velocity > -0.22370660305023193):
																			return True
												else:
													if(y_velocity <= -0.2002694457769394):
														if(angle_velocity <= -0.1456744521856308):
															if(y_velocity <= -0.2088509127497673):
																if(angle_velocity <= -0.31164443492889404):
																	return True
																else:
																	if(angle <= 0.20877940952777863):
																		if(angle > 0.2042865976691246):
																			return True
															else:
																return True
														else:
															if(lander_x <= 0.11833129078149796):
																if(angle <= 0.15269678831100464):
																	if(angle_velocity <= -0.04049842804670334):
																		if(x_velocity <= 0.06560581922531128):
																			if(lander_y <= 1.0275564193725586):
																				return True
																		else:
																			return True
																else:
																	if(angle_velocity <= -0.09067074954509735):
																		return True
													else:
														if(lander_y <= 0.9670573770999908):
															return True
										else:
											if(lander_y <= 0.5836990177631378):
												if(x_velocity > 0.057437339797616005):
													if(y_velocity <= -0.20619171857833862):
														if(x_velocity > 0.05988443270325661):
															return True
											else:
												if(x_velocity <= 0.010020026937127113):
													if(x_velocity > 0.007299841847270727):
														return True
							else:
								if(y_velocity <= -0.20843198895454407):
									if(y_velocity <= -0.22065477073192596):
										return True
								else:
									if(angle <= -0.04813877120614052):
										if(y_velocity <= -0.16151153296232224):
											if(lander_y <= 1.508604645729065):
												if(lander_x <= -0.04733452759683132):
													return True
												else:
													if(y_velocity <= -0.17122621089220047):
														return True
											else:
												if(lander_y > 1.5100222826004028):
													return True
										else:
											if(y_velocity > -0.15729797631502151):
												if(angle_velocity <= -0.13756970316171646):
													if(angle_velocity > -0.48991283774375916):
														return True
												else:
													if(angle > -0.09075165167450905):
														return True
									else:
										if(angle_velocity <= -0.06140822544693947):
											return True
						else:
							if(lander_x <= 0.08426184579730034):
								return True
							else:
								if(y_velocity <= -0.17774006724357605):
									if(y_velocity <= -0.2086435928940773):
										if(x_velocity <= 0.1553923711180687):
											if(lander_y <= 1.1958619356155396):
												if(y_velocity <= -0.22336044907569885):
													return True
										else:
											if(angle <= 0.2830250412225723):
												if(angle_velocity <= -0.05138550139963627):
													return True
									else:
										if(x_velocity <= 0.27152805030345917):
											if(angle_velocity <= -0.05723921023309231):
												if(lander_x <= 0.15445046871900558):
													if(angle_velocity <= -0.0723775066435337):
														return True
													else:
														if(angle_velocity > -0.0646637212485075):
															return True
												else:
													if(angle_velocity <= -0.16303861886262894):
														if(angle <= 0.34828269481658936):
															return True
				else:
					if(angle <= -0.06543062441051006):
						if(angle_velocity <= -0.5765689015388489):
							if(y_velocity <= -0.21171773225069046):
								if(angle_velocity <= -0.6924467980861664):
									return True
							else:
								return True
						else:
							if(angle <= -0.28274887800216675):
								return True
					else:
						if(x_velocity <= 0.1321985051035881):
							if(angle_velocity <= -0.724619597196579):
								return True
							else:
								if(y_velocity <= -0.2181570902466774):
									return True
						else:
							if(left_leg_contact != True):
								return True
			else:
				if(y_velocity <= -0.19208889454603195):
					if(lander_y <= 0.2897540479898453):
						if(angle <= -0.001974301296286285):
							if(x_velocity <= -0.01461441582068801):
								if(lander_y <= 0.00980702368542552):
									if(angle_velocity <= -0.005119665991514921):
										return True
									else:
										if(right_leg_contact != True):
											if(lander_y > 0.004544887458905578):
												if(lander_y <= 0.006062713917344809):
													if(angle <= -0.030654183588922024):
														return True
								else:
									if(y_velocity <= -0.21065139770507812):
										if(lander_y <= 0.16549677401781082):
											if(angle <= -0.03493528999388218):
												if(x_velocity <= -0.03977541998028755):
													if(angle_velocity <= -0.0024486881447955966):
														if(angle_velocity <= -0.005835844436660409):
															if(angle_velocity <= -0.006929071620106697):
																if(lander_y > 0.1217980831861496):
																	return True
															else:
																return True
													else:
														if(lander_x <= 0.0528874397277832):
															if(lander_y > 0.05295024998486042):
																if(lander_y > 0.12028517574071884):
																	if(lander_y <= 0.1318969614803791):
																		return True
												else:
													if(lander_x <= -0.11710600554943085):
														if(angle_velocity <= -0.004093042458407581):
															return True
													else:
														if(angle <= -0.0471199844032526):
															return True
														else:
															if(lander_y > 0.1439994052052498):
																return True
											else:
												if(lander_y > 0.07413315400481224):
													if(y_velocity > -0.21574554592370987):
														if(angle <= -0.02462300844490528):
															return True
										else:
											if(angle <= -0.024513673037290573):
												if(lander_x > 0.11286602169275284):
													if(lander_y <= 0.22845791280269623):
														return True
											else:
												if(y_velocity > -0.22127367556095123):
													if(angle_velocity <= 0.03473819978535175):
														if(lander_y > 0.24431777745485306):
															if(x_velocity > -0.03543645143508911):
																if(lander_x > -0.0016593458130955696):
																	return True
									else:
										if(x_velocity <= -0.025622901506721973):
											if(angle <= -0.047295982018113136):
												if(lander_x <= 0.0035557270057324786):
													if(x_velocity <= -0.03496578708291054):
														if(angle <= -0.060785090550780296):
															if(angle > -0.06955886632204056):
																return True
													else:
														return True
												else:
													return True
											else:
												if(lander_y > 0.014223549049347639):
													if(angle <= -0.0398060604929924):
														if(angle > -0.04114944115281105):
															return True
										else:
											if(angle_velocity <= 0.00881808646954596):
												if(lander_x > -0.121637724339962):
													if(angle_velocity > -0.008143778424710035):
														if(y_velocity > -0.20849178731441498):
															return True
											else:
												if(lander_x <= 0.09575405344367027):
													if(angle <= -0.04643068462610245):
														if(lander_y > 0.06374220550060272):
															return True
												else:
													return True
							else:
								if(lander_y <= 0.17636018991470337):
									if(y_velocity <= -0.20780175924301147):
										if(angle <= -0.029647454619407654):
											if(x_velocity <= 0.004933268181048334):
												if(angle <= -0.03637485392391682):
													if(angle > -0.04454756900668144):
														if(lander_x > -0.05945158191025257):
															return True
												else:
													if(angle_velocity <= -0.006891900207847357):
														return True
											else:
												if(lander_x > -0.244578555226326):
													if(lander_x <= -0.19666409492492676):
														if(angle <= -0.049405982717871666):
															return True
														else:
															if(x_velocity > 0.024441578425467014):
																if(lander_y <= 0.08263836614787579):
																	return True
													else:
														return True
										else:
											if(angle_velocity <= -0.0058912960812449455):
												if(x_velocity <= 0.0614925604313612):
													if(angle <= -0.012152002658694983):
														return True
												else:
													return True
											else:
												if(angle <= -0.002356428885832429):
													if(y_velocity <= -0.2082531675696373):
														if(angle_velocity <= 0.017753158695995808):
															if(angle_velocity <= 0.014326295349746943):
																if(lander_y <= 0.003790936549194157):
																	return True
																else:
																	if(x_velocity <= 0.0821458138525486):
																		if(angle_velocity > 0.012988659553229809):
																			if(lander_x > -0.11444887891411781):
																				return True
																	else:
																		return True
															else:
																if(lander_x > -0.10722851753234863):
																	return True
														else:
															if(lander_x > 0.02890787087380886):
																if(lander_x <= 0.02928457222878933):
																	return True
												else:
													return True
									else:
										if(angle_velocity <= 0.014084470458328724):
											if(angle <= -0.018581273965537548):
												if(y_velocity > -0.20756550878286362):
													if(angle_velocity > -0.010733573231846094):
														if(y_velocity <= -0.20055539906024933):
															return True
														else:
															if(angle <= -0.023613708093762398):
																return True
											else:
												if(x_velocity <= 0.04151764698326588):
													if(lander_x > -0.08645911142230034):
														if(x_velocity > 0.0019716447714017704):
															return True
												else:
													if(angle > -0.009684664197266102):
														if(angle <= -0.0025655411882326007):
															if(x_velocity <= 0.05394873768091202):
																if(lander_y <= 0.07882348075509071):
																	return True
															else:
																return True
										else:
											if(lander_y <= 0.08455385640263557):
												if(angle_velocity > 0.01682453602552414):
													if(lander_y > 0.022858796641230583):
														if(angle <= -0.03435870446264744):
															if(angle <= -0.04383568838238716):
																return True
														else:
															if(x_velocity > -0.005795223638415337):
																if(y_velocity > -0.1949629932641983):
																	return True
											else:
												if(x_velocity <= 0.06846123188734055):
													if(lander_x <= 0.10798463970422745):
														if(x_velocity > 0.01650381088256836):
															if(angle_velocity > 0.0359306912869215):
																if(lander_y > 0.1353665217757225):
																	return True
													else:
														return True
								else:
									if(y_velocity <= -0.21350980550050735):
										if(lander_y <= 0.22156928479671478):
											if(x_velocity > 0.0022984480601735413):
												if(angle_velocity <= -0.0065377524588257074):
													return True
												else:
													if(angle > -0.0063004810363054276):
														return True
										else:
											if(angle_velocity <= 0.00941420067101717):
												if(angle <= -0.00994016882032156):
													return True
												else:
													if(y_velocity > -0.21747388690710068):
														if(x_velocity <= 0.0126884994097054):
															return True
											else:
												if(x_velocity <= 0.04361279867589474):
													if(lander_x > 0.01591725368052721):
														if(y_velocity <= -0.21712232381105423):
															if(lander_y > 0.24246787279844284):
																return True
												else:
													if(angle <= -0.014380637090653181):
														return True
									else:
										if(angle_velocity <= 0.010462206788361073):
											if(lander_y <= 0.25021277368068695):
												if(y_velocity > -0.21185879409313202):
													if(lander_y <= 0.18268869817256927):
														if(lander_x <= -0.23379047214984894):
															return True
													else:
														if(lander_x <= -0.17782209068536758):
															if(x_velocity > 0.023040185420541093):
																return True
														else:
															return True
										else:
											if(x_velocity <= 0.05154911056160927):
												if(lander_x > -0.02145376242697239):
													if(angle <= -0.018772676587104797):
														return True
													else:
														if(angle_velocity <= 0.02569399494677782):
															return True
											else:
												if(x_velocity <= 0.056840525940060616):
													if(x_velocity > 0.05473960563540459):
														return True
												else:
													if(angle <= -0.013219031039625406):
														if(lander_x > -0.22745025157928467):
															return True
						else:
							if(right_leg_contact != True):
								if(y_velocity <= -0.20635643601417542):
									if(x_velocity > -0.027317581698298454):
										if(angle <= 0.10114578157663345):
											if(lander_x > -0.2811438590288162):
												if(angle <= 0.018739018589258194):
													if(angle_velocity <= -0.005446673603728414):
														if(lander_x <= 0.04728131368756294):
															if(angle_velocity <= -0.006448284490033984):
																if(x_velocity <= 0.04670148901641369):
																	if(lander_x > 0.014701509848237038):
																		if(lander_y <= 0.0636820551007986):
																			return True
																else:
																	return True
														else:
															return True
													else:
														if(angle <= 0.018694463185966015):
															if(lander_y <= 0.2418917417526245):
																if(lander_x <= 0.15335922688245773):
																	if(lander_x > -0.2490876391530037):
																		if(x_velocity > 0.05325937829911709):
																			if(lander_x <= 0.01578388176858425):
																				if(angle_velocity <= 0.012258684262633324):
																					if(lander_x > -0.14829573407769203):
																						return True
																			else:
																				return True
																else:
																	if(lander_y <= 0.2299494370818138):
																		return True
															else:
																if(y_velocity > -0.21332582831382751):
																	if(lander_y > 0.2714949995279312):
																		if(lander_y > 0.2775247097015381):
																			return True
														else:
															return True
												else:
													if(y_velocity <= -0.207355335354805):
														if(lander_y > 0.2796950787305832):
															if(lander_y <= 0.28052231669425964):
																return True
													else:
														if(x_velocity > 0.12062624469399452):
															return True
								else:
									if(angle <= 0.027642766945064068):
										if(lander_y <= 0.11291278526186943):
											if(x_velocity > -0.009744551964104176):
												if(lander_x <= 0.038906002417206764):
													if(angle <= 0.026989192701876163):
														if(x_velocity > -0.0020548300817608833):
															if(angle_velocity <= -0.004507679492235184):
																if(angle_velocity > -0.004781218944117427):
																	return True
												else:
													if(angle_velocity <= 0.0020055713539477438):
														return True
													else:
														if(lander_x <= 0.07076811790466309):
															if(y_velocity > -0.1983875408768654):
																return True
														else:
															if(x_velocity > 0.03445328865200281):
																return True
										else:
											if(angle <= 0.011901159305125475):
												if(angle_velocity <= 0.020643576979637146):
													if(angle <= 0.00960160605609417):
														if(y_velocity <= -0.1995120793581009):
															if(lander_y > 0.17736715823411942):
																if(y_velocity <= -0.20391415804624557):
																	return True
																else:
																	if(lander_x <= -0.11024045944213867):
																		if(angle_velocity > -0.0008247115183621645):
																			return True
														else:
															return True
												else:
													if(lander_y <= 0.27392782270908356):
														if(angle <= 0.0006887250929139555):
															if(angle_velocity <= 0.04476818349212408):
																return True
													else:
														if(lander_y <= 0.2880541682243347):
															return True
											else:
												if(x_velocity > -0.0062241205014288425):
													if(y_velocity <= -0.19909492135047913):
														if(angle_velocity <= 0.08634553849697113):
															if(angle_velocity <= 0.01964742224663496):
																if(lander_x > -0.14925479888916016):
																	if(x_velocity > 0.04161417856812477):
																		return True
													else:
														if(lander_x <= 0.07373743131756783):
															if(lander_x > -0.14914417266845703):
																if(x_velocity > 0.05354272201657295):
																	if(lander_y > 0.22295434027910233):
																		return True
														else:
															return True
									else:
										if(angle_velocity <= 0.27043651044368744):
											if(lander_y <= 0.25494179129600525):
												if(angle_velocity <= -0.005314721260219812):
													if(angle_velocity <= -0.005757053149864078):
														if(lander_y <= 0.21493321657180786):
															if(angle <= 0.03667156584560871):
																if(lander_y <= 0.15531865507364273):
																	if(angle_velocity > -0.008354404475539923):
																		return True
														else:
															return True
												else:
													if(angle <= 0.027910239063203335):
														if(angle > 0.02786886226385832):
															return True
											else:
												if(x_velocity <= 0.07137685641646385):
													if(lander_y > 0.2812550216913223):
														return True
					else:
						if(angle <= 0.034049760550260544):
							if(x_velocity <= 0.05305109918117523):
								if(y_velocity <= -0.21372266113758087):
									if(lander_y <= 0.3575222045183182):
										if(x_velocity <= -0.010724043473601341):
											if(lander_y <= 0.3515322655439377):
												if(angle_velocity > -0.006636293372139335):
													if(angle <= -0.03804014250636101):
														if(angle > -0.042344069108366966):
															if(lander_y <= 0.32745474576950073):
																return True
											else:
												return True
										else:
											if(angle <= -0.004033001489005983):
												if(y_velocity <= -0.22201097756624222):
													if(lander_y <= 0.30483753979206085):
														return True
												else:
													if(angle <= -0.020024338737130165):
														return True
													else:
														if(angle > -0.009953859262168407):
															if(lander_x > -0.12826881557703018):
																return True
											else:
												if(angle_velocity <= -0.004115351592190564):
													return True
												else:
													if(lander_y > 0.34391212463378906):
														if(lander_y <= 0.34799720346927643):
															return True
									else:
										if(x_velocity > -0.03364337235689163):
											if(angle_velocity <= -0.0014139081467874348):
												if(angle <= -0.003988478682003915):
													return True
												else:
													if(lander_x > -0.03471369808539748):
														if(angle_velocity > -0.007659282069653273):
															return True
											else:
												if(lander_y <= 0.5525970458984375):
													if(lander_x > -0.10589723661541939):
														if(y_velocity <= -0.2196420505642891):
															if(angle_velocity <= 0.020431251265108585):
																if(angle <= 0.012532577500678599):
																	return True
															else:
																if(y_velocity <= -0.22150888293981552):
																	if(angle_velocity <= 0.033169619739055634):
																		if(angle <= -0.006665428867563605):
																			if(angle_velocity <= 0.026700724847614765):
																				return True
																else:
																	if(lander_x > -0.02060365746729076):
																		return True
														else:
															if(lander_y <= 0.5222991704940796):
																if(x_velocity <= 0.03970935940742493):
																	if(angle_velocity <= 0.023540607653558254):
																		if(angle <= -2.1919142454862595e-05):
																			if(lander_x > -0.06499791145324707):
																				return True
																else:
																	if(angle <= 0.011842965614050627):
																		return True
															else:
																if(y_velocity > -0.21910078078508377):
																	return True
												else:
													if(angle > 0.023786209523677826):
														if(angle <= 0.024443095549941063):
															return True
														else:
															if(lander_x > 0.0425267219543457):
																if(x_velocity > 0.028033524751663208):
																	return True
								else:
									if(lander_x <= -0.0046904562041163445):
										if(angle_velocity <= -0.010266120545566082):
											return True
										else:
											if(angle <= 0.025997248478233814):
												if(angle <= -0.03068194631487131):
													if(angle > -0.0321212038397789):
														return True
												else:
													if(x_velocity > 0.04653698578476906):
														if(x_velocity <= 0.04709045775234699):
															return True
									else:
										if(x_velocity <= -0.02208183240145445):
											if(lander_x <= 0.033309316262602806):
												if(lander_x > 0.030749320052564144):
													return True
										else:
											if(angle_velocity <= 0.0024770539021119475):
												if(lander_y <= 0.4256361424922943):
													return True
											else:
												if(x_velocity <= 0.03922008164227009):
													if(x_velocity <= -0.02160018589347601):
														return True
													else:
														if(lander_x <= -0.004368925001472235):
															return True
														else:
															if(y_velocity > -0.2135368511080742):
																if(angle <= -0.025066950358450413):
																	if(angle > -0.02567780762910843):
																		return True
																else:
																	if(lander_x <= 0.13135547190904617):
																		if(x_velocity <= 0.023885557428002357):
																			if(angle_velocity <= 0.01477389084175229):
																				if(angle_velocity > 0.012111582327634096):
																					return True
																	else:
																		if(lander_x <= 0.13403763622045517):
																			return True
												else:
													if(angle_velocity <= 0.023443574085831642):
														return True
							else:
								if(lander_y <= 0.4885428249835968):
									if(y_velocity <= -0.20921574532985687):
										if(angle <= 0.011685142293572426):
											if(angle_velocity <= 0.015439566690474749):
												if(angle <= 0.010880847461521626):
													return True
											else:
												if(y_velocity <= -0.2136419340968132):
													if(angle <= -0.0005988302873447537):
														if(y_velocity <= -0.2184489294886589):
															if(x_velocity <= 0.060930537059903145):
																return True
														else:
															return True
										else:
											if(angle_velocity <= -0.0015045297041069716):
												if(angle_velocity > -0.007135703461244702):
													return True
											else:
												if(lander_x > -0.326427698135376):
													if(x_velocity <= 0.06233610399067402):
														if(lander_x > -0.14032430946826935):
															if(lander_y > 0.4427211880683899):
																return True
													else:
														if(x_velocity > 0.10567198321223259):
															if(lander_x > -0.18099598586559296):
																return True
									else:
										if(lander_x <= -0.09546852111816406):
											if(angle_velocity <= 0.005387932527810335):
												if(lander_x > -0.2620481252670288):
													if(x_velocity <= 0.08193737268447876):
														if(angle <= 0.013746412936598063):
															return True
													else:
														return True
											else:
												if(x_velocity <= 0.07738113403320312):
													if(lander_x <= -0.18783941119909286):
														if(angle_velocity <= 0.013788129203021526):
															return True
												else:
													if(lander_y > 0.3158178925514221):
														if(y_velocity <= -0.19682814180850983):
															if(angle <= 0.02384153939783573):
																if(lander_x > -0.33112064003944397):
																	if(angle_velocity <= 0.05205644108355045):
																		return True
										else:
											if(angle <= 0.015679037664085627):
												return True
											else:
												if(y_velocity > -0.19918718934059143):
													if(angle_velocity <= 0.04334738478064537):
														return True
								else:
									if(lander_y <= 1.3911697268486023):
										if(angle_velocity <= 0.02309056557714939):
											if(y_velocity <= -0.218096524477005):
												if(angle <= 0.02420397661626339):
													return True
												else:
													if(y_velocity <= -0.21971922367811203):
														if(angle > 0.030224091373384):
															return True
											else:
												if(x_velocity <= 0.09193065017461777):
													if(lander_x > -0.15274892002344131):
														if(angle_velocity <= 0.009516449877992272):
															return True
												else:
													if(lander_x > -0.23825695365667343):
														return True
										else:
											if(x_velocity <= 0.14600562304258347):
												if(angle_velocity <= 0.04647490940988064):
													if(angle_velocity <= 0.043493252247571945):
														if(y_velocity <= -0.21315408498048782):
															if(lander_x <= -0.14153748005628586):
																if(lander_y <= 0.5870274603366852):
																	if(y_velocity <= -0.21557246148586273):
																		return True
															else:
																if(lander_y > 0.6160241663455963):
																	return True
													else:
														if(lander_y > 0.5992819666862488):
															return True
												else:
													if(lander_y > 0.5280139744281769):
														if(y_velocity > -0.22308366000652313):
															if(x_velocity > 0.12485217303037643):
																if(x_velocity <= 0.12699494510889053):
																	return True
											else:
												if(angle_velocity <= 0.14660384505987167):
													if(angle_velocity <= 0.06831873580813408):
														return True
													else:
														if(y_velocity > -0.2058495506644249):
															if(lander_y > 0.5763521194458008):
																return True
									else:
										return True
						else:
							if(lander_y <= 0.5863185822963715):
								if(y_velocity <= -0.20273584127426147):
									if(angle <= 0.1946142390370369):
										if(lander_y > 0.44142310321331024):
											if(x_velocity <= 0.1046687550842762):
												if(y_velocity <= -0.21798130124807358):
													if(angle_velocity <= 0.02302786521613598):
														if(y_velocity <= -0.22318175435066223):
															return True
												else:
													if(y_velocity > -0.20877746492624283):
														if(angle_velocity <= 0.029814787209033966):
															if(y_velocity <= -0.20628339052200317):
																if(angle_velocity <= 0.019804266281425953):
																	return True
											else:
												if(angle_velocity <= 0.005676704226061702):
													if(y_velocity <= -0.2129640057682991):
														if(angle <= 0.04993030987679958):
															return True
													else:
														return True
												else:
													if(lander_y <= 0.4477561116218567):
														return True
													else:
														if(y_velocity > -0.20807651430368423):
															if(y_velocity <= -0.2072468250989914):
																return True
								else:
									if(x_velocity <= 0.09705938026309013):
										if(lander_y <= 0.42095011472702026):
											if(lander_x > -0.1157781109213829):
												if(x_velocity > 0.07562413811683655):
													if(y_velocity > -0.196133591234684):
														return True
									else:
										if(angle <= 0.11374308541417122):
											if(lander_y <= 0.508734256029129):
												if(angle > 0.04096033237874508):
													if(lander_x > -0.28699319064617157):
														if(y_velocity > -0.19332081079483032):
															if(angle > 0.06660915538668633):
																return True
											else:
												if(x_velocity <= 0.17307308316230774):
													if(angle <= 0.048182547092437744):
														return True
													else:
														if(lander_x > -0.1486435905098915):
															if(x_velocity > 0.11889481917023659):
																return True
												else:
													if(y_velocity <= -0.1931348517537117):
														if(y_velocity <= -0.20176877081394196):
															return True
													else:
														return True
							else:
								if(x_velocity <= 0.2813781797885895):
									if(x_velocity <= 0.2044903039932251):
										if(lander_x <= -0.11335830762982368):
											if(y_velocity <= -0.20570598542690277):
												if(lander_y <= 0.6806885898113251):
													if(lander_x <= -0.21587343513965607):
														if(angle_velocity > 0.010703293140977621):
															if(x_velocity > 0.15296711772680283):
																return True
												else:
													if(y_velocity <= -0.2210519015789032):
														return True
											else:
												if(angle > 0.05711753852665424):
													return True
										else:
											if(y_velocity > -0.22416681796312332):
												if(lander_y <= 1.0864827036857605):
													if(lander_y <= 1.0452588200569153):
														if(angle_velocity <= 0.01179392309859395):
															if(y_velocity <= -0.22135239094495773):
																if(lander_y <= 0.6182665824890137):
																	return True
															else:
																if(angle <= 0.046070387586951256):
																	if(angle > 0.04330882430076599):
																		return True
													else:
														if(angle <= 0.1444753035902977):
															if(x_velocity <= 0.16547763347625732):
																return True
												else:
													if(lander_y > 1.4217828512191772):
														if(angle_velocity <= 0.11284030228853226):
															return True
									else:
										if(angle_velocity <= 0.0879020132124424):
											if(lander_y > 1.3319485187530518):
												if(angle_velocity <= 0.04395821690559387):
													return True
										else:
											if(angle <= 0.12765425071120262):
												if(lander_y <= 1.4216150641441345):
													return True
				else:
					if(x_velocity <= 0.07045570015907288):
						if(right_leg_contact != True):
							if(left_leg_contact != True):
								if(y_velocity <= -0.18674296140670776):
									if(angle <= 0.0206502266228199):
										if(x_velocity <= 0.05978120490908623):
											if(x_velocity > -0.0097250547260046):
												if(lander_x <= 0.02540740929543972):
													if(angle <= -0.019759160466492176):
														if(lander_x <= -0.06997428089380264):
															if(angle > -0.02061108872294426):
																return True
														else:
															return True
													else:
														if(y_velocity <= -0.19151069968938828):
															if(y_velocity > -0.19160612672567368):
																return True
												else:
													if(lander_y <= 0.11629515886306763):
														if(x_velocity > 0.028145658783614635):
															return True
													else:
														if(lander_y <= 0.20330068469047546):
															return True
														else:
															if(angle_velocity <= 0.038037100806832314):
																return True
										else:
											if(lander_x > -0.1872841790318489):
												if(angle <= 0.0050793820882972796):
													return True
												else:
													if(y_velocity <= -0.18915868550539017):
														return True
									else:
										if(lander_y <= 0.12287139892578125):
											if(lander_x > -0.023945760913193226):
												if(angle <= 0.02484336867928505):
													if(lander_x > 0.11174916848540306):
														return True
										else:
											if(angle <= 0.022526774555444717):
												if(lander_y > 0.2275855839252472):
													return True
											else:
												if(lander_x > 0.017209386453032494):
													if(x_velocity > 0.024150562472641468):
														if(angle_velocity <= 0.005531748756766319):
															if(angle <= 0.03523879311978817):
																return True
								else:
									if(angle_velocity <= 0.0069290283136069775):
										if(lander_x <= 0.056334782391786575):
											if(angle_velocity <= 0.006530629703775048):
												if(y_velocity <= -0.1764686405658722):
													if(lander_x <= -0.0709809772670269):
														if(lander_y > 0.44085314869880676):
															return True
													else:
														if(x_velocity <= 0.03471241518855095):
															if(angle <= 0.037080058827996254):
																if(lander_y <= 0.028778360225260258):
																	if(angle_velocity > 0.0017520603723824024):
																		return True
														else:
															if(lander_y <= 0.09074575453996658):
																if(angle <= 0.024390445090830326):
																	return True
															else:
																if(x_velocity > 0.06363154761493206):
																	return True
												else:
													if(lander_y <= 0.0062898253090679646):
														return True
													else:
														if(x_velocity > 0.06309620290994644):
															if(lander_x > -0.10298142209649086):
																return True
											else:
												if(x_velocity <= 0.04881565645337105):
													return True
										else:
											if(x_velocity <= 0.011500594671815634):
												if(lander_x > 0.15299248695373535):
													if(angle <= 0.030505016446113586):
														return True
											else:
												if(lander_y <= 0.1928277686238289):
													if(angle <= 0.04679787531495094):
														return True
									else:
										if(lander_y <= 0.004686186322942376):
											if(lander_y <= 0.003906575497239828):
												if(x_velocity <= 0.020605999510735273):
													return True
										else:
											if(angle <= 0.04520220868289471):
												if(lander_y <= 0.09839480742812157):
													if(lander_y <= 0.09669607505202293):
														if(angle <= -0.03468683920800686):
															if(angle > -0.03810938447713852):
																return True
														else:
															if(angle_velocity <= 0.025887180119752884):
																if(angle_velocity <= 0.02547292783856392):
																	if(angle_velocity <= 0.023870393633842468):
																		if(lander_y <= 0.07685845717787743):
																			if(angle_velocity > 0.019193929620087147):
																				if(angle_velocity <= 0.020013706758618355):
																					return True
																		else:
																			if(angle_velocity <= 0.02060716412961483):
																				if(y_velocity <= -0.1640598401427269):
																					return True
																else:
																	return True
												else:
													if(y_velocity <= -0.14746209233999252):
														if(lander_x > 0.03522481769323349):
															if(lander_x <= 0.035636186599731445):
																return True
															else:
																if(x_velocity > 0.05211150087416172):
																	return True
													else:
														if(lander_x > -0.005261325975880027):
															return True
					else:
						if(y_velocity <= -0.17878469824790955):
							if(lander_y <= 0.3682808578014374):
								if(angle <= 0.033226991072297096):
									if(angle_velocity <= 0.032327210530638695):
										if(y_velocity <= -0.1822424978017807):
											if(y_velocity <= -0.18755576759576797):
												if(y_velocity <= -0.18873679637908936):
													if(angle <= 0.022810661233961582):
														return True
													else:
														if(y_velocity > -0.18998104333877563):
															if(angle <= 0.03160081245005131):
																return True
											else:
												return True
										else:
											if(lander_y <= 0.056553278118371964):
												if(angle_velocity <= 0.003849118947982788):
													return True
									else:
										if(lander_y > 0.09766757115721703):
											if(y_velocity <= -0.19040030241012573):
												if(lander_y > 0.16231553256511688):
													return True
											else:
												if(x_velocity > 0.11845383793115616):
													return True
								else:
									if(angle_velocity <= 0.004390476504340768):
										if(angle <= 0.05328214913606644):
											if(lander_y <= 0.21552962809801102):
												if(lander_x <= 0.008582782465964556):
													if(angle_velocity > 0.0017641475424170494):
														return True
												else:
													return True
											else:
												return True
									else:
										if(lander_y <= 0.2763689309358597):
											if(x_velocity <= 0.08989990502595901):
												if(x_velocity <= 0.08929217234253883):
													if(y_velocity <= -0.188216932117939):
														if(y_velocity > -0.18979504704475403):
															if(lander_x > -0.06621541827917099):
																if(lander_y <= 0.1490542283281684):
																	return True
											else:
												if(lander_x <= -0.1520765796303749):
													if(x_velocity > 0.1060619167983532):
														if(angle_velocity <= 0.01666631130501628):
															if(lander_x > -0.18893247097730637):
																return True
							else:
								if(x_velocity <= 0.3764907121658325):
									if(lander_y <= 1.4620787501335144):
										if(angle <= 0.07854641228914261):
											if(lander_x <= -0.012809991836547852):
												if(angle_velocity <= 0.0007023490179562941):
													if(angle_velocity > -0.003477644408121705):
														return True
												else:
													if(x_velocity <= 0.2039438560605049):
														if(x_velocity <= 0.19526255130767822):
															if(angle <= 0.009554685559123755):
																if(x_velocity > 0.16872210055589676):
																	return True
													else:
														return True
											else:
												return True
										else:
											if(angle <= 0.09951448440551758):
												if(angle_velocity <= 0.05455542355775833):
													if(x_velocity > 0.12013629823923111):
														if(lander_y > 0.5086338073015213):
															if(lander_y <= 0.5402218699455261):
																return True
												else:
													if(lander_x > -0.18617639690637589):
														if(y_velocity <= -0.18636740744113922):
															return True
									else:
										return True
								else:
									if(angle <= 0.06874822499230504):
										return True
						else:
							if(x_velocity <= 0.45725807547569275):
								if(angle_velocity <= 0.020849051885306835):
									if(angle <= 0.010707416106015444):
										return True
									else:
										if(x_velocity <= 0.1138673722743988):
											if(lander_x <= -0.10730233043432236):
												if(angle_velocity <= 0.012343046255409718):
													if(angle_velocity <= -0.006565750110894442):
														if(angle_velocity > -0.006728500593453646):
															return True
												else:
													if(angle <= 0.04613827168941498):
														if(lander_y > 0.037872765213251114):
															return True
											else:
												if(angle <= 0.049654776230454445):
													if(angle_velocity <= 0.0133334556594491):
														if(angle_velocity > -0.009545674081891775):
															if(y_velocity > -0.17694725841283798):
																return True
												else:
													if(y_velocity > -0.17403686791658401):
														if(x_velocity > 0.09220557659864426):
															if(y_velocity > -0.16615163534879684):
																if(angle_velocity <= -0.0054708197712898254):
																	return True
										else:
											if(angle <= 0.09788025543093681):
												if(y_velocity <= -0.17339228838682175):
													if(angle_velocity <= 0.003842043923214078):
														if(lander_y <= 0.3522111475467682):
															if(lander_y <= 0.10307086631655693):
																return True
															else:
																if(lander_y <= 0.19324154406785965):
																	if(lander_y > 0.17379280924797058):
																		return True
														else:
															if(x_velocity > 0.1355704814195633):
																return True
												else:
													if(y_velocity <= -0.1659632921218872):
														return True
													else:
														if(angle <= 0.06073630414903164):
															return True
														else:
															if(angle > 0.06834540143609047):
																if(y_velocity > -0.1597970724105835):
																	return True
								else:
									if(lander_y <= 0.04226007126271725):
										if(left_leg_contact != True):
											if(y_velocity <= -0.16917701810598373):
												if(angle > 0.019545963034033775):
													if(lander_y <= 0.003287003026343882):
														if(lander_y > -0.013078692252747715):
															return True
											else:
												if(x_velocity <= 0.15987766534090042):
													if(lander_x <= -0.2338159829378128):
														return True
												else:
													if(x_velocity > 0.16599652916193008):
														return True
									else:
										if(y_velocity <= -0.13968756049871445):
											if(x_velocity <= 0.40679629147052765):
												if(y_velocity <= -0.17383474111557007):
													if(lander_y <= 0.3370380997657776):
														if(angle <= 0.07535969465970993):
															if(y_velocity <= -0.1740221008658409):
																if(x_velocity > 0.13857810199260712):
																	return True
															else:
																if(y_velocity > -0.1738743633031845):
																	return True
													else:
														if(lander_y > 1.4222396612167358):
															return True
												else:
													if(angle <= -0.004808521131053567):
														if(angle > -0.007374115288257599):
															return True
													else:
														if(angle_velocity <= 0.15649355202913284):
															if(angle_velocity <= 0.02203170582652092):
																if(angle_velocity > 0.021947107277810574):
																	return True
															else:
																if(lander_y <= 0.1910090520977974):
																	if(lander_y <= 0.18781189620494843):
																		if(lander_x <= 0.009559154510498047):
																			if(angle <= 0.029744844883680344):
																				if(lander_y > 0.13008564338088036):
																					return True
														else:
															if(y_velocity <= -0.16667479276657104):
																return True
															else:
																if(angle_velocity <= 0.16878244280815125):
																	if(angle_velocity > 0.16628387570381165):
																		return True
											else:
												if(y_velocity <= -0.1588578298687935):
													if(angle_velocity > 0.2123352363705635):
														if(x_velocity <= 0.4303390234708786):
															return True
										else:
											if(angle <= 0.09093538671731949):
												return True
							else:
								if(x_velocity <= 0.5235196650028229):
									if(angle_velocity <= 0.2699975222349167):
										if(angle <= 0.1340556386858225):
											return True
	else:
		if(angle <= 0.18057335913181305):
			if(lander_y <= 0.04876668006181717):
				if(angle_velocity <= 0.459291011095047):
					if(x_velocity > -0.138141967356205):
						if(angle_velocity <= -0.6161576211452484):
							if(left_leg_contact != True):
								return True
						else:
							if(angle_velocity <= 0.38545961678028107):
								if(angle <= -0.3233342170715332):
									if(angle_velocity <= -0.25130046159029007):
										return True
			else:
				if(x_velocity <= -0.29952582716941833):
					if(angle <= -0.0669122189283371):
						if(angle_velocity <= -0.31141039729118347):
							if(x_velocity > -0.6054616570472717):
								if(y_velocity <= -0.1259635053575039):
									return True
								else:
									if(lander_y <= 1.459312617778778):
										return True
						else:
							return True
				else:
					if(x_velocity <= 0.2370886579155922):
						if(angle <= -0.00334473280236125):
							if(y_velocity <= -0.1187281422317028):
								if(lander_x <= -0.008284378331154585):
									return True
							else:
								if(angle <= -0.02227552980184555):
									if(angle_velocity <= -0.0828390121459961):
										if(y_velocity <= -0.11646486073732376):
											if(x_velocity > -0.23474515974521637):
												return True
										else:
											if(lander_y <= 1.4232779741287231):
												if(lander_y > 1.4201720356941223):
													if(angle_velocity > -0.1772889941930771):
														return True
											else:
												if(angle <= -0.15128538757562637):
													if(lander_x > -0.062276314944028854):
														return True
								else:
									if(x_velocity > -0.24020950496196747):
										if(y_velocity <= -0.07852547243237495):
											if(angle_velocity <= -0.04063395503908396):
												return True
										else:
											if(lander_x > 0.005284500075504184):
												if(y_velocity <= 0.27142174541950226):
													if(angle_velocity <= 0.02164728008210659):
														if(x_velocity <= 0.16837178170681):
															if(y_velocity <= 0.15363261103630066):
																if(angle_velocity <= 0.007625528844073415):
																	return True
															else:
																if(angle <= -0.01668528001755476):
																	return True
														else:
															return True
													else:
														if(lander_y > 1.4907854795455933):
															if(x_velocity > 0.123173076659441):
																return True
						else:
							if(x_velocity > -0.12136666104197502):
								if(y_velocity <= -0.03921147249639034):
									if(angle_velocity <= 0.17280402034521103):
										if(x_velocity <= 0.19898531585931778):
											if(angle_velocity <= 0.13633114844560623):
												if(lander_y > 1.404726803302765):
													if(x_velocity <= 0.11053816229104996):
														if(angle_velocity <= 0.02529743779450655):
															return True
													else:
														return True
											else:
												if(lander_x <= 0.015069055370986462):
													return True
										else:
											return True
									else:
										if(x_velocity > 0.22994697093963623):
											return True
								else:
									if(lander_x > 0.0017909050220623612):
										if(angle_velocity <= 0.10761477425694466):
											if(y_velocity <= 0.18568943440914154):
												if(angle_velocity <= 0.06498461216688156):
													return True
												else:
													if(angle <= 0.0021552671678364277):
														if(lander_x > 0.024590635672211647):
															return True
													else:
														if(y_velocity <= 0.10900164768099785):
															return True
														else:
															if(angle > 0.009164376650005579):
																return True
										else:
											if(angle_velocity <= 0.19915063679218292):
												if(lander_y <= 1.4240711331367493):
													return True
												else:
													if(lander_x <= 0.0422650333493948):
														if(angle_velocity <= 0.14905401319265366):
															if(angle <= 0.02732013911008835):
																if(lander_x <= 0.020147276110947132):
																	if(angle_velocity <= 0.12353972345590591):
																		if(angle > 0.010281411465257406):
																			return True
															else:
																return True
														else:
															if(angle_velocity > 0.17684370279312134):
																if(angle > 0.04242449067533016):
																	return True
													else:
														return True
					else:
						if(x_velocity <= 0.46994757652282715):
							if(lander_y <= 1.4616153836250305):
								if(y_velocity <= 0.2778199464082718):
									if(lander_x <= 0.06875791400671005):
										return True
									else:
										if(angle_velocity <= 0.3267119824886322):
											return True
								else:
									if(x_velocity <= 0.3102336823940277):
										if(y_velocity <= 0.351259708404541):
											if(y_velocity > 0.31201910972595215):
												return True
									else:
										return True
							else:
								if(y_velocity <= -0.01241840049624443):
									if(angle_velocity <= 0.1952170878648758):
										return True
								else:
									if(angle_velocity <= 0.1323314756155014):
										if(y_velocity <= 0.3109956532716751):
											return True
									else:
										if(lander_x <= 0.09310021251440048):
											if(angle_velocity <= 0.16254669427871704):
												if(x_velocity <= 0.2891625463962555):
													return True
						else:
							if(angle_velocity <= 0.48394937813282013):
								return True
							else:
								if(x_velocity > 0.5864104330539703):
									return True
		else:
			if(angle_velocity > -0.0002966387401102111):
				if(lander_y > -0.04202711209654808):
					if(left_leg_contact != True):
						if(angle <= 0.20635519921779633):
							if(angle <= 0.19654808193445206):
								if(x_velocity > 0.582934558391571):
									return True
							else:
								return True
						else:
							if(x_velocity <= 0.6184144616127014):
								if(lander_y > 1.5055248737335205):
									if(angle_velocity <= 0.35301069915294647):
										if(x_velocity > 0.49113956093788147):
											return True
	return False

def weShould_main_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.13108108192682266):
		if(y_velocity <= -0.22433070093393326):
			if(angle_velocity <= -0.033176204189658165):
				if(lander_y <= 1.3444701433181763):
					if(y_velocity <= -0.273845911026001):
						if(angle <= 0.024799825623631477):
							if(angle_velocity <= -0.059247663244605064):
								if(y_velocity <= -0.2988070696592331):
									if(angle_velocity <= -0.37396079301834106):
										if(lander_y <= 1.3258112668991089):
											if(y_velocity <= -0.5854084193706512):
												return True
											else:
												if(angle_velocity > -0.44097302854061127):
													if(lander_y <= 1.3106675744056702):
														if(lander_x <= 0.1759875789284706):
															if(y_velocity <= -0.4950762987136841):
																if(angle > -0.2834938168525696):
																	if(lander_y <= 1.2984379529953003):
																		return True
														else:
															return True
													else:
														return True
									else:
										if(angle <= -0.17935995012521744):
											if(y_velocity <= -0.4330245852470398):
												if(angle_velocity <= -0.19668453186750412):
													if(angle <= -0.20540592074394226):
														if(y_velocity <= -0.5109458863735199):
															if(angle <= -0.313695952296257):
																if(x_velocity <= -0.6070241034030914):
																	if(angle_velocity <= -0.2956071197986603):
																		if(x_velocity <= -0.6256603896617889):
																			if(lander_x > -0.19057030230760574):
																				return True
																	else:
																		return True
																else:
																	if(lander_y <= 1.0964854955673218):
																		if(x_velocity <= -0.5373500883579254):
																			return True
																		else:
																			if(angle > -0.3279412090778351):
																				return True
																	else:
																		if(lander_x <= -0.2093058079481125):
																			if(x_velocity <= -0.5842687487602234):
																				return True
															else:
																if(x_velocity <= -0.4836074560880661):
																	if(lander_y <= 1.1334953904151917):
																		if(y_velocity <= -0.5321527123451233):
																			return True
																	else:
																		return True
																else:
																	if(lander_x <= -0.14405455440282822):
																		return True
														else:
															if(x_velocity > -0.5982315242290497):
																if(angle > -0.2599492073059082):
																	if(y_velocity <= -0.47442156076431274):
																		if(y_velocity <= -0.48567211627960205):
																			if(x_velocity <= -0.5408328175544739):
																				return True
																		else:
																			return True
													else:
														if(angle <= -0.18944034725427628):
															return True
												else:
													if(angle <= -0.23576706647872925):
														if(x_velocity <= -0.5415813624858856):
															if(angle <= -0.4017997086048126):
																if(angle_velocity <= -0.14701531827449799):
																	if(x_velocity <= -0.5794510841369629):
																		return True
																else:
																	if(angle <= -0.47650036215782166):
																		if(y_velocity <= -0.591996043920517):
																			return True
																	else:
																		return True
															else:
																return True
														else:
															if(lander_x <= -0.2238810509443283):
																if(y_velocity <= -0.5997353196144104):
																	if(lander_x > -0.24918199330568314):
																		return True
															else:
																if(angle_velocity <= -0.11672377586364746):
																	if(angle_velocity <= -0.16923823952674866):
																		if(y_velocity <= -0.4514021724462509):
																			if(x_velocity <= -0.4411177337169647):
																				return True
																			else:
																				if(lander_x > -0.12251529842615128):
																					return True
																	else:
																		if(y_velocity <= -0.5715382993221283):
																			return True
																		else:
																			if(angle <= -0.2806345522403717):
																				if(x_velocity <= -0.5356830954551697):
																					return True
																			else:
																				if(y_velocity <= -0.4643421918153763):
																					if(angle <= -0.2704138904809952):
																						if(lander_x <= -0.13970622420310974):
																							return True
																					else:
																						return True
																else:
																	if(y_velocity <= -0.5278385281562805):
																		if(x_velocity <= -0.40742215514183044):
																			return True
																	else:
																		if(angle <= -0.29466553032398224):
																			if(x_velocity <= -0.4519476890563965):
																				if(angle_velocity > -0.08787873014807701):
																					return True
																			else:
																				if(angle_velocity <= -0.08251367881894112):
																					if(angle > -0.3342030197381973):
																						return True
																		else:
																			if(angle_velocity <= -0.09223894774913788):
																				if(x_velocity <= -0.431535080075264):
																					return True
																				else:
																					if(lander_y <= 1.120452105998993):
																						if(x_velocity <= -0.34248849749565125):
																							return True
																			else:
																				return True
													else:
														if(x_velocity <= -0.3409680724143982):
															if(angle_velocity <= -0.18334412574768066):
																if(y_velocity > -0.4420445114374161):
																	return True
															else:
																if(lander_y <= 0.5386775732040405):
																	if(x_velocity <= -0.3683338314294815):
																		return True
																else:
																	return True
														else:
															if(lander_y > 1.2742559313774109):
																return True
											else:
												if(y_velocity <= -0.4094104766845703):
													if(x_velocity <= -0.3373663127422333):
														if(angle_velocity <= -0.13404980301856995):
															if(lander_x <= -0.13412489742040634):
																if(lander_y > 1.0713378190994263):
																	return True
														else:
															if(angle > -0.22553379833698273):
																if(angle_velocity <= -0.06849892809987068):
																	return True
										else:
											if(y_velocity <= -0.4337708652019501):
												if(lander_y <= 1.29323410987854):
													if(x_velocity <= -0.43729841709136963):
														if(y_velocity <= -0.5011577010154724):
															if(angle_velocity <= -0.08882353827357292):
																if(lander_x <= -0.05888814851641655):
																	if(x_velocity <= -0.6063183546066284):
																		if(x_velocity <= -0.6112581491470337):
																			return True
																	else:
																		return True
																else:
																	if(lander_x > -0.053932713344693184):
																		return True
														else:
															if(angle_velocity <= -0.23740269988775253):
																if(x_velocity <= -0.521897166967392):
																	if(angle > -0.1680200695991516):
																		if(y_velocity > -0.4903692156076431):
																			return True
																else:
																	return True
															else:
																if(lander_y <= 1.1536120176315308):
																	if(angle > -0.05422508344054222):
																		return True
													else:
														return True
												else:
													if(x_velocity <= -0.5180715620517731):
														if(y_velocity <= -0.5468528866767883):
															if(y_velocity > -0.5587777495384216):
																return True
													else:
														if(angle_velocity <= -0.21660000085830688):
															if(lander_y <= 1.3219497203826904):
																if(lander_y > 1.299863576889038):
																	return True
														else:
															return True
											else:
												if(angle <= -0.00803579343482852):
													if(y_velocity <= -0.36119943857192993):
														if(lander_x <= -0.048978567123413086):
															if(angle_velocity <= -0.18610703945159912):
																if(angle <= -0.07978971302509308):
																	if(x_velocity <= -0.3541252464056015):
																		if(angle_velocity <= -0.22655729949474335):
																			if(y_velocity <= -0.4039473682641983):
																				if(angle_velocity <= -0.2346111163496971):
																					if(angle <= -0.11017873510718346):
																						if(angle_velocity > -0.2751312702894211):
																							if(angle_velocity <= -0.2598416358232498):
																								return True
																		else:
																			if(x_velocity > -0.3892449885606766):
																				return True
																	else:
																		if(lander_y <= 1.3376284837722778):
																			if(angle <= -0.08771895989775658):
																				if(lander_y > 1.3183715343475342):
																					if(lander_y <= 1.3271225690841675):
																						return True
																		else:
																			return True
																else:
																	if(x_velocity > -0.3651866614818573):
																		return True
															else:
																if(y_velocity <= -0.4065731167793274):
																	if(y_velocity <= -0.4108072370290756):
																		return True
																	else:
																		if(lander_y <= 1.2151699662208557):
																			return True
																else:
																	if(angle <= -0.12085811421275139):
																		if(y_velocity <= -0.36271941661834717):
																			if(x_velocity > -0.3558248430490494):
																				if(angle_velocity > -0.09198614582419395):
																					if(x_velocity <= -0.26327161490917206):
																						return True
																	else:
																		if(x_velocity <= -0.22532016038894653):
																			if(lander_x <= -0.05470695346593857):
																				return True
														else:
															if(x_velocity <= -0.36446189880371094):
																if(lander_y > 0.6396991312503815):
																	if(x_velocity <= -0.3678661584854126):
																		return True
															else:
																if(angle <= -0.013763591181486845):
																	if(lander_y <= 1.3147606253623962):
																		if(angle <= -0.025734934955835342):
																			if(x_velocity <= -0.34728533029556274):
																				if(y_velocity <= -0.3774220198392868):
																					return True
																			else:
																				if(x_velocity <= -0.19715038686990738):
																					return True
																				else:
																					if(lander_x > -0.034735774621367455):
																						return True
																		else:
																			if(x_velocity <= -0.24336615204811096):
																				return True
																	else:
																		if(y_velocity <= -0.4041459262371063):
																			return True
													else:
														if(angle_velocity <= -0.06438378989696503):
															if(lander_x <= 0.14272303879261017):
																if(angle_velocity <= -0.08884239196777344):
																	if(lander_y <= 1.210818886756897):
																		if(x_velocity > -0.1250804290175438):
																			if(x_velocity <= -0.12362043559551239):
																				return True
																else:
																	if(y_velocity <= -0.3359816372394562):
																		if(x_velocity > -0.19562559574842453):
																			if(lander_x > -0.032077884301543236):
																				return True
																	else:
																		if(lander_x <= 0.13328395038843155):
																			if(y_velocity <= -0.30143213272094727):
																				if(lander_y <= 1.1246248483657837):
																					if(angle <= -0.014325159136205912):
																						if(angle_velocity > -0.07771759107708931):
																							if(x_velocity <= -0.12454863637685776):
																								if(x_velocity > -0.1958720162510872):
																									return True
																							else:
																								if(x_velocity > -0.08081450685858727):
																									if(angle_velocity > -0.07152122259140015):
																										return True
																					else:
																						return True
																			else:
																				if(angle <= -0.039074202068150043):
																					return True
																		else:
																			return True
															else:
																if(lander_y <= 0.7706000208854675):
																	if(x_velocity <= -0.2208804190158844):
																		if(y_velocity <= -0.337039589881897):
																			return True
																		else:
																			if(lander_y <= 0.48573848605155945):
																				if(angle > -0.12391063198447227):
																					if(lander_x > 0.17291436344385147):
																						return True
																	else:
																		if(x_velocity <= -0.18279066681861877):
																			return True
																else:
																	if(y_velocity <= -0.3521493077278137):
																		if(lander_x > 0.19722943007946014):
																			return True
																	else:
																		if(lander_x <= 0.2635515630245209):
																			if(x_velocity > -0.13918402791023254):
																				return True
																		else:
																			if(angle_velocity <= -0.14140108972787857):
																				return True
														else:
															if(angle <= -0.05002631992101669):
																if(angle_velocity > -0.0614648275077343):
																	if(angle <= -0.10693388804793358):
																		return True
															else:
																return True
												else:
													if(y_velocity <= -0.32478559017181396):
														if(lander_x > -0.03480634745210409):
															return True
													else:
														if(angle_velocity <= -0.08423697203397751):
															if(x_velocity <= -0.10184061527252197):
																if(angle_velocity > -0.19225498288869858):
																	if(angle > 0.0030389951425604522):
																		if(y_velocity <= -0.301647886633873):
																			return True
																		else:
																			if(angle_velocity > -0.12690065801143646):
																				return True
														else:
															if(angle_velocity <= -0.06011812388896942):
																if(angle_velocity <= -0.06475789099931717):
																	return True
																else:
																	if(angle_velocity > -0.06261859461665154):
																		return True
								else:
									if(lander_y <= 0.7050610482692719):
										if(angle <= -0.016425722744315863):
											if(y_velocity <= -0.2863665968179703):
												if(angle_velocity > -0.08904643729329109):
													if(lander_y <= 0.6451204121112823):
														if(angle <= -0.037636296823620796):
															if(lander_y <= 0.43963347375392914):
																return True
														else:
															return True
											else:
												if(lander_x <= -0.20630282908678055):
													return True
										else:
											if(y_velocity <= -0.27654169499874115):
												if(angle_velocity <= -0.06510399654507637):
													if(y_velocity > -0.2940068542957306):
														if(angle_velocity <= -0.08824694529175758):
															if(lander_y <= 0.6597811579704285):
																return True
														else:
															return True
									else:
										if(angle <= 0.004968515830114484):
											if(lander_y <= 1.1829760670661926):
												if(lander_y > 0.9118808507919312):
													if(lander_y <= 0.926120936870575):
														return True
										else:
											if(angle_velocity > -0.08426381647586823):
												if(x_velocity <= -0.058141548186540604):
													if(lander_y <= 1.0551754832267761):
														if(lander_x <= 0.1210385337471962):
															if(angle_velocity > -0.0816766582429409):
																return True
														else:
															if(x_velocity <= -0.10559209063649178):
																return True
												else:
													if(y_velocity <= -0.2911544591188431):
														return True
							else:
								if(lander_y <= 0.8993513584136963):
									if(angle <= -0.03608830086886883):
										if(y_velocity <= -0.28350360691547394):
											if(lander_y <= 0.7270106077194214):
												if(angle_velocity > -0.05718567967414856):
													if(angle_velocity <= -0.033221347257494926):
														if(x_velocity <= -0.020858132280409336):
															if(angle <= -0.10625071451067924):
																if(y_velocity <= -0.33073922991752625):
																	if(lander_x > 0.08706545829772949):
																		return True
															else:
																if(y_velocity <= -0.2871044874191284):
																	if(angle_velocity <= -0.04851607233285904):
																		if(angle_velocity <= -0.04945286735892296):
																			return True
																	else:
																		return True
																else:
																	if(lander_y <= 0.6390789747238159):
																		if(angle_velocity <= -0.044836126267910004):
																			if(angle_velocity <= -0.04730966500937939):
																				return True
																		else:
																			return True
											else:
												if(y_velocity <= -0.3133092075586319):
													if(angle > -0.09916141256690025):
														if(angle_velocity <= -0.04292111285030842):
															return True
														else:
															if(y_velocity <= -0.3179745227098465):
																if(y_velocity > -0.34161847829818726):
																	return True
												else:
													if(y_velocity <= -0.28776492178440094):
														if(angle_velocity <= -0.03477237932384014):
															if(angle_velocity <= -0.05153496190905571):
																if(x_velocity <= -0.15227125585079193):
																	return True
															else:
																if(angle > -0.0412223432213068):
																	if(angle <= -0.039473528042435646):
																		return True
														else:
															return True
										else:
											if(lander_y <= 0.469486266374588):
												if(angle_velocity <= -0.04586024023592472):
													if(x_velocity > -0.06577751412987709):
														return True
												else:
													return True
											else:
												if(y_velocity <= -0.2753429412841797):
													if(angle > -0.04135387763381004):
														if(angle_velocity > -0.04640534892678261):
															return True
									else:
										if(y_velocity <= -0.2771090269088745):
											if(y_velocity <= -0.28404779732227325):
												if(x_velocity > -0.14623917639255524):
													if(lander_y <= 0.8852115869522095):
														if(angle <= -0.03160950541496277):
															if(angle <= -0.03189449943602085):
																if(angle <= -0.03372976556420326):
																	if(lander_y <= 0.6550625860691071):
																		return True
																else:
																	return True
														else:
															if(lander_x <= 0.16130437701940536):
																if(angle_velocity <= -0.05151553079485893):
																	if(angle_velocity <= -0.05165383778512478):
																		return True
																else:
																	return True
															else:
																if(lander_y <= 0.748996376991272):
																	return True
													else:
														if(angle > -0.021644615568220615):
															if(lander_y > 0.8878841400146484):
																return True
											else:
												if(lander_y <= 0.6336986422538757):
													if(angle <= -0.0298122838139534):
														if(x_velocity <= -0.07587196305394173):
															return True
														else:
															if(y_velocity > -0.27869923412799835):
																return True
													else:
														return True
												else:
													if(angle <= -0.002378964680247009):
														if(lander_x <= 0.04290165938436985):
															if(y_velocity > -0.2811284810304642):
																return True
													else:
														return True
										else:
											if(lander_y <= 0.5317091047763824):
												return True
											else:
												if(x_velocity <= -0.07187707349658012):
													if(x_velocity > -0.10545333102345467):
														return True
												else:
													if(y_velocity > -0.2747925966978073):
														if(lander_y <= 0.7707552313804626):
															return True
								else:
									if(y_velocity <= -0.29669009149074554):
										if(lander_x <= -0.003475999808870256):
											if(y_velocity <= -0.342788428068161):
												if(lander_x <= -0.07627568393945694):
													if(y_velocity <= -0.4099150002002716):
														if(angle_velocity > -0.05680711194872856):
															if(lander_x <= -0.2660738676786423):
																if(x_velocity <= -0.6355670988559723):
																	return True
															else:
																if(x_velocity <= -0.48067183792591095):
																	return True
																else:
																	if(lander_x <= -0.19408683478832245):
																		if(angle_velocity <= -0.03933914750814438):
																			if(lander_x > -0.23800327628850937):
																				return True
																	else:
																		if(lander_y <= 1.1852357387542725):
																			if(angle <= -0.30683842301368713):
																				if(x_velocity <= -0.3961202949285507):
																					return True
																			else:
																				return True
																		else:
																			if(angle_velocity <= -0.0436124037951231):
																				if(angle_velocity > -0.05217815563082695):
																					return True
													else:
														if(x_velocity > -0.33552083373069763):
															if(y_velocity > -0.37997524440288544):
																if(y_velocity <= -0.367921844124794):
																	return True
												else:
													if(angle_velocity <= -0.04700538143515587):
														if(y_velocity <= -0.37741243839263916):
															if(lander_x <= -0.031278944574296474):
																return True
														else:
															if(lander_x > -0.04243931919336319):
																if(y_velocity <= -0.3486199826002121):
																	return True
													else:
														return True
											else:
												if(lander_x <= -0.03591289557516575):
													if(angle_velocity > -0.036549970507621765):
														if(y_velocity <= -0.312905415892601):
															return True
												else:
													if(y_velocity <= -0.32739101350307465):
														if(lander_x > -0.024667883291840553):
															return True
													else:
														if(x_velocity <= -0.08919725939631462):
															if(y_velocity <= -0.31665223836898804):
																return True
														else:
															if(lander_y <= 1.0605363249778748):
																return True
															else:
																if(lander_y > 1.31239652633667):
																	if(x_velocity <= -0.051038533449172974):
																		return True
										else:
											if(y_velocity <= -0.3068675696849823):
												if(angle <= -0.05213010683655739):
													if(x_velocity <= -0.16359515488147736):
														return True
												else:
													return True
											else:
												if(angle_velocity <= -0.05088780261576176):
													return True
												else:
													if(lander_x <= 0.21108727902173996):
														if(lander_y <= 1.096395194530487):
															if(angle > 0.008978136640507728):
																return True
													else:
														if(lander_x <= 0.2387922778725624):
															return True
									else:
										if(x_velocity <= -0.06396332010626793):
											if(x_velocity > -0.09581229835748672):
												if(angle <= 0.005803724052384496):
													if(x_velocity > -0.08584951609373093):
														if(y_velocity <= -0.2916957288980484):
															if(angle > -0.002429311629384756):
																return True
												else:
													if(lander_y <= 0.976494312286377):
														return True
										else:
											if(angle > 0.015422617085278034):
												if(y_velocity <= -0.2848079204559326):
													return True
												else:
													if(y_velocity > -0.2767981141805649):
														return True
						else:
							if(angle <= 0.23191983997821808):
								if(angle_velocity <= -0.05972559005022049):
									if(angle <= 0.0912783332169056):
										if(y_velocity <= -0.28658297657966614):
											if(lander_x <= 0.039663076400756836):
												if(y_velocity <= -0.3101351112127304):
													return True
												else:
													if(angle <= 0.027676471509039402):
														return True
													else:
														if(angle > 0.0576394647359848):
															if(angle_velocity <= -0.07374140247702599):
																return True
											else:
												if(angle_velocity <= -0.10369608923792839):
													if(lander_y <= 1.1294952034950256):
														if(angle_velocity <= -0.36916184425354004):
															if(angle > 0.06587366387248039):
																if(angle_velocity > -0.47625304758548737):
																	return True
														else:
															if(lander_x > 0.06910424306988716):
																return True
													else:
														if(y_velocity <= -0.30115795135498047):
															if(lander_y <= 1.1519516706466675):
																if(y_velocity <= -0.36087512969970703):
																	return True
															else:
																return True
												else:
													if(angle_velocity <= -0.0598941296339035):
														if(angle <= 0.05225302837789059):
															if(angle_velocity > -0.0939495638012886):
																if(x_velocity <= -0.030840015038847923):
																	if(lander_y <= 1.2010349035263062):
																		if(angle <= 0.02745828777551651):
																			if(y_velocity <= -0.3056199252605438):
																				return True
																		else:
																			if(angle_velocity <= -0.09268640726804733):
																				if(lander_x <= 0.1837688460946083):
																					return True
																			else:
																				return True
																else:
																	if(lander_y <= 0.9904069006443024):
																		return True
														else:
															return True
										else:
											if(x_velocity <= -0.0033900575945153832):
												if(angle <= 0.05077522248029709):
													if(lander_y <= 0.8034813106060028):
														if(y_velocity <= -0.27736397087574005):
															return True
													else:
														if(lander_x > 0.042511845007538795):
															if(angle > 0.026534578762948513):
																if(x_velocity <= -0.048390813171863556):
																	if(lander_y <= 0.998577892780304):
																		return True
												else:
													if(angle_velocity <= -0.09065785631537437):
														if(lander_y <= 0.9230482876300812):
															if(angle_velocity > -0.35589443147182465):
																return True
													else:
														return True
											else:
												if(y_velocity > -0.2744954973459244):
													return True
									else:
										if(lander_x <= 0.2587932199239731):
											if(lander_x > 0.05486712232232094):
												if(x_velocity <= -0.3030150681734085):
													if(y_velocity > -0.31355656683444977):
														return True
												else:
													if(x_velocity <= -0.1765737608075142):
														if(x_velocity <= -0.18656593561172485):
															if(angle > 0.11395077407360077):
																return True
													else:
														return True
										else:
											if(lander_y <= 1.2129668593406677):
												if(y_velocity <= -0.32512956857681274):
													if(lander_y > 1.168076753616333):
														return True
											else:
												if(x_velocity <= 0.047188255935907364):
													if(y_velocity <= -0.2758232653141022):
														return True
													else:
														if(x_velocity > -0.04902367852628231):
															return True
								else:
									if(lander_x <= 0.037775563076138496):
										if(y_velocity <= -0.29584261775016785):
											return True
										else:
											if(angle_velocity > -0.05103209242224693):
												if(y_velocity <= -0.27884821593761444):
													if(y_velocity > -0.28947247564792633):
														return True
									else:
										if(x_velocity <= -0.073564313352108):
											if(lander_x > 0.11718139797449112):
												return True
										else:
											if(lander_x <= 0.07187323644757271):
												if(lander_x <= 0.07159404829144478):
													if(x_velocity <= -0.05135893262922764):
														if(angle_velocity <= -0.048243479803204536):
															return True
													else:
														if(angle <= 0.029172008857131004):
															if(angle <= 0.029036596417427063):
																return True
														else:
															return True
											else:
												return True
							else:
								if(y_velocity <= -0.33794403076171875):
									if(x_velocity <= -0.21052471548318863):
										if(lander_x <= 0.22968025505542755):
											return True
									else:
										return True
								else:
									if(x_velocity <= -0.14011316746473312):
										if(lander_y <= 0.6879697442054749):
											if(y_velocity <= -0.3158489018678665):
												return True
									else:
										if(angle <= 0.45971862971782684):
											if(angle_velocity <= -0.24738627672195435):
												return True
											else:
												if(x_velocity <= -0.009210229036398232):
													if(y_velocity <= -0.31540529429912567):
														return True
													else:
														if(y_velocity <= -0.30606696009635925):
															if(angle <= 0.4194222539663315):
																return True
												else:
													return True
										else:
											if(x_velocity <= 0.032838575541973114):
												if(lander_y <= 0.7740776836872101):
													if(y_velocity <= -0.31369757652282715):
														return True
													else:
														if(angle_velocity > -0.06954314932227135):
															return True
											else:
												if(y_velocity <= -0.28642818331718445):
													return True
												else:
													if(x_velocity > 0.09212664887309074):
														return True
					else:
						if(angle <= 0.034930093213915825):
							if(lander_y <= 0.5064136981964111):
								if(angle_velocity <= -0.06040847301483154):
									if(y_velocity <= -0.2535327672958374):
										if(angle <= -0.05017863027751446):
											if(x_velocity <= -0.13901380449533463):
												return True
										else:
											if(lander_x <= -0.011474322993308306):
												if(lander_y <= 0.305573508143425):
													return True
												else:
													if(angle_velocity > -0.08623545616865158):
														if(lander_y > 0.32553939521312714):
															if(angle_velocity <= -0.06177215836942196):
																if(angle_velocity <= -0.07961239293217659):
																	if(x_velocity <= -0.03432629816234112):
																		return True
																else:
																	return True
											else:
												if(lander_y <= 0.15798208117485046):
													return True
									else:
										if(angle <= 0.019497358240187168):
											if(lander_y <= 0.151559479534626):
												if(angle <= -0.01771371066570282):
													if(angle_velocity <= -0.06213214062154293):
														if(y_velocity <= -0.2358163446187973):
															if(angle > -0.049251850694417953):
																if(lander_y <= 0.1297844871878624):
																	return True
													else:
														return True
												else:
													if(angle_velocity > -0.0768754780292511):
														if(y_velocity <= -0.22891531884670258):
															return True
											else:
												if(angle <= -0.0032971256878226995):
													if(lander_x <= 0.09063887596130371):
														if(angle > -0.012972843833267689):
															if(angle <= -0.012694571167230606):
																return True
													else:
														if(lander_y <= 0.2776852548122406):
															return True
												else:
													if(y_velocity <= -0.2518458515405655):
														if(x_velocity > -0.03732426092028618):
															return True
													else:
														if(angle <= -0.0022858771844767034):
															return True
														else:
															if(angle_velocity > -0.06998409330844879):
																if(angle_velocity <= -0.06887462735176086):
																	return True
																else:
																	if(lander_y <= 0.3043612092733383):
																		return True
										else:
											if(y_velocity <= -0.22808357328176498):
												return True
								else:
									if(y_velocity <= -0.2400168478488922):
										if(angle <= -0.026978999376296997):
											if(lander_y <= 0.30345430970191956):
												if(y_velocity <= -0.25478316843509674):
													if(angle <= -0.05877453275024891):
														if(lander_y <= 0.1870751455426216):
															if(angle > -0.09331268817186356):
																return True
													else:
														if(lander_y <= 0.300640270113945):
															return True
														else:
															if(angle_velocity > -0.045744482427835464):
																return True
												else:
													if(angle <= -0.04732763580977917):
														if(x_velocity <= -0.09919827803969383):
															return True
													else:
														if(lander_y <= 0.21261925250291824):
															if(angle_velocity <= -0.05174741521477699):
																if(x_velocity <= -0.05522949621081352):
																	return True
															else:
																if(lander_x > -0.23906293511390686):
																	if(lander_y > 0.008540538605302572):
																		return True
														else:
															if(lander_x <= -0.16728148609399796):
																return True
															else:
																if(x_velocity <= -0.04996753856539726):
																	if(lander_x <= 0.018435811973176897):
																		return True
											else:
												if(y_velocity <= -0.26821960508823395):
													if(angle > -0.04693380370736122):
														return True
												else:
													if(angle_velocity <= -0.03502657637000084):
														if(lander_x <= -0.06985316053032875):
															if(x_velocity <= -0.019727726466953754):
																if(y_velocity <= -0.24895920604467392):
																	return True
										else:
											if(lander_y <= 0.3868850916624069):
												if(y_velocity <= -0.24550068378448486):
													if(angle <= -0.024723769165575504):
														if(angle <= -0.025082661770284176):
															return True
													else:
														if(angle_velocity <= -0.054817020893096924):
															if(angle_velocity <= -0.055450962856411934):
																return True
														else:
															return True
												else:
													if(angle <= -0.012742995750159025):
														if(lander_y <= 0.2760889083147049):
															return True
													else:
														if(y_velocity <= -0.24428729712963104):
															if(y_velocity <= -0.24458645284175873):
																return True
														else:
															return True
											else:
												if(lander_x <= 0.0450282096862793):
													if(y_velocity <= -0.24334080517292023):
														if(angle <= -0.01838515792042017):
															if(angle_velocity <= -0.04829507879912853):
																return True
															else:
																if(lander_x > 0.03531451150774956):
																	return True
														else:
															if(x_velocity <= 0.05778321996331215):
																if(x_velocity <= -0.011092393659055233):
																	return True
																else:
																	if(x_velocity > -0.00418945134151727):
																		if(lander_y <= 0.48397214710712433):
																			if(lander_y <= 0.4557829946279526):
																				if(lander_y <= 0.4191170185804367):
																					return True
																				else:
																					if(angle_velocity <= -0.042285582050681114):
																						return True
																			else:
																				return True
																		else:
																			if(angle_velocity > -0.05122653767466545):
																				return True
													else:
														if(angle > 0.009552558418363333):
															return True
												else:
													if(x_velocity <= -0.0911533460021019):
														if(y_velocity <= -0.2479846179485321):
															return True
													else:
														if(y_velocity <= -0.2600053548812866):
															if(angle_velocity > -0.04805313982069492):
																return True
									else:
										if(lander_y <= 0.19187165051698685):
											if(angle <= -0.020316937007009983):
												if(x_velocity <= -0.029020866379141808):
													if(y_velocity <= -0.23269294202327728):
														if(angle <= -0.045829424634575844):
															if(y_velocity > -0.23651983588933945):
																if(angle <= -0.06055501289665699):
																	return True
														else:
															if(lander_x <= 0.057770490646362305):
																return True
													else:
														if(y_velocity <= -0.2259705513715744):
															if(lander_y <= 0.011627081548795104):
																return True
														else:
															return True
												else:
													if(lander_y <= 0.01037331029510824):
														return True
											else:
												if(lander_x <= -0.20268094539642334):
													if(lander_y > 0.17623337358236313):
														return True
												else:
													if(lander_x <= 0.04868140257894993):
														if(lander_y <= 0.15951377153396606):
															return True
														else:
															if(lander_y > 0.16665298491716385):
																return True
													else:
														if(angle > -0.00803783256560564):
															return True
										else:
											if(angle <= 0.008964150212705135):
												if(lander_y <= 0.295793741941452):
													if(angle > -0.031182220205664635):
														if(y_velocity <= -0.2264702022075653):
															if(y_velocity <= -0.22923804819583893):
																if(x_velocity <= -0.021200704388320446):
																	if(angle <= -0.011414513923227787):
																		if(lander_x <= -0.023135279770940542):
																			if(lander_y <= 0.2618270516395569):
																				return True
																		else:
																			if(lander_x > 0.07161402702331543):
																				if(y_velocity <= -0.23272212594747543):
																					return True
																	else:
																		return True
																else:
																	if(angle <= 0.002715824404731393):
																		if(angle_velocity > -0.038494376465678215):
																			if(y_velocity > -0.23635271936655045):
																				return True
																	else:
																		return True
															else:
																if(lander_x <= -0.08069820515811443):
																	return True
												else:
													if(lander_y <= 0.4847024381160736):
														if(y_velocity <= -0.22604333609342575):
															if(angle > -0.047422030940651894):
																if(angle_velocity <= -0.03338231146335602):
																	if(lander_y > 0.2988537400960922):
																		if(y_velocity <= -0.2378656566143036):
																			if(lander_y <= 0.3742271065711975):
																				if(lander_y > 0.3361288011074066):
																					if(lander_x > -0.208277128636837):
																						return True
											else:
												if(lander_y <= 0.39980554580688477):
													if(angle_velocity <= -0.0341972541064024):
														if(angle_velocity <= -0.05086044780910015):
															if(angle <= 0.014690518844872713):
																return True
														else:
															return True
												else:
													if(lander_y > 0.42888352274894714):
														if(angle > 0.015268184244632721):
															if(lander_x <= -0.17105422168970108):
																return True
															else:
																if(angle <= 0.019403917714953423):
																	return True
							else:
								if(angle_velocity <= -0.05284256301820278):
									if(x_velocity <= -0.10827244073152542):
										if(y_velocity <= -0.26872535049915314):
											if(angle > -0.0041271538939327):
												return True
									else:
										if(angle <= -0.00010752363596111536):
											if(lander_x <= -0.06001458130776882):
												if(lander_x > -0.06097531318664551):
													return True
										else:
											if(x_velocity <= -0.07380442321300507):
												if(angle_velocity > -0.08547554910182953):
													if(x_velocity <= -0.0753205195069313):
														if(angle <= 0.0007209324394352734):
															if(y_velocity <= -0.26561057567596436):
																return True
													else:
														return True
											else:
												if(lander_y <= 0.7227818071842194):
													if(y_velocity <= -0.25040990114212036):
														if(angle <= 0.021464388817548752):
															if(x_velocity <= -0.053918564692139626):
																return True
															else:
																if(angle_velocity <= -0.06892808526754379):
																	if(angle_velocity > -0.07234077528119087):
																		return True
														else:
															if(x_velocity <= 0.02297267783433199):
																return True
															else:
																if(angle_velocity > -0.06391268596053123):
																	return True
													else:
														if(lander_y <= 0.5163798630237579):
															return True
														else:
															if(y_velocity <= -0.24693111330270767):
																if(angle_velocity > -0.060279881581664085):
																	return True
								else:
									if(x_velocity <= -0.03969418443739414):
										if(angle <= -0.004477277863770723):
											if(angle_velocity <= -0.04905989393591881):
												if(angle <= -0.020632019266486168):
													return True
											else:
												if(x_velocity <= -0.08537657558917999):
													if(angle_velocity > -0.03913089446723461):
														if(y_velocity <= -0.2715301811695099):
															if(x_velocity <= -0.10004038363695145):
																return True
												else:
													if(angle <= -0.006619237828999758):
														if(angle <= -0.0167265422642231):
															if(lander_y <= 0.5122690498828888):
																if(y_velocity <= -0.26554323732852936):
																	return True
														else:
															if(lander_x <= 0.06441674008965492):
																if(y_velocity <= -0.25397640466690063):
																	if(lander_y <= 0.7686985731124878):
																		return True
															else:
																if(angle <= -0.015261868480592966):
																	return True
										else:
											if(y_velocity <= -0.2564547210931778):
												if(x_velocity > -0.06182005628943443):
													if(angle > 0.003093022503890097):
														if(lander_y <= 0.95409095287323):
															if(angle <= 0.007898449199274182):
																if(y_velocity <= -0.2625900208950043):
																	if(lander_x <= 0.059391019865870476):
																		return True
																else:
																	return True
															else:
																return True
											else:
												if(lander_x <= 0.14655842632055283):
													if(angle <= 0.008637923747301102):
														if(x_velocity <= -0.045624028891325):
															if(lander_x <= 0.10051970183849335):
																if(lander_y > 0.6209210157394409):
																	if(y_velocity > -0.2510424256324768):
																		return True
															else:
																return True
														else:
															if(lander_y <= 0.6419882774353027):
																return True
									else:
										if(lander_y <= 0.5522063076496124):
											if(lander_y <= 0.5241343975067139):
												if(angle > 0.029883023351430893):
													return True
											else:
												if(y_velocity <= -0.23848091810941696):
													if(lander_x <= -0.025369883282110095):
														if(lander_y <= 0.548709362745285):
															return True
														else:
															if(angle > 0.01152773480862379):
																return True
													else:
														if(x_velocity <= -0.022533725015819073):
															return True
												else:
													if(x_velocity <= -0.016883855685591698):
														return True
										else:
											if(y_velocity <= -0.2282232791185379):
												if(angle <= 0.016525248996913433):
													if(angle_velocity <= -0.033497318625450134):
														if(y_velocity <= -0.23080382496118546):
															if(y_velocity <= -0.27197331190109253):
																if(y_velocity > -0.27213045954704285):
																	return True
															else:
																if(angle_velocity <= -0.034667354077100754):
																	if(angle > 0.015077714342623949):
																		if(lander_x > -0.014067841693758965):
																			return True
																else:
																	if(lander_y > 0.7341466546058655):
																		return True
												else:
													if(y_velocity <= -0.2586463689804077):
														if(lander_y <= 0.7615549564361572):
															return True
														else:
															if(lander_x <= 0.05675811693072319):
																if(x_velocity <= 0.030231313779950142):
																	return True
													else:
														if(x_velocity <= -0.03337454795837402):
															if(lander_x > 0.0971221923828125):
																return True
														else:
															if(angle_velocity <= -0.04700267128646374):
																return True
															else:
																if(angle <= 0.018388327211141586):
																	if(y_velocity <= -0.2452925369143486):
																		return True
						else:
							if(x_velocity <= 0.025186216458678246):
								if(angle_velocity <= -0.071587685495615):
									if(angle <= 0.1095874160528183):
										if(x_velocity <= -0.030848713591694832):
											if(lander_x <= 0.2282298132777214):
												if(y_velocity <= -0.2566540092229843):
													if(x_velocity <= -0.03515925072133541):
														if(lander_y <= 0.9161396026611328):
															if(lander_x <= 0.1795550361275673):
																if(angle <= 0.04489714466035366):
																	if(x_velocity <= -0.06841016933321953):
																		return True
																else:
																	return True
															else:
																if(lander_x > 0.2239033207297325):
																	return True
														else:
															if(lander_x > 0.1899833232164383):
																return True
												else:
													if(angle_velocity <= -0.19618981331586838):
														if(angle_velocity <= -0.2810531258583069):
															if(x_velocity > -0.0608994010835886):
																return True
										else:
											if(y_velocity <= -0.24221179634332657):
												if(angle > 0.07443808019161224):
													if(x_velocity <= -0.01105482317507267):
														if(y_velocity <= -0.25863175094127655):
															if(lander_y <= 1.177529513835907):
																return True
													else:
														if(y_velocity <= -0.2670303285121918):
															if(y_velocity > -0.27025872468948364):
																if(angle <= 0.0959988385438919):
																	return True
											else:
												if(lander_y <= 0.9253587424755096):
													if(angle_velocity > -0.0964064821600914):
														return True
									else:
										if(angle <= 0.2809743285179138):
											if(x_velocity > -0.11730331182479858):
												if(y_velocity <= -0.24049507081508636):
													if(lander_y <= 1.2089558243751526):
														if(angle <= 0.15761693567037582):
															if(angle_velocity <= -0.13329292088747025):
																if(y_velocity <= -0.2707895487546921):
																	return True
																else:
																	if(y_velocity <= -0.2581660896539688):
																		if(angle_velocity > -0.2602323293685913):
																			return True
															else:
																return True
														else:
															return True
													else:
														if(angle > 0.11862792074680328):
															if(lander_x > 0.2416369915008545):
																if(angle_velocity <= -0.16942324489355087):
																	if(lander_y <= 1.2879590392112732):
																		if(y_velocity > -0.25517041981220245):
																			if(y_velocity <= -0.2500557228922844):
																				return True
																	else:
																		return True
																else:
																	return True
												else:
													if(angle_velocity <= -0.2143898606300354):
														if(angle <= 0.19621512293815613):
															if(lander_x <= -0.019423335790634155):
																return True
														else:
															return True
										else:
											if(lander_y <= 0.9295924305915833):
												if(y_velocity <= -0.25443483889102936):
													return True
												else:
													if(lander_y <= 0.7515280842781067):
														return True
								else:
									if(lander_y <= 1.0452626943588257):
										if(x_velocity <= -0.020400109700858593):
											if(y_velocity <= -0.25144486129283905):
												if(lander_y <= 0.9741859138011932):
													if(angle_velocity <= -0.058106349781155586):
														if(angle_velocity <= -0.06286430172622204):
															if(lander_y > 0.8521100580692291):
																return True
													else:
														if(x_velocity > -0.04720745235681534):
															return True
												else:
													if(angle_velocity > -0.03587900660932064):
														return True
										else:
											if(lander_y <= 0.8571777045726776):
												if(lander_x <= 0.16427383571863174):
													if(x_velocity > -0.018550340086221695):
														if(y_velocity <= -0.22877222299575806):
															return True
														else:
															if(x_velocity > 0.003077297005802393):
																return True
											else:
												if(lander_y <= 0.986799955368042):
													if(angle <= 0.08642616868019104):
														if(lander_x > 0.13354911655187607):
															if(lander_x <= 0.13364215195178986):
																return True
													else:
														if(x_velocity <= 0.01179939930443652):
															return True
												else:
													if(y_velocity <= -0.2546733021736145):
														if(x_velocity <= -0.010123291984200478):
															if(lander_y <= 1.0212674140930176):
																return True
														else:
															return True
													else:
														if(angle > 0.07542070746421814):
															if(x_velocity > 0.009290582500398159):
																return True
									else:
										if(y_velocity <= -0.2708752453327179):
											if(x_velocity <= 0.016764324624091387):
												return True
										else:
											if(x_velocity > 0.013716375455260277):
												if(y_velocity <= -0.2602417767047882):
													if(lander_x > 0.04520964436233044):
														return True
							else:
								if(lander_y <= 0.5665508806705475):
									if(angle <= 0.26563510298728943):
										if(y_velocity <= -0.22618267685174942):
											return True
										else:
											if(y_velocity > -0.22588810324668884):
												return True
									else:
										if(y_velocity <= -0.24123495072126389):
											return True
								else:
									if(angle <= 0.08744543418288231):
										if(lander_y <= 0.6420569717884064):
											if(lander_y > 0.6070963740348816):
												return True
										else:
											if(y_velocity <= -0.2731200158596039):
												return True
									else:
										if(y_velocity <= -0.24430807679891586):
											if(angle <= 0.35814069211483):
												if(angle <= 0.16630902886390686):
													if(angle_velocity <= -0.07869734987616539):
														if(lander_y <= 1.1464273929595947):
															if(angle > 0.10493464395403862):
																if(angle_velocity <= -0.12545626237988472):
																	if(lander_y <= 1.1010660529136658):
																		return True
																else:
																	return True
														else:
															if(x_velocity <= 0.05530468001961708):
																if(angle_velocity <= -0.12411325797438622):
																	if(y_velocity > -0.25613246858119965):
																		return True
																else:
																	if(angle <= 0.11198022589087486):
																		if(y_velocity <= -0.2632356882095337):
																			return True
																	else:
																		if(lander_x <= 0.17672505229711533):
																			return True
															else:
																if(y_velocity <= -0.2695635259151459):
																	if(angle > 0.13553710281848907):
																		return True
																else:
																	if(lander_x <= 0.06755213811993599):
																		if(x_velocity > 0.09038050100207329):
																			return True
													else:
														if(lander_x <= 0.14297018200159073):
															if(angle <= 0.11749140173196793):
																if(x_velocity <= 0.0647285096347332):
																	if(lander_y <= 1.210197925567627):
																		if(y_velocity <= -0.24939091503620148):
																			if(angle <= 0.09439653530716896):
																				if(angle_velocity > -0.05749609135091305):
																					return True
																			else:
																				return True
																		else:
																			if(x_velocity > 0.04607129655778408):
																				return True
																	else:
																		if(lander_y > 1.2297842502593994):
																			return True
																else:
																	if(angle_velocity > -0.046996111050248146):
																		if(angle <= 0.10676972568035126):
																			return True
															else:
																if(y_velocity <= -0.24746445566415787):
																	return True
																else:
																	if(x_velocity > 0.05793793871998787):
																		return True
												else:
													if(angle_velocity > -0.2895004451274872):
														if(angle <= 0.3314230591058731):
															return True
														else:
															if(y_velocity <= -0.2498018741607666):
																return True
											else:
												if(y_velocity <= -0.26091068983078003):
													if(angle <= 0.4594730883836746):
														return True
										else:
											if(angle <= 0.18603547662496567):
												if(angle_velocity <= -0.06871051341295242):
													if(x_velocity <= 0.039872072637081146):
														if(lander_y <= 0.9838990867137909):
															if(angle > 0.12621251866221428):
																return True
													else:
														if(angle_velocity > -0.12319521978497505):
															if(angle <= 0.13856685906648636):
																if(lander_y <= 1.2852905988693237):
																	if(lander_y <= 0.9667399525642395):
																		if(x_velocity <= 0.05916708894073963):
																			return True
															else:
																if(lander_y <= 1.1982311010360718):
																	if(y_velocity <= -0.23231351375579834):
																		return True
																	else:
																		if(y_velocity > -0.226052924990654):
																			return True
																else:
																	if(x_velocity <= 0.09304017201066017):
																		if(angle_velocity <= -0.0915611982345581):
																			if(y_velocity > -0.2395741418004036):
																				return True
												else:
													if(x_velocity <= 0.0782221369445324):
														if(lander_y <= 0.9920945465564728):
															if(lander_x > 0.12876948714256287):
																return True
														else:
															if(angle > 0.1434386521577835):
																return True
													else:
														if(lander_y <= 1.2898206114768982):
															if(y_velocity <= -0.23597051948308945):
																return True
															else:
																if(angle <= 0.13227420300245285):
																	return True
														else:
															if(lander_x > 0.0880582332611084):
																if(lander_x <= 0.10917820781469345):
																	return True
											else:
												if(angle_velocity <= -0.15143311768770218):
													if(angle <= 0.2426048144698143):
														if(lander_x <= 0.12378249317407608):
															return True
													else:
														if(lander_x > 0.16154446452856064):
															if(y_velocity <= -0.22632065415382385):
																if(angle_velocity > -0.2848382294178009):
																	return True
												else:
													if(angle <= 0.3542786091566086):
														if(angle <= 0.28392522037029266):
															return True
														else:
															if(lander_x > 0.17048988118767738):
																return True
				else:
					if(x_velocity <= -0.33664602041244507):
						if(angle <= -0.11459648981690407):
							if(angle_velocity > -0.09190931171178818):
								if(y_velocity <= -0.4107735753059387):
									if(x_velocity <= -0.5631673336029053):
										if(y_velocity <= -0.5357753932476044):
											return True
									else:
										if(angle_velocity <= -0.04858700558543205):
											if(angle_velocity > -0.08055906742811203):
												if(y_velocity <= -0.5393632650375366):
													return True
										else:
											return True
					else:
						if(angle <= 0.13649334758520126):
							if(x_velocity <= -0.12586691230535507):
								if(angle <= -0.04123163782060146):
									if(angle_velocity <= -0.05977979861199856):
										if(lander_x > -0.01974854525178671):
											return True
									else:
										if(y_velocity <= -0.3848797380924225):
											if(y_velocity <= -0.4178415685892105):
												return True
											else:
												if(lander_y <= 1.3663490414619446):
													return True
										else:
											if(lander_x > -0.04711418226361275):
												if(y_velocity <= -0.3718634694814682):
													return True
								else:
									if(lander_x <= -0.028066777624189854):
										return True
							else:
								if(lander_y > 1.3478015065193176):
									if(lander_y <= 1.3526949882507324):
										if(angle_velocity > -0.0776585042476654):
											return True
						else:
							if(lander_y <= 1.3533155918121338):
								if(y_velocity > -0.25446075201034546):
									if(y_velocity > -0.23582569509744644):
										return True
							else:
								if(y_velocity <= -0.22856424748897552):
									if(lander_x <= 0.09026093408465385):
										if(lander_y > 1.381516456604004):
											return True
									else:
										if(angle <= 0.567365825176239):
											return True
										else:
											if(x_velocity > 0.19226755946874619):
												return True
								else:
									if(angle_velocity <= -0.0935678705573082):
										return True
			else:
				if(lander_y <= 0.4006982296705246):
					if(y_velocity <= -0.23569615185260773):
						if(angle <= -0.058152781799435616):
							if(y_velocity <= -0.25839124619960785):
								if(x_velocity <= -0.13590740412473679):
									if(y_velocity <= -0.29675520956516266):
										if(angle <= -0.19683077186346054):
											if(angle_velocity > 0.09490758925676346):
												if(lander_y > 0.35257023572921753):
													return True
										else:
											return True
									else:
										if(angle_velocity <= -0.01466236962005496):
											return True
										else:
											if(y_velocity <= -0.27699221670627594):
												if(angle_velocity > 0.0550838578492403):
													if(x_velocity > -0.1734641119837761):
														if(lander_x <= 0.041015053167939186):
															return True
											else:
												if(lander_x > 0.14075402915477753):
													return True
								else:
									if(lander_x <= 0.14820809662342072):
										if(y_velocity <= -0.2689857631921768):
											if(angle <= -0.11797886714339256):
												if(x_velocity <= -0.11671330034732819):
													return True
											else:
												return True
										else:
											if(angle > -0.10477631539106369):
												if(y_velocity > -0.2687617987394333):
													if(x_velocity <= -0.1222674734890461):
														if(angle_velocity <= 0.010657726787030697):
															return True
													else:
														if(angle_velocity <= -0.009205518756061792):
															if(lander_x > -0.23955176025629044):
																if(lander_y <= 0.3038367033004761):
																	return True
														else:
															if(angle <= -0.09133792668581009):
																if(angle <= -0.09316127747297287):
																	return True
															else:
																return True
							else:
								if(lander_y <= 0.1527993083000183):
									if(x_velocity <= -0.007451545679941773):
										if(angle > -0.09280223399400711):
											if(angle_velocity > -0.03134900890290737):
												if(angle_velocity <= -0.024035007692873478):
													if(lander_y <= 0.07305090129375458):
														return True
												else:
													return True
									else:
										if(lander_y > 0.147546648979187):
											return True
								else:
									if(x_velocity <= -0.07946266233921051):
										if(y_velocity <= -0.25577312707901):
											return True
									else:
										if(angle <= -0.05995078384876251):
											if(x_velocity <= -0.024109167978167534):
												if(y_velocity <= -0.2559092044830322):
													if(y_velocity <= -0.25742679834365845):
														return True
												else:
													if(y_velocity <= -0.24186769127845764):
														return True
						else:
							if(angle_velocity <= -0.015326505992561579):
								if(lander_y <= 0.25232017040252686):
									if(angle <= -0.03989301435649395):
										if(y_velocity <= -0.24880661815404892):
											return True
										else:
											if(lander_y <= 0.1596236675977707):
												if(x_velocity <= -0.011941983830183744):
													return True
												else:
													if(lander_x <= -0.16848482936620712):
														return True
											else:
												if(lander_y > 0.21536662429571152):
													if(lander_y > 0.2309582680463791):
														return True
									else:
										if(lander_x <= 0.12734685093164444):
											return True
										else:
											if(lander_y <= 0.2011852115392685):
												return True
								else:
									if(angle <= -0.019317341037094593):
										if(y_velocity <= -0.2652069330215454):
											return True
										else:
											if(angle_velocity <= -0.026273712515830994):
												if(angle_velocity <= -0.032510457560420036):
													return True
												else:
													if(lander_x <= -0.2069142386317253):
														return True
													else:
														if(lander_x > 0.08081717416644096):
															return True
											else:
												if(x_velocity <= -0.050697602331638336):
													if(lander_y > 0.27971217036247253):
														if(y_velocity <= -0.24368827044963837):
															if(angle_velocity > -0.0188182620331645):
																return True
												else:
													if(x_velocity <= 0.01107311388477683):
														if(angle_velocity <= -0.0155005375854671):
															return True
													else:
														if(angle <= -0.03387994319200516):
															return True
									else:
										if(y_velocity <= -0.2414861023426056):
											return True
										else:
											if(lander_x <= -0.051000071689486504):
												return True
											else:
												if(angle <= 0.013151626102626324):
													if(angle_velocity <= -0.016257576644420624):
														if(angle_velocity <= -0.022562923841178417):
															if(lander_x <= 0.040557241067290306):
																return True
													else:
														return True
												else:
													return True
							else:
								if(angle <= 0.1076303981244564):
									if(x_velocity <= -0.07047595828771591):
										if(y_velocity <= -0.2393423095345497):
											if(y_velocity <= -0.2515132427215576):
												if(y_velocity <= -0.25362326204776764):
													return True
												else:
													if(y_velocity > -0.2534611374139786):
														return True
											else:
												if(lander_y <= 0.27551068365573883):
													return True
												else:
													if(lander_x <= 0.09606976807117462):
														if(x_velocity > -0.0761597640812397):
															if(lander_y <= 0.35375913977622986):
																return True
													else:
														if(x_velocity <= -0.07320167869329453):
															return True
										else:
											if(lander_y <= 0.20869382470846176):
												return True
									else:
										if(angle <= -0.04748993366956711):
											if(angle <= -0.0478067621588707):
												if(x_velocity <= 0.016812524758279324):
													if(lander_x <= 0.02426991518586874):
														if(y_velocity <= -0.24017248302698135):
															return True
														else:
															if(y_velocity > -0.2390705943107605):
																return True
													else:
														if(lander_x > 0.0256518367677927):
															if(lander_y <= 0.31341123580932617):
																return True
															else:
																if(x_velocity > -0.06130965054035187):
																	return True
												else:
													if(lander_x > -0.2577451467514038):
														return True
										else:
											if(y_velocity <= -0.24577776342630386):
												return True
											else:
												if(y_velocity > -0.24573373794555664):
													if(lander_y <= 0.34662970900535583):
														if(y_velocity <= -0.2367456704378128):
															if(angle <= -0.025782080367207527):
																if(angle <= -0.026252281852066517):
																	if(lander_x <= 0.05234885215759277):
																		if(angle <= -0.029134863056242466):
																			return True
																		else:
																			if(angle > -0.028867912478744984):
																				return True
																	else:
																		if(angle_velocity > 0.019958649529144168):
																			return True
															else:
																return True
														else:
															if(y_velocity > -0.23673775792121887):
																return True
													else:
														if(x_velocity <= -0.0319372471421957):
															if(y_velocity <= -0.24006640911102295):
																return True
															else:
																if(angle_velocity <= 0.0012883221497759223):
																	if(lander_x <= 0.053998565301299095):
																		return True
														else:
															if(lander_y > 0.3471149504184723):
																if(angle > -0.03399592638015747):
																	if(angle_velocity <= -0.001515519164968282):
																		if(angle_velocity <= -0.0021210895502008498):
																			return True
																	else:
																		return True
					else:
						if(x_velocity <= -0.04648813232779503):
							if(lander_y <= 0.19113826006650925):
								if(angle <= -0.046979352831840515):
									if(angle_velocity <= 0.02028462290763855):
										if(x_velocity <= -0.09238986298441887):
											if(x_velocity <= -0.09955183044075966):
												return True
										else:
											if(lander_y <= 0.12361043319106102):
												if(lander_x <= 0.030186462681740522):
													if(angle <= -0.04844336397945881):
														if(x_velocity <= -0.05976850725710392):
															return True
														else:
															if(angle_velocity > 0.0025002136826515198):
																return True
									else:
										if(lander_y <= 0.01318421121686697):
											return True
										else:
											if(angle <= -0.08574359491467476):
												if(angle > -0.09479870647192001):
													if(lander_y <= 0.0951540544629097):
														return True
								else:
									if(x_velocity > -0.09178847447037697):
										if(x_velocity <= -0.04701359197497368):
											if(lander_x <= 0.13120436668395996):
												if(lander_x <= -0.05006728135049343):
													if(angle <= -0.04138617776334286):
														return True
												else:
													return True
							else:
								if(angle_velocity <= -0.00023782247444614768):
									if(angle <= -0.026178336702287197):
										if(lander_x <= -0.020393419545143843):
											if(angle_velocity <= -0.0047756817657500505):
												return True
									else:
										if(x_velocity > -0.0636415109038353):
											if(x_velocity <= -0.04927167296409607):
												if(lander_x > -0.023161982651799917):
													return True
								else:
									if(x_velocity > -0.07402462884783745):
										if(x_velocity <= -0.06454848125576973):
											if(y_velocity <= -0.23083890974521637):
												return True
										else:
											if(lander_x <= 0.08132438734173775):
												if(angle_velocity <= 0.013537989929318428):
													if(angle > -0.029097859282046556):
														if(angle_velocity > 0.004578798310831189):
															return True
											else:
												return True
						else:
							if(angle_velocity <= -0.009669447783380747):
								if(angle <= -0.011002792976796627):
									if(lander_y <= 0.13093000650405884):
										if(lander_x <= -0.107452392578125):
											if(x_velocity > -0.04382038861513138):
												if(lander_x > -0.23999667167663574):
													if(angle <= -0.06118393503129482):
														if(x_velocity <= -0.037861282005906105):
															return True
													else:
														return True
										else:
											if(x_velocity <= -0.018888779915869236):
												if(lander_x <= 0.04912071116268635):
													return True
												else:
													if(y_velocity <= -0.22811774909496307):
														return True
											else:
												if(lander_y <= 0.017065117601305246):
													return True
												else:
													if(lander_y <= 0.12869887053966522):
														if(angle > -0.015971645712852478):
															if(angle <= -0.011573934461921453):
																return True
													else:
														return True
									else:
										if(lander_x <= -0.053118277341127396):
											if(x_velocity <= -0.01717822067439556):
												if(lander_x <= -0.11784172058105469):
													if(lander_y <= 0.16643508523702621):
														return True
												else:
													if(angle > -0.03396008908748627):
														return True
											else:
												if(angle <= -0.01267700083553791):
													if(lander_x <= -0.13374271243810654):
														if(angle_velocity > -0.025852824561297894):
															if(angle <= -0.014359915163367987):
																if(angle <= -0.030668151564896107):
																	if(lander_x <= -0.23997964709997177):
																		return True
																else:
																	return True
												else:
													return True
								else:
									if(angle <= 0.0026032080641016364):
										if(angle <= 0.0001600760042492766):
											if(y_velocity <= -0.2289690598845482):
												if(y_velocity > -0.2350490614771843):
													if(lander_x <= 0.04257049597799778):
														return True
													else:
														if(y_velocity > -0.2317463606595993):
															return True
											else:
												if(lander_y <= 0.24653103202581406):
													if(lander_x <= 0.004316091537475586):
														return True
									else:
										if(angle_velocity <= -0.030009222216904163):
											if(lander_y <= 0.3308558464050293):
												return True
										else:
											if(lander_y <= 0.39159490168094635):
												if(angle <= 0.005531423492357135):
													if(angle <= 0.005103458883240819):
														return True
												else:
													return True
											else:
												if(lander_x <= 0.060754725243896246):
													return True
							else:
								if(lander_y <= 0.26726894080638885):
									if(lander_y > -0.0023655378608964384):
										if(angle <= -0.07237591594457626):
											if(angle_velocity > 0.019305534195154905):
												if(x_velocity > -0.03855601325631142):
													return True
										else:
											if(angle <= -0.0323178693652153):
												if(y_velocity <= -0.2266954481601715):
													if(angle <= -0.03243671730160713):
														if(x_velocity <= -0.0008773153240326792):
															if(lander_x <= -0.2236066311597824):
																if(lander_y > 0.08764000982046127):
																	return True
															else:
																return True
														else:
															if(x_velocity > 0.005487707094289362):
																return True
												else:
													if(angle_velocity <= 0.0038238561246544123):
														if(x_velocity <= -0.011577209457755089):
															return True
													else:
														if(lander_y <= 0.0928050484508276):
															return True
											else:
												if(x_velocity > -0.04456006549298763):
													if(x_velocity <= -0.03155418112874031):
														if(lander_y <= 0.17070479691028595):
															return True
														else:
															if(lander_y <= 0.23987478762865067):
																if(y_velocity <= -0.23088078945875168):
																	return True
																else:
																	if(angle_velocity <= -0.004556837142445147):
																		return True
													else:
														return True
								else:
									if(angle <= -0.002756904112175107):
										if(x_velocity <= 0.013403969816863537):
											if(angle <= -0.029252595268189907):
												if(angle_velocity <= 0.049676163122057915):
													if(x_velocity <= -0.03640488535165787):
														if(x_velocity <= -0.041138842701911926):
															if(angle_velocity <= 0.02936954889446497):
																return True
											else:
												if(angle <= -0.025236784480512142):
													return True
												else:
													if(y_velocity <= -0.23320049792528152):
														if(lander_x <= 0.02387318667024374):
															if(lander_y <= 0.38562603294849396):
																return True
													else:
														if(lander_y <= 0.2971774637699127):
															if(lander_y > 0.27523885667324066):
																if(angle_velocity <= 0.05619689077138901):
																	if(angle <= -0.021180149167776108):
																		if(y_velocity <= -0.227064311504364):
																			return True
																	else:
																		return True
														else:
															if(y_velocity <= -0.22572313249111176):
																if(angle_velocity <= -0.0019480733899399638):
																	if(angle_velocity > -0.005438260734081268):
																		return True
															else:
																if(lander_x > -0.03360905568115413):
																	return True
										else:
											if(angle_velocity <= 0.05213731341063976):
												if(lander_x <= -0.06083793565630913):
													if(angle <= -0.022042084485292435):
														if(lander_x <= -0.2704541087150574):
															return True
													else:
														if(x_velocity <= 0.06282635405659676):
															return True
														else:
															if(angle_velocity > 0.01550420792773366):
																return True
											else:
												return True
									else:
										if(x_velocity <= 0.0007018791511654854):
											if(lander_x <= 0.02224893495440483):
												if(lander_y <= 0.3690223693847656):
													if(y_velocity <= -0.2266487404704094):
														if(angle > 0.0024472602981404634):
															return True
													else:
														return True
											else:
												if(x_velocity > -0.04012374207377434):
													return True
										else:
											return True
				else:
					if(y_velocity <= -0.2605880945920944):
						if(lander_y <= 0.7481449842453003):
							if(angle <= -0.02181170228868723):
								if(y_velocity <= -0.27377182245254517):
									if(x_velocity <= -0.12312685325741768):
										if(y_velocity <= -0.28999267518520355):
											if(angle <= -0.09409844875335693):
												if(y_velocity <= -0.3070802539587021):
													if(x_velocity <= -0.15461762249469757):
														if(angle_velocity <= 0.011445730458945036):
															if(y_velocity <= -0.33848021924495697):
																if(lander_y > 0.43884681165218353):
																	if(angle_velocity > -0.028521228581666946):
																		return True
															else:
																if(angle_velocity > -0.0010421707120258361):
																	if(angle > -0.1446538306772709):
																		return True
														else:
															if(lander_y > 0.41049598157405853):
																if(y_velocity <= -0.3190077096223831):
																	return True
																else:
																	if(x_velocity > -0.20831692963838577):
																		return True
													else:
														if(x_velocity > -0.14397743344306946):
															if(lander_y <= 0.7201682031154633):
																if(y_velocity <= -0.31099455058574677):
																	return True
												else:
													if(angle_velocity > 0.057761792093515396):
														return True
											else:
												if(lander_x <= 0.03306412696838379):
													if(lander_y <= 0.7044136822223663):
														return True
												else:
													return True
										else:
											if(angle_velocity <= 0.0013880389160476625):
												if(angle > -0.0708085373044014):
													return True
											else:
												if(lander_y <= 0.4773557186126709):
													if(angle_velocity <= 0.06706838868558407):
														return True
												else:
													if(y_velocity <= -0.28843483328819275):
														if(angle <= -0.09170417487621307):
															return True
									else:
										if(angle_velocity <= -0.02546069025993347):
											if(y_velocity <= -0.27917616069316864):
												if(lander_y <= 0.7350277602672577):
													if(lander_x <= 0.14085469022393227):
														if(y_velocity <= -0.28723202645778656):
															return True
														else:
															if(y_velocity > -0.28289762139320374):
																return True
											else:
												if(angle_velocity <= -0.03183677792549133):
													return True
										else:
											if(lander_y <= 0.6829327642917633):
												if(angle <= -0.11299680918455124):
													if(angle_velocity <= 0.027471397072076797):
														if(x_velocity > -0.10862397775053978):
															if(lander_y > 0.5757111012935638):
																return True
													else:
														if(angle <= -0.1144704520702362):
															if(angle <= -0.2945413142442703):
																if(y_velocity <= -0.4682534784078598):
																	return True
															else:
																if(lander_x <= -0.25343234837055206):
																	return True
																else:
																	if(x_velocity > -0.11931423470377922):
																		return True
												else:
													if(y_velocity <= -0.2816237658262253):
														if(x_velocity <= -0.001457451144233346):
															return True
														else:
															if(x_velocity > -0.0009232910815626383):
																return True
													else:
														if(y_velocity > -0.2815605252981186):
															if(lander_x <= 0.08335079997777939):
																return True
															else:
																if(lander_x > 0.08381500095129013):
																	if(x_velocity <= -0.0811101607978344):
																		return True
											else:
												if(angle_velocity <= 0.0030370953027158976):
													if(y_velocity <= -0.2869114726781845):
														if(angle_velocity <= -0.02223268896341324):
															if(angle_velocity <= -0.024180482141673565):
																return True
														else:
															if(angle_velocity <= 0.0024429350160062313):
																return True
													else:
														if(angle_velocity <= -0.022267588414251804):
															return True
												else:
													if(lander_y > 0.6835232675075531):
														if(y_velocity <= -0.2742239385843277):
															if(angle <= -0.040644459426403046):
																if(angle <= -0.04082971066236496):
																	if(y_velocity <= -0.29040004312992096):
																		if(angle <= -0.33636410534381866):
																			if(lander_x > -0.3255809098482132):
																				return True
																		else:
																			if(angle <= -0.10107427462935448):
																				if(angle_velocity > 0.14220482856035233):
																					if(lander_y <= 0.6909043788909912):
																						if(angle <= -0.2481434866786003):
																							return True
																					else:
																						if(x_velocity <= -0.06813829019665718):
																							if(y_velocity <= -0.3600621819496155):
																								return True
																						else:
																							return True
																			else:
																				return True
																	else:
																		if(lander_x <= -0.17059163749217987):
																			if(angle > -0.137898251414299):
																				if(y_velocity <= -0.2748130261898041):
																					if(angle <= -0.04301474429666996):
																						return True
																					else:
																						if(lander_x > -0.24942755699157715):
																							return True
																				else:
																					if(y_velocity > -0.27454207837581635):
																						return True
																		else:
																			if(lander_y <= 0.7137521505355835):
																				if(x_velocity <= -0.020681929774582386):
																					return True
															else:
																return True
								else:
									if(angle_velocity <= -0.01597929745912552):
										if(x_velocity <= -0.0942218005657196):
											if(angle > -0.059978656470775604):
												if(angle <= -0.03969539329409599):
													if(lander_y <= 0.5571637153625488):
														return True
										else:
											if(y_velocity <= -0.26919007301330566):
												if(lander_y <= 0.5307645499706268):
													return True
												else:
													if(lander_x <= -0.1637360081076622):
														if(lander_x > -0.18021659553050995):
															return True
									else:
										if(x_velocity <= -0.11434036493301392):
											if(angle_velocity <= -0.0038744015619158745):
												return True
											else:
												if(lander_x > 0.13892173767089844):
													if(lander_x <= 0.18229293823242188):
														if(y_velocity > -0.26780669391155243):
															return True
										else:
											if(angle <= -0.054483141750097275):
												if(angle_velocity <= 0.12010367587208748):
													if(lander_y <= 0.4569232165813446):
														if(x_velocity <= -0.04819830134510994):
															if(x_velocity <= -0.07681286707520485):
																return True
															else:
																if(y_velocity <= -0.2695690393447876):
																	if(x_velocity > -0.06151467375457287):
																		return True
																else:
																	return True
														else:
															if(angle_velocity > 0.039116187021136284):
																return True
													else:
														if(y_velocity <= -0.26215559244155884):
															if(x_velocity <= -0.038297983817756176):
																if(lander_x <= 0.022746515460312366):
																	if(x_velocity <= -0.09948572516441345):
																		return True
																else:
																	if(angle_velocity > 0.04956074431538582):
																		return True
															else:
																if(y_velocity <= -0.26380398869514465):
																	if(lander_y > 0.7288891673088074):
																		if(angle > -0.08069190010428429):
																			return True
																else:
																	return True
												else:
													if(x_velocity <= 0.05011344328522682):
														if(y_velocity > -0.26904501020908356):
															return True
													else:
														if(y_velocity <= -0.26122117042541504):
															return True
											else:
												if(lander_y <= 0.6975981593132019):
													if(x_velocity <= -0.09737060591578484):
														if(y_velocity <= -0.26768849790096283):
															return True
													else:
														if(angle <= -0.022035779431462288):
															if(y_velocity <= -0.2633034735918045):
																if(angle_velocity <= -0.010728998109698296):
																	if(y_velocity > -0.2719820439815521):
																		if(lander_x <= 0.13725967705249786):
																			if(angle <= -0.02529054321348667):
																				return True
																else:
																	if(x_velocity <= -0.08750950545072556):
																		if(angle > -0.05205370485782623):
																			return True
																	else:
																		if(y_velocity <= -0.27327577769756317):
																			if(angle_velocity > 0.0019136578775942326):
																				return True
																		else:
																			if(y_velocity <= -0.26708464324474335):
																				return True
																			else:
																				if(y_velocity > -0.2669599801301956):
																					if(y_velocity <= -0.2661731094121933):
																						if(lander_x <= 0.07894434640184045):
																							return True
																					else:
																						if(lander_y <= 0.6357315182685852):
																							if(lander_y <= 0.5822017192840576):
																								return True
																							else:
																								if(lander_y > 0.5902732610702515):
																									return True
																						else:
																							if(lander_y > 0.643723875284195):
																								return True
															else:
																if(y_velocity > -0.2629808038473129):
																	if(lander_x <= 0.025634002406150103):
																		if(angle <= -0.04536372795701027):
																			if(angle <= -0.04816283844411373):
																				return True
																		else:
																			if(y_velocity <= -0.2607315331697464):
																				if(x_velocity <= -0.048706160858273506):
																					if(lander_y <= 0.5282087624073029):
																						return True
																				else:
																					return True
																			else:
																				if(lander_y > 0.543288841843605):
																					return True
												else:
													if(x_velocity <= -0.003156482183840126):
														if(lander_y > 0.7053253650665283):
															if(angle_velocity <= 0.022812683135271072):
																if(y_velocity <= -0.26225148141384125):
																	return True
															else:
																if(lander_x <= 0.021719026379287243):
																	if(y_velocity > -0.2611839026212692):
																		return True
																else:
																	return True
													else:
														if(angle_velocity <= 0.0421996358782053):
															if(x_velocity <= 0.010008121520513669):
																if(angle > -0.036612335592508316):
																	return True
														else:
															if(angle_velocity <= 0.04846490919589996):
																if(y_velocity <= -0.2639511823654175):
																	return True
															else:
																return True
							else:
								if(angle_velocity <= -0.0003560411714715883):
									if(y_velocity <= -0.27034956216812134):
										if(angle_velocity <= -0.0008982796862255782):
											if(angle <= -0.019256810657680035):
												if(x_velocity <= -0.03592772223055363):
													return True
												else:
													if(x_velocity > -0.006472905835835263):
														return True
											else:
												return True
									else:
										if(lander_x <= 0.1070275790989399):
											if(angle <= -0.0019573994795791805):
												if(x_velocity <= 0.023342729546129704):
													if(lander_x <= 0.027657413855195045):
														return True
													else:
														if(x_velocity <= -0.03038112446665764):
															if(lander_x <= 0.08523745462298393):
																if(x_velocity > -0.08026697114109993):
																	return True
															else:
																if(lander_x > 0.0926971435546875):
																	if(y_velocity <= -0.2669934332370758):
																		return True
												else:
													if(lander_y <= 0.5626631677150726):
														return True
											else:
												if(angle_velocity <= -0.0014532044006045908):
													if(angle_velocity <= -0.03194776177406311):
														if(angle_velocity <= -0.03241371363401413):
															return True
													else:
														if(lander_y <= 0.697488933801651):
															return True
														else:
															if(lander_y > 0.70826855301857):
																return True
												else:
													if(angle > 0.019649216905236244):
														return True
										else:
											if(angle <= -0.0036085695028305054):
												if(x_velocity <= -0.08577810600399971):
													return True
											else:
												if(lander_x <= 0.1511659175157547):
													return True
								else:
									if(x_velocity <= -0.09095006063580513):
										if(y_velocity <= -0.26875996589660645):
											return True
									else:
										if(lander_x <= 0.15463419258594513):
											if(lander_y <= 0.6874419748783112):
												return True
											else:
												if(y_velocity <= -0.26212240755558014):
													if(y_velocity <= -0.2651161700487137):
														if(angle_velocity <= 0.004804711090400815):
															if(angle_velocity <= 0.004528076155111194):
																return True
														else:
															return True
													else:
														if(x_velocity > -0.04879201017320156):
															if(angle_velocity <= 0.013109767809510231):
																if(x_velocity <= 0.003676973283290863):
																	return True
															else:
																return True
										else:
											if(angle_velocity > 0.00947924517095089):
												return True
						else:
							if(angle <= 0.02187927905470133):
								if(y_velocity <= -0.2870802879333496):
									if(x_velocity <= 0.28544867038726807):
										if(lander_y <= 0.927573561668396):
											if(angle <= -0.05751131847500801):
												if(y_velocity <= -0.3031482994556427):
													if(x_velocity <= -0.07524305582046509):
														if(y_velocity <= -0.3130800426006317):
															if(angle <= -0.1344577819108963):
																if(y_velocity <= -0.35077668726444244):
																	if(angle_velocity <= 0.008511662017554045):
																		if(y_velocity <= -0.5918124914169312):
																			return True
																	else:
																		if(angle_velocity <= 0.15972856432199478):
																			if(lander_x <= -0.3242046386003494):
																				if(angle_velocity > 0.1528751254081726):
																					if(y_velocity > -0.4986424446105957):
																						return True
																			else:
																				if(angle_velocity <= 0.15597213804721832):
																					if(angle <= -0.23700503259897232):
																						if(y_velocity <= -0.3955126404762268):
																							if(x_velocity <= -0.15833336859941483):
																								if(x_velocity <= -0.26440951228141785):
																									if(angle_velocity <= 0.08291301131248474):
																										if(lander_x > -0.30285125970840454):
																											if(lander_y > 0.817107230424881):
																												if(lander_y <= 0.8611823618412018):
																													if(angle <= -0.38690371811389923):
																														return True
																												else:
																													return True
																									else:
																										return True
																								else:
																									if(angle > -0.3712017238140106):
																										if(x_velocity > -0.25631169974803925):
																											if(lander_y <= 0.9086543321609497):
																												return True
																											else:
																												if(y_velocity <= -0.4517647922039032):
																													return True
																					else:
																						if(angle_velocity > 0.038537709042429924):
																							return True
																		else:
																			if(angle <= -0.42627476155757904):
																				if(y_velocity <= -0.602351188659668):
																					return True
																			else:
																				if(lander_y <= 0.7881056070327759):
																					if(lander_y <= 0.786048024892807):
																						if(angle_velocity <= 0.17853285372257233):
																							if(angle <= -0.31298042833805084):
																								return True
																							else:
																								if(lander_x > -0.2539311647415161):
																									return True
																						else:
																							return True
																				else:
																					return True
																else:
																	if(angle <= -0.18281710892915726):
																		if(x_velocity > -0.15664704889059067):
																			if(angle_velocity <= 0.19388870149850845):
																				if(y_velocity <= -0.34917406737804413):
																					return True
																	else:
																		if(y_velocity <= -0.33404724299907684):
																			if(angle_velocity <= 0.07215861603617668):
																				if(y_velocity <= -0.339968666434288):
																					return True
																			else:
																				return True
																		else:
																			if(y_velocity <= -0.3166087418794632):
																				if(x_velocity <= -0.10577506572008133):
																					if(angle <= -0.14599348604679108):
																						return True
															else:
																if(angle_velocity <= 0.13706297054886818):
																	if(angle_velocity <= -0.010039173532277346):
																		if(x_velocity <= -0.12081129848957062):
																			return True
																		else:
																			if(angle > -0.08164716698229313):
																				return True
																	else:
																		if(y_velocity <= -0.3169088214635849):
																			return True
																		else:
																			if(y_velocity > -0.31652095913887024):
																				return True
														else:
															if(angle > -0.09483622759580612):
																if(angle <= -0.0794033445417881):
																	if(lander_y <= 0.8506254851818085):
																		return True
													else:
														if(angle_velocity <= 0.03566866181790829):
															if(lander_x <= -0.1368904635310173):
																if(x_velocity <= -0.01631470862776041):
																	if(angle <= -0.07994751259684563):
																		if(x_velocity <= -0.05027257464826107):
																			if(angle > -0.1067640520632267):
																				if(angle_velocity > -0.004978791810572147):
																					return True
																	else:
																		return True
														else:
															if(lander_y > 0.7518079578876495):
																if(lander_y <= 0.773534506559372):
																	if(lander_y <= 0.7727174758911133):
																		if(lander_x <= -0.2134246602654457):
																			return True
																else:
																	if(angle <= -0.19352463632822037):
																		if(angle_velocity > 0.1966862976551056):
																			return True
																	else:
																		if(angle_velocity <= 0.24249832332134247):
																			if(angle <= -0.13196848332881927):
																				if(angle <= -0.1350964531302452):
																					return True
																			else:
																				return True
																		else:
																			if(lander_x > -0.2854953110218048):
																				return True
												else:
													if(x_velocity <= -0.03121186699718237):
														if(angle_velocity <= 0.060871485620737076):
															if(lander_x <= -0.14834103733301163):
																if(y_velocity <= -0.29245810210704803):
																	return True
															else:
																if(lander_x <= 0.006495429202914238):
																	if(y_velocity > -0.2896360158920288):
																		return True
														else:
															if(lander_y <= 0.8233723044395447):
																if(y_velocity <= -0.2951791435480118):
																	return True
															else:
																if(angle > -0.1473691686987877):
																	if(angle_velocity <= 0.06705183163285255):
																		if(angle_velocity > 0.06404086947441101):
																			return True
													else:
														if(angle_velocity > 0.03155993763357401):
															if(angle > -0.14376632124185562):
																if(y_velocity <= -0.3021085411310196):
																	if(angle <= -0.09847354143857956):
																		return True
																else:
																	if(lander_y <= 0.8006114363670349):
																		if(angle_velocity <= 0.18462839722633362):
																			return True
																		else:
																			if(angle_velocity > 0.2033485770225525):
																				return True
																	else:
																		if(lander_y <= 0.8174704313278198):
																			if(angle_velocity > 0.1395440325140953):
																				if(lander_y <= 0.8094200193881989):
																					return True
																		else:
																			if(y_velocity <= -0.29175035655498505):
																				if(angle <= -0.09574378281831741):
																					if(angle <= -0.09988484159111977):
																						return True
																				else:
																					return True
																			else:
																				if(angle_velocity <= 0.07651634141802788):
																					return True
																				else:
																					if(lander_y > 0.9152035415172577):
																						return True
											else:
												if(lander_x <= 0.21776456385850906):
													if(y_velocity <= -0.2921095937490463):
														if(y_velocity <= -0.29952065646648407):
															return True
														else:
															if(y_velocity > -0.29944540560245514):
																if(angle <= -0.047937532886862755):
																	if(angle <= -0.04831410199403763):
																		if(x_velocity <= -0.010877876309677958):
																			return True
																		else:
																			if(lander_x <= -0.2377481460571289):
																				return True
																else:
																	if(y_velocity <= -0.29815472662448883):
																		if(y_velocity <= -0.2982545644044876):
																			return True
																	else:
																		return True
													else:
														if(x_velocity > -0.11104102060198784):
															if(y_velocity > -0.2919992655515671):
																if(lander_x <= -0.13604015856981277):
																	if(angle_velocity <= 0.018082361668348312):
																		if(angle_velocity <= -0.0016877823509275913):
																			if(angle <= -0.045225536450743675):
																				return True
																	else:
																		return True
																else:
																	return True
												else:
													if(y_velocity <= -0.3133704215288162):
														return True
										else:
											if(y_velocity <= -0.3181559443473816):
												if(x_velocity <= -0.09489988535642624):
													if(y_velocity <= -0.3449101150035858):
														if(angle <= 0.003930528182536364):
															if(angle <= -0.1493743658065796):
																if(y_velocity <= -0.3789035230875015):
																	if(angle_velocity <= 0.027191842906177044):
																		if(y_velocity <= -0.3943863660097122):
																			if(lander_x <= -0.1216805949807167):
																				if(x_velocity <= -0.2808101028203964):
																					if(angle <= -0.263735756278038):
																						if(y_velocity <= -0.45882800221443176):
																							if(lander_y <= 1.059090793132782):
																								if(x_velocity <= -0.42039482295513153):
																									if(y_velocity <= -0.5972758829593658):
																										if(angle_velocity > -0.027917093597352505):
																											return True
																									else:
																										if(lander_x > -0.2559261620044708):
																											return True
																								else:
																									if(lander_x > -0.21821627020835876):
																										if(angle_velocity > -0.004105630214326084):
																											return True
																							else:
																								if(angle <= -0.3265712559223175):
																									if(y_velocity <= -0.5662457346916199):
																										if(lander_x > -0.30618157982826233):
																											return True
																									else:
																										if(lander_x > -0.24335196614265442):
																											if(y_velocity <= -0.49221718311309814):
																												if(lander_y <= 1.078147292137146):
																													if(x_velocity <= -0.44973519444465637):
																														return True
																												else:
																													if(y_velocity <= -0.5497466921806335):
																														if(lander_y > 1.247488021850586):
																															return True
																													else:
																														return True
																								else:
																									return True
																						else:
																							if(lander_y <= 1.3552486300468445):
																								if(lander_x <= -0.15971794724464417):
																									if(y_velocity <= -0.45118361711502075):
																										if(y_velocity > -0.45621345937252045):
																											return True
																								else:
																									if(x_velocity <= -0.3526459187269211):
																										if(angle_velocity > -0.01725156349129975):
																											if(x_velocity <= -0.36262474954128265):
																												return True
																									else:
																										return True
																					else:
																						if(y_velocity <= -0.4173963814973831):
																							return True
																						else:
																							if(lander_x <= -0.12892670929431915):
																								if(lander_y <= 1.1672784686088562):
																									return True
																			else:
																				if(lander_y <= 1.4432497024536133):
																					if(angle_velocity <= -0.013694960623979568):
																						if(y_velocity <= -0.42696885764598846):
																							return True
																						else:
																							if(lander_x > -0.09979639202356339):
																								if(x_velocity <= -0.22518950700759888):
																									return True
																					else:
																						if(x_velocity <= -0.20433081686496735):
																							if(angle <= -0.2172703817486763):
																								if(x_velocity <= -0.30415695905685425):
																									return True
																							else:
																								return True
																						else:
																							if(x_velocity > -0.19579389691352844):
																								return True
																		else:
																			if(angle > -0.16770220547914505):
																				if(lander_y <= 1.2943825125694275):
																					if(x_velocity <= -0.19877690821886063):
																						return True
																					else:
																						if(angle > -0.15145599842071533):
																							return True
																	else:
																		if(angle <= -0.24870789796113968):
																			if(y_velocity <= -0.4152718335390091):
																				if(angle <= -0.2919051945209503):
																					if(angle_velocity <= 0.12940814346075058):
																						if(y_velocity <= -0.43711379170417786):
																							if(x_velocity <= -0.25607793033123016):
																								if(lander_x <= -0.29538968205451965):
																									if(y_velocity <= -0.5677783489227295):
																										if(lander_x <= -0.3023550808429718):
																											return True
																										else:
																											if(lander_x > -0.3002033233642578):
																												return True
																									else:
																										if(angle_velocity > 0.06695100665092468):
																											if(lander_y <= 1.1772054433822632):
																												if(lander_y > 0.9512946605682373):
																													if(angle > -0.43317753076553345):
																														if(angle_velocity <= 0.12379167601466179):
																															return True
																											else:
																												return True
																								else:
																									if(x_velocity <= -0.33678731322288513):
																										if(angle <= -0.39501728117465973):
																											if(y_velocity <= -0.5294573307037354):
																												if(x_velocity <= -0.34816914796829224):
																													if(x_velocity <= -0.3924696743488312):
																														return True
																													else:
																														if(y_velocity <= -0.5837084054946899):
																															return True
																										else:
																											if(y_velocity <= -0.44568154215812683):
																												return True
																											else:
																												if(x_velocity <= -0.35553309321403503):
																													return True
																									else:
																										if(angle > -0.3540605157613754):
																											if(angle_velocity <= 0.07370385155081749):
																												if(x_velocity <= -0.28236123919487):
																													if(lander_y <= 1.2610137462615967):
																														if(angle <= -0.3481638729572296):
																															if(x_velocity <= -0.32118093967437744):
																																return True
																														else:
																															return True
																											else:
																												return True
																					else:
																						if(y_velocity <= -0.4627908915281296):
																							if(y_velocity <= -0.505884200334549):
																								return True
																							else:
																								if(y_velocity > -0.5048397183418274):
																									if(angle <= -0.3451588451862335):
																										if(lander_x <= -0.28787775337696075):
																											return True
																									else:
																										return True
																						else:
																							if(y_velocity <= -0.42912642657756805):
																								if(y_velocity <= -0.44839824736118317):
																									if(y_velocity > -0.45893318951129913):
																										return True
																							else:
																								return True
																				else:
																					if(lander_y <= 1.2647876143455505):
																						if(x_velocity <= -0.2129044607281685):
																							return True
																						else:
																							if(x_velocity > -0.21264341473579407):
																								return True
																			else:
																				if(angle_velocity <= 0.12427567690610886):
																					if(angle_velocity > 0.03626669943332672):
																						if(angle_velocity > 0.10418592393398285):
																							if(x_velocity <= -0.24043092131614685):
																								return True
																				else:
																					if(y_velocity <= -0.38959696888923645):
																						if(angle > -0.2965431958436966):
																							return True
																		else:
																			if(lander_y <= 1.3016756772994995):
																				if(y_velocity <= -0.38997744023799896):
																					return True
																				else:
																					if(angle <= -0.2142021581530571):
																						if(y_velocity > -0.38691025972366333):
																							if(lander_y <= 1.0195478796958923):
																								return True
																					else:
																						if(lander_y <= 1.232926845550537):
																							return True
																						else:
																							if(lander_y > 1.2661542296409607):
																								return True
																			else:
																				if(lander_y > 1.3090237379074097):
																					if(y_velocity <= -0.40720145404338837):
																						return True
																					else:
																						if(lander_y <= 1.3310995697975159):
																							return True
																else:
																	if(angle_velocity <= 0.08153198659420013):
																		if(x_velocity <= -0.20065878331661224):
																			if(angle_velocity <= 0.02515404112637043):
																				if(x_velocity > -0.2927251011133194):
																					if(lander_y <= 1.315960168838501):
																						if(lander_x > -0.089191485196352):
																							if(x_velocity <= -0.22504987567663193):
																								return True
																			else:
																				if(lander_x <= -0.1706898733973503):
																					if(angle_velocity > 0.05479501187801361):
																						return True
																				else:
																					if(x_velocity > -0.2175237238407135):
																						if(lander_y <= 1.1773555278778076):
																							if(y_velocity <= -0.3669579178094864):
																								if(angle > -0.18903785943984985):
																									return True
																		else:
																			if(angle <= -0.1647794246673584):
																				if(y_velocity <= -0.37773849070072174):
																					return True
																				else:
																					if(y_velocity <= -0.3698619157075882):
																						if(y_velocity > -0.37271711230278015):
																							return True
																			else:
																				if(lander_y <= 1.119242548942566):
																					if(angle_velocity <= 0.06505804881453514):
																						if(x_velocity <= -0.14835474640130997):
																							return True
																				else:
																					if(angle_velocity <= 0.05683406628668308):
																						if(lander_y <= 1.138571321964264):
																							if(angle <= -0.14969803392887115):
																								return True
																					else:
																						if(lander_x <= -0.16711640357971191):
																							if(y_velocity <= -0.35712553560733795):
																								return True
																	else:
																		if(x_velocity <= -0.17687823623418808):
																			if(y_velocity <= -0.373647078871727):
																				if(angle > -0.2283104658126831):
																					return True
																		else:
																			if(angle <= -0.1857243850827217):
																				if(y_velocity <= -0.36425161361694336):
																					return True
																				else:
																					if(lander_x > -0.2079010233283043):
																						if(lander_y <= 1.0139910280704498):
																							return True
																			else:
																				if(x_velocity <= -0.10079789534211159):
																					return True
																				else:
																					if(lander_x <= -0.1928778663277626):
																						return True
															else:
																if(y_velocity <= -0.3684648126363754):
																	return True
																else:
																	if(lander_y <= 1.1058405637741089):
																		if(angle <= -0.13921111822128296):
																			if(angle_velocity > 0.06504715979099274):
																				return True
																		else:
																			return True
																	else:
																		if(angle <= -0.09695779904723167):
																			if(angle_velocity > 0.016172837931662798):
																				if(lander_x <= -0.11046252027153969):
																					if(x_velocity <= -0.10460624098777771):
																						return True
																				else:
																					if(angle > -0.12689248099923134):
																						if(x_velocity <= -0.15471931546926498):
																							return True
																		else:
																			if(x_velocity <= -0.0986231192946434):
																				return True
														else:
															if(x_velocity > -0.4781825542449951):
																if(y_velocity <= -0.37012022733688354):
																	if(x_velocity <= -0.2534838616847992):
																		if(y_velocity <= -0.4598539471626282):
																			if(angle_velocity <= 0.03951640985906124):
																				return True
																			else:
																				if(y_velocity <= -0.5635539889335632):
																					return True
																				else:
																					if(x_velocity > -0.3460630029439926):
																						return True
																	else:
																		return True
													else:
														if(x_velocity <= -0.1294594332575798):
															if(lander_y <= 1.0964109301567078):
																if(y_velocity <= -0.33047036826610565):
																	if(angle > -0.10855249688029289):
																		if(x_velocity > -0.18380198627710342):
																			return True
																else:
																	if(angle_velocity <= -0.027879856526851654):
																		return True
														else:
															if(angle_velocity <= 0.09766862168908119):
																if(lander_y <= 1.2238355875015259):
																	if(angle <= -0.10366370156407356):
																		if(y_velocity <= -0.3361032158136368):
																			if(x_velocity <= -0.10726776719093323):
																				return True
																			else:
																				if(y_velocity <= -0.3405596613883972):
																					if(lander_x > -0.1029202938079834):
																						return True
																				else:
																					return True
																		else:
																			if(lander_y <= 1.1015729904174805):
																				if(y_velocity <= -0.3212449848651886):
																					if(lander_y <= 0.9507454037666321):
																						if(lander_y > 0.9412374198436737):
																							return True
																	else:
																		if(y_velocity <= -0.31983761489391327):
																			if(angle_velocity <= -0.004824674921110272):
																				if(angle > -0.05814482271671295):
																					return True
																			else:
																				return True
																else:
																	if(angle <= -0.05679384432733059):
																		if(angle_velocity <= 0.03945926018059254):
																			if(lander_x <= -0.03557424433529377):
																				if(angle_velocity <= 0.022860653698444366):
																					return True
															else:
																if(lander_x > -0.13209228217601776):
																	return True
												else:
													if(x_velocity <= 0.07830312848091125):
														if(angle <= -0.049028461799025536):
															if(angle_velocity > -0.0056668659672141075):
																if(y_velocity <= -0.33644188940525055):
																	if(angle <= -0.16255146265029907):
																		if(angle_velocity > 0.1187651939690113):
																			if(angle > -0.27159905433654785):
																				if(angle_velocity <= 0.13883444666862488):
																					if(lander_y > 1.0594414472579956):
																						return True
																				else:
																					return True
																	else:
																		if(angle_velocity <= 0.03516257554292679):
																			if(y_velocity <= -0.3415589928627014):
																				return True
																		else:
																			if(lander_y <= 1.2206677198410034):
																				return True
																			else:
																				if(lander_y > 1.2255938053131104):
																					return True
																else:
																	if(angle <= -0.13604997098445892):
																		if(angle_velocity > 0.12364072352647781):
																			if(angle_velocity <= 0.14699287712574005):
																				return True
																	else:
																		if(lander_y <= 0.9831717312335968):
																			if(x_velocity <= -0.034359756857156754):
																				return True
																			else:
																				if(x_velocity > -0.03361884504556656):
																					return True
																		else:
																			if(angle <= -0.10840273648500443):
																				if(angle_velocity > 0.09908459335565567):
																					if(x_velocity > -0.05165109038352966):
																						return True
																			else:
																				if(angle_velocity <= 0.02375955879688263):
																					if(lander_x <= -0.036885930225253105):
																						if(lander_y <= 0.9906821846961975):
																							return True
																						else:
																							if(angle_velocity <= 0.011057153693400323):
																								if(lander_y > 1.1105560064315796):
																									return True
																					else:
																						return True
																				else:
																					if(angle <= -0.05209057219326496):
																						if(y_velocity > -0.33621786534786224):
																							if(lander_x <= -0.04987168312072754):
																								if(x_velocity <= -0.07587060704827309):
																									if(lander_y <= 1.104224145412445):
																										return True
																								else:
																									return True
																							else:
																								if(lander_x > -0.04258246347308159):
																									return True
														else:
															if(angle_velocity <= -0.017263861373066902):
																if(x_velocity <= -0.04866043105721474):
																	return True
																else:
																	if(y_velocity <= -0.3245055228471756):
																		return True
															else:
																if(x_velocity <= -0.08984805643558502):
																	if(y_velocity <= -0.3310033529996872):
																		return True
																else:
																	if(angle_velocity <= 0.05487595312297344):
																		if(angle_velocity <= -0.009400253649801016):
																			if(angle_velocity <= -0.009901043493300676):
																				return True
																		else:
																			return True
																	else:
																		if(x_velocity > -0.06072970665991306):
																			return True
													else:
														if(y_velocity <= -0.4098746329545975):
															if(x_velocity > 0.09423593804240227):
																if(lander_x <= 0.028951263055205345):
																	return True
																else:
																	if(lander_x > 0.03138618357479572):
																		return True
														else:
															if(x_velocity <= 0.139861561357975):
																if(angle_velocity > 0.07000225596129894):
																	return True
											else:
												if(angle <= -0.0553903765976429):
													if(angle_velocity <= 0.03671233169734478):
														if(x_velocity <= -0.10055548325181007):
															if(lander_y <= 1.0441427826881409):
																if(angle_velocity > -0.005032745364587754):
																	if(x_velocity > -0.1092936247587204):
																		if(x_velocity > -0.10599024221301079):
																			return True
													else:
														if(x_velocity <= -0.008781893644481897):
															if(x_velocity > -0.0656152106821537):
																if(angle_velocity <= 0.06168821267783642):
																	if(angle > -0.07233299687504768):
																		if(angle_velocity > 0.049714384600520134):
																			return True
																else:
																	if(angle <= -0.10798439756035805):
																		if(angle_velocity <= 0.12526226043701172):
																			if(lander_y > 0.9748157560825348):
																				if(lander_y <= 1.0776776671409607):
																					if(lander_x > -0.20778391510248184):
																						return True
																	else:
																		if(x_velocity <= -0.033516447991132736):
																			if(x_velocity <= -0.06454765796661377):
																				return True
																			else:
																				if(angle_velocity <= 0.06366688758134842):
																					if(angle > -0.08179156854748726):
																						return True
														else:
															if(angle_velocity <= 0.2539850026369095):
																return True
															else:
																if(angle_velocity > 0.28028079867362976):
																	return True
												else:
													if(lander_y <= 1.1245160102844238):
														if(angle <= -0.015948761254549026):
															if(y_velocity <= -0.3007678985595703):
																if(angle_velocity <= -0.003789520589634776):
																	if(y_velocity <= -0.3148154467344284):
																		return True
																	else:
																		if(lander_y > 1.0923163890838623):
																			return True
																else:
																	if(y_velocity <= -0.30417150259017944):
																		return True
																	else:
																		if(angle_velocity <= 0.0249061593785882):
																			if(x_velocity <= -0.0213432339951396):
																				if(x_velocity > -0.0866350494325161):
																					return True
																		else:
																			if(angle > -0.03972017206251621):
																				return True
															else:
																if(x_velocity <= -0.02867597248405218):
																	if(lander_y <= 1.0179275274276733):
																		if(x_velocity > -0.1044786274433136):
																			if(angle_velocity > -0.02350452821701765):
																				if(angle > -0.04621722735464573):
																					return True
																	else:
																		if(angle_velocity > -0.012505895458161831):
																			if(y_velocity <= -0.2940923422574997):
																				if(angle_velocity <= 0.029105588793754578):
																					if(angle > -0.041270218789577484):
																						return True
																else:
																	if(angle_velocity > 0.013016893062740564):
																		if(angle_velocity <= 0.08797763288021088):
																			return True
														else:
															if(angle_velocity <= -0.03197268210351467):
																if(angle_velocity <= -0.03258275426924229):
																	return True
															else:
																if(x_velocity <= -0.09236766397953033):
																	if(angle_velocity <= -0.01633040443994105):
																		return True
																else:
																	if(y_velocity <= -0.2938740998506546):
																		return True
																	else:
																		if(y_velocity <= -0.2932325005531311):
																			if(angle_velocity > 0.011414687149226665):
																				return True
																		else:
																			return True
													else:
														if(x_velocity <= -0.05114337243139744):
															if(y_velocity <= -0.3057635873556137):
																if(x_velocity > -0.06747142970561981):
																	if(x_velocity <= -0.05498969741165638):
																		return True
														else:
															if(angle_velocity > -0.009729324374347925):
																if(lander_x <= -0.0009590625850250944):
																	if(y_velocity <= -0.29851967096328735):
																		if(angle_velocity <= 0.008440156932920218):
																			if(angle > -0.012899728026241064):
																				if(lander_x <= -0.008013629936613142):
																					return True
																		else:
																			if(angle_velocity <= 0.05459572561085224):
																				if(angle <= -0.03455031104385853):
																					if(lander_y <= 1.24310702085495):
																						return True
																				else:
																					return True
																			else:
																				if(x_velocity > -0.034596946090459824):
																					return True
																	else:
																		if(lander_y <= 1.2052368521690369):
																			if(angle <= -0.012046248652040958):
																				if(lander_y <= 1.1463180780410767):
																					return True
																			else:
																				return True
									else:
										if(angle > 0.0004229727273923345):
											if(y_velocity <= -0.5899165868759155):
												if(x_velocity <= 0.5952281653881073):
													return True
												else:
													if(x_velocity > 0.6212974190711975):
														if(x_velocity <= 0.6719889342784882):
															return True
											else:
												if(x_velocity <= 0.3466893136501312):
													if(lander_y <= 1.3488011956214905):
														return True
								else:
									if(x_velocity <= 0.015524227172136307):
										if(angle_velocity <= 0.04227382689714432):
											if(lander_y <= 0.9449955224990845):
												if(angle <= -0.015402767807245255):
													if(x_velocity <= -0.06508280709385872):
														if(angle_velocity <= 0.017942871898412704):
															if(y_velocity <= -0.2811204195022583):
																if(angle_velocity > -0.013506073970347643):
																	if(angle > -0.04564303532242775):
																		if(angle_velocity <= 0.006933748722076416):
																			return True
														else:
															if(x_velocity > -0.101777333766222):
																if(x_velocity > -0.07272878289222717):
																	if(lander_y <= 0.7930634021759033):
																		return True
													else:
														if(angle_velocity <= -0.008661546278744936):
															if(lander_y <= 0.8945707976818085):
																if(y_velocity <= -0.28486965596675873):
																	if(x_velocity <= -0.013673179782927036):
																		return True
															else:
																if(y_velocity > -0.2810187488794327):
																	if(y_velocity <= -0.2743857055902481):
																		return True
														else:
															if(angle <= -0.04194432869553566):
																if(lander_x <= -0.25347161293029785):
																	return True
																else:
																	if(x_velocity <= -0.04370899684727192):
																		if(angle > -0.0710131861269474):
																			if(lander_x > -0.146842859685421):
																				if(y_velocity <= -0.2832375317811966):
																					return True
																	else:
																		if(angle > -0.04754991829395294):
																			if(angle <= -0.0447126105427742):
																				if(lander_y <= 0.761259138584137):
																					return True
															else:
																if(y_velocity <= -0.2726004123687744):
																	if(lander_y <= 0.9051461517810822):
																		if(angle <= -0.0164434970356524):
																			if(lander_x <= 0.038593340665102005):
																				if(lander_y <= 0.844296395778656):
																					return True
																				else:
																					if(lander_y > 0.8504377901554108):
																						return True
																			else:
																				if(angle_velocity <= 0.025795327965170145):
																					return True
																	else:
																		if(x_velocity <= -0.03634175006300211):
																			if(x_velocity <= -0.0475185289978981):
																				return True
																else:
																	if(lander_x <= -0.042421627789735794):
																		if(x_velocity > -0.024506441317498684):
																			if(angle_velocity > 0.019499734975397587):
																				if(lander_y > 0.7526534795761108):
																					return True
												else:
													if(y_velocity <= -0.270012304186821):
														if(x_velocity <= -0.016377419233322144):
															if(x_velocity <= -0.07929385080933571):
																if(lander_x > 0.0782318115234375):
																	if(angle_velocity <= 0.01603014604188502):
																		if(x_velocity <= -0.0810648761689663):
																			return True
															else:
																if(angle_velocity > -0.03231810964643955):
																	if(angle <= -0.014144010841846466):
																		if(lander_y <= 0.8775476217269897):
																			return True
																	else:
																		if(lander_y <= 0.933695912361145):
																			return True
																		else:
																			if(angle > 0.0010680061823222786):
																				return True
														else:
															if(angle > 0.0021461513824760914):
																if(angle_velocity <= -0.014884327538311481):
																	if(y_velocity <= -0.27731068432331085):
																		if(x_velocity > -0.014287586323916912):
																			return True
																else:
																	return True
													else:
														if(x_velocity <= -0.041608575731515884):
															if(angle <= -0.014454931486397982):
																return True
														else:
															if(angle > -0.009365124627947807):
																if(lander_x <= 0.04172668419778347):
																	if(lander_y <= 0.8535655438899994):
																		if(y_velocity > -0.2688470184803009):
																			if(lander_x <= -0.08810577169060707):
																				if(lander_x <= -0.10726046562194824):
																					return True
																			else:
																				return True
																	else:
																		if(x_velocity > -0.017397197894752026):
																			return True
																else:
																	if(lander_y <= 0.7868961989879608):
																		return True
											else:
												if(x_velocity <= -0.02750662248581648):
													if(angle_velocity > -0.029355192556977272):
														if(angle > -0.028561473824083805):
															if(lander_x > -0.05922546423971653):
																if(y_velocity <= -0.28388258814811707):
																	if(lander_y <= 1.0503873825073242):
																		return True
												else:
													if(angle_velocity <= 0.01791199017316103):
														if(angle <= 0.02093520388007164):
															if(lander_y <= 0.9808626770973206):
																if(angle_velocity <= 0.006866823881864548):
																	if(lander_x <= -0.04376626014709473):
																		return True
																else:
																	return True
															else:
																if(angle > 0.011638423427939415):
																	if(lander_x <= 0.016232823953032494):
																		if(angle <= 0.014327658340334892):
																			return True
														else:
															return True
													else:
														if(x_velocity > -0.022695248015224934):
															if(angle_velocity <= 0.04090994782745838):
																if(angle_velocity <= 0.023044532164931297):
																	if(angle > -0.0038583377609029412):
																		return True
										else:
											if(lander_y <= 0.7757551670074463):
												if(angle > -0.08683010935783386):
													if(x_velocity <= -0.0165997426956892):
														if(y_velocity <= -0.28112266957759857):
															return True
														else:
															if(angle_velocity <= 0.05906456150114536):
																return True
													else:
														return True
											else:
												if(x_velocity <= -0.0007985317497514188):
													if(y_velocity <= -0.2753151059150696):
														if(angle_velocity <= 0.0611433032900095):
															if(angle > -0.06968993693590164):
																if(lander_y <= 0.9312511086463928):
																	if(x_velocity > -0.039910824969410896):
																		if(x_velocity <= -0.012965789763256907):
																			return True
																else:
																	if(lander_x > -0.022850417532026768):
																		return True
														else:
															if(y_velocity <= -0.28602685034275055):
																return True
												else:
													if(angle_velocity <= 0.060412293300032616):
														if(angle > -0.06914813071489334):
															if(angle <= 0.008634249912574887):
																return True
													else:
														if(y_velocity <= -0.2839789241552353):
															return True
														else:
															if(angle > 0.0011150131758768111):
																if(angle_velocity <= 0.07279662787914276):
																	return True
									else:
										if(lander_y <= 1.027734100818634):
											if(angle_velocity <= 0.19868455827236176):
												if(angle_velocity <= 0.03819133900105953):
													if(angle <= -0.005042276810854673):
														if(lander_x <= -0.29285429418087006):
															if(y_velocity <= -0.27130232751369476):
																return True
														else:
															if(y_velocity <= -0.2829112708568573):
																if(lander_x <= -0.15746107697486877):
																	return True
													else:
														if(lander_y <= 0.9751328825950623):
															if(lander_x <= 0.03997826483100653):
																if(angle <= 0.002066176733933389):
																	if(angle_velocity > 0.0063968447502702475):
																		return True
																else:
																	if(lander_y <= 0.8892716765403748):
																		return True
																	else:
																		if(lander_y > 0.9010481536388397):
																			return True
														else:
															if(angle_velocity > 0.020914265885949135):
																return True
												else:
													if(y_velocity <= -0.26225630939006805):
														if(lander_y <= 0.8528149425983429):
															return True
														else:
															if(angle <= -0.019997977651655674):
																if(lander_x <= -0.3382154703140259):
																	return True
																else:
																	if(y_velocity <= -0.2685592323541641):
																		if(x_velocity <= 0.047774912789464):
																			if(y_velocity <= -0.27596136927604675):
																				return True
															else:
																if(lander_y <= 1.0097745656967163):
																	return True
																else:
																	if(y_velocity <= -0.27412787079811096):
																		return True
													else:
														if(lander_x > -0.13444466888904572):
															return True
										else:
											if(y_velocity <= -0.27959856390953064):
												if(y_velocity <= -0.28085172176361084):
													return True
												else:
													if(angle > 0.016716327518224716):
														return True
							else:
								if(y_velocity <= -0.27584148943424225):
									if(x_velocity > -0.4281509518623352):
										if(angle <= 0.46151159703731537):
											if(lander_y <= 1.281448781490326):
												if(lander_x <= 0.07046699523925781):
													if(lander_x <= 0.07010574266314507):
														if(y_velocity <= -0.42698056995868683):
															if(y_velocity <= -0.44625256955623627):
																if(lander_x <= 0.06561880186200142):
																	if(angle_velocity <= 0.07942770421504974):
																		if(lander_y > 1.2210199236869812):
																			return True
																	else:
																		return True
																else:
																	if(lander_y <= 1.1946439743041992):
																		return True
															else:
																if(angle > 0.040779996663331985):
																	return True
														else:
															if(y_velocity <= -0.28613579273223877):
																if(y_velocity <= -0.3309361934661865):
																	if(y_velocity <= -0.33264076709747314):
																		return True
																else:
																	return True
															else:
																if(y_velocity > -0.2858380228281021):
																	if(lander_x <= 0.059750746935606):
																		if(lander_y <= 1.1131130456924438):
																			return True
																		else:
																			if(angle <= 0.06077605113387108):
																				if(y_velocity <= -0.2832896411418915):
																					return True
																				else:
																					if(x_velocity > 0.045092782005667686):
																						return True
																			else:
																				return True
												else:
													if(angle_velocity <= -0.02794352639466524):
														if(angle_velocity <= -0.02803539764136076):
															return True
													else:
														return True
											else:
												if(x_velocity <= 0.42733925580978394):
													if(angle <= 0.04763258434832096):
														if(x_velocity <= 0.34170304238796234):
															if(y_velocity <= -0.2994955778121948):
																if(lander_y <= 1.3377133011817932):
																	if(lander_y <= 1.3345809578895569):
																		if(lander_y <= 1.3234125971794128):
																			return True
																		else:
																			if(lander_y > 1.3256255984306335):
																				return True
																else:
																	return True
															else:
																if(angle_velocity > 0.06817084550857544):
																	if(lander_y > 1.347132384777069):
																		return True
													else:
														return True
												else:
													if(lander_y <= 1.2984944581985474):
														if(x_velocity <= 0.5707046687602997):
															return True
										else:
											if(y_velocity <= -0.2788342982530594):
												if(x_velocity <= 0.08405783027410507):
													if(angle_velocity <= -0.011437477078288794):
														return True
												else:
													return True
								else:
									if(angle <= 0.4801601767539978):
										if(angle <= 0.07749898359179497):
											if(lander_y <= 0.9992907345294952):
												if(angle_velocity > -0.03134584240615368):
													if(x_velocity <= -0.04115448147058487):
														if(y_velocity > -0.2683117389678955):
															return True
													else:
														if(x_velocity <= 0.030899989418685436):
															if(y_velocity <= -0.2625493109226227):
																if(angle <= 0.024610111489892006):
																	if(angle <= 0.02446788363158703):
																		if(angle_velocity > -0.020123986527323723):
																			return True
																else:
																	return True
															else:
																if(lander_y <= 0.8922903537750244):
																	return True
														else:
															if(angle_velocity > -0.007334933150559664):
																if(x_velocity > 0.03253500908613205):
																	return True
											else:
												if(x_velocity <= -0.0016471044509671628):
													if(angle_velocity <= 0.005621369840810075):
														if(angle <= 0.023702352307736874):
															return True
													else:
														if(x_velocity > -0.023332281969487667):
															return True
												else:
													if(lander_y <= 1.1409984827041626):
														if(y_velocity <= -0.2676937133073807):
															if(lander_x > -0.10712022706866264):
																return True
														else:
															if(x_velocity > 0.023460568860173225):
																if(x_velocity <= 0.0555493850260973):
																	return True
													else:
														if(x_velocity > 0.06683329120278358):
															if(angle_velocity <= 0.0761478841304779):
																if(x_velocity <= 0.08216015994548798):
																	return True
															else:
																return True
										else:
											if(lander_x <= 0.042531490325927734):
												if(y_velocity <= -0.26233261823654175):
													if(lander_y > 1.1407285928726196):
														if(x_velocity <= 0.052847832441329956):
															if(y_velocity > -0.269765242934227):
																return True
														else:
															if(angle_velocity <= -0.0067379591055214405):
																if(angle_velocity <= -0.01262631407007575):
																	return True
															else:
																return True
											else:
												if(angle <= 0.10374780744314194):
													if(angle <= 0.10111378505825996):
														return True
												else:
													return True
									else:
										if(x_velocity > 0.17136754840612411):
											return True
					else:
						if(x_velocity <= -0.0031562260119244456):
							if(lander_y <= 0.6404740214347839):
								if(y_velocity <= -0.24344873428344727):
									if(x_velocity <= -0.06039332039654255):
										if(y_velocity <= -0.25149276852607727):
											if(angle <= -0.052637698128819466):
												if(x_velocity <= -0.07406633719801903):
													if(angle > -0.07045106589794159):
														if(lander_x > 0.04302477976307273):
															if(lander_y > 0.4100666046142578):
																return True
											else:
												if(lander_y <= 0.5075192451477051):
													if(x_velocity <= -0.09953827410936356):
														if(angle_velocity <= -0.008703956351382658):
															if(angle > -0.04968533478677273):
																return True
													else:
														if(angle_velocity > -0.019486697390675545):
															if(lander_x > -0.02772045088931918):
																return True
												else:
													if(x_velocity <= -0.07289041206240654):
														if(angle_velocity <= -0.031676873564720154):
															return True
													else:
														if(x_velocity <= -0.0684046596288681):
															return True
														else:
															if(lander_x > 0.04579372517764568):
																if(x_velocity <= -0.06336255371570587):
																	return True
										else:
											if(angle_velocity <= -0.01959348376840353):
												if(lander_x <= 0.1270311400294304):
													if(angle > -0.015862680040299892):
														return True
											else:
												if(y_velocity <= -0.25109076499938965):
													if(lander_x <= 0.030603693798184395):
														return True
												else:
													if(angle > -0.01704938057810068):
														if(angle_velocity > 0.01485033379867673):
															return True
									else:
										if(angle_velocity <= -0.01589978439733386):
											if(angle > -0.012967045418918133):
												if(lander_x <= 0.05797553062438965):
													if(angle <= -0.011343478690832853):
														if(y_velocity > -0.2503780648112297):
															return True
													else:
														return True
												else:
													if(angle <= 0.015683614183217287):
														if(lander_y <= 0.423337921500206):
															return True
														else:
															if(y_velocity <= -0.2555522918701172):
																return True
															else:
																if(angle_velocity > -0.025193702429533005):
																	if(lander_x <= 0.11938934028148651):
																		return True
													else:
														return True
										else:
											if(angle <= -0.01587140467017889):
												if(y_velocity <= -0.25238659977912903):
													if(angle > -0.07502445578575134):
														if(x_velocity > -0.05832513049244881):
															if(lander_y <= 0.6256686747074127):
																if(angle_velocity <= 0.0064967426005750895):
																	if(lander_x <= 0.042778730392456055):
																		if(x_velocity <= -0.016078908927738667):
																			return True
																else:
																	if(y_velocity <= -0.25620295107364655):
																		return True
																	else:
																		if(y_velocity > -0.2560510039329529):
																			return True
												else:
													if(lander_y <= 0.4490576684474945):
														if(angle > -0.0433986522257328):
															return True
													else:
														if(angle_velocity > 0.005488356575369835):
															if(lander_x > -0.06326909177005291):
																if(x_velocity <= -0.02738816197961569):
																	if(y_velocity <= -0.25114990770816803):
																		return True
											else:
												if(lander_y <= 0.6370363831520081):
													if(y_velocity <= -0.24830061942338943):
														if(angle_velocity <= 0.0023282679030671716):
															if(lander_x <= 0.10510415956377983):
																if(angle_velocity <= 0.0005936576635576785):
																	return True
														else:
															return True
													else:
														if(x_velocity <= -0.04007616080343723):
															if(lander_y <= 0.5664487481117249):
																if(lander_x > 0.0707700252532959):
																	return True
														else:
															if(lander_y <= 0.6330767869949341):
																if(lander_x <= 0.17243342846632004):
																	if(x_velocity <= -0.005723278969526291):
																		return True
																	else:
																		if(angle_velocity > 0.014232780085876584):
																			return True
																else:
																	if(angle <= -3.338768146932125e-05):
																		return True
								else:
									if(angle <= 0.02445459645241499):
										if(angle_velocity <= -0.010594240389764309):
											if(x_velocity > -0.06686000898480415):
												if(lander_x <= -0.0601667407900095):
													if(angle_velocity <= -0.026763037778437138):
														if(y_velocity <= -0.23292602598667145):
															return True
												else:
													if(angle > -0.008313758298754692):
														if(y_velocity <= -0.23741857707500458):
															if(angle > -0.006637597922235727):
																return True
														else:
															if(lander_x > -0.0330034252256155):
																if(x_velocity <= -0.050365911796689034):
																	if(angle_velocity > -0.018073328770697117):
																		return True
																else:
																	if(angle_velocity <= -0.029944712296128273):
																		return True
										else:
											if(x_velocity <= -0.01786466594785452):
												if(lander_x <= 0.1260085552930832):
													if(angle > -0.042609021067619324):
														if(y_velocity <= -0.24284666776657104):
															if(angle > -0.012368390802294016):
																return True
														else:
															if(lander_x > 0.06515040248632431):
																if(x_velocity > -0.036348216235637665):
																	if(y_velocity <= -0.2354392409324646):
																		if(y_velocity <= -0.23693405836820602):
																			if(lander_y <= 0.5332871377468109):
																				return True
																	else:
																		if(angle_velocity <= 0.004569892073050141):
																			return True
												else:
													if(lander_y <= 0.5181255340576172):
														if(y_velocity <= -0.23288510739803314):
															if(lander_x <= 0.1619691401720047):
																return True
											else:
												if(lander_x <= 0.0003012180095538497):
													if(y_velocity <= -0.24066445976495743):
														if(angle > -0.018292360240593553):
															return True
													else:
														if(angle_velocity <= 0.015264656394720078):
															if(y_velocity <= -0.23373811691999435):
																return True
												else:
													if(lander_x > 0.014161825180053711):
														if(angle_velocity <= 0.01480414578691125):
															if(angle_velocity <= 0.003977410204242915):
																return True
														else:
															if(angle > -0.013240710832178593):
																return True
									else:
										if(lander_x > -0.023941373452544212):
											return True
							else:
								if(angle_velocity <= 0.004404015140607953):
									if(lander_y <= 0.889331191778183):
										if(y_velocity <= -0.2563770264387131):
											if(angle <= 0.00019111810252070427):
												if(lander_x > -0.10800261422991753):
													if(lander_y <= 0.6656315922737122):
														if(lander_x > 0.02359118452295661):
															return True
											else:
												if(angle <= 0.04863712377846241):
													if(lander_y > 0.679532527923584):
														if(x_velocity <= -0.007133440347388387):
															return True
										else:
											if(x_velocity <= -0.035182226449251175):
												if(angle > -0.012895056512206793):
													if(angle_velocity > -0.01736298482865095):
														if(y_velocity <= -0.2547205984592438):
															if(x_velocity > -0.055073849856853485):
																return True
											else:
												if(lander_x <= -0.013243150431662798):
													if(angle_velocity <= -0.03206194378435612):
														return True
												else:
													if(angle <= 0.032609907910227776):
														if(angle > 0.018990540876984596):
															if(lander_x <= 0.09156174957752228):
																if(x_velocity > -0.009674486238509417):
																	return True
															else:
																if(lander_y <= 0.8121799826622009):
																	return True
													else:
														if(y_velocity <= -0.24763967841863632):
															return True
								else:
									if(y_velocity <= -0.25405117869377136):
										if(lander_y <= 0.6789322793483734):
											if(angle > -0.03022855520248413):
												return True
										else:
											if(angle > -0.03126440942287445):
												if(angle <= 0.032678719609975815):
													if(y_velocity <= -0.25985635817050934):
														if(y_velocity > -0.25999659299850464):
															return True
												else:
													if(lander_y <= 0.8699574768543243):
														return True
									else:
										if(lander_x > 0.0815114974975586):
											if(lander_x > 0.0852104164659977):
												if(y_velocity <= -0.2509196400642395):
													if(x_velocity > -0.060327403247356415):
														if(lander_y <= 0.7441609501838684):
															return True
						else:
							if(lander_y <= 0.6782035827636719):
								if(y_velocity <= -0.24171631038188934):
									if(angle <= -0.007669943850487471):
										if(angle_velocity <= -0.00637316657230258):
											if(lander_y <= 0.4557790011167526):
												if(y_velocity <= -0.24838769435882568):
													return True
											else:
												if(lander_x <= -0.18014349788427353):
													if(y_velocity <= -0.2494477555155754):
														return True
										else:
											if(angle <= -0.07778352499008179):
												if(angle_velocity <= 0.2345825880765915):
													if(lander_y > 0.45886167883872986):
														if(angle_velocity > 0.202462337911129):
															return True
											else:
												if(angle <= -0.008114891592413187):
													if(angle_velocity <= 0.019101232290267944):
														if(angle > -0.03783738240599632):
															if(angle_velocity <= 0.01796173956245184):
																if(lander_y > 0.4165329188108444):
																	if(lander_y <= 0.5537807047367096):
																		return True
																	else:
																		if(lander_y > 0.6194112002849579):
																			return True
													else:
														if(x_velocity <= 0.028966717422008514):
															if(lander_y <= 0.617910772562027):
																if(lander_y <= 0.5552093386650085):
																	return True
																else:
																	if(y_velocity <= -0.24796930700540543):
																		return True
														else:
															if(y_velocity <= -0.2502943277359009):
																return True
															else:
																if(y_velocity > -0.24990147352218628):
																	if(angle_velocity <= 0.08107097074389458):
																		return True
																	else:
																		if(lander_x <= -0.23189949989318848):
																			return True
																		else:
																			if(lander_y <= 0.5135963261127472):
																				return True
									else:
										if(lander_y <= 0.6139775216579437):
											if(angle_velocity <= -0.030039803124964237):
												if(lander_x <= -0.07439098320901394):
													return True
											else:
												if(angle <= -0.0029058005893602967):
													if(angle <= -0.0031031006947159767):
														if(lander_y <= 0.5822350084781647):
															return True
														else:
															if(x_velocity <= 0.035679278895258904):
																return True
												else:
													if(lander_y <= 0.5913910567760468):
														return True
													else:
														if(lander_y > 0.5915193259716034):
															return True
										else:
											if(angle_velocity <= -0.009488389594480395):
												if(x_velocity <= 0.001788595604011789):
													return True
												else:
													if(y_velocity <= -0.25768475234508514):
														return True
											else:
												if(y_velocity <= -0.24195438623428345):
													if(angle <= 0.010575601365417242):
														if(angle_velocity <= 0.031161028891801834):
															if(x_velocity <= 0.07554014772176743):
																if(angle <= 0.009950333274900913):
																	if(angle_velocity <= 0.019285897724330425):
																		return True
														else:
															return True
													else:
														return True
								else:
									if(angle <= 0.013375560287386179):
										if(angle_velocity <= 0.013561869505792856):
											if(y_velocity <= -0.2267807349562645):
												if(lander_x <= -0.21681082248687744):
													if(angle <= 0.001464070926886052):
														if(x_velocity <= 0.05326969921588898):
															if(angle_velocity <= -0.004545956966467202):
																if(lander_y <= 0.497398242354393):
																	return True
														else:
															if(lander_y <= 0.4434673339128494):
																return True
															else:
																if(x_velocity <= 0.059055546298623085):
																	if(angle_velocity > -0.019966778345406055):
																		return True
													else:
														return True
												else:
													if(lander_y <= 0.4119488000869751):
														if(x_velocity <= 0.009427490178495646):
															return True
													else:
														if(x_velocity <= 0.0024043101584538817):
															if(y_velocity > -0.23941097408533096):
																if(angle_velocity <= -0.0018066087504848838):
																	return True
														else:
															if(lander_x <= -0.1056583859026432):
																if(x_velocity <= 0.05768898129463196):
																	if(angle <= 0.0019282285938970745):
																		if(x_velocity <= 0.05442582629621029):
																			if(lander_x <= -0.18547696620225906):
																				if(x_velocity <= 0.034452106803655624):
																					if(angle <= -0.009836547076702118):
																						return True
																		else:
																			return True
																	else:
																		if(x_velocity > 0.0122235924936831):
																			return True
										else:
											if(y_velocity <= -0.2323838621377945):
												if(angle <= -0.017087535001337528):
													if(angle_velocity > 0.05514552257955074):
														if(lander_x <= -0.13679399341344833):
															if(x_velocity > 0.12649815529584885):
																return True
												else:
													if(lander_y <= 0.5022633373737335):
														if(x_velocity <= 0.014691042713820934):
															if(angle_velocity <= 0.0686153769493103):
																if(lander_y > 0.42673711478710175):
																	return True
														else:
															return True
													else:
														if(angle_velocity <= 0.043021826073527336):
															if(angle_velocity <= 0.03569735586643219):
																if(lander_x <= -0.22361929714679718):
																	return True
																else:
																	if(x_velocity > 0.016786151565611362):
																		if(x_velocity <= 0.06459629163146019):
																			if(lander_y <= 0.5536052584648132):
																				return True
																			else:
																				if(lander_y > 0.6176618039608002):
																					return True
															else:
																if(lander_y > 0.6595658659934998):
																	return True
														else:
															if(lander_x <= -0.25233928859233856):
																if(lander_y <= 0.6343375742435455):
																	return True
															else:
																return True
											else:
												if(y_velocity <= -0.22693373262882233):
													if(angle <= -0.001148426381405443):
														if(lander_x <= -0.05325303040444851):
															if(angle <= -0.02865183725953102):
																if(lander_x <= -0.17642078548669815):
																	if(angle > -0.04011384770274162):
																		return True
														else:
															return True
													else:
														if(x_velocity <= 0.029866842553019524):
															if(lander_y <= 0.48457862436771393):
																return True
														else:
															if(lander_y <= 0.6139527559280396):
																if(lander_y > 0.41525180637836456):
																	return True
															else:
																if(angle_velocity > 0.07019239291548729):
																	if(lander_y > 0.6493671834468842):
																		return True
									else:
										if(angle_velocity <= -0.007965500000864267):
											if(lander_y <= 0.5712693631649017):
												if(angle > 0.015446372795850039):
													if(y_velocity <= -0.23750809580087662):
														return True
													else:
														if(angle <= 0.03104319889098406):
															if(lander_y <= 0.5300270020961761):
																if(angle_velocity <= -0.018493170849978924):
																	if(y_velocity > -0.23020152002573013):
																		return True
																else:
																	return True
														else:
															if(lander_y > 0.42854906618595123):
																return True
											else:
												if(lander_x <= -0.23724763840436935):
													return True
												else:
													if(x_velocity <= 0.05604192614555359):
														if(lander_x <= -0.0666357520967722):
															if(x_velocity > 0.03696584515273571):
																return True
										else:
											if(x_velocity <= 0.06353048235177994):
												if(lander_x <= -0.12678442150354385):
													if(lander_y <= 0.49421779811382294):
														return True
													else:
														if(y_velocity > -0.23695968091487885):
															if(angle <= 0.019469118677079678):
																if(y_velocity > -0.23121558129787445):
																	return True
												else:
													if(y_velocity <= -0.22701957821846008):
														if(lander_y <= 0.585104376077652):
															if(angle_velocity <= 0.01406114175915718):
																if(lander_x <= 0.05004258011467755):
																	return True
															else:
																return True
														else:
															if(lander_y > 0.5877785384654999):
																if(angle <= 0.032382840290665627):
																	return True
													else:
														if(y_velocity > -0.2264140397310257):
															return True
											else:
												if(angle_velocity <= 0.007223339751362801):
													if(angle <= 0.03302682004868984):
														if(x_velocity <= 0.08436202630400658):
															return True
														else:
															if(angle_velocity <= -0.0061489667277783155):
																return True
													else:
														return True
												else:
													if(angle <= 0.014735022094100714):
														if(lander_x > -0.21026001125574112):
															return True
													else:
														if(y_velocity <= -0.2248585820198059):
															if(angle_velocity <= 0.014313715510070324):
																if(lander_x > -0.2393665760755539):
																	return True
															else:
																return True
														else:
															if(angle_velocity <= 0.055678676813840866):
																return True
							else:
								if(angle <= 0.10295573249459267):
									if(angle_velocity <= 0.042507754638791084):
										if(y_velocity <= -0.24878141283988953):
											if(lander_y <= 0.8880913555622101):
												if(angle <= -0.008234894834458828):
													if(angle_velocity <= 0.033598922193050385):
														if(x_velocity > 0.07583780214190483):
															return True
													else:
														if(angle > -0.022935448214411736):
															return True
												else:
													if(angle_velocity <= -0.009366677608340979):
														if(angle <= 0.03616303578019142):
															if(x_velocity <= 0.011128692887723446):
																if(lander_x > -0.0501461997628212):
																	return True
														else:
															return True
													else:
														if(lander_x <= -0.05180711857974529):
															if(lander_y <= 0.7781370282173157):
																if(angle_velocity > -0.0005504920845851302):
																	if(angle > -0.0077021608594805):
																		return True
															else:
																if(x_velocity > 0.02442897390574217):
																	if(y_velocity <= -0.2541348934173584):
																		return True
														else:
															return True
											else:
												if(angle > 0.03284945897758007):
													if(x_velocity <= 0.052442971616983414):
														if(lander_x <= 0.1016031764447689):
															if(lander_y <= 1.1686013340950012):
																if(angle_velocity <= 0.014928619842976332):
																	if(x_velocity <= 0.01401378819718957):
																		if(angle_velocity > -0.01967438729479909):
																			return True
																	else:
																		if(x_velocity <= 0.03209437523037195):
																			if(lander_y <= 0.9470468163490295):
																				return True
																		else:
																			return True
														else:
															if(angle_velocity > -0.023328247480094433):
																return True
													else:
														if(y_velocity <= -0.25468458235263824):
															if(angle_velocity <= 0.0397985614836216):
																return True
														else:
															if(angle > 0.10042272508144379):
																return True
										else:
											if(lander_y <= 0.8257634937763214):
												if(angle_velocity <= -0.007427188102155924):
													if(angle_velocity > -0.010084525682032108):
														if(angle_velocity <= -0.009553197305649519):
															return True
												else:
													if(x_velocity <= 0.043249502778053284):
														if(y_velocity <= -0.2370046228170395):
															if(x_velocity > 0.010765003971755505):
																if(lander_x > -0.16030530631542206):
																	if(y_velocity <= -0.23792554438114166):
																		if(lander_y <= 0.7956951260566711):
																			if(angle <= 0.0006219688802957535):
																				if(y_velocity <= -0.2414242923259735):
																					return True
																			else:
																				return True
													else:
														if(angle <= 0.03740200214087963):
															if(angle_velocity > 0.03658078983426094):
																if(lander_x > -0.35036981105804443):
																	return True
														else:
															return True
											else:
												if(angle <= 0.029133042320609093):
													if(x_velocity <= 0.02190345898270607):
														if(y_velocity <= -0.24772899597883224):
															return True
									else:
										if(x_velocity <= 0.1433681845664978):
											if(lander_y <= 0.7128623425960541):
												if(y_velocity <= -0.23475246876478195):
													if(x_velocity <= 0.04234972223639488):
														if(lander_x > -0.11548614501953125):
															if(x_velocity <= 0.030800731852650642):
																return True
													else:
														if(angle_velocity <= 0.13825778663158417):
															if(lander_x > -0.3019168972969055):
																if(angle_velocity <= 0.06672092899680138):
																	if(angle <= -0.00637528661172837):
																		if(y_velocity > -0.24509673565626144):
																			if(angle <= -0.015334553085267544):
																				return True
																	else:
																		return True
																else:
																	return True
											else:
												if(y_velocity <= -0.24383505433797836):
													if(angle > -0.04584505222737789):
														if(lander_y <= 0.7992344200611115):
															if(x_velocity <= 0.05489739216864109):
																if(lander_y <= 0.781582772731781):
																	if(x_velocity > 0.04552813433110714):
																		if(angle > -0.03147723991423845):
																			return True
																else:
																	if(y_velocity <= -0.24961332231760025):
																		return True
															else:
																return True
														else:
															if(lander_x <= -0.338242769241333):
																return True
															else:
																if(lander_y <= 1.4189164638519287):
																	if(y_velocity <= -0.24742591381072998):
																		if(x_velocity <= 0.016765374690294266):
																			if(y_velocity <= -0.2541370987892151):
																				return True
																else:
																	if(x_velocity > 0.1303340345621109):
																		if(lander_y <= 1.4234117269515991):
																			return True
												else:
													if(x_velocity > 0.13658814877271652):
														return True
										else:
											if(angle_velocity <= 0.06932657957077026):
												return True
								else:
									if(y_velocity <= -0.23747292160987854):
										if(angle <= 0.4293469339609146):
											if(lander_x <= 0.05115861818194389):
												if(x_velocity <= 0.13500040024518967):
													if(angle <= 0.11096933484077454):
														if(lander_y <= 1.2102004885673523):
															return True
														else:
															if(x_velocity > 0.11366458982229233):
																return True
												else:
													if(lander_y <= 1.4222301244735718):
														if(lander_x <= 0.03817935101687908):
															if(lander_x <= 0.036213064566254616):
																return True
														else:
															return True
											else:
												if(angle <= 0.3634513318538666):
													if(lander_x <= 0.069710873067379):
														if(lander_x <= 0.0687967799603939):
															if(angle_velocity > -0.027906393632292747):
																if(y_velocity > -0.2599165290594101):
																	if(lander_y <= 1.4051954746246338):
																		if(lander_x <= 0.05755038373172283):
																			if(lander_x <= 0.057309580966830254):
																				if(angle <= 0.13579915463924408):
																					if(x_velocity <= 0.14063924551010132):
																						return True
																				else:
																					return True
																		else:
																			return True
																	else:
																		if(angle <= 0.14150158315896988):
																			if(x_velocity <= 0.21210245043039322):
																				if(x_velocity <= 0.16459538042545319):
																					if(y_velocity <= -0.25008321553468704):
																						return True
																				else:
																					return True
														else:
															if(lander_y <= 1.187575101852417):
																return True
													else:
														return True
												else:
													if(y_velocity <= -0.24047396332025528):
														if(angle <= 0.3823806792497635):
															if(y_velocity <= -0.2507116347551346):
																return True
														else:
															if(x_velocity > 0.12505142763257027):
																if(y_velocity <= -0.2495308592915535):
																	return True
																else:
																	if(y_velocity > -0.2468038946390152):
																		return True
										else:
											if(x_velocity <= 0.24664103984832764):
												if(angle <= 0.4505787491798401):
													if(angle > 0.43866419792175293):
														return True
											else:
												return True
									else:
										if(x_velocity > 0.12892448157072067):
											if(angle <= 0.3770904541015625):
												if(lander_y <= 1.356264591217041):
													if(angle <= 0.2588009312748909):
														if(lander_x > 0.05328202247619629):
															if(lander_y <= 1.3061116337776184):
																if(y_velocity <= -0.22721433639526367):
																	return True
																else:
																	if(x_velocity > 0.17450890690088272):
																		return True
															else:
																if(lander_y > 1.3299434185028076):
																	return True
													else:
														if(x_velocity <= 0.2344096377491951):
															if(lander_x > 0.1925528571009636):
																return True
														else:
															return True
												else:
													if(y_velocity <= -0.2308005914092064):
														if(x_velocity > 0.13182853162288666):
															if(y_velocity <= -0.23138921707868576):
																if(angle > 0.16412196308374405):
																	if(x_velocity <= 0.1717679351568222):
																		return True
																	else:
																		if(x_velocity > 0.20298302918672562):
																			return True
													else:
														return True
											else:
												if(x_velocity > 0.3085941970348358):
													return True
		else:
			if(angle_velocity <= -0.01109519088640809):
				if(right_leg_contact != True):
					if(lander_y <= 0.5234372615814209):
						if(y_velocity <= -0.1971578523516655):
							if(angle <= 0.0107335583306849):
								if(x_velocity <= -0.04500272683799267):
									if(angle_velocity <= -0.03327598422765732):
										if(angle <= -0.008505767676979303):
											if(y_velocity <= -0.20618872344493866):
												if(x_velocity > -0.08068354055285454):
													if(lander_x > -0.16330795362591743):
														if(angle_velocity > -0.04211241379380226):
															if(lander_y <= 0.05079450458288193):
																return True
										else:
											if(lander_y <= 0.21201618760824203):
												if(angle_velocity <= -0.06125285662710667):
													if(lander_x <= 0.07096729148179293):
														return True
												else:
													return True
									else:
										if(lander_x > -0.04515476152300835):
											if(lander_y <= 0.08018750697374344):
												if(y_velocity <= -0.2137577161192894):
													return True
											else:
												if(y_velocity <= -0.2175784334540367):
													if(lander_y <= 0.3196537494659424):
														if(x_velocity > -0.05980289727449417):
															if(angle_velocity > -0.013619365636259317):
																return True
								else:
									if(angle_velocity <= -0.03873600624501705):
										if(angle <= 0.009614271577447653):
											if(lander_y <= 0.38996393978595734):
												if(y_velocity <= -0.2237100526690483):
													if(lander_y > 0.11958654969930649):
														return True
												else:
													if(lander_y <= 0.04265764728188515):
														if(angle_velocity <= -0.05158418416976929):
															if(angle > -0.003320852294564247):
																if(lander_y <= 0.011282346211373806):
																	return True
														else:
															if(lander_y > 0.01953489612787962):
																if(angle > -0.017878013662993908):
																	return True
													else:
														if(angle > -0.0033316476037725806):
															if(angle <= -0.0019331203075125813):
																if(lander_x > -0.11544475331902504):
																	if(angle_velocity > -0.048041269183158875):
																		return True
															else:
																if(y_velocity <= -0.21046802401542664):
																	if(y_velocity <= -0.21110012382268906):
																		if(angle <= 0.008313753642141819):
																			if(angle_velocity > -0.04226374626159668):
																				if(lander_x > -0.03500175569206476):
																					return True
																		else:
																			if(lander_x <= -0.05994052952155471):
																				return True
																	else:
																		return True
										else:
											if(lander_y <= 0.49673160910606384):
												if(x_velocity > 0.023714778944849968):
													if(angle > 0.01028698030859232):
														return True
									else:
										if(angle <= -0.017591786570847034):
											if(lander_x <= -0.06204400025308132):
												if(x_velocity <= -0.009615412447601557):
													if(angle <= -0.022226118482649326):
														if(lander_x > -0.17760396003723145):
															if(angle > -0.030797327868640423):
																if(y_velocity <= -0.20748993754386902):
																	if(lander_y <= 0.16800661385059357):
																		return True
												else:
													if(angle <= -0.04703420028090477):
														return True
													else:
														if(lander_y <= 0.0005610740336123854):
															return True
														else:
															if(angle_velocity <= -0.011851252987980843):
																if(y_velocity <= -0.22352906316518784):
																	if(angle > -0.02740698680281639):
																		return True
																else:
																	if(x_velocity <= -0.007450368953868747):
																		if(angle_velocity > -0.017297599464654922):
																			return True
															else:
																return True
										else:
											if(lander_y <= 0.3056928813457489):
												if(y_velocity <= -0.2121613472700119):
													if(lander_y <= 0.17421792447566986):
														if(x_velocity <= 0.06556670367717743):
															if(angle <= -0.007533589843660593):
																if(y_velocity <= -0.21823590248823166):
																	return True
																else:
																	if(angle <= -0.014045950025320053):
																		return True
															else:
																if(angle <= 0.007243534550070763):
																	return True
																else:
																	if(x_velocity <= 0.04306749999523163):
																		return True
													else:
														if(y_velocity <= -0.21849275380373):
															if(lander_x <= -0.2251472920179367):
																return True
															else:
																if(x_velocity <= 0.042945344001054764):
																	if(lander_x <= -0.060500429943203926):
																		if(x_velocity > -0.042161500081419945):
																			return True
																	else:
																		if(x_velocity <= -0.010808070888742805):
																			return True
														else:
															if(x_velocity <= 0.014525707345455885):
																if(angle <= -0.003087206627242267):
																	return True
															else:
																if(lander_y > 0.2945549488067627):
																	return True
												else:
													if(lander_y <= 0.02314615063369274):
														if(x_velocity <= 0.03162580728530884):
															return True
													else:
														if(lander_x <= 0.014187526423484087):
															if(x_velocity <= -0.001215156189573463):
																if(angle > 0.0037311719497665763):
																	return True
															else:
																if(angle <= -0.0017017050413414836):
																	if(angle_velocity <= -0.013581103645265102):
																		if(angle_velocity > -0.020318916998803616):
																			if(angle_velocity <= -0.01922200620174408):
																				return True
																	else:
																		if(x_velocity <= 0.04162782244384289):
																			if(lander_x > -0.23897194862365723):
																				return True
																else:
																	if(lander_y <= 0.11638302728533745):
																		if(lander_x <= -0.08995795249938965):
																			if(x_velocity <= 0.08517949283123016):
																				return True
																	else:
																		if(angle > 0.006933571537956595):
																			if(y_velocity > -0.20877941697835922):
																				return True
														else:
															if(angle_velocity <= -0.03484294191002846):
																if(x_velocity <= -0.016145913861691952):
																	return True
											else:
												if(lander_x <= -0.02732639294117689):
													if(x_velocity > 0.04054240509867668):
														if(angle <= 0.009536838624626398):
															if(lander_x > -0.21133217215538025):
																return True
							else:
								if(angle_velocity <= -0.06347468122839928):
									if(angle <= 0.11405843868851662):
										if(lander_y <= 0.1087837889790535):
											if(lander_y <= 0.06165244244039059):
												if(y_velocity <= -0.21278832107782364):
													return True
											else:
												return True
										else:
											if(angle > 0.052092377096414566):
												if(y_velocity <= -0.2149878814816475):
													return True
												else:
													if(y_velocity <= -0.2003796547651291):
														if(angle <= 0.058106908574700356):
															if(y_velocity <= -0.20573554933071136):
																return True
									else:
										if(angle <= 0.18815135210752487):
											return True
								else:
									if(lander_y <= 0.15496191382408142):
										if(y_velocity <= -0.20434628427028656):
											if(angle <= 0.02040480077266693):
												if(y_velocity <= -0.21522805094718933):
													if(angle_velocity <= -0.05080771818757057):
														if(y_velocity > -0.22017275542020798):
															return True
													else:
														return True
												else:
													if(lander_x <= 0.059494875371456146):
														if(x_velocity <= 0.01969167683273554):
															return True
														else:
															if(lander_x <= -0.14242224395275116):
																return True
											else:
												if(x_velocity <= 0.08594369143247604):
													if(angle_velocity <= -0.012429318856447935):
														return True
													else:
														if(angle > 0.02965648379176855):
															return True
												else:
													if(y_velocity <= -0.20771224051713943):
														return True
										else:
											if(angle_velocity <= -0.031124630942940712):
												if(angle <= 0.04484415240585804):
													if(lander_y <= 0.03519080579280853):
														if(y_velocity <= -0.19916348904371262):
															return True
													else:
														if(y_velocity > -0.19731296598911285):
															return True
												else:
													return True
											else:
												if(angle <= 0.020403779111802578):
													if(y_velocity > -0.2004377841949463):
														if(y_velocity > -0.19963639229536057):
															return True
												else:
													return True
									else:
										if(angle <= 0.042803024873137474):
											if(y_velocity <= -0.21623970568180084):
												if(lander_y <= 0.34502965211868286):
													if(angle_velocity <= -0.036895280703902245):
														if(y_velocity <= -0.22144688665866852):
															return True
														else:
															if(lander_y <= 0.21191608905792236):
																return True
															else:
																if(lander_y > 0.3218018412590027):
																	return True
													else:
														if(y_velocity <= -0.21681158244609833):
															return True
														else:
															if(lander_x <= 0.08846440352499485):
																return True
												else:
													if(angle <= 0.02758010569959879):
														if(x_velocity <= -0.01779560884460807):
															if(angle_velocity > -0.03028054442256689):
																return True
														else:
															if(x_velocity <= -0.0012674953613895923):
																if(lander_x <= 0.03411898575723171):
																	return True
													else:
														if(x_velocity <= 0.09785904735326767):
															if(lander_x <= -0.13933706283569336):
																return True
															else:
																if(angle_velocity > -0.02688912022858858):
																	if(lander_x > -0.072903823107481):
																		return True
											else:
												if(x_velocity <= 0.06280925124883652):
													if(lander_y <= 0.3163684159517288):
														if(lander_x <= 0.025122356601059437):
															if(angle_velocity > -0.04699285887181759):
																if(y_velocity <= -0.20552700757980347):
																	if(angle > 0.01394487265497446):
																		if(x_velocity <= 0.056929245591163635):
																			return True
																		else:
																			if(lander_y > 0.19123990833759308):
																				return True
																else:
																	if(angle > 0.029211956076323986):
																		return True
														else:
															if(x_velocity > -0.03566419705748558):
																if(angle_velocity <= -0.01410002913326025):
																	if(y_velocity <= -0.21473976969718933):
																		return True
																else:
																	return True
													else:
														if(y_velocity > -0.21319089084863663):
															if(x_velocity > 0.05624804459512234):
																if(y_velocity <= -0.21005799621343613):
																	return True
												else:
													if(y_velocity <= -0.20755164325237274):
														if(lander_y <= 0.17654933035373688):
															return True
														else:
															if(lander_x <= -0.1600053757429123):
																if(angle > 0.02932643610984087):
																	return True
															else:
																if(angle_velocity > -0.01821210514754057):
																	if(angle_velocity <= -0.018008616752922535):
																		return True
										else:
											if(y_velocity <= -0.19896094501018524):
												if(angle <= 0.06532834470272064):
													if(angle_velocity <= -0.03555918484926224):
														if(x_velocity <= 0.09161169081926346):
															if(lander_x <= -0.08843240514397621):
																if(x_velocity > 0.04285657778382301):
																	return True
															else:
																if(x_velocity <= 0.02752626407891512):
																	if(lander_x > -0.00529823312535882):
																		return True
																else:
																	if(x_velocity > 0.07643027231097221):
																		return True
														else:
															if(lander_x <= -0.25998570024967194):
																if(lander_x > -0.2754611521959305):
																	return True
													else:
														if(lander_y <= 0.4755209684371948):
															if(x_velocity <= 0.15868263691663742):
																if(y_velocity <= -0.20105457305908203):
																	if(x_velocity <= 0.10151506215333939):
																		if(y_velocity <= -0.20671191811561584):
																			return True
																		else:
																			if(y_velocity > -0.20404434949159622):
																				return True
																	else:
																		if(lander_x <= -0.18458478152751923):
																			return True
																else:
																	if(y_velocity > -0.19981536269187927):
																		return True
												else:
													return True
											else:
												if(angle_velocity <= -0.025362825952470303):
													if(x_velocity <= 0.06007133238017559):
														if(lander_x <= 0.0679500075057149):
															return True
													else:
														if(angle_velocity <= -0.043294887989759445):
															if(y_velocity > -0.19818031042814255):
																return True
												else:
													return True
						else:
							if(x_velocity <= 0.0011435417691245675):
								if(lander_x > 0.015800190158188343):
									if(angle_velocity <= -0.04469680041074753):
										if(lander_y <= 0.10058356449007988):
											if(lander_y <= 0.0019821441455860622):
												if(y_velocity <= -0.17780404537916183):
													return True
									else:
										if(x_velocity <= -0.023783325217664242):
											if(angle > -0.010971731040626764):
												if(angle > 0.03952940180897713):
													if(x_velocity <= -0.028548584319651127):
														return True
										else:
											if(angle <= 0.025992137379944324):
												if(angle_velocity <= -0.013786638621240854):
													if(y_velocity <= -0.19353199750185013):
														if(lander_x <= 0.10590395703911781):
															return True
											else:
												if(lander_y <= 0.4093811511993408):
													if(y_velocity <= -0.18997720628976822):
														if(x_velocity > -0.008326976094394922):
															if(angle <= 0.03605004400014877):
																return True
							else:
								if(y_velocity <= -0.15708663314580917):
									if(angle <= 0.055927980691194534):
										if(angle_velocity <= -0.029996730387210846):
											if(lander_y <= 0.22265808284282684):
												if(x_velocity <= 0.05057523027062416):
													if(lander_x <= 0.003647613455541432):
														if(angle <= 0.03232170734554529):
															if(x_velocity > 0.01392990630120039):
																if(x_velocity <= 0.04961695522069931):
																	if(x_velocity > 0.04707523062825203):
																		if(lander_y > 0.0654207319021225):
																			return True
														else:
															if(angle > 0.037334516644477844):
																if(angle_velocity > -0.0630903709679842):
																	return True
										else:
											if(angle <= 0.0255026426166296):
												if(lander_x <= -0.04367666319012642):
													if(x_velocity > 0.01822946034371853):
														if(angle_velocity > -0.028262783773243427):
															if(angle_velocity <= -0.01770548801869154):
																if(y_velocity <= -0.1745178923010826):
																	if(lander_x > -0.22383809089660645):
																		if(angle > 0.014435872435569763):
																			if(x_velocity <= 0.04773258417844772):
																				return True
											else:
												if(y_velocity <= -0.18513454496860504):
													if(lander_y <= 0.22858544439077377):
														if(x_velocity <= 0.09050897136330605):
															if(lander_x <= 0.14186649024486542):
																if(x_velocity <= 0.03864736296236515):
																	if(x_velocity <= 0.03466221131384373):
																		if(angle <= 0.04619345813989639):
																			return True
																else:
																	return True
														else:
															if(y_velocity > -0.19011235982179642):
																return True
												else:
													if(x_velocity <= 0.0833539068698883):
														if(angle_velocity <= -0.013280750252306461):
															if(x_velocity <= 0.029910244047641754):
																if(x_velocity > 0.018781989812850952):
																	if(angle_velocity <= -0.01790214516222477):
																		return True
															else:
																if(lander_x <= -0.06425094604492188):
																	if(angle_velocity <= -0.014119629748165607):
																		if(lander_y <= 0.08994792401790619):
																			if(angle > 0.037441227585077286):
																				return True
									else:
										if(y_velocity <= -0.18687207251787186):
											if(lander_y <= 0.3379046618938446):
												if(lander_x <= -0.13328032940626144):
													return True
												else:
													if(x_velocity <= 0.10170841962099075):
														if(lander_y <= 0.2902415916323662):
															return True
													else:
														if(angle > 0.07501555234193802):
															return True
											else:
												if(angle_velocity <= -0.016473854891955853):
													if(angle_velocity <= -0.05001203343272209):
														if(lander_y > 0.4006785899400711):
															if(angle_velocity > -0.11767267063260078):
																if(y_velocity <= -0.19001012295484543):
																	return True
																else:
																	if(angle_velocity > -0.05983622930943966):
																		return True
												else:
													return True
										else:
											if(lander_y <= 0.1910877674818039):
												if(angle_velocity > -0.056722452864050865):
													if(lander_x <= -0.04229102050885558):
														return True
													else:
														if(lander_x > 0.018885421566665173):
															return True
											else:
												if(x_velocity <= 0.11261632665991783):
													if(lander_y <= 0.255778931081295):
														if(x_velocity <= 0.08044421672821045):
															if(angle > 0.06523803994059563):
																return True
												else:
													if(x_velocity <= 0.17195049673318863):
														if(lander_y <= 0.4196188747882843):
															if(angle_velocity <= -0.06635932996869087):
																if(angle <= 0.08471350744366646):
																	return True
														else:
															if(angle_velocity > -0.08727699518203735):
																if(x_velocity > 0.14947761595249176):
																	if(x_velocity <= 0.169244222342968):
																		if(y_velocity <= -0.18446720391511917):
																			return True
													else:
														return True
					else:
						if(x_velocity <= 0.1182720772922039):
							if(lander_y <= 1.4159489870071411):
								if(x_velocity > -0.2558598518371582):
									if(angle > 0.015097778290510178):
										if(angle_velocity <= -0.03397380746901035):
											if(lander_y > 0.6864185929298401):
												if(x_velocity <= 0.058617839589715004):
													if(angle_velocity > -0.37056033313274384):
														if(x_velocity > 0.012419880833476782):
															if(angle_velocity <= -0.2228338047862053):
																if(angle_velocity > -0.27831925451755524):
																	return True
												else:
													if(y_velocity <= -0.2002694457769394):
														if(angle_velocity <= -0.1456744521856308):
															if(y_velocity <= -0.2088509127497673):
																if(angle_velocity > -0.31164443492889404):
																	if(angle <= 0.20877940952777863):
																		if(angle <= 0.2042865976691246):
																			return True
																	else:
																		return True
														else:
															if(lander_x <= 0.11833129078149796):
																if(angle <= 0.15269678831100464):
																	if(angle_velocity > -0.04049842804670334):
																		return True
																else:
																	if(angle_velocity > -0.09067074954509735):
																		if(angle_velocity > -0.05935409851372242):
																			return True
										else:
											if(lander_y <= 0.5836990177631378):
												if(x_velocity > 0.057437339797616005):
													if(y_velocity <= -0.20619171857833862):
														if(x_velocity <= 0.05988443270325661):
															return True
						else:
							if(lander_x > 0.08426184579730034):
								if(y_velocity <= -0.17774006724357605):
									if(y_velocity <= -0.2086435928940773):
										if(x_velocity <= 0.1553923711180687):
											if(lander_y <= 1.1958619356155396):
												if(y_velocity > -0.22336044907569885):
													return True
											else:
												if(y_velocity <= -0.22044707089662552):
													return True
										else:
											if(angle <= 0.2830250412225723):
												if(angle_velocity > -0.05138550139963627):
													return True
											else:
												return True
									else:
										if(x_velocity <= 0.27152805030345917):
											if(angle_velocity <= -0.05723921023309231):
												if(lander_x <= 0.15445046871900558):
													if(angle_velocity > -0.0723775066435337):
														if(angle_velocity <= -0.0646637212485075):
															return True
												else:
													if(angle_velocity <= -0.16303861886262894):
														if(angle > 0.34828269481658936):
															if(angle_velocity <= -0.20622273534536362):
																return True
													else:
														if(x_velocity <= 0.23525077104568481):
															if(lander_x <= 0.22326912730932236):
																if(angle_velocity <= -0.14127739518880844):
																	return True
																else:
																	if(angle_velocity <= -0.0871920995414257):
																		if(lander_y > 1.3360260725021362):
																			return True
																	else:
																		return True
														else:
															return True
											else:
												if(lander_x <= 0.10068545490503311):
													return True
										else:
											if(angle <= 0.4899993985891342):
												return True
											else:
												if(lander_x <= 0.25046396255493164):
													return True
								else:
									if(x_velocity > 0.29067718982696533):
										return True
			else:
				if(y_velocity <= -0.19208889454603195):
					if(lander_y <= 0.2897540479898453):
						if(angle <= -0.001974301296286285):
							if(x_velocity <= -0.01461441582068801):
								if(lander_y <= 0.00980702368542552):
									if(angle_velocity > -0.005119665991514921):
										if(right_leg_contact != True):
											if(lander_y <= 0.004544887458905578):
												return True
											else:
												if(lander_y > 0.006062713917344809):
													return True
								else:
									if(y_velocity <= -0.21065139770507812):
										if(lander_y <= 0.16549677401781082):
											if(angle <= -0.03493528999388218):
												if(x_velocity <= -0.03977541998028755):
													if(angle_velocity <= -0.0024486881447955966):
														if(angle_velocity > -0.005835844436660409):
															return True
													else:
														if(lander_x <= 0.0528874397277832):
															if(lander_y <= 0.05295024998486042):
																if(y_velocity <= -0.2188088223338127):
																	if(y_velocity > -0.22296956926584244):
																		return True
														else:
															return True
												else:
													if(lander_x <= -0.11710600554943085):
														if(angle_velocity > -0.004093042458407581):
															if(y_velocity <= -0.22099005430936813):
																if(lander_y > 0.06058395840227604):
																	return True
													else:
														if(angle > -0.0471199844032526):
															if(lander_y <= 0.1439994052052498):
																if(lander_x <= 0.047720860689878464):
																	return True
											else:
												if(lander_y <= 0.07413315400481224):
													return True
												else:
													if(y_velocity <= -0.21574554592370987):
														if(lander_x > -0.0669793114066124):
															if(angle_velocity <= -0.005755024263635278):
																if(angle <= -0.024487187154591084):
																	return True
															else:
																return True
													else:
														if(angle > -0.02462300844490528):
															if(y_velocity > -0.21370692551136017):
																if(lander_x > 0.02692174818366766):
																	return True
										else:
											if(angle <= -0.024513673037290573):
												if(lander_x <= 0.11286602169275284):
													if(y_velocity <= -0.22343513369560242):
														if(lander_x <= -0.02529301680624485):
															return True
											else:
												if(y_velocity <= -0.22127367556095123):
													return True
												else:
													if(angle_velocity > 0.03473819978535175):
														if(angle <= -0.015831599477678537):
															return True
														else:
															if(angle > -0.00635238247923553):
																return True
									else:
										if(x_velocity <= -0.025622901506721973):
											if(angle > -0.047295982018113136):
												if(lander_y <= 0.014223549049347639):
													return True
										else:
											if(angle_velocity <= 0.00881808646954596):
												if(lander_x > -0.121637724339962):
													if(angle_velocity <= -0.008143778424710035):
														return True
							else:
								if(lander_y <= 0.17636018991470337):
									if(y_velocity <= -0.20780175924301147):
										if(angle <= -0.029647454619407654):
											if(x_velocity <= 0.004933268181048334):
												if(angle <= -0.03637485392391682):
													if(angle > -0.04454756900668144):
														if(lander_x <= -0.05945158191025257):
															return True
												else:
													if(angle_velocity > -0.006891900207847357):
														if(lander_x > -0.07776127010583878):
															return True
											else:
												if(lander_x > -0.244578555226326):
													if(lander_x <= -0.19666409492492676):
														if(angle > -0.049405982717871666):
															if(x_velocity <= 0.024441578425467014):
																return True
															else:
																if(lander_y > 0.08263836614787579):
																	return True
										else:
											if(angle_velocity <= -0.0058912960812449455):
												if(x_velocity <= 0.0614925604313612):
													if(angle > -0.012152002658694983):
														return True
											else:
												if(angle <= -0.002356428885832429):
													if(y_velocity <= -0.2082531675696373):
														if(angle_velocity <= 0.017753158695995808):
															if(angle_velocity <= 0.014326295349746943):
																if(lander_y > 0.003790936549194157):
																	if(x_velocity <= 0.0821458138525486):
																		if(angle_velocity <= 0.012988659553229809):
																			return True
																		else:
																			if(lander_x <= -0.11444887891411781):
																				return True
															else:
																if(lander_x <= -0.10722851753234863):
																	if(lander_y <= 0.08121594041585922):
																		return True
														else:
															if(lander_x <= 0.02890787087380886):
																return True
															else:
																if(lander_x > 0.02928457222878933):
																	return True
													else:
														if(y_velocity > -0.20811493694782257):
															return True
									else:
										if(angle_velocity <= 0.014084470458328724):
											if(angle > -0.018581273965537548):
												if(x_velocity <= 0.04151764698326588):
													if(lander_x <= -0.08645911142230034):
														if(angle > -0.006798464106395841):
															return True
													else:
														if(x_velocity <= 0.0019716447714017704):
															return True
												else:
													if(angle <= -0.009684664197266102):
														return True
													else:
														if(angle <= -0.0025655411882326007):
															if(x_velocity <= 0.05394873768091202):
																if(lander_y > 0.07882348075509071):
																	return True
														else:
															return True
										else:
											if(lander_y <= 0.08455385640263557):
												if(angle_velocity > 0.01682453602552414):
													if(lander_y <= 0.022858796641230583):
														return True
													else:
														if(angle > -0.03435870446264744):
															if(x_velocity > -0.005795223638415337):
																if(y_velocity <= -0.1949629932641983):
																	if(y_velocity <= -0.20029407739639282):
																		return True
																	else:
																		if(lander_x <= -0.13982105255126953):
																			if(lander_x <= -0.18819518387317657):
																				return True
																		else:
																			return True
											else:
												if(x_velocity <= 0.06846123188734055):
													if(lander_x <= 0.10798463970422745):
														if(x_velocity > 0.01650381088256836):
															if(angle_velocity <= 0.0359306912869215):
																return True
												else:
													return True
								else:
									if(y_velocity <= -0.21350980550050735):
										if(lander_y <= 0.22156928479671478):
											if(x_velocity <= 0.0022984480601735413):
												if(lander_y <= 0.18454410880804062):
													return True
											else:
												if(angle_velocity > -0.0065377524588257074):
													if(angle <= -0.0063004810363054276):
														return True
										else:
											if(angle_velocity <= 0.00941420067101717):
												if(angle > -0.00994016882032156):
													if(y_velocity <= -0.21747388690710068):
														return True
											else:
												if(x_velocity <= 0.04361279867589474):
													if(lander_x <= 0.01591725368052721):
														if(y_velocity <= -0.2211196944117546):
															if(angle_velocity > 0.015095389913767576):
																return True
													else:
														if(y_velocity <= -0.21712232381105423):
															if(lander_y <= 0.24246787279844284):
																return True
												else:
													if(angle > -0.014380637090653181):
														return True
									else:
										if(angle_velocity > 0.010462206788361073):
											if(x_velocity > 0.05154911056160927):
												if(x_velocity <= 0.056840525940060616):
													if(x_velocity <= 0.05473960563540459):
														return True
						else:
							if(right_leg_contact != True):
								if(y_velocity <= -0.20635643601417542):
									if(x_velocity <= -0.027317581698298454):
										if(y_velocity <= -0.20972612500190735):
											if(y_velocity > -0.22286126762628555):
												if(angle_velocity <= 0.020856578834354877):
													return True
												else:
													if(angle_velocity > 0.025851380079984665):
														return True
									else:
										if(angle <= 0.10114578157663345):
											if(lander_x > -0.2811438590288162):
												if(angle <= 0.018739018589258194):
													if(angle_velocity <= -0.005446673603728414):
														if(lander_x <= 0.04728131368756294):
															if(angle_velocity <= -0.006448284490033984):
																if(x_velocity <= 0.04670148901641369):
																	if(lander_x <= 0.014701509848237038):
																		return True
																	else:
																		if(lander_y > 0.0636820551007986):
																			return True
													else:
														if(angle <= 0.018694463185966015):
															if(lander_y <= 0.2418917417526245):
																if(lander_x <= 0.15335922688245773):
																	if(lander_x <= -0.2490876391530037):
																		if(lander_x <= -0.2502325177192688):
																			return True
																	else:
																		if(x_velocity <= 0.05325937829911709):
																			return True
																		else:
																			if(lander_x <= 0.01578388176858425):
																				if(angle_velocity <= 0.012258684262633324):
																					if(lander_x <= -0.14829573407769203):
																						return True
																				else:
																					return True
																else:
																	if(lander_y > 0.2299494370818138):
																		return True
															else:
																if(y_velocity <= -0.21332582831382751):
																	if(angle_velocity > 0.0018679435597732663):
																		return True
																else:
																	if(lander_y > 0.2714949995279312):
																		if(lander_y <= 0.2775247097015381):
																			return True
												else:
													if(y_velocity <= -0.207355335354805):
														if(lander_y <= 0.2796950787305832):
															return True
														else:
															if(lander_y > 0.28052231669425964):
																return True
													else:
														if(x_velocity <= 0.12062624469399452):
															if(angle_velocity <= 0.03943806141614914):
																return True
								else:
									if(angle <= 0.027642766945064068):
										if(lander_y <= 0.11291278526186943):
											if(x_velocity <= -0.009744551964104176):
												if(angle > 0.010740743018686771):
													if(lander_y <= 0.07252175360918045):
														return True
											else:
												if(lander_x <= 0.038906002417206764):
													if(angle <= 0.026989192701876163):
														if(x_velocity <= -0.0020548300817608833):
															if(angle_velocity <= 0.0316975973546505):
																return True
														else:
															if(angle_velocity <= -0.004507679492235184):
																if(angle_velocity <= -0.004781218944117427):
																	return True
															else:
																if(angle <= 0.0025926113594323397):
																	if(angle <= 0.0023132554488256574):
																		return True
																else:
																	return True
													else:
														if(lander_x > -0.04813614021986723):
															return True
												else:
													if(angle_velocity > 0.0020055713539477438):
														if(lander_x > 0.07076811790466309):
															if(x_velocity <= 0.03445328865200281):
																return True
										else:
											if(angle <= 0.011901159305125475):
												if(angle_velocity <= 0.020643576979637146):
													if(angle <= 0.00960160605609417):
														if(y_velocity <= -0.1995120793581009):
															if(lander_y <= 0.17736715823411942):
																return True
															else:
																if(y_velocity > -0.20391415804624557):
																	if(lander_x <= -0.11024045944213867):
																		if(angle_velocity <= -0.0008247115183621645):
																			return True
												else:
													if(lander_y <= 0.27392782270908356):
														if(angle > 0.0006887250929139555):
															if(lander_x <= 0.10790705680847168):
																if(angle_velocity > 0.09454983100295067):
																	return True
															else:
																return True
													else:
														if(lander_y > 0.2880541682243347):
															return True
											else:
												if(x_velocity > -0.0062241205014288425):
													if(y_velocity <= -0.19909492135047913):
														if(angle_velocity <= 0.08634553849697113):
															if(angle_velocity <= 0.01964742224663496):
																if(lander_x <= -0.14925479888916016):
																	return True
																else:
																	if(x_velocity <= 0.04161417856812477):
																		if(angle_velocity <= 0.018095350824296474):
																			return True
															else:
																return True
													else:
														if(lander_x <= 0.07373743131756783):
															if(lander_x > -0.14914417266845703):
																if(x_velocity <= 0.05354272201657295):
																	if(y_velocity <= -0.1963896080851555):
																		if(angle <= 0.02702635433524847):
																			return True
																else:
																	if(lander_y <= 0.22295434027910233):
																		return True
									else:
										if(angle_velocity <= 0.27043651044368744):
											if(lander_y <= 0.25494179129600525):
												if(angle_velocity <= -0.005314721260219812):
													if(angle_velocity <= -0.005757053149864078):
														if(lander_y <= 0.21493321657180786):
															if(angle <= 0.03667156584560871):
																if(lander_y <= 0.15531865507364273):
																	if(angle_velocity <= -0.008354404475539923):
																		return True
															else:
																return True
												else:
													if(angle <= 0.027910239063203335):
														if(angle <= 0.02786886226385832):
															return True
													else:
														if(angle_velocity <= 0.07716051861643791):
															if(y_velocity <= -0.1948823481798172):
																return True
															else:
																if(y_velocity > -0.19475548714399338):
																	if(lander_y <= 0.23298634588718414):
																		return True
																	else:
																		if(lander_x > -0.12926983833312988):
																			return True
														else:
															if(angle_velocity > 0.077748142182827):
																return True
											else:
												if(x_velocity <= 0.07137685641646385):
													if(lander_y <= 0.2812550216913223):
														if(angle <= 0.028213849291205406):
															return True
														else:
															if(lander_x > 0.07850079517811537):
																if(x_velocity > 0.0152086834423244):
																	return True
												else:
													return True
					else:
						if(angle <= 0.034049760550260544):
							if(x_velocity <= 0.05305109918117523):
								if(y_velocity <= -0.21372266113758087):
									if(lander_y <= 0.3575222045183182):
										if(x_velocity <= -0.010724043473601341):
											if(lander_y <= 0.3515322655439377):
												if(angle_velocity <= -0.006636293372139335):
													if(angle > -0.015577009879052639):
														return True
										else:
											if(angle <= -0.004033001489005983):
												if(y_velocity <= -0.22201097756624222):
													if(lander_y > 0.30483753979206085):
														return True
											else:
												if(angle_velocity > -0.004115351592190564):
													if(lander_y <= 0.34391212463378906):
														return True
													else:
														if(lander_y > 0.34799720346927643):
															if(lander_x <= -0.08978910371661186):
																return True
									else:
										if(x_velocity > -0.03364337235689163):
											if(angle_velocity > -0.0014139081467874348):
												if(lander_y <= 0.5525970458984375):
													if(lander_x > -0.10589723661541939):
														if(y_velocity <= -0.2196420505642891):
															if(angle_velocity <= 0.020431251265108585):
																if(angle > 0.012532577500678599):
																	return True
															else:
																if(y_velocity <= -0.22150888293981552):
																	if(angle_velocity <= 0.033169619739055634):
																		if(angle > -0.006665428867563605):
																			return True
																else:
																	if(lander_x <= -0.02060365746729076):
																		return True
														else:
															if(lander_y <= 0.5222991704940796):
																if(x_velocity <= 0.03970935940742493):
																	if(angle_velocity <= 0.023540607653558254):
																		if(angle > -2.1919142454862595e-05):
																			if(angle_velocity > 0.021091575734317303):
																				return True
								else:
									if(lander_x <= -0.0046904562041163445):
										if(angle_velocity > -0.010266120545566082):
											if(angle > 0.025997248478233814):
												if(x_velocity <= 0.04489062912762165):
													return True
									else:
										if(x_velocity > -0.02208183240145445):
											if(angle_velocity > 0.0024770539021119475):
												if(x_velocity <= 0.03922008164227009):
													if(x_velocity > -0.02160018589347601):
														if(lander_x > -0.004368925001472235):
															if(y_velocity <= -0.2135368511080742):
																if(angle_velocity > 0.02621288038790226):
																	return True
															else:
																if(angle > -0.025066950358450413):
																	if(lander_x <= 0.13135547190904617):
																		if(x_velocity > 0.023885557428002357):
																			if(lander_x <= -0.0019715309608727694):
																				return True
												else:
													if(angle_velocity > 0.023443574085831642):
														if(x_velocity <= 0.044566577300429344):
															return True
							else:
								if(lander_y <= 0.4885428249835968):
									if(y_velocity <= -0.20921574532985687):
										if(angle <= 0.011685142293572426):
											if(angle_velocity > 0.015439566690474749):
												if(y_velocity <= -0.2136419340968132):
													if(angle <= -0.0005988302873447537):
														if(y_velocity <= -0.2184489294886589):
															if(x_velocity > 0.060930537059903145):
																return True
													else:
														return True
												else:
													if(angle_velocity > 0.10941843688488007):
														return True
										else:
											if(angle_velocity <= -0.0015045297041069716):
												if(angle_velocity <= -0.007135703461244702):
													return True
											else:
												if(lander_x > -0.326427698135376):
													if(x_velocity <= 0.06233610399067402):
														if(lander_x <= -0.14032430946826935):
															if(angle > 0.02828526869416237):
																return True
														else:
															if(lander_y <= 0.4427211880683899):
																return True
													else:
														if(x_velocity <= 0.10567198321223259):
															if(lander_x <= -0.20010306686162949):
																if(angle > 0.017873233184218407):
																	return True
															else:
																return True
														else:
															if(lander_x <= -0.18099598586559296):
																return True
									else:
										if(lander_x <= -0.09546852111816406):
											if(angle_velocity <= 0.005387932527810335):
												if(lander_x > -0.2620481252670288):
													if(x_velocity <= 0.08193737268447876):
														if(angle > 0.013746412936598063):
															return True
											else:
												if(x_velocity > 0.07738113403320312):
													if(lander_y <= 0.3158178925514221):
														return True
													else:
														if(y_velocity <= -0.19682814180850983):
															if(angle > 0.02384153939783573):
																if(y_velocity <= -0.20641037821769714):
																	return True
										else:
											if(angle > 0.015679037664085627):
												if(y_velocity <= -0.19918718934059143):
													return True
												else:
													if(angle_velocity > 0.04334738478064537):
														return True
								else:
									if(lander_y <= 1.3911697268486023):
										if(angle_velocity <= 0.02309056557714939):
											if(y_velocity <= -0.218096524477005):
												if(angle > 0.02420397661626339):
													if(y_velocity > -0.21971922367811203):
														return True
										else:
											if(x_velocity <= 0.14600562304258347):
												if(angle_velocity <= 0.04647490940988064):
													if(angle_velocity <= 0.043493252247571945):
														if(y_velocity <= -0.21315408498048782):
															if(lander_x > -0.14153748005628586):
																if(lander_y <= 0.6160241663455963):
																	return True
													else:
														if(lander_y <= 0.5992819666862488):
															return True
												else:
													if(lander_y <= 0.5280139744281769):
														if(x_velocity > 0.07425070367753506):
															return True
													else:
														if(y_velocity <= -0.22308366000652313):
															if(angle > 0.01521918410435319):
																return True
											else:
												if(angle_velocity <= 0.14660384505987167):
													if(angle_velocity > 0.06831873580813408):
														if(y_velocity <= -0.2058495506644249):
															if(lander_y <= 0.6285300850868225):
																return True
												else:
													if(lander_y <= 0.5652773082256317):
														return True
						else:
							if(lander_y <= 0.5863185822963715):
								if(y_velocity <= -0.20273584127426147):
									if(angle <= 0.1946142390370369):
										if(lander_y <= 0.44142310321331024):
											if(y_velocity <= -0.20535477250814438):
												return True
											else:
												if(y_velocity > -0.2051713764667511):
													if(x_velocity <= 0.07270235940814018):
														if(angle > 0.04248816519975662):
															return True
													else:
														return True
										else:
											if(x_velocity <= 0.1046687550842762):
												if(y_velocity <= -0.21798130124807358):
													if(angle_velocity <= 0.02302786521613598):
														if(y_velocity > -0.22318175435066223):
															if(lander_x > -0.1531415954232216):
																return True
													else:
														return True
												else:
													if(y_velocity <= -0.20877746492624283):
														if(angle <= 0.034671757370233536):
															return True
													else:
														if(angle_velocity > 0.029814787209033966):
															if(x_velocity <= 0.10193632915616035):
																return True
											else:
												if(angle_velocity <= 0.005676704226061702):
													if(y_velocity <= -0.2129640057682991):
														if(angle > 0.04993030987679958):
															return True
												else:
													if(lander_y > 0.4477561116218567):
														if(y_velocity <= -0.20807651430368423):
															if(x_velocity <= 0.113375473767519):
																if(x_velocity <= 0.11150490120053291):
																	return True
															else:
																return True
														else:
															if(y_velocity > -0.2072468250989914):
																if(angle_velocity <= 0.13744492456316948):
																	return True
									else:
										if(y_velocity <= -0.22159618139266968):
											return True
								else:
									if(x_velocity <= 0.09705938026309013):
										if(lander_y <= 0.42095011472702026):
											if(lander_x > -0.1157781109213829):
												if(x_velocity <= 0.07562413811683655):
													if(lander_y > 0.41697004437446594):
														return True
												else:
													if(y_velocity <= -0.196133591234684):
														return True
									else:
										if(angle <= 0.11374308541417122):
											if(lander_y <= 0.508734256029129):
												if(angle > 0.04096033237874508):
													if(lander_x > -0.28699319064617157):
														if(y_velocity <= -0.19332081079483032):
															return True
														else:
															if(angle <= 0.06660915538668633):
																return True
											else:
												if(x_velocity <= 0.17307308316230774):
													if(angle > 0.048182547092437744):
														if(lander_x > -0.1486435905098915):
															if(x_velocity <= 0.11889481917023659):
																return True
												else:
													if(y_velocity <= -0.1931348517537117):
														if(y_velocity > -0.20176877081394196):
															return True
							else:
								if(x_velocity <= 0.2813781797885895):
									if(x_velocity <= 0.2044903039932251):
										if(lander_x <= -0.11335830762982368):
											if(y_velocity <= -0.20570598542690277):
												if(lander_y <= 0.6806885898113251):
													if(lander_x <= -0.21587343513965607):
														if(angle_velocity <= 0.010703293140977621):
															return True
													else:
														return True
										else:
											if(y_velocity <= -0.22416681796312332):
												return True
											else:
												if(lander_y <= 1.0864827036857605):
													if(lander_y <= 1.0452588200569153):
														if(angle_velocity <= 0.01179392309859395):
															if(y_velocity <= -0.22135239094495773):
																if(lander_y > 0.6182665824890137):
																	return True
													else:
														if(angle > 0.1444753035902977):
															return True
												else:
													if(lander_y <= 1.4217828512191772):
														if(x_velocity > 0.19004350900650024):
															if(y_velocity <= -0.22363383322954178):
																return True
															else:
																if(x_velocity <= 0.1932922974228859):
																	return True
									else:
										if(angle_velocity <= 0.0879020132124424):
											if(lander_y <= 1.3319485187530518):
												return True
											else:
												if(angle_velocity > 0.04395821690559387):
													if(y_velocity <= -0.21488496661186218):
														return True
													else:
														if(x_velocity > 0.2296036332845688):
															return True
										else:
											if(angle > 0.12765425071120262):
												if(lander_y <= 1.2444899678230286):
													if(angle <= 0.3052857518196106):
														if(angle <= 0.17856942117214203):
															if(angle <= 0.16171462833881378):
																return True
														else:
															return True
												else:
													if(lander_y > 1.4481617212295532):
														if(lander_x > 0.07722954824566841):
															return True
								else:
									if(angle_velocity <= 0.31584182381629944):
										if(lander_x <= 0.2778894901275635):
											if(y_velocity <= -0.2168443650007248):
												if(angle <= 0.3000917434692383):
													return True
											else:
												return True
										else:
											if(y_velocity <= -0.211095929145813):
												return True
									else:
										if(angle <= 0.21356071531772614):
											return True
				else:
					if(x_velocity <= 0.07045570015907288):
						if(right_leg_contact != True):
							if(left_leg_contact != True):
								if(y_velocity <= -0.18674296140670776):
									if(angle <= 0.0206502266228199):
										if(x_velocity > 0.05978120490908623):
											if(lander_x > -0.1872841790318489):
												if(angle > 0.0050793820882972796):
													if(y_velocity > -0.18915868550539017):
														return True
									else:
										if(lander_y <= 0.12287139892578125):
											if(lander_x <= -0.023945760913193226):
												if(x_velocity > 0.039824316278100014):
													return True
											else:
												if(angle <= 0.02484336867928505):
													if(lander_x <= 0.11174916848540306):
														return True
												else:
													return True
										else:
											if(angle <= 0.022526774555444717):
												if(lander_y <= 0.2275855839252472):
													return True
											else:
												if(lander_x <= 0.017209386453032494):
													if(angle > 0.049267735332250595):
														return True
												else:
													if(x_velocity > 0.024150562472641468):
														if(angle_velocity > 0.005531748756766319):
															return True
								else:
									if(angle_velocity <= 0.0069290283136069775):
										if(lander_x <= 0.056334782391786575):
											if(angle_velocity <= 0.006530629703775048):
												if(y_velocity <= -0.1764686405658722):
													if(lander_x > -0.0709809772670269):
														if(x_velocity <= 0.03471241518855095):
															if(angle > 0.037080058827996254):
																return True
														else:
															if(lander_y <= 0.09074575453996658):
																if(angle > 0.024390445090830326):
																	return True
															else:
																if(x_velocity <= 0.06363154761493206):
																	if(y_velocity <= -0.17950208485126495):
																		if(angle_velocity <= 0.0011211353121325374):
																			return True
												else:
													if(lander_y > 0.0062898253090679646):
														if(x_velocity <= 0.06309620290994644):
															if(y_velocity <= -0.17502595484256744):
																if(y_velocity > -0.1752338483929634):
																	return True
											else:
												if(x_velocity > 0.04881565645337105):
													return True
										else:
											if(x_velocity > 0.011500594671815634):
												if(lander_y <= 0.1928277686238289):
													if(angle > 0.04679787531495094):
														return True
									else:
										if(lander_y <= 0.004686186322942376):
											if(lander_y > 0.003906575497239828):
												return True
										else:
											if(angle <= 0.04520220868289471):
												if(lander_y <= 0.09839480742812157):
													if(lander_y <= 0.09669607505202293):
														if(angle > -0.03468683920800686):
															if(angle_velocity <= 0.025887180119752884):
																if(angle_velocity <= 0.02547292783856392):
																	if(angle_velocity > 0.023870393633842468):
																		if(y_velocity <= -0.17367679625749588):
																			return True
													else:
														return True
											else:
												if(y_velocity <= -0.18225999176502228):
													if(x_velocity > 0.01939486525952816):
														return True
												else:
													if(lander_y <= 0.08131232112646103):
														if(lander_y > 0.07714713737368584):
															return True
							else:
								if(angle_velocity <= 0.48868122696876526):
									return True
								else:
									if(y_velocity <= -0.18849119544029236):
										return True
									else:
										if(x_velocity > 0.04647136479616165):
											if(lander_y > -0.010851457249373198):
												return True
					else:
						if(y_velocity <= -0.17878469824790955):
							if(lander_y <= 0.3682808578014374):
								if(angle <= 0.033226991072297096):
									if(angle_velocity <= 0.032327210530638695):
										if(y_velocity <= -0.1822424978017807):
											if(y_velocity <= -0.18755576759576797):
												if(y_velocity <= -0.18873679637908936):
													if(angle > 0.022810661233961582):
														if(y_velocity <= -0.18998104333877563):
															return True
												else:
													return True
										else:
											if(lander_y <= 0.056553278118371964):
												if(angle_velocity > 0.003849118947982788):
													return True
									else:
										if(lander_y <= 0.09766757115721703):
											if(angle <= 0.006735753966495395):
												if(angle_velocity <= 0.04572450928390026):
													return True
											else:
												return True
										else:
											if(y_velocity <= -0.19040030241012573):
												if(lander_y <= 0.16231553256511688):
													return True
								else:
									if(angle_velocity <= 0.004390476504340768):
										if(angle <= 0.05328214913606644):
											if(lander_y <= 0.21552962809801102):
												if(lander_x <= 0.008582782465964556):
													if(angle_velocity <= 0.0017641475424170494):
														return True
										else:
											if(angle_velocity <= -0.0003876490518450737):
												return True
									else:
										if(lander_y <= 0.2763689309358597):
											if(x_velocity <= 0.08989990502595901):
												if(x_velocity <= 0.08929217234253883):
													if(y_velocity <= -0.188216932117939):
														if(y_velocity <= -0.18979504704475403):
															return True
														else:
															if(lander_x > -0.06621541827917099):
																if(lander_y > 0.1490542283281684):
																	return True
													else:
														return True
											else:
												if(lander_x <= -0.1520765796303749):
													if(x_velocity > 0.1060619167983532):
														if(angle_velocity <= 0.01666631130501628):
															if(lander_x <= -0.18893247097730637):
																return True
														else:
															return True
												else:
													return True
										else:
											if(x_velocity <= 0.11118088290095329):
												if(lander_x > -0.07499551773071289):
													return True
											else:
												if(angle_velocity <= 0.05369450896978378):
													return True
							else:
								if(x_velocity <= 0.3764907121658325):
									if(lander_y <= 1.4620787501335144):
										if(angle <= 0.07854641228914261):
											if(lander_x <= -0.012809991836547852):
												if(angle_velocity > 0.0007023490179562941):
													if(x_velocity <= 0.2039438560605049):
														if(x_velocity > 0.19526255130767822):
															if(y_velocity <= -0.1825517937541008):
																return True
										else:
											if(angle <= 0.09951448440551758):
												if(angle_velocity <= 0.05455542355775833):
													if(x_velocity > 0.12013629823923111):
														if(lander_y <= 0.5086338073015213):
															if(y_velocity <= -0.1809346154332161):
																return True
															else:
																if(y_velocity > -0.17924510687589645):
																	return True
														else:
															if(lander_y > 0.5402218699455261):
																return True
												else:
													if(lander_x > -0.18617639690637589):
														if(y_velocity > -0.18636740744113922):
															return True
											else:
												if(lander_x <= -0.24475514888763428):
													if(lander_y <= 0.50161412358284):
														return True
												else:
													if(x_velocity > 0.3431735634803772):
														if(lander_y <= 1.3964890241622925):
															return True
								else:
									if(angle > 0.06874822499230504):
										if(angle <= 0.5347166955471039):
											return True
						else:
							if(x_velocity <= 0.45725807547569275):
								if(angle_velocity <= 0.020849051885306835):
									if(angle > 0.010707416106015444):
										if(x_velocity <= 0.1138673722743988):
											if(lander_x > -0.10730233043432236):
												if(angle > 0.049654776230454445):
													if(y_velocity <= -0.17403686791658401):
														return True
													else:
														if(x_velocity > 0.09220557659864426):
															if(y_velocity <= -0.16615163534879684):
																return True
										else:
											if(angle <= 0.09788025543093681):
												if(y_velocity <= -0.17339228838682175):
													if(angle_velocity <= 0.003842043923214078):
														if(lander_y <= 0.3522111475467682):
															if(lander_y > 0.10307086631655693):
																if(lander_y <= 0.19324154406785965):
																	if(lander_y <= 0.17379280924797058):
																		return True
																else:
																	return True
													else:
														if(lander_y <= 0.22012582421302795):
															return True
												else:
													if(y_velocity > -0.1659632921218872):
														if(angle > 0.06073630414903164):
															if(angle > 0.06834540143609047):
																if(y_velocity <= -0.1597970724105835):
																	if(angle <= 0.0780148021876812):
																		return True
								else:
									if(lander_y <= 0.04226007126271725):
										if(left_leg_contact != True):
											if(y_velocity <= -0.16917701810598373):
												if(angle > 0.019545963034033775):
													if(lander_y > 0.003287003026343882):
														return True
											else:
												if(x_velocity > 0.15987766534090042):
													if(x_velocity <= 0.16599652916193008):
														return True
										else:
											return True
									else:
										if(y_velocity <= -0.13968756049871445):
											if(x_velocity <= 0.40679629147052765):
												if(y_velocity <= -0.17383474111557007):
													if(lander_y <= 0.3370380997657776):
														if(angle <= 0.07535969465970993):
															if(y_velocity <= -0.1740221008658409):
																if(x_velocity <= 0.13857810199260712):
																	if(angle_velocity <= 0.03281082585453987):
																		if(lander_y <= 0.15390201658010483):
																			return True
															else:
																if(y_velocity <= -0.1738743633031845):
																	return True
														else:
															return True
												else:
													if(angle > -0.004808521131053567):
														if(angle_velocity <= 0.15649355202913284):
															if(angle_velocity > 0.02203170582652092):
																if(lander_y <= 0.1910090520977974):
																	if(lander_y <= 0.18781189620494843):
																		if(lander_x > 0.009559154510498047):
																			if(lander_x <= 0.012866020202636719):
																				return True
																	else:
																		return True
											else:
												if(y_velocity <= -0.1588578298687935):
													if(angle_velocity <= 0.2123352363705635):
														return True
							else:
								if(x_velocity <= 0.5235196650028229):
									if(angle_velocity <= 0.2699975222349167):
										if(angle > 0.1340556386858225):
											if(y_velocity <= -0.14206217974424362):
												return True
								else:
									if(y_velocity <= -0.13655703514814377):
										return True
									else:
										if(angle <= 0.3606109768152237):
											return True
	else:
		if(angle > 0.18057335913181305):
			if(angle_velocity > -0.0002966387401102111):
				if(lander_y > -0.04202711209654808):
					if(left_leg_contact != True):
						if(angle > 0.20635519921779633):
							if(x_velocity > 0.6184144616127014):
								return True
	return False

def weShould_right_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.13108108192682266):
		if(y_velocity <= -0.22433070093393326):
			if(angle_velocity <= -0.033176204189658165):
				if(lander_y <= 1.3444701433181763):
					if(y_velocity <= -0.273845911026001):
						if(angle <= 0.024799825623631477):
							if(angle_velocity <= -0.059247663244605064):
								if(y_velocity <= -0.2988070696592331):
									if(angle_velocity <= -0.37396079301834106):
										if(lander_y > 1.3258112668991089):
											if(angle > -0.17070841044187546):
												return True
									else:
										if(angle <= -0.17935995012521744):
											if(y_velocity <= -0.4330245852470398):
												if(angle_velocity <= -0.19668453186750412):
													if(angle <= -0.20540592074394226):
														if(y_velocity > -0.5109458863735199):
															if(x_velocity <= -0.5982315242290497):
																return True
															else:
																if(angle > -0.2599492073059082):
																	if(y_velocity > -0.47442156076431274):
																		if(lander_x <= -0.13941650092601776):
																			return True
											else:
												if(y_velocity <= -0.4094104766845703):
													if(x_velocity <= -0.3373663127422333):
														if(angle_velocity > -0.13404980301856995):
															if(angle <= -0.22553379833698273):
																if(x_velocity <= -0.3820887953042984):
																	return True
															else:
																if(angle_velocity > -0.06849892809987068):
																	return True
										else:
											if(y_velocity <= -0.4337708652019501):
												if(lander_y <= 1.29323410987854):
													if(x_velocity <= -0.43729841709136963):
														if(y_velocity <= -0.5011577010154724):
															if(angle_velocity <= -0.08882353827357292):
																if(lander_x <= -0.05888814851641655):
																	if(x_velocity <= -0.6063183546066284):
																		if(x_velocity > -0.6112581491470337):
																			return True
																else:
																	if(lander_x <= -0.053932713344693184):
																		return True
															else:
																return True
														else:
															if(angle_velocity <= -0.23740269988775253):
																if(x_velocity <= -0.521897166967392):
																	if(angle <= -0.1680200695991516):
																		return True
																	else:
																		if(y_velocity <= -0.4903692156076431):
																			return True
															else:
																if(lander_y <= 1.1536120176315308):
																	if(angle <= -0.05422508344054222):
																		return True
																else:
																	return True
												else:
													if(x_velocity <= -0.5180715620517731):
														if(y_velocity <= -0.5468528866767883):
															if(y_velocity <= -0.5587777495384216):
																return True
														else:
															return True
													else:
														if(angle_velocity <= -0.21660000085830688):
															if(lander_y <= 1.3219497203826904):
																if(lander_y <= 1.299863576889038):
																	if(angle_velocity <= -0.29600100219249725):
																		return True
															else:
																return True
											else:
												if(angle <= -0.00803579343482852):
													if(y_velocity <= -0.36119943857192993):
														if(lander_x <= -0.048978567123413086):
															if(angle_velocity <= -0.18610703945159912):
																if(angle <= -0.07978971302509308):
																	if(x_velocity <= -0.3541252464056015):
																		if(angle_velocity <= -0.22655729949474335):
																			if(y_velocity <= -0.4039473682641983):
																				if(angle_velocity <= -0.2346111163496971):
																					if(angle > -0.11017873510718346):
																						if(y_velocity > -0.41161997616291046):
																							return True
																				else:
																					return True
																			else:
																				return True
																		else:
																			if(x_velocity <= -0.3892449885606766):
																				return True
																	else:
																		if(lander_y <= 1.3376284837722778):
																			if(angle > -0.08771895989775658):
																				if(x_velocity <= -0.29317427426576614):
																					return True
																else:
																	if(x_velocity <= -0.3651866614818573):
																		return True
															else:
																if(y_velocity > -0.4065731167793274):
																	if(angle <= -0.12085811421275139):
																		if(y_velocity <= -0.36271941661834717):
																			if(x_velocity <= -0.3558248430490494):
																				return True
																		else:
																			return True
																	else:
																		if(x_velocity <= -0.22532016038894653):
																			if(lander_x > -0.05470695346593857):
																				return True
														else:
															if(x_velocity <= -0.36446189880371094):
																if(lander_y > 0.6396991312503815):
																	if(x_velocity > -0.3678661584854126):
																		if(lander_y > 0.9843174815177917):
																			return True
															else:
																if(angle <= -0.013763591181486845):
																	if(lander_y <= 1.3147606253623962):
																		if(angle > -0.025734934955835342):
																			if(x_velocity > -0.24336615204811096):
																				return True
																else:
																	return True
													else:
														if(angle_velocity <= -0.06438378989696503):
															if(lander_x <= 0.14272303879261017):
																if(angle_velocity <= -0.08884239196777344):
																	if(lander_y > 1.210818886756897):
																		if(x_velocity <= -0.2173689603805542):
																			return True
																else:
																	if(y_velocity <= -0.3359816372394562):
																		if(x_velocity <= -0.19562559574842453):
																			if(x_velocity > -0.20183955878019333):
																				return True
																	else:
																		if(lander_x <= 0.13328395038843155):
																			if(y_velocity > -0.30143213272094727):
																				if(angle > -0.039074202068150043):
																					return True
															else:
																if(lander_y <= 0.7706000208854675):
																	if(x_velocity <= -0.2208804190158844):
																		if(y_velocity > -0.337039589881897):
																			if(lander_y <= 0.48573848605155945):
																				if(angle > -0.12391063198447227):
																					if(lander_x <= 0.17291436344385147):
																						return True
																else:
																	if(y_velocity > -0.3521493077278137):
																		if(lander_x <= 0.2635515630245209):
																			if(x_velocity <= -0.13918402791023254):
																				if(angle_velocity <= -0.06700482964515686):
																					if(x_velocity <= -0.25093626976013184):
																						if(lander_x > 0.20511451363563538):
																							return True
																				else:
																					return True
																		else:
																			if(angle_velocity > -0.14140108972787857):
																				return True
														else:
															if(angle <= -0.05002631992101669):
																if(angle_velocity > -0.0614648275077343):
																	if(angle > -0.10693388804793358):
																		return True
												else:
													if(y_velocity <= -0.32478559017181396):
														if(lander_x <= -0.03480634745210409):
															return True
								else:
									if(lander_y <= 0.7050610482692719):
										if(angle <= -0.016425722744315863):
											if(y_velocity <= -0.2863665968179703):
												if(angle_velocity > -0.08904643729329109):
													if(lander_y > 0.6451204121112823):
														if(angle_velocity <= -0.07828659936785698):
															return True
									else:
										if(angle <= 0.004968515830114484):
											if(lander_y <= 1.1829760670661926):
												if(lander_y > 0.9118808507919312):
													if(lander_y > 0.926120936870575):
														if(angle <= -0.0050670604687184095):
															if(lander_x <= 0.16263370215892792):
																return True
											else:
												return True
										else:
											if(angle_velocity <= -0.08426381647586823):
												if(angle > 0.022597305476665497):
													if(angle <= 0.024377943947911263):
														return True
											else:
												if(x_velocity <= -0.058141548186540604):
													if(lander_y <= 1.0551754832267761):
														if(lander_x <= 0.1210385337471962):
															if(angle_velocity <= -0.0816766582429409):
																return True
													else:
														return True
							else:
								if(lander_y <= 0.8993513584136963):
									if(angle <= -0.03608830086886883):
										if(y_velocity <= -0.28350360691547394):
											if(lander_y <= 0.7270106077194214):
												if(angle_velocity <= -0.05718567967414856):
													return True
												else:
													if(angle_velocity <= -0.033221347257494926):
														if(x_velocity <= -0.020858132280409336):
															if(angle <= -0.10625071451067924):
																if(y_velocity > -0.33073922991752625):
																	if(y_velocity <= -0.31617048382759094):
																		return True
											else:
												if(y_velocity > -0.3133092075586319):
													if(y_velocity > -0.28776492178440094):
														return True
										else:
											if(lander_y > 0.469486266374588):
												if(y_velocity > -0.2753429412841797):
													if(lander_y > 0.6207251846790314):
														return True
									else:
										if(y_velocity <= -0.2771090269088745):
											if(y_velocity <= -0.28404779732227325):
												if(x_velocity <= -0.14623917639255524):
													return True
												else:
													if(lander_y > 0.8852115869522095):
														if(angle > -0.021644615568220615):
															if(lander_y <= 0.8878841400146484):
																return True
										else:
											if(lander_y > 0.5317091047763824):
												if(x_velocity <= -0.07187707349658012):
													if(x_velocity <= -0.10545333102345467):
														return True
								else:
									if(y_velocity <= -0.29669009149074554):
										if(lander_x <= -0.003475999808870256):
											if(y_velocity <= -0.342788428068161):
												if(lander_x <= -0.07627568393945694):
													if(y_velocity > -0.4099150002002716):
														if(x_velocity <= -0.33552083373069763):
															return True
												else:
													if(angle_velocity <= -0.04700538143515587):
														if(y_velocity <= -0.37741243839263916):
															if(lander_x > -0.031278944574296474):
																return True
											else:
												if(lander_x > -0.03591289557516575):
													if(y_velocity <= -0.32739101350307465):
														if(lander_x <= -0.024667883291840553):
															return True
													else:
														if(x_velocity <= -0.08919725939631462):
															if(y_velocity > -0.31665223836898804):
																if(x_velocity > -0.16322143375873566):
																	return True
										else:
											if(y_velocity > -0.3068675696849823):
												if(angle_velocity > -0.05088780261576176):
													if(lander_x <= 0.21108727902173996):
														if(lander_y > 1.096395194530487):
															return True
													else:
														if(lander_x > 0.2387922778725624):
															return True
									else:
										if(x_velocity <= -0.06396332010626793):
											if(x_velocity <= -0.09581229835748672):
												return True
											else:
												if(angle <= 0.005803724052384496):
													if(x_velocity <= -0.08584951609373093):
														if(angle > -0.020941817201673985):
															return True
												else:
													if(lander_y > 0.976494312286377):
														return True
										else:
											if(angle <= 0.015422617085278034):
												if(lander_y > 1.232492446899414):
													if(lander_y <= 1.3102829456329346):
														return True
						else:
							if(angle <= 0.23191983997821808):
								if(angle_velocity <= -0.05972559005022049):
									if(angle <= 0.0912783332169056):
										if(y_velocity <= -0.28658297657966614):
											if(lander_x > 0.039663076400756836):
												if(angle_velocity <= -0.10369608923792839):
													if(lander_y <= 1.1294952034950256):
														if(angle_velocity <= -0.36916184425354004):
															if(angle > 0.06587366387248039):
																if(angle_velocity <= -0.47625304758548737):
																	return True
												else:
													if(angle_velocity <= -0.0598941296339035):
														if(angle <= 0.05225302837789059):
															if(angle_velocity > -0.0939495638012886):
																if(x_velocity <= -0.030840015038847923):
																	if(lander_y > 1.2010349035263062):
																		return True
													else:
														return True
										else:
											if(x_velocity <= -0.0033900575945153832):
												if(angle <= 0.05077522248029709):
													if(lander_y > 0.8034813106060028):
														if(lander_x <= 0.042511845007538795):
															return True
														else:
															if(angle <= 0.026534578762948513):
																return True
									else:
										if(lander_x <= 0.2587932199239731):
											if(lander_x > 0.05486712232232094):
												if(x_velocity <= -0.3030150681734085):
													if(y_velocity <= -0.31355656683444977):
														return True
								else:
									if(lander_x <= 0.037775563076138496):
										if(y_velocity > -0.29584261775016785):
											if(angle_velocity > -0.05103209242224693):
												if(y_velocity <= -0.27884821593761444):
													if(y_velocity <= -0.28947247564792633):
														return True
												else:
													if(lander_x > 0.0034049036912620068):
														return True
									else:
										if(x_velocity <= -0.073564313352108):
											if(lander_x <= 0.11718139797449112):
												return True
										else:
											if(lander_x <= 0.07187323644757271):
												if(lander_x <= 0.07159404829144478):
													if(x_velocity <= -0.05135893262922764):
														if(angle_velocity > -0.048243479803204536):
															return True
							else:
								if(y_velocity <= -0.33794403076171875):
									if(x_velocity <= -0.21052471548318863):
										if(lander_x > 0.22968025505542755):
											return True
								else:
									if(x_velocity <= -0.14011316746473312):
										if(lander_y <= 0.6879697442054749):
											if(y_velocity > -0.3158489018678665):
												return True
										else:
											return True
									else:
										if(angle <= 0.45971862971782684):
											if(angle_velocity > -0.24738627672195435):
												if(x_velocity <= -0.009210229036398232):
													if(y_velocity > -0.31540529429912567):
														if(y_velocity <= -0.30606696009635925):
															if(angle > 0.4194222539663315):
																return True
														else:
															return True
										else:
											if(x_velocity <= 0.032838575541973114):
												if(lander_y <= 0.7740776836872101):
													if(y_velocity > -0.31369757652282715):
														if(angle_velocity <= -0.06954314932227135):
															return True
												else:
													return True
											else:
												if(y_velocity > -0.28642818331718445):
													if(x_velocity <= 0.09212664887309074):
														return True
					else:
						if(angle <= 0.034930093213915825):
							if(lander_y <= 0.5064136981964111):
								if(angle_velocity <= -0.06040847301483154):
									if(y_velocity > -0.2535327672958374):
										if(angle <= 0.019497358240187168):
											if(lander_y > 0.151559479534626):
												if(angle <= -0.0032971256878226995):
													if(lander_x <= 0.09063887596130371):
														if(angle > -0.012972843833267689):
															if(angle > -0.012694571167230606):
																if(angle_velocity > -0.06974704191088676):
																	if(x_velocity <= -0.027516911271959543):
																		return True
								else:
									if(y_velocity <= -0.2400168478488922):
										if(angle <= -0.026978999376296997):
											if(lander_y > 0.30345430970191956):
												if(y_velocity > -0.26821960508823395):
													if(angle_velocity <= -0.03502657637000084):
														if(lander_x > -0.06985316053032875):
															if(y_velocity <= -0.24487199634313583):
																if(x_velocity <= -0.11728962883353233):
																	if(y_velocity > -0.2559114843606949):
																		return True
															else:
																if(angle_velocity <= -0.042936887592077255):
																	return True
													else:
														if(x_velocity <= -0.061256490647792816):
															return True
										else:
											if(lander_y > 0.3868850916624069):
												if(lander_x > 0.0450282096862793):
													if(x_velocity <= -0.0911533460021019):
														if(y_velocity > -0.2479846179485321):
															return True
									else:
										if(lander_y > 0.19187165051698685):
											if(angle <= 0.008964150212705135):
												if(lander_y <= 0.295793741941452):
													if(angle <= -0.031182220205664635):
														if(lander_y > 0.2916702926158905):
															return True
													else:
														if(y_velocity <= -0.2264702022075653):
															if(y_velocity <= -0.22923804819583893):
																if(x_velocity <= -0.021200704388320446):
																	if(angle <= -0.011414513923227787):
																		if(lander_x <= -0.023135279770940542):
																			if(lander_y > 0.2618270516395569):
																				return True
															else:
																if(lander_x > -0.08069820515811443):
																	return True
														else:
															if(angle_velocity > -0.0400046780705452):
																if(lander_y > 0.23086553812026978):
																	return True
												else:
													if(lander_y <= 0.4847024381160736):
														if(y_velocity <= -0.22604333609342575):
															if(angle <= -0.047422030940651894):
																if(lander_x <= 0.03597393038216978):
																	return True
															else:
																if(angle_velocity <= -0.03338231146335602):
																	if(lander_y <= 0.2988537400960922):
																		return True
																	else:
																		if(y_velocity > -0.2378656566143036):
																			if(angle_velocity <= -0.05317089706659317):
																				if(angle_velocity > -0.05389358475804329):
																					return True
																else:
																	return True
														else:
															if(x_velocity <= 0.01014522387413308):
																if(lander_y > 0.312025249004364):
																	return True
													else:
														if(angle_velocity <= -0.03695204667747021):
															return True
											else:
												if(lander_y > 0.39980554580688477):
													if(lander_y > 0.42888352274894714):
														if(angle <= 0.015268184244632721):
															return True
							else:
								if(angle_velocity <= -0.05284256301820278):
									if(x_velocity <= -0.10827244073152542):
										if(y_velocity > -0.26872535049915314):
											if(lander_x > 0.06066169869154692):
												if(lander_x <= 0.21067585796117783):
													return True
												else:
													if(x_velocity <= -0.12532290443778038):
														return True
									else:
										if(angle > -0.00010752363596111536):
											if(x_velocity <= -0.07380442321300507):
												if(angle_velocity > -0.08547554910182953):
													if(x_velocity <= -0.0753205195069313):
														if(angle > 0.0007209324394352734):
															if(lander_x <= 0.14763760566711426):
																return True
											else:
												if(lander_y > 0.7227818071842194):
													if(angle <= 0.002522009424865246):
														if(angle > 0.0014628705102950335):
															return True
													else:
														if(y_velocity > -0.23857375979423523):
															if(x_velocity <= -0.029036267660558224):
																return True
								else:
									if(x_velocity <= -0.03969418443739414):
										if(angle <= -0.004477277863770723):
											if(angle_velocity <= -0.04905989393591881):
												if(angle > -0.020632019266486168):
													if(lander_x <= 0.04906487464904785):
														if(x_velocity <= -0.062626201659441):
															return True
											else:
												if(x_velocity <= -0.08537657558917999):
													if(angle_velocity <= -0.03913089446723461):
														if(x_velocity > -0.08689343929290771):
															return True
													else:
														if(y_velocity > -0.2715301811695099):
															if(lander_x > -0.028950500302016735):
																return True
												else:
													if(angle <= -0.006619237828999758):
														if(angle > -0.0167265422642231):
															if(lander_x <= 0.06441674008965492):
																if(y_velocity > -0.25397640466690063):
																	return True
													else:
														return True
										else:
											if(y_velocity <= -0.2564547210931778):
												if(x_velocity <= -0.06182005628943443):
													return True
												else:
													if(angle > 0.003093022503890097):
														if(lander_y > 0.95409095287323):
															return True
											else:
												if(lander_x <= 0.14655842632055283):
													if(angle <= 0.008637923747301102):
														if(x_velocity <= -0.045624028891325):
															if(lander_x <= 0.10051970183849335):
																if(lander_y <= 0.6209210157394409):
																	return True
																else:
																	if(y_velocity <= -0.2510424256324768):
																		return True
													else:
														return True
									else:
										if(lander_y <= 0.5522063076496124):
											if(lander_y > 0.5241343975067139):
												if(y_velocity > -0.23848091810941696):
													if(x_velocity > -0.016883855685591698):
														if(lander_y <= 0.5267400443553925):
															return True
										else:
											if(y_velocity <= -0.2282232791185379):
												if(angle <= 0.016525248996913433):
													if(angle_velocity <= -0.033497318625450134):
														if(y_velocity > -0.23080382496118546):
															if(y_velocity <= -0.22896210849285126):
																return True
													else:
														return True
											else:
												if(lander_y <= 0.7680761516094208):
													return True
						else:
							if(x_velocity <= 0.025186216458678246):
								if(angle_velocity <= -0.071587685495615):
									if(angle <= 0.1095874160528183):
										if(x_velocity <= -0.030848713591694832):
											if(lander_x <= 0.2282298132777214):
												if(y_velocity <= -0.2566540092229843):
													if(x_velocity > -0.03515925072133541):
														return True
												else:
													if(angle_velocity <= -0.19618981331586838):
														if(angle_velocity <= -0.2810531258583069):
															if(x_velocity <= -0.0608994010835886):
																if(x_velocity <= -0.18246731162071228):
																	return True
													else:
														if(x_velocity <= -0.035411085933446884):
															return True
														else:
															if(lander_y > 1.0392673015594482):
																return True
											else:
												return True
										else:
											if(y_velocity <= -0.24221179634332657):
												if(angle > 0.07443808019161224):
													if(x_velocity <= -0.01105482317507267):
														if(y_velocity > -0.25863175094127655):
															if(lander_y > 1.1389644742012024):
																return True
											else:
												if(lander_y > 0.9253587424755096):
													return True
									else:
										if(angle <= 0.2809743285179138):
											if(x_velocity <= -0.11730331182479858):
												return True
											else:
												if(y_velocity <= -0.24049507081508636):
													if(lander_y > 1.2089558243751526):
														if(angle <= 0.11862792074680328):
															return True
												else:
													if(angle_velocity > -0.2143898606300354):
														return True
										else:
											if(lander_y <= 0.9295924305915833):
												if(y_velocity > -0.25443483889102936):
													if(lander_y > 0.7515280842781067):
														return True
											else:
												return True
								else:
									if(lander_y <= 1.0452626943588257):
										if(x_velocity <= -0.020400109700858593):
											if(y_velocity <= -0.25144486129283905):
												if(lander_y <= 0.9741859138011932):
													if(angle_velocity <= -0.058106349781155586):
														if(angle_velocity <= -0.06286430172622204):
															if(lander_y <= 0.8521100580692291):
																return True
													else:
														if(x_velocity <= -0.04720745235681534):
															return True
												else:
													if(angle_velocity <= -0.03587900660932064):
														return True
											else:
												return True
										else:
											if(lander_y <= 0.8571777045726776):
												if(lander_x <= 0.16427383571863174):
													if(x_velocity > -0.018550340086221695):
														if(y_velocity > -0.22877222299575806):
															if(x_velocity <= 0.003077297005802393):
																return True
											else:
												if(lander_y <= 0.986799955368042):
													if(angle > 0.08642616868019104):
														if(x_velocity > 0.01179939930443652):
															return True
												else:
													if(y_velocity > -0.2546733021736145):
														if(angle <= 0.07542070746421814):
															if(x_velocity <= 0.0023838841589167714):
																return True
															else:
																if(y_velocity <= -0.2542535215616226):
																	return True
														else:
															if(x_velocity <= 0.009290582500398159):
																return True
									else:
										if(y_velocity > -0.2708752453327179):
											if(x_velocity <= 0.013716375455260277):
												if(lander_y <= 1.1067175269126892):
													if(angle <= 0.053557682782411575):
														return True
													else:
														if(lander_y <= 1.0700825452804565):
															return True
														else:
															if(angle > 0.06766245141625404):
																return True
												else:
													return True
											else:
												if(y_velocity > -0.2602417767047882):
													return True
							else:
								if(lander_y <= 0.5665508806705475):
									if(angle > 0.26563510298728943):
										if(y_velocity > -0.24123495072126389):
											return True
								else:
									if(angle <= 0.08744543418288231):
										if(lander_y > 0.6420569717884064):
											if(y_velocity > -0.2731200158596039):
												if(y_velocity > -0.23672164976596832):
													if(x_velocity <= 0.02860201057046652):
														return True
									else:
										if(y_velocity <= -0.24430807679891586):
											if(angle <= 0.35814069211483):
												if(angle <= 0.16630902886390686):
													if(angle_velocity > -0.07869734987616539):
														if(lander_x <= 0.14297018200159073):
															if(angle <= 0.11749140173196793):
																if(x_velocity <= 0.0647285096347332):
																	if(lander_y <= 1.210197925567627):
																		if(y_velocity > -0.24939091503620148):
																			if(x_velocity <= 0.04607129655778408):
																				if(lander_y <= 1.1609861850738525):
																					return True
																	else:
																		if(lander_y <= 1.2297842502593994):
																			if(y_velocity <= -0.251080185174942):
																				return True
															else:
																if(y_velocity > -0.24746445566415787):
																	if(x_velocity <= 0.05793793871998787):
																		return True
												else:
													if(angle_velocity > -0.2895004451274872):
														if(angle > 0.3314230591058731):
															if(y_velocity > -0.2498018741607666):
																return True
											else:
												if(y_velocity <= -0.26091068983078003):
													if(angle > 0.4594730883836746):
														return True
												else:
													return True
										else:
											if(angle <= 0.18603547662496567):
												if(angle_velocity <= -0.06871051341295242):
													if(x_velocity <= 0.039872072637081146):
														if(lander_y > 0.9838990867137909):
															return True
													else:
														if(angle_velocity > -0.12319521978497505):
															if(angle <= 0.13856685906648636):
																if(lander_y > 1.2852905988693237):
																	return True
															else:
																if(lander_y <= 1.1982311010360718):
																	if(y_velocity > -0.23231351375579834):
																		if(y_velocity <= -0.226052924990654):
																			return True
																else:
																	if(x_velocity <= 0.09304017201066017):
																		if(angle_velocity > -0.0915611982345581):
																			return True
												else:
													if(x_velocity <= 0.0782221369445324):
														if(lander_y > 0.9920945465564728):
															if(angle <= 0.1434386521577835):
																return True
													else:
														if(lander_y <= 1.2898206114768982):
															if(y_velocity > -0.23597051948308945):
																if(angle > 0.13227420300245285):
																	return True
														else:
															if(lander_x > 0.0880582332611084):
																if(lander_x > 0.10917820781469345):
																	return True
											else:
												if(angle_velocity <= -0.15143311768770218):
													if(angle > 0.2426048144698143):
														if(lander_x <= 0.16154446452856064):
															return True
														else:
															if(y_velocity > -0.22632065415382385):
																return True
												else:
													if(angle <= 0.3542786091566086):
														if(angle > 0.28392522037029266):
															if(lander_x <= 0.17048988118767738):
																return True
													else:
														return True
				else:
					if(x_velocity <= -0.33664602041244507):
						if(angle <= -0.11459648981690407):
							if(angle_velocity <= -0.09190931171178818):
								if(y_velocity <= -0.2519789934158325):
									if(angle_velocity <= -0.4578545540571213):
										if(angle > -0.15882235020399094):
											return True
									else:
										if(x_velocity <= -0.6710363924503326):
											if(y_velocity <= -0.47695353627204895):
												if(x_velocity <= -0.6842849552631378):
													return True
											else:
												return True
										else:
											if(lander_y <= 1.3608826398849487):
												if(lander_x <= -0.0814695805311203):
													if(lander_y <= 1.3590882420539856):
														if(lander_y <= 1.3492493033409119):
															if(lander_x <= -0.09263530001044273):
																return True
													else:
														return True
												else:
													return True
											else:
												if(angle_velocity > -0.18298624455928802):
													if(angle_velocity <= -0.15240415930747986):
														if(lander_y > 1.424329936504364):
															if(angle_velocity <= -0.16597214341163635):
																if(y_velocity > -0.32941558957099915):
																	return True
															else:
																return True
													else:
														if(lander_x > -0.12115335464477539):
															return True
								else:
									if(angle_velocity > -0.152280293405056):
										return True
							else:
								if(y_velocity <= -0.4107735753059387):
									if(x_velocity <= -0.5631673336029053):
										if(y_velocity > -0.5357753932476044):
											return True
									else:
										if(angle_velocity <= -0.04858700558543205):
											if(angle_velocity <= -0.08055906742811203):
												return True
								else:
									if(angle <= -0.31698454916477203):
										if(x_velocity <= -0.5021641850471497):
											return True
									else:
										return True
						else:
							if(x_velocity <= -0.340665265917778):
								if(angle <= -0.09723096713423729):
									if(lander_x <= -0.08354687690734863):
										return True
									else:
										if(angle_velocity > -0.35685573518276215):
											return True
								else:
									return True
					else:
						if(angle <= 0.13649334758520126):
							if(x_velocity <= -0.12586691230535507):
								if(angle <= -0.04123163782060146):
									if(angle_velocity <= -0.05977979861199856):
										if(lander_x <= -0.01974854525178671):
											if(y_velocity <= -0.29226353764533997):
												if(angle_velocity <= -0.30927467346191406):
													if(angle > -0.073415607213974):
														return True
											else:
												if(angle_velocity <= -0.08661189675331116):
													if(lander_y <= 1.3895248174667358):
														return True
												else:
													if(angle_velocity <= -0.07625826075673103):
														return True
													else:
														if(angle_velocity > -0.06168362684547901):
															return True
									else:
										if(y_velocity > -0.3848797380924225):
											if(lander_x <= -0.04711418226361275):
												return True
								else:
									if(lander_x > -0.028066777624189854):
										if(x_velocity <= -0.21400336176156998):
											return True
										else:
											if(y_velocity <= -0.31842872500419617):
												return True
											else:
												if(y_velocity > -0.275382399559021):
													return True
							else:
								if(lander_y <= 1.3478015065193176):
									return True
						else:
							if(lander_y <= 1.3533155918121338):
								if(y_velocity > -0.25446075201034546):
									if(y_velocity <= -0.23582569509744644):
										return True
							else:
								if(y_velocity <= -0.22856424748897552):
									if(lander_x <= 0.09026093408465385):
										if(lander_y <= 1.381516456604004):
											if(angle_velocity > -0.08300057239830494):
												return True
									else:
										if(angle > 0.567365825176239):
											if(x_velocity <= 0.19226755946874619):
												return True
			else:
				if(lander_y <= 0.4006982296705246):
					if(y_velocity <= -0.23569615185260773):
						if(angle <= -0.058152781799435616):
							if(y_velocity <= -0.25839124619960785):
								if(x_velocity <= -0.13590740412473679):
									if(y_velocity <= -0.29675520956516266):
										if(angle <= -0.19683077186346054):
											if(angle_velocity > 0.09490758925676346):
												if(lander_y <= 0.35257023572921753):
													return True
									else:
										if(angle_velocity > -0.01466236962005496):
											if(y_velocity <= -0.27699221670627594):
												if(angle_velocity > 0.0550838578492403):
													if(x_velocity <= -0.1734641119837761):
														return True
											else:
												if(lander_x <= 0.14075402915477753):
													if(angle > -0.16150250285863876):
														return True
								else:
									if(lander_x <= 0.14820809662342072):
										if(y_velocity > -0.2689857631921768):
											if(angle <= -0.10477631539106369):
												if(y_velocity <= -0.2667526602745056):
													return True
											else:
												if(y_velocity > -0.2687617987394333):
													if(x_velocity <= -0.1222674734890461):
														if(angle_velocity > 0.010657726787030697):
															return True
							else:
								if(lander_y > 0.1527993083000183):
									if(x_velocity <= -0.07946266233921051):
										if(y_velocity > -0.25577312707901):
											if(x_velocity <= -0.11398253962397575):
												if(x_velocity <= -0.13120853900909424):
													if(x_velocity <= -0.13429614901542664):
														return True
												else:
													return True
											else:
												if(angle_velocity <= 0.06525545194745064):
													if(angle > -0.07024536281824112):
														if(lander_x <= 0.0068527692928910255):
															return True
												else:
													return True
									else:
										if(angle <= -0.05995078384876251):
											if(x_velocity <= -0.024109167978167534):
												if(y_velocity > -0.2559092044830322):
													if(y_velocity > -0.24186769127845764):
														return True
										else:
											if(angle <= -0.059398721903562546):
												return True
						else:
							if(angle_velocity <= -0.015326505992561579):
								if(lander_y <= 0.25232017040252686):
									if(angle <= -0.03989301435649395):
										if(y_velocity > -0.24880661815404892):
											if(lander_y > 0.1596236675977707):
												if(lander_y > 0.21536662429571152):
													if(lander_y <= 0.2309582680463791):
														return True
								else:
									if(angle <= -0.019317341037094593):
										if(y_velocity > -0.2652069330215454):
											if(angle_velocity <= -0.026273712515830994):
												if(angle_velocity > -0.032510457560420036):
													if(lander_x > -0.2069142386317253):
														if(lander_x <= 0.08081717416644096):
															if(angle > -0.023284176364541054):
																if(lander_y <= 0.34060676395893097):
																	return True
											else:
												if(x_velocity <= -0.050697602331638336):
													if(lander_y > 0.27971217036247253):
														if(y_velocity <= -0.24368827044963837):
															if(angle_velocity <= -0.0188182620331645):
																if(angle <= -0.04977857135236263):
																	return True
														else:
															if(angle > -0.03225914016366005):
																return True
							else:
								if(angle <= 0.1076303981244564):
									if(x_velocity <= -0.07047595828771591):
										if(y_velocity <= -0.2393423095345497):
											if(y_velocity > -0.2515132427215576):
												if(lander_y > 0.27551068365573883):
													if(lander_x <= 0.09606976807117462):
														if(x_velocity <= -0.0761597640812397):
															return True
														else:
															if(lander_y > 0.35375913977622986):
																return True
										else:
											if(lander_y > 0.20869382470846176):
												if(lander_y <= 0.3306434154510498):
													return True
									else:
										if(angle > -0.04748993366956711):
											if(y_velocity > -0.24577776342630386):
												if(y_velocity > -0.24573373794555664):
													if(lander_y > 0.34662970900535583):
														if(x_velocity <= -0.0319372471421957):
															if(y_velocity > -0.24006640911102295):
																if(angle_velocity > 0.0012883221497759223):
																	return True
								else:
									return True
					else:
						if(x_velocity <= -0.04648813232779503):
							if(lander_y <= 0.19113826006650925):
								if(angle <= -0.046979352831840515):
									if(angle_velocity <= 0.02028462290763855):
										if(x_velocity <= -0.09238986298441887):
											if(x_velocity > -0.09955183044075966):
												return True
									else:
										if(lander_y > 0.01318421121686697):
											if(angle <= -0.08574359491467476):
												if(angle <= -0.09479870647192001):
													return True
											else:
												return True
								else:
									if(x_velocity <= -0.09178847447037697):
										return True
									else:
										if(x_velocity <= -0.04701359197497368):
											if(lander_x <= 0.13120436668395996):
												if(lander_x <= -0.05006728135049343):
													if(angle > -0.04138617776334286):
														return True
							else:
								if(angle_velocity <= -0.00023782247444614768):
									if(angle <= -0.026178336702287197):
										if(lander_x <= -0.020393419545143843):
											if(angle_velocity > -0.0047756817657500505):
												return True
										else:
											if(angle_velocity <= -0.029352606274187565):
												return True
									else:
										if(x_velocity <= -0.0636415109038353):
											return True
										else:
											if(x_velocity <= -0.04927167296409607):
												if(lander_x <= -0.023161982651799917):
													return True
								else:
									if(x_velocity <= -0.07402462884783745):
										return True
									else:
										if(x_velocity <= -0.06454848125576973):
											if(y_velocity > -0.23083890974521637):
												if(lander_y <= 0.2897157371044159):
													if(y_velocity > -0.227664552628994):
														return True
										else:
											if(lander_x <= 0.08132438734173775):
												if(angle_velocity <= 0.013537989929318428):
													if(angle <= -0.029097859282046556):
														return True
													else:
														if(angle_velocity <= 0.004578798310831189):
															return True
												else:
													return True
						else:
							if(angle_velocity <= -0.009669447783380747):
								if(angle <= -0.011002792976796627):
									if(lander_y <= 0.13093000650405884):
										if(lander_x <= -0.107452392578125):
											if(x_velocity <= -0.04382038861513138):
												return True
									else:
										if(lander_x <= -0.053118277341127396):
											if(x_velocity <= -0.01717822067439556):
												if(lander_x <= -0.11784172058105469):
													if(lander_y > 0.16643508523702621):
														return True
								else:
									if(angle <= 0.0026032080641016364):
										if(angle > 0.0001600760042492766):
											if(x_velocity <= -0.016053935629315674):
												return True
							else:
								if(lander_y <= 0.26726894080638885):
									if(lander_y <= -0.0023655378608964384):
										if(lander_x <= -0.10059509612619877):
											return True
									else:
										if(angle <= -0.07237591594457626):
											if(angle_velocity > 0.019305534195154905):
												if(x_velocity <= -0.03855601325631142):
													return True
										else:
											if(angle <= -0.0323178693652153):
												if(y_velocity <= -0.2266954481601715):
													if(angle <= -0.03243671730160713):
														if(x_velocity <= -0.0008773153240326792):
															if(lander_x <= -0.2236066311597824):
																if(lander_y <= 0.08764000982046127):
																	return True
												else:
													if(angle_velocity > 0.0038238561246544123):
														if(lander_y > 0.0928050484508276):
															return True
											else:
												if(x_velocity <= -0.04456006549298763):
													return True
												else:
													if(x_velocity <= -0.03155418112874031):
														if(lander_y > 0.17070479691028595):
															if(lander_y > 0.23987478762865067):
																return True
								else:
									if(angle <= -0.002756904112175107):
										if(x_velocity <= 0.013403969816863537):
											if(angle <= -0.029252595268189907):
												if(angle_velocity <= 0.049676163122057915):
													if(x_velocity <= -0.03640488535165787):
														if(x_velocity > -0.041138842701911926):
															return True
													else:
														if(lander_y <= 0.27811114490032196):
															return True
												else:
													return True
											else:
												if(angle > -0.025236784480512142):
													if(y_velocity <= -0.23320049792528152):
														if(lander_x <= 0.02387318667024374):
															if(lander_y > 0.38562603294849396):
																return True
													else:
														if(lander_y <= 0.2971774637699127):
															if(lander_y <= 0.27523885667324066):
																return True
															else:
																if(angle_velocity <= 0.05619689077138901):
																	if(angle <= -0.021180149167776108):
																		if(y_velocity > -0.227064311504364):
																			return True
																else:
																	return True
														else:
															if(y_velocity <= -0.22572313249111176):
																if(angle_velocity <= -0.0019480733899399638):
																	if(angle_velocity <= -0.005438260734081268):
																		return True
																else:
																	return True
															else:
																if(lander_x <= -0.03360905568115413):
																	return True
									else:
										if(x_velocity <= 0.0007018791511654854):
											if(lander_x <= 0.02224893495440483):
												if(lander_y <= 0.3690223693847656):
													if(y_velocity <= -0.2266487404704094):
														if(angle <= 0.0024472602981404634):
															return True
												else:
													return True
											else:
												if(x_velocity <= -0.04012374207377434):
													return True
				else:
					if(y_velocity <= -0.2605880945920944):
						if(lander_y <= 0.7481449842453003):
							if(angle <= -0.02181170228868723):
								if(y_velocity <= -0.27377182245254517):
									if(x_velocity <= -0.12312685325741768):
										if(y_velocity <= -0.28999267518520355):
											if(angle <= -0.09409844875335693):
												if(y_velocity <= -0.3070802539587021):
													if(x_velocity <= -0.15461762249469757):
														if(angle_velocity <= 0.011445730458945036):
															if(y_velocity > -0.33848021924495697):
																if(angle_velocity > -0.0010421707120258361):
																	if(angle <= -0.1446538306772709):
																		if(x_velocity <= -0.2682112604379654):
																			return True
														else:
															if(lander_y > 0.41049598157405853):
																if(y_velocity > -0.3190077096223831):
																	if(x_velocity <= -0.20831692963838577):
																		if(x_velocity <= -0.21005607396364212):
																			return True
													else:
														if(x_velocity <= -0.14397743344306946):
															if(lander_y <= 0.7010950446128845):
																return True
														else:
															if(lander_y <= 0.7201682031154633):
																if(y_velocity > -0.31099455058574677):
																	return True
															else:
																if(x_velocity <= -0.13563267141580582):
																	return True
										else:
											if(angle_velocity > 0.0013880389160476625):
												if(lander_y <= 0.4773557186126709):
													if(angle_velocity > 0.06706838868558407):
														return True
												else:
													if(y_velocity <= -0.28843483328819275):
														if(angle > -0.09170417487621307):
															return True
													else:
														return True
									else:
										if(angle_velocity > -0.02546069025993347):
											if(lander_y <= 0.6829327642917633):
												if(angle <= -0.11299680918455124):
													if(angle_velocity > 0.027471397072076797):
														if(angle <= -0.1144704520702362):
															if(angle > -0.2945413142442703):
																if(lander_x > -0.25343234837055206):
																	if(x_velocity <= -0.11931423470377922):
																		return True
											else:
												if(angle_velocity > 0.0030370953027158976):
													if(lander_y > 0.6835232675075531):
														if(y_velocity <= -0.2742239385843277):
															if(angle <= -0.040644459426403046):
																if(angle <= -0.04082971066236496):
																	if(y_velocity > -0.29040004312992096):
																		if(lander_x <= -0.17059163749217987):
																			if(angle <= -0.137898251414299):
																				return True
																			else:
																				if(y_velocity > -0.2748130261898041):
																					if(y_velocity <= -0.27454207837581635):
																						return True
																		else:
																			if(lander_y > 0.7137521505355835):
																				if(angle <= -0.046668656170368195):
																					return True
																else:
																	return True
								else:
									if(angle_velocity <= -0.01597929745912552):
										if(x_velocity <= -0.0942218005657196):
											if(angle > -0.059978656470775604):
												if(angle <= -0.03969539329409599):
													if(lander_y > 0.5571637153625488):
														return True
												else:
													return True
									else:
										if(x_velocity <= -0.11434036493301392):
											if(angle_velocity > -0.0038744015619158745):
												if(lander_x <= 0.13892173767089844):
													return True
												else:
													if(lander_x > 0.18229293823242188):
														return True
										else:
											if(angle <= -0.054483141750097275):
												if(angle_velocity <= 0.12010367587208748):
													if(lander_y > 0.4569232165813446):
														if(y_velocity <= -0.26215559244155884):
															if(x_velocity <= -0.038297983817756176):
																if(lander_x <= 0.022746515460312366):
																	if(x_velocity > -0.09948572516441345):
																		return True
												else:
													if(x_velocity <= 0.05011344328522682):
														if(y_velocity <= -0.26904501020908356):
															return True
													else:
														if(y_velocity > -0.26122117042541504):
															return True
											else:
												if(lander_y <= 0.6975981593132019):
													if(x_velocity <= -0.09737060591578484):
														if(y_velocity > -0.26768849790096283):
															if(lander_x <= 0.17318911850452423):
																return True
													else:
														if(angle <= -0.022035779431462288):
															if(y_velocity <= -0.2633034735918045):
																if(angle_velocity <= -0.010728998109698296):
																	if(y_velocity <= -0.2719820439815521):
																		return True
																else:
																	if(x_velocity <= -0.08750950545072556):
																		if(angle <= -0.05205370485782623):
																			return True
																	else:
																		if(y_velocity > -0.27327577769756317):
																			if(y_velocity > -0.26708464324474335):
																				if(y_velocity <= -0.2669599801301956):
																					return True
																				else:
																					if(y_velocity > -0.2661731094121933):
																						if(lander_y > 0.6357315182685852):
																							if(lander_y <= 0.643723875284195):
																								return True
															else:
																if(y_velocity <= -0.2629808038473129):
																	if(angle_velocity > 0.005176165024749935):
																		return True
																else:
																	if(lander_x <= 0.025634002406150103):
																		if(angle <= -0.04536372795701027):
																			if(angle > -0.04816283844411373):
																				if(angle_velocity > 0.008913603611290455):
																					return True
																		else:
																			if(y_velocity <= -0.2607315331697464):
																				if(x_velocity <= -0.048706160858273506):
																					if(lander_y > 0.5282087624073029):
																						return True
																	else:
																		if(lander_x > 0.09302086941897869):
																			return True
														else:
															if(y_velocity > -0.26244987547397614):
																return True
												else:
													if(x_velocity <= -0.003156482183840126):
														if(lander_y > 0.7053253650665283):
															if(angle_velocity <= 0.022812683135271072):
																if(y_velocity > -0.26225148141384125):
																	return True
															else:
																if(lander_x <= 0.021719026379287243):
																	if(y_velocity <= -0.2611839026212692):
																		return True
							else:
								if(angle_velocity <= -0.0003560411714715883):
									if(y_velocity > -0.27034956216812134):
										if(lander_x <= 0.1070275790989399):
											if(angle <= -0.0019573994795791805):
												if(x_velocity <= 0.023342729546129704):
													if(lander_x > 0.027657413855195045):
														if(x_velocity <= -0.03038112446665764):
															if(lander_x <= 0.08523745462298393):
																if(x_velocity <= -0.08026697114109993):
																	return True
															else:
																if(lander_x > 0.0926971435546875):
																	if(y_velocity > -0.2669934332370758):
																		return True
								else:
									if(x_velocity <= -0.09095006063580513):
										if(y_velocity > -0.26875996589660645):
											return True
									else:
										if(lander_x <= 0.15463419258594513):
											if(lander_y > 0.6874419748783112):
												if(y_velocity <= -0.26212240755558014):
													if(y_velocity > -0.2651161700487137):
														if(x_velocity <= -0.04879201017320156):
															return True
												else:
													return True
						else:
							if(angle <= 0.02187927905470133):
								if(y_velocity <= -0.2870802879333496):
									if(x_velocity <= 0.28544867038726807):
										if(lander_y <= 0.927573561668396):
											if(angle <= -0.05751131847500801):
												if(y_velocity <= -0.3031482994556427):
													if(x_velocity <= -0.07524305582046509):
														if(y_velocity <= -0.3130800426006317):
															if(angle <= -0.1344577819108963):
																if(y_velocity <= -0.35077668726444244):
																	if(angle_velocity > 0.008511662017554045):
																		if(angle_velocity <= 0.15972856432199478):
																			if(lander_x > -0.3242046386003494):
																				if(angle_velocity > 0.15597213804721832):
																					if(lander_x > -0.23805096000432968):
																						return True
																else:
																	if(angle <= -0.18281710892915726):
																		if(x_velocity <= -0.15664704889059067):
																			if(angle_velocity <= 0.07859205082058907):
																				if(y_velocity > -0.3229181617498398):
																					return True
																			else:
																				return True
																		else:
																			if(angle_velocity > 0.19388870149850845):
																				return True
																	else:
																		if(y_velocity > -0.33404724299907684):
																			if(y_velocity <= -0.3166087418794632):
																				if(x_velocity <= -0.10577506572008133):
																					if(angle > -0.14599348604679108):
																						return True
																				else:
																					return True
															else:
																if(angle_velocity <= 0.13706297054886818):
																	if(angle_velocity > -0.010039173532277346):
																		if(y_velocity > -0.3169088214635849):
																			if(y_velocity <= -0.31652095913887024):
																				return True
																else:
																	return True
														else:
															if(angle <= -0.09483622759580612):
																return True
															else:
																if(angle > -0.0794033445417881):
																	return True
													else:
														if(angle_velocity > 0.03566866181790829):
															if(lander_y > 0.7518079578876495):
																if(lander_y <= 0.773534506559372):
																	if(lander_y > 0.7727174758911133):
																		return True
																else:
																	if(angle > -0.19352463632822037):
																		if(angle_velocity > 0.24249832332134247):
																			if(lander_x <= -0.2854953110218048):
																				return True
												else:
													if(x_velocity <= -0.03121186699718237):
														if(angle_velocity <= 0.060871485620737076):
															if(lander_x <= -0.14834103733301163):
																if(y_velocity > -0.29245810210704803):
																	if(lander_y <= 0.8403781354427338):
																		return True
															else:
																if(lander_x <= 0.006495429202914238):
																	if(y_velocity <= -0.2896360158920288):
																		if(angle_velocity > 0.04137590713799):
																			if(lander_x > -0.10703735053539276):
																				return True
																else:
																	return True
														else:
															if(lander_y <= 0.8233723044395447):
																if(y_velocity > -0.2951791435480118):
																	if(lander_y <= 0.8095289468765259):
																		if(lander_y <= 0.7858394086360931):
																			return True
																	else:
																		return True
															else:
																if(angle > -0.1473691686987877):
																	if(angle_velocity <= 0.06705183163285255):
																		if(angle_velocity <= 0.06404086947441101):
																			return True
																	else:
																		if(angle_velocity <= 0.07787059992551804):
																			if(lander_y <= 0.8877435326576233):
																				return True
																		else:
																			return True
													else:
														if(angle_velocity > 0.03155993763357401):
															if(angle <= -0.14376632124185562):
																if(y_velocity > -0.29525814950466156):
																	return True
															else:
																if(y_velocity > -0.3021085411310196):
																	if(lander_y <= 0.8006114363670349):
																		if(angle_velocity > 0.18462839722633362):
																			if(angle_velocity <= 0.2033485770225525):
																				return True
																	else:
																		if(lander_y <= 0.8174704313278198):
																			if(angle_velocity > 0.1395440325140953):
																				if(lander_y > 0.8094200193881989):
																					return True
																		else:
																			if(y_velocity > -0.29175035655498505):
																				if(angle_velocity > 0.07651634141802788):
																					if(lander_y <= 0.9152035415172577):
																						if(angle <= -0.07856425270438194):
																							if(y_velocity <= -0.29131732881069183):
																								return True
																						else:
																							return True
											else:
												if(lander_x <= 0.21776456385850906):
													if(y_velocity > -0.2921095937490463):
														if(x_velocity <= -0.11104102060198784):
															if(angle_velocity > -0.013931303285062313):
																return True
														else:
															if(y_velocity <= -0.2919992655515671):
																return True
															else:
																if(lander_x <= -0.13604015856981277):
																	if(angle_velocity <= 0.018082361668348312):
																		if(angle_velocity <= -0.0016877823509275913):
																			if(angle > -0.045225536450743675):
																				return True
												else:
													if(y_velocity > -0.3133704215288162):
														if(angle > -0.05219015292823315):
															return True
										else:
											if(y_velocity <= -0.3181559443473816):
												if(x_velocity <= -0.09489988535642624):
													if(y_velocity <= -0.3449101150035858):
														if(angle <= 0.003930528182536364):
															if(angle <= -0.1493743658065796):
																if(y_velocity <= -0.3789035230875015):
																	if(angle_velocity <= 0.027191842906177044):
																		if(y_velocity <= -0.3943863660097122):
																			if(lander_x <= -0.1216805949807167):
																				if(x_velocity <= -0.2808101028203964):
																					if(angle <= -0.263735756278038):
																						if(y_velocity > -0.45882800221443176):
																							if(lander_y <= 1.3552486300468445):
																								if(lander_x > -0.15971794724464417):
																									if(x_velocity <= -0.3526459187269211):
																										if(angle_velocity > -0.01725156349129975):
																											if(x_velocity > -0.36262474954128265):
																												return True
																							else:
																								return True
																					else:
																						if(y_velocity > -0.4173963814973831):
																							if(lander_x <= -0.12892670929431915):
																								if(lander_y > 1.1672784686088562):
																									return True
																			else:
																				if(lander_y <= 1.4432497024536133):
																					if(angle_velocity > -0.013694960623979568):
																						if(x_velocity <= -0.20433081686496735):
																							if(angle <= -0.2172703817486763):
																								if(x_velocity > -0.30415695905685425):
																									return True
																				else:
																					return True
																		else:
																			if(angle <= -0.16770220547914505):
																				if(lander_y > 1.2468570470809937):
																					if(lander_x <= -0.10054440796375275):
																						return True
																			else:
																				if(lander_y > 1.2943825125694275):
																					if(y_velocity > -0.3899398148059845):
																						return True
																	else:
																		if(angle <= -0.24870789796113968):
																			if(y_velocity <= -0.4152718335390091):
																				if(angle <= -0.2919051945209503):
																					if(angle_velocity <= 0.12940814346075058):
																						if(y_velocity <= -0.43711379170417786):
																							if(x_velocity <= -0.25607793033123016):
																								if(lander_x > -0.29538968205451965):
																									if(x_velocity <= -0.33678731322288513):
																										if(angle > -0.39501728117465973):
																											if(y_velocity > -0.44568154215812683):
																												if(x_velocity > -0.35553309321403503):
																													return True
																				else:
																					if(lander_y > 1.2647876143455505):
																						return True
																			else:
																				if(angle_velocity <= 0.12427567690610886):
																					if(angle_velocity <= 0.03626669943332672):
																						return True
																				else:
																					if(y_velocity > -0.38959696888923645):
																						return True
																		else:
																			if(lander_y <= 1.3016756772994995):
																				if(y_velocity > -0.38997744023799896):
																					if(angle <= -0.2142021581530571):
																						if(y_velocity > -0.38691025972366333):
																							if(lander_y > 1.0195478796958923):
																								return True
																					else:
																						if(lander_y > 1.232926845550537):
																							if(lander_y <= 1.2661542296409607):
																								return True
																else:
																	if(angle_velocity <= 0.08153198659420013):
																		if(x_velocity <= -0.20065878331661224):
																			if(angle_velocity <= 0.02515404112637043):
																				if(x_velocity <= -0.2927251011133194):
																					return True
																				else:
																					if(lander_y > 1.315960168838501):
																						if(lander_y <= 1.4129882454872131):
																							return True
																			else:
																				if(lander_x > -0.1706898733973503):
																					if(x_velocity <= -0.2175237238407135):
																						return True
																					else:
																						if(lander_y <= 1.1773555278778076):
																							if(y_velocity > -0.3669579178094864):
																								return True
																						else:
																							return True
																		else:
																			if(angle > -0.1647794246673584):
																				if(lander_y <= 1.119242548942566):
																					if(angle_velocity > 0.06505804881453514):
																						return True
																				else:
																					if(angle_velocity > 0.05683406628668308):
																						if(lander_x > -0.16711640357971191):
																							return True
																	else:
																		if(x_velocity <= -0.17687823623418808):
																			if(y_velocity <= -0.373647078871727):
																				if(angle <= -0.2283104658126831):
																					if(angle_velocity <= 0.10583164915442467):
																						return True
																			else:
																				if(lander_y > 0.9352032542228699):
																					return True
																		else:
																			if(angle <= -0.1857243850827217):
																				if(y_velocity > -0.36425161361694336):
																					if(lander_x <= -0.2079010233283043):
																						if(x_velocity > -0.10532455891370773):
																							return True
																					else:
																						if(lander_y > 1.0139910280704498):
																							return True
															else:
																if(y_velocity > -0.3684648126363754):
																	if(lander_y > 1.1058405637741089):
																		if(angle <= -0.09695779904723167):
																			if(angle_velocity <= 0.016172837931662798):
																				if(y_velocity <= -0.35028357803821564):
																					if(x_velocity <= -0.1887539029121399):
																						return True
																				else:
																					return True
																			else:
																				if(lander_x <= -0.11046252027153969):
																					if(x_velocity > -0.10460624098777771):
																						return True
																				else:
																					if(angle > -0.12689248099923134):
																						if(x_velocity > -0.15471931546926498):
																							return True
														else:
															if(x_velocity <= -0.4781825542449951):
																return True
															else:
																if(y_velocity <= -0.37012022733688354):
																	if(x_velocity <= -0.2534838616847992):
																		if(y_velocity <= -0.4598539471626282):
																			if(angle_velocity > 0.03951640985906124):
																				if(y_velocity > -0.5635539889335632):
																					if(x_velocity <= -0.3460630029439926):
																						return True
																		else:
																			return True
																else:
																	return True
													else:
														if(x_velocity <= -0.1294594332575798):
															if(lander_y <= 1.0964109301567078):
																if(y_velocity <= -0.33047036826610565):
																	if(angle <= -0.10855249688029289):
																		if(angle <= -0.16138630360364914):
																			if(y_velocity > -0.3409622013568878):
																				if(lander_x > -0.1911008358001709):
																					return True
																else:
																	if(angle_velocity > -0.027879856526851654):
																		return True
															else:
																if(angle_velocity <= -0.010259217116981745):
																	if(angle_velocity <= -0.015121657401323318):
																		return True
																else:
																	return True
														else:
															if(angle_velocity <= 0.09766862168908119):
																if(lander_y <= 1.2238355875015259):
																	if(angle <= -0.10366370156407356):
																		if(y_velocity > -0.3361032158136368):
																			if(lander_y <= 1.1015729904174805):
																				if(y_velocity > -0.3212449848651886):
																					return True
																			else:
																				return True
																	else:
																		if(y_velocity > -0.31983761489391327):
																			return True
																else:
																	if(angle <= -0.05679384432733059):
																		if(angle_velocity > 0.03945926018059254):
																			return True
																	else:
																		return True
															else:
																if(lander_x <= -0.13209228217601776):
																	return True
												else:
													if(x_velocity <= 0.07830312848091125):
														if(angle <= -0.049028461799025536):
															if(angle_velocity > -0.0056668659672141075):
																if(y_velocity > -0.33644188940525055):
																	if(angle <= -0.13604997098445892):
																		if(angle_velocity > 0.12364072352647781):
																			if(angle_velocity > 0.14699287712574005):
																				return True
																	else:
																		if(lander_y > 0.9831717312335968):
																			if(angle <= -0.10840273648500443):
																				if(angle_velocity > 0.09908459335565567):
																					if(x_velocity <= -0.05165109038352966):
																						return True
																			else:
																				if(angle_velocity > 0.02375955879688263):
																					if(angle <= -0.05209057219326496):
																						if(y_velocity > -0.33621786534786224):
																							if(lander_x > -0.04987168312072754):
																								if(lander_x <= -0.04258246347308159):
																									return True
																					else:
																						return True
														else:
															if(angle_velocity > -0.017263861373066902):
																if(x_velocity <= -0.08984805643558502):
																	if(y_velocity > -0.3310033529996872):
																		return True
																else:
																	if(angle_velocity > 0.05487595312297344):
																		if(x_velocity <= -0.06072970665991306):
																			return True
											else:
												if(angle <= -0.0553903765976429):
													if(angle_velocity <= 0.03671233169734478):
														if(x_velocity <= -0.10055548325181007):
															if(lander_y <= 1.0441427826881409):
																if(angle_velocity > -0.005032745364587754):
																	if(x_velocity <= -0.1092936247587204):
																		return True
															else:
																if(lander_x <= -0.10713229328393936):
																	if(lander_x <= -0.12103839218616486):
																		return True
																else:
																	return True
														else:
															if(lander_y > 1.2491780519485474):
																return True
													else:
														if(x_velocity <= -0.008781893644481897):
															if(x_velocity <= -0.0656152106821537):
																if(y_velocity > -0.31772029399871826):
																	if(angle_velocity <= 0.12409865856170654):
																		return True
																	else:
																		if(angle_velocity > 0.12992875277996063):
																			return True
															else:
																if(angle_velocity > 0.06168821267783642):
																	if(angle <= -0.10798439756035805):
																		if(angle_velocity <= 0.12526226043701172):
																			if(lander_y > 0.9748157560825348):
																				if(lander_y <= 1.0776776671409607):
																					if(lander_x <= -0.20778391510248184):
																						return True
																		else:
																			return True
																	else:
																		if(x_velocity <= -0.033516447991132736):
																			if(x_velocity > -0.06454765796661377):
																				if(angle_velocity <= 0.06366688758134842):
																					if(angle <= -0.08179156854748726):
																						return True
																				else:
																					return True
																		else:
																			if(lander_x <= -0.22974779456853867):
																				return True
														else:
															if(angle_velocity > 0.2539850026369095):
																if(angle_velocity <= 0.28028079867362976):
																	return True
												else:
													if(lander_y <= 1.1245160102844238):
														if(angle <= -0.015948761254549026):
															if(y_velocity <= -0.3007678985595703):
																if(angle_velocity <= -0.003789520589634776):
																	if(y_velocity > -0.3148154467344284):
																		if(lander_y <= 1.0923163890838623):
																			if(lander_y > 1.080258846282959):
																				if(angle_velocity <= -0.014787520281970501):
																					return True
																else:
																	if(y_velocity > -0.30417150259017944):
																		if(angle_velocity <= 0.0249061593785882):
																			if(x_velocity <= -0.0213432339951396):
																				if(x_velocity <= -0.0866350494325161):
																					return True
																		else:
																			if(angle <= -0.03972017206251621):
																				return True
															else:
																if(x_velocity <= -0.02867597248405218):
																	if(lander_y <= 1.0179275274276733):
																		if(x_velocity <= -0.1044786274433136):
																			return True
																		else:
																			if(angle_velocity > -0.02350452821701765):
																				if(angle <= -0.04621722735464573):
																					return True
																	else:
																		if(angle_velocity > -0.012505895458161831):
																			if(y_velocity <= -0.2940923422574997):
																				if(angle_velocity <= 0.029105588793754578):
																					if(angle <= -0.041270218789577484):
																						return True
																				else:
																					return True
																			else:
																				return True
																else:
																	if(angle_velocity > 0.013016893062740564):
																		if(angle_velocity > 0.08797763288021088):
																			return True
														else:
															if(angle_velocity > -0.03197268210351467):
																if(x_velocity <= -0.09236766397953033):
																	if(angle_velocity > -0.01633040443994105):
																		return True
													else:
														if(x_velocity <= -0.05114337243139744):
															if(y_velocity <= -0.3057635873556137):
																if(x_velocity <= -0.06747142970561981):
																	if(angle_velocity <= -0.005634115310385823):
																		if(y_velocity <= -0.3119460642337799):
																			return True
																	else:
																		return True
															else:
																if(angle <= -0.03042167890816927):
																	if(angle_velocity <= 0.021263832692056894):
																		if(y_velocity <= -0.3027724474668503):
																			return True
																	else:
																		return True
																else:
																	return True
														else:
															if(angle_velocity > -0.009729324374347925):
																if(lander_x <= -0.0009590625850250944):
																	if(y_velocity <= -0.29851967096328735):
																		if(angle_velocity <= 0.008440156932920218):
																			if(angle > -0.012899728026241064):
																				if(lander_x > -0.008013629936613142):
																					return True
																		else:
																			if(angle_velocity > 0.05459572561085224):
																				if(x_velocity <= -0.034596946090459824):
																					return True
																	else:
																		if(lander_y <= 1.2052368521690369):
																			if(angle <= -0.012046248652040958):
																				if(lander_y > 1.1463180780410767):
																					return True
																		else:
																			if(lander_y <= 1.2466508150100708):
																				if(y_velocity > -0.290356770157814):
																					return True
																			else:
																				return True
								else:
									if(x_velocity <= 0.015524227172136307):
										if(angle_velocity <= 0.04227382689714432):
											if(lander_y <= 0.9449955224990845):
												if(angle <= -0.015402767807245255):
													if(x_velocity <= -0.06508280709385872):
														if(angle_velocity <= 0.017942871898412704):
															if(y_velocity <= -0.2811204195022583):
																if(angle_velocity <= -0.013506073970347643):
																	return True
																else:
																	if(angle > -0.04564303532242775):
																		if(angle_velocity > 0.006933748722076416):
																			return True
															else:
																if(y_velocity <= -0.26141560077667236):
																	return True
														else:
															if(x_velocity <= -0.101777333766222):
																return True
															else:
																if(x_velocity > -0.07272878289222717):
																	if(lander_y > 0.7930634021759033):
																		if(x_velocity <= -0.07104366645216942):
																			return True
													else:
														if(angle_velocity <= -0.008661546278744936):
															if(lander_y > 0.8945707976818085):
																if(y_velocity > -0.2810187488794327):
																	if(y_velocity > -0.2743857055902481):
																		return True
														else:
															if(angle <= -0.04194432869553566):
																if(lander_x > -0.25347161293029785):
																	if(x_velocity <= -0.04370899684727192):
																		if(angle > -0.0710131861269474):
																			if(lander_x <= -0.146842859685421):
																				return True
																			else:
																				if(y_velocity > -0.2832375317811966):
																					if(x_velocity <= -0.061524951830506325):
																						return True
																	else:
																		if(angle > -0.04754991829395294):
																			if(angle <= -0.0447126105427742):
																				if(lander_y > 0.761259138584137):
																					return True
															else:
																if(y_velocity <= -0.2726004123687744):
																	if(lander_y <= 0.9051461517810822):
																		if(angle <= -0.0164434970356524):
																			if(lander_x > 0.038593340665102005):
																				if(angle_velocity > 0.025795327965170145):
																					return True
																	else:
																		if(x_velocity <= -0.03634175006300211):
																			if(x_velocity > -0.0475185289978981):
																				return True
																else:
																	if(lander_x <= -0.042421627789735794):
																		if(x_velocity <= -0.024506441317498684):
																			return True
												else:
													if(y_velocity <= -0.270012304186821):
														if(x_velocity <= -0.016377419233322144):
															if(x_velocity <= -0.07929385080933571):
																if(lander_x <= 0.0782318115234375):
																	return True
																else:
																	if(angle_velocity > 0.01603014604188502):
																		return True
															else:
																if(angle_velocity > -0.03231810964643955):
																	if(angle <= -0.014144010841846466):
																		if(lander_y > 0.8775476217269897):
																			return True
																	else:
																		if(lander_y > 0.933695912361145):
																			if(angle <= 0.0010680061823222786):
																				return True
													else:
														if(x_velocity <= -0.041608575731515884):
															if(angle > -0.014454931486397982):
																if(angle_velocity <= -0.025408386252820492):
																	if(x_velocity <= -0.05687848851084709):
																		return True
																else:
																	return True
														else:
															if(angle > -0.009365124627947807):
																if(lander_x <= 0.04172668419778347):
																	if(lander_y <= 0.8535655438899994):
																		if(y_velocity <= -0.2688470184803009):
																			return True
																		else:
																			if(lander_x <= -0.08810577169060707):
																				if(lander_x > -0.10726046562194824):
																					return True
																	else:
																		if(x_velocity <= -0.017397197894752026):
																			return True
											else:
												if(x_velocity <= -0.02750662248581648):
													if(angle_velocity > -0.029355192556977272):
														if(angle <= -0.028561473824083805):
															if(x_velocity <= -0.08187180384993553):
																return True
															else:
																if(y_velocity <= -0.2762713134288788):
																	if(angle_velocity <= 0.026599155738949776):
																		if(angle_velocity > 0.010037757456302643):
																			if(angle_velocity <= 0.015962203964591026):
																				return True
																	else:
																		return True
																else:
																	return True
														else:
															if(lander_x > -0.05922546423971653):
																if(y_velocity <= -0.28388258814811707):
																	if(lander_y > 1.0503873825073242):
																		return True
																else:
																	if(lander_x <= 0.0641079917550087):
																		return True
																	else:
																		if(lander_x > 0.0650944709777832):
																			return True
												else:
													if(angle_velocity <= 0.01791199017316103):
														if(angle <= 0.02093520388007164):
															if(lander_y > 0.9808626770973206):
																if(angle > 0.011638423427939415):
																	if(lander_x <= 0.016232823953032494):
																		if(angle > 0.014327658340334892):
																			return True
													else:
														if(x_velocity <= -0.022695248015224934):
															if(lander_x > -0.04166054632514715):
																return True
														else:
															if(angle_velocity <= 0.04090994782745838):
																if(angle_velocity <= 0.023044532164931297):
																	if(angle <= -0.0038583377609029412):
																		return True
																else:
																	return True
										else:
											if(lander_y <= 0.7757551670074463):
												if(angle <= -0.08683010935783386):
													if(lander_y <= 0.766150176525116):
														return True
												else:
													if(x_velocity <= -0.0165997426956892):
														if(y_velocity > -0.28112266957759857):
															if(angle_velocity > 0.05906456150114536):
																return True
											else:
												if(x_velocity <= -0.0007985317497514188):
													if(y_velocity <= -0.2753151059150696):
														if(angle_velocity <= 0.0611433032900095):
															if(angle <= -0.06968993693590164):
																if(lander_x <= -0.14791449904441833):
																	return True
															else:
																if(lander_y <= 0.9312511086463928):
																	if(x_velocity <= -0.039910824969410896):
																		return True
																else:
																	if(lander_x <= -0.022850417532026768):
																		return True
														else:
															if(y_velocity > -0.28602685034275055):
																if(lander_y <= 1.1093484163284302):
																	return True
																else:
																	if(lander_y > 1.2606794238090515):
																		return True
													else:
														if(angle <= -0.09860137477517128):
															if(angle <= -0.12000813707709312):
																return True
															else:
																if(lander_y > 0.9309572279453278):
																	return True
														else:
															if(lander_y <= 0.7897994220256805):
																if(lander_y <= 0.786220133304596):
																	return True
															else:
																return True
												else:
													if(angle_velocity <= 0.060412293300032616):
														if(angle > -0.06914813071489334):
															if(angle > 0.008634249912574887):
																return True
													else:
														if(y_velocity > -0.2839789241552353):
															if(angle <= 0.0011150131758768111):
																return True
															else:
																if(angle_velocity > 0.07279662787914276):
																	return True
									else:
										if(lander_y <= 1.027734100818634):
											if(angle_velocity <= 0.19868455827236176):
												if(angle_velocity <= 0.03819133900105953):
													if(angle <= -0.005042276810854673):
														if(lander_x <= -0.29285429418087006):
															if(y_velocity > -0.27130232751369476):
																if(lander_y <= 0.7967526912689209):
																	return True
												else:
													if(y_velocity <= -0.26225630939006805):
														if(lander_y > 0.8528149425983429):
															if(angle <= -0.019997977651655674):
																if(lander_x > -0.3382154703140259):
																	if(y_velocity > -0.2685592323541641):
																		return True
															else:
																if(lander_y > 1.0097745656967163):
																	if(y_velocity > -0.27412787079811096):
																		return True
													else:
														if(lander_x <= -0.13444466888904572):
															return True
											else:
												return True
										else:
											if(y_velocity <= -0.27959856390953064):
												if(y_velocity > -0.28085172176361084):
													if(angle <= 0.016716327518224716):
														return True
											else:
												if(angle_velocity <= 0.1332056187093258):
													if(angle > 0.014942340552806854):
														if(y_velocity > -0.2724715769290924):
															return True
												else:
													return True
							else:
								if(y_velocity <= -0.27584148943424225):
									if(x_velocity <= -0.4281509518623352):
										return True
									else:
										if(angle <= 0.46151159703731537):
											if(lander_y <= 1.281448781490326):
												if(lander_x <= 0.07046699523925781):
													if(lander_x <= 0.07010574266314507):
														if(y_velocity > -0.42698056995868683):
															if(y_velocity > -0.28613579273223877):
																if(y_velocity <= -0.2858380228281021):
																	if(x_velocity <= 0.031264145189197734):
																		return True
																else:
																	if(lander_x <= 0.059750746935606):
																		if(lander_y > 1.1131130456924438):
																			if(angle <= 0.06077605113387108):
																				if(y_velocity > -0.2832896411418915):
																					if(x_velocity <= 0.045092782005667686):
																						return True
																	else:
																		return True
											else:
												if(x_velocity <= 0.42733925580978394):
													if(angle <= 0.04763258434832096):
														if(x_velocity <= 0.34170304238796234):
															if(y_velocity > -0.2994955778121948):
																if(angle_velocity > 0.06817084550857544):
																	if(lander_y <= 1.347132384777069):
																		return True
										else:
											if(y_velocity <= -0.2788342982530594):
												if(x_velocity <= 0.08405783027410507):
													if(angle_velocity > -0.011437477078288794):
														return True
											else:
												return True
								else:
									if(angle <= 0.4801601767539978):
										if(angle <= 0.07749898359179497):
											if(lander_y <= 0.9992907345294952):
												if(angle_velocity > -0.03134584240615368):
													if(x_velocity <= -0.04115448147058487):
														if(y_velocity <= -0.2683117389678955):
															return True
													else:
														if(x_velocity <= 0.030899989418685436):
															if(y_velocity <= -0.2625493109226227):
																if(angle <= 0.024610111489892006):
																	if(angle > 0.02446788363158703):
																		return True
															else:
																if(lander_y > 0.8922903537750244):
																	return True
											else:
												if(x_velocity <= -0.0016471044509671628):
													if(angle_velocity <= 0.005621369840810075):
														if(angle > 0.023702352307736874):
															return True
													else:
														if(x_velocity <= -0.023332281969487667):
															return True
												else:
													if(lander_y <= 1.1409984827041626):
														if(y_velocity > -0.2676937133073807):
															if(x_velocity <= 0.023460568860173225):
																return True
													else:
														if(x_velocity <= 0.06683329120278358):
															if(angle_velocity > -0.014909314457327127):
																if(angle <= 0.03697366826236248):
																	if(angle_velocity > 0.07720512337982655):
																		return True
																else:
																	return True
										else:
											if(lander_x <= 0.042531490325927734):
												if(y_velocity <= -0.26233261823654175):
													if(lander_y <= 1.1407285928726196):
														return True
													else:
														if(x_velocity <= 0.052847832441329956):
															if(y_velocity <= -0.269765242934227):
																return True
												else:
													return True
									else:
										if(x_velocity <= 0.17136754840612411):
											return True
					else:
						if(x_velocity <= -0.0031562260119244456):
							if(lander_y <= 0.6404740214347839):
								if(y_velocity <= -0.24344873428344727):
									if(x_velocity <= -0.06039332039654255):
										if(y_velocity <= -0.25149276852607727):
											if(angle <= -0.052637698128819466):
												if(x_velocity <= -0.07406633719801903):
													if(angle > -0.07045106589794159):
														if(lander_x <= 0.04302477976307273):
															return True
											else:
												if(lander_y <= 0.5075192451477051):
													if(x_velocity <= -0.09953827410936356):
														if(angle_velocity > -0.008703956351382658):
															return True
													else:
														if(angle_velocity > -0.019486697390675545):
															if(lander_x <= -0.02772045088931918):
																return True
												else:
													if(x_velocity <= -0.07289041206240654):
														if(angle_velocity > -0.031676873564720154):
															if(y_velocity <= -0.2521260380744934):
																return True
													else:
														if(x_velocity > -0.0684046596288681):
															if(lander_x <= 0.04579372517764568):
																return True
															else:
																if(x_velocity > -0.06336255371570587):
																	if(angle_velocity > 0.010023372946307063):
																		return True
										else:
											if(angle_velocity <= -0.01959348376840353):
												if(lander_x <= 0.1270311400294304):
													if(angle <= -0.015862680040299892):
														return True
												else:
													if(y_velocity <= -0.2499309778213501):
														return True
											else:
												if(y_velocity <= -0.25109076499938965):
													if(lander_x > 0.030603693798184395):
														return True
												else:
													if(angle <= -0.01704938057810068):
														return True
													else:
														if(angle_velocity <= 0.01485033379867673):
															return True
									else:
										if(angle_velocity <= -0.01589978439733386):
											if(angle <= -0.012967045418918133):
												if(lander_x <= -0.17397456616163254):
													return True
										else:
											if(angle <= -0.01587140467017889):
												if(y_velocity <= -0.25238659977912903):
													if(angle <= -0.07502445578575134):
														return True
													else:
														if(x_velocity <= -0.05832513049244881):
															return True
														else:
															if(lander_y <= 0.6256686747074127):
																if(angle_velocity > 0.0064967426005750895):
																	if(y_velocity > -0.25620295107364655):
																		if(y_velocity <= -0.2560510039329529):
																			return True
												else:
													if(lander_y <= 0.4490576684474945):
														if(angle <= -0.0433986522257328):
															if(angle <= -0.05176094174385071):
																return True
													else:
														if(angle_velocity <= 0.005488356575369835):
															if(x_velocity <= -0.05075988546013832):
																return True
															else:
																if(angle_velocity <= -0.00937642203643918):
																	return True
														else:
															if(lander_x <= -0.06326909177005291):
																return True
															else:
																if(x_velocity <= -0.02738816197961569):
																	if(y_velocity > -0.25114990770816803):
																		return True
											else:
												if(lander_y <= 0.6370363831520081):
													if(y_velocity > -0.24830061942338943):
														if(x_velocity <= -0.04007616080343723):
															if(lander_y <= 0.5664487481117249):
																if(lander_x <= 0.0707700252532959):
																	return True
															else:
																return True
														else:
															if(lander_y > 0.6330767869949341):
																return True
								else:
									if(angle <= 0.02445459645241499):
										if(angle_velocity <= -0.010594240389764309):
											if(x_velocity <= -0.06686000898480415):
												if(lander_y <= 0.4584890604019165):
													if(angle <= -0.037527257576584816):
														if(x_velocity <= -0.11899762600660324):
															return True
													else:
														return True
												else:
													return True
											else:
												if(lander_x <= -0.0601667407900095):
													if(angle_velocity > -0.026763037778437138):
														if(lander_y > 0.4152933359146118):
															return True
												else:
													if(angle <= -0.008313758298754692):
														if(angle_velocity > -0.015609695110470057):
															if(lander_y > 0.5234057009220123):
																return True
													else:
														if(y_velocity <= -0.23741857707500458):
															if(angle <= -0.006637597922235727):
																if(y_velocity > -0.24024755507707596):
																	return True
														else:
															if(lander_x <= -0.0330034252256155):
																return True
															else:
																if(x_velocity <= -0.050365911796689034):
																	if(angle_velocity <= -0.018073328770697117):
																		return True
										else:
											if(x_velocity <= -0.01786466594785452):
												if(lander_x <= 0.1260085552930832):
													if(angle <= -0.042609021067619324):
														if(angle_velocity <= 0.011550815310329199):
															if(y_velocity > -0.2373959869146347):
																if(lander_y <= 0.5282864272594452):
																	return True
														else:
															if(angle <= -0.043867696076631546):
																return True
													else:
														if(y_velocity <= -0.24284666776657104):
															if(angle <= -0.012368390802294016):
																return True
														else:
															if(lander_x <= 0.06515040248632431):
																if(angle <= -0.03354115970432758):
																	if(angle <= -0.03557468019425869):
																		return True
																else:
																	return True
															else:
																if(x_velocity <= -0.036348216235637665):
																	return True
																else:
																	if(y_velocity <= -0.2354392409324646):
																		if(y_velocity <= -0.23693405836820602):
																			if(lander_y > 0.5332871377468109):
																				return True
																	else:
																		if(angle_velocity > 0.004569892073050141):
																			return True
												else:
													if(lander_y <= 0.5181255340576172):
														if(y_velocity <= -0.23288510739803314):
															if(lander_x > 0.1619691401720047):
																return True
														else:
															return True
													else:
														if(angle_velocity <= 0.037727318704128265):
															return True
														else:
															if(lander_x <= 0.1447037234902382):
																return True
											else:
												if(lander_x <= 0.0003012180095538497):
													if(y_velocity > -0.24066445976495743):
														if(angle_velocity <= 0.015264656394720078):
															if(y_velocity > -0.23373811691999435):
																if(y_velocity <= -0.22842319309711456):
																	if(lander_x <= -0.09522390365600586):
																		return True
																else:
																	return True
														else:
															return True
												else:
													if(lander_x > 0.014161825180053711):
														if(angle_velocity > 0.01480414578691125):
															if(angle <= -0.013240710832178593):
																return True
									else:
										if(lander_x <= -0.023941373452544212):
											return True
							else:
								if(angle_velocity <= 0.004404015140607953):
									if(lander_y <= 0.889331191778183):
										if(y_velocity <= -0.2563770264387131):
											if(angle <= 0.00019111810252070427):
												if(lander_x > -0.10800261422991753):
													if(lander_y <= 0.6656315922737122):
														if(lander_x <= 0.02359118452295661):
															return True
													else:
														return True
											else:
												if(angle > 0.04863712377846241):
													return True
										else:
											if(x_velocity <= -0.035182226449251175):
												if(angle <= -0.012895056512206793):
													if(lander_x <= 0.155231811106205):
														if(x_velocity <= -0.04647834226489067):
															if(angle_velocity <= -0.00507610198110342):
																if(lander_x <= -0.00315556516579818):
																	if(angle_velocity <= -0.005973226157948375):
																		return True
																else:
																	if(x_velocity <= -0.056853245943784714):
																		if(lander_x <= 0.08292656019330025):
																			if(x_velocity <= -0.07345131039619446):
																				return True
																			else:
																				if(angle > -0.01731928624212742):
																					return True
																		else:
																			if(lander_x > 0.1478385478258133):
																				return True
															else:
																return True
														else:
															if(lander_y > 0.7306103110313416):
																return True
												else:
													if(angle_velocity <= -0.01736298482865095):
														if(angle_velocity <= -0.020350169390439987):
															if(angle <= -0.002092047070618719):
																if(angle <= -0.005188233917579055):
																	return True
															else:
																return True
													else:
														if(y_velocity <= -0.2547205984592438):
															if(x_velocity <= -0.055073849856853485):
																return True
														else:
															return True
											else:
												if(lander_x <= -0.013243150431662798):
													if(angle_velocity > -0.03206194378435612):
														if(angle_velocity <= -0.02984893135726452):
															if(y_velocity > -0.24922583997249603):
																return True
														else:
															return True
												else:
													if(angle <= 0.032609907910227776):
														if(angle <= 0.018990540876984596):
															if(angle_velocity > -0.0018641488859429955):
																if(lander_y <= 0.7314731478691101):
																	return True
														else:
															if(lander_x <= 0.09156174957752228):
																if(x_velocity <= -0.009674486238509417):
																	return True
													else:
														if(y_velocity > -0.24763967841863632):
															return True
									else:
										if(x_velocity <= -0.005072366213425994):
											if(angle_velocity <= -0.02592717669904232):
												if(x_velocity <= -0.01937578897923231):
													if(lander_x <= 0.1564117893576622):
														return True
													else:
														if(lander_y > 1.0071746706962585):
															return True
												else:
													if(lander_y <= 0.9797953069210052):
														return True
											else:
												if(lander_x <= -0.02310938760638237):
													if(x_velocity <= -0.015252894721925259):
														return True
												else:
													return True
								else:
									if(y_velocity <= -0.25405117869377136):
										if(lander_y <= 0.6789322793483734):
											if(angle <= -0.03022855520248413):
												return True
										else:
											if(angle <= -0.03126440942287445):
												if(angle_velocity <= 0.03554973937571049):
													if(lander_y <= 0.7018381059169769):
														return True
													else:
														if(lander_x <= -0.1862165406346321):
															if(lander_x > -0.20063187927007675):
																return True
												else:
													return True
											else:
												if(angle <= 0.032678719609975815):
													if(y_velocity <= -0.25985635817050934):
														if(y_velocity <= -0.25999659299850464):
															return True
													else:
														return True
												else:
													if(lander_y > 0.8699574768543243):
														return True
									else:
										if(lander_x <= 0.0815114974975586):
											return True
										else:
											if(lander_x > 0.0852104164659977):
												if(y_velocity <= -0.2509196400642395):
													if(x_velocity <= -0.060327403247356415):
														return True
													else:
														if(lander_y > 0.7441609501838684):
															if(lander_y > 0.7657613754272461):
																return True
												else:
													return True
						else:
							if(lander_y <= 0.6782035827636719):
								if(y_velocity <= -0.24171631038188934):
									if(angle <= -0.007669943850487471):
										if(angle_velocity > -0.00637316657230258):
											if(angle <= -0.07778352499008179):
												if(angle_velocity <= 0.2345825880765915):
													if(lander_y <= 0.45886167883872986):
														return True
												else:
													return True
											else:
												if(angle <= -0.008114891592413187):
													if(angle_velocity > 0.019101232290267944):
														if(x_velocity <= 0.028966717422008514):
															if(lander_y <= 0.617910772562027):
																if(lander_y > 0.5552093386650085):
																	if(y_velocity > -0.24796930700540543):
																		return True
															else:
																if(lander_y > 0.6395766735076904):
																	return True
														else:
															if(y_velocity > -0.2502943277359009):
																if(y_velocity > -0.24990147352218628):
																	if(angle_velocity > 0.08107097074389458):
																		if(lander_x > -0.23189949989318848):
																			if(lander_y > 0.5135963261127472):
																				if(lander_x > -0.2213435396552086):
																					return True
									else:
										if(lander_y > 0.6139775216579437):
											if(angle_velocity > -0.009488389594480395):
												if(y_velocity <= -0.24195438623428345):
													if(angle <= 0.010575601365417242):
														if(angle_velocity <= 0.031161028891801834):
															if(x_velocity <= 0.07554014772176743):
																if(angle <= 0.009950333274900913):
																	if(angle_velocity > 0.019285897724330425):
																		return True
												else:
													return True
								else:
									if(angle <= 0.013375560287386179):
										if(angle_velocity <= 0.013561869505792856):
											if(y_velocity <= -0.2267807349562645):
												if(lander_x <= -0.21681082248687744):
													if(angle <= 0.001464070926886052):
														if(x_velocity <= 0.05326969921588898):
															if(angle_velocity <= -0.004545956966467202):
																if(lander_y > 0.497398242354393):
																	return True
															else:
																return True
												else:
													if(lander_y <= 0.4119488000869751):
														if(x_velocity > 0.009427490178495646):
															return True
													else:
														if(x_velocity <= 0.0024043101584538817):
															if(y_velocity > -0.23941097408533096):
																if(angle_velocity > -0.0018066087504848838):
																	return True
														else:
															if(lander_x <= -0.1056583859026432):
																if(x_velocity <= 0.05768898129463196):
																	if(angle <= 0.0019282285938970745):
																		if(x_velocity <= 0.05442582629621029):
																			if(lander_x <= -0.18547696620225906):
																				if(x_velocity <= 0.034452106803655624):
																					if(angle > -0.009836547076702118):
																						return True
																	else:
																		if(x_velocity <= 0.0122235924936831):
																			return True
											else:
												if(x_velocity <= 0.0576079897582531):
													if(lander_x <= -0.0866231918334961):
														return True
										else:
											if(y_velocity <= -0.2323838621377945):
												if(angle <= -0.017087535001337528):
													if(angle_velocity <= 0.05514552257955074):
														if(lander_y <= 0.552348256111145):
															if(angle_velocity > 0.03485310636460781):
																return True
													else:
														if(lander_x <= -0.13679399341344833):
															if(x_velocity <= 0.12649815529584885):
																return True
												else:
													if(lander_y <= 0.5022633373737335):
														if(x_velocity <= 0.014691042713820934):
															if(angle_velocity <= 0.0686153769493103):
																if(lander_y <= 0.42673711478710175):
																	return True
															else:
																return True
													else:
														if(angle_velocity <= 0.043021826073527336):
															if(angle_velocity <= 0.03569735586643219):
																if(lander_x > -0.22361929714679718):
																	if(x_velocity <= 0.016786151565611362):
																		if(angle_velocity > 0.018224431201815605):
																			return True
															else:
																if(lander_y <= 0.6595658659934998):
																	return True
											else:
												if(y_velocity <= -0.22693373262882233):
													if(angle <= -0.001148426381405443):
														if(lander_x <= -0.05325303040444851):
															if(angle <= -0.02865183725953102):
																if(lander_x <= -0.17642078548669815):
																	if(angle <= -0.04011384770274162):
																		return True
															else:
																if(angle_velocity > 0.015399147756397724):
																	return True
													else:
														if(x_velocity <= 0.029866842553019524):
															if(lander_y > 0.48457862436771393):
																return True
														else:
															if(lander_y > 0.6139527559280396):
																if(angle_velocity > 0.07019239291548729):
																	if(lander_y <= 0.6493671834468842):
																		return True
												else:
													if(angle > -0.03398860339075327):
														return True
									else:
										if(angle_velocity <= -0.007965500000864267):
											if(lander_y <= 0.5712693631649017):
												if(angle > 0.015446372795850039):
													if(y_velocity > -0.23750809580087662):
														if(angle <= 0.03104319889098406):
															if(lander_y <= 0.5300270020961761):
																if(angle_velocity <= -0.018493170849978924):
																	if(y_velocity <= -0.23020152002573013):
																		if(lander_x <= -0.06969141773879528):
																			if(angle <= 0.027289587073028088):
																				return True
														else:
															if(lander_y <= 0.42854906618595123):
																if(angle_velocity <= -0.025564314797520638):
																	return True
											else:
												if(lander_x > -0.23724763840436935):
													if(x_velocity <= 0.05604192614555359):
														if(lander_x <= -0.0666357520967722):
															if(x_velocity <= 0.03696584515273571):
																return True
										else:
											if(x_velocity <= 0.06353048235177994):
												if(lander_x <= -0.12678442150354385):
													if(lander_y > 0.49421779811382294):
														if(y_velocity > -0.23695968091487885):
															if(angle <= 0.019469118677079678):
																if(y_velocity <= -0.23121558129787445):
																	return True
															else:
																return True
												else:
													if(y_velocity <= -0.22701957821846008):
														if(lander_y > 0.585104376077652):
															if(lander_y <= 0.5877785384654999):
																return True
															else:
																if(angle > 0.032382840290665627):
																	return True
													else:
														if(y_velocity <= -0.2264140397310257):
															return True
											else:
												if(angle_velocity > 0.007223339751362801):
													if(angle > 0.014735022094100714):
														if(y_velocity > -0.2248585820198059):
															if(angle_velocity > 0.055678676813840866):
																return True
							else:
								if(angle <= 0.10295573249459267):
									if(angle_velocity <= 0.042507754638791084):
										if(y_velocity <= -0.24878141283988953):
											if(lander_y <= 0.8880913555622101):
												if(angle <= -0.008234894834458828):
													if(angle_velocity <= 0.033598922193050385):
														if(x_velocity <= 0.07583780214190483):
															if(x_velocity <= 0.010667488910257816):
																if(x_velocity > 0.004334267621743493):
																	return True
												else:
													if(angle_velocity <= -0.009366677608340979):
														if(angle <= 0.03616303578019142):
															if(x_velocity <= 0.011128692887723446):
																if(lander_x <= -0.0501461997628212):
																	return True
													else:
														if(lander_x <= -0.05180711857974529):
															if(lander_y <= 0.7781370282173157):
																if(angle_velocity > -0.0005504920845851302):
																	if(angle <= -0.0077021608594805):
																		return True
															else:
																if(x_velocity <= 0.02442897390574217):
																	return True
											else:
												if(angle <= 0.03284945897758007):
													if(angle_velocity <= 0.0365157425403595):
														if(y_velocity <= -0.2595241367816925):
															if(lander_x > -0.06111025810241699):
																return True
													else:
														return True
												else:
													if(x_velocity <= 0.052442971616983414):
														if(lander_x <= 0.1016031764447689):
															if(lander_y <= 1.1686013340950012):
																if(angle_velocity <= 0.014928619842976332):
																	if(x_velocity <= 0.01401378819718957):
																		if(angle_velocity <= -0.01967438729479909):
																			return True
																else:
																	return True
															else:
																return True
														else:
															if(angle_velocity <= -0.023328247480094433):
																if(lander_x <= 0.10581402853131294):
																	return True
													else:
														if(y_velocity > -0.25468458235263824):
															if(angle <= 0.10042272508144379):
																if(lander_x > 0.02957077044993639):
																	if(y_velocity <= -0.2497774437069893):
																		return True
										else:
											if(lander_y <= 0.8257634937763214):
												if(angle_velocity <= -0.007427188102155924):
													if(angle_velocity <= -0.010084525682032108):
														if(x_velocity <= 3.487712820060551e-05):
															if(angle_velocity > -0.019358133897185326):
																return True
												else:
													if(x_velocity <= 0.043249502778053284):
														if(y_velocity <= -0.2370046228170395):
															if(x_velocity <= 0.010765003971755505):
																if(lander_y > 0.6931203007698059):
																	return True
															else:
																if(lander_x <= -0.16030530631542206):
																	return True
																else:
																	if(y_velocity > -0.23792554438114166):
																		if(x_velocity <= 0.013965237885713577):
																			return True
														else:
															if(angle_velocity <= 0.038914481177926064):
																return True
													else:
														if(angle <= 0.03740200214087963):
															if(angle_velocity <= 0.03658078983426094):
																if(lander_y <= 0.6787808537483215):
																	return True
															else:
																if(lander_x <= -0.35036981105804443):
																	return True
											else:
												if(angle <= 0.029133042320609093):
													if(x_velocity <= 0.02190345898270607):
														if(y_velocity > -0.24772899597883224):
															if(y_velocity <= -0.24310211092233658):
																return True
												else:
													if(angle_velocity <= -0.01388505706563592):
														if(angle > 0.04368908703327179):
															if(lander_x > 0.04123663902282715):
																if(angle <= 0.05412131920456886):
																	if(lander_x > 0.05120539665222168):
																		return True
																else:
																	return True
													else:
														if(x_velocity <= 0.08881065249443054):
															return True
									else:
										if(x_velocity <= 0.1433681845664978):
											if(lander_y <= 0.7128623425960541):
												if(y_velocity <= -0.23475246876478195):
													if(x_velocity <= 0.04234972223639488):
														if(lander_x <= -0.11548614501953125):
															return True
														else:
															if(x_velocity > 0.030800731852650642):
																return True
													else:
														if(angle_velocity <= 0.13825778663158417):
															if(lander_x <= -0.3019168972969055):
																return True
														else:
															return True
												else:
													if(y_velocity <= -0.22491396218538284):
														return True
											else:
												if(y_velocity <= -0.24383505433797836):
													if(angle <= -0.04584505222737789):
														if(angle_velocity > 0.06662938743829727):
															if(x_velocity <= 0.07981361076235771):
																if(y_velocity > -0.2601442039012909):
																	if(lander_y <= 0.7318928837776184):
																		if(angle > -0.060628389939665794):
																			return True
																	else:
																		return True
													else:
														if(lander_y <= 0.7992344200611115):
															if(x_velocity <= 0.05489739216864109):
																if(lander_y <= 0.781582772731781):
																	if(x_velocity <= 0.04552813433110714):
																		return True
																	else:
																		if(angle <= -0.03147723991423845):
																			return True
																else:
																	if(y_velocity > -0.24961332231760025):
																		return True
														else:
															if(lander_x > -0.338242769241333):
																if(lander_y <= 1.4189164638519287):
																	if(y_velocity <= -0.24742591381072998):
																		if(x_velocity <= 0.016765374690294266):
																			if(y_velocity > -0.2541370987892151):
																				return True
																		else:
																			return True
																	else:
																		if(y_velocity > -0.24654389917850494):
																			return True
																else:
																	if(x_velocity <= 0.1303340345621109):
																		return True
												else:
													if(x_velocity <= 0.13658814877271652):
														if(angle <= -0.06513085588812828):
															if(lander_y > 0.8160543739795685):
																return True
														else:
															return True
								else:
									if(y_velocity <= -0.23747292160987854):
										if(angle <= 0.4293469339609146):
											if(lander_x <= 0.05115861818194389):
												if(x_velocity <= 0.13500040024518967):
													if(angle <= 0.11096933484077454):
														if(lander_y > 1.2102004885673523):
															if(x_velocity <= 0.11366458982229233):
																return True
													else:
														return True
												else:
													if(lander_y <= 1.4222301244735718):
														if(lander_x <= 0.03817935101687908):
															if(lander_x > 0.036213064566254616):
																return True
											else:
												if(angle <= 0.3634513318538666):
													if(lander_x <= 0.069710873067379):
														if(lander_x <= 0.0687967799603939):
															if(angle_velocity > -0.027906393632292747):
																if(y_velocity > -0.2599165290594101):
																	if(lander_y <= 1.4051954746246338):
																		if(lander_x <= 0.05755038373172283):
																			if(lander_x <= 0.057309580966830254):
																				if(angle <= 0.13579915463924408):
																					if(x_velocity > 0.14063924551010132):
																						if(lander_y > 1.3546212315559387):
																							return True
																			else:
																				return True
																	else:
																		if(angle <= 0.14150158315896988):
																			if(x_velocity <= 0.21210245043039322):
																				if(x_velocity <= 0.16459538042545319):
																					if(y_velocity > -0.25008321553468704):
																						return True
																		else:
																			return True
														else:
															if(lander_y > 1.187575101852417):
																return True
												else:
													if(y_velocity <= -0.24047396332025528):
														if(angle <= 0.3823806792497635):
															if(y_velocity > -0.2507116347551346):
																return True
														else:
															if(x_velocity <= 0.12505142763257027):
																return True
															else:
																if(y_velocity > -0.2495308592915535):
																	if(y_velocity <= -0.2468038946390152):
																		return True
													else:
														return True
										else:
											if(x_velocity <= 0.24664103984832764):
												if(angle <= 0.4505787491798401):
													if(angle <= 0.43866419792175293):
														return True
												else:
													return True
									else:
										if(x_velocity <= 0.12892448157072067):
											if(lander_x <= 0.04707613028585911):
												if(x_velocity <= 0.1123315803706646):
													return True
											else:
												return True
										else:
											if(angle <= 0.3770904541015625):
												if(lander_y <= 1.356264591217041):
													if(angle <= 0.2588009312748909):
														if(lander_x > 0.05328202247619629):
															if(lander_y <= 1.3061116337776184):
																if(y_velocity > -0.22721433639526367):
																	if(x_velocity <= 0.17450890690088272):
																		return True
															else:
																if(lander_y <= 1.3299434185028076):
																	return True
													else:
														if(x_velocity <= 0.2344096377491951):
															if(lander_x <= 0.1925528571009636):
																return True
												else:
													if(y_velocity <= -0.2308005914092064):
														if(x_velocity > 0.13182853162288666):
															if(y_velocity <= -0.23138921707868576):
																if(angle <= 0.16412196308374405):
																	return True
																else:
																	if(x_velocity > 0.1717679351568222):
																		if(x_velocity <= 0.20298302918672562):
																			return True
											else:
												if(x_velocity <= 0.3085941970348358):
													return True
		else:
			if(angle_velocity <= -0.01109519088640809):
				if(right_leg_contact != True):
					if(lander_y <= 0.5234372615814209):
						if(y_velocity <= -0.1971578523516655):
							if(angle <= 0.0107335583306849):
								if(x_velocity <= -0.04500272683799267):
									if(angle_velocity <= -0.03327598422765732):
										if(angle <= -0.008505767676979303):
											if(y_velocity <= -0.20618872344493866):
												if(x_velocity <= -0.08068354055285454):
													if(lander_y > 0.1223687157034874):
														return True
												else:
													if(lander_x <= -0.16330795362591743):
														return True
													else:
														if(angle_velocity > -0.04211241379380226):
															if(lander_y > 0.05079450458288193):
																if(lander_x <= 0.003806733526289463):
																	if(x_velocity <= -0.06500869616866112):
																		return True
											else:
												if(y_velocity <= -0.2041017785668373):
													return True
												else:
													if(x_velocity <= -0.09441464766860008):
														return True
													else:
														if(lander_y <= 0.029630658216774464):
															return True
										else:
											if(lander_y <= 0.21201618760824203):
												if(angle_velocity <= -0.06125285662710667):
													if(lander_x > 0.07096729148179293):
														if(x_velocity <= -0.08806149661540985):
															return True
											else:
												if(angle <= -0.0007596094947075471):
													return True
									else:
										if(lander_x <= -0.04515476152300835):
											return True
										else:
											if(lander_y <= 0.08018750697374344):
												if(y_velocity > -0.2137577161192894):
													if(x_velocity <= -0.07389353215694427):
														return True
											else:
												if(y_velocity <= -0.2175784334540367):
													if(lander_y <= 0.3196537494659424):
														if(x_velocity <= -0.05980289727449417):
															if(lander_x <= 0.04013786278665066):
																return True
															else:
																if(y_velocity <= -0.2228735014796257):
																	return True
													else:
														if(x_velocity <= -0.048792796209454536):
															return True
												else:
													if(angle <= -0.022246772423386574):
														if(lander_x <= 0.04974265210330486):
															return True
														else:
															if(x_velocity <= -0.09106046706438065):
																return True
													else:
														return True
								else:
									if(angle_velocity <= -0.03873600624501705):
										if(angle <= 0.009614271577447653):
											if(lander_y <= 0.38996393978595734):
												if(y_velocity > -0.2237100526690483):
													if(lander_y > 0.04265764728188515):
														if(angle <= -0.0033316476037725806):
															if(angle_velocity <= -0.0416334867477417):
																if(y_velocity > -0.2038421705365181):
																	if(y_velocity <= -0.20269667357206345):
																		return True
															else:
																if(lander_y <= 0.2587813660502434):
																	if(angle_velocity <= -0.04149291478097439):
																		return True
																else:
																	return True
														else:
															if(angle <= -0.0019331203075125813):
																if(lander_x <= -0.11544475331902504):
																	return True
											else:
												if(angle_velocity > -0.05217112973332405):
													if(lander_y <= 0.4278799444437027):
														return True
										else:
											if(lander_y <= 0.49673160910606384):
												if(x_velocity <= 0.023714778944849968):
													return True
									else:
										if(angle <= -0.017591786570847034):
											if(lander_x <= -0.06204400025308132):
												if(x_velocity <= -0.009615412447601557):
													if(angle <= -0.022226118482649326):
														if(lander_x <= -0.17760396003723145):
															if(angle <= -0.05206279829144478):
																if(x_velocity <= -0.03890976682305336):
																	return True
															else:
																return True
														else:
															if(angle <= -0.030797327868640423):
																if(y_velocity > -0.2020140364766121):
																	return True
															else:
																if(y_velocity <= -0.20748993754386902):
																	if(lander_y > 0.16800661385059357):
																		if(angle_velocity > -0.024481746833771467):
																			return True
													else:
														return True
										else:
											if(lander_y <= 0.3056928813457489):
												if(y_velocity <= -0.2121613472700119):
													if(lander_y > 0.17421792447566986):
														if(y_velocity <= -0.21849275380373):
															if(lander_x > -0.2251472920179367):
																if(x_velocity <= 0.042945344001054764):
																	if(lander_x <= -0.060500429943203926):
																		if(x_velocity <= -0.042161500081419945):
																			return True
														else:
															if(x_velocity <= 0.014525707345455885):
																if(angle > -0.003087206627242267):
																	if(angle_velocity <= -0.02701878733932972):
																		return True
												else:
													if(lander_y > 0.02314615063369274):
														if(lander_x <= 0.014187526423484087):
															if(x_velocity <= -0.001215156189573463):
																if(angle <= 0.0037311719497665763):
																	return True
															else:
																if(angle <= -0.0017017050413414836):
																	if(angle_velocity > -0.013581103645265102):
																		if(x_velocity <= 0.04162782244384289):
																			if(lander_x <= -0.23897194862365723):
																				return True
																else:
																	if(lander_y > 0.11638302728533745):
																		if(angle <= 0.006933571537956595):
																			return True
											else:
												if(lander_x <= -0.02732639294117689):
													if(x_velocity <= 0.04054240509867668):
														if(lander_x <= -0.20129163563251495):
															return True
														else:
															if(x_velocity <= 0.006260686321184039):
																if(angle > -0.015639803372323513):
																	if(angle_velocity <= -0.03039668034762144):
																		if(x_velocity <= -0.011379038216546178):
																			return True
																	else:
																		return True
															else:
																if(angle > 0.002376112388446927):
																	if(lander_y > 0.33565984666347504):
																		return True
													else:
														if(angle > 0.009536838624626398):
															return True
												else:
													if(angle > 0.0015949156950227916):
														if(angle <= 0.004241250571794808):
															return True
							else:
								if(angle_velocity <= -0.06347468122839928):
									if(angle <= 0.11405843868851662):
										if(lander_y > 0.1087837889790535):
											if(angle > 0.052092377096414566):
												if(y_velocity > -0.2149878814816475):
													if(y_velocity > -0.2003796547651291):
														return True
									else:
										if(angle > 0.18815135210752487):
											return True
								else:
									if(lander_y <= 0.15496191382408142):
										if(y_velocity <= -0.20434628427028656):
											if(angle > 0.02040480077266693):
												if(x_velocity <= 0.08594369143247604):
													if(angle_velocity > -0.012429318856447935):
														if(angle <= 0.02965648379176855):
															return True
										else:
											if(angle_velocity > -0.031124630942940712):
												if(angle <= 0.020403779111802578):
													if(y_velocity <= -0.2004377841949463):
														return True
									else:
										if(angle <= 0.042803024873137474):
											if(y_velocity <= -0.21623970568180084):
												if(lander_y > 0.34502965211868286):
													if(angle <= 0.02758010569959879):
														if(x_velocity <= -0.01779560884460807):
															if(angle_velocity <= -0.03028054442256689):
																return True
													else:
														if(x_velocity <= 0.09785904735326767):
															if(lander_x > -0.13933706283569336):
																if(angle_velocity > -0.02688912022858858):
																	if(lander_x <= -0.072903823107481):
																		if(angle > 0.032312186434865):
																			return True
											else:
												if(x_velocity <= 0.06280925124883652):
													if(lander_y <= 0.3163684159517288):
														if(lander_x <= 0.025122356601059437):
															if(angle_velocity > -0.04699285887181759):
																if(y_velocity <= -0.20552700757980347):
																	if(angle <= 0.01394487265497446):
																		return True
														else:
															if(x_velocity <= -0.03566419705748558):
																return True
													else:
														if(y_velocity > -0.21319089084863663):
															if(x_velocity <= 0.05624804459512234):
																if(lander_x <= 0.10452795028686523):
																	if(lander_y <= 0.4113921821117401):
																		return True
																	else:
																		if(y_velocity > -0.20844776928424835):
																			return True
																else:
																	if(x_velocity <= -0.03246714733541012):
																		return True
										else:
											if(y_velocity <= -0.19896094501018524):
												if(angle <= 0.06532834470272064):
													if(angle_velocity <= -0.03555918484926224):
														if(x_velocity <= 0.09161169081926346):
															if(lander_x <= -0.08843240514397621):
																if(x_velocity <= 0.04285657778382301):
																	return True
															else:
																if(x_velocity <= 0.02752626407891512):
																	if(lander_x <= -0.00529823312535882):
																		return True
													else:
														if(lander_y <= 0.4755209684371948):
															if(x_velocity <= 0.15868263691663742):
																if(y_velocity <= -0.20105457305908203):
																	if(x_velocity <= 0.10151506215333939):
																		if(y_velocity > -0.20671191811561584):
																			if(y_velocity <= -0.20404434949159622):
																				return True
														else:
															return True
						else:
							if(x_velocity <= 0.0011435417691245675):
								if(lander_x <= 0.015800190158188343):
									if(angle > -0.055125484243035316):
										if(angle_velocity <= -0.07059032469987869):
											if(angle > 0.01665340829640627):
												return True
										else:
											if(angle_velocity <= -0.02607179619371891):
												if(angle_velocity <= -0.02760558482259512):
													if(angle <= -0.009582070168107748):
														if(angle <= -0.01621855143457651):
															return True
														else:
															if(angle > -0.014363113790750504):
																if(y_velocity > -0.19560135900974274):
																	return True
													else:
														return True
												else:
													if(angle <= -0.035965751856565475):
														return True
											else:
												return True
								else:
									if(angle_velocity <= -0.04469680041074753):
										if(lander_y <= 0.10058356449007988):
											if(lander_y > 0.0019821441455860622):
												if(y_velocity > -0.16840074956417084):
													return True
										else:
											if(lander_x > 0.016848516650497913):
												return True
									else:
										if(x_velocity <= -0.023783325217664242):
											if(angle <= -0.010971731040626764):
												if(x_velocity <= -0.04097524285316467):
													return True
											else:
												if(angle <= 0.03952940180897713):
													if(lander_y <= 0.3908946365118027):
														return True
													else:
														if(angle_velocity > -0.035638272762298584):
															return True
												else:
													if(x_velocity > -0.028548584319651127):
														return True
										else:
											if(angle <= 0.025992137379944324):
												if(angle_velocity <= -0.013786638621240854):
													if(y_velocity > -0.19353199750185013):
														if(angle_velocity > -0.022440374828875065):
															if(angle_velocity <= -0.019915688782930374):
																return True
												else:
													return True
											else:
												if(lander_y <= 0.4093811511993408):
													if(y_velocity <= -0.18997720628976822):
														if(x_velocity <= -0.008326976094394922):
															return True
													else:
														return True
							else:
								if(y_velocity <= -0.15708663314580917):
									if(angle <= 0.055927980691194534):
										if(angle_velocity <= -0.029996730387210846):
											if(lander_y <= 0.22265808284282684):
												if(x_velocity <= 0.05057523027062416):
													if(lander_x <= 0.003647613455541432):
														if(angle <= 0.03232170734554529):
															if(x_velocity <= 0.01392990630120039):
																if(x_velocity > 0.007273729424923658):
																	return True
															else:
																if(x_velocity > 0.04961695522069931):
																	return True
														else:
															if(angle <= 0.037334516644477844):
																return True
												else:
													if(lander_x <= -0.1860310062766075):
														if(lander_x > -0.18918657302856445):
															return True
											else:
												if(y_velocity <= -0.18175316601991653):
													if(x_velocity <= 0.058019060641527176):
														if(lander_x <= -0.13314781337976456):
															if(angle_velocity > -0.06879015266895294):
																if(y_velocity <= -0.18628955632448196):
																	return True
													else:
														if(lander_x > -0.12465257942676544):
															if(lander_y > 0.29560112208127975):
																return True
												else:
													return True
										else:
											if(angle <= 0.0255026426166296):
												if(lander_x <= -0.04367666319012642):
													if(x_velocity <= 0.01822946034371853):
														if(angle <= -0.004283868474885821):
															if(x_velocity > 0.015560395084321499):
																return True
														else:
															return True
													else:
														if(angle_velocity <= -0.028262783773243427):
															return True
														else:
															if(angle_velocity <= -0.01770548801869154):
																if(y_velocity <= -0.1745178923010826):
																	if(lander_x <= -0.22383809089660645):
																		if(lander_x > -0.2353208288550377):
																			return True
																else:
																	if(angle > 0.010273960826452821):
																		return True
															else:
																if(lander_x <= -0.09532566368579865):
																	if(x_velocity <= 0.0507375281304121):
																		if(x_velocity > 0.025258666835725307):
																			return True
																	else:
																		if(y_velocity > -0.17010528594255447):
																			return True
											else:
												if(y_velocity <= -0.18513454496860504):
													if(lander_y <= 0.22858544439077377):
														if(x_velocity <= 0.09050897136330605):
															if(lander_x <= 0.14186649024486542):
																if(x_velocity <= 0.03864736296236515):
																	if(x_velocity <= 0.03466221131384373):
																		if(angle > 0.04619345813989639):
																			return True
																	else:
																		return True
													else:
														if(lander_x <= -0.1384853795170784):
															return True
														else:
															if(angle <= 0.048908576369285583):
																if(lander_y <= 0.28573012351989746):
																	if(angle <= 0.04231484979391098):
																		return True
															else:
																return True
												else:
													if(x_velocity <= 0.0833539068698883):
														if(angle_velocity <= -0.013280750252306461):
															if(x_velocity <= 0.029910244047641754):
																if(x_velocity <= 0.018781989812850952):
																	return True
																else:
																	if(angle_velocity > -0.01790214516222477):
																		return True
															else:
																if(lander_x <= -0.06425094604492188):
																	if(angle_velocity <= -0.014119629748165607):
																		if(lander_y <= 0.08994792401790619):
																			if(angle <= 0.037441227585077286):
																				return True
																		else:
																			if(angle <= 0.03540452942252159):
																				if(angle_velocity <= -0.022842702455818653):
																					return True
																			else:
																				return True
														else:
															return True
													else:
														if(lander_x <= -0.23215117305517197):
															if(x_velocity <= 0.12539780884981155):
																return True
									else:
										if(y_velocity <= -0.18687207251787186):
											if(lander_y <= 0.3379046618938446):
												if(lander_x > -0.13328032940626144):
													if(x_velocity <= 0.10170841962099075):
														if(lander_y > 0.2902415916323662):
															return True
											else:
												if(angle_velocity <= -0.016473854891955853):
													if(angle_velocity <= -0.05001203343272209):
														if(lander_y <= 0.4006785899400711):
															if(angle_velocity > -0.07887016981840134):
																return True
										else:
											if(lander_y > 0.1910877674818039):
												if(x_velocity <= 0.11261632665991783):
													if(lander_y <= 0.255778931081295):
														if(x_velocity <= 0.08044421672821045):
															if(angle <= 0.06523803994059563):
																return True
													else:
														if(lander_x <= -0.06852855533361435):
															return True
														else:
															if(x_velocity <= 0.048225332982838154):
																return True
												else:
													if(x_velocity <= 0.17195049673318863):
														if(lander_y > 0.4196188747882843):
															if(angle_velocity > -0.08727699518203735):
																if(x_velocity <= 0.14947761595249176):
																	if(lander_x <= -0.13791736960411072):
																		return True
																else:
																	if(x_velocity > 0.169244222342968):
																		return True
								else:
									if(lander_y > 0.02113238349556923):
										if(angle_velocity <= -0.011243961751461029):
											if(lander_x <= -0.051788236014544964):
												return True
											else:
												if(lander_y <= 0.09482178464531898):
													return True
					else:
						if(x_velocity <= 0.1182720772922039):
							if(lander_y <= 1.4159489870071411):
								if(x_velocity <= -0.2558598518371582):
									if(angle <= -0.0816878229379654):
										if(lander_y > 1.3962932229042053):
											return True
									else:
										return True
								else:
									if(angle <= 0.015097778290510178):
										if(x_velocity <= -0.034011710435152054):
											if(angle_velocity <= -0.05374739691615105):
												if(angle <= -0.009260292630642653):
													if(lander_y <= 1.4135539531707764):
														if(y_velocity > -0.148211307823658):
															if(x_velocity > -0.17158370465040207):
																return True
													else:
														return True
												else:
													return True
											else:
												if(lander_x <= 0.10194678045809269):
													if(angle_velocity <= -0.03231293894350529):
														if(angle > -0.013385280966758728):
															return True
													else:
														return True
										else:
											if(lander_y <= 0.5317800343036652):
												if(lander_x <= -0.009291745722293854):
													return True
									else:
										if(angle_velocity <= -0.03397380746901035):
											if(lander_y <= 0.6864185929298401):
												if(y_velocity <= -0.22251423448324203):
													return True
												else:
													if(x_velocity <= 0.030961166135966778):
														if(x_velocity > -0.016317512840032578):
															if(angle > 0.01918367575854063):
																return True
											else:
												if(x_velocity <= 0.058617839589715004):
													if(angle_velocity > -0.37056033313274384):
														if(x_velocity <= 0.012419880833476782):
															return True
														else:
															if(angle_velocity > -0.2228338047862053):
																if(lander_y <= 0.9218689501285553):
																	if(angle > 0.12585018947720528):
																		if(x_velocity <= 0.046162309125065804):
																			return True
																else:
																	if(y_velocity <= -0.222663052380085):
																		if(y_velocity <= -0.22370660305023193):
																			return True
																	else:
																		return True
												else:
													if(y_velocity <= -0.2002694457769394):
														if(angle_velocity > -0.1456744521856308):
															if(lander_x <= 0.11833129078149796):
																if(angle <= 0.15269678831100464):
																	if(angle_velocity <= -0.04049842804670334):
																		if(x_velocity <= 0.06560581922531128):
																			if(lander_y > 1.0275564193725586):
																				return True
																else:
																	if(angle_velocity > -0.09067074954509735):
																		if(angle_velocity <= -0.05935409851372242):
																			return True
															else:
																return True
													else:
														if(lander_y > 0.9670573770999908):
															return True
										else:
											if(lander_y <= 0.5836990177631378):
												if(x_velocity <= 0.057437339797616005):
													return True
												else:
													if(y_velocity > -0.20619171857833862):
														return True
											else:
												if(x_velocity <= 0.010020026937127113):
													if(x_velocity <= 0.007299841847270727):
														return True
												else:
													return True
							else:
								if(y_velocity <= -0.20843198895454407):
									if(y_velocity > -0.22065477073192596):
										if(x_velocity > -0.37183597683906555):
											return True
								else:
									if(angle <= -0.04813877120614052):
										if(y_velocity <= -0.16151153296232224):
											if(lander_y <= 1.508604645729065):
												if(lander_x > -0.04733452759683132):
													if(y_velocity > -0.17122621089220047):
														return True
									else:
										if(angle_velocity > -0.06140822544693947):
											return True
						else:
							if(lander_x > 0.08426184579730034):
								if(y_velocity <= -0.17774006724357605):
									if(y_velocity <= -0.2086435928940773):
										if(x_velocity <= 0.1553923711180687):
											if(lander_y > 1.1958619356155396):
												if(y_velocity > -0.22044707089662552):
													return True
									else:
										if(x_velocity <= 0.27152805030345917):
											if(angle_velocity <= -0.05723921023309231):
												if(lander_x > 0.15445046871900558):
													if(angle_velocity <= -0.16303861886262894):
														if(angle > 0.34828269481658936):
															if(angle_velocity > -0.20622273534536362):
																return True
													else:
														if(x_velocity <= 0.23525077104568481):
															if(lander_x <= 0.22326912730932236):
																if(angle_velocity > -0.14127739518880844):
																	if(angle_velocity <= -0.0871920995414257):
																		if(lander_y <= 1.3360260725021362):
																			return True
															else:
																return True
											else:
												if(lander_x > 0.10068545490503311):
													return True
										else:
											if(angle > 0.4899993985891342):
												if(lander_x > 0.25046396255493164):
													return True
								else:
									if(x_velocity <= 0.29067718982696533):
										return True
			else:
				if(y_velocity <= -0.19208889454603195):
					if(lander_y <= 0.2897540479898453):
						if(angle <= -0.001974301296286285):
							if(x_velocity <= -0.01461441582068801):
								if(lander_y <= 0.00980702368542552):
									if(angle_velocity > -0.005119665991514921):
										if(right_leg_contact != True):
											if(lander_y > 0.004544887458905578):
												if(lander_y <= 0.006062713917344809):
													if(angle > -0.030654183588922024):
														return True
								else:
									if(y_velocity <= -0.21065139770507812):
										if(lander_y <= 0.16549677401781082):
											if(angle <= -0.03493528999388218):
												if(x_velocity <= -0.03977541998028755):
													if(angle_velocity <= -0.0024486881447955966):
														if(angle_velocity <= -0.005835844436660409):
															if(angle_velocity <= -0.006929071620106697):
																if(lander_y <= 0.1217980831861496):
																	return True
													else:
														if(lander_x <= 0.0528874397277832):
															if(lander_y <= 0.05295024998486042):
																if(y_velocity <= -0.2188088223338127):
																	if(y_velocity <= -0.22296956926584244):
																		return True
																else:
																	return True
															else:
																if(lander_y <= 0.12028517574071884):
																	return True
																else:
																	if(lander_y > 0.1318969614803791):
																		return True
												else:
													if(lander_x <= -0.11710600554943085):
														if(angle_velocity > -0.004093042458407581):
															if(y_velocity <= -0.22099005430936813):
																if(lander_y <= 0.06058395840227604):
																	return True
															else:
																return True
													else:
														if(angle > -0.0471199844032526):
															if(lander_y <= 0.1439994052052498):
																if(lander_x > 0.047720860689878464):
																	return True
											else:
												if(lander_y > 0.07413315400481224):
													if(y_velocity <= -0.21574554592370987):
														if(lander_x <= -0.0669793114066124):
															return True
														else:
															if(angle_velocity <= -0.005755024263635278):
																if(angle > -0.024487187154591084):
																	return True
													else:
														if(angle > -0.02462300844490528):
															if(y_velocity <= -0.21370692551136017):
																return True
															else:
																if(lander_x <= 0.02692174818366766):
																	return True
										else:
											if(angle <= -0.024513673037290573):
												if(lander_x <= 0.11286602169275284):
													if(y_velocity <= -0.22343513369560242):
														if(lander_x > -0.02529301680624485):
															return True
													else:
														return True
												else:
													if(lander_y > 0.22845791280269623):
														return True
											else:
												if(y_velocity > -0.22127367556095123):
													if(angle_velocity <= 0.03473819978535175):
														if(lander_y <= 0.24431777745485306):
															return True
														else:
															if(x_velocity <= -0.03543645143508911):
																return True
															else:
																if(lander_x <= -0.0016593458130955696):
																	return True
													else:
														if(angle > -0.015831599477678537):
															if(angle <= -0.00635238247923553):
																return True
									else:
										if(x_velocity <= -0.025622901506721973):
											if(angle <= -0.047295982018113136):
												if(lander_x <= 0.0035557270057324786):
													if(x_velocity <= -0.03496578708291054):
														if(angle <= -0.060785090550780296):
															if(angle <= -0.06955886632204056):
																return True
														else:
															return True
											else:
												if(lander_y > 0.014223549049347639):
													if(angle <= -0.0398060604929924):
														if(angle <= -0.04114944115281105):
															return True
													else:
														return True
										else:
											if(angle_velocity <= 0.00881808646954596):
												if(lander_x <= -0.121637724339962):
													return True
												else:
													if(angle_velocity > -0.008143778424710035):
														if(y_velocity <= -0.20849178731441498):
															return True
											else:
												if(lander_x <= 0.09575405344367027):
													if(angle <= -0.04643068462610245):
														if(lander_y <= 0.06374220550060272):
															return True
													else:
														return True
							else:
								if(lander_y <= 0.17636018991470337):
									if(y_velocity <= -0.20780175924301147):
										if(angle <= -0.029647454619407654):
											if(x_velocity <= 0.004933268181048334):
												if(angle <= -0.03637485392391682):
													if(angle <= -0.04454756900668144):
														return True
												else:
													if(angle_velocity > -0.006891900207847357):
														if(lander_x <= -0.07776127010583878):
															return True
											else:
												if(lander_x <= -0.244578555226326):
													return True
										else:
											if(angle_velocity > -0.0058912960812449455):
												if(angle <= -0.002356428885832429):
													if(y_velocity <= -0.2082531675696373):
														if(angle_velocity <= 0.017753158695995808):
															if(angle_velocity > 0.014326295349746943):
																if(lander_x <= -0.10722851753234863):
																	if(lander_y > 0.08121594041585922):
																		return True
													else:
														if(y_velocity <= -0.20811493694782257):
															return True
									else:
										if(angle_velocity <= 0.014084470458328724):
											if(angle <= -0.018581273965537548):
												if(y_velocity <= -0.20756550878286362):
													return True
												else:
													if(angle_velocity <= -0.010733573231846094):
														return True
													else:
														if(y_velocity > -0.20055539906024933):
															if(angle > -0.023613708093762398):
																return True
											else:
												if(x_velocity <= 0.04151764698326588):
													if(lander_x <= -0.08645911142230034):
														if(angle <= -0.006798464106395841):
															return True
										else:
											if(lander_y <= 0.08455385640263557):
												if(angle_velocity <= 0.01682453602552414):
													return True
												else:
													if(lander_y > 0.022858796641230583):
														if(angle <= -0.03435870446264744):
															if(angle > -0.04383568838238716):
																return True
														else:
															if(x_velocity <= -0.005795223638415337):
																return True
															else:
																if(y_velocity <= -0.1949629932641983):
																	if(y_velocity > -0.20029407739639282):
																		if(lander_x <= -0.13982105255126953):
																			if(lander_x > -0.18819518387317657):
																				return True
											else:
												if(x_velocity <= 0.06846123188734055):
													if(lander_x <= 0.10798463970422745):
														if(x_velocity <= 0.01650381088256836):
															return True
														else:
															if(angle_velocity > 0.0359306912869215):
																if(lander_y <= 0.1353665217757225):
																	return True
								else:
									if(y_velocity <= -0.21350980550050735):
										if(lander_y <= 0.22156928479671478):
											if(x_velocity <= 0.0022984480601735413):
												if(lander_y > 0.18454410880804062):
													return True
										else:
											if(angle_velocity <= 0.00941420067101717):
												if(angle > -0.00994016882032156):
													if(y_velocity > -0.21747388690710068):
														if(x_velocity > 0.0126884994097054):
															return True
											else:
												if(x_velocity <= 0.04361279867589474):
													if(lander_x <= 0.01591725368052721):
														if(y_velocity <= -0.2211196944117546):
															if(angle_velocity <= 0.015095389913767576):
																return True
														else:
															return True
													else:
														if(y_velocity > -0.21712232381105423):
															return True
									else:
										if(angle_velocity <= 0.010462206788361073):
											if(lander_y <= 0.25021277368068695):
												if(y_velocity <= -0.21185879409313202):
													return True
												else:
													if(lander_y <= 0.18268869817256927):
														if(lander_x > -0.23379047214984894):
															return True
													else:
														if(lander_x <= -0.17782209068536758):
															if(x_velocity <= 0.023040185420541093):
																return True
											else:
												return True
										else:
											if(x_velocity <= 0.05154911056160927):
												if(lander_x <= -0.02145376242697239):
													return True
												else:
													if(angle > -0.018772676587104797):
														if(angle_velocity > 0.02569399494677782):
															return True
											else:
												if(x_velocity > 0.056840525940060616):
													if(angle <= -0.013219031039625406):
														if(lander_x <= -0.22745025157928467):
															return True
													else:
														return True
						else:
							if(right_leg_contact != True):
								if(y_velocity <= -0.20635643601417542):
									if(x_velocity <= -0.027317581698298454):
										if(y_velocity <= -0.20972612500190735):
											if(y_velocity <= -0.22286126762628555):
												return True
											else:
												if(angle_velocity > 0.020856578834354877):
													if(angle_velocity <= 0.025851380079984665):
														return True
										else:
											return True
									else:
										if(angle <= 0.10114578157663345):
											if(lander_x <= -0.2811438590288162):
												return True
											else:
												if(angle <= 0.018739018589258194):
													if(angle_velocity <= -0.005446673603728414):
														if(lander_x <= 0.04728131368756294):
															if(angle_velocity > -0.006448284490033984):
																return True
													else:
														if(angle <= 0.018694463185966015):
															if(lander_y <= 0.2418917417526245):
																if(lander_x <= 0.15335922688245773):
																	if(lander_x <= -0.2490876391530037):
																		if(lander_x > -0.2502325177192688):
																			return True
															else:
																if(y_velocity <= -0.21332582831382751):
																	if(angle_velocity <= 0.0018679435597732663):
																		return True
																else:
																	if(lander_y <= 0.2714949995279312):
																		return True
												else:
													if(y_velocity > -0.207355335354805):
														if(x_velocity <= 0.12062624469399452):
															if(angle_velocity > 0.03943806141614914):
																return True
										else:
											return True
								else:
									if(angle <= 0.027642766945064068):
										if(lander_y <= 0.11291278526186943):
											if(x_velocity <= -0.009744551964104176):
												if(angle <= 0.010740743018686771):
													return True
												else:
													if(lander_y > 0.07252175360918045):
														return True
											else:
												if(lander_x <= 0.038906002417206764):
													if(angle <= 0.026989192701876163):
														if(x_velocity <= -0.0020548300817608833):
															if(angle_velocity > 0.0316975973546505):
																return True
														else:
															if(angle_velocity > -0.004507679492235184):
																if(angle <= 0.0025926113594323397):
																	if(angle > 0.0023132554488256574):
																		return True
													else:
														if(lander_x <= -0.04813614021986723):
															return True
												else:
													if(angle_velocity > 0.0020055713539477438):
														if(lander_x <= 0.07076811790466309):
															if(y_velocity <= -0.1983875408768654):
																return True
										else:
											if(angle <= 0.011901159305125475):
												if(angle_velocity <= 0.020643576979637146):
													if(angle <= 0.00960160605609417):
														if(y_velocity <= -0.1995120793581009):
															if(lander_y > 0.17736715823411942):
																if(y_velocity > -0.20391415804624557):
																	if(lander_x > -0.11024045944213867):
																		return True
													else:
														return True
												else:
													if(lander_y <= 0.27392782270908356):
														if(angle <= 0.0006887250929139555):
															if(angle_velocity > 0.04476818349212408):
																return True
														else:
															if(lander_x <= 0.10790705680847168):
																if(angle_velocity <= 0.09454983100295067):
																	return True
											else:
												if(x_velocity <= -0.0062241205014288425):
													return True
												else:
													if(y_velocity <= -0.19909492135047913):
														if(angle_velocity <= 0.08634553849697113):
															if(angle_velocity <= 0.01964742224663496):
																if(lander_x > -0.14925479888916016):
																	if(x_velocity <= 0.04161417856812477):
																		if(angle_velocity > 0.018095350824296474):
																			return True
														else:
															return True
													else:
														if(lander_x <= 0.07373743131756783):
															if(lander_x <= -0.14914417266845703):
																return True
															else:
																if(x_velocity <= 0.05354272201657295):
																	if(y_velocity <= -0.1963896080851555):
																		if(angle > 0.02702635433524847):
																			return True
																	else:
																		return True
									else:
										if(angle_velocity <= 0.27043651044368744):
											if(lander_y <= 0.25494179129600525):
												if(angle_velocity <= -0.005314721260219812):
													if(angle_velocity <= -0.005757053149864078):
														if(lander_y <= 0.21493321657180786):
															if(angle <= 0.03667156584560871):
																if(lander_y > 0.15531865507364273):
																	return True
													else:
														return True
												else:
													if(angle > 0.027910239063203335):
														if(angle_velocity <= 0.07716051861643791):
															if(y_velocity > -0.1948823481798172):
																if(y_velocity <= -0.19475548714399338):
																	return True
																else:
																	if(lander_y > 0.23298634588718414):
																		if(lander_x <= -0.12926983833312988):
																			return True
														else:
															if(angle_velocity <= 0.077748142182827):
																return True
											else:
												if(x_velocity <= 0.07137685641646385):
													if(lander_y <= 0.2812550216913223):
														if(angle > 0.028213849291205406):
															if(lander_x <= 0.07850079517811537):
																return True
															else:
																if(x_velocity <= 0.0152086834423244):
																	return True
										else:
											return True
							else:
								if(lander_x <= -0.12573399394750595):
									return True
					else:
						if(angle <= 0.034049760550260544):
							if(x_velocity <= 0.05305109918117523):
								if(y_velocity <= -0.21372266113758087):
									if(lander_y <= 0.3575222045183182):
										if(x_velocity <= -0.010724043473601341):
											if(lander_y <= 0.3515322655439377):
												if(angle_velocity <= -0.006636293372139335):
													if(angle <= -0.015577009879052639):
														return True
												else:
													if(angle <= -0.03804014250636101):
														if(angle <= -0.042344069108366966):
															return True
														else:
															if(lander_y > 0.32745474576950073):
																return True
													else:
														return True
										else:
											if(angle <= -0.004033001489005983):
												if(y_velocity > -0.22201097756624222):
													if(angle > -0.020024338737130165):
														if(angle <= -0.009953859262168407):
															return True
														else:
															if(lander_x <= -0.12826881557703018):
																return True
											else:
												if(angle_velocity > -0.004115351592190564):
													if(lander_y > 0.34391212463378906):
														if(lander_y > 0.34799720346927643):
															if(lander_x > -0.08978910371661186):
																return True
									else:
										if(x_velocity <= -0.03364337235689163):
											return True
										else:
											if(angle_velocity <= -0.0014139081467874348):
												if(angle > -0.003988478682003915):
													if(lander_x <= -0.03471369808539748):
														return True
													else:
														if(angle_velocity <= -0.007659282069653273):
															return True
											else:
												if(lander_y <= 0.5525970458984375):
													if(lander_x <= -0.10589723661541939):
														return True
													else:
														if(y_velocity <= -0.2196420505642891):
															if(angle_velocity > 0.020431251265108585):
																if(y_velocity <= -0.22150888293981552):
																	if(angle_velocity <= 0.033169619739055634):
																		if(angle <= -0.006665428867563605):
																			if(angle_velocity > 0.026700724847614765):
																				return True
																	else:
																		return True
														else:
															if(lander_y <= 0.5222991704940796):
																if(x_velocity <= 0.03970935940742493):
																	if(angle_velocity <= 0.023540607653558254):
																		if(angle <= -2.1919142454862595e-05):
																			if(lander_x <= -0.06499791145324707):
																				return True
																		else:
																			if(angle_velocity <= 0.021091575734317303):
																				return True
																	else:
																		return True
																else:
																	if(angle > 0.011842965614050627):
																		return True
															else:
																if(y_velocity <= -0.21910078078508377):
																	return True
												else:
													if(angle <= 0.023786209523677826):
														return True
													else:
														if(angle > 0.024443095549941063):
															if(lander_x <= 0.0425267219543457):
																return True
															else:
																if(x_velocity <= 0.028033524751663208):
																	return True
								else:
									if(lander_x <= -0.0046904562041163445):
										if(angle_velocity > -0.010266120545566082):
											if(angle <= 0.025997248478233814):
												if(angle <= -0.03068194631487131):
													if(angle <= -0.0321212038397789):
														return True
												else:
													if(x_velocity <= 0.04653698578476906):
														return True
													else:
														if(x_velocity > 0.04709045775234699):
															return True
											else:
												if(x_velocity > 0.04489062912762165):
													return True
									else:
										if(x_velocity <= -0.02208183240145445):
											if(lander_x <= 0.033309316262602806):
												if(lander_x <= 0.030749320052564144):
													return True
											else:
												return True
										else:
											if(angle_velocity <= 0.0024770539021119475):
												if(lander_y > 0.4256361424922943):
													return True
											else:
												if(x_velocity <= 0.03922008164227009):
													if(x_velocity > -0.02160018589347601):
														if(lander_x > -0.004368925001472235):
															if(y_velocity <= -0.2135368511080742):
																if(angle_velocity <= 0.02621288038790226):
																	return True
															else:
																if(angle <= -0.025066950358450413):
																	if(angle <= -0.02567780762910843):
																		return True
																else:
																	if(lander_x <= 0.13135547190904617):
																		if(x_velocity <= 0.023885557428002357):
																			if(angle_velocity <= 0.01477389084175229):
																				if(angle_velocity <= 0.012111582327634096):
																					return True
																			else:
																				return True
																		else:
																			if(lander_x > -0.0019715309608727694):
																				return True
																	else:
																		if(lander_x > 0.13403763622045517):
																			return True
												else:
													if(angle_velocity > 0.023443574085831642):
														if(x_velocity > 0.044566577300429344):
															return True
							else:
								if(lander_y <= 0.4885428249835968):
									if(y_velocity <= -0.20921574532985687):
										if(angle <= 0.011685142293572426):
											if(angle_velocity <= 0.015439566690474749):
												if(angle > 0.010880847461521626):
													return True
											else:
												if(y_velocity > -0.2136419340968132):
													if(angle_velocity <= 0.10941843688488007):
														return True
										else:
											if(angle_velocity > -0.0015045297041069716):
												if(lander_x <= -0.326427698135376):
													return True
												else:
													if(x_velocity <= 0.06233610399067402):
														if(lander_x <= -0.14032430946826935):
															if(angle <= 0.02828526869416237):
																return True
													else:
														if(x_velocity <= 0.10567198321223259):
															if(lander_x <= -0.20010306686162949):
																if(angle <= 0.017873233184218407):
																	return True
									else:
										if(lander_x <= -0.09546852111816406):
											if(angle_velocity <= 0.005387932527810335):
												if(lander_x <= -0.2620481252670288):
													return True
											else:
												if(x_velocity <= 0.07738113403320312):
													if(lander_x <= -0.18783941119909286):
														if(angle_velocity > 0.013788129203021526):
															return True
													else:
														return True
												else:
													if(lander_y > 0.3158178925514221):
														if(y_velocity <= -0.19682814180850983):
															if(angle <= 0.02384153939783573):
																if(lander_x <= -0.33112064003944397):
																	return True
																else:
																	if(angle_velocity > 0.05205644108355045):
																		return True
															else:
																if(y_velocity > -0.20641037821769714):
																	return True
														else:
															return True
								else:
									if(lander_y <= 1.3911697268486023):
										if(angle_velocity <= 0.02309056557714939):
											if(y_velocity <= -0.218096524477005):
												if(angle > 0.02420397661626339):
													if(y_velocity <= -0.21971922367811203):
														if(angle <= 0.030224091373384):
															return True
											else:
												if(x_velocity <= 0.09193065017461777):
													if(lander_x <= -0.15274892002344131):
														return True
													else:
														if(angle_velocity > 0.009516449877992272):
															return True
												else:
													if(lander_x <= -0.23825695365667343):
														return True
										else:
											if(x_velocity <= 0.14600562304258347):
												if(angle_velocity <= 0.04647490940988064):
													if(angle_velocity <= 0.043493252247571945):
														if(y_velocity <= -0.21315408498048782):
															if(lander_x <= -0.14153748005628586):
																if(lander_y <= 0.5870274603366852):
																	if(y_velocity > -0.21557246148586273):
																		return True
																else:
																	return True
														else:
															return True
												else:
													if(lander_y <= 0.5280139744281769):
														if(x_velocity <= 0.07425070367753506):
															return True
													else:
														if(y_velocity <= -0.22308366000652313):
															if(angle <= 0.01521918410435319):
																return True
														else:
															if(x_velocity <= 0.12485217303037643):
																return True
															else:
																if(x_velocity > 0.12699494510889053):
																	return True
											else:
												if(angle_velocity <= 0.14660384505987167):
													if(angle_velocity > 0.06831873580813408):
														if(y_velocity <= -0.2058495506644249):
															if(lander_y > 0.6285300850868225):
																return True
														else:
															if(lander_y <= 0.5763521194458008):
																return True
												else:
													if(lander_y > 0.5652773082256317):
														return True
						else:
							if(lander_y <= 0.5863185822963715):
								if(y_velocity <= -0.20273584127426147):
									if(angle <= 0.1946142390370369):
										if(lander_y <= 0.44142310321331024):
											if(y_velocity > -0.20535477250814438):
												if(y_velocity <= -0.2051713764667511):
													return True
												else:
													if(x_velocity <= 0.07270235940814018):
														if(angle <= 0.04248816519975662):
															return True
										else:
											if(x_velocity <= 0.1046687550842762):
												if(y_velocity <= -0.21798130124807358):
													if(angle_velocity <= 0.02302786521613598):
														if(y_velocity > -0.22318175435066223):
															if(lander_x <= -0.1531415954232216):
																return True
												else:
													if(y_velocity <= -0.20877746492624283):
														if(angle > 0.034671757370233536):
															return True
													else:
														if(angle_velocity <= 0.029814787209033966):
															if(y_velocity <= -0.20628339052200317):
																if(angle_velocity > 0.019804266281425953):
																	return True
															else:
																return True
														else:
															if(x_velocity > 0.10193632915616035):
																return True
											else:
												if(angle_velocity > 0.005676704226061702):
													if(lander_y > 0.4477561116218567):
														if(y_velocity <= -0.20807651430368423):
															if(x_velocity <= 0.113375473767519):
																if(x_velocity > 0.11150490120053291):
																	return True
														else:
															if(y_velocity > -0.2072468250989914):
																if(angle_velocity > 0.13744492456316948):
																	return True
									else:
										if(y_velocity > -0.22159618139266968):
											return True
								else:
									if(x_velocity <= 0.09705938026309013):
										if(lander_y <= 0.42095011472702026):
											if(lander_x <= -0.1157781109213829):
												return True
											else:
												if(x_velocity <= 0.07562413811683655):
													if(lander_y <= 0.41697004437446594):
														return True
										else:
											return True
									else:
										if(angle <= 0.11374308541417122):
											if(lander_y <= 0.508734256029129):
												if(angle <= 0.04096033237874508):
													return True
												else:
													if(lander_x <= -0.28699319064617157):
														return True
											else:
												if(x_velocity <= 0.17307308316230774):
													if(angle > 0.048182547092437744):
														if(lander_x <= -0.1486435905098915):
															return True
										else:
											return True
							else:
								if(x_velocity <= 0.2813781797885895):
									if(x_velocity <= 0.2044903039932251):
										if(lander_x <= -0.11335830762982368):
											if(y_velocity <= -0.20570598542690277):
												if(lander_y <= 0.6806885898113251):
													if(lander_x <= -0.21587343513965607):
														if(angle_velocity > 0.010703293140977621):
															if(x_velocity <= 0.15296711772680283):
																return True
												else:
													if(y_velocity > -0.2210519015789032):
														return True
											else:
												if(angle <= 0.05711753852665424):
													return True
										else:
											if(y_velocity > -0.22416681796312332):
												if(lander_y <= 1.0864827036857605):
													if(lander_y <= 1.0452588200569153):
														if(angle_velocity <= 0.01179392309859395):
															if(y_velocity > -0.22135239094495773):
																if(angle <= 0.046070387586951256):
																	if(angle <= 0.04330882430076599):
																		return True
																else:
																	return True
														else:
															return True
													else:
														if(angle <= 0.1444753035902977):
															if(x_velocity > 0.16547763347625732):
																return True
												else:
													if(lander_y <= 1.4217828512191772):
														if(x_velocity <= 0.19004350900650024):
															return True
														else:
															if(y_velocity > -0.22363383322954178):
																if(x_velocity > 0.1932922974228859):
																	return True
													else:
														if(angle_velocity > 0.11284030228853226):
															return True
									else:
										if(angle_velocity <= 0.0879020132124424):
											if(lander_y > 1.3319485187530518):
												if(angle_velocity > 0.04395821690559387):
													if(y_velocity > -0.21488496661186218):
														if(x_velocity <= 0.2296036332845688):
															return True
										else:
											if(angle <= 0.12765425071120262):
												if(lander_y > 1.4216150641441345):
													return True
											else:
												if(lander_y <= 1.2444899678230286):
													if(angle <= 0.3052857518196106):
														if(angle <= 0.17856942117214203):
															if(angle > 0.16171462833881378):
																return True
													else:
														return True
												else:
													if(lander_y <= 1.4481617212295532):
														return True
													else:
														if(lander_x <= 0.07722954824566841):
															return True
								else:
									if(angle_velocity <= 0.31584182381629944):
										if(lander_x <= 0.2778894901275635):
											if(y_velocity <= -0.2168443650007248):
												if(angle > 0.3000917434692383):
													return True
										else:
											if(y_velocity > -0.211095929145813):
												return True
									else:
										if(angle > 0.21356071531772614):
											return True
				else:
					if(x_velocity <= 0.07045570015907288):
						if(right_leg_contact != True):
							if(left_leg_contact != True):
								if(y_velocity <= -0.18674296140670776):
									if(angle <= 0.0206502266228199):
										if(x_velocity <= 0.05978120490908623):
											if(x_velocity <= -0.0097250547260046):
												return True
											else:
												if(lander_x <= 0.02540740929543972):
													if(angle <= -0.019759160466492176):
														if(lander_x <= -0.06997428089380264):
															if(angle <= -0.02061108872294426):
																return True
													else:
														if(y_velocity <= -0.19151069968938828):
															if(y_velocity <= -0.19160612672567368):
																return True
														else:
															return True
												else:
													if(lander_y <= 0.11629515886306763):
														if(x_velocity <= 0.028145658783614635):
															return True
													else:
														if(lander_y > 0.20330068469047546):
															if(angle_velocity > 0.038037100806832314):
																return True
										else:
											if(lander_x <= -0.1872841790318489):
												return True
									else:
										if(lander_y <= 0.12287139892578125):
											if(lander_x <= -0.023945760913193226):
												if(x_velocity <= 0.039824316278100014):
													return True
										else:
											if(angle > 0.022526774555444717):
												if(lander_x <= 0.017209386453032494):
													if(angle <= 0.049267735332250595):
														return True
												else:
													if(x_velocity <= 0.024150562472641468):
														return True
													else:
														if(angle_velocity <= 0.005531748756766319):
															if(angle > 0.03523879311978817):
																return True
								else:
									if(angle_velocity <= 0.0069290283136069775):
										if(lander_x <= 0.056334782391786575):
											if(angle_velocity <= 0.006530629703775048):
												if(y_velocity <= -0.1764686405658722):
													if(lander_x <= -0.0709809772670269):
														if(lander_y <= 0.44085314869880676):
															return True
													else:
														if(x_velocity <= 0.03471241518855095):
															if(angle <= 0.037080058827996254):
																if(lander_y <= 0.028778360225260258):
																	if(angle_velocity <= 0.0017520603723824024):
																		return True
																else:
																	return True
														else:
															if(lander_y > 0.09074575453996658):
																if(x_velocity <= 0.06363154761493206):
																	if(y_velocity <= -0.17950208485126495):
																		if(angle_velocity > 0.0011211353121325374):
																			return True
																	else:
																		return True
												else:
													if(lander_y > 0.0062898253090679646):
														if(x_velocity <= 0.06309620290994644):
															if(y_velocity <= -0.17502595484256744):
																if(y_velocity <= -0.1752338483929634):
																	return True
															else:
																return True
														else:
															if(lander_x <= -0.10298142209649086):
																return True
										else:
											if(x_velocity <= 0.011500594671815634):
												if(lander_x <= 0.15299248695373535):
													return True
												else:
													if(angle > 0.030505016446113586):
														return True
											else:
												if(lander_y > 0.1928277686238289):
													return True
									else:
										if(lander_y <= 0.004686186322942376):
											if(lander_y <= 0.003906575497239828):
												if(x_velocity > 0.020605999510735273):
													return True
										else:
											if(angle <= 0.04520220868289471):
												if(lander_y <= 0.09839480742812157):
													if(lander_y <= 0.09669607505202293):
														if(angle <= -0.03468683920800686):
															if(angle <= -0.03810938447713852):
																return True
														else:
															if(angle_velocity <= 0.025887180119752884):
																if(angle_velocity <= 0.02547292783856392):
																	if(angle_velocity <= 0.023870393633842468):
																		if(lander_y <= 0.07685845717787743):
																			if(angle_velocity <= 0.019193929620087147):
																				return True
																			else:
																				if(angle_velocity > 0.020013706758618355):
																					return True
																		else:
																			if(angle_velocity <= 0.02060716412961483):
																				if(y_velocity > -0.1640598401427269):
																					return True
																			else:
																				return True
																	else:
																		if(y_velocity > -0.17367679625749588):
																			return True
															else:
																return True
												else:
													if(y_velocity <= -0.14746209233999252):
														if(lander_x <= 0.03522481769323349):
															return True
														else:
															if(lander_x > 0.035636186599731445):
																if(x_velocity <= 0.05211150087416172):
																	return True
													else:
														if(lander_x <= -0.005261325975880027):
															return True
											else:
												if(y_velocity <= -0.18225999176502228):
													if(x_velocity <= 0.01939486525952816):
														return True
												else:
													if(lander_y <= 0.08131232112646103):
														if(lander_y <= 0.07714713737368584):
															return True
													else:
														return True
							else:
								if(angle_velocity > 0.48868122696876526):
									if(y_velocity > -0.18849119544029236):
										if(x_velocity <= 0.04647136479616165):
											return True
										else:
											if(lander_y <= -0.010851457249373198):
												return True
						else:
							if(angle_velocity <= 0.40840761363506317):
								if(lander_y <= -0.02071993052959442):
									if(angle <= 0.1901896819472313):
										if(angle <= 0.18110547959804535):
											return True
									else:
										return True
								else:
									if(x_velocity <= -0.09408597834408283):
										return True
							else:
								if(y_velocity <= -0.13969463109970093):
									return True
								else:
									if(x_velocity <= -0.04035506024956703):
										return True
									else:
										if(x_velocity > -0.022401030641049147):
											return True
					else:
						if(y_velocity <= -0.17878469824790955):
							if(lander_y <= 0.3682808578014374):
								if(angle <= 0.033226991072297096):
									if(angle_velocity <= 0.032327210530638695):
										if(y_velocity > -0.1822424978017807):
											if(lander_y > 0.056553278118371964):
												return True
									else:
										if(lander_y <= 0.09766757115721703):
											if(angle <= 0.006735753966495395):
												if(angle_velocity > 0.04572450928390026):
													return True
										else:
											if(y_velocity > -0.19040030241012573):
												if(x_velocity <= 0.11845383793115616):
													return True
								else:
									if(angle_velocity <= 0.004390476504340768):
										if(angle > 0.05328214913606644):
											if(angle_velocity > -0.0003876490518450737):
												return True
									else:
										if(lander_y <= 0.2763689309358597):
											if(x_velocity <= 0.08989990502595901):
												if(x_velocity <= 0.08929217234253883):
													if(y_velocity <= -0.188216932117939):
														if(y_velocity > -0.18979504704475403):
															if(lander_x <= -0.06621541827917099):
																return True
												else:
													return True
											else:
												if(lander_x <= -0.1520765796303749):
													if(x_velocity <= 0.1060619167983532):
														return True
										else:
											if(x_velocity <= 0.11118088290095329):
												if(lander_x <= -0.07499551773071289):
													return True
											else:
												if(angle_velocity > 0.05369450896978378):
													return True
							else:
								if(x_velocity <= 0.3764907121658325):
									if(lander_y <= 1.4620787501335144):
										if(angle <= 0.07854641228914261):
											if(lander_x <= -0.012809991836547852):
												if(angle_velocity <= 0.0007023490179562941):
													if(angle_velocity <= -0.003477644408121705):
														return True
												else:
													if(x_velocity <= 0.2039438560605049):
														if(x_velocity <= 0.19526255130767822):
															if(angle <= 0.009554685559123755):
																if(x_velocity <= 0.16872210055589676):
																	return True
															else:
																return True
														else:
															if(y_velocity > -0.1825517937541008):
																return True
										else:
											if(angle <= 0.09951448440551758):
												if(angle_velocity <= 0.05455542355775833):
													if(x_velocity <= 0.12013629823923111):
														return True
													else:
														if(lander_y <= 0.5086338073015213):
															if(y_velocity > -0.1809346154332161):
																if(y_velocity <= -0.17924510687589645):
																	return True
												else:
													if(lander_x <= -0.18617639690637589):
														return True
											else:
												if(lander_x <= -0.24475514888763428):
													if(lander_y > 0.50161412358284):
														return True
												else:
													if(x_velocity <= 0.3431735634803772):
														return True
													else:
														if(lander_y > 1.3964890241622925):
															return True
								else:
									if(angle > 0.06874822499230504):
										if(angle > 0.5347166955471039):
											return True
						else:
							if(x_velocity <= 0.45725807547569275):
								if(angle_velocity <= 0.020849051885306835):
									if(angle > 0.010707416106015444):
										if(x_velocity <= 0.1138673722743988):
											if(lander_x <= -0.10730233043432236):
												if(angle_velocity <= 0.012343046255409718):
													if(angle_velocity <= -0.006565750110894442):
														if(angle_velocity <= -0.006728500593453646):
															return True
													else:
														return True
												else:
													if(angle <= 0.04613827168941498):
														if(lander_y <= 0.037872765213251114):
															return True
													else:
														return True
											else:
												if(angle <= 0.049654776230454445):
													if(angle_velocity <= 0.0133334556594491):
														if(angle_velocity <= -0.009545674081891775):
															return True
														else:
															if(y_velocity <= -0.17694725841283798):
																return True
													else:
														return True
												else:
													if(y_velocity > -0.17403686791658401):
														if(x_velocity <= 0.09220557659864426):
															return True
														else:
															if(y_velocity > -0.16615163534879684):
																if(angle_velocity > -0.0054708197712898254):
																	return True
										else:
											if(angle <= 0.09788025543093681):
												if(y_velocity <= -0.17339228838682175):
													if(angle_velocity <= 0.003842043923214078):
														if(lander_y > 0.3522111475467682):
															if(x_velocity <= 0.1355704814195633):
																return True
													else:
														if(lander_y > 0.22012582421302795):
															return True
												else:
													if(y_velocity > -0.1659632921218872):
														if(angle > 0.06073630414903164):
															if(angle <= 0.06834540143609047):
																return True
															else:
																if(y_velocity <= -0.1597970724105835):
																	if(angle > 0.0780148021876812):
																		return True
											else:
												return True
								else:
									if(lander_y <= 0.04226007126271725):
										if(left_leg_contact != True):
											if(y_velocity <= -0.16917701810598373):
												if(angle <= 0.019545963034033775):
													return True
												else:
													if(lander_y <= 0.003287003026343882):
														if(lander_y <= -0.013078692252747715):
															return True
											else:
												if(x_velocity <= 0.15987766534090042):
													if(lander_x > -0.2338159829378128):
														if(right_leg_contact != True):
															return True
														else:
															if(lander_x <= -0.19359001517295837):
																return True
									else:
										if(y_velocity <= -0.13968756049871445):
											if(x_velocity <= 0.40679629147052765):
												if(y_velocity <= -0.17383474111557007):
													if(lander_y <= 0.3370380997657776):
														if(angle <= 0.07535969465970993):
															if(y_velocity <= -0.1740221008658409):
																if(x_velocity <= 0.13857810199260712):
																	if(angle_velocity <= 0.03281082585453987):
																		if(lander_y > 0.15390201658010483):
																			return True
																	else:
																		return True
													else:
														if(lander_y <= 1.4222396612167358):
															return True
												else:
													if(angle <= -0.004808521131053567):
														if(angle <= -0.007374115288257599):
															return True
													else:
														if(angle_velocity <= 0.15649355202913284):
															if(angle_velocity <= 0.02203170582652092):
																if(angle_velocity <= 0.021947107277810574):
																	return True
															else:
																if(lander_y <= 0.1910090520977974):
																	if(lander_y <= 0.18781189620494843):
																		if(lander_x <= 0.009559154510498047):
																			if(angle <= 0.029744844883680344):
																				if(lander_y <= 0.13008564338088036):
																					return True
																			else:
																				return True
																		else:
																			if(lander_x > 0.012866020202636719):
																				return True
																else:
																	return True
														else:
															if(y_velocity > -0.16667479276657104):
																if(angle_velocity <= 0.16878244280815125):
																	if(angle_velocity <= 0.16628387570381165):
																		return True
																else:
																	return True
											else:
												if(y_velocity <= -0.1588578298687935):
													if(angle_velocity > 0.2123352363705635):
														if(x_velocity > 0.4303390234708786):
															return True
												else:
													return True
										else:
											if(angle > 0.09093538671731949):
												return True
							else:
								if(x_velocity <= 0.5235196650028229):
									if(angle_velocity <= 0.2699975222349167):
										if(angle > 0.1340556386858225):
											if(y_velocity > -0.14206217974424362):
												return True
									else:
										return True
								else:
									if(y_velocity > -0.13655703514814377):
										if(angle > 0.3606109768152237):
											return True
	else:
		if(angle <= 0.18057335913181305):
			if(lander_y <= 0.04876668006181717):
				if(angle_velocity <= 0.459291011095047):
					if(x_velocity <= -0.138141967356205):
						if(lander_x <= -0.16982293128967285):
							if(angle <= 0.1695684865117073):
								if(x_velocity <= -0.1505345180630684):
									if(lander_y <= -0.021395273506641388):
										return True
									else:
										if(y_velocity <= -0.025826004333794117):
											return True
										else:
											if(lander_y > -0.020888819359242916):
												if(angle > 0.14696944504976273):
													return True
							else:
								return True
						else:
							if(y_velocity <= -0.07581898756325245):
								return True
							else:
								if(x_velocity <= -0.1820785105228424):
									if(lander_x > -0.16601614654064178):
										return True
					else:
						if(angle_velocity > -0.6161576211452484):
							if(angle_velocity <= 0.38545961678028107):
								if(angle > -0.3233342170715332):
									if(x_velocity <= -0.10150237381458282):
										if(angle_velocity <= 0.19341470301151276):
											if(x_velocity > -0.10205988958477974):
												return True
										else:
											if(lander_y <= -0.013565602246671915):
												return True
									else:
										if(angle_velocity <= 0.31549812853336334):
											if(right_leg_contact != True):
												if(angle_velocity > 0.06605993956327438):
													if(y_velocity <= 0.019714023917913437):
														return True
										else:
											if(angle > 0.13291499763727188):
												return True
							else:
								if(lander_x <= -0.1301352009177208):
									if(angle_velocity <= 0.4115541875362396):
										return True
				else:
					return True
			else:
				if(x_velocity <= -0.29952582716941833):
					if(angle <= -0.0669122189283371):
						if(angle_velocity <= -0.31141039729118347):
							if(x_velocity <= -0.6054616570472717):
								return True
							else:
								if(y_velocity > -0.1259635053575039):
									if(lander_y > 1.459312617778778):
										if(x_velocity <= -0.5541252493858337):
											if(angle > -0.12758800759911537):
												return True
					else:
						if(lander_y <= 1.5030698776245117):
							return True
						else:
							if(x_velocity <= -0.445543497800827):
								return True
				else:
					if(x_velocity <= 0.2370886579155922):
						if(angle <= -0.00334473280236125):
							if(y_velocity <= -0.1187281422317028):
								if(lander_x > -0.008284378331154585):
									return True
							else:
								if(angle <= -0.02227552980184555):
									if(angle_velocity <= -0.0828390121459961):
										if(y_velocity > -0.11646486073732376):
											if(lander_y <= 1.4232779741287231):
												if(lander_y > 1.4201720356941223):
													if(angle_velocity <= -0.1772889941930771):
														return True
											else:
												if(angle > -0.15128538757562637):
													if(angle_velocity > -0.11093137785792351):
														if(lander_x <= -0.028021334670484066):
															return True
									else:
										return True
								else:
									if(x_velocity <= -0.24020950496196747):
										if(angle_velocity > -0.174425907433033):
											return True
									else:
										if(y_velocity <= -0.07852547243237495):
											if(angle_velocity > -0.04063395503908396):
												return True
										else:
											if(lander_x <= 0.005284500075504184):
												if(angle_velocity <= -0.024072550237178802):
													if(angle <= -0.021963967010378838):
														return True
													else:
														if(angle_velocity <= -0.07620223984122276):
															if(angle_velocity > -0.10634908080101013):
																if(y_velocity <= 0.3189091980457306):
																	return True
														else:
															if(angle_velocity > -0.03161052614450455):
																if(angle <= -0.00671025225892663):
																	return True
												else:
													return True
						else:
							if(x_velocity <= -0.12136666104197502):
								return True
							else:
								if(y_velocity <= -0.03921147249639034):
									if(angle_velocity <= 0.17280402034521103):
										if(x_velocity <= 0.19898531585931778):
											if(angle_velocity <= 0.13633114844560623):
												if(lander_y <= 1.404726803302765):
													return True
												else:
													if(x_velocity <= 0.11053816229104996):
														if(angle_velocity > 0.02529743779450655):
															if(lander_x > 0.014724159613251686):
																return True
											else:
												if(lander_x > 0.015069055370986462):
													return True
									else:
										if(x_velocity <= 0.22994697093963623):
											return True
								else:
									if(lander_x <= 0.0017909050220623612):
										if(lander_y <= 1.4155747890472412):
											if(x_velocity <= -0.051502836868166924):
												return True
											else:
												if(angle <= -0.0009680459916125983):
													return True
										else:
											if(angle <= 0.006337355822324753):
												if(lander_x <= -0.010935783386230469):
													if(x_velocity <= -0.10414125770330429):
														return True
												else:
													if(lander_y <= 1.4177979230880737):
														if(lander_y > 1.4172518849372864):
															return True
											else:
												return True
									else:
										if(angle_velocity > 0.10761477425694466):
											if(angle_velocity > 0.19915063679218292):
												return True
					else:
						if(x_velocity <= 0.46994757652282715):
							if(lander_y <= 1.4616153836250305):
								if(y_velocity <= 0.2778199464082718):
									if(lander_x > 0.06875791400671005):
										if(angle_velocity > 0.3267119824886322):
											return True
							else:
								if(y_velocity <= -0.01241840049624443):
									if(angle_velocity > 0.1952170878648758):
										return True
								else:
									if(angle_velocity > 0.1323314756155014):
										if(lander_x > 0.09310021251440048):
											return True
						else:
							if(angle_velocity > 0.48394937813282013):
								if(x_velocity <= 0.5864104330539703):
									return True
		else:
			if(angle_velocity <= -0.0002966387401102111):
				if(angle <= 0.3039054870605469):
					if(lander_x <= -0.28749994933605194):
						return True
					else:
						if(lander_y <= -0.04361077770590782):
							if(y_velocity <= 0.0002322039581486024):
								return True
				else:
					if(x_velocity <= 0.0013785074697807431):
						if(lander_x <= -0.23232891410589218):
							if(x_velocity <= 0.0013156583881936967):
								return True
							else:
								if(lander_y <= -0.0431901179254055):
									return True
						else:
							if(lander_x <= -0.23217620700597763):
								if(lander_x > -0.23226668685674667):
									return True
					else:
						if(lander_x <= -0.24004290252923965):
							return True
						else:
							if(angle_velocity > -0.0005263057246338576):
								if(angle > 0.304432675242424):
									return True
			else:
				if(lander_y <= -0.04202711209654808):
					if(y_velocity <= -0.0002578590210760012):
						if(lander_x <= -0.23773784190416336):
							if(lander_x <= -0.23841527104377747):
								if(x_velocity <= -0.0014504787395708263):
									return True
								else:
									if(lander_x <= -0.2729504704475403):
										return True
							else:
								if(lander_y <= -0.04298262298107147):
									if(y_velocity <= -0.0006346373702399433):
										return True
								else:
									return True
						else:
							if(angle <= 0.29945676028728485):
								if(y_velocity <= -0.0009148360113613307):
									if(y_velocity <= -0.0013403847115114331):
										if(angle <= 0.29289789497852325):
											if(angle_velocity > 0.00512483436614275):
												return True
										else:
											return True
									else:
										if(angle > 0.29685693979263306):
											if(lander_x <= -0.2296057939529419):
												return True
							else:
								if(x_velocity <= -0.0028954772278666496):
									if(lander_x <= -0.23037397861480713):
										return True
									else:
										if(x_velocity <= -0.004811337450519204):
											return True
								else:
									if(angle <= 0.3015734851360321):
										if(lander_x <= -0.23662061989307404):
											return True
									else:
										return True
					else:
						if(angle <= 0.303544357419014):
							if(lander_x <= -0.27298156917095184):
								return True
							else:
								if(lander_y <= -0.043588677421212196):
									return True
								else:
									if(x_velocity <= -0.0015286349807865918):
										return True
									else:
										if(y_velocity <= -0.00014368049596669152):
											if(angle <= 0.3028325289487839):
												if(angle <= 0.2964203506708145):
													return True
											else:
												return True
						else:
							if(lander_x <= -0.2321137711405754):
								return True
							else:
								if(x_velocity <= -0.00029814841036568396):
									return True
				else:
					if(left_leg_contact != True):
						if(angle <= 0.20635519921779633):
							if(angle <= 0.19654808193445206):
								if(x_velocity <= 0.582934558391571):
									return True
						else:
							if(x_velocity <= 0.6184144616127014):
								if(lander_y <= 1.5055248737335205):
									return True
								else:
									if(angle_velocity <= 0.35301069915294647):
										if(x_velocity <= 0.49113956093788147):
											return True
									else:
										return True
					else:
						if(lander_x <= -0.23503723740577698):
							if(lander_y <= -0.03342694975435734):
								if(y_velocity <= -0.00031181934173218906):
									if(angle <= 0.29256346821784973):
										if(lander_x <= -0.27979449927806854):
											if(y_velocity <= -0.005563078681007028):
												if(x_velocity <= -0.03565696254372597):
													return True
											else:
												if(angle > 0.24749747663736343):
													if(x_velocity <= -0.04683324880897999):
														return True
													else:
														if(angle_velocity > 0.008627701085060835):
															if(angle <= 0.2606273740530014):
																if(angle_velocity > 0.011774625163525343):
																	if(angle > 0.2534070312976837):
																		return True
															else:
																return True
										else:
											if(y_velocity <= -0.0006552657578140497):
												if(lander_x <= -0.27048829197883606):
													if(lander_x <= -0.2708262652158737):
														return True
													else:
														if(lander_y > -0.041449401527643204):
															return True
												else:
													if(x_velocity <= -0.00947643257677555):
														if(lander_x <= -0.2688800096511841):
															return True
														else:
															if(x_velocity <= -0.01223765965551138):
																if(lander_y <= -0.04041311889886856):
																	return True
																else:
																	if(y_velocity <= -0.0025606987765058875):
																		if(lander_x <= -0.26284368336200714):
																			return True
																		else:
																			if(x_velocity <= -0.026978440582752228):
																				if(lander_x <= -0.26045216619968414):
																					return True
																				else:
																					if(x_velocity <= -0.06665289029479027):
																						return True
																					else:
																						if(y_velocity <= -0.003999263746663928):
																							if(lander_x <= -0.2584616243839264):
																								return True
																							else:
																								if(angle > 0.24389991164207458):
																									if(angle_velocity <= 0.018895636312663555):
																										if(lander_y <= -0.03638923354446888):
																											if(y_velocity <= -0.005372762447223067):
																												return True
																											else:
																												if(angle > 0.2633099853992462):
																													if(x_velocity <= -0.035358116030693054):
																														return True
																									else:
																										if(lander_x <= -0.24810293316841125):
																											return True
																										else:
																											if(angle_velocity > 0.022017963230609894):
																												return True
																	else:
																		if(lander_y <= -0.04012190364301205):
																			if(y_velocity <= -0.0020756263402290642):
																				return True
													else:
														if(lander_y <= -0.041261376813054085):
															if(y_velocity <= -0.0009450570505578071):
																return True
									else:
										if(lander_x <= -0.2535083740949631):
											return True
										else:
											if(angle_velocity > 0.0032097346847876906):
												return True
								else:
									if(lander_x <= -0.27284882962703705):
										if(angle_velocity > 0.0005846305866725743):
											return True
							else:
								if(y_velocity <= -0.009919839445501566):
									return True
								else:
									if(y_velocity <= -0.009197108913213015):
										if(angle > 0.229521743953228):
											return True
						else:
							if(y_velocity <= -0.0017634674441069365):
								if(y_velocity <= -0.014181504491716623):
									if(x_velocity <= 0.045335978269577026):
										if(angle <= 0.20899919420480728):
											if(x_velocity <= -0.11125599592924118):
												if(angle <= 0.1932438611984253):
													if(angle_velocity <= 0.06029107794165611):
														if(angle > 0.18885479122400284):
															if(y_velocity <= -0.01869307179003954):
																return True
													else:
														return True
												else:
													return True
											else:
												if(lander_x <= -0.1810481995344162):
													if(x_velocity <= -0.10662930458784103):
														if(angle_velocity <= 0.05132148042321205):
															return True
												else:
													return True
										else:
											return True
								else:
									if(angle <= 0.29117703437805176):
										if(x_velocity <= -0.014963520225137472):
											if(angle <= 0.28673432767391205):
												if(x_velocity <= -0.02327061351388693):
													if(lander_y <= -0.03942263312637806):
														if(angle <= 0.27718666195869446):
															if(lander_x > -0.22879020869731903):
																return True
														else:
															return True
													else:
														if(y_velocity <= -0.005009366665035486):
															if(lander_y <= -0.03856287710368633):
																return True
															else:
																if(x_velocity <= -0.04225950874388218):
																	if(angle <= 0.25911061465740204):
																		if(lander_x <= -0.21519596874713898):
																			if(angle > 0.20358587801456451):
																				if(x_velocity <= -0.052496904507279396):
																					if(angle <= 0.2514372915029526):
																						if(y_velocity <= -0.012675213161855936):
																							return True
																						else:
																							if(lander_y <= -0.029767395928502083):
																								if(y_velocity <= -0.011487866286188364):
																									return True
																								else:
																									if(lander_y <= -0.03101267386227846):
																										if(y_velocity <= -0.010406606364995241):
																											return True
																										else:
																											if(angle > 0.24915795773267746):
																												if(x_velocity <= -0.05765606090426445):
																													return True
																					else:
																						return True
																		else:
																			if(y_velocity > -0.013802431058138609):
																				if(x_velocity <= -0.07644497230648994):
																					if(y_velocity <= -0.006820400943979621):
																						if(angle_velocity <= 0.03866227902472019):
																							return True
																						else:
																							if(y_velocity <= -0.013106403406709433):
																								return True
																					else:
																						if(y_velocity <= -0.005661074770614505):
																							if(lander_x <= -0.18308457732200623):
																								return True
																						else:
																							return True
																				else:
																					if(lander_y <= -0.03367278166115284):
																						if(y_velocity <= -0.010693163145333529):
																							return True
																						else:
																							if(angle <= 0.2468985989689827):
																								if(x_velocity <= -0.06347637996077538):
																									if(angle_velocity <= 0.030273349955677986):
																										return True
																							else:
																								if(x_velocity <= -0.04866452142596245):
																									if(x_velocity <= -0.05291973799467087):
																										return True
																									else:
																										if(lander_x <= -0.2128155753016472):
																											return True
																					else:
																						if(angle_velocity > 0.03657999262213707):
																							if(lander_x <= -0.20477870106697083):
																								return True
																	else:
																		return True
																else:
																	if(angle > 0.2676932066679001):
																		if(angle_velocity <= 0.017368759959936142):
																			if(angle > 0.27267181873321533):
																				return True
																		else:
																			return True
														else:
															if(angle > 0.2776561379432678):
																if(angle <= 0.27853506803512573):
																	return True
												else:
													if(lander_x <= -0.23180026561021805):
														if(angle_velocity > 0.009558133315294981):
															return True
													else:
														if(angle > 0.2844739258289337):
															if(y_velocity <= -0.0033114090329036117):
																return True
											else:
												if(lander_x <= -0.22632689028978348):
													return True
												else:
													if(angle_velocity > 0.009472921025007963):
														return True
									else:
										if(y_velocity <= -0.0017753514694049954):
											return True
										else:
											if(y_velocity > -0.0017680999008007348):
												return True
							else:
								if(angle_velocity <= 0.10090447217226028):
									if(angle <= 0.2965114265680313):
										if(angle > 0.295711025595665):
											if(angle_velocity > 0.003781290724873543):
												return True
									else:
										return True
								else:
									return True
	return False

