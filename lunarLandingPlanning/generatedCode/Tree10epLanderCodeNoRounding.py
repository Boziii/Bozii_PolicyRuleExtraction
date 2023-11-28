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
	if(y_velocity <= -0.1794271618127823):
		if(angle_velocity <= -0.03374768979847431):
			if(x_velocity > -0.5751650929450989):
				if(lander_x <= 0.08611369132995605):
					if(angle_velocity <= -0.06118399649858475):
						if(y_velocity > -0.471153199672699):
							if(lander_y <= 1.337690532207489):
								if(lander_y <= 0.0026220297440886497):
									if(lander_y <= 0.00022762175649404526):
										return True
								else:
									if(angle_velocity <= -0.0741475485265255):
										if(lander_y <= 1.3131136894226074):
											if(lander_y <= 0.020061002112925053):
												if(lander_x <= -0.1745845302939415):
													return True
											else:
												if(lander_x <= -0.26607297360897064):
													if(angle <= -0.04963227920234203):
														if(angle > -0.09790131822228432):
															if(x_velocity > -0.040723237209022045):
																return True
									else:
										if(angle_velocity > -0.07155049592256546):
											if(lander_y > 0.04048412851989269):
												if(lander_x <= -0.2675226926803589):
													return True
							else:
								if(lander_x <= -0.044382667168974876):
									if(x_velocity > -0.495346337556839):
										if(lander_y > 1.3572929501533508):
											if(lander_y > 1.405482828617096):
												if(lander_x > -0.11175217851996422):
													if(y_velocity > -0.26613157987594604):
														if(angle_velocity > -0.24807125329971313):
															if(y_velocity > -0.24698907881975174):
																if(y_velocity > -0.21964573115110397):
																	if(angle_velocity <= -0.13918894156813622):
																		return True
		else:
			if(y_velocity > -0.21407920122146606):
				if(x_velocity <= 0.05567553639411926):
					if(lander_y <= 0.15316959470510483):
						if(y_velocity <= -0.20384977012872696):
							if(angle <= -0.02807968109846115):
								if(lander_x <= -0.1437944397330284):
									if(x_velocity > 0.003558885306119919):
										return True
				else:
					if(lander_y <= 0.3776385486125946):
						if(angle_velocity <= -0.005083222407847643):
							if(angle <= 0.042888093739748):
								if(y_velocity > -0.20252463966608047):
									if(lander_y <= 0.00828982365783304):
										return True
	else:
		if(y_velocity <= -5.539971425605472e-06):
			if(lander_y <= -0.04273167438805103):
				if(x_velocity <= -0.0013848317903466523):
					if(angle <= 0.29617390036582947):
						if(angle_velocity <= 0.000927366258110851):
							return True
				else:
					if(lander_x > -0.23545122146606445):
						return True
			else:
				if(y_velocity <= -0.13607718795537949):
					if(angle <= 0.0022962415823712945):
						if(lander_y <= 0.00013242126442492008):
							return True
						else:
							if(angle <= -0.06730449758470058):
								if(angle_velocity <= -0.12910724058747292):
									if(x_velocity <= -0.4386965483427048):
										return True
								else:
									return True
					else:
						if(lander_y <= 0.0935308188199997):
							if(y_velocity <= -0.17297670990228653):
								if(angle > 0.02057494269683957):
									if(angle > 0.04552014172077179):
										return True
							else:
								if(angle <= 0.010550695471465588):
									if(right_leg_contact == True):
										return True
				else:
					if(angle <= 0.16217593103647232):
						if(right_leg_contact != True):
							if(angle <= 0.0024438646505586803):
								if(x_velocity <= 0.08589649200439453):
									if(angle <= -0.16033270955085754):
										if(y_velocity > -0.10403138026595116):
											return True
									else:
										if(x_velocity > -0.4444125294685364):
											if(lander_y <= 1.423512041568756):
												if(lander_x <= -0.06536378897726536):
													return True
											else:
												return True
						else:
							if(angle_velocity <= 0.3967301696538925):
								if(lander_y <= 0.004199722781777382):
									return True
					else:
						if(angle_velocity <= 0.0017847815761342645):
							if(lander_y <= -0.04265029542148113):
								if(x_velocity <= -0.0024095873814076185):
									if(angle > 0.3002530485391617):
										return True
								else:
									return True
							else:
								return True
						else:
							if(lander_y <= -0.04234050214290619):
								if(x_velocity > -0.0046468020882457495):
									if(lander_y > -0.04249696433544159):
										return True
							else:
								if(angle_velocity <= 0.0032612187787890434):
									if(lander_x <= -0.2615768313407898):
										if(x_velocity > -0.006839883280918002):
											return True
									else:
										return True
								else:
									if(lander_y <= -0.04181877709925175):
										if(x_velocity > -0.008380806539207697):
											if(angle <= 0.29680824279785156):
												return True
									else:
										if(x_velocity <= -0.012251785025000572):
											if(lander_y > -0.04118398763239384):
												if(y_velocity <= -0.002687436994165182):
													if(lander_y > -0.0404499564319849):
														if(angle_velocity <= 0.011433977633714676):
															if(lander_x <= -0.25365176796913147):
																if(x_velocity > -0.022373304702341557):
																	return True
															else:
																if(angle <= 0.28308115899562836):
																	return True
																else:
																	if(lander_y <= -0.04019818641245365):
																		return True
														else:
															if(lander_y > -0.03899117186665535):
																if(y_velocity <= -0.005640836199745536):
																	if(angle_velocity <= 0.04400370270013809):
																		if(angle <= 0.2571589797735214):
																			if(x_velocity <= -0.05234070494771004):
																				if(angle <= 0.251819372177124):
																					if(y_velocity <= -0.007373640080913901):
																						if(lander_x > -0.23819973319768906):
																							if(x_velocity <= -0.06272612698376179):
																								if(angle <= 0.24191226810216904):
																									if(x_velocity <= -0.07616688311100006):
																										if(lander_y <= -0.03136422112584114):
																											if(angle_velocity <= 0.033190540969371796):
																												if(angle <= 0.2267962023615837):
																													return True
																												else:
																													if(angle_velocity <= 0.030724934302270412):
																														if(lander_y > -0.033196063712239265):
																															return True
																										else:
																											if(y_velocity <= -0.012519416864961386):
																												if(lander_x > -0.22018971294164658):
																													if(angle_velocity <= 0.042367175221443176):
																														return True
																													else:
																														if(angle_velocity > 0.04368840530514717):
																															return True
																											else:
																												return True
																									else:
																										if(lander_x <= -0.23429329693317413):
																											if(angle_velocity <= 0.027161788195371628):
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
																			if(x_velocity <= -0.04083433002233505):
																				if(lander_y > -0.03676494024693966):
																					if(lander_x <= -0.21776404976844788):
																						return True
																			else:
																				if(angle <= 0.2682659924030304):
																					return True
																				else:
																					if(lander_x > -0.22226682305335999):
																						if(angle_velocity <= 0.017718179151415825):
																							return True
																	else:
																		if(lander_y <= -0.027718706987798214):
																			if(lander_x > -0.19709019362926483):
																				if(angle_velocity <= 0.05161963030695915):
																					return True
																		else:
																			if(x_velocity <= -0.11905135959386826):
																				if(angle <= 0.1867682784795761):
																					if(x_velocity <= -0.13479279726743698):
																						if(angle <= 0.17366572469472885):
																							if(lander_y <= -0.02362812403589487):
																								if(x_velocity > -0.151354618370533):
																									return True
																					else:
																						return True
																			else:
																				return True
																else:
																	if(lander_x <= -0.24843239784240723):
																		if(y_velocity <= -0.00434582494199276):
																			if(x_velocity > -0.03575035743415356):
																				if(angle <= 0.2678629904985428):
																					return True
																		else:
																			return True
																	else:
																		return True
												else:
													if(lander_x <= -0.25743556022644043):
														if(x_velocity > -0.01417884137481451):
															return True
													else:
														return True
										else:
											if(angle <= 0.2935708165168762):
												return True
											else:
												if(lander_x <= -0.23190200328826904):
													return True
		else:
			if(x_velocity <= -0.3530505746603012):
				if(angle_velocity <= -0.33629027009010315):
					return True
			else:
				if(lander_y <= -0.04316948354244232):
					if(y_velocity > 0.00021419233235064894):
						return True
				else:
					if(y_velocity <= 0.3010060638189316):
						if(lander_y <= 1.4903365969657898):
							if(lander_y <= -0.043138207867741585):
								if(angle_velocity <= -0.00026711064856499434):
									return True
							else:
								if(x_velocity <= 0.10652254521846771):
									if(x_velocity <= 0.0929892361164093):
										if(x_velocity <= 0.0282497750595212):
											return True
										else:
											if(angle <= 0.15381637960672379):
												return True
									else:
										if(y_velocity > 0.0400815699249506):
											return True
								else:
									if(y_velocity > 0.17286856845021248):
										return True
	return False

def weShould_left_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.1794271618127823):
		if(angle_velocity <= -0.03374768979847431):
			if(x_velocity > -0.5751650929450989):
				if(lander_x <= 0.08611369132995605):
					if(angle_velocity <= -0.06118399649858475):
						if(y_velocity <= -0.471153199672699):
							if(x_velocity <= -0.45727430284023285):
								if(y_velocity <= -0.4953022450208664):
									if(angle <= -0.3465820550918579):
										if(y_velocity > -0.5506829917430878):
											if(lander_y <= 1.1288045644760132):
												if(angle <= -0.37658238410949707):
													return True
												else:
													if(lander_y <= 0.9626513123512268):
														return True
											else:
												return True
									else:
										if(angle_velocity <= -0.24690931290388107):
											if(lander_x > -0.19378521293401718):
												return True
								else:
									return True
						else:
							if(lander_y <= 1.337690532207489):
								if(lander_y > 0.0026220297440886497):
									if(angle_velocity <= -0.0741475485265255):
										if(lander_y <= 1.3131136894226074):
											if(lander_y <= 0.020061002112925053):
												if(lander_x > -0.1745845302939415):
													return True
											else:
												if(lander_x <= -0.26607297360897064):
													if(angle <= -0.04963227920234203):
														if(angle <= -0.09790131822228432):
															return True
														else:
															if(x_velocity <= -0.040723237209022045):
																return True
												else:
													return True
										else:
											if(lander_x > -0.06945323944091797):
												return True
									else:
										if(angle_velocity <= -0.07155049592256546):
											if(lander_y <= 0.19064445793628693):
												if(angle_velocity <= -0.07257240638136864):
													return True
										else:
											if(lander_y <= 0.04048412851989269):
												if(angle <= -0.029536149464547634):
													return True
											else:
												if(lander_x > -0.2675226926803589):
													if(y_velocity <= -0.22875476628541946):
														if(lander_y > 0.28995607048273087):
															if(x_velocity <= 0.055796544067561626):
																if(angle_velocity <= -0.06678783893585205):
																	if(lander_y <= 0.5890035629272461):
																		if(x_velocity <= -0.09857357665896416):
																			if(x_velocity > -0.12064360454678535):
																				return True
																	else:
																		return True
																else:
																	return True
													else:
														return True
							else:
								if(lander_x <= -0.044382667168974876):
									if(x_velocity > -0.495346337556839):
										if(lander_y <= 1.3572929501533508):
											if(x_velocity > -0.3490128368139267):
												return True
										else:
											if(lander_y <= 1.405482828617096):
												return True
											else:
												if(lander_x <= -0.11175217851996422):
													if(angle <= -0.2549261003732681):
														if(y_velocity > -0.39258597791194916):
															return True
												else:
													if(y_velocity <= -0.26613157987594604):
														return True
													else:
														if(angle_velocity <= -0.24807125329971313):
															return True
														else:
															if(y_velocity > -0.24698907881975174):
																if(y_velocity <= -0.21964573115110397):
																	return True
																else:
																	if(angle_velocity > -0.13918894156813622):
																		if(x_velocity > -0.22581874579191208):
																			return True
					else:
						if(y_velocity <= -0.21787553280591965):
							if(lander_y <= 0.16229546815156937):
								if(lander_x > 0.017193173989653587):
									return True
							else:
								if(y_velocity <= -0.2387385368347168):
									if(lander_y <= 0.3841242343187332):
										if(y_velocity <= -0.26827841997146606):
											return True
									else:
										if(lander_y <= 1.06383216381073):
											if(angle <= 0.002238634799141437):
												if(x_velocity <= -0.0601305216550827):
													if(y_velocity <= -0.2705176919698715):
														if(lander_y <= 1.0086975693702698):
															if(angle_velocity <= -0.040436457842588425):
																if(lander_x <= -0.24930714070796967):
																	return True
																else:
																	if(y_velocity > -0.3079618811607361):
																		if(lander_y > 0.689493864774704):
																			return True
															else:
																return True
														else:
															return True
												else:
													if(y_velocity <= -0.27133090794086456):
														if(lander_y <= 0.6653814017772675):
															if(lander_y <= 0.550684005022049):
																return True
														else:
															return True
													else:
														return True
											else:
												if(lander_y <= 0.8134848177433014):
													if(lander_x <= -0.01664447784423828):
														if(angle > 0.03958132490515709):
															if(angle <= 0.048138877376914024):
																return True
													else:
														return True
												else:
													return True
										else:
											if(y_velocity <= -0.2716999799013138):
												if(lander_y <= 1.4152650833129883):
													if(angle_velocity <= -0.04379095137119293):
														if(angle_velocity <= -0.054561953991651535):
															if(y_velocity > -0.4885164946317673):
																if(lander_y <= 1.3260449767112732):
																	return True
													else:
														if(y_velocity > -0.46020735800266266):
															if(lander_y <= 1.2770281434059143):
																if(angle_velocity <= -0.03769991733133793):
																	if(y_velocity <= -0.3716417998075485):
																		return True
															else:
																return True
								else:
									if(lander_x <= -0.17753000557422638):
										if(lander_x <= -0.20264949649572372):
											if(x_velocity > -0.005664132535457611):
												if(y_velocity <= -0.2187153846025467):
													if(angle_velocity > -0.058140555396676064):
														return True
										else:
											if(y_velocity > -0.2191307619214058):
												return True
									else:
										if(x_velocity <= -0.022700208239257336):
											if(angle_velocity > -0.041635483503341675):
												return True
										else:
											return True
						else:
							if(x_velocity <= -0.005532991839572787):
								if(y_velocity <= -0.214475579559803):
									return True
								else:
									if(lander_y <= 0.04115825518965721):
										return True
									else:
										if(lander_x > 0.020705843344330788):
											return True
							else:
								if(angle <= 0.037747710943222046):
									if(x_velocity <= 0.03981081768870354):
										if(lander_x > -0.18413691222667694):
											if(lander_y > 0.036178966984152794):
												return True
									else:
										return True
								else:
									if(angle > 0.046605899930000305):
										return True
				else:
					if(y_velocity <= -0.28930096328258514):
						if(x_velocity <= -0.09774887561798096):
							if(y_velocity <= -0.3197402209043503):
								if(y_velocity > -0.3251473754644394):
									if(y_velocity <= -0.3240727335214615):
										return True
							else:
								if(y_velocity <= -0.30194254219532013):
									if(lander_y > 0.8830546736717224):
										if(x_velocity <= -0.14677271991968155):
											return True
										else:
											if(lander_y > 0.9878422915935516):
												return True
					else:
						if(lander_y <= 1.0637657046318054):
							if(angle_velocity <= -0.3381737321615219):
								return True
							else:
								if(angle <= 0.0773346540518105):
									return True
		else:
			if(y_velocity <= -0.21407920122146606):
				if(lander_y <= 0.3921949416399002):
					if(angle <= -0.04154000245034695):
						if(angle_velocity <= -0.0036754703614860773):
							if(lander_x <= -0.060271358117461205):
								return True
						else:
							if(angle_velocity <= 0.036015814170241356):
								if(y_velocity <= -0.2208710014820099):
									if(angle_velocity <= 0.013978915754705667):
										if(angle_velocity > 0.012660620268434286):
											return True
					else:
						if(lander_y <= 0.3257696032524109):
							if(angle_velocity <= 0.060555048286914825):
								if(angle_velocity <= -0.03097302559763193):
									if(angle <= -0.00851858058013022):
										return True
								else:
									if(x_velocity <= 0.07102743536233902):
										if(angle <= -0.032545069232583046):
											if(lander_x > -0.08671960979700089):
												return True
									else:
										if(x_velocity <= 0.07179636508226395):
											return True
										else:
											if(lander_y > 0.2872631996870041):
												if(x_velocity <= 0.09572063013911247):
													return True
						else:
							if(y_velocity <= -0.22192434966564178):
								if(angle <= -0.02769833616912365):
									if(y_velocity > -0.24259628355503082):
										return True
								else:
									if(lander_x <= 0.016397570725530386):
										if(angle <= -0.019261649809777737):
											if(x_velocity <= 0.01757714617997408):
												return True
									else:
										if(x_velocity > -0.004945871303789318):
											return True
							else:
								if(angle <= 0.004637096542865038):
									if(angle_velocity <= 0.021830779500305653):
										if(lander_x <= -0.24376244097948074):
											if(y_velocity <= -0.21736398339271545):
												return True
										else:
											return True
				else:
					if(y_velocity <= -0.25619785487651825):
						if(lander_y <= 0.756659984588623):
							if(angle_velocity <= 0.053107040002942085):
								if(lander_x <= -0.3122215270996094):
									return True
								else:
									if(angle_velocity <= -0.02403460629284382):
										if(lander_x <= 0.049027539789676666):
											if(x_velocity <= 0.013191134203225374):
												if(angle_velocity > -0.024255387485027313):
													return True
											else:
												if(lander_y <= 0.7294978499412537):
													return True
										else:
											return True
									else:
										if(lander_y <= 0.7253215312957764):
											if(lander_x <= 0.04834899865090847):
												if(lander_y <= 0.6934561133384705):
													if(x_velocity > 0.027755615301430225):
														if(x_velocity <= 0.03154201339930296):
															return True
												else:
													if(lander_y <= 0.6977581083774567):
														return True
											else:
												if(y_velocity > -0.2674541026353836):
													if(x_velocity > -0.047152647748589516):
														return True
										else:
											if(y_velocity > -0.27764803171157837):
												if(angle <= 0.0003093401901423931):
													if(lander_y <= 0.736640989780426):
														return True
													else:
														if(lander_y > 0.7442370653152466):
															return True
							else:
								if(y_velocity <= -0.2809235751628876):
									if(lander_x <= -0.3022411912679672):
										if(lander_x <= -0.3024405688047409):
											if(lander_x <= -0.3025939017534256):
												if(angle_velocity <= 0.07512351870536804):
													if(angle_velocity > 0.06418810971081257):
														return True
											else:
												if(y_velocity <= -0.3078501671552658):
													return True
								else:
									if(lander_y > 0.6383659839630127):
										if(lander_y <= 0.7437300682067871):
											if(angle <= -0.13229959458112717):
												return True
						else:
							if(y_velocity <= -0.28801071643829346):
								if(x_velocity > -0.6012959033250809):
									if(angle <= -0.08344867825508118):
										if(y_velocity <= -0.3144092857837677):
											if(angle_velocity <= 0.07320805639028549):
												if(y_velocity <= -0.477528378367424):
													if(lander_x <= -0.2730148583650589):
														return True
													else:
														if(angle <= -0.40019458532333374):
															return True
												else:
													if(angle <= -0.1618097871541977):
														if(lander_y <= 1.035351276397705):
															return True
														else:
															if(angle_velocity <= 0.042507411912083626):
																if(x_velocity > -0.4070647954940796):
																	if(lander_y <= 1.1711307764053345):
																		if(angle > -0.23966187983751297):
																			return True
																	else:
																		return True
															else:
																if(y_velocity <= -0.4351184517145157):
																	if(lander_x <= -0.22564711421728134):
																		return True
																else:
																	if(angle_velocity > 0.0557756032794714):
																		return True
													else:
														if(y_velocity > -0.3831930011510849):
															if(lander_y <= 1.2878214716911316):
																if(angle_velocity <= 0.05483861267566681):
																	return True
																else:
																	if(angle_velocity > 0.0682828240096569):
																		if(angle <= -0.10975176095962524):
																			return True
											else:
												if(y_velocity <= -0.4177473336458206):
													if(angle <= -0.3375735878944397):
														if(angle <= -0.3402484655380249):
															if(angle <= -0.37468601763248444):
																if(y_velocity > -0.5115708261728287):
																	return True
														else:
															return True
												else:
													if(angle <= -0.29154936969280243):
														return True
													else:
														if(angle <= -0.18757214397192):
															if(angle_velocity <= 0.11136408150196075):
																if(angle_velocity > 0.08498131856322289):
																	if(y_velocity <= -0.3588618338108063):
																		if(y_velocity <= -0.3929747939109802):
																			if(lander_y > 1.1615955829620361):
																				return True
																		else:
																			return True
															else:
																if(angle_velocity > 0.1375076174736023):
																	if(lander_y <= 0.7631669342517853):
																		return True
																	else:
																		if(x_velocity > -0.11636003851890564):
																			if(angle_velocity <= 0.21785646677017212):
																				return True
														else:
															if(y_velocity > -0.3378104418516159):
																if(x_velocity <= -0.06753591820597649):
																	if(angle <= -0.16573705524206161):
																		return True
																else:
																	if(angle <= -0.1466396152973175):
																		if(x_velocity <= -0.04957428388297558):
																			return True
										else:
											if(x_velocity > -0.04757325537502766):
												if(lander_x <= -0.23177415877580643):
													if(angle_velocity > 0.12944075465202332):
														if(angle <= -0.1436707004904747):
															return True
												else:
													return True
									else:
										if(x_velocity <= 0.4006662517786026):
											if(lander_y <= 1.4005308151245117):
												if(angle <= -0.056163057684898376):
													if(angle <= -0.057672999799251556):
														if(angle_velocity <= -0.006322822999209166):
															return True
														else:
															if(x_velocity > 0.0047135800996329635):
																if(angle_velocity <= 0.09392179548740387):
																	return True
													else:
														return True
												else:
													if(angle_velocity <= -0.017868186347186565):
														if(x_velocity <= -0.006938037695363164):
															if(angle_velocity > -0.018235708586871624):
																return True
														else:
															if(lander_x <= 0.06481532752513885):
																return True
													else:
														if(angle_velocity <= 0.12197757884860039):
															if(lander_y > 1.3639748096466064):
																if(angle_velocity <= 0.025284748058766127):
																	return True
											else:
												return True
										else:
											return True
							else:
								if(x_velocity <= 0.0004683749375544721):
									if(angle_velocity <= -0.0074590276926755905):
										if(angle <= 0.006225094897672534):
											if(x_velocity > -0.06540152803063393):
												return True
										else:
											if(lander_y > 1.0984411835670471):
												if(angle_velocity > -0.00896394718438387):
													return True
									else:
										if(x_velocity <= -0.01113809272646904):
											if(y_velocity <= -0.2866400480270386):
												if(lander_x <= -0.098794125020504):
													return True
										else:
											if(y_velocity <= -0.2648134231567383):
												if(x_velocity > -0.008833963423967361):
													return True
								else:
									if(lander_y <= 1.331590175628662):
										if(lander_x <= 0.12066392600536346):
											if(angle <= 0.005490051116794348):
												if(angle_velocity <= 0.04106120765209198):
													if(angle_velocity <= -0.01197604276239872):
														if(angle > 0.0009966541547328234):
															return True
													else:
														return True
												else:
													if(angle <= -0.05581046640872955):
														if(y_velocity > -0.27606625854969025):
															return True
													else:
														if(x_velocity <= 0.06725877523422241):
															if(lander_x > -0.12219705432653427):
																if(x_velocity > 0.04005394130945206):
																	return True
														else:
															return True
											else:
												if(angle_velocity <= -0.016522443387657404):
													if(y_velocity > -0.2783309370279312):
														return True
												else:
													if(y_velocity <= -0.25755906105041504):
														if(angle <= 0.013389595318585634):
															if(angle > 0.011251746211200953):
																return True
									else:
										if(x_velocity > 0.05715778097510338):
											if(lander_y <= 1.3929938077926636):
												return True
					else:
						if(x_velocity <= 0.07023638486862183):
							if(lander_y <= 0.6529476046562195):
								if(y_velocity <= -0.23563557863235474):
									if(angle <= -0.03550895117223263):
										if(angle_velocity <= 0.019470511935651302):
											if(y_velocity > -0.25209230184555054):
												return True
									else:
										if(angle_velocity <= -0.01508759567514062):
											if(lander_x <= -0.0686207739636302):
												if(lander_x <= -0.16119647026062012):
													if(y_velocity <= -0.2506799176335335):
														return True
											else:
												return True
								else:
									if(angle_velocity <= -0.005014266120269895):
										if(angle <= 0.03147323336452246):
											if(lander_x <= -0.015294408425688744):
												if(angle <= -0.023666472174227238):
													return True
												else:
													if(angle_velocity <= -0.02928320039063692):
														return True
											else:
												return True
									else:
										if(x_velocity <= 0.06135108321905136):
											if(lander_y <= 0.3956930786371231):
												return True
											else:
												if(lander_y <= 0.6477735638618469):
													if(x_velocity <= 0.05222979746758938):
														if(lander_y <= 0.43056365847587585):
															if(y_velocity > -0.23276302218437195):
																if(angle_velocity <= 0.0032132955093402416):
																	if(x_velocity > 0.00970655819401145):
																		return True
													else:
														if(y_velocity <= -0.22384222596883774):
															return True
												else:
													return True
							else:
								if(y_velocity <= -0.25602202117443085):
									return True
								else:
									if(angle_velocity <= 0.008530027233064175):
										if(angle <= -0.014491644687950611):
											return True
										else:
											if(lander_x <= -0.017577027902007103):
												if(lander_y > 0.9551971554756165):
													if(y_velocity <= -0.2336241751909256):
														return True
											else:
												if(angle <= 0.015776697546243668):
													if(x_velocity > -0.00970389656140469):
														return True
						else:
							if(lander_y <= 0.7661446332931519):
								if(angle_velocity <= 0.10483866930007935):
									if(angle_velocity <= -0.029461241327226162):
										return True
									else:
										if(y_velocity <= -0.21726177632808685):
											if(angle <= 0.012266078498214483):
												if(angle_velocity <= 0.054696567356586456):
													if(x_velocity > 0.08238735049962997):
														return True
											else:
												if(x_velocity > 0.14151576161384583):
													if(x_velocity <= 0.14326975494623184):
														return True
										else:
											if(lander_y <= 0.5303158313035965):
												return True
							else:
								if(y_velocity <= -0.23934240639209747):
									if(angle <= 0.30774688720703125):
										if(angle <= 0.019939959049224854):
											return True
										else:
											if(angle_velocity <= 0.0170087325386703):
												return True
								else:
									if(angle_velocity <= 0.07050533220171928):
										if(y_velocity <= -0.2216755598783493):
											if(angle_velocity <= 0.06220582313835621):
												return True
									else:
										if(lander_y > 1.3443123698234558):
											return True
			else:
				if(x_velocity <= 0.05567553639411926):
					if(lander_y <= 0.15316959470510483):
						if(y_velocity <= -0.20384977012872696):
							if(angle <= -0.02807968109846115):
								if(lander_x <= -0.1437944397330284):
									if(x_velocity <= 0.003558885306119919):
										return True
							else:
								if(y_velocity <= -0.20461011677980423):
									if(angle <= -0.024680593982338905):
										if(angle > -0.025135292671620846):
											return True
								else:
									if(lander_x > -0.12728147208690643):
										if(angle_velocity <= 0.0047361282631754875):
											return True
						else:
							if(y_velocity > -0.19585410505533218):
								if(lander_x <= -0.0862305611371994):
									if(x_velocity <= 0.05218663439154625):
										if(angle <= -0.02899283729493618):
											if(lander_x <= -0.13113193586468697):
												return True
									else:
										if(lander_x <= -0.1685732826590538):
											return True
								else:
									if(lander_x <= 0.02997350785881281):
										return True
					else:
						if(angle_velocity <= -0.02037798799574375):
							if(x_velocity > 0.0009630420245230198):
								if(lander_x <= -0.14824142307043076):
									if(lander_x <= -0.18080510944128036):
										return True
								else:
									return True
						else:
							if(y_velocity <= -0.20896346867084503):
								if(lander_x <= -0.007932853419333696):
									if(y_velocity <= -0.20905029773712158):
										if(x_velocity <= -0.028763396199792624):
											return True
										else:
											if(y_velocity > -0.21027535945177078):
												if(angle <= 0.0017396897310391068):
													return True
								else:
									if(lander_y > 0.2702901065349579):
										return True
							else:
								if(x_velocity <= 0.03942222706973553):
									if(lander_x > 0.037769366055727005):
										if(x_velocity > -0.004351045587100089):
											if(lander_y > 0.21746324747800827):
												return True
								else:
									if(lander_y > 0.18184484541416168):
										if(angle <= -0.004419736564159393):
											if(lander_x > -0.18882811069488525):
												return True
										else:
											if(angle_velocity <= -0.006318030529655516):
												if(angle_velocity > -0.013952825218439102):
													if(x_velocity <= 0.04744401201605797):
														return True
				else:
					if(lander_y <= 0.3776385486125946):
						if(angle_velocity <= -0.005083222407847643):
							if(angle <= 0.042888093739748):
								if(y_velocity <= -0.20252463966608047):
									if(angle <= 0.0035445267567411065):
										return True
									else:
										if(x_velocity > 0.07558076456189156):
											return True
								else:
									if(lander_y > 0.00828982365783304):
										return True
							else:
								if(x_velocity > 0.11827506497502327):
									return True
						else:
							if(angle <= 0.005951379658654332):
								if(y_velocity > -0.2052592635154724):
									if(angle_velocity <= 0.020243342965841293):
										if(lander_y > 0.08994452841579914):
											return True
							else:
								if(angle > 0.012189941480755806):
									if(x_velocity > 0.11312342807650566):
										if(lander_x > -0.16688861697912216):
											return True
					else:
						if(x_velocity <= 0.13456472754478455):
							if(y_velocity <= -0.20617227256298065):
								if(angle_velocity <= 0.025103840045630932):
									if(lander_x > -0.20976068824529648):
										if(angle_velocity <= -0.012998236808925867):
											return True
							else:
								if(lander_x <= -0.034827230498194695):
									if(lander_y <= 0.4492153078317642):
										if(lander_y <= 0.4398427754640579):
											if(angle_velocity <= -0.011567938141524792):
												if(lander_y <= 0.41154973208904266):
													return True
										else:
											return True
								else:
									return True
						else:
							if(angle <= 0.031415401957929134):
								return True
							else:
								if(y_velocity <= -0.18768766522407532):
									if(angle_velocity <= 0.005937085719779134):
										if(x_velocity > 0.14010006934404373):
											return True
								else:
									if(angle_velocity <= 0.033176626078784466):
										return True
	else:
		if(y_velocity <= -5.539971425605472e-06):
			if(lander_y > -0.04273167438805103):
				if(y_velocity <= -0.13607718795537949):
					if(angle <= 0.0022962415823712945):
						if(lander_y > 0.00013242126442492008):
							if(angle <= -0.06730449758470058):
								if(angle_velocity <= -0.12910724058747292):
									if(x_velocity > -0.4386965483427048):
										return True
							else:
								if(x_velocity > 0.03798787482082844):
									if(lander_x > -0.22996079921722412):
										return True
					else:
						if(lander_y <= 0.0935308188199997):
							if(y_velocity <= -0.17297670990228653):
								if(angle > 0.02057494269683957):
									if(angle <= 0.04552014172077179):
										return True
							else:
								if(angle <= 0.010550695471465588):
									if(right_leg_contact != True):
										if(angle > 0.004727513180114329):
											if(lander_x > -0.12393169477581978):
												return True
								else:
									if(angle_velocity <= -0.019128063693642616):
										if(angle_velocity > -0.022645185701549053):
											return True
				else:
					if(angle <= 0.16217593103647232):
						if(right_leg_contact != True):
							if(angle <= 0.0024438646505586803):
								if(x_velocity <= 0.08589649200439453):
									if(angle <= -0.16033270955085754):
										if(y_velocity <= -0.10403138026595116):
											return True
								else:
									return True
							else:
								if(x_velocity > 0.07595284655690193):
									return True
						else:
							if(angle_velocity <= 0.3967301696538925):
								if(lander_y > 0.004199722781777382):
									return True
		else:
			if(x_velocity > -0.3530505746603012):
				if(lander_y > -0.04316948354244232):
					if(y_velocity <= 0.3010060638189316):
						if(lander_y <= 1.4903365969657898):
							if(lander_y > -0.043138207867741585):
								if(x_velocity <= 0.10652254521846771):
									if(x_velocity > 0.0929892361164093):
										if(y_velocity <= 0.0400815699249506):
											return True
								else:
									if(y_velocity <= 0.17286856845021248):
										return True
	return False

def weShould_main_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.1794271618127823):
		if(angle_velocity <= -0.03374768979847431):
			if(x_velocity <= -0.5751650929450989):
				if(lander_y <= 1.3026283979415894):
					if(x_velocity > -0.7040518224239349):
						if(x_velocity <= -0.6311948895454407):
							if(y_velocity <= -0.5590022504329681):
								if(angle_velocity <= -0.23465460538864136):
									return True
								else:
									if(x_velocity <= -0.6929857730865479):
										return True
							else:
								if(y_velocity > -0.5400729477405548):
									if(lander_y > 1.1291956901550293):
										return True
						else:
							return True
			else:
				if(lander_x <= 0.08611369132995605):
					if(angle_velocity <= -0.06118399649858475):
						if(y_velocity <= -0.471153199672699):
							if(x_velocity <= -0.45727430284023285):
								if(y_velocity <= -0.4953022450208664):
									if(angle <= -0.3465820550918579):
										if(y_velocity <= -0.5506829917430878):
											return True
										else:
											if(lander_y <= 1.1288045644760132):
												if(angle > -0.37658238410949707):
													if(lander_y > 0.9626513123512268):
														return True
									else:
										if(angle_velocity <= -0.24690931290388107):
											if(lander_x <= -0.19378521293401718):
												return True
										else:
											return True
							else:
								return True
						else:
							if(lander_y <= 1.337690532207489):
								if(lander_y <= 0.0026220297440886497):
									if(lander_y > 0.00022762175649404526):
										return True
								else:
									if(angle_velocity <= -0.0741475485265255):
										if(lander_y <= 1.3131136894226074):
											if(lander_y > 0.020061002112925053):
												if(lander_x <= -0.26607297360897064):
													if(angle > -0.04963227920234203):
														return True
										else:
											if(lander_x <= -0.06945323944091797):
												return True
									else:
										if(angle_velocity <= -0.07155049592256546):
											if(lander_y <= 0.19064445793628693):
												if(angle_velocity > -0.07257240638136864):
													return True
											else:
												return True
										else:
											if(lander_y <= 0.04048412851989269):
												if(angle > -0.029536149464547634):
													return True
											else:
												if(lander_x > -0.2675226926803589):
													if(y_velocity <= -0.22875476628541946):
														if(lander_y <= 0.28995607048273087):
															return True
														else:
															if(x_velocity <= 0.055796544067561626):
																if(angle_velocity <= -0.06678783893585205):
																	if(lander_y <= 0.5890035629272461):
																		if(x_velocity > -0.09857357665896416):
																			return True
															else:
																return True
					else:
						if(y_velocity <= -0.21787553280591965):
							if(lander_y <= 0.16229546815156937):
								if(lander_x <= 0.017193173989653587):
									return True
							else:
								if(y_velocity <= -0.2387385368347168):
									if(lander_y <= 0.3841242343187332):
										if(y_velocity > -0.26827841997146606):
											return True
									else:
										if(lander_y <= 1.06383216381073):
											if(angle <= 0.002238634799141437):
												if(x_velocity <= -0.0601305216550827):
													if(y_velocity <= -0.2705176919698715):
														if(lander_y <= 1.0086975693702698):
															if(angle_velocity <= -0.040436457842588425):
																if(lander_x > -0.24930714070796967):
																	if(y_velocity <= -0.3079618811607361):
																		return True
																	else:
																		if(lander_y <= 0.689493864774704):
																			return True
												else:
													if(y_velocity <= -0.27133090794086456):
														if(lander_y <= 0.6653814017772675):
															if(lander_y > 0.550684005022049):
																return True
											else:
												if(lander_y <= 0.8134848177433014):
													if(lander_x <= -0.01664447784423828):
														if(angle <= 0.03958132490515709):
															return True
														else:
															if(angle > 0.048138877376914024):
																return True
										else:
											if(y_velocity <= -0.2716999799013138):
												if(lander_y <= 1.4152650833129883):
													if(angle_velocity <= -0.04379095137119293):
														if(angle_velocity <= -0.054561953991651535):
															if(y_velocity <= -0.4885164946317673):
																return True
														else:
															return True
													else:
														if(y_velocity <= -0.46020735800266266):
															return True
														else:
															if(lander_y <= 1.2770281434059143):
																if(angle_velocity > -0.03769991733133793):
																	return True
								else:
									if(lander_x <= -0.17753000557422638):
										if(lander_x <= -0.20264949649572372):
											if(x_velocity > -0.005664132535457611):
												if(y_velocity <= -0.2187153846025467):
													if(angle_velocity <= -0.058140555396676064):
														return True
												else:
													return True
										else:
											if(y_velocity <= -0.2191307619214058):
												return True
									else:
										if(x_velocity <= -0.022700208239257336):
											if(angle_velocity <= -0.041635483503341675):
												return True
						else:
							if(x_velocity > -0.005532991839572787):
								if(angle <= 0.037747710943222046):
									if(x_velocity <= 0.03981081768870354):
										if(lander_x <= -0.18413691222667694):
											if(y_velocity <= -0.20890448242425919):
												return True
										else:
											if(lander_y <= 0.036178966984152794):
												return True
								else:
									if(angle <= 0.046605899930000305):
										return True
				else:
					if(y_velocity <= -0.28930096328258514):
						if(x_velocity <= -0.09774887561798096):
							if(y_velocity <= -0.3197402209043503):
								if(y_velocity <= -0.3251473754644394):
									return True
								else:
									if(y_velocity > -0.3240727335214615):
										return True
							else:
								if(y_velocity <= -0.30194254219532013):
									if(lander_y <= 0.8830546736717224):
										return True
									else:
										if(x_velocity > -0.14677271991968155):
											if(lander_y <= 0.9878422915935516):
												return True
						else:
							return True
					else:
						if(lander_y <= 1.0637657046318054):
							if(angle_velocity > -0.3381737321615219):
								if(angle > 0.0773346540518105):
									if(y_velocity <= -0.27242928743362427):
										return True
		else:
			if(y_velocity <= -0.21407920122146606):
				if(lander_y <= 0.3921949416399002):
					if(angle <= -0.04154000245034695):
						if(angle_velocity <= -0.0036754703614860773):
							if(lander_x > -0.060271358117461205):
								if(y_velocity <= -0.264682412147522):
									return True
						else:
							if(angle_velocity <= 0.036015814170241356):
								if(y_velocity <= -0.2208710014820099):
									if(angle_velocity <= 0.013978915754705667):
										if(angle_velocity <= 0.012660620268434286):
											if(angle_velocity <= 0.00855690473690629):
												return True
											else:
												if(x_velocity > -0.08197527378797531):
													return True
									else:
										return True
							else:
								if(angle_velocity > 0.041479285806417465):
									if(lander_y > 0.2313317060470581):
										return True
					else:
						if(lander_y <= 0.3257696032524109):
							if(angle_velocity <= 0.060555048286914825):
								if(angle_velocity <= -0.03097302559763193):
									if(angle > -0.00851858058013022):
										return True
								else:
									if(x_velocity <= 0.07102743536233902):
										if(angle <= -0.032545069232583046):
											if(lander_x <= -0.08671960979700089):
												return True
										else:
											if(y_velocity <= -0.2173435166478157):
												return True
											else:
												if(y_velocity > -0.21717221289873123):
													return True
									else:
										if(x_velocity > 0.07179636508226395):
											if(lander_y <= 0.2872631996870041):
												return True
											else:
												if(x_velocity > 0.09572063013911247):
													return True
							else:
								if(x_velocity <= 0.042198874056339264):
									return True
						else:
							if(y_velocity <= -0.22192434966564178):
								if(angle <= -0.02769833616912365):
									if(y_velocity <= -0.24259628355503082):
										return True
								else:
									if(lander_x <= 0.016397570725530386):
										if(angle <= -0.019261649809777737):
											if(x_velocity > 0.01757714617997408):
												return True
										else:
											return True
									else:
										if(x_velocity <= -0.004945871303789318):
											return True
							else:
								if(angle > 0.004637096542865038):
									return True
				else:
					if(y_velocity <= -0.25619785487651825):
						if(lander_y <= 0.756659984588623):
							if(angle_velocity <= 0.053107040002942085):
								if(lander_x > -0.3122215270996094):
									if(angle_velocity <= -0.02403460629284382):
										if(lander_x <= 0.049027539789676666):
											if(x_velocity <= 0.013191134203225374):
												if(angle_velocity <= -0.024255387485027313):
													return True
											else:
												if(lander_y > 0.7294978499412537):
													return True
									else:
										if(lander_y <= 0.7253215312957764):
											if(lander_x <= 0.04834899865090847):
												if(lander_y <= 0.6934561133384705):
													if(x_velocity <= 0.027755615301430225):
														return True
													else:
														if(x_velocity > 0.03154201339930296):
															return True
												else:
													if(lander_y > 0.6977581083774567):
														return True
											else:
												if(y_velocity <= -0.2674541026353836):
													return True
												else:
													if(x_velocity <= -0.047152647748589516):
														return True
										else:
											if(y_velocity <= -0.27764803171157837):
												return True
											else:
												if(angle <= 0.0003093401901423931):
													if(lander_y > 0.736640989780426):
														if(lander_y <= 0.7442370653152466):
															return True
												else:
													return True
							else:
								if(y_velocity <= -0.2809235751628876):
									if(lander_x <= -0.3022411912679672):
										if(lander_x <= -0.3024405688047409):
											if(lander_x <= -0.3025939017534256):
												if(angle_velocity <= 0.07512351870536804):
													if(angle_velocity <= 0.06418810971081257):
														return True
												else:
													if(y_velocity <= -0.29105426371097565):
														if(x_velocity <= -0.08011345565319061):
															if(y_velocity <= -0.3396390825510025):
																return True
														else:
															return True
													else:
														if(y_velocity > -0.2880503237247467):
															return True
											else:
												if(y_velocity > -0.3078501671552658):
													return True
									else:
										return True
								else:
									if(lander_y <= 0.6383659839630127):
										if(lander_x <= -0.3118230104446411):
											if(y_velocity <= -0.26830536127090454):
												return True
										else:
											return True
									else:
										if(lander_y > 0.7437300682067871):
											return True
						else:
							if(y_velocity <= -0.28801071643829346):
								if(x_velocity > -0.6012959033250809):
									if(angle <= -0.08344867825508118):
										if(y_velocity <= -0.3144092857837677):
											if(angle_velocity <= 0.07320805639028549):
												if(y_velocity <= -0.477528378367424):
													if(lander_x > -0.2730148583650589):
														if(angle > -0.40019458532333374):
															return True
												else:
													if(angle <= -0.1618097871541977):
														if(lander_y > 1.035351276397705):
															if(angle_velocity <= 0.042507411912083626):
																if(x_velocity <= -0.4070647954940796):
																	return True
																else:
																	if(lander_y <= 1.1711307764053345):
																		if(angle <= -0.23966187983751297):
																			return True
															else:
																if(y_velocity <= -0.4351184517145157):
																	if(lander_x > -0.22564711421728134):
																		return True
																else:
																	if(angle_velocity <= 0.0557756032794714):
																		if(angle_velocity > 0.05136653780937195):
																			return True
													else:
														if(y_velocity <= -0.3831930011510849):
															return True
														else:
															if(lander_y <= 1.2878214716911316):
																if(angle_velocity > 0.05483861267566681):
																	if(angle_velocity <= 0.0682828240096569):
																		return True
																	else:
																		if(angle > -0.10975176095962524):
																			return True
											else:
												if(y_velocity <= -0.4177473336458206):
													if(angle <= -0.3375735878944397):
														if(angle <= -0.3402484655380249):
															if(angle <= -0.37468601763248444):
																if(y_velocity <= -0.5115708261728287):
																	return True
															else:
																return True
													else:
														return True
												else:
													if(angle > -0.29154936969280243):
														if(angle <= -0.18757214397192):
															if(angle_velocity <= 0.11136408150196075):
																if(angle_velocity <= 0.08498131856322289):
																	return True
																else:
																	if(y_velocity <= -0.3588618338108063):
																		if(y_velocity <= -0.3929747939109802):
																			if(lander_y <= 1.1615955829620361):
																				return True
															else:
																if(angle_velocity <= 0.1375076174736023):
																	if(x_velocity <= -0.15036680549383163):
																		if(angle > -0.23042155802249908):
																			return True
																else:
																	if(lander_y > 0.7631669342517853):
																		if(x_velocity <= -0.11636003851890564):
																			return True
																		else:
																			if(angle_velocity > 0.21785646677017212):
																				return True
														else:
															if(y_velocity <= -0.3378104418516159):
																return True
															else:
																if(x_velocity > -0.06753591820597649):
																	if(angle <= -0.1466396152973175):
																		if(x_velocity > -0.04957428388297558):
																			return True
																	else:
																		if(angle_velocity <= 0.10377313569188118):
																			if(angle_velocity <= 0.10169947519898415):
																				return True
																		else:
																			return True
										else:
											if(x_velocity > -0.04757325537502766):
												if(lander_x <= -0.23177415877580643):
													if(angle_velocity <= 0.12944075465202332):
														return True
									else:
										if(x_velocity <= 0.4006662517786026):
											if(lander_y <= 1.4005308151245117):
												if(angle <= -0.056163057684898376):
													if(angle <= -0.057672999799251556):
														if(angle_velocity > -0.006322822999209166):
															if(x_velocity <= 0.0047135800996329635):
																return True
															else:
																if(angle_velocity > 0.09392179548740387):
																	return True
												else:
													if(angle_velocity <= -0.017868186347186565):
														if(x_velocity <= -0.006938037695363164):
															if(angle_velocity <= -0.018235708586871624):
																return True
														else:
															if(lander_x > 0.06481532752513885):
																return True
													else:
														if(angle_velocity <= 0.12197757884860039):
															if(lander_y <= 1.3639748096466064):
																return True
															else:
																if(angle_velocity > 0.025284748058766127):
																	return True
														else:
															if(angle_velocity > 0.12269959971308708):
																return True
							else:
								if(x_velocity <= 0.0004683749375544721):
									if(angle_velocity <= -0.0074590276926755905):
										if(angle > 0.006225094897672534):
											if(lander_y <= 1.0984411835670471):
												return True
									else:
										if(x_velocity > -0.01113809272646904):
											if(y_velocity <= -0.2648134231567383):
												if(x_velocity <= -0.008833963423967361):
													return True
								else:
									if(lander_y <= 1.331590175628662):
										if(lander_x <= 0.12066392600536346):
											if(angle <= 0.005490051116794348):
												if(angle_velocity <= 0.04106120765209198):
													if(angle_velocity <= -0.01197604276239872):
														if(angle <= 0.0009966541547328234):
															return True
												else:
													if(angle > -0.05581046640872955):
														if(x_velocity <= 0.06725877523422241):
															if(lander_x <= -0.12219705432653427):
																if(lander_x > -0.2725980579853058):
																	return True
											else:
												if(angle_velocity <= -0.016522443387657404):
													if(y_velocity <= -0.2783309370279312):
														return True
												else:
													if(y_velocity <= -0.25755906105041504):
														if(angle <= 0.013389595318585634):
															if(angle <= 0.011251746211200953):
																return True
														else:
															return True
													else:
														if(lander_x > 0.07076082192361355):
															return True
					else:
						if(x_velocity <= 0.07023638486862183):
							if(lander_y <= 0.6529476046562195):
								if(y_velocity <= -0.23563557863235474):
									if(angle <= -0.03550895117223263):
										if(angle_velocity > 0.019470511935651302):
											if(x_velocity > 0.036672985181212425):
												return True
									else:
										if(angle_velocity <= -0.01508759567514062):
											if(lander_x <= -0.0686207739636302):
												if(lander_x > -0.16119647026062012):
													return True
										else:
											if(lander_y <= 0.5687136352062225):
												if(x_velocity > -0.0600774772465229):
													if(angle_velocity <= 0.057700389996171):
														return True
													else:
														if(y_velocity > -0.23685677349567413):
															return True
											else:
												if(angle <= -0.0014976148377172649):
													if(y_velocity <= -0.24673493951559067):
														if(lander_y <= 0.636212557554245):
															return True
												else:
													return True
								else:
									if(angle_velocity <= -0.005014266120269895):
										if(angle > 0.03147323336452246):
											return True
									else:
										if(x_velocity <= 0.06135108321905136):
											if(lander_y > 0.3956930786371231):
												if(lander_y <= 0.6477735638618469):
													if(x_velocity <= 0.05222979746758938):
														if(lander_y <= 0.43056365847587585):
															if(y_velocity <= -0.23276302218437195):
																return True
														else:
															if(angle > 0.00560384220443666):
																if(angle <= 0.00898532778955996):
																	return True
										else:
											return True
							else:
								if(y_velocity > -0.25602202117443085):
									if(angle_velocity <= 0.008530027233064175):
										if(angle > -0.014491644687950611):
											if(lander_x > -0.017577027902007103):
												if(angle <= 0.015776697546243668):
													if(x_velocity <= -0.00970389656140469):
														if(angle_velocity <= -0.025836301036179066):
															return True
												else:
													if(lander_y <= 0.7837152481079102):
														if(lander_x > -0.015791273675858974):
															return True
									else:
										if(lander_y <= 0.7200841009616852):
											if(lander_y <= 0.7013551890850067):
												if(angle_velocity > 0.04412267729640007):
													if(lander_y > 0.6666223108768463):
														return True
											else:
												return True
						else:
							if(lander_y <= 0.7661446332931519):
								if(angle_velocity <= 0.10483866930007935):
									if(angle_velocity > -0.029461241327226162):
										if(y_velocity <= -0.21726177632808685):
											if(angle <= 0.012266078498214483):
												if(angle_velocity <= 0.054696567356586456):
													if(x_velocity <= 0.08238735049962997):
														if(x_velocity <= 0.07704402506351471):
															return True
												else:
													return True
											else:
												if(x_velocity <= 0.14151576161384583):
													return True
												else:
													if(x_velocity > 0.14326975494623184):
														return True
										else:
											if(lander_y > 0.5303158313035965):
												return True
							else:
								if(y_velocity <= -0.23934240639209747):
									if(angle <= 0.30774688720703125):
										if(angle > 0.019939959049224854):
											if(angle_velocity > 0.0170087325386703):
												return True
								else:
									if(angle_velocity <= 0.07050533220171928):
										if(y_velocity <= -0.2216755598783493):
											if(angle_velocity > 0.06220582313835621):
												return True
			else:
				if(x_velocity <= 0.05567553639411926):
					if(lander_y <= 0.15316959470510483):
						if(y_velocity <= -0.20384977012872696):
							if(angle > -0.02807968109846115):
								if(y_velocity <= -0.20461011677980423):
									if(angle <= -0.024680593982338905):
										if(angle <= -0.025135292671620846):
											return True
									else:
										return True
								else:
									if(lander_x <= -0.12728147208690643):
										return True
						else:
							if(y_velocity <= -0.19585410505533218):
								if(lander_x <= -0.11146488040685654):
									if(angle_velocity <= 0.03379661589860916):
										return True
								else:
									if(y_velocity > -0.19701533764600754):
										return True
					else:
						if(angle_velocity > -0.02037798799574375):
							if(y_velocity <= -0.20896346867084503):
								if(lander_x <= -0.007932853419333696):
									if(y_velocity > -0.20905029773712158):
										return True
								else:
									if(lander_y <= 0.2702901065349579):
										return True
							else:
								if(x_velocity > 0.03942222706973553):
									if(lander_y <= 0.18184484541416168):
										return True
									else:
										if(angle > -0.004419736564159393):
											if(angle_velocity <= -0.006318030529655516):
												if(angle_velocity > -0.013952825218439102):
													if(x_velocity > 0.04744401201605797):
														return True
				else:
					if(lander_y <= 0.3776385486125946):
						if(angle_velocity <= -0.005083222407847643):
							if(angle <= 0.042888093739748):
								if(y_velocity <= -0.20252463966608047):
									if(angle > 0.0035445267567411065):
										if(x_velocity <= 0.07558076456189156):
											return True
							else:
								if(x_velocity <= 0.11827506497502327):
									if(angle_velocity <= -0.019246652722358704):
										return True
									else:
										if(lander_y <= 0.028286334592849016):
											return True
						else:
							if(angle <= 0.005951379658654332):
								if(y_velocity <= -0.2052592635154724):
									return True
								else:
									if(angle_velocity <= 0.020243342965841293):
										if(lander_y <= 0.08994452841579914):
											return True
							else:
								if(angle <= 0.012189941480755806):
									if(y_velocity <= -0.19001075625419617):
										if(angle_velocity <= 0.051504479721188545):
											return True
								else:
									if(x_velocity <= 0.11312342807650566):
										return True
									else:
										if(lander_x <= -0.16688861697912216):
											return True
					else:
						if(x_velocity <= 0.13456472754478455):
							if(y_velocity <= -0.20617227256298065):
								if(angle_velocity <= 0.025103840045630932):
									if(lander_x <= -0.20976068824529648):
										return True
								else:
									if(y_velocity <= -0.21295955777168274):
										return True
						else:
							if(angle > 0.031415401957929134):
								if(y_velocity <= -0.18768766522407532):
									if(angle_velocity <= 0.005937085719779134):
										if(x_velocity <= 0.14010006934404373):
											return True
									else:
										return True
	else:
		if(y_velocity <= -5.539971425605472e-06):
			if(lander_y > -0.04273167438805103):
				if(y_velocity <= -0.13607718795537949):
					if(angle > 0.0022962415823712945):
						if(lander_y <= 0.0935308188199997):
							if(y_velocity > -0.17297670990228653):
								if(angle <= 0.010550695471465588):
									if(right_leg_contact != True):
										if(angle <= 0.004727513180114329):
											return True
								else:
									if(angle_velocity > -0.019128063693642616):
										if(lander_x <= -0.15040688961744308):
											if(angle_velocity > 0.21426767483353615):
												return True
	return False

def weShould_right_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.1794271618127823):
		if(angle_velocity <= -0.03374768979847431):
			if(x_velocity <= -0.5751650929450989):
				if(lander_y <= 1.3026283979415894):
					if(x_velocity <= -0.7040518224239349):
						return True
					else:
						if(x_velocity <= -0.6311948895454407):
							if(y_velocity <= -0.5590022504329681):
								if(angle_velocity > -0.23465460538864136):
									if(x_velocity > -0.6929857730865479):
										return True
							else:
								if(y_velocity <= -0.5400729477405548):
									return True
								else:
									if(lander_y <= 1.1291956901550293):
										return True
				else:
					return True
			else:
				if(lander_x <= 0.08611369132995605):
					if(angle_velocity <= -0.06118399649858475):
						if(y_velocity > -0.471153199672699):
							if(lander_y <= 1.337690532207489):
								if(lander_y > 0.0026220297440886497):
									if(angle_velocity > -0.0741475485265255):
										if(angle_velocity > -0.07155049592256546):
											if(lander_y > 0.04048412851989269):
												if(lander_x > -0.2675226926803589):
													if(y_velocity <= -0.22875476628541946):
														if(lander_y > 0.28995607048273087):
															if(x_velocity <= 0.055796544067561626):
																if(angle_velocity <= -0.06678783893585205):
																	if(lander_y <= 0.5890035629272461):
																		if(x_velocity <= -0.09857357665896416):
																			if(x_velocity <= -0.12064360454678535):
																				return True
							else:
								if(lander_x <= -0.044382667168974876):
									if(x_velocity <= -0.495346337556839):
										return True
									else:
										if(lander_y <= 1.3572929501533508):
											if(x_velocity <= -0.3490128368139267):
												return True
										else:
											if(lander_y > 1.405482828617096):
												if(lander_x <= -0.11175217851996422):
													if(angle <= -0.2549261003732681):
														if(y_velocity <= -0.39258597791194916):
															return True
													else:
														return True
												else:
													if(y_velocity > -0.26613157987594604):
														if(angle_velocity > -0.24807125329971313):
															if(y_velocity <= -0.24698907881975174):
																return True
															else:
																if(y_velocity > -0.21964573115110397):
																	if(angle_velocity > -0.13918894156813622):
																		if(x_velocity <= -0.22581874579191208):
																			return True
								else:
									return True
					else:
						if(y_velocity <= -0.21787553280591965):
							if(lander_y > 0.16229546815156937):
								if(y_velocity <= -0.2387385368347168):
									if(lander_y > 0.3841242343187332):
										if(lander_y <= 1.06383216381073):
											if(angle <= 0.002238634799141437):
												if(x_velocity <= -0.0601305216550827):
													if(y_velocity > -0.2705176919698715):
														return True
										else:
											if(y_velocity <= -0.2716999799013138):
												if(lander_y <= 1.4152650833129883):
													if(angle_velocity <= -0.04379095137119293):
														if(angle_velocity <= -0.054561953991651535):
															if(y_velocity > -0.4885164946317673):
																if(lander_y > 1.3260449767112732):
																	return True
													else:
														if(y_velocity > -0.46020735800266266):
															if(lander_y <= 1.2770281434059143):
																if(angle_velocity <= -0.03769991733133793):
																	if(y_velocity > -0.3716417998075485):
																		return True
												else:
													return True
											else:
												return True
								else:
									if(lander_x <= -0.17753000557422638):
										if(lander_x <= -0.20264949649572372):
											if(x_velocity <= -0.005664132535457611):
												return True
						else:
							if(x_velocity <= -0.005532991839572787):
								if(y_velocity > -0.214475579559803):
									if(lander_y > 0.04115825518965721):
										if(lander_x <= 0.020705843344330788):
											return True
							else:
								if(angle <= 0.037747710943222046):
									if(x_velocity <= 0.03981081768870354):
										if(lander_x <= -0.18413691222667694):
											if(y_velocity > -0.20890448242425919):
												return True
				else:
					if(y_velocity <= -0.28930096328258514):
						if(x_velocity <= -0.09774887561798096):
							if(y_velocity > -0.3197402209043503):
								if(y_velocity > -0.30194254219532013):
									return True
					else:
						if(lander_y <= 1.0637657046318054):
							if(angle_velocity > -0.3381737321615219):
								if(angle > 0.0773346540518105):
									if(y_velocity > -0.27242928743362427):
										return True
						else:
							return True
		else:
			if(y_velocity <= -0.21407920122146606):
				if(lander_y <= 0.3921949416399002):
					if(angle <= -0.04154000245034695):
						if(angle_velocity <= -0.0036754703614860773):
							if(lander_x > -0.060271358117461205):
								if(y_velocity > -0.264682412147522):
									return True
						else:
							if(angle_velocity <= 0.036015814170241356):
								if(y_velocity <= -0.2208710014820099):
									if(angle_velocity <= 0.013978915754705667):
										if(angle_velocity <= 0.012660620268434286):
											if(angle_velocity > 0.00855690473690629):
												if(x_velocity <= -0.08197527378797531):
													return True
								else:
									return True
							else:
								if(angle_velocity <= 0.041479285806417465):
									return True
								else:
									if(lander_y <= 0.2313317060470581):
										return True
					else:
						if(lander_y <= 0.3257696032524109):
							if(angle_velocity <= 0.060555048286914825):
								if(angle_velocity > -0.03097302559763193):
									if(x_velocity <= 0.07102743536233902):
										if(angle > -0.032545069232583046):
											if(y_velocity > -0.2173435166478157):
												if(y_velocity <= -0.21717221289873123):
													return True
							else:
								if(x_velocity > 0.042198874056339264):
									return True
						else:
							if(y_velocity > -0.22192434966564178):
								if(angle <= 0.004637096542865038):
									if(angle_velocity <= 0.021830779500305653):
										if(lander_x <= -0.24376244097948074):
											if(y_velocity > -0.21736398339271545):
												return True
									else:
										return True
				else:
					if(y_velocity <= -0.25619785487651825):
						if(lander_y <= 0.756659984588623):
							if(angle_velocity > 0.053107040002942085):
								if(y_velocity <= -0.2809235751628876):
									if(lander_x <= -0.3022411912679672):
										if(lander_x <= -0.3024405688047409):
											if(lander_x <= -0.3025939017534256):
												if(angle_velocity > 0.07512351870536804):
													if(y_velocity <= -0.29105426371097565):
														if(x_velocity <= -0.08011345565319061):
															if(y_velocity > -0.3396390825510025):
																return True
													else:
														if(y_velocity <= -0.2880503237247467):
															return True
										else:
											return True
								else:
									if(lander_y <= 0.6383659839630127):
										if(lander_x <= -0.3118230104446411):
											if(y_velocity > -0.26830536127090454):
												return True
									else:
										if(lander_y <= 0.7437300682067871):
											if(angle > -0.13229959458112717):
												return True
						else:
							if(y_velocity <= -0.28801071643829346):
								if(x_velocity <= -0.6012959033250809):
									return True
								else:
									if(angle <= -0.08344867825508118):
										if(y_velocity <= -0.3144092857837677):
											if(angle_velocity <= 0.07320805639028549):
												if(y_velocity > -0.477528378367424):
													if(angle <= -0.1618097871541977):
														if(lander_y > 1.035351276397705):
															if(angle_velocity > 0.042507411912083626):
																if(y_velocity > -0.4351184517145157):
																	if(angle_velocity <= 0.0557756032794714):
																		if(angle_velocity <= 0.05136653780937195):
																			return True
													else:
														if(y_velocity > -0.3831930011510849):
															if(lander_y > 1.2878214716911316):
																return True
											else:
												if(y_velocity > -0.4177473336458206):
													if(angle > -0.29154936969280243):
														if(angle <= -0.18757214397192):
															if(angle_velocity <= 0.11136408150196075):
																if(angle_velocity > 0.08498131856322289):
																	if(y_velocity > -0.3588618338108063):
																		return True
															else:
																if(angle_velocity <= 0.1375076174736023):
																	if(x_velocity <= -0.15036680549383163):
																		if(angle <= -0.23042155802249908):
																			return True
																	else:
																		return True
														else:
															if(y_velocity > -0.3378104418516159):
																if(x_velocity <= -0.06753591820597649):
																	if(angle > -0.16573705524206161):
																		return True
																else:
																	if(angle > -0.1466396152973175):
																		if(angle_velocity <= 0.10377313569188118):
																			if(angle_velocity > 0.10169947519898415):
																				return True
										else:
											if(x_velocity <= -0.04757325537502766):
												return True
											else:
												if(lander_x <= -0.23177415877580643):
													if(angle_velocity > 0.12944075465202332):
														if(angle > -0.1436707004904747):
															return True
									else:
										if(x_velocity <= 0.4006662517786026):
											if(lander_y <= 1.4005308151245117):
												if(angle > -0.056163057684898376):
													if(angle_velocity > -0.017868186347186565):
														if(angle_velocity > 0.12197757884860039):
															if(angle_velocity <= 0.12269959971308708):
																return True
							else:
								if(x_velocity <= 0.0004683749375544721):
									if(angle_velocity <= -0.0074590276926755905):
										if(angle <= 0.006225094897672534):
											if(x_velocity <= -0.06540152803063393):
												return True
										else:
											if(lander_y > 1.0984411835670471):
												if(angle_velocity <= -0.00896394718438387):
													return True
									else:
										if(x_velocity <= -0.01113809272646904):
											if(y_velocity <= -0.2866400480270386):
												if(lander_x > -0.098794125020504):
													return True
											else:
												return True
										else:
											if(y_velocity > -0.2648134231567383):
												return True
								else:
									if(lander_y <= 1.331590175628662):
										if(lander_x <= 0.12066392600536346):
											if(angle <= 0.005490051116794348):
												if(angle_velocity > 0.04106120765209198):
													if(angle <= -0.05581046640872955):
														if(y_velocity <= -0.27606625854969025):
															return True
													else:
														if(x_velocity <= 0.06725877523422241):
															if(lander_x <= -0.12219705432653427):
																if(lander_x <= -0.2725980579853058):
																	return True
															else:
																if(x_velocity <= 0.04005394130945206):
																	return True
											else:
												if(angle_velocity > -0.016522443387657404):
													if(y_velocity > -0.25755906105041504):
														if(lander_x <= 0.07076082192361355):
															return True
										else:
											return True
									else:
										if(x_velocity <= 0.05715778097510338):
											return True
										else:
											if(lander_y > 1.3929938077926636):
												return True
					else:
						if(x_velocity <= 0.07023638486862183):
							if(lander_y <= 0.6529476046562195):
								if(y_velocity <= -0.23563557863235474):
									if(angle <= -0.03550895117223263):
										if(angle_velocity <= 0.019470511935651302):
											if(y_velocity <= -0.25209230184555054):
												return True
										else:
											if(x_velocity <= 0.036672985181212425):
												return True
									else:
										if(angle_velocity <= -0.01508759567514062):
											if(lander_x <= -0.0686207739636302):
												if(lander_x <= -0.16119647026062012):
													if(y_velocity > -0.2506799176335335):
														return True
										else:
											if(lander_y <= 0.5687136352062225):
												if(x_velocity <= -0.0600774772465229):
													return True
												else:
													if(angle_velocity > 0.057700389996171):
														if(y_velocity <= -0.23685677349567413):
															return True
											else:
												if(angle <= -0.0014976148377172649):
													if(y_velocity <= -0.24673493951559067):
														if(lander_y > 0.636212557554245):
															return True
													else:
														return True
								else:
									if(angle_velocity <= -0.005014266120269895):
										if(angle <= 0.03147323336452246):
											if(lander_x <= -0.015294408425688744):
												if(angle > -0.023666472174227238):
													if(angle_velocity > -0.02928320039063692):
														return True
									else:
										if(x_velocity <= 0.06135108321905136):
											if(lander_y > 0.3956930786371231):
												if(lander_y <= 0.6477735638618469):
													if(x_velocity <= 0.05222979746758938):
														if(lander_y <= 0.43056365847587585):
															if(y_velocity > -0.23276302218437195):
																if(angle_velocity <= 0.0032132955093402416):
																	if(x_velocity <= 0.00970655819401145):
																		return True
																else:
																	return True
														else:
															if(angle <= 0.00560384220443666):
																return True
															else:
																if(angle > 0.00898532778955996):
																	return True
													else:
														if(y_velocity > -0.22384222596883774):
															return True
							else:
								if(y_velocity > -0.25602202117443085):
									if(angle_velocity <= 0.008530027233064175):
										if(angle > -0.014491644687950611):
											if(lander_x <= -0.017577027902007103):
												if(lander_y <= 0.9551971554756165):
													return True
												else:
													if(y_velocity > -0.2336241751909256):
														return True
											else:
												if(angle <= 0.015776697546243668):
													if(x_velocity <= -0.00970389656140469):
														if(angle_velocity > -0.025836301036179066):
															return True
												else:
													if(lander_y <= 0.7837152481079102):
														if(lander_x <= -0.015791273675858974):
															return True
													else:
														return True
									else:
										if(lander_y <= 0.7200841009616852):
											if(lander_y <= 0.7013551890850067):
												if(angle_velocity <= 0.04412267729640007):
													return True
												else:
													if(lander_y <= 0.6666223108768463):
														return True
										else:
											return True
						else:
							if(lander_y <= 0.7661446332931519):
								if(angle_velocity <= 0.10483866930007935):
									if(angle_velocity > -0.029461241327226162):
										if(y_velocity <= -0.21726177632808685):
											if(angle <= 0.012266078498214483):
												if(angle_velocity <= 0.054696567356586456):
													if(x_velocity <= 0.08238735049962997):
														if(x_velocity > 0.07704402506351471):
															return True
								else:
									return True
							else:
								if(y_velocity <= -0.23934240639209747):
									if(angle > 0.30774688720703125):
										return True
								else:
									if(angle_velocity <= 0.07050533220171928):
										if(y_velocity > -0.2216755598783493):
											return True
									else:
										if(lander_y <= 1.3443123698234558):
											return True
			else:
				if(x_velocity <= 0.05567553639411926):
					if(lander_y <= 0.15316959470510483):
						if(y_velocity <= -0.20384977012872696):
							if(angle <= -0.02807968109846115):
								if(lander_x > -0.1437944397330284):
									return True
							else:
								if(y_velocity > -0.20461011677980423):
									if(lander_x > -0.12728147208690643):
										if(angle_velocity > 0.0047361282631754875):
											return True
						else:
							if(y_velocity <= -0.19585410505533218):
								if(lander_x <= -0.11146488040685654):
									if(angle_velocity > 0.03379661589860916):
										return True
								else:
									if(y_velocity <= -0.19701533764600754):
										return True
							else:
								if(lander_x <= -0.0862305611371994):
									if(x_velocity <= 0.05218663439154625):
										if(angle <= -0.02899283729493618):
											if(lander_x > -0.13113193586468697):
												return True
										else:
											return True
									else:
										if(lander_x > -0.1685732826590538):
											return True
								else:
									if(lander_x > 0.02997350785881281):
										return True
					else:
						if(angle_velocity <= -0.02037798799574375):
							if(x_velocity <= 0.0009630420245230198):
								return True
							else:
								if(lander_x <= -0.14824142307043076):
									if(lander_x > -0.18080510944128036):
										return True
						else:
							if(y_velocity <= -0.20896346867084503):
								if(lander_x <= -0.007932853419333696):
									if(y_velocity <= -0.20905029773712158):
										if(x_velocity > -0.028763396199792624):
											if(y_velocity <= -0.21027535945177078):
												return True
											else:
												if(angle > 0.0017396897310391068):
													return True
							else:
								if(x_velocity <= 0.03942222706973553):
									if(lander_x <= 0.037769366055727005):
										return True
									else:
										if(x_velocity <= -0.004351045587100089):
											return True
										else:
											if(lander_y <= 0.21746324747800827):
												return True
								else:
									if(lander_y > 0.18184484541416168):
										if(angle <= -0.004419736564159393):
											if(lander_x <= -0.18882811069488525):
												return True
										else:
											if(angle_velocity <= -0.006318030529655516):
												if(angle_velocity <= -0.013952825218439102):
													return True
											else:
												return True
				else:
					if(lander_y <= 0.3776385486125946):
						if(angle_velocity <= -0.005083222407847643):
							if(angle > 0.042888093739748):
								if(x_velocity <= 0.11827506497502327):
									if(angle_velocity > -0.019246652722358704):
										if(lander_y > 0.028286334592849016):
											return True
						else:
							if(angle <= 0.005951379658654332):
								if(y_velocity > -0.2052592635154724):
									if(angle_velocity > 0.020243342965841293):
										return True
							else:
								if(angle <= 0.012189941480755806):
									if(y_velocity <= -0.19001075625419617):
										if(angle_velocity > 0.051504479721188545):
											return True
									else:
										return True
					else:
						if(x_velocity <= 0.13456472754478455):
							if(y_velocity <= -0.20617227256298065):
								if(angle_velocity <= 0.025103840045630932):
									if(lander_x > -0.20976068824529648):
										if(angle_velocity > -0.012998236808925867):
											return True
								else:
									if(y_velocity > -0.21295955777168274):
										return True
							else:
								if(lander_x <= -0.034827230498194695):
									if(lander_y <= 0.4492153078317642):
										if(lander_y <= 0.4398427754640579):
											if(angle_velocity <= -0.011567938141524792):
												if(lander_y > 0.41154973208904266):
													return True
											else:
												return True
									else:
										return True
						else:
							if(angle > 0.031415401957929134):
								if(y_velocity > -0.18768766522407532):
									if(angle_velocity > 0.033176626078784466):
										return True
	else:
		if(y_velocity <= -5.539971425605472e-06):
			if(lander_y <= -0.04273167438805103):
				if(x_velocity <= -0.0013848317903466523):
					if(angle <= 0.29617390036582947):
						if(angle_velocity > 0.000927366258110851):
							return True
					else:
						return True
				else:
					if(lander_x <= -0.23545122146606445):
						return True
			else:
				if(y_velocity <= -0.13607718795537949):
					if(angle <= 0.0022962415823712945):
						if(lander_y > 0.00013242126442492008):
							if(angle > -0.06730449758470058):
								if(x_velocity <= 0.03798787482082844):
									return True
								else:
									if(lander_x <= -0.22996079921722412):
										return True
					else:
						if(lander_y <= 0.0935308188199997):
							if(y_velocity <= -0.17297670990228653):
								if(angle <= 0.02057494269683957):
									return True
							else:
								if(angle <= 0.010550695471465588):
									if(right_leg_contact != True):
										if(angle > 0.004727513180114329):
											if(lander_x <= -0.12393169477581978):
												return True
								else:
									if(angle_velocity <= -0.019128063693642616):
										if(angle_velocity <= -0.022645185701549053):
											return True
									else:
										if(lander_x <= -0.15040688961744308):
											if(angle_velocity <= 0.21426767483353615):
												return True
										else:
											return True
						else:
							return True
				else:
					if(angle <= 0.16217593103647232):
						if(right_leg_contact != True):
							if(angle <= 0.0024438646505586803):
								if(x_velocity <= 0.08589649200439453):
									if(angle > -0.16033270955085754):
										if(x_velocity <= -0.4444125294685364):
											return True
										else:
											if(lander_y <= 1.423512041568756):
												if(lander_x > -0.06536378897726536):
													return True
							else:
								if(x_velocity <= 0.07595284655690193):
									return True
						else:
							if(angle_velocity > 0.3967301696538925):
								return True
					else:
						if(angle_velocity <= 0.0017847815761342645):
							if(lander_y <= -0.04265029542148113):
								if(x_velocity <= -0.0024095873814076185):
									if(angle <= 0.3002530485391617):
										return True
						else:
							if(lander_y <= -0.04234050214290619):
								if(x_velocity <= -0.0046468020882457495):
									return True
								else:
									if(lander_y <= -0.04249696433544159):
										return True
							else:
								if(angle_velocity <= 0.0032612187787890434):
									if(lander_x <= -0.2615768313407898):
										if(x_velocity <= -0.006839883280918002):
											return True
								else:
									if(lander_y <= -0.04181877709925175):
										if(x_velocity <= -0.008380806539207697):
											return True
										else:
											if(angle > 0.29680824279785156):
												return True
									else:
										if(x_velocity <= -0.012251785025000572):
											if(lander_y <= -0.04118398763239384):
												return True
											else:
												if(y_velocity <= -0.002687436994165182):
													if(lander_y <= -0.0404499564319849):
														return True
													else:
														if(angle_velocity <= 0.011433977633714676):
															if(lander_x <= -0.25365176796913147):
																if(x_velocity <= -0.022373304702341557):
																	return True
															else:
																if(angle > 0.28308115899562836):
																	if(lander_y > -0.04019818641245365):
																		return True
														else:
															if(lander_y <= -0.03899117186665535):
																return True
															else:
																if(y_velocity <= -0.005640836199745536):
																	if(angle_velocity <= 0.04400370270013809):
																		if(angle <= 0.2571589797735214):
																			if(x_velocity <= -0.05234070494771004):
																				if(angle <= 0.251819372177124):
																					if(y_velocity <= -0.007373640080913901):
																						if(lander_x <= -0.23819973319768906):
																							return True
																						else:
																							if(x_velocity <= -0.06272612698376179):
																								if(angle <= 0.24191226810216904):
																									if(x_velocity <= -0.07616688311100006):
																										if(lander_y <= -0.03136422112584114):
																											if(angle_velocity <= 0.033190540969371796):
																												if(angle > 0.2267962023615837):
																													if(angle_velocity <= 0.030724934302270412):
																														if(lander_y <= -0.033196063712239265):
																															return True
																													else:
																														return True
																											else:
																												return True
																										else:
																											if(y_velocity <= -0.012519416864961386):
																												if(lander_x <= -0.22018971294164658):
																													return True
																												else:
																													if(angle_velocity > 0.042367175221443176):
																														if(angle_velocity <= 0.04368840530514717):
																															return True
																									else:
																										if(lander_x <= -0.23429329693317413):
																											if(angle_velocity > 0.027161788195371628):
																												return True
																								else:
																									return True
																				else:
																					return True
																		else:
																			if(x_velocity <= -0.04083433002233505):
																				if(lander_y <= -0.03676494024693966):
																					return True
																				else:
																					if(lander_x > -0.21776404976844788):
																						return True
																			else:
																				if(angle > 0.2682659924030304):
																					if(lander_x <= -0.22226682305335999):
																						return True
																					else:
																						if(angle_velocity > 0.017718179151415825):
																							return True
																	else:
																		if(lander_y <= -0.027718706987798214):
																			if(lander_x <= -0.19709019362926483):
																				return True
																			else:
																				if(angle_velocity > 0.05161963030695915):
																					return True
																		else:
																			if(x_velocity <= -0.11905135959386826):
																				if(angle <= 0.1867682784795761):
																					if(x_velocity <= -0.13479279726743698):
																						if(angle <= 0.17366572469472885):
																							if(lander_y <= -0.02362812403589487):
																								if(x_velocity <= -0.151354618370533):
																									return True
																							else:
																								return True
																						else:
																							return True
																				else:
																					return True
																else:
																	if(lander_x <= -0.24843239784240723):
																		if(y_velocity <= -0.00434582494199276):
																			if(x_velocity <= -0.03575035743415356):
																				return True
																			else:
																				if(angle > 0.2678629904985428):
																					return True
												else:
													if(lander_x <= -0.25743556022644043):
														if(x_velocity <= -0.01417884137481451):
															return True
										else:
											if(angle > 0.2935708165168762):
												if(lander_x > -0.23190200328826904):
													return True
		else:
			if(x_velocity <= -0.3530505746603012):
				if(angle_velocity > -0.33629027009010315):
					return True
			else:
				if(lander_y <= -0.04316948354244232):
					if(y_velocity <= 0.00021419233235064894):
						return True
				else:
					if(y_velocity <= 0.3010060638189316):
						if(lander_y <= 1.4903365969657898):
							if(lander_y <= -0.043138207867741585):
								if(angle_velocity > -0.00026711064856499434):
									return True
							else:
								if(x_velocity <= 0.10652254521846771):
									if(x_velocity <= 0.0929892361164093):
										if(x_velocity > 0.0282497750595212):
											if(angle > 0.15381637960672379):
												return True
						else:
							return True
					else:
						return True
	return False

