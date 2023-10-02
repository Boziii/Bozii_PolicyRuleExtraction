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
	if(y_velocity <= -0.13701249659061432):
		if(y_velocity <= -0.220126174390316):
			if(angle_velocity <= -0.030239202082157135):
				if(angle <= 0.19462168961763382):
					if(lander_y <= 1.3413802981376648):
						if(y_velocity > -0.2712501585483551):
							if(lander_y <= 0.2888483852148056):
								if(angle_velocity <= -0.06200191378593445):
									if(y_velocity > -0.2447967603802681):
										if(angle <= 0.017069307155907154):
											if(lander_y <= 0.01458512875251472):
												return True
		else:
			if(angle_velocity <= -0.010854553431272507):
				if(right_leg_contact != True):
					if(angle <= 0.06201705522835255):
						if(angle_velocity <= -0.035603923723101616):
							if(x_velocity <= -0.049048325046896935):
								if(angle <= -0.018289437517523766):
									if(x_velocity <= -0.3122575879096985):
										return True
									else:
										if(x_velocity <= -0.051378997042775154):
											if(x_velocity <= -0.09737235680222511):
												if(angle_velocity <= -0.06120913475751877):
													if(x_velocity <= -0.2234330028295517):
														if(angle_velocity <= -0.1633089929819107):
															if(lander_x > -0.05506153218448162):
																if(angle_velocity > -0.21268966794013977):
																	return True
				else:
					if(x_velocity <= 0.09106511250138283):
						if(lander_y <= 0.015181741677224636):
							return True
						else:
							if(angle_velocity > -0.42805245518684387):
								return True
					else:
						if(angle_velocity > -0.5140106678009033):
							if(angle > -0.09820253774523735):
								return True
			else:
				if(lander_y <= 0.2456214353442192):
					if(y_velocity <= -0.18587703257799149):
						if(x_velocity <= 0.018928966484963894):
							if(y_velocity <= -0.20360344648361206):
								if(x_velocity > -0.02664847020059824):
									if(lander_y <= 0.18653695285320282):
										if(lander_x > -0.1305283084511757):
											if(lander_y <= 0.0018440998392179608):
												return True
							else:
								if(angle_velocity > -0.005452348385006189):
									if(lander_y <= 0.004058173857629299):
										if(y_velocity <= -0.19918935745954514):
											return True
						else:
							if(angle > 0.010951127856969833):
								if(right_leg_contact == True):
									if(x_velocity > 0.04395904578268528):
										return True
					else:
						if(x_velocity <= 0.07906698435544968):
							if(left_leg_contact == True):
								if(angle_velocity <= 0.4526590257883072):
									if(angle > -0.007183142472058535):
										if(angle <= 0.09468194097280502):
											return True
	else:
		if(y_velocity <= -0.00010637535888236016):
			if(angle <= 0.10152852162718773):
				if(lander_y <= 0.04580237716436386):
					if(angle_velocity <= 0.48136158287525177):
						if(right_leg_contact != True):
							if(angle_velocity <= 0.1452050693333149):
								if(y_velocity <= -0.00044665002496913075):
									if(lander_x <= -0.16949333995580673):
										if(lander_x > -0.1700868085026741):
											if(y_velocity > -0.0005231824179645628):
												return True
									else:
										if(x_velocity <= 0.11339053511619568):
											if(lander_x <= -0.13660965114831924):
												if(angle_velocity <= 0.023821291513741016):
													if(angle_velocity <= 0.0022404646733775735):
														return True
													else:
														if(angle <= 0.09779782965779305):
															if(angle_velocity <= 0.0031157652847468853):
																return True
															else:
																if(angle <= 0.0957130566239357):
																	if(y_velocity <= -0.0013466599630191922):
																		if(lander_x > -0.1653372272849083):
																			if(y_velocity <= -0.0017541252309456468):
																				if(angle <= 0.0891181118786335):
																					if(y_velocity <= -0.0026475487975403666):
																						if(lander_y > -0.011308970395475626):
																							if(y_velocity <= -0.0032512116013094783):
																								if(angle <= 0.07668516412377357):
																									if(x_velocity <= -0.03841491602361202):
																										if(lander_x > -0.1522982120513916):
																											if(y_velocity <= -0.004972377559170127):
																												if(lander_y > -0.008437450975179672):
																													if(lander_y <= -0.007270439760759473):
																														if(y_velocity > -0.00610409677028656):
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
																						if(lander_y <= -0.01185235008597374):
																							if(x_velocity > -0.02051302045583725):
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
					if(x_velocity <= 0.22380287945270538):
						if(angle <= 0.000588659371715039):
							if(y_velocity <= -0.09979284182190895):
								if(angle <= -0.00119297718629241):
									if(lander_y > 1.450961410999298):
										if(lander_x > -0.060761069878935814):
											return True
							else:
								if(x_velocity <= 0.04741138778626919):
									return True
								else:
									if(angle > -0.0013583254476543516):
										return True
						else:
							if(lander_x > 0.0010599136294331402):
								if(angle_velocity > 0.16573119163513184):
									if(y_velocity > -0.03173424582928419):
										return True
			else:
				if(x_velocity <= -0.005076864268630743):
					if(lander_y <= -0.040867967531085014):
						if(lander_y > -0.04322237707674503):
							if(x_velocity <= -0.006252878112718463):
								if(lander_x > -0.22876594215631485):
									if(angle_velocity <= 0.005053321830928326):
										return True
									else:
										if(lander_y > -0.04223550297319889):
											if(y_velocity > -0.003313863999210298):
												if(lander_y <= -0.04185234010219574):
													if(angle_velocity <= 0.007289826404303312):
														if(x_velocity <= -0.013963682111352682):
															return True
														else:
															if(lander_y <= -0.04213329218327999):
																return True
												else:
													return True
							else:
								if(lander_x > -0.2916949987411499):
									return True
					else:
						if(angle_velocity <= 0.032445382326841354):
							if(lander_y <= -0.030225195921957493):
								if(lander_x <= -0.24702756106853485):
									if(angle_velocity <= 0.002535531297326088):
										return True
									else:
										if(lander_y <= -0.040405914187431335):
											if(lander_x > -0.2901028096675873):
												if(angle_velocity <= 0.003162378096021712):
													if(lander_x <= -0.2899189591407776):
														return True
													else:
														if(lander_x > -0.28955352306365967):
															return True
										else:
											if(y_velocity <= -0.001300012692809105):
												if(lander_y > -0.0399930514395237):
													if(y_velocity > -0.009448048658668995):
														if(y_velocity <= -0.0020027427235618234):
															if(angle <= 0.27492058277130127):
																if(x_velocity <= -0.02388850599527359):
																	if(angle <= 0.271944522857666):
																		if(lander_y <= -0.03183153457939625):
																			if(angle_velocity <= 0.02463008649647236):
																				if(lander_y <= -0.03319629654288292):
																					if(x_velocity > -0.06756819784641266):
																						if(angle_velocity <= 0.008943982422351837):
																							return True
																						else:
																							if(lander_y > -0.03799544833600521):
																								if(x_velocity <= -0.034321149811148643):
																									if(lander_x > -0.27617640793323517):
																										if(y_velocity <= -0.004396326374262571):
																											if(lander_x > -0.2724975496530533):
																												if(y_velocity <= -0.005186355905607343):
																													if(lander_x > -0.2676380127668381):
																														if(angle_velocity <= 0.018718767911195755):
																															return True
																														else:
																															if(lander_y > -0.034252943471074104):
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
															if(lander_x <= -0.28642332553863525):
																if(x_velocity > -0.014965435490012169):
																	return True
															else:
																return True
											else:
												return True
								else:
									if(y_velocity <= -0.00414756964892149):
										if(lander_x > -0.2216823771595955):
											if(x_velocity <= -0.03225703351199627):
												if(angle <= 0.2706599235534668):
													if(angle_velocity <= 0.0208817757666111):
														return True
													else:
														if(y_velocity <= -0.01039180625230074):
															return True
														else:
															if(lander_x > -0.2161952704191208):
																if(x_velocity <= -0.046815114095807076):
																	if(x_velocity > -0.05645548179745674):
																		if(lander_x > -0.21385163813829422):
																			if(lander_x <= -0.2128172591328621):
																				if(lander_y <= -0.036792315542697906):
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
							if(angle <= 0.12490641325712204):
								return True
							else:
								if(y_velocity <= -0.016846172511577606):
									if(angle <= 0.16777461767196655):
										if(angle <= 0.16400884836912155):
											if(lander_y > -0.020555618219077587):
												if(lander_y <= -0.019934686832129955):
													return True
										else:
											return True
								else:
									if(lander_x <= -0.19663996249437332):
										if(lander_x > -0.20542516559362411):
											if(x_velocity <= -0.07825136929750443):
												if(lander_y > -0.031701572239398956):
													if(lander_y <= -0.03137205448001623):
														return True
											else:
												return True
									else:
										return True
				else:
					if(x_velocity <= -0.0014448040747083724):
						if(x_velocity <= -0.002252619480714202):
							if(lander_y <= -0.041341789066791534):
								if(lander_x > -0.23093562573194504):
									if(y_velocity <= -0.0007678197580389678):
										if(angle_velocity > 0.0023570136399939656):
											return True
									else:
										return True
							else:
								if(right_leg_contact != True):
									if(lander_y > -0.01395166153088212):
										if(angle_velocity <= 0.0009756921208463609):
											return True
								else:
									if(lander_x <= -0.2923773229122162):
										if(angle_velocity <= 0.001023857417749241):
											return True
									else:
										if(x_velocity > -0.005046358564868569):
											return True
						else:
							if(angle <= 0.10238726437091827):
								return True
							else:
								if(x_velocity <= -0.0015063146129250526):
									if(angle_velocity <= 0.0009597683092579246):
										if(x_velocity > -0.0015524578629992902):
											if(x_velocity <= -0.0015518521540798247):
												return True
									else:
										return True
								else:
									if(angle_velocity <= 0.000487971497932449):
										if(angle <= 0.10283709317445755):
											return True
									else:
										if(lander_x > -0.2934667617082596):
											return True
					else:
						if(angle_velocity <= 0.18233278393745422):
							if(angle <= 0.2907939851284027):
								if(lander_y <= -0.02451244741678238):
									return True
								else:
									if(lander_x > -0.17154951393604279):
										return True
							else:
								if(lander_x > -0.23196563869714737):
									return True
						else:
							if(lander_y <= 1.4422094821929932):
								if(angle_velocity <= 0.23621858656406403):
									if(x_velocity > 0.03866477310657501):
										return True
		else:
			if(x_velocity <= 0.18656544387340546):
				if(lander_y <= -0.044073011726140976):
					if(angle_velocity <= -0.0004694566159741953):
						if(angle <= 0.30547989904880524):
							return True
				else:
					if(x_velocity > -0.29649674892425537):
						if(x_velocity <= -0.13633117079734802):
							if(angle_velocity <= -0.19100315123796463):
								if(angle_velocity <= -0.23226524889469147):
									if(y_velocity <= 0.035931989550590515):
										return True
								else:
									return True
						else:
							if(angle <= 0.3047634959220886):
								if(lander_y <= 1.454972743988037):
									if(x_velocity <= 0.17811888456344604):
										if(y_velocity <= -9.444370880373754e-05):
											if(y_velocity <= -9.544390923110768e-05):
												if(angle <= 0.10312356427311897):
													return True
												else:
													if(x_velocity > -0.0012096493737772107):
														return True
										else:
											return True
									else:
										if(lander_y <= 0.705919228726998):
											return True
								else:
									if(lander_y > 1.4570536017417908):
										if(y_velocity > 0.011451031547039747):
											return True
							else:
								if(angle_velocity <= -0.00037222792161628604):
									return True
			else:
				if(x_velocity <= 0.44430138170719147):
					if(lander_y <= 1.4766086339950562):
						if(x_velocity > 0.23011696338653564):
							if(x_velocity <= 0.27121466398239136):
								if(angle_velocity <= 0.09294815734028816):
									if(angle <= -0.0002486870507709682):
										if(x_velocity <= 0.26243607699871063):
											if(y_velocity <= 0.2615943029522896):
												return True
										else:
											return True
								else:
									return True
					else:
						if(angle <= 0.14202280342578888):
							return True
	return False

def weShould_left_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.13701249659061432):
		if(y_velocity <= -0.220126174390316):
			if(angle_velocity <= -0.030239202082157135):
				if(angle <= 0.19462168961763382):
					if(lander_y <= 1.3413802981376648):
						if(y_velocity <= -0.2712501585483551):
							if(angle <= 0.061055488884449005):
								if(y_velocity <= -0.47413963079452515):
									if(x_velocity > -0.5935395658016205):
										if(angle <= -0.28904587030410767):
											if(y_velocity <= -0.5010827481746674):
												if(y_velocity > -0.5407353937625885):
													if(lander_y <= 1.07346510887146):
														if(angle_velocity <= -0.05043032579123974):
															if(lander_y <= 1.035538136959076):
																return True
															else:
																if(angle_velocity <= -0.19462913274765015):
																	return True
											else:
												if(y_velocity <= -0.4779440760612488):
													return True
										else:
											if(angle <= -0.03099391609430313):
												if(lander_x <= -0.14950332790613174):
													if(lander_x <= -0.1533764824271202):
														if(angle_velocity <= -0.26971299946308136):
															if(x_velocity > -0.5262067019939423):
																return True
													else:
														return True
								else:
									if(angle_velocity <= -0.08699863031506538):
										if(y_velocity <= -0.342959463596344):
											if(angle <= -0.18322286009788513):
												if(x_velocity > -0.5325293242931366):
													if(lander_y <= 1.0766575336456299):
														if(x_velocity <= -0.4057718515396118):
															if(y_velocity <= -0.4388863295316696):
																if(lander_x <= -0.1599287986755371):
																	if(y_velocity <= -0.4611012190580368):
																		return True
															else:
																return True
														else:
															if(angle_velocity <= -0.10576049610972404):
																return True
													else:
														return True
											else:
												if(x_velocity > -0.4903474748134613):
													if(angle_velocity <= -0.32994210720062256):
														if(angle <= 0.017730834893882275):
															if(x_velocity > -0.486134335398674):
																if(angle_velocity <= -0.3343295305967331):
																	if(lander_y <= 0.9598945379257202):
																		if(angle_velocity > -0.3922143280506134):
																			return True
																	else:
																		return True
																else:
																	if(angle_velocity > -0.3325864374637604):
																		return True
														else:
															if(lander_x > 0.23512211441993713):
																if(y_velocity > -0.3725551664829254):
																	return True
													else:
														if(y_velocity <= -0.4216584116220474):
															if(lander_y <= 0.8977401554584503):
																if(angle_velocity <= -0.2290351763367653):
																	return True
															else:
																if(x_velocity > -0.30474819242954254):
																	if(lander_y <= 1.271756112575531):
																		if(angle_velocity <= -0.11983776837587357):
																			return True
														else:
															if(angle <= -0.09334746748209):
																if(lander_y > 0.8961840569972992):
																	if(x_velocity > -0.4140353798866272):
																		if(angle <= -0.11283218860626221):
																			if(x_velocity <= -0.3804764300584793):
																				if(lander_x > 0.18944025039672852):
																					return True
																			else:
																				return True
																		else:
																			if(angle_velocity <= -0.12647632881999016):
																				if(lander_x > -0.05339784733951092):
																					if(lander_y <= 1.3081669807434082):
																						return True
																					else:
																						if(y_velocity > -0.3763630539178848):
																							return True
															else:
																if(x_velocity <= -0.1488664746284485):
																	if(angle_velocity <= -0.25299203395843506):
																		if(y_velocity <= -0.3954121917486191):
																			if(lander_x <= -0.05110583454370499):
																				return True
																		else:
																			if(angle <= 0.014111994300037622):
																				return True
																	else:
																		if(x_velocity <= -0.2530298978090286):
																			if(y_velocity > -0.3705414682626724):
																				if(lander_x <= 0.1948225498199463):
																					return True
																				else:
																					if(y_velocity > -0.3451025038957596):
																						return True
																		else:
																			if(lander_y > 1.3227459788322449):
																				if(lander_y <= 1.3251177668571472):
																					return True
																else:
																	return True
										else:
											if(y_velocity <= -0.28863246738910675):
												if(angle <= 0.005772620206698775):
													if(lander_y <= 1.3169233798980713):
														if(lander_y <= 0.8466216921806335):
															if(lander_y <= 0.793368399143219):
																return True
															else:
																if(x_velocity <= -0.21715107560157776):
																	if(x_velocity <= -0.22931460291147232):
																		if(y_velocity <= -0.31617462635040283):
																			return True
																else:
																	return True
														else:
															if(angle_velocity <= -0.09502262994647026):
																return True
															else:
																if(angle_velocity > -0.09259713813662529):
																	if(lander_x <= 0.19910035282373428):
																		return True
												else:
													if(angle_velocity <= -0.11864189431071281):
														if(angle <= 0.050486838445067406):
															if(lander_y > 0.7911439538002014):
																return True
														else:
															if(lander_y > 1.0645220875740051):
																return True
													else:
														if(lander_x <= 0.04182085837237537):
															return True
														else:
															if(y_velocity > -0.2934129238128662):
																if(lander_y > 1.0263058245182037):
																	return True
											else:
												if(angle_velocity <= -0.09310219064354897):
													return True
									else:
										if(y_velocity <= -0.29542168974876404):
											if(angle <= -0.07191513851284981):
												if(y_velocity <= -0.34861670434474945):
													if(y_velocity <= -0.44248321652412415):
														if(y_velocity <= -0.4702040106058121):
															return True
													else:
														if(angle <= -0.22638513892889023):
															return True
														else:
															if(x_velocity <= -0.15816737711429596):
																if(angle <= -0.12100015580654144):
																	if(y_velocity <= -0.4032207280397415):
																		if(y_velocity <= -0.42613089084625244):
																			if(y_velocity > -0.43078747391700745):
																				return True
																	else:
																		if(y_velocity <= -0.38404443860054016):
																			if(y_velocity <= -0.3966951072216034):
																				if(y_velocity <= -0.4016437828540802):
																					return True
																			else:
																				return True
																		else:
																			if(angle <= -0.15946373343467712):
																				if(angle > -0.19899845123291016):
																					if(angle <= -0.16517337411642075):
																						return True
																					else:
																						if(angle > -0.16229700297117233):
																							return True
															else:
																if(y_velocity > -0.36866995692253113):
																	return True
												else:
													if(lander_x <= 0.14664892852306366):
														return True
													else:
														if(x_velocity <= -0.20580187439918518):
															if(lander_x > 0.15389323234558105):
																if(angle_velocity <= -0.04370689205825329):
																	return True
											else:
												if(lander_x <= -0.007135295774787664):
													if(y_velocity > -0.321407288312912):
														if(lander_y > 0.8598849773406982):
															if(angle <= -0.005697358166798949):
																if(x_velocity <= -0.08528625592589378):
																	if(angle_velocity <= -0.05914578586816788):
																		return True
																else:
																	return True
															else:
																if(x_velocity <= -0.04308090731501579):
																	if(lander_y > 1.1663776636123657):
																		return True
												else:
													if(lander_y <= 1.2945742011070251):
														if(angle <= -0.03646194934844971):
															if(y_velocity <= -0.31038226187229156):
																if(angle_velocity <= -0.07628023251891136):
																	if(angle_velocity > -0.0856061577796936):
																		return True
															else:
																if(x_velocity > -0.1803419589996338):
																	if(lander_y <= 0.7398872971534729):
																		if(angle_velocity <= -0.06400062888860703):
																			return True
																	else:
																		return True
														else:
															if(x_velocity > -0.15120955556631088):
																if(lander_y <= 0.8536113202571869):
																	if(lander_y > 0.8424327373504639):
																		return True
																else:
																	if(y_velocity > -0.2977818697690964):
																		if(y_velocity <= -0.2975992411375046):
																			return True
													else:
														if(y_velocity > -0.32024289667606354):
															return True
										else:
											if(lander_y <= 0.6564100086688995):
												if(angle <= -0.023787091486155987):
													if(lander_y > 0.4388291835784912):
														if(lander_y <= 0.6390377581119537):
															return True
												else:
													if(angle_velocity <= -0.06376543268561363):
														if(lander_x <= -0.006406688829883933):
															return True
											else:
												if(angle <= 0.004643378080800176):
													if(x_velocity <= -0.1016995906829834):
														if(lander_y <= 0.8948809802532196):
															if(lander_x > 0.045068979263305664):
																return True
													else:
														if(angle_velocity <= -0.038199782371520996):
															if(y_velocity <= -0.29217106103897095):
																if(angle_velocity <= -0.05975296162068844):
																	return True
															else:
																if(angle <= 0.002516412700060755):
																	if(lander_x <= -0.034493875689804554):
																		if(angle <= -0.011263435240834951):
																			return True
																	else:
																		return True
																else:
																	if(lander_y > 0.7866464257240295):
																		return True
														else:
															if(lander_y > 0.7516250014305115):
																if(angle <= -0.012499293312430382):
																	return True
																else:
																	if(x_velocity <= -0.030099776573479176):
																		if(lander_y <= 0.8385136127471924):
																			if(y_velocity <= -0.28446145355701447):
																				return True
																	else:
																		if(x_velocity <= -0.02367000002413988):
																			return True
												else:
													if(lander_y <= 0.9250941276550293):
														if(x_velocity <= 0.016601918265223503):
															if(x_velocity > -0.0030559178558178246):
																if(lander_x > -0.021962451981380582):
																	return True
														else:
															return True
													else:
														if(x_velocity <= -0.08201296627521515):
															if(y_velocity <= -0.291550949215889):
																return True
														else:
															if(lander_y <= 1.0987120866775513):
																if(angle_velocity <= -0.046588145196437836):
																	if(x_velocity <= -0.034358756616711617):
																		if(angle_velocity <= -0.053634967654943466):
																			if(y_velocity > -0.2848924994468689):
																				if(angle <= 0.025381755083799362):
																					return True
																				else:
																					if(angle_velocity <= -0.07505744695663452):
																						if(lander_y > 1.0517600178718567):
																							return True
																		else:
																			return True
																	else:
																		return True
																else:
																	if(lander_x > 0.12578401528298855):
																		return True
															else:
																return True
							else:
								if(angle_velocity <= -0.09253112599253654):
									if(angle_velocity <= -0.42367124557495117):
										if(y_velocity > -0.33871832489967346):
											if(lander_x <= 0.253693625330925):
												return True
									else:
										if(angle <= 0.11447752267122269):
											if(lander_y <= 1.1623373627662659):
												if(angle <= 0.07942209392786026):
													if(angle <= 0.07822135090827942):
														if(lander_x <= 0.12662281841039658):
															if(y_velocity <= -0.28110910952091217):
																return True
														else:
															if(x_velocity <= -0.2300647795200348):
																if(y_velocity > -0.3441176563501358):
																	return True
													else:
														return True
												else:
													if(angle > 0.10782143846154213):
														return True
											else:
												if(y_velocity > -0.29660703241825104):
													return True
										else:
											if(lander_x > 0.24194559454917908):
												if(x_velocity > -0.07774129137396812):
													return True
								else:
									if(x_velocity > -0.08083246648311615):
										if(lander_x <= 0.04924569092690945):
											if(lander_x > 0.048288917168974876):
												return True
						else:
							if(lander_y <= 0.2888483852148056):
								if(angle_velocity <= -0.06200191378593445):
									if(y_velocity <= -0.2447967603802681):
										if(lander_y > 0.14572245627641678):
											if(x_velocity <= -0.028530413284897804):
												return True
									else:
										if(angle <= 0.017069307155907154):
											if(lander_y > 0.01458512875251472):
												if(y_velocity <= -0.22116205841302872):
													return True
								else:
									if(y_velocity <= -0.22887907177209854):
										if(y_velocity > -0.24936990439891815):
											if(angle <= -0.05136376619338989):
												if(lander_x <= -0.1559777781367302):
													if(lander_y <= 0.04192422516644001):
														return True
												else:
													if(angle <= -0.05449499189853668):
														return True
											else:
												if(lander_y <= 0.21508169919252396):
													if(angle <= -0.018539821729063988):
														if(x_velocity <= -0.04069283977150917):
															if(lander_x > 0.09661459922790527):
																if(angle <= -0.02323413360863924):
																	if(lander_y > 0.11525148898363113):
																		return True
														else:
															if(y_velocity <= -0.23400668799877167):
																if(angle_velocity <= -0.050589609891176224):
																	return True
															else:
																return True
												else:
													if(angle <= 0.007701106835156679):
														if(angle_velocity <= -0.03694206476211548):
															if(y_velocity <= -0.2376723289489746):
																return True
															else:
																if(y_velocity > -0.23474687337875366):
																	return True
														else:
															if(x_velocity > -0.008021642453968525):
																return True
									else:
										if(angle <= -0.01896038744598627):
											if(lander_x > -0.192253015935421):
												if(lander_y <= 0.22453942149877548):
													if(lander_y <= 0.03258487954735756):
														if(x_velocity <= -0.09634300321340561):
															return True
													else:
														return True
										else:
											if(angle <= 0.008450696244835854):
												if(lander_y <= 0.1256880760192871):
													if(angle_velocity > -0.036593127995729446):
														if(angle <= -0.014632944948971272):
															return True
												else:
													if(x_velocity <= -0.01630639098584652):
														if(lander_x > 0.044598388485610485):
															return True
													else:
														return True
							else:
								if(angle <= -0.004452327499166131):
									if(angle_velocity <= -0.04128412716090679):
										if(y_velocity <= -0.2575591802597046):
											if(y_velocity <= -0.2603725492954254):
												if(x_velocity <= -0.0782817117869854):
													if(lander_y <= 0.576561838388443):
														if(angle <= -0.035669573582708836):
															return True
													else:
														return True
												else:
													if(lander_y <= 0.7038154304027557):
														return True
											else:
												if(x_velocity <= -0.05547204613685608):
													return True
										else:
											if(y_velocity <= -0.2245744913816452):
												return True
											else:
												if(lander_y > 0.3470495790243149):
													return True
									else:
										if(x_velocity > -0.09462021663784981):
											if(lander_y <= 0.4283932000398636):
												if(y_velocity <= -0.23456428200006485):
													if(angle <= -0.011457640212029219):
														if(x_velocity <= -0.015013983007520437):
															if(x_velocity <= -0.0848516970872879):
																return True
															else:
																if(y_velocity <= -0.23807018995285034):
																	if(lander_y <= 0.34453655779361725):
																		return True
																	else:
																		if(lander_x > 0.11262926831841469):
																			return True
														else:
															return True
												else:
													return True
											else:
												if(angle_velocity > -0.04054407589137554):
													if(lander_x > -0.2634451389312744):
														if(y_velocity <= -0.2645799368619919):
															if(y_velocity <= -0.26575031876564026):
																return True
														else:
															return True
								else:
									if(lander_y <= 0.5517165660858154):
										if(y_velocity <= -0.24928557872772217):
											if(angle <= 0.0003672398524940945):
												if(x_velocity <= -0.026792760007083416):
													return True
										else:
											if(angle_velocity <= -0.056966641917824745):
												if(lander_x > -0.20418450981378555):
													if(x_velocity <= -0.03333435021340847):
														if(angle_velocity <= -0.09238193556666374):
															return True
													else:
														if(lander_x <= -0.10655899345874786):
															if(x_velocity > -0.0034981155768036842):
																return True
														else:
															return True
											else:
												if(y_velocity <= -0.23306214064359665):
													if(angle <= 0.0028039898024871945):
														if(lander_y <= 0.461465984582901):
															return True
													else:
														if(angle_velocity <= -0.03815866634249687):
															if(angle_velocity <= -0.03934674896299839):
																if(x_velocity <= 0.07032981887459755):
																	if(y_velocity > -0.2391762062907219):
																		if(x_velocity <= 0.034316143952310085):
																			if(y_velocity <= -0.2384628802537918):
																				return True
																		else:
																			return True
																else:
																	return True
															else:
																return True
												else:
													if(x_velocity > -0.024672605097293854):
														if(x_velocity <= 0.03441648930311203):
															if(y_velocity <= -0.22759557515382767):
																if(y_velocity > -0.2315051183104515):
																	return True
														else:
															if(lander_x > -0.19954264163970947):
																return True
									else:
										if(x_velocity <= -0.0434639286249876):
											if(lander_x <= 0.12592416256666183):
												if(lander_y > 0.6986694633960724):
													if(angle <= 0.012611632235348225):
														if(angle_velocity <= -0.05445677787065506):
															if(x_velocity > -0.08741334080696106):
																return True
											else:
												if(y_velocity <= -0.24674434214830399):
													if(x_velocity <= -0.06307151541113853):
														if(angle <= 0.17386354506015778):
															if(angle_velocity <= -0.04279521852731705):
																if(x_velocity > -0.2494330257177353):
																	return True
												else:
													if(lander_x <= 0.12972688674926758):
														return True
										else:
											if(angle <= 0.051375413313508034):
												if(angle_velocity <= -0.03644077107310295):
													if(x_velocity <= 0.0021949945949018):
														if(angle_velocity <= -0.05742747709155083):
															if(angle > -0.001935446955030784):
																return True
														else:
															if(lander_y <= 0.7053986489772797):
																if(angle <= 0.01381576550193131):
																	if(angle_velocity <= -0.04249518737196922):
																		return True
															else:
																if(lander_y <= 0.8759246468544006):
																	return True
																else:
																	if(x_velocity > -0.0039746804686728865):
																		return True
													else:
														return True
												else:
													if(y_velocity <= -0.25737951695919037):
														if(x_velocity > 0.005887146107852459):
															if(x_velocity <= 0.02421198459342122):
																return True
													else:
														if(lander_x <= 0.030249882489442825):
															if(angle <= 0.032342150807380676):
																if(x_velocity > -0.012385504087433219):
																	return True
															else:
																if(angle > 0.03969847038388252):
																	return True
											else:
												if(y_velocity <= -0.25443829596042633):
													if(angle <= 0.10417304188013077):
														if(angle_velocity <= -0.08819719403982162):
															return True
														else:
															if(x_velocity > 0.003025089274160564):
																if(y_velocity > -0.267055481672287):
																	if(angle <= 0.0846092477440834):
																		if(x_velocity <= 0.009261439554393291):
																			if(y_velocity <= -0.265315979719162):
																				return True
																		else:
																			return True
																	else:
																		if(lander_y > 1.2405642867088318):
																			return True
													else:
														if(lander_x <= 0.09951886907219887):
															if(angle_velocity <= -0.06006043031811714):
																return True
														else:
															if(angle_velocity <= -0.11974053084850311):
																if(angle <= 0.1628476306796074):
																	return True
												else:
													if(angle_velocity <= -0.09558995440602303):
														if(y_velocity <= -0.22947585582733154):
															if(angle_velocity <= -0.13757845014333725):
																return True
															else:
																if(angle <= 0.11318513751029968):
																	return True
																else:
																	if(x_velocity > 0.017923153936862946):
																		if(y_velocity <= -0.24464258551597595):
																			if(angle <= 0.1373646855354309):
																				if(lander_y > 0.9796440303325653):
																					return True
																		else:
																			if(angle_velocity > -0.13193659484386444):
																				return True
														else:
															if(x_velocity > 0.03917247615754604):
																return True
													else:
														if(x_velocity <= 0.025266282260417938):
															if(lander_y <= 0.8956425487995148):
																return True
															else:
																if(lander_y > 0.9250913858413696):
																	if(angle_velocity <= -0.08545486629009247):
																		if(angle_velocity > -0.08999278023838997):
																			return True
														else:
															if(angle <= 0.12195507436990738):
																if(lander_x > -0.014197825454175472):
																	if(y_velocity <= -0.2534603327512741):
																		if(angle_velocity <= -0.06740169413387775):
																			return True
																	else:
																		return True
															else:
																if(x_velocity > 0.08360905200242996):
																	if(lander_y > 1.2113174200057983):
																		if(y_velocity > -0.24811803549528122):
																			return True
					else:
						if(x_velocity > -0.32714836299419403):
							if(angle <= -0.004083811771124601):
								if(y_velocity <= -0.3513885885477066):
									if(lander_y <= 1.373328447341919):
										if(lander_x <= -0.020254516042768955):
											if(lander_y <= 1.3663036227226257):
												return True
											else:
												if(x_velocity <= -0.3185473084449768):
													return True
									else:
										if(x_velocity <= -0.3144731968641281):
											if(lander_y > 1.4056146144866943):
												return True
										else:
											return True
								else:
									if(lander_y > 1.3652410507202148):
										if(x_velocity <= -0.18263256549835205):
											if(angle <= -0.03330042492598295):
												if(angle_velocity <= -0.1117359884083271):
													return True
												else:
													if(x_velocity <= -0.32189711928367615):
														return True
													else:
														if(y_velocity <= -0.29995226860046387):
															if(angle_velocity <= -0.0641060322523117):
																return True
										else:
											return True
							else:
								if(y_velocity > -0.24147136509418488):
									if(lander_x > 0.08810477331280708):
										return True
				else:
					if(angle <= 0.2628934383392334):
						if(lander_y > 0.7854368686676025):
							if(lander_x <= 0.1162346825003624):
								if(x_velocity <= 0.1752893328666687):
									return True
							else:
								if(x_velocity > -0.18661167472600937):
									if(y_velocity > -0.23782780021429062):
										if(angle_velocity <= -0.17055439203977585):
											if(y_velocity <= -0.2292066365480423):
												return True
			else:
				if(lander_y <= 0.3988706022500992):
					if(angle_velocity <= -0.005895595299080014):
						if(y_velocity <= -0.23697848618030548):
							if(angle <= -0.03992721438407898):
								if(lander_y <= 0.174763984978199):
									if(y_velocity > -0.2448679730296135):
										if(lander_x <= 0.024794816970825195):
											if(lander_y <= 0.058977493084967136):
												return True
								else:
									if(y_velocity <= -0.2558140754699707):
										if(angle_velocity <= -0.018434702418744564):
											if(lander_x > -0.05044736934360117):
												return True
									else:
										if(x_velocity <= -0.07868277654051781):
											if(angle <= -0.08147457987070084):
												return True
										else:
											if(lander_y <= 0.37730106711387634):
												return True
							else:
								if(lander_y <= 0.3966212570667267):
									if(lander_y > 0.29461008310317993):
										if(lander_y <= 0.29696352779865265):
											return True
										else:
											if(lander_x > -0.032745121978223324):
												if(lander_x <= -0.0028357982664601877):
													if(angle_velocity <= -0.0138159841299057):
														return True
								else:
									return True
						else:
							if(angle <= -0.025198427960276604):
								if(x_velocity <= -0.08618466928601265):
									if(angle <= -0.0487993024289608):
										return True
								else:
									if(angle_velocity > -0.027504215016961098):
										if(x_velocity <= -0.03842702694237232):
											if(lander_y <= 0.29612164199352264):
												if(y_velocity <= -0.22554226964712143):
													if(lander_y <= 0.026572690345346928):
														if(x_velocity > -0.06104778125882149):
															return True
													else:
														return True
										else:
											return True
							else:
								if(lander_y <= 0.20550113171339035):
									if(x_velocity > -0.06678585708141327):
										if(angle <= -0.019534876570105553):
											if(lander_y > 0.08102371357381344):
												return True
								else:
									if(lander_x <= -0.10965194553136826):
										if(angle <= -0.010702112689614296):
											if(lander_y > 0.3300902396440506):
												return True
									else:
										if(angle <= 0.013557164464145899):
											if(angle_velocity <= -0.007875385228544474):
												if(angle <= -0.004473929526284337):
													if(angle_velocity > -0.02599407359957695):
														if(x_velocity > -0.06300520338118076):
															return True
												else:
													if(x_velocity <= 0.0025092814466916025):
														if(x_velocity <= -0.0267856540158391):
															return True
													else:
														if(angle_velocity <= -0.009860043413937092):
															if(lander_y > 0.22057675570249557):
																return True
											else:
												if(y_velocity <= -0.2295401468873024):
													return True
										else:
											if(x_velocity <= 0.042379504069685936):
												if(lander_y > 0.3628438115119934):
													if(lander_x > 0.03796401061117649):
														return True
											else:
												return True
					else:
						if(angle_velocity <= 0.1071605421602726):
							if(angle <= -0.007234708871692419):
								if(y_velocity <= -0.23764991760253906):
									if(x_velocity > -0.13719099014997482):
										if(angle <= -0.06476367264986038):
											if(y_velocity > -0.2619546800851822):
												if(angle_velocity <= 0.03959674946963787):
													if(lander_y <= 0.30810460448265076):
														if(x_velocity <= -0.0584693793207407):
															if(lander_y > 0.2459413707256317):
																if(lander_y <= 0.26593248546123505):
																	return True
														else:
															return True
													else:
														return True
										else:
											if(y_velocity > -0.2452927529811859):
												if(lander_y > 0.2798342704772949):
													if(x_velocity <= -0.0206613726913929):
														if(x_velocity <= -0.03133177664130926):
															if(lander_y <= 0.2984888553619385):
																if(angle > -0.03760555759072304):
																	return True
														else:
															return True
													else:
														if(x_velocity > 0.03322521224617958):
															return True
								else:
									if(lander_y <= 0.26747365295886993):
										if(x_velocity > -0.0627112053334713):
											if(angle_velocity <= 0.005520625039935112):
												if(angle_velocity <= 0.003953332896344364):
													if(x_velocity <= 0.026511111296713352):
														if(angle_velocity <= -0.00425525032915175):
															if(angle_velocity > -0.00488924328237772):
																return True
													else:
														return True
												else:
													if(angle > -0.04426326975226402):
														return True
									else:
										if(lander_x <= -0.08530726283788681):
											if(x_velocity > 0.024723042268306017):
												return True
										else:
											if(angle_velocity <= 0.001189333685033489):
												return True
											else:
												if(x_velocity <= -0.009728663600981236):
													if(y_velocity > -0.23149458318948746):
														if(angle_velocity <= 0.05043022893369198):
															if(angle <= -0.08178627863526344):
																return True
														else:
															return True
												else:
													if(lander_x <= -0.009571123402565718):
														if(x_velocity > 0.023265737108886242):
															if(angle_velocity <= 0.0569342914968729):
																return True
													else:
														if(angle_velocity <= 0.05781659111380577):
															return True
							else:
								if(x_velocity > -0.05363779328763485):
									if(y_velocity <= -0.22065309435129166):
										if(y_velocity > -0.2258555367588997):
											if(y_velocity <= -0.22582001984119415):
												return True
				else:
					if(y_velocity <= -0.2591031938791275):
						if(x_velocity > -0.4677737355232239):
							if(angle <= -0.05331459268927574):
								if(y_velocity <= -0.28979015350341797):
									if(y_velocity <= -0.32377180457115173):
										if(lander_y <= 1.0612746477127075):
											if(angle <= -0.20151109993457794):
												if(y_velocity <= -0.3569426089525223):
													if(angle_velocity <= 0.03919844701886177):
														if(y_velocity <= -0.40547867119312286):
															if(lander_x <= -0.24282576888799667):
																if(angle_velocity <= 0.033268094062805176):
																	return True
															else:
																if(y_velocity > -0.4243869483470917):
																	if(angle > -0.2885611355304718):
																		if(angle <= -0.2438676431775093):
																			return True
														else:
															return True
													else:
														if(y_velocity <= -0.3872532546520233):
															if(angle <= -0.3148250877857208):
																if(y_velocity <= -0.461546927690506):
																	if(angle_velocity <= 0.05595002695918083):
																		return True
																	else:
																		if(x_velocity > -0.28484678268432617):
																			if(angle_velocity <= 0.10261939838528633):
																				return True
																else:
																	return True
															else:
																if(lander_y <= 1.037104070186615):
																	if(x_velocity > -0.31900712847709656):
																		if(x_velocity > -0.09326792880892754):
																			if(x_velocity <= -0.08039824664592743):
																				return True
																else:
																	if(angle > -0.3008088916540146):
																		return True
														else:
															if(angle <= -0.23443743586540222):
																if(lander_x <= -0.23447678238153458):
																	if(y_velocity <= -0.36935967206954956):
																		if(angle_velocity <= 0.07885494455695152):
																			return True
																	else:
																		return True
																else:
																	if(y_velocity <= -0.37790706753730774):
																		return True
															else:
																if(lander_y > 0.9833517670631409):
																	return True
												else:
													if(angle <= -0.20489487797021866):
														if(angle_velocity <= 0.11081285029649734):
															return True
														else:
															if(y_velocity > -0.34119923412799835):
																return True
											else:
												if(y_velocity <= -0.3360630124807358):
													if(x_velocity > -0.3516712188720703):
														if(angle_velocity <= 0.21774686127901077):
															if(lander_y > 1.0004624426364899):
																if(lander_y <= 1.0024277567863464):
																	return True
																else:
																	if(angle_velocity <= -0.005694378829502966):
																		if(lander_x <= -0.08002576977014542):
																			return True
																	else:
																		if(angle <= -0.1520085111260414):
																			if(lander_x <= -0.1869145855307579):
																				return True
																		else:
																			if(angle_velocity <= 0.024869399145245552):
																				if(angle_velocity > 0.020315569825470448):
																					return True
												else:
													if(angle <= -0.16341836005449295):
														if(angle_velocity > 0.03856382332742214):
															if(angle_velocity <= 0.13748598098754883):
																if(lander_y > 0.7049829363822937):
																	return True
													else:
														if(angle_velocity <= 0.04832232557237148):
															if(lander_x <= -0.10481705516576767):
																return True
															else:
																if(angle <= -0.0997859351336956):
																	if(lander_y > 0.6811869740486145):
																		if(angle > -0.1066688820719719):
																			return True
										else:
											if(y_velocity <= -0.3447175920009613):
												if(angle <= -0.14506709575653076):
													if(y_velocity <= -0.3985508531332016):
														if(lander_y <= 1.063765048980713):
															return True
														else:
															if(angle_velocity <= -0.01774553209543228):
																if(x_velocity <= -0.2994004786014557):
																	if(x_velocity <= -0.3445555120706558):
																		return True
																else:
																	return True
															else:
																if(lander_y <= 1.3167800903320312):
																	if(lander_x <= -0.1942407563328743):
																		return True
																	else:
																		if(lander_y > 1.2698836922645569):
																			if(lander_y <= 1.2792267799377441):
																				if(y_velocity <= -0.40654876828193665):
																					return True
																else:
																	if(angle_velocity <= 0.001375226303935051):
																		return True
													else:
														if(angle <= -0.1828475147485733):
															if(angle_velocity <= 0.04813747853040695):
																if(lander_x <= -0.1620314121246338):
																	if(lander_x <= -0.17086639255285263):
																		return True
																else:
																	return True
															else:
																if(lander_y <= 1.1418097615242004):
																	return True
														else:
															if(y_velocity <= -0.36406198143959045):
																if(angle_velocity <= 0.005274130031466484):
																	if(y_velocity > -0.38150131702423096):
																		return True
																else:
																	if(y_velocity <= -0.39671097695827484):
																		return True
																	else:
																		if(angle <= -0.17899803817272186):
																			if(angle > -0.18128757923841476):
																				return True
															else:
																if(angle_velocity <= 0.04756132513284683):
																	return True
																else:
																	if(x_velocity > -0.14022498577833176):
																		if(lander_y <= 1.1165762543678284):
																			return True
												else:
													if(y_velocity > -0.3601759523153305):
														if(y_velocity <= -0.35688579082489014):
															if(y_velocity <= -0.3574644923210144):
																return True
														else:
															if(lander_y <= 1.3207906484603882):
																if(y_velocity <= -0.35348817706108093):
																	if(lander_x <= -0.057523250579833984):
																		return True
															else:
																return True
											else:
												if(angle <= -0.06962037831544876):
													if(y_velocity <= -0.33256442844867706):
														if(x_velocity <= -0.15777025371789932):
															if(lander_y <= 1.1435661315917969):
																return True
														else:
															if(lander_y <= 1.0779027342796326):
																return True
															else:
																if(angle <= -0.07502911239862442):
																	if(y_velocity <= -0.34312212467193604):
																		if(angle > -0.13438867777585983):
																			return True
																else:
																	return True
													else:
														if(angle_velocity <= -0.010737831704318523):
															return True
												else:
													if(y_velocity <= -0.33425386250019073):
														return True
									else:
										if(lander_y <= 0.9724603593349457):
											if(angle <= -0.13911590725183487):
												if(y_velocity <= -0.3128570020198822):
													if(angle <= -0.16731970012187958):
														if(lander_x <= -0.2830394506454468):
															return True
													else:
														if(angle_velocity <= 0.05194188840687275):
															return True
												else:
													if(angle_velocity <= 0.15131288766860962):
														if(lander_x > -0.2863030731678009):
															if(lander_y <= 0.6544494330883026):
																if(y_velocity <= -0.31085169315338135):
																	return True
																else:
																	if(x_velocity > -0.15985646098852158):
																		if(lander_y <= 0.6447462141513824):
																			return True
															else:
																return True
											else:
												if(lander_x <= 0.17120051383972168):
													if(angle_velocity <= -0.005081556271761656):
														if(x_velocity > -0.1315990537405014):
															if(angle <= -0.0725240409374237):
																return True
															else:
																if(x_velocity <= -0.12408722564578056):
																	return True
													else:
														if(angle <= -0.11836115643382072):
															if(angle_velocity <= 0.035113219171762466):
																return True
															else:
																if(angle <= -0.12105177715420723):
																	if(lander_y <= 0.5059874653816223):
																		return True
																else:
																	if(y_velocity <= -0.30349576473236084):
																		return True
														else:
															if(angle <= -0.05388873629271984):
																if(lander_y <= 0.9470905959606171):
																	if(y_velocity <= -0.30324292182922363):
																		if(angle <= -0.05917237140238285):
																			if(angle <= -0.11068673804402351):
																				if(lander_y > 0.7255429923534393):
																					return True
																		else:
																			if(angle <= -0.05811325088143349):
																				return True
																	else:
																		if(y_velocity > -0.3031436502933502):
																			if(angle_velocity <= 0.001812802569475025):
																				if(lander_y <= 0.6748694181442261):
																					return True
																			else:
																				if(x_velocity > -0.14478172361850739):
																					if(lander_y <= 0.890732079744339):
																						if(angle_velocity <= 0.017454905435442924):
																							if(x_velocity > -0.10349521413445473):
																								return True
																						else:
																							if(angle <= -0.10757024213671684):
																								if(x_velocity <= -0.106439758092165):
																									return True
																					else:
																						if(y_velocity <= -0.2978654056787491):
																							return True
																else:
																	if(angle_velocity <= 0.03174198791384697):
																		return True
															else:
																return True
												else:
													if(angle <= -0.11172544583678246):
														return True
										else:
											if(x_velocity <= -0.0746455229818821):
												if(angle_velocity <= 0.027894112281501293):
													if(lander_x <= -0.08236465603113174):
														if(angle <= -0.08952869474887848):
															return True
													else:
														if(y_velocity > -0.31221911311149597):
															if(lander_y > 1.083028793334961):
																return True
												else:
													if(angle <= -0.1307736337184906):
														if(lander_x > -0.16486988216638565):
															return True
													else:
														if(lander_x <= -0.12311496585607529):
															if(lander_y > 1.070564091205597):
																return True
											else:
												if(y_velocity <= -0.2972036898136139):
													if(x_velocity > -0.06677962467074394):
														if(lander_x <= -0.1553829237818718):
															if(angle_velocity > 0.10363348573446274):
																return True
														else:
															if(angle_velocity <= 0.08678365498781204):
																return True
								else:
									if(angle_velocity <= 0.05515405908226967):
										if(lander_y <= 0.5726955235004425):
											if(angle <= -0.07068922743201256):
												if(y_velocity <= -0.2825336307287216):
													return True
												else:
													if(x_velocity > -0.12021123990416527):
														if(lander_x > -0.3089955896139145):
															if(y_velocity <= -0.26162753999233246):
																return True
											else:
												if(y_velocity > -0.2722477614879608):
													if(angle_velocity <= 0.008120624348521233):
														return True
										else:
											if(x_velocity <= -0.06573277339339256):
												if(lander_y <= 0.6902416348457336):
													if(angle_velocity <= 0.03395815286785364):
														return True
													else:
														if(lander_y > 0.6364759206771851):
															if(angle <= -0.0842120386660099):
																return True
												else:
													if(y_velocity <= -0.2708781063556671):
														if(lander_y <= 1.0126219987869263):
															if(x_velocity > -0.06814582273364067):
																if(lander_y <= 0.9211913049221039):
																	return True
														else:
															return True
													else:
														return True
											else:
												if(y_velocity <= -0.28788553178310394):
													if(x_velocity > -0.025965365581214428):
														return True
												else:
													return True
									else:
										if(lander_y <= 0.7663210034370422):
											if(angle <= -0.10654593259096146):
												if(y_velocity > -0.2830393612384796):
													if(y_velocity <= -0.27401989698410034):
														if(lander_x <= -0.2698782831430435):
															return True
											else:
												if(x_velocity > -0.14428503811359406):
													if(y_velocity <= -0.270984947681427):
														if(angle <= -0.1030520498752594):
															if(angle > -0.10459158197045326):
																return True
													else:
														if(lander_y <= 0.5829871296882629):
															if(lander_y <= 0.4420061707496643):
																if(x_velocity > -0.07857425697147846):
																	return True
										else:
											if(x_velocity <= 0.017174482811242342):
												if(y_velocity > -0.2667526751756668):
													if(y_velocity <= -0.26349999010562897):
														return True
											else:
												if(y_velocity > -0.27996663749217987):
													if(angle_velocity <= 0.1108262650668621):
														return True
							else:
								if(lander_y <= 0.7862126231193542):
									if(y_velocity <= -0.264681339263916):
										if(lander_y <= 0.726870208978653):
											if(x_velocity > -0.11643403023481369):
												if(angle_velocity <= 0.0818091630935669):
													if(y_velocity <= -0.2663245052099228):
														if(y_velocity > -0.27826161682605743):
															if(y_velocity <= -0.2781319171190262):
																return True
															else:
																if(x_velocity > -0.09295184165239334):
																	if(angle_velocity <= 0.0037979177432134748):
																		if(angle_velocity <= 0.0032262742752209306):
																			if(lander_y > 0.6484237611293793):
																				if(angle <= -0.03455995116382837):
																					return True
																				else:
																					if(x_velocity > 0.025959890335798264):
																						if(angle_velocity <= -0.006534545042086393):
																							return True
																		else:
																			return True
													else:
														if(y_velocity <= -0.2662261426448822):
															return True
														else:
															if(lander_x > 0.09752116352319717):
																if(x_velocity > -0.03866182826459408):
																	return True
										else:
											if(lander_y <= 0.7282095849514008):
												if(lander_x <= -0.015373898670077324):
													return True
											else:
												if(y_velocity <= -0.27001261711120605):
													if(angle <= -0.036538174375891685):
														if(y_velocity <= -0.2824312895536423):
															if(y_velocity > -0.2909196615219116):
																if(lander_x > 0.06868495792150497):
																	return True
														else:
															if(angle_velocity <= -0.00475817546248436):
																return True
													else:
														if(y_velocity > -0.27545684576034546):
															if(y_velocity <= -0.2753885090351105):
																return True
												else:
													if(angle_velocity <= -0.00363212579395622):
														if(y_velocity <= -0.26842033863067627):
															return True
									else:
										if(angle <= -0.018328707665205002):
											if(lander_y <= 0.6719333529472351):
												if(angle <= -0.020177501253783703):
													if(angle_velocity <= -0.015758157707750797):
														if(angle_velocity > -0.024554399773478508):
															return True
													else:
														if(lander_x <= 0.09896249696612358):
															if(lander_y > 0.568742573261261):
																if(x_velocity <= -0.044225575402379036):
																	return True
												else:
													return True
											else:
												if(angle_velocity <= 0.030637436546385288):
													if(y_velocity > -0.2641945630311966):
														return True
												else:
													if(x_velocity > 0.023183227516710758):
														if(angle_velocity > 0.040583858266472816):
															return True
										else:
											if(lander_x <= 0.15579185634851456):
												if(angle <= -0.012741807848215103):
													if(x_velocity > 0.042152289301157):
														return True
												else:
													if(lander_x <= -0.17127098888158798):
														if(y_velocity > -0.26009903848171234):
															return True
											else:
												if(x_velocity > -0.061157720163464546):
													if(angle <= 0.003152078716084361):
														return True
								else:
									if(y_velocity <= -0.28120529651641846):
										if(lander_y <= 1.3223260641098022):
											if(x_velocity <= 0.689288318157196):
												if(y_velocity <= -0.29172690212726593):
													if(lander_y <= 1.1302112936973572):
														if(lander_y <= 0.7932920157909393):
															if(lander_x > 0.04580864869058132):
																return True
													else:
														if(x_velocity > -0.06834279373288155):
															if(angle <= 0.032738350331783295):
																if(y_velocity <= -0.2967776656150818):
																	if(lander_x <= 0.054551173001527786):
																		if(y_velocity <= -0.31002724170684814):
																			if(lander_y <= 1.1310220956802368):
																				return True
																			else:
																				if(angle_velocity <= -0.028702893294394016):
																					return True
																		else:
																			if(x_velocity > -0.024523289874196053):
																				if(angle_velocity <= 0.01953697530552745):
																					return True
																	else:
																		return True
												else:
													if(angle <= -0.03183910623192787):
														if(angle_velocity <= 0.03209804557263851):
															if(lander_y > 0.8246901035308838):
																return True
													else:
														if(angle_velocity <= -0.014398808125406504):
															if(angle <= -0.00023564865114167333):
																return True
														else:
															if(lander_y <= 1.0982114672660828):
																if(angle <= -0.02307185810059309):
																	if(angle_velocity <= 0.0034483526833355427):
																		return True
																else:
																	if(lander_x <= -0.06691999360918999):
																		if(lander_y > 0.9380663931369781):
																			if(lander_x > -0.06859641149640083):
																				return True
															else:
																if(lander_x <= -0.014168167021125555):
																	if(lander_x <= -0.04693288914859295):
																		return True
																else:
																	if(lander_y <= 1.1329796314239502):
																		if(y_velocity <= -0.28620511293411255):
																			return True
																	else:
																		if(angle <= 0.05461981147527695):
																			if(x_velocity > 0.068813756108284):
																				return True
											else:
												return True
										else:
											if(x_velocity <= 0.3373533934354782):
												if(angle_velocity <= 0.02754958253353834):
													if(y_velocity <= -0.3092615008354187):
														if(lander_x > 0.0002729415718931705):
															if(angle_velocity <= 0.013891918584704399):
																return True
													else:
														if(x_velocity <= -0.025174960494041443):
															if(angle <= -0.0073786829598248005):
																return True
														else:
															return True
												else:
													if(x_velocity <= 0.26448947191238403):
														if(lander_x > -0.007713413331657648):
															if(y_velocity > -0.2839295417070389):
																if(lander_x <= 0.015925979241728783):
																	return True
													else:
														if(angle_velocity <= 0.22475795447826385):
															return True
											else:
												if(lander_x <= 0.08645286411046982):
													return True
									else:
										if(angle <= 0.008823844138532877):
											if(x_velocity <= 0.02957223169505596):
												if(angle_velocity <= -0.003948292229324579):
													if(x_velocity <= -0.07307593896985054):
														if(angle <= -0.03909788653254509):
															return True
													else:
														if(y_velocity <= -0.2766232490539551):
															if(lander_x <= 0.12454085052013397):
																if(lander_y <= 1.0828734040260315):
																	if(lander_x > 0.050665806978940964):
																		if(lander_x <= 0.06941809505224228):
																			return True
																else:
																	return True
															else:
																return True
														else:
															if(y_velocity <= -0.2619604170322418):
																if(angle_velocity > -0.029291611164808273):
																	if(x_velocity <= -0.008382251020520926):
																		return True
																	else:
																		if(x_velocity > -0.004336855374276638):
																			return True
												else:
													if(lander_y > 0.8370178639888763):
														if(x_velocity <= 0.0015450450009666383):
															if(lander_x > -0.14837151020765305):
																if(lander_x > 0.03444819524884224):
																	if(lander_x <= 0.03544206731021404):
																		return True
														else:
															if(angle_velocity <= 0.07028498873114586):
																if(x_velocity <= 0.018781457096338272):
																	return True
											else:
												if(lander_y <= 0.8839908838272095):
													if(angle > 0.0016690654447302222):
														if(lander_y <= 0.825396716594696):
															return True
												else:
													if(x_velocity > 0.04417895898222923):
														return True
										else:
											if(x_velocity > -0.024900871329009533):
												if(lander_y <= 1.1035210490226746):
													if(angle_velocity <= -0.007809704169631004):
														if(lander_x <= -0.0066200734581798315):
															if(lander_y <= 0.8830638229846954):
																if(lander_x > -0.025331116281449795):
																	return True
															else:
																return True
														else:
															if(angle_velocity > -0.009957340080291033):
																return True
													else:
														if(x_velocity > 0.0636452604085207):
															if(angle_velocity <= 0.011627326952293515):
																return True
												else:
													if(angle <= 0.059718646109104156):
														if(x_velocity <= 0.07696686312556267):
															if(angle_velocity <= 0.049309903755784035):
																if(y_velocity > -0.27673155069351196):
																	return True
														else:
															if(angle <= 0.044628797098994255):
																return True
													else:
														if(x_velocity > 0.016323771327733994):
															if(angle <= 0.5938259661197662):
																if(angle <= 0.0917450375854969):
																	if(angle <= 0.08894968032836914):
																		if(angle_velocity <= -0.0218551866710186):
																			return True
																		else:
																			if(x_velocity > 0.10189161077141762):
																				if(angle_velocity <= 0.040689398534595966):
																					return True
																	else:
																		if(angle_velocity <= -0.007655544090084732):
																			return True
					else:
						if(x_velocity <= 0.0351233147084713):
							if(lander_y <= 0.6716362833976746):
								if(y_velocity <= -0.24182037264108658):
									if(angle <= -0.030423035845160484):
										if(angle_velocity <= 0.012476997915655375):
											if(y_velocity > -0.2574797421693802):
												if(x_velocity > -0.0958431251347065):
													if(lander_y <= 0.6339707970619202):
														if(lander_x > -0.26393239200115204):
															if(angle_velocity <= -0.00016509604756720364):
																return True
															else:
																if(angle <= -0.03813371993601322):
																	return True
																else:
																	if(lander_y > 0.441238209605217):
																		if(angle_velocity > 0.010764136910438538):
																			return True
										else:
											if(x_velocity <= -0.04057971388101578):
												if(x_velocity > -0.06967438757419586):
													if(x_velocity <= -0.060181522741913795):
														return True
											else:
												if(angle_velocity <= 0.06265179812908173):
													if(lander_y > 0.5813332498073578):
														return True
												else:
													if(x_velocity <= -0.02495346311479807):
														return True
									else:
										if(x_velocity <= -0.022938490845263004):
											if(y_velocity <= -0.2510243207216263):
												if(x_velocity <= -0.03385838866233826):
													if(x_velocity > -0.09269861876964569):
														if(y_velocity <= -0.25851693749427795):
															if(angle > -0.023491637781262398):
																return True
														else:
															if(angle <= -0.02707223128527403):
																if(x_velocity > -0.049005866050720215):
																	return True
												else:
													if(y_velocity <= -0.2551529258489609):
														return True
											else:
												if(lander_y <= 0.5494007766246796):
													if(angle_velocity <= 0.028564566746354103):
														if(angle <= -0.008791954722255468):
															if(lander_x <= 0.0940522663295269):
																if(angle <= -0.020844724029302597):
																	if(angle_velocity <= -0.011721173767000437):
																		if(x_velocity <= -0.03165749553591013):
																			return True
															else:
																if(angle <= -0.00977978901937604):
																	return True
												else:
													if(angle > -0.0006147521489765495):
														if(angle_velocity <= -0.01710554864257574):
															return True
										else:
											if(angle <= 0.0027327592251822352):
												if(angle_velocity <= -0.006165155675262213):
													if(lander_x <= -0.07699122466146946):
														if(x_velocity > 0.004193082917481661):
															if(angle_velocity <= -0.020906340330839157):
																if(y_velocity > -0.25711099803447723):
																	return True
													else:
														if(y_velocity <= -0.2523545101284981):
															if(lander_y > 0.5161055624485016):
																return True
														else:
															return True
												else:
													if(y_velocity > -0.24814879894256592):
														if(lander_x > -0.18955111503601074):
															if(lander_x <= 0.0545903705060482):
																if(lander_y <= 0.6457645297050476):
																	if(angle_velocity <= 0.012857219204306602):
																		if(x_velocity <= 0.006761582451872528):
																			return True
															else:
																return True
								else:
									if(angle <= 0.027446957305073738):
										if(angle_velocity <= 0.015449421480298042):
											if(x_velocity <= -0.05134405195713043):
												if(angle_velocity <= -0.01985674723982811):
													if(angle_velocity > -0.02292475476861):
														return True
											else:
												if(lander_y <= 0.519020140171051):
													if(lander_x <= -0.061965130269527435):
														if(angle <= -0.012045792769640684):
															if(x_velocity > 0.0061883446760475636):
																if(lander_x > -0.17679109424352646):
																	return True
														else:
															if(y_velocity > -0.2332426756620407):
																if(angle <= -0.007997591746971011):
																	return True
													else:
														if(angle <= 0.0022921893396414816):
															if(y_velocity <= -0.23914062976837158):
																if(angle_velocity <= -0.01008171821013093):
																	return True
															else:
																if(angle_velocity <= 0.011842083651572466):
																	return True
																else:
																	if(x_velocity > -0.013829858973622322):
																		return True
														else:
															if(x_velocity > -0.0018326767021790147):
																if(x_velocity <= 0.007200711057521403):
																	return True
												else:
													if(x_velocity <= 0.014209448359906673):
														if(lander_x <= 0.05866269953548908):
															if(angle <= -0.024396699853241444):
																return True
															else:
																if(x_velocity > 0.00514195254072547):
																	if(x_velocity <= 0.010421523824334145):
																		return True
														else:
															if(y_velocity <= -0.221526637673378):
																return True
													else:
														if(y_velocity > -0.23830954730510712):
															if(lander_y <= 0.6105600893497467):
																return True
															else:
																if(x_velocity <= 0.02576621249318123):
																	return True
										else:
											if(y_velocity <= -0.2299792394042015):
												if(x_velocity <= -0.011013717856258154):
													if(angle <= -0.05876550450921059):
														if(angle > -0.06508327648043633):
															return True
													else:
														if(lander_y > 0.4012627750635147):
															if(y_velocity <= -0.23913636058568954):
																if(y_velocity > -0.2392851710319519):
																	return True
												else:
													if(lander_x <= -0.028031492605805397):
														if(angle_velocity > 0.05883670784533024):
															return True
											else:
												if(angle <= -0.04651179164648056):
													if(angle > -0.05712807551026344):
														return True
												else:
													if(lander_y > 0.5853285491466522):
														if(lander_x > 0.00987095944583416):
															return True
									else:
										if(lander_y > 0.5512659549713135):
											if(lander_y <= 0.5924049317836761):
												if(lander_x <= 0.02894001081585884):
													return True
							else:
								if(y_velocity <= -0.254315048456192):
									if(lander_y <= 0.805266261100769):
										if(x_velocity <= -0.019964149221777916):
											if(y_velocity <= -0.2566714882850647):
												if(y_velocity <= -0.25739650428295135):
													if(angle <= -0.05967635475099087):
														return True
												else:
													return True
										else:
											if(y_velocity <= -0.25867871940135956):
												if(lander_y > 0.7090049088001251):
													return True
									else:
										if(y_velocity <= -0.25615353882312775):
											if(angle_velocity <= -0.015440585557371378):
												if(lander_y <= 0.825337827205658):
													return True
										else:
											if(lander_x <= 0.03419036790728569):
												if(lander_x <= 0.028237628750503063):
													if(x_velocity <= 0.022617443464696407):
														return True
													else:
														if(angle_velocity <= 0.003099274355918169):
															return True
								else:
									if(angle <= -0.02805306576192379):
										if(lander_y <= 0.7217203080654144):
											return True
										else:
											if(lander_y > 0.7736753225326538):
												if(angle > -0.04144858382642269):
													return True
									else:
										if(angle <= 0.00988092040643096):
											if(angle <= 0.008488973136991262):
												if(angle_velocity <= 0.018945268355309963):
													if(x_velocity > -0.05272674560546875):
														if(lander_x <= -0.008359670639038086):
															if(x_velocity <= 0.0004283926245989278):
																if(lander_x > -0.022936105728149414):
																	if(lander_y <= 1.0335189700126648):
																		return True
															else:
																if(lander_x > -0.12854037433862686):
																	if(lander_y > 0.7229493260383606):
																		return True
														else:
															return True
											else:
												return True
										else:
											if(lander_y > 0.6982258856296539):
												if(y_velocity <= -0.25035081803798676):
													if(lander_y > 0.8034637272357941):
														if(y_velocity > -0.25065740942955017):
															return True
												else:
													if(angle <= 0.01460183598101139):
														if(angle > 0.014256236143410206):
															return True
						else:
							if(lander_y <= 0.6493006646633148):
								if(angle_velocity <= -0.006822241935878992):
									if(x_velocity <= 0.05531732365489006):
										if(angle <= -0.011808109877165407):
											return True
										else:
											if(lander_x > 0.03598055802285671):
												return True
									else:
										if(angle <= 0.020863776095211506):
											return True
										else:
											if(y_velocity <= -0.22930432856082916):
												if(lander_x > -0.09005723148584366):
													if(angle <= 0.04609214700758457):
														return True
											else:
												if(angle_velocity > -0.029126125387847424):
													return True
								else:
									if(angle <= 0.013355567120015621):
										if(y_velocity <= -0.23322056233882904):
											if(angle_velocity <= 0.00859047519043088):
												if(x_velocity > 0.042379479855298996):
													if(y_velocity <= -0.2457507625222206):
														if(angle <= -0.005473450990393758):
															return True
													else:
														return True
											else:
												if(lander_x <= -0.3024490624666214):
													if(lander_y > 0.5087575167417526):
														return True
												else:
													if(lander_y > 0.6396333873271942):
														if(lander_x <= -0.13431158289313316):
															return True
										else:
											if(lander_y <= 0.5424078404903412):
												if(x_velocity <= 0.09163873642683029):
													if(x_velocity <= 0.04795690439641476):
														return True
													else:
														if(angle_velocity <= 0.0155371087603271):
															return True
												else:
													return True
											else:
												if(angle_velocity <= 0.02319413097575307):
													return True
									else:
										if(y_velocity <= -0.22986306250095367):
											if(angle_velocity <= -0.0014708756352774799):
												if(lander_x > -0.01130828820168972):
													return True
							else:
								if(angle <= 0.131209097802639):
									if(lander_y <= 0.7742876708507538):
										if(y_velocity <= -0.22755412012338638):
											if(angle_velocity <= -0.008942980319261551):
												if(angle <= 0.03935479559004307):
													return True
											else:
												if(angle <= 0.015457208268344402):
													if(angle_velocity <= 0.07502374239265919):
														if(y_velocity <= -0.24598274379968643):
															if(angle_velocity > 0.053720030933618546):
																return True
														else:
															if(lander_x <= -0.18042293190956116):
																if(lander_x <= -0.21004779636859894):
																	return True
															else:
																if(angle_velocity <= 0.04974053055047989):
																	return True
																else:
																	if(lander_y > 0.7130709290504456):
																		return True
												else:
													if(x_velocity > 0.046755023300647736):
														if(y_velocity <= -0.228505440056324):
															if(angle_velocity <= 0.0038729080697521567):
																if(angle <= 0.037339987233281136):
																	if(y_velocity > -0.2473110780119896):
																		return True
														else:
															return True
										else:
											if(angle_velocity <= 0.026497455313801765):
												if(lander_y <= 0.6824868023395538):
													return True
									else:
										if(y_velocity <= -0.24771227687597275):
											if(angle <= 0.02712376043200493):
												if(angle_velocity <= 0.044933730736374855):
													if(lander_y > 0.7800486981868744):
														return True
												else:
													if(lander_y > 0.8468361496925354):
														if(x_velocity > 0.042589107528328896):
															if(angle_velocity <= 0.08546962589025497):
																return True
											else:
												if(x_velocity > 0.06934664398431778):
													if(angle_velocity <= 0.013977652648463845):
														return True
													else:
														if(lander_y > 1.3851042985916138):
															return True
										else:
											if(lander_y <= 1.3818557262420654):
												if(angle_velocity <= 0.034344857558608055):
													if(lander_y <= 0.847799152135849):
														if(angle_velocity <= 0.014621262438595295):
															return True
													else:
														if(lander_x <= -0.04421668127179146):
															return True
														else:
															if(x_velocity > 0.06390602700412273):
																if(x_velocity > 0.06762076169252396):
																	if(lander_x <= 0.03119287546724081):
																		return True
												else:
													if(x_velocity <= 0.040507689118385315):
														if(angle <= -0.006548960052896291):
															return True
											else:
												if(x_velocity > 0.12040232121944427):
													return True
		else:
			if(angle_velocity <= -0.010854553431272507):
				if(right_leg_contact != True):
					if(angle <= 0.06201705522835255):
						if(angle_velocity <= -0.035603923723101616):
							if(x_velocity <= -0.049048325046896935):
								if(angle <= -0.018289437517523766):
									if(x_velocity > -0.3122575879096985):
										if(x_velocity <= -0.051378997042775154):
											if(x_velocity <= -0.09737235680222511):
												if(angle_velocity <= -0.06120913475751877):
													if(x_velocity <= -0.2234330028295517):
														if(angle_velocity <= -0.1633089929819107):
															if(lander_x <= -0.05506153218448162):
																return True
															else:
																if(angle_velocity <= -0.21268966794013977):
																	return True
														else:
															if(x_velocity <= -0.3115724176168442):
																return True
													else:
														return True
											else:
												if(y_velocity <= -0.217939130961895):
													if(y_velocity <= -0.218879796564579):
														return True
												else:
													return True
								else:
									if(y_velocity > -0.2162977084517479):
										if(lander_x <= 0.10602355003356934):
											if(lander_y <= 0.07603959739208221):
												if(x_velocity > -0.0640704408288002):
													return True
										else:
											if(lander_y > 0.011788675794377923):
												if(y_velocity <= -0.18697983026504517):
													return True
							else:
								if(angle_velocity <= -0.052182361483573914):
									if(angle <= 0.0359882228076458):
										if(lander_y <= 0.6568058431148529):
											if(lander_x <= 0.046082401648163795):
												return True
											else:
												if(lander_x > 0.046274567022919655):
													return True
										else:
											if(angle <= 0.009671386913396418):
												return True
									else:
										if(angle_velocity <= -0.06976191699504852):
											return True
										else:
											if(angle_velocity > -0.06222432106733322):
												if(x_velocity > 0.043531442526727915):
													if(angle <= 0.04994909465312958):
														return True
								else:
									if(lander_x <= -0.1753547191619873):
										if(y_velocity <= -0.2071043848991394):
											if(angle <= -0.0018436736281728372):
												if(lander_x > -0.19440116733312607):
													return True
										else:
											if(lander_y <= 0.31869086623191833):
												if(angle_velocity > -0.04627278633415699):
													return True
									else:
										if(x_velocity <= 0.02934814989566803):
											if(angle <= 0.024723194539546967):
												if(lander_x <= -0.07197494432330132):
													if(angle <= -0.01471952348947525):
														return True
													else:
														if(x_velocity > 0.007668731268495321):
															if(angle <= 0.011623566970229149):
																return True
												else:
													if(left_leg_contact != True):
														if(angle <= 0.01774296723306179):
															if(x_velocity <= -0.034288011491298676):
																if(angle_velocity > -0.045387158170342445):
																	if(lander_x <= 0.01595573453232646):
																		if(lander_y <= 0.08574990928173065):
																			return True
																	else:
																		return True
															else:
																return True
														else:
															if(lander_x > 0.05536680109798908):
																return True
											else:
												if(lander_y > 0.17466771602630615):
													if(lander_y <= 0.27532683312892914):
														return True
										else:
											if(angle <= 0.058603471145033836):
												if(lander_y <= 0.5580495595932007):
													if(y_velocity <= -0.1641298085451126):
														return True
						else:
							if(x_velocity <= 0.002305949805304408):
								if(lander_y <= 0.17234846204519272):
									if(y_velocity <= -0.1974310204386711):
										if(angle <= -0.0044709129724651575):
											if(lander_x > -0.16076922416687012):
												if(x_velocity > -0.07829222083091736):
													if(angle <= -0.021579984575510025):
														if(x_velocity > -0.07385072857141495):
															return True
													else:
														if(angle > -0.00968098221346736):
															return True
										else:
											if(lander_y > 0.09052756428718567):
												if(lander_x <= 0.025167417712509632):
													if(y_velocity > -0.2042122557759285):
														return True
												else:
													if(angle_velocity <= -0.020028371829539537):
														return True
									else:
										if(angle <= -0.0011818526545539498):
											if(x_velocity <= -0.04211076907813549):
												if(y_velocity > -0.18710999935865402):
													return True
											else:
												return True
								else:
									if(lander_x <= 0.07196741178631783):
										if(y_velocity <= -0.2186787948012352):
											return True
										else:
											if(angle_velocity <= -0.011381357908248901):
												if(y_velocity > -0.2059616968035698):
													if(y_velocity <= -0.20232993364334106):
														if(angle > -0.011455237166956067):
															if(x_velocity > -0.020496421959251165):
																return True
									else:
										if(x_velocity > -0.06836742162704468):
											return True
							else:
								if(lander_y <= 0.21626899391412735):
									if(y_velocity <= -0.18917064368724823):
										if(angle <= 0.005225776461884379):
											if(angle <= -0.010194838978350163):
												return True
											else:
												if(x_velocity <= 0.02813156321644783):
													if(lander_x > -0.048626137897372246):
														return True
												else:
													return True
										else:
											if(x_velocity <= 0.07935518398880959):
												if(lander_y <= 0.1443529948592186):
													if(angle <= 0.01576882740482688):
														if(angle <= 0.015076188370585442):
															if(lander_x > -0.02224073465913534):
																if(lander_x <= 0.0026698587462306023):
																	return True
														else:
															return True
												else:
													if(lander_x <= -0.027375363744795322):
														if(lander_y > 0.1602785587310791):
															if(y_velocity <= -0.21792226284742355):
																return True
													else:
														if(angle_velocity > -0.030583099462091923):
															return True
											else:
												return True
									else:
										if(lander_x <= -0.0855782963335514):
											if(x_velocity <= 0.05733836628496647):
												if(angle <= -0.003876910370308906):
													if(y_velocity <= -0.1745867356657982):
														return True
											else:
												if(angle_velocity > -0.023472610861063004):
													return True
										else:
											if(angle <= 0.045848630368709564):
												if(y_velocity <= -0.18624678254127502):
													if(lander_y > 0.11104568094015121):
														if(y_velocity <= -0.18801934272050858):
															return True
												else:
													if(lander_y <= 0.043340716511011124):
														if(lander_y <= 0.034660836681723595):
															return True
													else:
														return True
											else:
												if(y_velocity > -0.1697707325220108):
													if(x_velocity > 0.0822056233882904):
														return True
								else:
									if(lander_x <= -0.04364814795553684):
										if(x_velocity <= 0.061992842704057693):
											if(y_velocity <= -0.20960137993097305):
												if(angle <= 0.003252117079682648):
													return True
												else:
													if(lander_y > 0.4394170939922333):
														if(angle_velocity <= -0.0245559960603714):
															return True
											else:
												if(angle_velocity <= -0.01183604821562767):
													if(angle_velocity <= -0.023065774701535702):
														if(y_velocity <= -0.18910478800535202):
															if(angle_velocity > -0.03213549219071865):
																return True
												else:
													return True
										else:
											if(lander_x <= -0.18886275589466095):
												if(angle_velocity > -0.023781098425388336):
													return True
											else:
												return True
									else:
										if(x_velocity <= 0.010280539281666279):
											if(x_velocity <= 0.008855934720486403):
												if(y_velocity > -0.18366089463233948):
													return True
										else:
											if(lander_y <= 0.6267885267734528):
												if(y_velocity <= -0.21158729493618011):
													if(y_velocity <= -0.21374759823083878):
														return True
												else:
													return True
											else:
												if(angle <= 0.016695001628249884):
													return True
					else:
						if(y_velocity <= -0.17376063019037247):
							if(angle <= 0.0821714960038662):
								if(angle_velocity <= -0.041054217144846916):
									if(lander_x <= 0.11134877428412437):
										return True
								else:
									if(lander_x > -0.06110477261245251):
										if(x_velocity > 0.06728479266166687):
											return True
							else:
								if(x_velocity <= 0.1566612273454666):
									if(angle_velocity <= -0.11321457102894783):
										if(lander_y <= 1.1185217499732971):
											return True
										else:
											if(y_velocity <= -0.21329336613416672):
												if(lander_x > 0.16910595446825027):
													return True
									else:
										if(lander_y > 1.0543045401573181):
											if(lander_x <= 0.07900691032409668):
												if(y_velocity > -0.2166367694735527):
													return True
								else:
									if(angle_velocity <= -0.1363706737756729):
										if(angle <= 0.3233770728111267):
											if(y_velocity <= -0.18574092537164688):
												if(x_velocity <= 0.17242160439491272):
													if(lander_x > 0.21601442992687225):
														return True
												else:
													return True
						else:
							if(lander_y <= 0.32353532314300537):
								if(x_velocity <= 0.13265391439199448):
									if(y_velocity <= -0.16440926492214203):
										if(y_velocity > -0.17137716710567474):
											return True
								else:
									if(angle_velocity <= -0.033276102505624294):
										return True
									else:
										if(lander_y > 0.10371938720345497):
											return True
							else:
								if(angle_velocity <= -0.13533566892147064):
									if(x_velocity > 0.2214430645108223):
										return True
				else:
					if(x_velocity <= 0.09106511250138283):
						if(lander_y > 0.015181741677224636):
							if(angle_velocity <= -0.42805245518684387):
								return True
					else:
						if(angle_velocity <= -0.5140106678009033):
							return True
						else:
							if(angle <= -0.09820253774523735):
								return True
			else:
				if(lander_y <= 0.2456214353442192):
					if(y_velocity <= -0.18587703257799149):
						if(x_velocity <= 0.018928966484963894):
							if(y_velocity <= -0.20360344648361206):
								if(x_velocity <= -0.02664847020059824):
									if(left_leg_contact != True):
										if(angle_velocity <= 0.0043722393456846476):
											if(lander_x <= 0.06290278211236):
												if(angle <= -0.05439945496618748):
													if(angle > -0.07327098399400711):
														return True
											else:
												if(y_velocity > -0.21166489273309708):
													return True
								else:
									if(lander_y <= 0.18653695285320282):
										if(lander_x > -0.1305283084511757):
											if(lander_y > 0.0018440998392179608):
												if(angle_velocity <= -0.0051151760853827):
													if(lander_y > 0.12370817363262177):
														if(y_velocity <= -0.2048422396183014):
															return True
									else:
										if(lander_x > -0.03983144648373127):
											if(y_velocity > -0.21081820875406265):
												if(x_velocity <= 0.009407946839928627):
													if(angle_velocity <= 0.004333603545092046):
														return True
							else:
								if(angle_velocity <= -0.005452348385006189):
									if(angle <= -0.0012260186485946178):
										return True
									else:
										if(angle_velocity <= -0.009282009676098824):
											if(angle_velocity > -0.010182993952184916):
												return True
								else:
									if(lander_y > 0.004058173857629299):
										if(angle <= 0.019453133456408978):
											if(x_velocity <= 0.018647784367203712):
												if(x_velocity > -0.0010153257171623409):
													if(angle_velocity <= 0.013525543734431267):
														if(y_velocity <= -0.19654496759176254):
															if(angle <= -0.001700681183137931):
																return True
													else:
														if(lander_y > 0.010608843760564923):
															if(lander_x > 0.06910615041851997):
																if(angle <= 0.009757897583767772):
																	return True
											else:
												return True
						else:
							if(angle <= 0.010951127856969833):
								if(y_velocity <= -0.20143694430589676):
									if(angle <= -0.030738230794668198):
										if(angle_velocity <= 0.028853715397417545):
											return True
									else:
										if(angle_velocity <= -0.0014800538774579763):
											if(y_velocity <= -0.20968253910541534):
												if(angle_velocity > -0.006079734768718481):
													return True
											else:
												return True
										else:
											if(angle <= -0.014598495326936245):
												if(lander_x <= -0.11413297429680824):
													if(x_velocity > 0.08296073973178864):
														return True
												else:
													if(angle > -0.019936557859182358):
														return True
											else:
												if(x_velocity > 0.05898321233689785):
													if(x_velocity <= 0.06136663444340229):
														return True
								else:
									if(lander_y <= 0.1378457024693489):
										if(angle <= -0.010311076417565346):
											if(angle_velocity <= 0.029651219956576824):
												return True
										else:
											if(angle_velocity <= -0.004529626341536641):
												if(lander_x > -0.08064927905797958):
													return True
									else:
										if(y_velocity > -0.19555621594190598):
											if(lander_x <= -0.03502068482339382):
												if(x_velocity > 0.04528339020907879):
													return True
											else:
												return True
							else:
								if(right_leg_contact != True):
									if(lander_y <= 0.14798488467931747):
										if(lander_x <= -0.2437056079506874):
											if(y_velocity > -0.1990210860967636):
												return True
										else:
											if(lander_x > 0.06865129619836807):
												if(lander_x <= 0.07467718049883842):
													return True
									else:
										if(angle_velocity <= -0.0038335329154506326):
											if(lander_x > -0.1481214016675949):
												return True
										else:
											if(y_velocity > -0.20047180354595184):
												if(angle <= 0.0336521752178669):
													if(angle_velocity <= 0.030562994070351124):
														if(y_velocity > -0.19980782270431519):
															return True
					else:
						if(x_velocity <= 0.07906698435544968):
							if(left_leg_contact != True):
								if(x_velocity <= 0.05338051915168762):
									if(angle <= -0.010246748104691505):
										if(angle_velocity <= 0.02813830692321062):
											if(x_velocity > -0.0043573916191235185):
												return True
									else:
										if(lander_y <= 0.010773012414574623):
											if(lander_y > 0.004012576304376125):
												return True
										else:
											if(lander_x <= 0.1222846508026123):
												if(angle <= 0.048809004947543144):
													if(angle <= 0.006585653172805905):
														if(angle > 0.006035603350028396):
															return True
											else:
												if(x_velocity > -0.016186186112463474):
													return True
								else:
									if(y_velocity <= -0.17120373994112015):
										if(lander_x <= -0.03570122644305229):
											if(angle_velocity <= 0.018130283802747726):
												if(angle <= 0.033740317448973656):
													return True
											else:
												if(angle <= -0.011443637544289231):
													return True
										else:
											if(lander_y <= 0.16543927043676376):
												if(y_velocity > -0.1722951903939247):
													return True
											else:
												return True
									else:
										if(angle_velocity <= -0.0038011515280231833):
											if(y_velocity <= -0.15989500284194946):
												if(angle <= 0.0491067785769701):
													return True
						else:
							if(y_velocity <= -0.16376685351133347):
								if(angle_velocity <= -0.006967407651245594):
									return True
								else:
									if(angle_velocity <= 0.07804835960268974):
										if(lander_y <= 0.1487085074186325):
											if(lander_y > -0.005065127625130117):
												if(angle <= 0.049094974994659424):
													if(angle <= 0.046546122059226036):
														if(x_velocity > 0.09626342356204987):
															if(angle_velocity <= 0.04645492136478424):
																if(lander_x <= -0.06786765903234482):
																	return True
													else:
														return True
							else:
								if(x_velocity <= 0.08246087282896042):
									if(lander_y > 0.08970695361495018):
										return True
								else:
									if(x_velocity > 0.14585117995738983):
										if(y_velocity <= -0.1420469731092453):
											if(lander_y <= 0.04941176995635033):
												if(y_velocity > -0.14626598358154297):
													return True
											else:
												if(lander_y <= 0.07711452059447765):
													return True
												else:
													if(angle_velocity <= 0.02045962167903781):
														return True
				else:
					if(x_velocity <= 0.08962250128388405):
						if(y_velocity <= -0.2100314348936081):
							if(x_velocity <= 0.013507533818483353):
								if(angle_velocity <= -0.0003657425886558485):
									if(lander_x > -0.002429866697639227):
										if(lander_y > 0.2888552248477936):
											return True
								else:
									if(y_velocity <= -0.2182958945631981):
										if(lander_y <= 0.31259019672870636):
											if(angle <= -0.008802084950730205):
												if(lander_y > 0.27899427711963654):
													return True
										else:
											if(angle_velocity <= 0.003876933013089001):
												return True
											else:
												if(y_velocity > -0.21834351867437363):
													return True
									else:
										if(x_velocity > -0.0056305848993361):
											if(x_velocity <= -0.003742182394489646):
												return True
							else:
								if(lander_y <= 0.4193870723247528):
									if(angle <= -0.001474948861869052):
										if(angle > -0.016262791585177183):
											if(angle_velocity <= 0.04632934741675854):
												return True
									else:
										if(angle_velocity <= 0.0005050814943388104):
											if(x_velocity > 0.051337866112589836):
												return True
								else:
									if(lander_x <= 0.029781436547636986):
										if(y_velocity <= -0.21131696552038193):
											if(angle <= -0.01164768310263753):
												return True
										else:
											if(angle_velocity <= 0.028776037506759167):
												return True
											else:
												if(lander_y > 1.308901071548462):
													return True
									else:
										if(lander_y > 0.5562295019626617):
											if(lander_y <= 0.7017165124416351):
												return True
						else:
							if(x_velocity <= 0.07109396904706955):
								if(lander_y <= 0.3324655741453171):
									if(y_velocity <= -0.20063641667366028):
										if(angle <= 0.018269051797688007):
											if(lander_x > -0.041123056784272194):
												if(x_velocity <= 0.013495360501110554):
													if(angle_velocity <= 0.008620021399110556):
														if(angle <= -6.578245665878057e-05):
															return True
												else:
													if(lander_y <= 0.30388055741786957):
														if(lander_x > 0.07888107374310493):
															return True
													else:
														return True
									else:
										if(angle_velocity <= -0.00905592879280448):
											return True
										else:
											if(lander_x <= 0.08181328698992729):
												if(x_velocity <= 0.05668545141816139):
													if(y_velocity <= -0.19879302382469177):
														if(y_velocity > -0.19897308200597763):
															return True
												else:
													if(angle_velocity <= 0.028413920663297176):
														return True
								else:
									if(y_velocity <= -0.14808505773544312):
										if(lander_y <= 1.4096754789352417):
											if(x_velocity > 0.03250040113925934):
												if(x_velocity <= 0.03326038084924221):
													return True
												else:
													if(lander_y <= 1.0460107028484344):
														if(lander_y > 0.5858725905418396):
															if(lander_y <= 0.5930267870426178):
																return True
													else:
														return True
										else:
											if(x_velocity <= 0.03156116837635636):
												return True
									else:
										return True
							else:
								if(angle_velocity <= 0.007354301633313298):
									if(lander_x > -0.1750681847333908):
										return True
								else:
									if(lander_x > -0.08735213428735733):
										if(angle <= 0.05054444633424282):
											if(angle <= 0.04708305187523365):
												return True
					else:
						if(y_velocity <= -0.17320022732019424):
							if(x_velocity <= 0.3846900016069412):
								if(angle_velocity <= 0.08039089664816856):
									if(lander_y <= 0.4670753479003906):
										if(angle <= 0.05356734059751034):
											if(y_velocity <= -0.18619784712791443):
												if(lander_x <= -0.24747539311647415):
													if(angle_velocity <= 0.004820773145183921):
														return True
													else:
														if(lander_y > 0.43625740706920624):
															return True
												else:
													return True
											else:
												if(angle > 0.04843461699783802):
													return True
										else:
											if(x_velocity > 0.17527805268764496):
												if(angle_velocity <= 0.02628040115814656):
													return True
									else:
										if(x_velocity <= 0.26192905008792877):
											if(lander_y <= 0.6769025325775146):
												if(y_velocity <= -0.2017100751399994):
													if(angle <= 0.05155929550528526):
														if(angle_velocity <= 0.032015779055655):
															return True
											else:
												if(x_velocity <= 0.09086872637271881):
													return True
								else:
									if(lander_y <= 1.3846285939216614):
										if(y_velocity > -0.2153453752398491):
											if(y_velocity <= -0.20936059206724167):
												if(lander_y <= 0.5769548416137695):
													return True
									else:
										if(angle_velocity > 0.1266830489039421):
											if(x_velocity <= 0.224543996155262):
												if(lander_x <= 0.0231489185243845):
													return True
											else:
												return True
							else:
								if(angle <= 0.1528271809220314):
									return True
						else:
							if(x_velocity <= 0.5413434505462646):
								if(lander_y <= 1.4870757460594177):
									if(angle <= 0.0240612612105906):
										return True
									else:
										if(x_velocity <= 0.520891547203064):
											if(lander_y <= 1.4652548432350159):
												if(lander_x <= -0.25273650884628296):
													if(lander_x > -0.2589814364910126):
														return True
												else:
													if(y_velocity > -0.14577040076255798):
														if(angle <= 0.2433258295059204):
															return True
							else:
								if(lander_x <= 0.11860914528369904):
									return True
	else:
		if(y_velocity <= -0.00010637535888236016):
			if(angle <= 0.10152852162718773):
				if(lander_y <= 0.04580237716436386):
					if(angle_velocity <= 0.48136158287525177):
						if(right_leg_contact != True):
							if(angle_velocity <= 0.1452050693333149):
								if(y_velocity <= -0.00044665002496913075):
									if(lander_x > -0.16949333995580673):
										if(x_velocity > 0.11339053511619568):
											return True
				else:
					if(x_velocity <= 0.22380287945270538):
						if(angle <= 0.000588659371715039):
							if(y_velocity <= -0.09979284182190895):
								if(angle <= -0.00119297718629241):
									if(lander_y <= 1.450961410999298):
										return True
									else:
										if(lander_x <= -0.060761069878935814):
											return True
							else:
								if(x_velocity > 0.04741138778626919):
									if(angle <= -0.0013583254476543516):
										return True
						else:
							if(lander_x > 0.0010599136294331402):
								if(angle_velocity <= 0.16573119163513184):
									if(x_velocity <= 0.0771014615893364):
										if(lander_x <= 0.002822351409122348):
											return True
									else:
										return True
					else:
						return True
			else:
				if(x_velocity > -0.005076864268630743):
					if(x_velocity > -0.0014448040747083724):
						if(angle_velocity > 0.18233278393745422):
							if(lander_y > 1.4422094821929932):
								if(x_velocity > 0.40666310489177704):
									if(angle <= 0.19336441904306412):
										return True
									else:
										if(angle_velocity <= 0.2609146162867546):
											return True
		else:
			if(x_velocity <= 0.18656544387340546):
				if(lander_y > -0.044073011726140976):
					if(x_velocity > -0.29649674892425537):
						if(x_velocity > -0.13633117079734802):
							if(angle <= 0.3047634959220886):
								if(lander_y <= 1.454972743988037):
									if(x_velocity > 0.17811888456344604):
										if(lander_y > 0.705919228726998):
											return True
								else:
									if(lander_y <= 1.4570536017417908):
										if(x_velocity > -0.014905132353305817):
											return True
									else:
										if(y_velocity <= 0.011451031547039747):
											return True
			else:
				if(x_velocity <= 0.44430138170719147):
					if(lander_y <= 1.4766086339950562):
						if(x_velocity <= 0.23011696338653564):
							return True
						else:
							if(x_velocity <= 0.27121466398239136):
								if(angle_velocity <= 0.09294815734028816):
									if(angle <= -0.0002486870507709682):
										if(x_velocity <= 0.26243607699871063):
											if(y_velocity > 0.2615943029522896):
												return True
									else:
										return True
							else:
								return True
				else:
					return True
	return False

def weShould_main_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.13701249659061432):
		if(y_velocity <= -0.220126174390316):
			if(angle_velocity <= -0.030239202082157135):
				if(angle <= 0.19462168961763382):
					if(lander_y <= 1.3413802981376648):
						if(y_velocity <= -0.2712501585483551):
							if(angle <= 0.061055488884449005):
								if(y_velocity <= -0.47413963079452515):
									if(x_velocity <= -0.5935395658016205):
										if(y_velocity <= -0.5741690397262573):
											return True
									else:
										if(angle <= -0.28904587030410767):
											if(y_velocity <= -0.5010827481746674):
												if(y_velocity <= -0.5407353937625885):
													return True
												else:
													if(lander_y <= 1.07346510887146):
														if(angle_velocity <= -0.05043032579123974):
															if(lander_y > 1.035538136959076):
																if(angle_velocity > -0.19462913274765015):
																	return True
														else:
															return True
													else:
														return True
											else:
												if(y_velocity > -0.4779440760612488):
													return True
										else:
											if(angle <= -0.03099391609430313):
												if(lander_x <= -0.14950332790613174):
													if(lander_x <= -0.1533764824271202):
														if(angle_velocity <= -0.26971299946308136):
															if(x_velocity <= -0.5262067019939423):
																return True
														else:
															return True
												else:
													if(angle <= -0.06514751352369785):
														return True
													else:
														if(angle > -0.06125149503350258):
															if(y_velocity <= -0.498701810836792):
																return True
															else:
																if(x_velocity > -0.47367043793201447):
																	return True
											else:
												if(y_velocity <= -0.5455013811588287):
													if(x_velocity > -0.5699999332427979):
														if(x_velocity <= -0.5565437078475952):
															if(lander_y > 1.3011165261268616):
																return True
														else:
															return True
								else:
									if(angle_velocity <= -0.08699863031506538):
										if(y_velocity <= -0.342959463596344):
											if(angle <= -0.18322286009788513):
												if(x_velocity <= -0.5325293242931366):
													return True
												else:
													if(lander_y <= 1.0766575336456299):
														if(x_velocity <= -0.4057718515396118):
															if(y_velocity <= -0.4388863295316696):
																if(lander_x <= -0.1599287986755371):
																	if(y_velocity > -0.4611012190580368):
																		return True
																else:
																	return True
														else:
															if(angle_velocity > -0.10576049610972404):
																return True
											else:
												if(x_velocity <= -0.4903474748134613):
													if(angle_velocity <= -0.3599099814891815):
														return True
												else:
													if(angle_velocity <= -0.32994210720062256):
														if(angle <= 0.017730834893882275):
															if(x_velocity <= -0.486134335398674):
																return True
															else:
																if(angle_velocity <= -0.3343295305967331):
																	if(lander_y <= 0.9598945379257202):
																		if(angle_velocity <= -0.3922143280506134):
																			return True
														else:
															if(lander_x <= 0.23512211441993713):
																return True
															else:
																if(y_velocity <= -0.3725551664829254):
																	return True
													else:
														if(y_velocity <= -0.4216584116220474):
															if(lander_y <= 0.8977401554584503):
																if(angle_velocity > -0.2290351763367653):
																	return True
															else:
																if(x_velocity <= -0.30474819242954254):
																	if(x_velocity <= -0.473934605717659):
																		if(lander_y <= 1.1218289136886597):
																			return True
																	else:
																		return True
																else:
																	if(lander_y <= 1.271756112575531):
																		if(angle_velocity > -0.11983776837587357):
																			return True
																	else:
																		return True
														else:
															if(angle <= -0.09334746748209):
																if(lander_y <= 0.8961840569972992):
																	return True
																else:
																	if(x_velocity > -0.4140353798866272):
																		if(angle <= -0.11283218860626221):
																			if(x_velocity <= -0.3804764300584793):
																				if(lander_x <= 0.18944025039672852):
																					return True
																		else:
																			if(angle_velocity > -0.12647632881999016):
																				return True
															else:
																if(x_velocity <= -0.1488664746284485):
																	if(angle_velocity <= -0.25299203395843506):
																		if(y_velocity <= -0.3954121917486191):
																			if(lander_x > -0.05110583454370499):
																				return True
																		else:
																			if(angle > 0.014111994300037622):
																				return True
																	else:
																		if(x_velocity <= -0.2530298978090286):
																			if(y_velocity <= -0.3705414682626724):
																				if(x_velocity <= -0.3272215723991394):
																					if(angle_velocity <= -0.24009552597999573):
																						return True
																				else:
																					return True
																			else:
																				if(lander_x > 0.1948225498199463):
																					if(y_velocity <= -0.3451025038957596):
																						return True
																		else:
																			if(lander_y <= 1.3227459788322449):
																				return True
																			else:
																				if(lander_y > 1.3251177668571472):
																					return True
										else:
											if(y_velocity <= -0.28863246738910675):
												if(angle <= 0.005772620206698775):
													if(lander_y <= 1.3169233798980713):
														if(lander_y <= 0.8466216921806335):
															if(lander_y > 0.793368399143219):
																if(x_velocity <= -0.21715107560157776):
																	if(x_velocity <= -0.22931460291147232):
																		if(y_velocity > -0.31617462635040283):
																			if(lander_y > 0.8036152422428131):
																				return True
																	else:
																		return True
														else:
															if(angle_velocity > -0.09502262994647026):
																if(angle_velocity <= -0.09259713813662529):
																	return True
												else:
													if(angle_velocity <= -0.11864189431071281):
														if(angle <= 0.050486838445067406):
															if(lander_y <= 0.7911439538002014):
																return True
														else:
															if(lander_y <= 1.0645220875740051):
																return True
													else:
														if(lander_x > 0.04182085837237537):
															if(y_velocity <= -0.2934129238128662):
																return True
															else:
																if(lander_y <= 1.0263058245182037):
																	return True
									else:
										if(y_velocity <= -0.29542168974876404):
											if(angle <= -0.07191513851284981):
												if(y_velocity <= -0.34861670434474945):
													if(y_velocity <= -0.44248321652412415):
														if(y_velocity > -0.4702040106058121):
															return True
													else:
														if(angle > -0.22638513892889023):
															if(x_velocity <= -0.15816737711429596):
																if(angle <= -0.12100015580654144):
																	if(y_velocity <= -0.4032207280397415):
																		if(y_velocity <= -0.42613089084625244):
																			if(y_velocity <= -0.43078747391700745):
																				return True
																		else:
																			return True
																	else:
																		if(y_velocity <= -0.38404443860054016):
																			if(y_velocity <= -0.3966951072216034):
																				if(y_velocity > -0.4016437828540802):
																					return True
																		else:
																			if(angle <= -0.15946373343467712):
																				if(angle <= -0.19899845123291016):
																					if(y_velocity <= -0.37981468439102173):
																						return True
																				else:
																					if(angle > -0.16517337411642075):
																						if(angle <= -0.16229700297117233):
																							return True
																			else:
																				if(y_velocity <= -0.3745879828929901):
																					return True
																				else:
																					if(lander_x > 0.13403596729040146):
																						return True
																else:
																	return True
															else:
																if(y_velocity <= -0.36866995692253113):
																	return True
												else:
													if(lander_x > 0.14664892852306366):
														if(x_velocity <= -0.20580187439918518):
															if(lander_x <= 0.15389323234558105):
																if(angle > -0.10972855612635612):
																	return True
														else:
															return True
											else:
												if(lander_x <= -0.007135295774787664):
													if(y_velocity <= -0.321407288312912):
														if(lander_x <= -0.031374311074614525):
															if(angle_velocity <= -0.053911035880446434):
																if(y_velocity <= -0.42186667025089264):
																	return True
															else:
																return True
														else:
															if(x_velocity > -0.28811974823474884):
																if(y_velocity <= -0.33403821289539337):
																	return True
																else:
																	if(lander_x > -0.020509767811745405):
																		return True
													else:
														if(lander_y <= 0.8598849773406982):
															return True
														else:
															if(angle <= -0.005697358166798949):
																if(x_velocity <= -0.08528625592589378):
																	if(angle_velocity > -0.05914578586816788):
																		return True
															else:
																if(x_velocity <= -0.04308090731501579):
																	if(lander_y <= 1.1663776636123657):
																		return True
																else:
																	return True
												else:
													if(lander_y <= 1.2945742011070251):
														if(angle <= -0.03646194934844971):
															if(y_velocity <= -0.31038226187229156):
																if(angle_velocity <= -0.07628023251891136):
																	if(angle_velocity <= -0.0856061577796936):
																		return True
																else:
																	return True
															else:
																if(x_velocity > -0.1803419589996338):
																	if(lander_y <= 0.7398872971534729):
																		if(angle_velocity > -0.06400062888860703):
																			return True
														else:
															if(x_velocity <= -0.15120955556631088):
																if(y_velocity <= -0.3107106536626816):
																	return True
															else:
																if(lander_y <= 0.8536113202571869):
																	if(lander_y <= 0.8424327373504639):
																		return True
																else:
																	if(y_velocity <= -0.2977818697690964):
																		return True
																	else:
																		if(y_velocity > -0.2975992411375046):
																			return True
													else:
														if(y_velocity <= -0.32024289667606354):
															return True
										else:
											if(lander_y <= 0.6564100086688995):
												if(angle <= -0.023787091486155987):
													if(lander_y <= 0.4388291835784912):
														return True
													else:
														if(lander_y > 0.6390377581119537):
															return True
												else:
													if(angle_velocity <= -0.06376543268561363):
														if(lander_x > -0.006406688829883933):
															return True
													else:
														return True
											else:
												if(angle <= 0.004643378080800176):
													if(x_velocity > -0.1016995906829834):
														if(angle_velocity <= -0.038199782371520996):
															if(y_velocity <= -0.29217106103897095):
																if(angle_velocity > -0.05975296162068844):
																	return True
															else:
																if(angle <= 0.002516412700060755):
																	if(lander_x <= -0.034493875689804554):
																		if(angle > -0.011263435240834951):
																			return True
																else:
																	if(lander_y <= 0.7866464257240295):
																		return True
														else:
															if(lander_y <= 0.7516250014305115):
																return True
															else:
																if(angle > -0.012499293312430382):
																	if(x_velocity <= -0.030099776573479176):
																		if(lander_y <= 0.8385136127471924):
																			if(y_velocity > -0.28446145355701447):
																				return True
																		else:
																			return True
																	else:
																		if(x_velocity > -0.02367000002413988):
																			return True
												else:
													if(lander_y <= 0.9250941276550293):
														if(x_velocity <= 0.016601918265223503):
															if(x_velocity <= -0.0030559178558178246):
																return True
															else:
																if(lander_x <= -0.021962451981380582):
																	return True
													else:
														if(x_velocity > -0.08201296627521515):
															if(lander_y <= 1.0987120866775513):
																if(angle_velocity <= -0.046588145196437836):
																	if(x_velocity <= -0.034358756616711617):
																		if(angle_velocity <= -0.053634967654943466):
																			if(y_velocity <= -0.2848924994468689):
																				return True
																			else:
																				if(angle > 0.025381755083799362):
																					if(angle_velocity > -0.07505744695663452):
																						return True
																else:
																	if(lander_x <= 0.12578401528298855):
																		return True
							else:
								if(angle_velocity <= -0.09253112599253654):
									if(angle_velocity <= -0.42367124557495117):
										if(y_velocity <= -0.33871832489967346):
											return True
										else:
											if(lander_x > 0.253693625330925):
												if(angle > 0.1764698028564453):
													return True
									else:
										if(angle <= 0.11447752267122269):
											if(lander_y <= 1.1623373627662659):
												if(angle <= 0.07942209392786026):
													if(angle <= 0.07822135090827942):
														if(lander_x <= 0.12662281841039658):
															if(y_velocity > -0.28110910952091217):
																return True
														else:
															if(x_velocity <= -0.2300647795200348):
																if(y_velocity <= -0.3441176563501358):
																	return True
															else:
																return True
												else:
													if(angle <= 0.10782143846154213):
														return True
											else:
												if(y_velocity <= -0.29660703241825104):
													return True
										else:
											if(lander_x <= 0.24194559454917908):
												return True
											else:
												if(x_velocity <= -0.07774129137396812):
													return True
								else:
									if(x_velocity > -0.08083246648311615):
										if(lander_x <= 0.04924569092690945):
											if(lander_x <= 0.048288917168974876):
												return True
										else:
											return True
						else:
							if(lander_y <= 0.2888483852148056):
								if(angle_velocity <= -0.06200191378593445):
									if(y_velocity <= -0.2447967603802681):
										if(lander_y <= 0.14572245627641678):
											return True
										else:
											if(x_velocity > -0.028530413284897804):
												return True
									else:
										if(angle > 0.017069307155907154):
											return True
								else:
									if(y_velocity <= -0.22887907177209854):
										if(y_velocity <= -0.24936990439891815):
											return True
										else:
											if(angle <= -0.05136376619338989):
												if(lander_x <= -0.1559777781367302):
													if(lander_y > 0.04192422516644001):
														return True
											else:
												if(lander_y <= 0.21508169919252396):
													if(angle <= -0.018539821729063988):
														if(x_velocity <= -0.04069283977150917):
															if(lander_x <= 0.09661459922790527):
																return True
															else:
																if(angle <= -0.02323413360863924):
																	if(lander_y <= 0.11525148898363113):
																		return True
																else:
																	return True
														else:
															if(y_velocity <= -0.23400668799877167):
																if(angle_velocity > -0.050589609891176224):
																	return True
													else:
														return True
												else:
													if(angle <= 0.007701106835156679):
														if(angle_velocity <= -0.03694206476211548):
															if(y_velocity > -0.2376723289489746):
																if(y_velocity <= -0.23474687337875366):
																	return True
														else:
															if(x_velocity <= -0.008021642453968525):
																return True
													else:
														return True
									else:
										if(angle <= -0.01896038744598627):
											if(lander_x > -0.192253015935421):
												if(lander_y <= 0.22453942149877548):
													if(lander_y <= 0.03258487954735756):
														if(x_velocity > -0.09634300321340561):
															return True
										else:
											if(angle <= 0.008450696244835854):
												if(lander_y <= 0.1256880760192871):
													if(angle_velocity <= -0.036593127995729446):
														return True
													else:
														if(angle > -0.014632944948971272):
															return True
												else:
													if(x_velocity <= -0.01630639098584652):
														if(lander_x <= 0.044598388485610485):
															return True
											else:
												return True
							else:
								if(angle <= -0.004452327499166131):
									if(angle_velocity <= -0.04128412716090679):
										if(y_velocity <= -0.2575591802597046):
											if(y_velocity <= -0.2603725492954254):
												if(x_velocity <= -0.0782817117869854):
													if(lander_y <= 0.576561838388443):
														if(angle > -0.035669573582708836):
															return True
											else:
												if(x_velocity > -0.05547204613685608):
													return True
									else:
										if(x_velocity > -0.09462021663784981):
											if(lander_y <= 0.4283932000398636):
												if(y_velocity <= -0.23456428200006485):
													if(angle <= -0.011457640212029219):
														if(x_velocity <= -0.015013983007520437):
															if(x_velocity > -0.0848516970872879):
																if(y_velocity <= -0.23807018995285034):
																	if(lander_y > 0.34453655779361725):
																		if(lander_x <= 0.11262926831841469):
																			return True
													else:
														return True
											else:
												if(angle_velocity <= -0.04054407589137554):
													if(lander_y <= 0.4673583507537842):
														return True
												else:
													if(lander_x <= -0.2634451389312744):
														return True
													else:
														if(y_velocity <= -0.2645799368619919):
															if(y_velocity > -0.26575031876564026):
																return True
								else:
									if(lander_y <= 0.5517165660858154):
										if(y_velocity <= -0.24928557872772217):
											if(angle <= 0.0003672398524940945):
												if(x_velocity > -0.026792760007083416):
													return True
											else:
												return True
										else:
											if(angle_velocity <= -0.056966641917824745):
												if(lander_x <= -0.20418450981378555):
													return True
												else:
													if(x_velocity <= -0.03333435021340847):
														if(angle_velocity > -0.09238193556666374):
															return True
													else:
														if(lander_x <= -0.10655899345874786):
															if(x_velocity <= -0.0034981155768036842):
																return True
											else:
												if(y_velocity <= -0.23306214064359665):
													if(angle <= 0.0028039898024871945):
														if(lander_y > 0.461465984582901):
															return True
													else:
														if(angle_velocity <= -0.03815866634249687):
															if(angle_velocity <= -0.03934674896299839):
																if(x_velocity <= 0.07032981887459755):
																	if(y_velocity <= -0.2391762062907219):
																		return True
																	else:
																		if(x_velocity <= 0.034316143952310085):
																			if(y_velocity > -0.2384628802537918):
																				return True
														else:
															return True
												else:
													if(x_velocity > -0.024672605097293854):
														if(x_velocity <= 0.03441648930311203):
															if(y_velocity <= -0.22759557515382767):
																if(y_velocity <= -0.2315051183104515):
																	return True
															else:
																return True
														else:
															if(lander_x <= -0.19954264163970947):
																return True
									else:
										if(x_velocity <= -0.0434639286249876):
											if(lander_x <= 0.12592416256666183):
												if(lander_y <= 0.6986694633960724):
													if(angle > -5.954792140983045e-05):
														return True
											else:
												if(y_velocity <= -0.24674434214830399):
													if(x_velocity <= -0.06307151541113853):
														if(angle <= 0.17386354506015778):
															if(angle_velocity > -0.04279521852731705):
																if(angle <= 0.014630157500505447):
																	return True
														else:
															return True
													else:
														if(y_velocity <= -0.26617731153964996):
															return True
										else:
											if(angle <= 0.051375413313508034):
												if(angle_velocity <= -0.03644077107310295):
													if(x_velocity <= 0.0021949945949018):
														if(angle_velocity <= -0.05742747709155083):
															if(angle <= -0.001935446955030784):
																return True
														else:
															if(lander_y <= 0.7053986489772797):
																if(angle > 0.01381576550193131):
																	return True
												else:
													if(y_velocity <= -0.25737951695919037):
														if(x_velocity <= 0.005887146107852459):
															return True
														else:
															if(x_velocity > 0.02421198459342122):
																return True
													else:
														if(lander_x <= 0.030249882489442825):
															if(angle > 0.032342150807380676):
																if(angle <= 0.03969847038388252):
																	return True
											else:
												if(y_velocity <= -0.25443829596042633):
													if(angle <= 0.10417304188013077):
														if(angle_velocity > -0.08819719403982162):
															if(x_velocity <= 0.003025089274160564):
																if(lander_y <= 1.0567522048950195):
																	if(angle > 0.0741884894669056):
																		return True
															else:
																if(y_velocity <= -0.267055481672287):
																	return True
																else:
																	if(angle <= 0.0846092477440834):
																		if(x_velocity <= 0.009261439554393291):
																			if(y_velocity > -0.265315979719162):
																				return True
																	else:
																		if(lander_y <= 1.2405642867088318):
																			return True
													else:
														if(lander_x <= 0.09951886907219887):
															if(angle_velocity > -0.06006043031811714):
																return True
														else:
															if(angle_velocity <= -0.11974053084850311):
																if(angle > 0.1628476306796074):
																	return True
															else:
																return True
												else:
													if(angle_velocity <= -0.09558995440602303):
														if(y_velocity <= -0.22947585582733154):
															if(angle_velocity > -0.13757845014333725):
																if(angle > 0.11318513751029968):
																	if(x_velocity > 0.017923153936862946):
																		if(y_velocity <= -0.24464258551597595):
																			if(angle <= 0.1373646855354309):
																				if(lander_y <= 0.9796440303325653):
																					return True
																			else:
																				return True
																		else:
																			if(angle_velocity <= -0.13193659484386444):
																				return True
													else:
														if(x_velocity <= 0.025266282260417938):
															if(lander_y > 0.8956425487995148):
																if(lander_y <= 0.9250913858413696):
																	if(lander_x > 0.1451617255806923):
																		return True
														else:
															if(angle <= 0.12195507436990738):
																if(lander_x <= -0.014197825454175472):
																	return True
															else:
																if(x_velocity <= 0.08360905200242996):
																	if(y_velocity <= -0.24660468101501465):
																		if(lander_y <= 1.2066875100135803):
																			return True
																	else:
																		if(lander_y <= 1.0585106313228607):
																			if(lander_x <= 0.14338817447423935):
																				return True
																else:
																	if(lander_y <= 1.2113174200057983):
																		return True
																	else:
																		if(y_velocity <= -0.24811803549528122):
																			return True
					else:
						if(x_velocity <= -0.32714836299419403):
							if(y_velocity <= -0.4239038676023483):
								if(angle <= 0.010263814125210047):
									if(lander_y > 1.3426799178123474):
										return True
						else:
							if(angle <= -0.004083811771124601):
								if(y_velocity <= -0.3513885885477066):
									if(lander_y <= 1.373328447341919):
										if(lander_x <= -0.020254516042768955):
											if(lander_y > 1.3663036227226257):
												if(x_velocity > -0.3185473084449768):
													return True
										else:
											return True
							else:
								if(y_velocity <= -0.24147136509418488):
									return True
				else:
					if(angle <= 0.2628934383392334):
						if(lander_y > 0.7854368686676025):
							if(lander_x <= 0.1162346825003624):
								if(x_velocity > 0.1752893328666687):
									return True
							else:
								if(x_velocity <= -0.18661167472600937):
									if(y_velocity <= -0.3029929995536804):
										return True
									else:
										if(lander_x <= 0.22991995513439178):
											return True
								else:
									if(y_velocity <= -0.23782780021429062):
										return True
									else:
										if(angle_velocity <= -0.17055439203977585):
											if(y_velocity > -0.2292066365480423):
												return True
										else:
											return True
					else:
						if(y_velocity <= -0.29137198626995087):
							if(x_velocity <= -0.0018345066928304732):
								if(angle_velocity <= -0.19024939090013504):
									if(lander_y <= 1.1114172339439392):
										if(x_velocity > -0.2529485374689102):
											if(lander_x <= 0.2829801142215729):
												return True
											else:
												if(y_velocity <= -0.34217211604118347):
													return True
									else:
										if(y_velocity <= -0.3132486641407013):
											if(x_velocity <= -0.08621768280863762):
												if(angle_velocity <= -0.3131147474050522):
													if(lander_y > 1.116659939289093):
														if(y_velocity <= -0.32104529440402985):
															return True
											else:
												return True
										else:
											if(x_velocity > -0.014863400720059872):
												return True
							else:
								if(lander_x <= 0.29769958555698395):
									return True
								else:
									if(lander_y <= 1.1944284439086914):
										return True
						else:
							if(angle <= 0.33221641182899475):
								if(x_velocity > -0.11266310513019562):
									if(angle <= 0.284756600856781):
										if(x_velocity > 0.10586587339639664):
											return True
									else:
										return True
							else:
								if(x_velocity > 0.010269048856571317):
									if(lander_y <= 1.0403451323509216):
										if(y_velocity <= -0.257622167468071):
											if(angle <= 0.5124571323394775):
												return True
										else:
											if(x_velocity > 0.12006763368844986):
												return True
									else:
										if(x_velocity > 0.18458912521600723):
											return True
			else:
				if(lander_y <= 0.3988706022500992):
					if(angle_velocity <= -0.005895595299080014):
						if(y_velocity <= -0.23697848618030548):
							if(angle <= -0.03992721438407898):
								if(lander_y <= 0.174763984978199):
									if(y_velocity <= -0.2448679730296135):
										return True
									else:
										if(lander_x > 0.024794816970825195):
											return True
								else:
									if(y_velocity <= -0.2558140754699707):
										if(angle_velocity <= -0.018434702418744564):
											if(lander_x <= -0.05044736934360117):
												return True
										else:
											return True
							else:
								if(lander_y <= 0.3966212570667267):
									if(lander_y <= 0.29461008310317993):
										return True
									else:
										if(lander_y > 0.29696352779865265):
											if(lander_x <= -0.032745121978223324):
												return True
											else:
												if(lander_x <= -0.0028357982664601877):
													if(angle_velocity > -0.0138159841299057):
														return True
												else:
													return True
						else:
							if(angle <= -0.025198427960276604):
								if(x_velocity > -0.08618466928601265):
									if(angle_velocity <= -0.027504215016961098):
										return True
									else:
										if(x_velocity <= -0.03842702694237232):
											if(lander_y <= 0.29612164199352264):
												if(y_velocity <= -0.22554226964712143):
													if(lander_y <= 0.026572690345346928):
														if(x_velocity <= -0.06104778125882149):
															return True
												else:
													return True
							else:
								if(lander_y <= 0.20550113171339035):
									if(x_velocity <= -0.06678585708141327):
										if(angle <= -0.017246378120034933):
											return True
									else:
										if(angle <= -0.019534876570105553):
											if(lander_y <= 0.08102371357381344):
												return True
										else:
											return True
								else:
									if(lander_x <= -0.10965194553136826):
										if(angle <= -0.010702112689614296):
											if(lander_y <= 0.3300902396440506):
												return True
										else:
											return True
									else:
										if(angle <= 0.013557164464145899):
											if(angle_velocity <= -0.007875385228544474):
												if(angle <= -0.004473929526284337):
													if(angle_velocity <= -0.02599407359957695):
														return True
													else:
														if(x_velocity <= -0.06300520338118076):
															return True
												else:
													if(x_velocity <= 0.0025092814466916025):
														if(x_velocity > -0.0267856540158391):
															return True
													else:
														if(angle_velocity <= -0.009860043413937092):
															if(lander_y <= 0.22057675570249557):
																return True
														else:
															return True
										else:
											if(x_velocity <= 0.042379504069685936):
												if(lander_y <= 0.3628438115119934):
													return True
												else:
													if(lander_x <= 0.03796401061117649):
														return True
					else:
						if(angle_velocity <= 0.1071605421602726):
							if(angle <= -0.007234708871692419):
								if(y_velocity <= -0.23764991760253906):
									if(x_velocity <= -0.13719099014997482):
										if(angle <= -0.09720682725310326):
											return True
									else:
										if(angle <= -0.06476367264986038):
											if(y_velocity <= -0.2619546800851822):
												return True
											else:
												if(angle_velocity <= 0.03959674946963787):
													if(lander_y <= 0.30810460448265076):
														if(x_velocity <= -0.0584693793207407):
															if(lander_y <= 0.2459413707256317):
																return True
															else:
																if(lander_y > 0.26593248546123505):
																	return True
										else:
											if(y_velocity <= -0.2452927529811859):
												return True
											else:
												if(lander_y <= 0.2798342704772949):
													return True
												else:
													if(x_velocity <= -0.0206613726913929):
														if(x_velocity <= -0.03133177664130926):
															if(lander_y > 0.2984888553619385):
																if(x_velocity > -0.06447276473045349):
																	return True
													else:
														if(x_velocity <= 0.03322521224617958):
															return True
								else:
									if(lander_y <= 0.26747365295886993):
										if(x_velocity <= -0.0627112053334713):
											if(lander_y <= 0.14145410060882568):
												if(lander_x <= -0.028346871957182884):
													if(y_velocity > -0.22304968535900116):
														return True
												else:
													if(angle > -0.05757788009941578):
														if(angle_velocity > -0.002111430570948869):
															return True
											else:
												if(lander_x > 0.11924776807427406):
													return True
										else:
											if(angle_velocity <= 0.005520625039935112):
												if(angle_velocity <= 0.003953332896344364):
													if(x_velocity <= 0.026511111296713352):
														if(angle_velocity <= -0.00425525032915175):
															if(angle_velocity <= -0.00488924328237772):
																return True
														else:
															return True
												else:
													if(angle <= -0.04426326975226402):
														return True
											else:
												if(x_velocity <= -0.05737740360200405):
													if(y_velocity > -0.23243707418441772):
														return True
												else:
													return True
									else:
										if(lander_x <= -0.08530726283788681):
											if(x_velocity <= 0.024723042268306017):
												if(lander_y <= 0.2900426834821701):
													if(lander_y > 0.27483803033828735):
														return True
										else:
											if(angle_velocity > 0.001189333685033489):
												if(x_velocity <= -0.009728663600981236):
													if(y_velocity <= -0.23149458318948746):
														if(lander_y > 0.315429225564003):
															if(angle <= -0.008066202979534864):
																return True
												else:
													if(lander_x <= -0.009571123402565718):
														if(x_velocity <= 0.023265737108886242):
															return True
														else:
															if(angle_velocity > 0.0569342914968729):
																return True
													else:
														if(angle_velocity > 0.05781659111380577):
															return True
							else:
								if(x_velocity <= -0.05363779328763485):
									if(lander_x > 0.05827446095645428):
										return True
								else:
									if(y_velocity <= -0.22065309435129166):
										if(y_velocity <= -0.2258555367588997):
											return True
										else:
											if(y_velocity > -0.22582001984119415):
												if(x_velocity <= -0.00616769096814096):
													if(lander_x > -0.043342018499970436):
														return True
												else:
													return True
									else:
										if(y_velocity > -0.22063478827476501):
											return True
						else:
							if(lander_y <= 0.3933049440383911):
								if(x_velocity <= -0.06872013211250305):
									return True
							else:
								return True
				else:
					if(y_velocity <= -0.2591031938791275):
						if(x_velocity <= -0.4677737355232239):
							if(y_velocity <= -0.6010503172874451):
								return True
						else:
							if(angle <= -0.05331459268927574):
								if(y_velocity <= -0.28979015350341797):
									if(y_velocity <= -0.32377180457115173):
										if(lander_y <= 1.0612746477127075):
											if(angle <= -0.20151109993457794):
												if(y_velocity <= -0.3569426089525223):
													if(angle_velocity <= 0.03919844701886177):
														if(y_velocity <= -0.40547867119312286):
															if(lander_x <= -0.24282576888799667):
																if(angle_velocity > 0.033268094062805176):
																	return True
															else:
																if(y_velocity <= -0.4243869483470917):
																	return True
																else:
																	if(angle <= -0.2885611355304718):
																		return True
																	else:
																		if(angle > -0.2438676431775093):
																			return True
													else:
														if(y_velocity <= -0.3872532546520233):
															if(angle <= -0.3148250877857208):
																if(y_velocity <= -0.461546927690506):
																	if(angle_velocity > 0.05595002695918083):
																		if(x_velocity <= -0.28484678268432617):
																			return True
																		else:
																			if(angle_velocity > 0.10261939838528633):
																				return True
															else:
																if(lander_y <= 1.037104070186615):
																	if(x_velocity <= -0.31900712847709656):
																		if(y_velocity <= -0.4142201989889145):
																			return True
																	else:
																		if(x_velocity <= -0.09326792880892754):
																			return True
																		else:
																			if(x_velocity > -0.08039824664592743):
																				return True
																else:
																	if(angle <= -0.3008088916540146):
																		return True
														else:
															if(angle <= -0.23443743586540222):
																if(lander_x <= -0.23447678238153458):
																	if(y_velocity <= -0.36935967206954956):
																		if(angle_velocity > 0.07885494455695152):
																			return True
															else:
																if(lander_y <= 0.9833517670631409):
																	return True
												else:
													if(angle <= -0.20489487797021866):
														if(angle_velocity > 0.11081285029649734):
															if(y_velocity <= -0.34119923412799835):
																if(x_velocity > -0.16044805943965912):
																	return True
											else:
												if(y_velocity <= -0.3360630124807358):
													if(x_velocity <= -0.3516712188720703):
														if(angle_velocity <= -0.006786177633330226):
															return True
													else:
														if(angle_velocity <= 0.21774686127901077):
															if(lander_y <= 1.0004624426364899):
																return True
															else:
																if(lander_y > 1.0024277567863464):
																	if(angle_velocity <= -0.005694378829502966):
																		if(lander_x > -0.08002576977014542):
																			return True
																	else:
																		if(angle <= -0.1520085111260414):
																			if(lander_x > -0.1869145855307579):
																				return True
																		else:
																			if(angle_velocity <= 0.024869399145245552):
																				if(angle_velocity <= 0.020315569825470448):
																					return True
																			else:
																				return True
														else:
															if(x_velocity > -0.05380119942128658):
																return True
												else:
													if(angle <= -0.16341836005449295):
														if(angle_velocity > 0.03856382332742214):
															if(angle_velocity <= 0.13748598098754883):
																if(lander_y <= 0.7049829363822937):
																	return True
															else:
																if(angle > -0.1892790049314499):
																	return True
													else:
														if(angle_velocity <= 0.04832232557237148):
															if(lander_x > -0.10481705516576767):
																if(angle <= -0.0997859351336956):
																	if(lander_y <= 0.6811869740486145):
																		return True
																	else:
																		if(angle <= -0.1066688820719719):
																			if(lander_x > -0.08522148057818413):
																				return True
																else:
																	return True
														else:
															return True
										else:
											if(y_velocity <= -0.3447175920009613):
												if(angle <= -0.14506709575653076):
													if(y_velocity <= -0.3985508531332016):
														if(lander_y > 1.063765048980713):
															if(angle_velocity <= -0.01774553209543228):
																if(x_velocity <= -0.2994004786014557):
																	if(x_velocity > -0.3445555120706558):
																		if(y_velocity <= -0.4132232069969177):
																			return True
															else:
																if(lander_y <= 1.3167800903320312):
																	if(lander_x > -0.1942407563328743):
																		if(lander_y <= 1.2698836922645569):
																			return True
																		else:
																			if(lander_y > 1.2792267799377441):
																				return True
																else:
																	if(angle_velocity > 0.001375226303935051):
																		if(angle <= -0.226822629570961):
																			return True
																		else:
																			if(angle > -0.2175343856215477):
																				return True
													else:
														if(angle > -0.1828475147485733):
															if(y_velocity <= -0.36406198143959045):
																if(angle_velocity > 0.005274130031466484):
																	if(y_velocity > -0.39671097695827484):
																		if(angle <= -0.17899803817272186):
																			if(angle <= -0.18128757923841476):
																				return True
																		else:
																			return True
															else:
																if(angle_velocity > 0.04756132513284683):
																	if(x_velocity > -0.14022498577833176):
																		if(lander_y > 1.1165762543678284):
																			return True
												else:
													if(y_velocity <= -0.3601759523153305):
														return True
													else:
														if(y_velocity > -0.35688579082489014):
															if(lander_y <= 1.3207906484603882):
																if(y_velocity <= -0.35348817706108093):
																	if(lander_x > -0.057523250579833984):
																		return True
																else:
																	return True
											else:
												if(angle <= -0.06962037831544876):
													if(y_velocity <= -0.33256442844867706):
														if(x_velocity > -0.15777025371789932):
															if(lander_y > 1.0779027342796326):
																if(angle <= -0.07502911239862442):
																	if(y_velocity <= -0.34312212467193604):
																		if(angle <= -0.13438867777585983):
																			return True
																	else:
																		return True
												else:
													if(y_velocity > -0.33425386250019073):
														return True
									else:
										if(lander_y <= 0.9724603593349457):
											if(angle <= -0.13911590725183487):
												if(y_velocity <= -0.3128570020198822):
													if(angle > -0.16731970012187958):
														if(angle_velocity > 0.05194188840687275):
															if(lander_y <= 0.869787186384201):
																return True
												else:
													if(angle_velocity <= 0.15131288766860962):
														if(lander_x <= -0.2863030731678009):
															if(angle_velocity <= 0.10642845928668976):
																return True
													else:
														if(y_velocity > -0.3040447533130646):
															return True
											else:
												if(lander_x <= 0.17120051383972168):
													if(angle_velocity <= -0.005081556271761656):
														if(x_velocity <= -0.1315990537405014):
															if(lander_y <= 0.7717319130897522):
																return True
														else:
															if(angle > -0.0725240409374237):
																if(x_velocity > -0.12408722564578056):
																	return True
													else:
														if(angle <= -0.11836115643382072):
															if(angle_velocity > 0.035113219171762466):
																if(angle <= -0.12105177715420723):
																	if(lander_y > 0.5059874653816223):
																		if(lander_x <= 0.0654900074005127):
																			return True
																		else:
																			if(x_velocity > -0.14474781602621078):
																				return True
														else:
															if(angle <= -0.05388873629271984):
																if(lander_y <= 0.9470905959606171):
																	if(y_velocity <= -0.30324292182922363):
																		if(angle <= -0.05917237140238285):
																			if(angle <= -0.11068673804402351):
																				if(lander_y <= 0.7255429923534393):
																					return True
																			else:
																				return True
																		else:
																			if(angle > -0.05811325088143349):
																				return True
																	else:
																		if(y_velocity > -0.3031436502933502):
																			if(angle_velocity <= 0.001812802569475025):
																				if(lander_y > 0.6748694181442261):
																					return True
																			else:
																				if(x_velocity <= -0.14478172361850739):
																					if(angle_velocity <= 0.023746936582028866):
																						return True
																					else:
																						if(angle <= -0.0906406044960022):
																							if(angle_velocity > 0.025198789313435555):
																								return True
																				else:
																					if(lander_y <= 0.890732079744339):
																						if(angle_velocity <= 0.017454905435442924):
																							if(x_velocity <= -0.10349521413445473):
																								return True
																						else:
																							if(angle <= -0.10757024213671684):
																								if(x_velocity > -0.106439758092165):
																									return True
																							else:
																								return True
																					else:
																						if(y_velocity > -0.2978654056787491):
																							return True
																else:
																	if(angle_velocity > 0.03174198791384697):
																		if(lander_x <= -0.09213199466466904):
																			if(y_velocity <= -0.29576967656612396):
																				return True
																			else:
																				if(y_velocity > -0.2923332005739212):
																					return True
										else:
											if(x_velocity <= -0.0746455229818821):
												if(angle_velocity <= 0.027894112281501293):
													if(lander_x <= -0.08236465603113174):
														if(angle > -0.08952869474887848):
															return True
											else:
												if(y_velocity <= -0.2972036898136139):
													if(x_velocity <= -0.06677962467074394):
														return True
													else:
														if(lander_x <= -0.1553829237818718):
															if(angle_velocity <= 0.10363348573446274):
																return True
														else:
															if(angle_velocity > 0.08678365498781204):
																return True
								else:
									if(angle_velocity <= 0.05515405908226967):
										if(lander_y <= 0.5726955235004425):
											if(angle <= -0.07068922743201256):
												if(y_velocity > -0.2825336307287216):
													if(x_velocity > -0.12021123990416527):
														if(lander_x <= -0.3089955896139145):
															return True
											else:
												if(y_velocity <= -0.2722477614879608):
													return True
												else:
													if(angle_velocity > 0.008120624348521233):
														if(x_velocity > -0.08208607323467731):
															return True
										else:
											if(x_velocity <= -0.06573277339339256):
												if(lander_y <= 0.6902416348457336):
													if(angle_velocity > 0.03395815286785364):
														if(lander_y > 0.6364759206771851):
															if(angle > -0.0842120386660099):
																return True
									else:
										if(lander_y <= 0.7663210034370422):
											if(angle <= -0.10654593259096146):
												if(y_velocity <= -0.2830393612384796):
													return True
											else:
												if(x_velocity > -0.14428503811359406):
													if(y_velocity <= -0.270984947681427):
														if(angle <= -0.1030520498752594):
															if(angle <= -0.10459158197045326):
																return True
														else:
															return True
													else:
														if(lander_y <= 0.5829871296882629):
															if(lander_y > 0.4420061707496643):
																return True
										else:
											if(x_velocity > 0.017174482811242342):
												if(y_velocity <= -0.27996663749217987):
													return True
							else:
								if(lander_y <= 0.7862126231193542):
									if(y_velocity <= -0.264681339263916):
										if(lander_y <= 0.726870208978653):
											if(x_velocity <= -0.11643403023481369):
												if(x_velocity <= -0.12472354620695114):
													return True
											else:
												if(angle_velocity <= 0.0818091630935669):
													if(y_velocity <= -0.2663245052099228):
														if(y_velocity <= -0.27826161682605743):
															return True
														else:
															if(y_velocity > -0.2781319171190262):
																if(x_velocity <= -0.09295184165239334):
																	if(y_velocity <= -0.2704695612192154):
																		return True
																else:
																	if(angle_velocity <= 0.0037979177432134748):
																		if(angle_velocity <= 0.0032262742752209306):
																			if(lander_y <= 0.6484237611293793):
																				return True
																			else:
																				if(angle > -0.03455995116382837):
																					if(x_velocity <= 0.025959890335798264):
																						return True
																					else:
																						if(angle_velocity > -0.006534545042086393):
																							return True
																	else:
																		return True
													else:
														if(y_velocity > -0.2662261426448822):
															if(lander_x <= 0.09752116352319717):
																return True
															else:
																if(x_velocity <= -0.03866182826459408):
																	return True
												else:
													if(angle_velocity > 0.08660867437720299):
														return True
										else:
											if(lander_y > 0.7282095849514008):
												if(y_velocity <= -0.27001261711120605):
													if(angle <= -0.036538174375891685):
														if(y_velocity <= -0.2824312895536423):
															if(y_velocity <= -0.2909196615219116):
																return True
															else:
																if(lander_x <= 0.06868495792150497):
																	return True
													else:
														if(y_velocity <= -0.27545684576034546):
															return True
														else:
															if(y_velocity > -0.2753885090351105):
																return True
												else:
													if(angle_velocity <= -0.00363212579395622):
														if(y_velocity > -0.26842033863067627):
															if(y_velocity > -0.2679774612188339):
																return True
													else:
														if(y_velocity <= -0.26930294930934906):
															if(lander_y > 0.7515392601490021):
																return True
														else:
															return True
									else:
										if(angle <= -0.018328707665205002):
											if(lander_y <= 0.6719333529472351):
												if(angle <= -0.020177501253783703):
													if(angle_velocity <= -0.015758157707750797):
														if(angle_velocity <= -0.024554399773478508):
															return True
													else:
														if(lander_x <= 0.09896249696612358):
															if(lander_y <= 0.568742573261261):
																return True
															else:
																if(x_velocity > -0.044225575402379036):
																	return True
														else:
															if(angle_velocity <= 0.02418297529220581):
																return True
											else:
												if(angle_velocity > 0.030637436546385288):
													if(x_velocity <= 0.023183227516710758):
														if(y_velocity > -0.26006515324115753):
															if(lander_x <= 0.010152911767363548):
																return True
													else:
														if(angle_velocity <= 0.040583858266472816):
															return True
										else:
											if(lander_x <= 0.15579185634851456):
												if(angle <= -0.012741807848215103):
													if(x_velocity <= 0.042152289301157):
														return True
												else:
													if(lander_x <= -0.17127098888158798):
														if(y_velocity <= -0.26009903848171234):
															return True
													else:
														return True
											else:
												if(x_velocity > -0.061157720163464546):
													if(angle > 0.003152078716084361):
														return True
								else:
									if(y_velocity <= -0.28120529651641846):
										if(lander_y <= 1.3223260641098022):
											if(x_velocity <= 0.689288318157196):
												if(y_velocity <= -0.29172690212726593):
													if(lander_y <= 1.1302112936973572):
														if(lander_y <= 0.7932920157909393):
															if(lander_x <= 0.04580864869058132):
																return True
														else:
															if(x_velocity <= -0.10984238237142563):
																if(y_velocity <= -0.29639288783073425):
																	return True
															else:
																if(x_velocity <= -0.07861029356718063):
																	if(x_velocity <= -0.07864519581198692):
																		return True
																else:
																	return True
													else:
														if(x_velocity <= -0.06834279373288155):
															if(y_velocity <= -0.3363427072763443):
																return True
														else:
															if(angle <= 0.032738350331783295):
																if(y_velocity <= -0.2967776656150818):
																	if(lander_x <= 0.054551173001527786):
																		if(y_velocity <= -0.31002724170684814):
																			if(lander_y > 1.1310220956802368):
																				if(angle_velocity > -0.028702893294394016):
																					return True
																		else:
																			if(x_velocity <= -0.024523289874196053):
																				if(x_velocity <= -0.03669215552508831):
																					if(y_velocity <= -0.3072790056467056):
																						return True
																					else:
																						if(lander_y <= 1.1619901657104492):
																							return True
																				else:
																					return True
																			else:
																				if(angle_velocity > 0.01953697530552745):
																					return True
															else:
																return True
												else:
													if(angle <= -0.03183910623192787):
														if(angle_velocity <= 0.03209804557263851):
															if(lander_y <= 0.8246901035308838):
																if(lander_y > 0.8146162927150726):
																	return True
														else:
															if(lander_x <= -0.08121781423687935):
																return True
													else:
														if(angle_velocity <= -0.014398808125406504):
															if(angle > -0.00023564865114167333):
																if(lander_x > -0.005478000617586076):
																	if(x_velocity > -0.10330203175544739):
																		if(angle <= 0.31670014560222626):
																			if(angle_velocity > -0.02983016800135374):
																				return True
														else:
															if(lander_y <= 1.0982114672660828):
																if(angle <= -0.02307185810059309):
																	if(angle_velocity > 0.0034483526833355427):
																		return True
																else:
																	if(lander_x <= -0.06691999360918999):
																		if(lander_y <= 0.9380663931369781):
																			return True
																	else:
																		return True
															else:
																if(lander_x > -0.014168167021125555):
																	if(lander_y <= 1.1329796314239502):
																		if(y_velocity > -0.28620511293411255):
																			return True
																	else:
																		if(angle <= 0.05461981147527695):
																			if(x_velocity <= 0.068813756108284):
																				return True
																		else:
																			return True
										else:
											if(x_velocity <= 0.3373533934354782):
												if(angle_velocity <= 0.02754958253353834):
													if(y_velocity <= -0.3092615008354187):
														if(lander_x <= 0.0002729415718931705):
															if(angle_velocity <= -0.00404905981849879):
																return True
															else:
																if(x_velocity > -0.11783743649721146):
																	if(y_velocity <= -0.3257075399160385):
																		return True
														else:
															if(angle_velocity > 0.013891918584704399):
																return True
												else:
													if(x_velocity <= 0.26448947191238403):
														if(lander_x <= -0.007713413331657648):
															if(y_velocity <= -0.3825749307870865):
																return True
														else:
															if(y_velocity <= -0.2839295417070389):
																if(angle <= 0.002377282246015966):
																	if(lander_x > -0.001703500747680664):
																		return True
																else:
																	return True
															else:
																if(lander_x > 0.015925979241728783):
																	return True
													else:
														if(angle_velocity > 0.22475795447826385):
															return True
											else:
												if(lander_x > 0.08645286411046982):
													return True
									else:
										if(angle <= 0.008823844138532877):
											if(x_velocity <= 0.02957223169505596):
												if(angle_velocity <= -0.003948292229324579):
													if(x_velocity > -0.07307593896985054):
														if(y_velocity <= -0.2766232490539551):
															if(lander_x <= 0.12454085052013397):
																if(lander_y <= 1.0828734040260315):
																	if(lander_x <= 0.050665806978940964):
																		return True
																	else:
																		if(lander_x > 0.06941809505224228):
																			return True
														else:
															if(y_velocity <= -0.2619604170322418):
																if(angle_velocity <= -0.029291611164808273):
																	return True
																else:
																	if(x_velocity > -0.008382251020520926):
																		if(x_velocity <= -0.004336855374276638):
																			return True
															else:
																if(angle > -0.005207735957810655):
																	return True
												else:
													if(lander_y <= 0.8370178639888763):
														if(angle > -0.03568756766617298):
															if(y_velocity <= -0.2723460793495178):
																return True
															else:
																if(lander_y <= 0.8015757501125336):
																	return True
													else:
														if(x_velocity <= 0.0015450450009666383):
															if(lander_x <= -0.14837151020765305):
																if(y_velocity <= -0.27156203985214233):
																	return True
														else:
															if(angle_velocity <= 0.07028498873114586):
																if(x_velocity > 0.018781457096338272):
																	return True
															else:
																if(lander_y > 0.8849963247776031):
																	if(x_velocity <= 0.023016029968857765):
																		return True
											else:
												if(lander_y <= 0.8839908838272095):
													if(angle <= 0.0016690654447302222):
														return True
													else:
														if(lander_y > 0.825396716594696):
															return True
										else:
											if(x_velocity <= -0.024900871329009533):
												if(lander_y <= 0.8975584805011749):
													return True
												else:
													if(y_velocity <= -0.274201899766922):
														if(lander_y <= 1.1256186366081238):
															return True
											else:
												if(lander_y <= 1.1035210490226746):
													if(angle_velocity <= -0.007809704169631004):
														if(lander_x <= -0.0066200734581798315):
															if(lander_y <= 0.8830638229846954):
																if(lander_x <= -0.025331116281449795):
																	return True
														else:
															if(angle_velocity <= -0.009957340080291033):
																return True
													else:
														if(x_velocity <= 0.0636452604085207):
															return True
														else:
															if(angle_velocity > 0.011627326952293515):
																return True
												else:
													if(angle <= 0.059718646109104156):
														if(x_velocity <= 0.07696686312556267):
															if(angle_velocity <= 0.049309903755784035):
																if(y_velocity <= -0.27673155069351196):
																	return True
														else:
															if(angle > 0.044628797098994255):
																return True
													else:
														if(x_velocity > 0.016323771327733994):
															if(angle <= 0.5938259661197662):
																if(angle <= 0.0917450375854969):
																	if(angle <= 0.08894968032836914):
																		if(angle_velocity > -0.0218551866710186):
																			if(x_velocity <= 0.10189161077141762):
																				if(angle_velocity <= 0.07326102256774902):
																					return True
																			else:
																				if(angle_velocity > 0.040689398534595966):
																					return True
																else:
																	if(lander_y <= 1.1470887660980225):
																		if(lander_x <= 0.17361994087696075):
																			return True
																	else:
																		return True
															else:
																if(x_velocity > 0.220756433904171):
																	return True
					else:
						if(x_velocity <= 0.0351233147084713):
							if(lander_y <= 0.6716362833976746):
								if(y_velocity <= -0.24182037264108658):
									if(angle <= -0.030423035845160484):
										if(angle_velocity <= 0.012476997915655375):
											if(y_velocity <= -0.2574797421693802):
												return True
											else:
												if(x_velocity > -0.0958431251347065):
													if(lander_y <= 0.6339707970619202):
														if(lander_x > -0.26393239200115204):
															if(angle_velocity > -0.00016509604756720364):
																if(angle > -0.03813371993601322):
																	if(lander_y <= 0.441238209605217):
																		return True
										else:
											if(x_velocity > -0.04057971388101578):
												if(angle_velocity <= 0.06265179812908173):
													if(lander_y <= 0.5813332498073578):
														return True
												else:
													if(x_velocity > -0.02495346311479807):
														if(y_velocity <= -0.2550571858882904):
															if(lander_x > -0.26875877380371094):
																return True
									else:
										if(x_velocity <= -0.022938490845263004):
											if(y_velocity <= -0.2510243207216263):
												if(x_velocity <= -0.03385838866233826):
													if(x_velocity > -0.09269861876964569):
														if(y_velocity <= -0.25851693749427795):
															if(angle <= -0.023491637781262398):
																return True
														else:
															if(angle <= -0.02707223128527403):
																if(x_velocity <= -0.049005866050720215):
																	return True
															else:
																return True
												else:
													if(y_velocity > -0.2551529258489609):
														return True
											else:
												if(lander_y <= 0.5494007766246796):
													if(angle_velocity <= 0.028564566746354103):
														if(angle <= -0.008791954722255468):
															if(lander_x <= 0.0940522663295269):
																if(angle <= -0.020844724029302597):
																	if(angle_velocity <= -0.011721173767000437):
																		if(x_velocity > -0.03165749553591013):
																			return True
																	else:
																		return True
																else:
																	if(lander_y <= 0.43996697664260864):
																		return True
															else:
																if(angle > -0.00977978901937604):
																	return True
														else:
															return True
													else:
														if(y_velocity <= -0.24814147502183914):
															return True
												else:
													if(angle <= -0.0006147521489765495):
														if(y_velocity <= -0.2501870170235634):
															if(lander_x <= 0.07091212132945657):
																return True
													else:
														if(angle_velocity > -0.01710554864257574):
															if(angle <= 0.009854057570919394):
																return True
										else:
											if(angle <= 0.0027327592251822352):
												if(angle_velocity <= -0.006165155675262213):
													if(lander_x <= -0.07699122466146946):
														if(x_velocity <= 0.004193082917481661):
															return True
														else:
															if(angle_velocity <= -0.020906340330839157):
																if(y_velocity <= -0.25711099803447723):
																	return True
															else:
																return True
													else:
														if(y_velocity <= -0.2523545101284981):
															if(lander_y <= 0.5161055624485016):
																return True
												else:
													if(y_velocity <= -0.24814879894256592):
														return True
													else:
														if(lander_x > -0.18955111503601074):
															if(lander_x <= 0.0545903705060482):
																if(lander_y <= 0.6457645297050476):
																	if(angle_velocity <= 0.012857219204306602):
																		if(x_velocity > 0.006761582451872528):
																			return True
																	else:
																		return True
											else:
												if(angle_velocity <= 0.051283856853842735):
													return True
												else:
													if(angle_velocity > 0.05207928642630577):
														return True
								else:
									if(angle <= 0.027446957305073738):
										if(angle_velocity <= 0.015449421480298042):
											if(x_velocity > -0.05134405195713043):
												if(lander_y <= 0.519020140171051):
													if(lander_x <= -0.061965130269527435):
														if(angle > -0.012045792769640684):
															if(y_velocity <= -0.2332426756620407):
																return True
															else:
																if(angle > -0.007997591746971011):
																	if(angle <= 0.0037133883452042937):
																		if(x_velocity <= 0.010035439161583781):
																			return True
													else:
														if(angle <= 0.0022921893396414816):
															if(y_velocity <= -0.23914062976837158):
																if(angle_velocity > -0.01008171821013093):
																	return True
															else:
																if(angle_velocity > 0.011842083651572466):
																	if(x_velocity <= -0.013829858973622322):
																		return True
														else:
															if(x_velocity <= -0.0018326767021790147):
																return True
															else:
																if(x_velocity > 0.007200711057521403):
																	return True
										else:
											if(y_velocity <= -0.2299792394042015):
												if(x_velocity <= -0.011013717856258154):
													if(angle > -0.05876550450921059):
														if(lander_y <= 0.4012627750635147):
															return True
												else:
													if(lander_x <= -0.028031492605805397):
														if(angle_velocity <= 0.05883670784533024):
															if(lander_y <= 0.43440139293670654):
																return True
															else:
																if(angle > 0.008804187411442399):
																	return True
													else:
														if(y_velocity <= -0.23702511936426163):
															if(lander_x <= 0.038957834243774414):
																return True
														else:
															return True
									else:
										if(lander_y <= 0.5512659549713135):
											return True
										else:
											if(lander_y > 0.5924049317836761):
												return True
							else:
								if(y_velocity <= -0.254315048456192):
									if(lander_y <= 0.805266261100769):
										if(x_velocity > -0.019964149221777916):
											if(y_velocity <= -0.25867871940135956):
												if(lander_y <= 0.7090049088001251):
													if(angle <= -0.026516162790358067):
														return True
											else:
												if(angle > -0.03542984742671251):
													return True
									else:
										if(y_velocity > -0.25615353882312775):
											if(lander_x <= 0.03419036790728569):
												if(lander_x > 0.028237628750503063):
													return True
								else:
									if(angle > -0.02805306576192379):
										if(angle <= 0.00988092040643096):
											if(angle <= 0.008488973136991262):
												if(angle_velocity <= 0.018945268355309963):
													if(x_velocity > -0.05272674560546875):
														if(lander_x <= -0.008359670639038086):
															if(x_velocity > 0.0004283926245989278):
																if(lander_x > -0.12854037433862686):
																	if(lander_y <= 0.7229493260383606):
																		return True
												else:
													if(angle_velocity > 0.06711917370557785):
														if(angle_velocity <= 0.07086296379566193):
															return True
										else:
											if(lander_y <= 0.6982258856296539):
												if(y_velocity <= -0.24224982410669327):
													return True
											else:
												if(y_velocity <= -0.25035081803798676):
													if(lander_y <= 0.8034637272357941):
														return True
						else:
							if(lander_y <= 0.6493006646633148):
								if(angle_velocity <= -0.006822241935878992):
									if(x_velocity <= 0.05531732365489006):
										if(angle > -0.011808109877165407):
											if(lander_x <= 0.03598055802285671):
												return True
									else:
										if(angle > 0.020863776095211506):
											if(y_velocity <= -0.22930432856082916):
												if(lander_x <= -0.09005723148584366):
													return True
												else:
													if(angle > 0.04609214700758457):
														return True
											else:
												if(angle_velocity <= -0.029126125387847424):
													return True
								else:
									if(angle <= 0.013355567120015621):
										if(y_velocity <= -0.23322056233882904):
											if(angle_velocity <= 0.00859047519043088):
												if(x_velocity <= 0.042379479855298996):
													return True
												else:
													if(y_velocity <= -0.2457507625222206):
														if(angle > -0.005473450990393758):
															return True
											else:
												if(lander_x > -0.3024490624666214):
													if(lander_y <= 0.6396333873271942):
														return True
													else:
														if(lander_x > -0.13431158289313316):
															return True
										else:
											if(lander_y <= 0.5424078404903412):
												if(x_velocity <= 0.09163873642683029):
													if(x_velocity > 0.04795690439641476):
														if(angle_velocity > 0.0155371087603271):
															if(y_velocity <= -0.22487520426511765):
																return True
									else:
										if(y_velocity <= -0.22986306250095367):
											if(angle_velocity <= -0.0014708756352774799):
												if(lander_x <= -0.01130828820168972):
													return True
											else:
												return True
										else:
											if(lander_y <= 0.6228525638580322):
												if(lander_y <= 0.5419533252716064):
													return True
												else:
													if(angle > 0.03544514626264572):
														return True
							else:
								if(angle <= 0.131209097802639):
									if(lander_y <= 0.7742876708507538):
										if(y_velocity <= -0.22755412012338638):
											if(angle_velocity <= -0.008942980319261551):
												if(angle > 0.03935479559004307):
													return True
											else:
												if(angle <= 0.015457208268344402):
													if(angle_velocity <= 0.07502374239265919):
														if(y_velocity <= -0.24598274379968643):
															if(angle_velocity <= 0.053720030933618546):
																return True
														else:
															if(lander_x > -0.18042293190956116):
																if(angle_velocity > 0.04974053055047989):
																	if(lander_y <= 0.7130709290504456):
																		return True
												else:
													if(x_velocity <= 0.046755023300647736):
														if(x_velocity <= 0.03802955523133278):
															return True
													else:
														if(y_velocity <= -0.228505440056324):
															if(angle_velocity <= 0.0038729080697521567):
																if(angle <= 0.037339987233281136):
																	if(y_velocity <= -0.2473110780119896):
																		return True
																else:
																	return True
															else:
																if(angle_velocity <= 0.060446394607424736):
																	return True
																else:
																	if(lander_x <= -0.14861049503087997):
																		return True
										else:
											if(angle_velocity <= 0.026497455313801765):
												if(lander_y > 0.6824868023395538):
													if(y_velocity <= -0.22351376712322235):
														return True
									else:
										if(y_velocity <= -0.24771227687597275):
											if(angle <= 0.02712376043200493):
												if(angle_velocity <= 0.044933730736374855):
													if(lander_y <= 0.7800486981868744):
														return True
												else:
													if(lander_y <= 0.8468361496925354):
														if(y_velocity <= -0.2513609975576401):
															return True
													else:
														if(x_velocity <= 0.042589107528328896):
															if(lander_y <= 0.9715511798858643):
																return True
											else:
												if(x_velocity <= 0.06934664398431778):
													if(lander_y <= 1.0812788605690002):
														return True
												else:
													if(angle_velocity > 0.013977652648463845):
														if(lander_y <= 1.3851042985916138):
															if(angle <= 0.11550601944327354):
																return True
															else:
																if(lander_y <= 1.3562791347503662):
																	return True
										else:
											if(lander_y <= 1.3818557262420654):
												if(angle_velocity <= 0.034344857558608055):
													if(lander_y <= 0.847799152135849):
														if(angle_velocity > 0.014621262438595295):
															return True
													else:
														if(lander_x > -0.04421668127179146):
															if(x_velocity > 0.06390602700412273):
																if(x_velocity <= 0.06762076169252396):
																	return True
								else:
									if(x_velocity <= 0.29419660568237305):
										if(angle <= 0.4251032918691635):
											if(y_velocity <= -0.23989219963550568):
												if(lander_x > 0.041028356179594994):
													return True
											else:
												if(x_velocity <= 0.2217264175415039):
													if(lander_y <= 1.1297022700309753):
														return True
													else:
														if(angle <= 0.16237346082925797):
															if(angle > 0.15144534409046173):
																return True
												else:
													return True
										else:
											if(y_velocity <= -0.2537519484758377):
												return True
											else:
												if(angle_velocity <= 0.009572558104991913):
													return True
												else:
													if(x_velocity <= 0.2756223827600479):
														if(angle_velocity > 0.19462165236473083):
															if(lander_x > 0.20777478069067):
																return True
													else:
														if(y_velocity <= -0.22703466564416885):
															return True
									else:
										return True
		else:
			if(angle_velocity <= -0.010854553431272507):
				if(right_leg_contact != True):
					if(angle <= 0.06201705522835255):
						if(angle_velocity <= -0.035603923723101616):
							if(x_velocity <= -0.049048325046896935):
								if(angle <= -0.018289437517523766):
									if(x_velocity > -0.3122575879096985):
										if(x_velocity <= -0.051378997042775154):
											if(x_velocity > -0.09737235680222511):
												if(y_velocity <= -0.217939130961895):
													if(y_velocity > -0.218879796564579):
														return True
								else:
									if(y_velocity <= -0.2162977084517479):
										return True
									else:
										if(lander_x > 0.10602355003356934):
											if(lander_y <= 0.011788675794377923):
												return True
							else:
								if(angle_velocity <= -0.052182361483573914):
									if(angle <= 0.0359882228076458):
										if(lander_y <= 0.6568058431148529):
											if(lander_x > 0.046082401648163795):
												if(lander_x <= 0.046274567022919655):
													return True
									else:
										if(angle_velocity > -0.06976191699504852):
											if(angle_velocity <= -0.06222432106733322):
												return True
											else:
												if(x_velocity > 0.043531442526727915):
													if(angle > 0.04994909465312958):
														return True
								else:
									if(lander_x <= -0.1753547191619873):
										if(y_velocity <= -0.2071043848991394):
											if(angle > -0.0018436736281728372):
												return True
									else:
										if(x_velocity <= 0.02934814989566803):
											if(angle <= 0.024723194539546967):
												if(lander_x <= -0.07197494432330132):
													if(angle > -0.01471952348947525):
														if(x_velocity <= 0.007668731268495321):
															if(lander_y <= 0.1319637969136238):
																return True
												else:
													if(left_leg_contact != True):
														if(angle <= 0.01774296723306179):
															if(x_velocity <= -0.034288011491298676):
																if(angle_velocity > -0.045387158170342445):
																	if(lander_x <= 0.01595573453232646):
																		if(lander_y > 0.08574990928173065):
																			return True
														else:
															if(lander_x <= 0.05536680109798908):
																if(x_velocity <= -0.003545665182173252):
																	return True
													else:
														return True
											else:
												if(lander_y <= 0.17466771602630615):
													if(y_velocity <= -0.18647807836532593):
														return True
										else:
											if(angle > 0.058603471145033836):
												return True
						else:
							if(x_velocity <= 0.002305949805304408):
								if(lander_y <= 0.17234846204519272):
									if(y_velocity <= -0.1974310204386711):
										if(angle <= -0.0044709129724651575):
											if(lander_x > -0.16076922416687012):
												if(x_velocity > -0.07829222083091736):
													if(angle <= -0.021579984575510025):
														if(x_velocity <= -0.07385072857141495):
															return True
													else:
														if(angle <= -0.00968098221346736):
															if(y_velocity <= -0.2120053917169571):
																return True
										else:
											if(lander_y <= 0.09052756428718567):
												return True
											else:
												if(lander_x <= 0.025167417712509632):
													if(y_velocity <= -0.2042122557759285):
														return True
												else:
													if(angle_velocity > -0.020028371829539537):
														return True
								else:
									if(lander_x <= 0.07196741178631783):
										if(y_velocity > -0.2186787948012352):
											if(angle_velocity > -0.011381357908248901):
												return True
							else:
								if(lander_y <= 0.21626899391412735):
									if(y_velocity <= -0.18917064368724823):
										if(angle <= 0.005225776461884379):
											if(angle > -0.010194838978350163):
												if(x_velocity <= 0.02813156321644783):
													if(lander_x <= -0.048626137897372246):
														if(x_velocity > 0.005624378565698862):
															return True
										else:
											if(x_velocity <= 0.07935518398880959):
												if(lander_y <= 0.1443529948592186):
													if(angle <= 0.01576882740482688):
														if(angle <= 0.015076188370585442):
															if(lander_x <= -0.02224073465913534):
																return True
															else:
																if(lander_x > 0.0026698587462306023):
																	return True
													else:
														return True
												else:
													if(lander_x <= -0.027375363744795322):
														if(lander_y > 0.1602785587310791):
															if(y_velocity > -0.21792226284742355):
																return True
													else:
														if(angle_velocity <= -0.030583099462091923):
															return True
									else:
										if(lander_x <= -0.0855782963335514):
											if(x_velocity > 0.05733836628496647):
												if(angle_velocity <= -0.023472610861063004):
													return True
										else:
											if(angle <= 0.045848630368709564):
												if(y_velocity <= -0.18624678254127502):
													if(lander_y <= 0.11104568094015121):
														return True
											else:
												if(y_velocity <= -0.1697707325220108):
													if(lander_x <= 0.007307147607207298):
														return True
								else:
									if(lander_x <= -0.04364814795553684):
										if(x_velocity <= 0.061992842704057693):
											if(y_velocity <= -0.20960137993097305):
												if(angle > 0.003252117079682648):
													if(lander_y <= 0.4394170939922333):
														if(lander_x > -0.19607630372047424):
															if(x_velocity > 0.01444409042596817):
																return True
										else:
											if(lander_x <= -0.18886275589466095):
												if(angle_velocity <= -0.023781098425388336):
													return True
									else:
										if(x_velocity <= 0.010280539281666279):
											if(x_velocity <= 0.008855934720486403):
												if(y_velocity <= -0.18366089463233948):
													return True
										else:
											if(lander_y <= 0.6267885267734528):
												if(y_velocity <= -0.21158729493618011):
													if(y_velocity > -0.21374759823083878):
														return True
					else:
						if(y_velocity <= -0.17376063019037247):
							if(angle <= 0.0821714960038662):
								if(angle_velocity <= -0.041054217144846916):
									if(lander_x > 0.11134877428412437):
										return True
								else:
									if(lander_x <= -0.06110477261245251):
										return True
									else:
										if(x_velocity <= 0.06728479266166687):
											return True
							else:
								if(x_velocity <= 0.1566612273454666):
									if(angle_velocity <= -0.11321457102894783):
										if(lander_y > 1.1185217499732971):
											if(y_velocity <= -0.21329336613416672):
												if(lander_x <= 0.16910595446825027):
													return True
											else:
												if(x_velocity > 0.13447826355695724):
													return True
									else:
										if(lander_y <= 1.0543045401573181):
											if(y_velocity <= -0.21630842983722687):
												return True
								else:
									if(angle_velocity <= -0.1363706737756729):
										if(angle <= 0.3233770728111267):
											if(y_velocity <= -0.18574092537164688):
												if(x_velocity <= 0.17242160439491272):
													if(lander_x <= 0.21601442992687225):
														return True
											else:
												return True
										else:
											return True
									else:
										if(y_velocity <= -0.19166146963834763):
											return True
										else:
											if(lander_y <= 1.386024832725525):
												if(x_velocity > 0.2562812268733978):
													if(lander_x > 0.18224620819091797):
														return True
											else:
												if(angle <= 0.35339273512363434):
													return True
						else:
							if(lander_y <= 0.32353532314300537):
								if(x_velocity > 0.13265391439199448):
									if(angle_velocity > -0.033276102505624294):
										if(lander_y <= 0.10371938720345497):
											return True
			else:
				if(lander_y <= 0.2456214353442192):
					if(y_velocity <= -0.18587703257799149):
						if(x_velocity <= 0.018928966484963894):
							if(y_velocity <= -0.20360344648361206):
								if(x_velocity <= -0.02664847020059824):
									if(left_leg_contact != True):
										if(angle_velocity <= 0.0043722393456846476):
											if(lander_x > 0.06290278211236):
												if(y_velocity <= -0.21166489273309708):
													return True
									else:
										return True
								else:
									if(lander_y <= 0.18653695285320282):
										if(lander_x <= -0.1305283084511757):
											if(y_velocity <= -0.213547945022583):
												return True
											else:
												if(left_leg_contact == True):
													return True
										else:
											if(lander_y > 0.0018440998392179608):
												if(angle_velocity <= -0.0051151760853827):
													if(lander_y <= 0.12370817363262177):
														return True
												else:
													if(x_velocity <= -0.0147034777328372):
														if(angle_velocity <= 0.05712492577731609):
															if(y_velocity <= -0.20699603855609894):
																return True
													else:
														return True
									else:
										if(lander_x > -0.03983144648373127):
											if(y_velocity <= -0.21081820875406265):
												return True
											else:
												if(x_velocity > 0.009407946839928627):
													return True
							else:
								if(angle_velocity <= -0.005452348385006189):
									if(angle > -0.0012260186485946178):
										if(angle_velocity > -0.009282009676098824):
											return True
								else:
									if(lander_y <= 0.004058173857629299):
										if(y_velocity > -0.19918935745954514):
											return True
									else:
										if(angle <= 0.019453133456408978):
											if(x_velocity <= 0.018647784367203712):
												if(x_velocity > -0.0010153257171623409):
													if(angle_velocity <= 0.013525543734431267):
														if(y_velocity <= -0.19654496759176254):
															if(angle > -0.001700681183137931):
																return True
													else:
														if(lander_y <= 0.010608843760564923):
															return True
										else:
											if(y_velocity <= -0.19190432876348495):
												if(lander_x > 0.04047045577317476):
													return True
						else:
							if(angle <= 0.010951127856969833):
								if(y_velocity <= -0.20143694430589676):
									if(angle > -0.030738230794668198):
										if(angle_velocity <= -0.0014800538774579763):
											if(y_velocity <= -0.20968253910541534):
												if(angle_velocity <= -0.006079734768718481):
													return True
										else:
											if(angle <= -0.014598495326936245):
												if(lander_x <= -0.11413297429680824):
													if(x_velocity <= 0.08296073973178864):
														return True
											else:
												if(x_velocity <= 0.05898321233689785):
													return True
												else:
													if(x_velocity > 0.06136663444340229):
														return True
								else:
									if(lander_y <= 0.1378457024693489):
										if(angle > -0.010311076417565346):
											if(angle_velocity <= -0.004529626341536641):
												if(lander_x <= -0.08064927905797958):
													return True
											else:
												if(angle <= -0.004287490737624466):
													if(angle_velocity <= 0.06631219387054443):
														if(angle <= -0.009036874398589134):
															return True
													else:
														return True
												else:
													if(angle_velocity <= 0.0691668651998043):
														return True
													else:
														if(angle_velocity > 0.24349431693553925):
															return True
									else:
										if(y_velocity <= -0.19555621594190598):
											if(x_velocity > 0.05857863835990429):
												return True
							else:
								if(right_leg_contact != True):
									if(lander_y <= 0.14798488467931747):
										if(lander_x <= -0.2437056079506874):
											if(y_velocity <= -0.1990210860967636):
												return True
										else:
											if(lander_x <= 0.06865129619836807):
												return True
											else:
												if(lander_x > 0.07467718049883842):
													return True
									else:
										if(angle_velocity <= -0.0038335329154506326):
											if(lander_x <= -0.1481214016675949):
												return True
										else:
											if(y_velocity <= -0.20047180354595184):
												if(angle <= 0.01672883704304695):
													if(angle <= 0.016196143813431263):
														return True
												else:
													return True
											else:
												if(angle <= 0.0336521752178669):
													if(angle_velocity > 0.030562994070351124):
														if(angle_velocity <= 0.07024921476840973):
															if(angle_velocity <= 0.04628653638064861):
																if(angle_velocity <= 0.043115682899951935):
																	return True
																else:
																	if(y_velocity > -0.18773110210895538):
																		return True
															else:
																return True
												else:
													if(x_velocity <= 0.054850198328495026):
														if(x_velocity <= 0.04581424593925476):
															return True
													else:
														return True
					else:
						if(x_velocity <= 0.07906698435544968):
							if(left_leg_contact != True):
								if(x_velocity <= 0.05338051915168762):
									if(angle > -0.010246748104691505):
										if(lander_y > 0.010773012414574623):
											if(lander_x <= 0.1222846508026123):
												if(angle > 0.048809004947543144):
													if(angle <= 0.05020749568939209):
														return True
								else:
									if(y_velocity <= -0.17120373994112015):
										if(lander_x <= -0.03570122644305229):
											if(angle_velocity <= 0.018130283802747726):
												if(angle > 0.033740317448973656):
													return True
										else:
											if(lander_y <= 0.16543927043676376):
												if(y_velocity <= -0.1722951903939247):
													if(angle_velocity <= 0.04081559181213379):
														return True
									else:
										if(angle_velocity <= -0.0038011515280231833):
											if(y_velocity <= -0.15989500284194946):
												if(angle > 0.0491067785769701):
													return True
							else:
								if(angle_velocity <= 0.4526590257883072):
									if(angle <= -0.007183142472058535):
										return True
						else:
							if(y_velocity <= -0.16376685351133347):
								if(angle_velocity > -0.006967407651245594):
									if(angle_velocity <= 0.07804835960268974):
										if(lander_y <= 0.1487085074186325):
											if(lander_y > -0.005065127625130117):
												if(angle <= 0.049094974994659424):
													if(angle <= 0.046546122059226036):
														if(x_velocity <= 0.09626342356204987):
															return True
														else:
															if(angle_velocity <= 0.04645492136478424):
																if(lander_x > -0.06786765903234482):
																	return True
															else:
																if(angle_velocity > 0.0490306057035923):
																	if(y_velocity <= -0.17212731391191483):
																		return True
																	else:
																		if(lander_x > -0.23703859001398087):
																			return True
												else:
													return True
										else:
											if(y_velocity <= -0.17225368320941925):
												if(angle > 0.03927383664995432):
													return True
							else:
								if(x_velocity > 0.08246087282896042):
									if(x_velocity > 0.14585117995738983):
										if(y_velocity <= -0.1420469731092453):
											if(lander_y <= 0.04941176995635033):
												if(y_velocity <= -0.14626598358154297):
													return True
				else:
					if(x_velocity <= 0.08962250128388405):
						if(y_velocity <= -0.2100314348936081):
							if(x_velocity <= 0.013507533818483353):
								if(angle_velocity <= -0.0003657425886558485):
									if(lander_x <= -0.002429866697639227):
										if(angle > 0.0009894473478198051):
											return True
								else:
									if(y_velocity <= -0.2182958945631981):
										if(lander_y <= 0.31259019672870636):
											if(angle > -0.008802084950730205):
												return True
									else:
										if(x_velocity > -0.0056305848993361):
											if(x_velocity > -0.003742182394489646):
												if(lander_y <= 0.30085957050323486):
													if(y_velocity > -0.21470963954925537):
														return True
							else:
								if(lander_y <= 0.4193870723247528):
									if(angle <= -0.001474948861869052):
										if(angle > -0.016262791585177183):
											if(angle_velocity > 0.04632934741675854):
												if(lander_y <= 0.3065548688173294):
													return True
									else:
										if(angle_velocity <= 0.0005050814943388104):
											if(x_velocity <= 0.051337866112589836):
												if(lander_y <= 0.3735746890306473):
													return True
										else:
											if(y_velocity <= -0.21081842482089996):
												return True
											else:
												if(angle_velocity > 0.02686710422858596):
													return True
								else:
									if(lander_x <= 0.029781436547636986):
										if(y_velocity <= -0.21131696552038193):
											if(angle > -0.01164768310263753):
												if(y_velocity <= -0.21611396223306656):
													if(lander_y <= 0.49484284222126007):
														return True
													else:
														if(x_velocity > 0.07839666306972504):
															if(lander_x > -0.16721048206090927):
																return True
									else:
										if(lander_y <= 0.5562295019626617):
											return True
						else:
							if(x_velocity <= 0.07109396904706955):
								if(lander_y <= 0.3324655741453171):
									if(y_velocity <= -0.20063641667366028):
										if(angle <= 0.018269051797688007):
											if(lander_x > -0.041123056784272194):
												if(x_velocity > 0.013495360501110554):
													if(lander_y <= 0.30388055741786957):
														if(lander_x <= 0.07888107374310493):
															return True
										else:
											if(angle <= 0.023812297731637955):
												if(angle <= 0.020734618417918682):
													return True
											else:
												return True
									else:
										if(angle_velocity > -0.00905592879280448):
											if(lander_x > 0.08181328698992729):
												if(lander_x <= 0.08230986446142197):
													return True
							else:
								if(angle_velocity > 0.007354301633313298):
									if(lander_x > -0.08735213428735733):
										if(angle <= 0.05054444633424282):
											if(angle > 0.04708305187523365):
												return True
					else:
						if(y_velocity <= -0.17320022732019424):
							if(x_velocity <= 0.3846900016069412):
								if(angle_velocity <= 0.08039089664816856):
									if(lander_y <= 0.4670753479003906):
										if(angle <= 0.05356734059751034):
											if(y_velocity <= -0.18619784712791443):
												if(lander_x <= -0.24747539311647415):
													if(angle_velocity > 0.004820773145183921):
														if(lander_y <= 0.43625740706920624):
															if(angle_velocity <= 0.04857376217842102):
																return True
															else:
																if(angle > 0.026115651009604335):
																	return True
										else:
											if(x_velocity <= 0.17527805268764496):
												return True
											else:
												if(angle_velocity > 0.02628040115814656):
													return True
									else:
										if(x_velocity <= 0.26192905008792877):
											if(lander_y <= 0.6769025325775146):
												if(y_velocity <= -0.2017100751399994):
													if(angle > 0.05155929550528526):
														return True
										else:
											if(y_velocity <= -0.18212506920099258):
												return True
											else:
												if(x_velocity > 0.3377969115972519):
													return True
								else:
									if(lander_y <= 1.3846285939216614):
										if(y_velocity <= -0.2153453752398491):
											if(angle_velocity <= 0.23447684198617935):
												if(x_velocity > 0.14172151684761047):
													if(angle <= 0.2707720771431923):
														if(x_velocity <= 0.1658013015985489):
															if(lander_x <= -0.09793412312865257):
																return True
														else:
															return True
													else:
														if(lander_y <= 1.1619606614112854):
															return True
										else:
											if(y_velocity <= -0.20936059206724167):
												if(lander_y > 0.5769548416137695):
													if(y_velocity <= -0.20969827473163605):
														if(angle_velocity > 0.28310975432395935):
															if(x_velocity > 0.3066330552101135):
																return True
													else:
														return True
											else:
												if(lander_y <= 0.46398530900478363):
													if(lander_y > 0.4484563171863556):
														return True
									else:
										if(angle_velocity <= 0.1266830489039421):
											return True
							else:
								if(angle > 0.1528271809220314):
									if(angle <= 0.38715721666812897):
										return True
									else:
										if(x_velocity <= 0.42747414112091064):
											if(y_velocity <= -0.20557909458875656):
												return True
										else:
											if(angle_velocity <= 0.38150255382061005):
												return True
						else:
							if(x_velocity <= 0.5413434505462646):
								if(lander_y <= 1.4870757460594177):
									if(angle > 0.0240612612105906):
										if(x_velocity <= 0.520891547203064):
											if(lander_y > 1.4652548432350159):
												if(y_velocity <= -0.1625053510069847):
													return True
										else:
											if(y_velocity <= -0.15388526767492294):
												return True
								else:
									if(x_velocity > 0.44563575088977814):
										return True
							else:
								if(lander_x > 0.11860914528369904):
									return True
	else:
		if(y_velocity <= -0.00010637535888236016):
			if(angle <= 0.10152852162718773):
				if(lander_y <= 0.04580237716436386):
					if(angle_velocity <= 0.48136158287525177):
						if(right_leg_contact != True):
							if(angle_velocity > 0.1452050693333149):
								if(lander_y <= -0.012606015428900719):
									return True
	return False

def weShould_right_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(y_velocity <= -0.13701249659061432):
		if(y_velocity <= -0.220126174390316):
			if(angle_velocity <= -0.030239202082157135):
				if(angle <= 0.19462168961763382):
					if(lander_y <= 1.3413802981376648):
						if(y_velocity <= -0.2712501585483551):
							if(angle <= 0.061055488884449005):
								if(y_velocity <= -0.47413963079452515):
									if(x_velocity <= -0.5935395658016205):
										if(y_velocity > -0.5741690397262573):
											return True
									else:
										if(angle > -0.28904587030410767):
											if(angle <= -0.03099391609430313):
												if(lander_x > -0.14950332790613174):
													if(angle > -0.06514751352369785):
														if(angle <= -0.06125149503350258):
															return True
														else:
															if(y_velocity > -0.498701810836792):
																if(x_velocity <= -0.47367043793201447):
																	return True
											else:
												if(y_velocity <= -0.5455013811588287):
													if(x_velocity <= -0.5699999332427979):
														return True
													else:
														if(x_velocity <= -0.5565437078475952):
															if(lander_y <= 1.3011165261268616):
																return True
												else:
													return True
								else:
									if(angle_velocity <= -0.08699863031506538):
										if(y_velocity <= -0.342959463596344):
											if(angle > -0.18322286009788513):
												if(x_velocity <= -0.4903474748134613):
													if(angle_velocity > -0.3599099814891815):
														return True
												else:
													if(angle_velocity <= -0.32994210720062256):
														if(angle <= 0.017730834893882275):
															if(x_velocity > -0.486134335398674):
																if(angle_velocity > -0.3343295305967331):
																	if(angle_velocity <= -0.3325864374637604):
																		return True
													else:
														if(y_velocity <= -0.4216584116220474):
															if(lander_y > 0.8977401554584503):
																if(x_velocity <= -0.30474819242954254):
																	if(x_velocity <= -0.473934605717659):
																		if(lander_y > 1.1218289136886597):
																			return True
														else:
															if(angle <= -0.09334746748209):
																if(lander_y > 0.8961840569972992):
																	if(x_velocity <= -0.4140353798866272):
																		return True
																	else:
																		if(angle > -0.11283218860626221):
																			if(angle_velocity <= -0.12647632881999016):
																				if(lander_x <= -0.05339784733951092):
																					return True
																				else:
																					if(lander_y > 1.3081669807434082):
																						if(y_velocity <= -0.3763630539178848):
																							return True
															else:
																if(x_velocity <= -0.1488664746284485):
																	if(angle_velocity > -0.25299203395843506):
																		if(x_velocity <= -0.2530298978090286):
																			if(y_velocity <= -0.3705414682626724):
																				if(x_velocity <= -0.3272215723991394):
																					if(angle_velocity > -0.24009552597999573):
																						return True
										else:
											if(y_velocity <= -0.28863246738910675):
												if(angle <= 0.005772620206698775):
													if(lander_y <= 1.3169233798980713):
														if(lander_y <= 0.8466216921806335):
															if(lander_y > 0.793368399143219):
																if(x_velocity <= -0.21715107560157776):
																	if(x_velocity <= -0.22931460291147232):
																		if(y_velocity > -0.31617462635040283):
																			if(lander_y <= 0.8036152422428131):
																				return True
														else:
															if(angle_velocity > -0.09502262994647026):
																if(angle_velocity > -0.09259713813662529):
																	if(lander_x > 0.19910035282373428):
																		return True
													else:
														return True
											else:
												if(angle_velocity > -0.09310219064354897):
													return True
									else:
										if(y_velocity <= -0.29542168974876404):
											if(angle <= -0.07191513851284981):
												if(y_velocity <= -0.34861670434474945):
													if(y_velocity > -0.44248321652412415):
														if(angle > -0.22638513892889023):
															if(x_velocity <= -0.15816737711429596):
																if(angle <= -0.12100015580654144):
																	if(y_velocity > -0.4032207280397415):
																		if(y_velocity > -0.38404443860054016):
																			if(angle <= -0.15946373343467712):
																				if(angle <= -0.19899845123291016):
																					if(y_velocity > -0.37981468439102173):
																						return True
																			else:
																				if(y_velocity > -0.3745879828929901):
																					if(lander_x <= 0.13403596729040146):
																						return True
												else:
													if(lander_x > 0.14664892852306366):
														if(x_velocity <= -0.20580187439918518):
															if(lander_x <= 0.15389323234558105):
																if(angle <= -0.10972855612635612):
																	return True
															else:
																if(angle_velocity > -0.04370689205825329):
																	return True
											else:
												if(lander_x <= -0.007135295774787664):
													if(y_velocity <= -0.321407288312912):
														if(lander_x <= -0.031374311074614525):
															if(angle_velocity <= -0.053911035880446434):
																if(y_velocity > -0.42186667025089264):
																	return True
														else:
															if(x_velocity <= -0.28811974823474884):
																return True
															else:
																if(y_velocity > -0.33403821289539337):
																	if(lander_x <= -0.020509767811745405):
																		return True
												else:
													if(lander_y <= 1.2945742011070251):
														if(angle <= -0.03646194934844971):
															if(y_velocity > -0.31038226187229156):
																if(x_velocity <= -0.1803419589996338):
																	return True
														else:
															if(x_velocity <= -0.15120955556631088):
																if(y_velocity > -0.3107106536626816):
																	return True
										else:
											if(lander_y > 0.6564100086688995):
												if(angle <= 0.004643378080800176):
													if(x_velocity <= -0.1016995906829834):
														if(lander_y <= 0.8948809802532196):
															if(lander_x <= 0.045068979263305664):
																return True
														else:
															return True
												else:
													if(lander_y > 0.9250941276550293):
														if(x_velocity <= -0.08201296627521515):
															if(y_velocity > -0.291550949215889):
																return True
														else:
															if(lander_y <= 1.0987120866775513):
																if(angle_velocity <= -0.046588145196437836):
																	if(x_velocity <= -0.034358756616711617):
																		if(angle_velocity <= -0.053634967654943466):
																			if(y_velocity > -0.2848924994468689):
																				if(angle > 0.025381755083799362):
																					if(angle_velocity <= -0.07505744695663452):
																						if(lander_y <= 1.0517600178718567):
																							return True
							else:
								if(angle_velocity <= -0.09253112599253654):
									if(angle_velocity <= -0.42367124557495117):
										if(y_velocity > -0.33871832489967346):
											if(lander_x > 0.253693625330925):
												if(angle <= 0.1764698028564453):
													return True
								else:
									if(x_velocity <= -0.08083246648311615):
										return True
						else:
							if(lander_y <= 0.2888483852148056):
								if(angle_velocity <= -0.06200191378593445):
									if(y_velocity > -0.2447967603802681):
										if(angle <= 0.017069307155907154):
											if(lander_y > 0.01458512875251472):
												if(y_velocity > -0.22116205841302872):
													return True
								else:
									if(y_velocity <= -0.22887907177209854):
										if(y_velocity > -0.24936990439891815):
											if(angle <= -0.05136376619338989):
												if(lander_x > -0.1559777781367302):
													if(angle > -0.05449499189853668):
														return True
									else:
										if(angle <= -0.01896038744598627):
											if(lander_x <= -0.192253015935421):
												return True
											else:
												if(lander_y > 0.22453942149877548):
													return True
							else:
								if(angle <= -0.004452327499166131):
									if(angle_velocity <= -0.04128412716090679):
										if(y_velocity <= -0.2575591802597046):
											if(y_velocity <= -0.2603725492954254):
												if(x_velocity > -0.0782817117869854):
													if(lander_y > 0.7038154304027557):
														return True
										else:
											if(y_velocity > -0.2245744913816452):
												if(lander_y <= 0.3470495790243149):
													return True
									else:
										if(x_velocity <= -0.09462021663784981):
											return True
										else:
											if(lander_y <= 0.4283932000398636):
												if(y_velocity <= -0.23456428200006485):
													if(angle <= -0.011457640212029219):
														if(x_velocity <= -0.015013983007520437):
															if(x_velocity > -0.0848516970872879):
																if(y_velocity > -0.23807018995285034):
																	return True
											else:
												if(angle_velocity <= -0.04054407589137554):
													if(lander_y > 0.4673583507537842):
														return True
								else:
									if(lander_y <= 0.5517165660858154):
										if(y_velocity > -0.24928557872772217):
											if(angle_velocity > -0.056966641917824745):
												if(y_velocity > -0.23306214064359665):
													if(x_velocity <= -0.024672605097293854):
														return True
									else:
										if(x_velocity <= -0.0434639286249876):
											if(lander_x <= 0.12592416256666183):
												if(lander_y <= 0.6986694633960724):
													if(angle <= -5.954792140983045e-05):
														return True
												else:
													if(angle <= 0.012611632235348225):
														if(angle_velocity <= -0.05445677787065506):
															if(x_velocity <= -0.08741334080696106):
																return True
														else:
															return True
													else:
														return True
											else:
												if(y_velocity <= -0.24674434214830399):
													if(x_velocity <= -0.06307151541113853):
														if(angle <= 0.17386354506015778):
															if(angle_velocity <= -0.04279521852731705):
																if(x_velocity <= -0.2494330257177353):
																	return True
															else:
																if(angle > 0.014630157500505447):
																	return True
													else:
														if(y_velocity > -0.26617731153964996):
															return True
												else:
													if(lander_x > 0.12972688674926758):
														return True
										else:
											if(angle <= 0.051375413313508034):
												if(angle_velocity <= -0.03644077107310295):
													if(x_velocity <= 0.0021949945949018):
														if(angle_velocity > -0.05742747709155083):
															if(lander_y <= 0.7053986489772797):
																if(angle <= 0.01381576550193131):
																	if(angle_velocity > -0.04249518737196922):
																		return True
															else:
																if(lander_y > 0.8759246468544006):
																	if(x_velocity <= -0.0039746804686728865):
																		return True
												else:
													if(y_velocity > -0.25737951695919037):
														if(lander_x <= 0.030249882489442825):
															if(angle <= 0.032342150807380676):
																if(x_velocity <= -0.012385504087433219):
																	return True
														else:
															return True
											else:
												if(y_velocity <= -0.25443829596042633):
													if(angle <= 0.10417304188013077):
														if(angle_velocity > -0.08819719403982162):
															if(x_velocity <= 0.003025089274160564):
																if(lander_y <= 1.0567522048950195):
																	if(angle <= 0.0741884894669056):
																		return True
																else:
																	return True
												else:
													if(angle_velocity <= -0.09558995440602303):
														if(y_velocity <= -0.22947585582733154):
															if(angle_velocity > -0.13757845014333725):
																if(angle > 0.11318513751029968):
																	if(x_velocity <= 0.017923153936862946):
																		return True
														else:
															if(x_velocity <= 0.03917247615754604):
																return True
													else:
														if(x_velocity <= 0.025266282260417938):
															if(lander_y > 0.8956425487995148):
																if(lander_y <= 0.9250913858413696):
																	if(lander_x <= 0.1451617255806923):
																		return True
																else:
																	if(angle_velocity <= -0.08545486629009247):
																		if(angle_velocity <= -0.08999278023838997):
																			return True
																	else:
																		return True
														else:
															if(angle <= 0.12195507436990738):
																if(lander_x > -0.014197825454175472):
																	if(y_velocity <= -0.2534603327512741):
																		if(angle_velocity > -0.06740169413387775):
																			return True
															else:
																if(x_velocity <= 0.08360905200242996):
																	if(y_velocity <= -0.24660468101501465):
																		if(lander_y > 1.2066875100135803):
																			return True
																	else:
																		if(lander_y <= 1.0585106313228607):
																			if(lander_x > 0.14338817447423935):
																				return True
																		else:
																			return True
					else:
						if(x_velocity <= -0.32714836299419403):
							if(y_velocity <= -0.4239038676023483):
								if(angle <= 0.010263814125210047):
									if(lander_y <= 1.3426799178123474):
										return True
								else:
									return True
							else:
								return True
						else:
							if(angle <= -0.004083811771124601):
								if(y_velocity <= -0.3513885885477066):
									if(lander_y > 1.373328447341919):
										if(x_velocity <= -0.3144731968641281):
											if(lander_y <= 1.4056146144866943):
												return True
								else:
									if(lander_y <= 1.3652410507202148):
										return True
									else:
										if(x_velocity <= -0.18263256549835205):
											if(angle <= -0.03330042492598295):
												if(angle_velocity > -0.1117359884083271):
													if(x_velocity > -0.32189711928367615):
														if(y_velocity <= -0.29995226860046387):
															if(angle_velocity > -0.0641060322523117):
																return True
														else:
															return True
											else:
												return True
							else:
								if(y_velocity > -0.24147136509418488):
									if(lander_x <= 0.08810477331280708):
										return True
				else:
					if(angle <= 0.2628934383392334):
						if(lander_y <= 0.7854368686676025):
							return True
						else:
							if(lander_x > 0.1162346825003624):
								if(x_velocity <= -0.18661167472600937):
									if(y_velocity > -0.3029929995536804):
										if(lander_x > 0.22991995513439178):
											return True
					else:
						if(y_velocity <= -0.29137198626995087):
							if(x_velocity <= -0.0018345066928304732):
								if(angle_velocity <= -0.19024939090013504):
									if(lander_y <= 1.1114172339439392):
										if(x_velocity <= -0.2529485374689102):
											return True
										else:
											if(lander_x > 0.2829801142215729):
												if(y_velocity > -0.34217211604118347):
													return True
									else:
										if(y_velocity <= -0.3132486641407013):
											if(x_velocity <= -0.08621768280863762):
												if(angle_velocity <= -0.3131147474050522):
													if(lander_y <= 1.116659939289093):
														return True
													else:
														if(y_velocity > -0.32104529440402985):
															return True
												else:
													return True
										else:
											if(x_velocity <= -0.014863400720059872):
												return True
								else:
									return True
							else:
								if(lander_x > 0.29769958555698395):
									if(lander_y > 1.1944284439086914):
										return True
						else:
							if(angle <= 0.33221641182899475):
								if(x_velocity <= -0.11266310513019562):
									return True
								else:
									if(angle <= 0.284756600856781):
										if(x_velocity <= 0.10586587339639664):
											return True
							else:
								if(x_velocity <= 0.010269048856571317):
									return True
								else:
									if(lander_y <= 1.0403451323509216):
										if(y_velocity <= -0.257622167468071):
											if(angle > 0.5124571323394775):
												return True
										else:
											if(x_velocity <= 0.12006763368844986):
												return True
									else:
										if(x_velocity <= 0.18458912521600723):
											return True
			else:
				if(lander_y <= 0.3988706022500992):
					if(angle_velocity <= -0.005895595299080014):
						if(y_velocity <= -0.23697848618030548):
							if(angle <= -0.03992721438407898):
								if(lander_y <= 0.174763984978199):
									if(y_velocity > -0.2448679730296135):
										if(lander_x <= 0.024794816970825195):
											if(lander_y > 0.058977493084967136):
												return True
								else:
									if(y_velocity > -0.2558140754699707):
										if(x_velocity <= -0.07868277654051781):
											if(angle > -0.08147457987070084):
												return True
										else:
											if(lander_y > 0.37730106711387634):
												return True
						else:
							if(angle <= -0.025198427960276604):
								if(x_velocity <= -0.08618466928601265):
									if(angle > -0.0487993024289608):
										return True
								else:
									if(angle_velocity > -0.027504215016961098):
										if(x_velocity <= -0.03842702694237232):
											if(lander_y > 0.29612164199352264):
												return True
							else:
								if(lander_y <= 0.20550113171339035):
									if(x_velocity <= -0.06678585708141327):
										if(angle > -0.017246378120034933):
											return True
								else:
									if(lander_x > -0.10965194553136826):
										if(angle <= 0.013557164464145899):
											if(angle_velocity > -0.007875385228544474):
												if(y_velocity > -0.2295401468873024):
													return True
					else:
						if(angle_velocity <= 0.1071605421602726):
							if(angle <= -0.007234708871692419):
								if(y_velocity <= -0.23764991760253906):
									if(x_velocity <= -0.13719099014997482):
										if(angle > -0.09720682725310326):
											return True
									else:
										if(angle <= -0.06476367264986038):
											if(y_velocity > -0.2619546800851822):
												if(angle_velocity > 0.03959674946963787):
													return True
										else:
											if(y_velocity > -0.2452927529811859):
												if(lander_y > 0.2798342704772949):
													if(x_velocity <= -0.0206613726913929):
														if(x_velocity <= -0.03133177664130926):
															if(lander_y <= 0.2984888553619385):
																if(angle <= -0.03760555759072304):
																	return True
															else:
																if(x_velocity <= -0.06447276473045349):
																	return True
								else:
									if(lander_y <= 0.26747365295886993):
										if(x_velocity <= -0.0627112053334713):
											if(lander_y <= 0.14145410060882568):
												if(lander_x <= -0.028346871957182884):
													if(y_velocity <= -0.22304968535900116):
														return True
												else:
													if(angle <= -0.05757788009941578):
														return True
													else:
														if(angle_velocity <= -0.002111430570948869):
															return True
											else:
												if(lander_x <= 0.11924776807427406):
													return True
										else:
											if(angle_velocity > 0.005520625039935112):
												if(x_velocity <= -0.05737740360200405):
													if(y_velocity <= -0.23243707418441772):
														return True
									else:
										if(lander_x <= -0.08530726283788681):
											if(x_velocity <= 0.024723042268306017):
												if(lander_y <= 0.2900426834821701):
													if(lander_y <= 0.27483803033828735):
														return True
												else:
													return True
										else:
											if(angle_velocity > 0.001189333685033489):
												if(x_velocity <= -0.009728663600981236):
													if(y_velocity <= -0.23149458318948746):
														if(lander_y <= 0.315429225564003):
															return True
														else:
															if(angle > -0.008066202979534864):
																return True
													else:
														if(angle_velocity <= 0.05043022893369198):
															if(angle > -0.08178627863526344):
																return True
							else:
								if(x_velocity <= -0.05363779328763485):
									if(lander_x <= 0.05827446095645428):
										return True
								else:
									if(y_velocity <= -0.22065309435129166):
										if(y_velocity > -0.2258555367588997):
											if(y_velocity > -0.22582001984119415):
												if(x_velocity <= -0.00616769096814096):
													if(lander_x <= -0.043342018499970436):
														return True
									else:
										if(y_velocity <= -0.22063478827476501):
											return True
						else:
							if(lander_y <= 0.3933049440383911):
								if(x_velocity > -0.06872013211250305):
									return True
				else:
					if(y_velocity <= -0.2591031938791275):
						if(x_velocity <= -0.4677737355232239):
							if(y_velocity > -0.6010503172874451):
								return True
						else:
							if(angle <= -0.05331459268927574):
								if(y_velocity <= -0.28979015350341797):
									if(y_velocity <= -0.32377180457115173):
										if(lander_y <= 1.0612746477127075):
											if(angle <= -0.20151109993457794):
												if(y_velocity <= -0.3569426089525223):
													if(angle_velocity > 0.03919844701886177):
														if(y_velocity <= -0.3872532546520233):
															if(angle > -0.3148250877857208):
																if(lander_y <= 1.037104070186615):
																	if(x_velocity <= -0.31900712847709656):
																		if(y_velocity > -0.4142201989889145):
																			return True
														else:
															if(angle <= -0.23443743586540222):
																if(lander_x > -0.23447678238153458):
																	if(y_velocity > -0.37790706753730774):
																		return True
												else:
													if(angle <= -0.20489487797021866):
														if(angle_velocity > 0.11081285029649734):
															if(y_velocity <= -0.34119923412799835):
																if(x_velocity <= -0.16044805943965912):
																	return True
													else:
														return True
											else:
												if(y_velocity <= -0.3360630124807358):
													if(x_velocity <= -0.3516712188720703):
														if(angle_velocity > -0.006786177633330226):
															return True
													else:
														if(angle_velocity > 0.21774686127901077):
															if(x_velocity <= -0.05380119942128658):
																return True
												else:
													if(angle <= -0.16341836005449295):
														if(angle_velocity <= 0.03856382332742214):
															return True
														else:
															if(angle_velocity > 0.13748598098754883):
																if(angle <= -0.1892790049314499):
																	return True
													else:
														if(angle_velocity <= 0.04832232557237148):
															if(lander_x > -0.10481705516576767):
																if(angle <= -0.0997859351336956):
																	if(lander_y > 0.6811869740486145):
																		if(angle <= -0.1066688820719719):
																			if(lander_x <= -0.08522148057818413):
																				return True
										else:
											if(y_velocity <= -0.3447175920009613):
												if(angle <= -0.14506709575653076):
													if(y_velocity <= -0.3985508531332016):
														if(lander_y > 1.063765048980713):
															if(angle_velocity <= -0.01774553209543228):
																if(x_velocity <= -0.2994004786014557):
																	if(x_velocity > -0.3445555120706558):
																		if(y_velocity > -0.4132232069969177):
																			return True
															else:
																if(lander_y <= 1.3167800903320312):
																	if(lander_x > -0.1942407563328743):
																		if(lander_y > 1.2698836922645569):
																			if(lander_y <= 1.2792267799377441):
																				if(y_velocity > -0.40654876828193665):
																					return True
																else:
																	if(angle_velocity > 0.001375226303935051):
																		if(angle > -0.226822629570961):
																			if(angle <= -0.2175343856215477):
																				return True
													else:
														if(angle <= -0.1828475147485733):
															if(angle_velocity <= 0.04813747853040695):
																if(lander_x <= -0.1620314121246338):
																	if(lander_x > -0.17086639255285263):
																		return True
															else:
																if(lander_y > 1.1418097615242004):
																	return True
														else:
															if(y_velocity <= -0.36406198143959045):
																if(angle_velocity <= 0.005274130031466484):
																	if(y_velocity <= -0.38150131702423096):
																		return True
															else:
																if(angle_velocity > 0.04756132513284683):
																	if(x_velocity <= -0.14022498577833176):
																		return True
												else:
													if(y_velocity > -0.3601759523153305):
														if(y_velocity <= -0.35688579082489014):
															if(y_velocity > -0.3574644923210144):
																return True
											else:
												if(angle <= -0.06962037831544876):
													if(y_velocity <= -0.33256442844867706):
														if(x_velocity <= -0.15777025371789932):
															if(lander_y > 1.1435661315917969):
																return True
													else:
														if(angle_velocity > -0.010737831704318523):
															return True
									else:
										if(lander_y <= 0.9724603593349457):
											if(angle <= -0.13911590725183487):
												if(y_velocity <= -0.3128570020198822):
													if(angle <= -0.16731970012187958):
														if(lander_x > -0.2830394506454468):
															return True
													else:
														if(angle_velocity > 0.05194188840687275):
															if(lander_y > 0.869787186384201):
																return True
												else:
													if(angle_velocity <= 0.15131288766860962):
														if(lander_x <= -0.2863030731678009):
															if(angle_velocity > 0.10642845928668976):
																return True
														else:
															if(lander_y <= 0.6544494330883026):
																if(y_velocity > -0.31085169315338135):
																	if(x_velocity <= -0.15985646098852158):
																		return True
																	else:
																		if(lander_y > 0.6447462141513824):
																			return True
													else:
														if(y_velocity <= -0.3040447533130646):
															return True
											else:
												if(lander_x <= 0.17120051383972168):
													if(angle_velocity <= -0.005081556271761656):
														if(x_velocity <= -0.1315990537405014):
															if(lander_y > 0.7717319130897522):
																return True
													else:
														if(angle <= -0.11836115643382072):
															if(angle_velocity > 0.035113219171762466):
																if(angle <= -0.12105177715420723):
																	if(lander_y > 0.5059874653816223):
																		if(lander_x > 0.0654900074005127):
																			if(x_velocity <= -0.14474781602621078):
																				return True
																else:
																	if(y_velocity > -0.30349576473236084):
																		return True
														else:
															if(angle <= -0.05388873629271984):
																if(lander_y <= 0.9470905959606171):
																	if(y_velocity > -0.30324292182922363):
																		if(y_velocity <= -0.3031436502933502):
																			return True
																		else:
																			if(angle_velocity > 0.001812802569475025):
																				if(x_velocity <= -0.14478172361850739):
																					if(angle_velocity > 0.023746936582028866):
																						if(angle <= -0.0906406044960022):
																							if(angle_velocity <= 0.025198789313435555):
																								return True
																						else:
																							return True
																else:
																	if(angle_velocity > 0.03174198791384697):
																		if(lander_x <= -0.09213199466466904):
																			if(y_velocity > -0.29576967656612396):
																				if(y_velocity <= -0.2923332005739212):
																					return True
																		else:
																			return True
												else:
													if(angle > -0.11172544583678246):
														return True
										else:
											if(x_velocity <= -0.0746455229818821):
												if(angle_velocity <= 0.027894112281501293):
													if(lander_x > -0.08236465603113174):
														if(y_velocity <= -0.31221911311149597):
															return True
														else:
															if(lander_y <= 1.083028793334961):
																return True
												else:
													if(angle <= -0.1307736337184906):
														if(lander_x <= -0.16486988216638565):
															return True
													else:
														if(lander_x <= -0.12311496585607529):
															if(lander_y <= 1.070564091205597):
																return True
														else:
															return True
											else:
												if(y_velocity > -0.2972036898136139):
													return True
								else:
									if(angle_velocity <= 0.05515405908226967):
										if(lander_y <= 0.5726955235004425):
											if(angle <= -0.07068922743201256):
												if(y_velocity > -0.2825336307287216):
													if(x_velocity <= -0.12021123990416527):
														return True
													else:
														if(lander_x > -0.3089955896139145):
															if(y_velocity > -0.26162753999233246):
																return True
											else:
												if(y_velocity > -0.2722477614879608):
													if(angle_velocity > 0.008120624348521233):
														if(x_velocity <= -0.08208607323467731):
															return True
										else:
											if(x_velocity <= -0.06573277339339256):
												if(lander_y <= 0.6902416348457336):
													if(angle_velocity > 0.03395815286785364):
														if(lander_y <= 0.6364759206771851):
															return True
												else:
													if(y_velocity <= -0.2708781063556671):
														if(lander_y <= 1.0126219987869263):
															if(x_velocity <= -0.06814582273364067):
																return True
															else:
																if(lander_y > 0.9211913049221039):
																	return True
											else:
												if(y_velocity <= -0.28788553178310394):
													if(x_velocity <= -0.025965365581214428):
														return True
									else:
										if(lander_y <= 0.7663210034370422):
											if(angle <= -0.10654593259096146):
												if(y_velocity > -0.2830393612384796):
													if(y_velocity <= -0.27401989698410034):
														if(lander_x > -0.2698782831430435):
															return True
													else:
														return True
											else:
												if(x_velocity <= -0.14428503811359406):
													return True
												else:
													if(y_velocity > -0.270984947681427):
														if(lander_y <= 0.5829871296882629):
															if(lander_y <= 0.4420061707496643):
																if(x_velocity <= -0.07857425697147846):
																	return True
														else:
															return True
										else:
											if(x_velocity <= 0.017174482811242342):
												if(y_velocity <= -0.2667526751756668):
													return True
												else:
													if(y_velocity > -0.26349999010562897):
														return True
											else:
												if(y_velocity > -0.27996663749217987):
													if(angle_velocity > 0.1108262650668621):
														return True
							else:
								if(lander_y <= 0.7862126231193542):
									if(y_velocity <= -0.264681339263916):
										if(lander_y <= 0.726870208978653):
											if(x_velocity <= -0.11643403023481369):
												if(x_velocity > -0.12472354620695114):
													return True
											else:
												if(angle_velocity <= 0.0818091630935669):
													if(y_velocity <= -0.2663245052099228):
														if(y_velocity > -0.27826161682605743):
															if(y_velocity > -0.2781319171190262):
																if(x_velocity <= -0.09295184165239334):
																	if(y_velocity > -0.2704695612192154):
																		return True
												else:
													if(angle_velocity <= 0.08660867437720299):
														return True
										else:
											if(lander_y <= 0.7282095849514008):
												if(lander_x > -0.015373898670077324):
													return True
											else:
												if(y_velocity <= -0.27001261711120605):
													if(angle <= -0.036538174375891685):
														if(y_velocity > -0.2824312895536423):
															if(angle_velocity > -0.00475817546248436):
																return True
												else:
													if(angle_velocity <= -0.00363212579395622):
														if(y_velocity > -0.26842033863067627):
															if(y_velocity <= -0.2679774612188339):
																return True
													else:
														if(y_velocity <= -0.26930294930934906):
															if(lander_y <= 0.7515392601490021):
																return True
									else:
										if(angle <= -0.018328707665205002):
											if(lander_y <= 0.6719333529472351):
												if(angle <= -0.020177501253783703):
													if(angle_velocity > -0.015758157707750797):
														if(lander_x > 0.09896249696612358):
															if(angle_velocity > 0.02418297529220581):
																return True
											else:
												if(angle_velocity <= 0.030637436546385288):
													if(y_velocity <= -0.2641945630311966):
														return True
												else:
													if(x_velocity <= 0.023183227516710758):
														if(y_velocity <= -0.26006515324115753):
															return True
														else:
															if(lander_x > 0.010152911767363548):
																return True
										else:
											if(lander_x > 0.15579185634851456):
												if(x_velocity <= -0.061157720163464546):
													return True
								else:
									if(y_velocity <= -0.28120529651641846):
										if(lander_y <= 1.3223260641098022):
											if(x_velocity <= 0.689288318157196):
												if(y_velocity <= -0.29172690212726593):
													if(lander_y <= 1.1302112936973572):
														if(lander_y > 0.7932920157909393):
															if(x_velocity <= -0.10984238237142563):
																if(y_velocity > -0.29639288783073425):
																	return True
															else:
																if(x_velocity <= -0.07861029356718063):
																	if(x_velocity > -0.07864519581198692):
																		return True
													else:
														if(x_velocity <= -0.06834279373288155):
															if(y_velocity > -0.3363427072763443):
																return True
														else:
															if(angle <= 0.032738350331783295):
																if(y_velocity <= -0.2967776656150818):
																	if(lander_x <= 0.054551173001527786):
																		if(y_velocity > -0.31002724170684814):
																			if(x_velocity <= -0.024523289874196053):
																				if(x_velocity <= -0.03669215552508831):
																					if(y_velocity > -0.3072790056467056):
																						if(lander_y > 1.1619901657104492):
																							return True
																else:
																	return True
												else:
													if(angle <= -0.03183910623192787):
														if(angle_velocity <= 0.03209804557263851):
															if(lander_y <= 0.8246901035308838):
																if(lander_y <= 0.8146162927150726):
																	return True
														else:
															if(lander_x > -0.08121781423687935):
																return True
													else:
														if(angle_velocity <= -0.014398808125406504):
															if(angle > -0.00023564865114167333):
																if(lander_x <= -0.005478000617586076):
																	return True
																else:
																	if(x_velocity <= -0.10330203175544739):
																		return True
																	else:
																		if(angle <= 0.31670014560222626):
																			if(angle_velocity <= -0.02983016800135374):
																				return True
																		else:
																			return True
														else:
															if(lander_y <= 1.0982114672660828):
																if(angle > -0.02307185810059309):
																	if(lander_x <= -0.06691999360918999):
																		if(lander_y > 0.9380663931369781):
																			if(lander_x <= -0.06859641149640083):
																				return True
															else:
																if(lander_x <= -0.014168167021125555):
																	if(lander_x > -0.04693288914859295):
																		return True
										else:
											if(x_velocity <= 0.3373533934354782):
												if(angle_velocity <= 0.02754958253353834):
													if(y_velocity <= -0.3092615008354187):
														if(lander_x <= 0.0002729415718931705):
															if(angle_velocity > -0.00404905981849879):
																if(x_velocity <= -0.11783743649721146):
																	return True
																else:
																	if(y_velocity > -0.3257075399160385):
																		return True
													else:
														if(x_velocity <= -0.025174960494041443):
															if(angle > -0.0073786829598248005):
																return True
												else:
													if(x_velocity <= 0.26448947191238403):
														if(lander_x <= -0.007713413331657648):
															if(y_velocity > -0.3825749307870865):
																return True
														else:
															if(y_velocity <= -0.2839295417070389):
																if(angle <= 0.002377282246015966):
																	if(lander_x <= -0.001703500747680664):
																		return True
									else:
										if(angle <= 0.008823844138532877):
											if(x_velocity <= 0.02957223169505596):
												if(angle_velocity <= -0.003948292229324579):
													if(x_velocity <= -0.07307593896985054):
														if(angle > -0.03909788653254509):
															return True
													else:
														if(y_velocity > -0.2766232490539551):
															if(y_velocity > -0.2619604170322418):
																if(angle <= -0.005207735957810655):
																	return True
												else:
													if(lander_y <= 0.8370178639888763):
														if(angle <= -0.03568756766617298):
															return True
														else:
															if(y_velocity > -0.2723460793495178):
																if(lander_y > 0.8015757501125336):
																	return True
													else:
														if(x_velocity <= 0.0015450450009666383):
															if(lander_x <= -0.14837151020765305):
																if(y_velocity > -0.27156203985214233):
																	return True
															else:
																if(lander_x <= 0.03444819524884224):
																	return True
																else:
																	if(lander_x > 0.03544206731021404):
																		return True
														else:
															if(angle_velocity > 0.07028498873114586):
																if(lander_y <= 0.8849963247776031):
																	return True
																else:
																	if(x_velocity > 0.023016029968857765):
																		return True
											else:
												if(lander_y > 0.8839908838272095):
													if(x_velocity <= 0.04417895898222923):
														return True
										else:
											if(x_velocity <= -0.024900871329009533):
												if(lander_y > 0.8975584805011749):
													if(y_velocity <= -0.274201899766922):
														if(lander_y > 1.1256186366081238):
															return True
													else:
														return True
											else:
												if(lander_y > 1.1035210490226746):
													if(angle <= 0.059718646109104156):
														if(x_velocity <= 0.07696686312556267):
															if(angle_velocity > 0.049309903755784035):
																return True
													else:
														if(x_velocity <= 0.016323771327733994):
															return True
														else:
															if(angle <= 0.5938259661197662):
																if(angle <= 0.0917450375854969):
																	if(angle <= 0.08894968032836914):
																		if(angle_velocity > -0.0218551866710186):
																			if(x_velocity <= 0.10189161077141762):
																				if(angle_velocity > 0.07326102256774902):
																					return True
																	else:
																		if(angle_velocity > -0.007655544090084732):
																			return True
																else:
																	if(lander_y <= 1.1470887660980225):
																		if(lander_x > 0.17361994087696075):
																			return True
															else:
																if(x_velocity <= 0.220756433904171):
																	return True
					else:
						if(x_velocity <= 0.0351233147084713):
							if(lander_y <= 0.6716362833976746):
								if(y_velocity <= -0.24182037264108658):
									if(angle <= -0.030423035845160484):
										if(angle_velocity <= 0.012476997915655375):
											if(y_velocity > -0.2574797421693802):
												if(x_velocity <= -0.0958431251347065):
													return True
												else:
													if(lander_y <= 0.6339707970619202):
														if(lander_x <= -0.26393239200115204):
															return True
														else:
															if(angle_velocity > -0.00016509604756720364):
																if(angle > -0.03813371993601322):
																	if(lander_y > 0.441238209605217):
																		if(angle_velocity <= 0.010764136910438538):
																			return True
													else:
														return True
										else:
											if(x_velocity <= -0.04057971388101578):
												if(x_velocity <= -0.06967438757419586):
													return True
												else:
													if(x_velocity > -0.060181522741913795):
														return True
											else:
												if(angle_velocity > 0.06265179812908173):
													if(x_velocity > -0.02495346311479807):
														if(y_velocity <= -0.2550571858882904):
															if(lander_x <= -0.26875877380371094):
																return True
														else:
															return True
									else:
										if(x_velocity <= -0.022938490845263004):
											if(y_velocity <= -0.2510243207216263):
												if(x_velocity <= -0.03385838866233826):
													if(x_velocity <= -0.09269861876964569):
														return True
											else:
												if(lander_y <= 0.5494007766246796):
													if(angle_velocity <= 0.028564566746354103):
														if(angle <= -0.008791954722255468):
															if(lander_x <= 0.0940522663295269):
																if(angle > -0.020844724029302597):
																	if(lander_y > 0.43996697664260864):
																		return True
													else:
														if(y_velocity > -0.24814147502183914):
															return True
												else:
													if(angle <= -0.0006147521489765495):
														if(y_velocity <= -0.2501870170235634):
															if(lander_x > 0.07091212132945657):
																return True
														else:
															return True
													else:
														if(angle_velocity > -0.01710554864257574):
															if(angle > 0.009854057570919394):
																return True
										else:
											if(angle <= 0.0027327592251822352):
												if(angle_velocity > -0.006165155675262213):
													if(y_velocity > -0.24814879894256592):
														if(lander_x <= -0.18955111503601074):
															return True
														else:
															if(lander_x <= 0.0545903705060482):
																if(lander_y > 0.6457645297050476):
																	return True
											else:
												if(angle_velocity > 0.051283856853842735):
													if(angle_velocity <= 0.05207928642630577):
														return True
								else:
									if(angle <= 0.027446957305073738):
										if(angle_velocity <= 0.015449421480298042):
											if(x_velocity <= -0.05134405195713043):
												if(angle_velocity <= -0.01985674723982811):
													if(angle_velocity <= -0.02292475476861):
														return True
												else:
													return True
											else:
												if(lander_y <= 0.519020140171051):
													if(lander_x <= -0.061965130269527435):
														if(angle <= -0.012045792769640684):
															if(x_velocity <= 0.0061883446760475636):
																return True
															else:
																if(lander_x <= -0.17679109424352646):
																	return True
														else:
															if(y_velocity > -0.2332426756620407):
																if(angle > -0.007997591746971011):
																	if(angle <= 0.0037133883452042937):
																		if(x_velocity > 0.010035439161583781):
																			return True
																	else:
																		return True
												else:
													if(x_velocity <= 0.014209448359906673):
														if(lander_x <= 0.05866269953548908):
															if(angle > -0.024396699853241444):
																if(x_velocity <= 0.00514195254072547):
																	return True
																else:
																	if(x_velocity > 0.010421523824334145):
																		return True
														else:
															if(y_velocity > -0.221526637673378):
																return True
													else:
														if(y_velocity <= -0.23830954730510712):
															return True
														else:
															if(lander_y > 0.6105600893497467):
																if(x_velocity > 0.02576621249318123):
																	return True
										else:
											if(y_velocity <= -0.2299792394042015):
												if(x_velocity <= -0.011013717856258154):
													if(angle <= -0.05876550450921059):
														if(angle <= -0.06508327648043633):
															return True
													else:
														if(lander_y > 0.4012627750635147):
															if(y_velocity <= -0.23913636058568954):
																if(y_velocity <= -0.2392851710319519):
																	return True
															else:
																return True
												else:
													if(lander_x <= -0.028031492605805397):
														if(angle_velocity <= 0.05883670784533024):
															if(lander_y > 0.43440139293670654):
																if(angle <= 0.008804187411442399):
																	return True
													else:
														if(y_velocity <= -0.23702511936426163):
															if(lander_x > 0.038957834243774414):
																return True
											else:
												if(angle <= -0.04651179164648056):
													if(angle <= -0.05712807551026344):
														return True
												else:
													if(lander_y <= 0.5853285491466522):
														return True
													else:
														if(lander_x <= 0.00987095944583416):
															return True
									else:
										if(lander_y > 0.5512659549713135):
											if(lander_y <= 0.5924049317836761):
												if(lander_x > 0.02894001081585884):
													return True
							else:
								if(y_velocity <= -0.254315048456192):
									if(lander_y <= 0.805266261100769):
										if(x_velocity <= -0.019964149221777916):
											if(y_velocity <= -0.2566714882850647):
												if(y_velocity <= -0.25739650428295135):
													if(angle > -0.05967635475099087):
														return True
											else:
												return True
										else:
											if(y_velocity <= -0.25867871940135956):
												if(lander_y <= 0.7090049088001251):
													if(angle > -0.026516162790358067):
														return True
											else:
												if(angle <= -0.03542984742671251):
													return True
									else:
										if(y_velocity <= -0.25615353882312775):
											if(angle_velocity <= -0.015440585557371378):
												if(lander_y > 0.825337827205658):
													return True
											else:
												return True
										else:
											if(lander_x <= 0.03419036790728569):
												if(lander_x <= 0.028237628750503063):
													if(x_velocity > 0.022617443464696407):
														if(angle_velocity > 0.003099274355918169):
															return True
											else:
												return True
								else:
									if(angle <= -0.02805306576192379):
										if(lander_y > 0.7217203080654144):
											if(lander_y <= 0.7736753225326538):
												return True
											else:
												if(angle <= -0.04144858382642269):
													return True
									else:
										if(angle <= 0.00988092040643096):
											if(angle <= 0.008488973136991262):
												if(angle_velocity <= 0.018945268355309963):
													if(x_velocity <= -0.05272674560546875):
														return True
													else:
														if(lander_x <= -0.008359670639038086):
															if(x_velocity <= 0.0004283926245989278):
																if(lander_x <= -0.022936105728149414):
																	return True
																else:
																	if(lander_y > 1.0335189700126648):
																		return True
															else:
																if(lander_x <= -0.12854037433862686):
																	return True
												else:
													if(angle_velocity <= 0.06711917370557785):
														return True
													else:
														if(angle_velocity > 0.07086296379566193):
															return True
										else:
											if(lander_y <= 0.6982258856296539):
												if(y_velocity > -0.24224982410669327):
													return True
											else:
												if(y_velocity <= -0.25035081803798676):
													if(lander_y > 0.8034637272357941):
														if(y_velocity <= -0.25065740942955017):
															return True
												else:
													if(angle <= 0.01460183598101139):
														if(angle <= 0.014256236143410206):
															return True
													else:
														return True
						else:
							if(lander_y <= 0.6493006646633148):
								if(angle_velocity > -0.006822241935878992):
									if(angle <= 0.013355567120015621):
										if(y_velocity <= -0.23322056233882904):
											if(angle_velocity > 0.00859047519043088):
												if(lander_x <= -0.3024490624666214):
													if(lander_y <= 0.5087575167417526):
														return True
										else:
											if(lander_y <= 0.5424078404903412):
												if(x_velocity <= 0.09163873642683029):
													if(x_velocity > 0.04795690439641476):
														if(angle_velocity > 0.0155371087603271):
															if(y_velocity > -0.22487520426511765):
																return True
											else:
												if(angle_velocity > 0.02319413097575307):
													return True
									else:
										if(y_velocity > -0.22986306250095367):
											if(lander_y <= 0.6228525638580322):
												if(lander_y > 0.5419533252716064):
													if(angle <= 0.03544514626264572):
														return True
											else:
												return True
							else:
								if(angle <= 0.131209097802639):
									if(lander_y <= 0.7742876708507538):
										if(y_velocity <= -0.22755412012338638):
											if(angle_velocity > -0.008942980319261551):
												if(angle <= 0.015457208268344402):
													if(angle_velocity <= 0.07502374239265919):
														if(y_velocity > -0.24598274379968643):
															if(lander_x <= -0.18042293190956116):
																if(lander_x > -0.21004779636859894):
																	return True
													else:
														return True
												else:
													if(x_velocity <= 0.046755023300647736):
														if(x_velocity > 0.03802955523133278):
															return True
													else:
														if(y_velocity <= -0.228505440056324):
															if(angle_velocity > 0.0038729080697521567):
																if(angle_velocity > 0.060446394607424736):
																	if(lander_x > -0.14861049503087997):
																		return True
										else:
											if(angle_velocity <= 0.026497455313801765):
												if(lander_y > 0.6824868023395538):
													if(y_velocity > -0.22351376712322235):
														return True
											else:
												return True
									else:
										if(y_velocity <= -0.24771227687597275):
											if(angle <= 0.02712376043200493):
												if(angle_velocity > 0.044933730736374855):
													if(lander_y <= 0.8468361496925354):
														if(y_velocity > -0.2513609975576401):
															return True
													else:
														if(x_velocity <= 0.042589107528328896):
															if(lander_y > 0.9715511798858643):
																return True
														else:
															if(angle_velocity > 0.08546962589025497):
																return True
											else:
												if(x_velocity <= 0.06934664398431778):
													if(lander_y > 1.0812788605690002):
														return True
												else:
													if(angle_velocity > 0.013977652648463845):
														if(lander_y <= 1.3851042985916138):
															if(angle > 0.11550601944327354):
																if(lander_y > 1.3562791347503662):
																	return True
										else:
											if(lander_y <= 1.3818557262420654):
												if(angle_velocity <= 0.034344857558608055):
													if(lander_y > 0.847799152135849):
														if(lander_x > -0.04421668127179146):
															if(x_velocity <= 0.06390602700412273):
																return True
															else:
																if(x_velocity > 0.06762076169252396):
																	if(lander_x > 0.03119287546724081):
																		return True
												else:
													if(x_velocity <= 0.040507689118385315):
														if(angle > -0.006548960052896291):
															return True
													else:
														return True
											else:
												if(x_velocity <= 0.12040232121944427):
													return True
								else:
									if(x_velocity <= 0.29419660568237305):
										if(angle <= 0.4251032918691635):
											if(y_velocity <= -0.23989219963550568):
												if(lander_x <= 0.041028356179594994):
													return True
											else:
												if(x_velocity <= 0.2217264175415039):
													if(lander_y > 1.1297022700309753):
														if(angle <= 0.16237346082925797):
															if(angle <= 0.15144534409046173):
																return True
														else:
															return True
										else:
											if(y_velocity > -0.2537519484758377):
												if(angle_velocity > 0.009572558104991913):
													if(x_velocity <= 0.2756223827600479):
														if(angle_velocity <= 0.19462165236473083):
															return True
														else:
															if(lander_x <= 0.20777478069067):
																return True
													else:
														if(y_velocity > -0.22703466564416885):
															return True
		else:
			if(angle_velocity <= -0.010854553431272507):
				if(right_leg_contact != True):
					if(angle <= 0.06201705522835255):
						if(angle_velocity <= -0.035603923723101616):
							if(x_velocity <= -0.049048325046896935):
								if(angle <= -0.018289437517523766):
									if(x_velocity > -0.3122575879096985):
										if(x_velocity <= -0.051378997042775154):
											if(x_velocity <= -0.09737235680222511):
												if(angle_velocity <= -0.06120913475751877):
													if(x_velocity <= -0.2234330028295517):
														if(angle_velocity > -0.1633089929819107):
															if(x_velocity > -0.3115724176168442):
																return True
												else:
													return True
										else:
											return True
								else:
									if(y_velocity > -0.2162977084517479):
										if(lander_x <= 0.10602355003356934):
											if(lander_y <= 0.07603959739208221):
												if(x_velocity <= -0.0640704408288002):
													return True
											else:
												return True
										else:
											if(lander_y > 0.011788675794377923):
												if(y_velocity > -0.18697983026504517):
													return True
							else:
								if(angle_velocity <= -0.052182361483573914):
									if(angle <= 0.0359882228076458):
										if(lander_y > 0.6568058431148529):
											if(angle > 0.009671386913396418):
												return True
									else:
										if(angle_velocity > -0.06976191699504852):
											if(angle_velocity > -0.06222432106733322):
												if(x_velocity <= 0.043531442526727915):
													return True
								else:
									if(lander_x <= -0.1753547191619873):
										if(y_velocity <= -0.2071043848991394):
											if(angle <= -0.0018436736281728372):
												if(lander_x <= -0.19440116733312607):
													return True
										else:
											if(lander_y <= 0.31869086623191833):
												if(angle_velocity <= -0.04627278633415699):
													return True
											else:
												return True
									else:
										if(x_velocity <= 0.02934814989566803):
											if(angle <= 0.024723194539546967):
												if(lander_x <= -0.07197494432330132):
													if(angle > -0.01471952348947525):
														if(x_velocity <= 0.007668731268495321):
															if(lander_y > 0.1319637969136238):
																return True
														else:
															if(angle > 0.011623566970229149):
																return True
												else:
													if(left_leg_contact != True):
														if(angle <= 0.01774296723306179):
															if(x_velocity <= -0.034288011491298676):
																if(angle_velocity <= -0.045387158170342445):
																	return True
														else:
															if(lander_x <= 0.05536680109798908):
																if(x_velocity > -0.003545665182173252):
																	return True
											else:
												if(lander_y <= 0.17466771602630615):
													if(y_velocity > -0.18647807836532593):
														return True
												else:
													if(lander_y > 0.27532683312892914):
														return True
										else:
											if(angle <= 0.058603471145033836):
												if(lander_y <= 0.5580495595932007):
													if(y_velocity > -0.1641298085451126):
														return True
												else:
													return True
						else:
							if(x_velocity <= 0.002305949805304408):
								if(lander_y <= 0.17234846204519272):
									if(y_velocity <= -0.1974310204386711):
										if(angle <= -0.0044709129724651575):
											if(lander_x <= -0.16076922416687012):
												return True
											else:
												if(x_velocity <= -0.07829222083091736):
													return True
												else:
													if(angle > -0.021579984575510025):
														if(angle <= -0.00968098221346736):
															if(y_velocity > -0.2120053917169571):
																return True
									else:
										if(angle <= -0.0011818526545539498):
											if(x_velocity <= -0.04211076907813549):
												if(y_velocity <= -0.18710999935865402):
													return True
										else:
											return True
								else:
									if(lander_x <= 0.07196741178631783):
										if(y_velocity > -0.2186787948012352):
											if(angle_velocity <= -0.011381357908248901):
												if(y_velocity <= -0.2059616968035698):
													return True
												else:
													if(y_velocity <= -0.20232993364334106):
														if(angle <= -0.011455237166956067):
															return True
														else:
															if(x_velocity <= -0.020496421959251165):
																return True
													else:
														return True
									else:
										if(x_velocity <= -0.06836742162704468):
											return True
							else:
								if(lander_y <= 0.21626899391412735):
									if(y_velocity <= -0.18917064368724823):
										if(angle <= 0.005225776461884379):
											if(angle > -0.010194838978350163):
												if(x_velocity <= 0.02813156321644783):
													if(lander_x <= -0.048626137897372246):
														if(x_velocity <= 0.005624378565698862):
															return True
										else:
											if(x_velocity <= 0.07935518398880959):
												if(lander_y > 0.1443529948592186):
													if(lander_x <= -0.027375363744795322):
														if(lander_y <= 0.1602785587310791):
															return True
									else:
										if(lander_x <= -0.0855782963335514):
											if(x_velocity <= 0.05733836628496647):
												if(angle <= -0.003876910370308906):
													if(y_velocity > -0.1745867356657982):
														return True
												else:
													return True
										else:
											if(angle <= 0.045848630368709564):
												if(y_velocity <= -0.18624678254127502):
													if(lander_y > 0.11104568094015121):
														if(y_velocity > -0.18801934272050858):
															return True
												else:
													if(lander_y <= 0.043340716511011124):
														if(lander_y > 0.034660836681723595):
															return True
											else:
												if(y_velocity <= -0.1697707325220108):
													if(lander_x > 0.007307147607207298):
														return True
												else:
													if(x_velocity <= 0.0822056233882904):
														return True
								else:
									if(lander_x <= -0.04364814795553684):
										if(x_velocity <= 0.061992842704057693):
											if(y_velocity <= -0.20960137993097305):
												if(angle > 0.003252117079682648):
													if(lander_y <= 0.4394170939922333):
														if(lander_x <= -0.19607630372047424):
															return True
														else:
															if(x_velocity <= 0.01444409042596817):
																return True
													else:
														if(angle_velocity > -0.0245559960603714):
															return True
											else:
												if(angle_velocity <= -0.01183604821562767):
													if(angle_velocity <= -0.023065774701535702):
														if(y_velocity <= -0.18910478800535202):
															if(angle_velocity <= -0.03213549219071865):
																return True
														else:
															return True
													else:
														return True
									else:
										if(x_velocity <= 0.010280539281666279):
											if(x_velocity > 0.008855934720486403):
												return True
										else:
											if(lander_y > 0.6267885267734528):
												if(angle > 0.016695001628249884):
													return True
					else:
						if(y_velocity <= -0.17376063019037247):
							if(angle > 0.0821714960038662):
								if(x_velocity <= 0.1566612273454666):
									if(angle_velocity <= -0.11321457102894783):
										if(lander_y > 1.1185217499732971):
											if(y_velocity > -0.21329336613416672):
												if(x_velocity <= 0.13447826355695724):
													return True
									else:
										if(lander_y <= 1.0543045401573181):
											if(y_velocity > -0.21630842983722687):
												return True
										else:
											if(lander_x <= 0.07900691032409668):
												if(y_velocity <= -0.2166367694735527):
													return True
											else:
												return True
								else:
									if(angle_velocity > -0.1363706737756729):
										if(y_velocity > -0.19166146963834763):
											if(lander_y <= 1.386024832725525):
												if(x_velocity <= 0.2562812268733978):
													return True
												else:
													if(lander_x <= 0.18224620819091797):
														return True
											else:
												if(angle > 0.35339273512363434):
													return True
						else:
							if(lander_y <= 0.32353532314300537):
								if(x_velocity <= 0.13265391439199448):
									if(y_velocity <= -0.16440926492214203):
										if(y_velocity <= -0.17137716710567474):
											return True
									else:
										return True
							else:
								if(angle_velocity <= -0.13533566892147064):
									if(x_velocity <= 0.2214430645108223):
										return True
								else:
									return True
			else:
				if(lander_y <= 0.2456214353442192):
					if(y_velocity <= -0.18587703257799149):
						if(x_velocity <= 0.018928966484963894):
							if(y_velocity <= -0.20360344648361206):
								if(x_velocity <= -0.02664847020059824):
									if(left_leg_contact != True):
										if(angle_velocity <= 0.0043722393456846476):
											if(lander_x <= 0.06290278211236):
												if(angle <= -0.05439945496618748):
													if(angle <= -0.07327098399400711):
														return True
												else:
													return True
										else:
											return True
								else:
									if(lander_y <= 0.18653695285320282):
										if(lander_x <= -0.1305283084511757):
											if(y_velocity > -0.213547945022583):
												if(left_leg_contact != True):
													return True
										else:
											if(lander_y > 0.0018440998392179608):
												if(angle_velocity <= -0.0051151760853827):
													if(lander_y > 0.12370817363262177):
														if(y_velocity > -0.2048422396183014):
															return True
												else:
													if(x_velocity <= -0.0147034777328372):
														if(angle_velocity <= 0.05712492577731609):
															if(y_velocity > -0.20699603855609894):
																return True
														else:
															return True
									else:
										if(lander_x <= -0.03983144648373127):
											return True
										else:
											if(y_velocity > -0.21081820875406265):
												if(x_velocity <= 0.009407946839928627):
													if(angle_velocity > 0.004333603545092046):
														return True
							else:
								if(angle_velocity <= -0.005452348385006189):
									if(angle > -0.0012260186485946178):
										if(angle_velocity <= -0.009282009676098824):
											if(angle_velocity <= -0.010182993952184916):
												return True
								else:
									if(lander_y > 0.004058173857629299):
										if(angle <= 0.019453133456408978):
											if(x_velocity <= 0.018647784367203712):
												if(x_velocity <= -0.0010153257171623409):
													return True
												else:
													if(angle_velocity <= 0.013525543734431267):
														if(y_velocity > -0.19654496759176254):
															return True
													else:
														if(lander_y > 0.010608843760564923):
															if(lander_x <= 0.06910615041851997):
																return True
															else:
																if(angle > 0.009757897583767772):
																	return True
										else:
											if(y_velocity <= -0.19190432876348495):
												if(lander_x <= 0.04047045577317476):
													return True
											else:
												return True
						else:
							if(angle <= 0.010951127856969833):
								if(y_velocity <= -0.20143694430589676):
									if(angle <= -0.030738230794668198):
										if(angle_velocity > 0.028853715397417545):
											return True
									else:
										if(angle_velocity > -0.0014800538774579763):
											if(angle <= -0.014598495326936245):
												if(lander_x > -0.11413297429680824):
													if(angle <= -0.019936557859182358):
														return True
								else:
									if(lander_y <= 0.1378457024693489):
										if(angle <= -0.010311076417565346):
											if(angle_velocity > 0.029651219956576824):
												return True
										else:
											if(angle_velocity > -0.004529626341536641):
												if(angle <= -0.004287490737624466):
													if(angle_velocity <= 0.06631219387054443):
														if(angle > -0.009036874398589134):
															return True
												else:
													if(angle_velocity > 0.0691668651998043):
														if(angle_velocity <= 0.24349431693553925):
															return True
									else:
										if(y_velocity <= -0.19555621594190598):
											if(x_velocity <= 0.05857863835990429):
												return True
										else:
											if(lander_x <= -0.03502068482339382):
												if(x_velocity <= 0.04528339020907879):
													return True
							else:
								if(right_leg_contact != True):
									if(lander_y > 0.14798488467931747):
										if(angle_velocity > -0.0038335329154506326):
											if(y_velocity <= -0.20047180354595184):
												if(angle <= 0.01672883704304695):
													if(angle > 0.016196143813431263):
														return True
											else:
												if(angle <= 0.0336521752178669):
													if(angle_velocity <= 0.030562994070351124):
														if(y_velocity <= -0.19980782270431519):
															return True
													else:
														if(angle_velocity <= 0.07024921476840973):
															if(angle_velocity <= 0.04628653638064861):
																if(angle_velocity > 0.043115682899951935):
																	if(y_velocity <= -0.18773110210895538):
																		return True
														else:
															return True
												else:
													if(x_velocity <= 0.054850198328495026):
														if(x_velocity > 0.04581424593925476):
															return True
								else:
									if(x_velocity <= 0.04395904578268528):
										return True
					else:
						if(x_velocity <= 0.07906698435544968):
							if(left_leg_contact != True):
								if(x_velocity <= 0.05338051915168762):
									if(angle <= -0.010246748104691505):
										if(angle_velocity <= 0.02813830692321062):
											if(x_velocity <= -0.0043573916191235185):
												return True
										else:
											return True
									else:
										if(lander_y <= 0.010773012414574623):
											if(lander_y <= 0.004012576304376125):
												return True
										else:
											if(lander_x <= 0.1222846508026123):
												if(angle <= 0.048809004947543144):
													if(angle <= 0.006585653172805905):
														if(angle <= 0.006035603350028396):
															return True
													else:
														return True
												else:
													if(angle > 0.05020749568939209):
														return True
											else:
												if(x_velocity <= -0.016186186112463474):
													return True
								else:
									if(y_velocity <= -0.17120373994112015):
										if(lander_x <= -0.03570122644305229):
											if(angle_velocity > 0.018130283802747726):
												if(angle > -0.011443637544289231):
													return True
										else:
											if(lander_y <= 0.16543927043676376):
												if(y_velocity <= -0.1722951903939247):
													if(angle_velocity > 0.04081559181213379):
														return True
									else:
										if(angle_velocity <= -0.0038011515280231833):
											if(y_velocity > -0.15989500284194946):
												return True
										else:
											return True
							else:
								if(angle_velocity <= 0.4526590257883072):
									if(angle > -0.007183142472058535):
										if(angle > 0.09468194097280502):
											return True
								else:
									return True
						else:
							if(y_velocity <= -0.16376685351133347):
								if(angle_velocity > -0.006967407651245594):
									if(angle_velocity <= 0.07804835960268974):
										if(lander_y <= 0.1487085074186325):
											if(lander_y <= -0.005065127625130117):
												return True
											else:
												if(angle <= 0.049094974994659424):
													if(angle <= 0.046546122059226036):
														if(x_velocity > 0.09626342356204987):
															if(angle_velocity > 0.04645492136478424):
																if(angle_velocity <= 0.0490306057035923):
																	return True
																else:
																	if(y_velocity > -0.17212731391191483):
																		if(lander_x <= -0.23703859001398087):
																			return True
										else:
											if(y_velocity <= -0.17225368320941925):
												if(angle <= 0.03927383664995432):
													return True
											else:
												return True
									else:
										return True
							else:
								if(x_velocity <= 0.08246087282896042):
									if(lander_y <= 0.08970695361495018):
										return True
								else:
									if(x_velocity <= 0.14585117995738983):
										return True
									else:
										if(y_velocity <= -0.1420469731092453):
											if(lander_y > 0.04941176995635033):
												if(lander_y > 0.07711452059447765):
													if(angle_velocity > 0.02045962167903781):
														return True
										else:
											return True
				else:
					if(x_velocity <= 0.08962250128388405):
						if(y_velocity <= -0.2100314348936081):
							if(x_velocity <= 0.013507533818483353):
								if(angle_velocity <= -0.0003657425886558485):
									if(lander_x <= -0.002429866697639227):
										if(angle <= 0.0009894473478198051):
											return True
									else:
										if(lander_y <= 0.2888552248477936):
											return True
								else:
									if(y_velocity <= -0.2182958945631981):
										if(lander_y <= 0.31259019672870636):
											if(angle <= -0.008802084950730205):
												if(lander_y <= 0.27899427711963654):
													return True
										else:
											if(angle_velocity > 0.003876933013089001):
												if(y_velocity <= -0.21834351867437363):
													return True
									else:
										if(x_velocity <= -0.0056305848993361):
											return True
										else:
											if(x_velocity > -0.003742182394489646):
												if(lander_y <= 0.30085957050323486):
													if(y_velocity <= -0.21470963954925537):
														return True
												else:
													return True
							else:
								if(lander_y <= 0.4193870723247528):
									if(angle <= -0.001474948861869052):
										if(angle <= -0.016262791585177183):
											return True
										else:
											if(angle_velocity > 0.04632934741675854):
												if(lander_y > 0.3065548688173294):
													return True
									else:
										if(angle_velocity <= 0.0005050814943388104):
											if(x_velocity <= 0.051337866112589836):
												if(lander_y > 0.3735746890306473):
													return True
										else:
											if(y_velocity > -0.21081842482089996):
												if(angle_velocity <= 0.02686710422858596):
													return True
								else:
									if(lander_x <= 0.029781436547636986):
										if(y_velocity <= -0.21131696552038193):
											if(angle > -0.01164768310263753):
												if(y_velocity <= -0.21611396223306656):
													if(lander_y > 0.49484284222126007):
														if(x_velocity <= 0.07839666306972504):
															return True
														else:
															if(lander_x <= -0.16721048206090927):
																return True
												else:
													return True
										else:
											if(angle_velocity > 0.028776037506759167):
												if(lander_y <= 1.308901071548462):
													return True
									else:
										if(lander_y > 0.5562295019626617):
											if(lander_y > 0.7017165124416351):
												return True
						else:
							if(x_velocity <= 0.07109396904706955):
								if(lander_y <= 0.3324655741453171):
									if(y_velocity <= -0.20063641667366028):
										if(angle <= 0.018269051797688007):
											if(lander_x <= -0.041123056784272194):
												return True
											else:
												if(x_velocity <= 0.013495360501110554):
													if(angle_velocity <= 0.008620021399110556):
														if(angle > -6.578245665878057e-05):
															return True
													else:
														return True
										else:
											if(angle <= 0.023812297731637955):
												if(angle > 0.020734618417918682):
													return True
									else:
										if(angle_velocity > -0.00905592879280448):
											if(lander_x <= 0.08181328698992729):
												if(x_velocity <= 0.05668545141816139):
													if(y_velocity <= -0.19879302382469177):
														if(y_velocity <= -0.19897308200597763):
															return True
													else:
														return True
												else:
													if(angle_velocity > 0.028413920663297176):
														return True
											else:
												if(lander_x > 0.08230986446142197):
													return True
								else:
									if(y_velocity <= -0.14808505773544312):
										if(lander_y <= 1.4096754789352417):
											if(x_velocity <= 0.03250040113925934):
												return True
											else:
												if(x_velocity > 0.03326038084924221):
													if(lander_y <= 1.0460107028484344):
														if(lander_y <= 0.5858725905418396):
															return True
														else:
															if(lander_y > 0.5930267870426178):
																return True
										else:
											if(x_velocity > 0.03156116837635636):
												return True
							else:
								if(angle_velocity <= 0.007354301633313298):
									if(lander_x <= -0.1750681847333908):
										return True
								else:
									if(lander_x <= -0.08735213428735733):
										return True
									else:
										if(angle > 0.05054444633424282):
											return True
					else:
						if(y_velocity <= -0.17320022732019424):
							if(x_velocity <= 0.3846900016069412):
								if(angle_velocity <= 0.08039089664816856):
									if(lander_y <= 0.4670753479003906):
										if(angle <= 0.05356734059751034):
											if(y_velocity <= -0.18619784712791443):
												if(lander_x <= -0.24747539311647415):
													if(angle_velocity > 0.004820773145183921):
														if(lander_y <= 0.43625740706920624):
															if(angle_velocity > 0.04857376217842102):
																if(angle <= 0.026115651009604335):
																	return True
											else:
												if(angle <= 0.04843461699783802):
													return True
									else:
										if(x_velocity <= 0.26192905008792877):
											if(lander_y <= 0.6769025325775146):
												if(y_velocity <= -0.2017100751399994):
													if(angle <= 0.05155929550528526):
														if(angle_velocity > 0.032015779055655):
															return True
												else:
													return True
											else:
												if(x_velocity > 0.09086872637271881):
													return True
										else:
											if(y_velocity > -0.18212506920099258):
												if(x_velocity <= 0.3377969115972519):
													return True
								else:
									if(lander_y <= 1.3846285939216614):
										if(y_velocity <= -0.2153453752398491):
											if(angle_velocity <= 0.23447684198617935):
												if(x_velocity <= 0.14172151684761047):
													return True
												else:
													if(angle <= 0.2707720771431923):
														if(x_velocity <= 0.1658013015985489):
															if(lander_x > -0.09793412312865257):
																return True
													else:
														if(lander_y > 1.1619606614112854):
															return True
											else:
												return True
										else:
											if(y_velocity <= -0.20936059206724167):
												if(lander_y > 0.5769548416137695):
													if(y_velocity <= -0.20969827473163605):
														if(angle_velocity <= 0.28310975432395935):
															return True
														else:
															if(x_velocity <= 0.3066330552101135):
																return True
											else:
												if(lander_y <= 0.46398530900478363):
													if(lander_y <= 0.4484563171863556):
														return True
												else:
													return True
									else:
										if(angle_velocity > 0.1266830489039421):
											if(x_velocity <= 0.224543996155262):
												if(lander_x > 0.0231489185243845):
													return True
							else:
								if(angle > 0.1528271809220314):
									if(angle > 0.38715721666812897):
										if(x_velocity <= 0.42747414112091064):
											if(y_velocity > -0.20557909458875656):
												return True
										else:
											if(angle_velocity > 0.38150255382061005):
												return True
						else:
							if(x_velocity <= 0.5413434505462646):
								if(lander_y <= 1.4870757460594177):
									if(angle > 0.0240612612105906):
										if(x_velocity <= 0.520891547203064):
											if(lander_y <= 1.4652548432350159):
												if(lander_x <= -0.25273650884628296):
													if(lander_x <= -0.2589814364910126):
														return True
												else:
													if(y_velocity <= -0.14577040076255798):
														return True
													else:
														if(angle > 0.2433258295059204):
															return True
											else:
												if(y_velocity > -0.1625053510069847):
													return True
										else:
											if(y_velocity > -0.15388526767492294):
												return True
								else:
									if(x_velocity <= 0.44563575088977814):
										return True
	else:
		if(y_velocity <= -0.00010637535888236016):
			if(angle <= 0.10152852162718773):
				if(lander_y <= 0.04580237716436386):
					if(angle_velocity <= 0.48136158287525177):
						if(right_leg_contact != True):
							if(angle_velocity <= 0.1452050693333149):
								if(y_velocity <= -0.00044665002496913075):
									if(lander_x <= -0.16949333995580673):
										if(lander_x <= -0.1700868085026741):
											return True
										else:
											if(y_velocity <= -0.0005231824179645628):
												return True
									else:
										if(x_velocity <= 0.11339053511619568):
											if(lander_x <= -0.13660965114831924):
												if(angle_velocity <= 0.023821291513741016):
													if(angle_velocity > 0.0022404646733775735):
														if(angle <= 0.09779782965779305):
															if(angle_velocity > 0.0031157652847468853):
																if(angle <= 0.0957130566239357):
																	if(y_velocity <= -0.0013466599630191922):
																		if(lander_x <= -0.1653372272849083):
																			return True
																		else:
																			if(y_velocity <= -0.0017541252309456468):
																				if(angle <= 0.0891181118786335):
																					if(y_velocity <= -0.0026475487975403666):
																						if(lander_y <= -0.011308970395475626):
																							return True
																						else:
																							if(y_velocity <= -0.0032512116013094783):
																								if(angle <= 0.07668516412377357):
																									if(x_velocity <= -0.03841491602361202):
																										if(lander_x <= -0.1522982120513916):
																											return True
																										else:
																											if(y_velocity <= -0.004972377559170127):
																												if(lander_y <= -0.008437450975179672):
																													return True
																												else:
																													if(lander_y <= -0.007270439760759473):
																														if(y_velocity <= -0.00610409677028656):
																															return True
																								else:
																									return True
																					else:
																						if(lander_y <= -0.01185235008597374):
																							if(x_velocity <= -0.02051302045583725):
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
								if(lander_y > -0.012606015428900719):
									return True
					else:
						return True
				else:
					if(x_velocity <= 0.22380287945270538):
						if(angle <= 0.000588659371715039):
							if(y_velocity <= -0.09979284182190895):
								if(angle > -0.00119297718629241):
									return True
						else:
							if(lander_x <= 0.0010599136294331402):
								return True
							else:
								if(angle_velocity <= 0.16573119163513184):
									if(x_velocity <= 0.0771014615893364):
										if(lander_x > 0.002822351409122348):
											return True
								else:
									if(y_velocity <= -0.03173424582928419):
										return True
			else:
				if(x_velocity <= -0.005076864268630743):
					if(lander_y <= -0.040867967531085014):
						if(lander_y <= -0.04322237707674503):
							return True
						else:
							if(x_velocity <= -0.006252878112718463):
								if(lander_x <= -0.22876594215631485):
									return True
								else:
									if(angle_velocity > 0.005053321830928326):
										if(lander_y <= -0.04223550297319889):
											return True
										else:
											if(y_velocity <= -0.003313863999210298):
												return True
											else:
												if(lander_y <= -0.04185234010219574):
													if(angle_velocity <= 0.007289826404303312):
														if(x_velocity > -0.013963682111352682):
															if(lander_y > -0.04213329218327999):
																return True
													else:
														return True
							else:
								if(lander_x <= -0.2916949987411499):
									return True
					else:
						if(angle_velocity <= 0.032445382326841354):
							if(lander_y <= -0.030225195921957493):
								if(lander_x <= -0.24702756106853485):
									if(angle_velocity > 0.002535531297326088):
										if(lander_y <= -0.040405914187431335):
											if(lander_x <= -0.2901028096675873):
												return True
											else:
												if(angle_velocity <= 0.003162378096021712):
													if(lander_x > -0.2899189591407776):
														if(lander_x <= -0.28955352306365967):
															return True
												else:
													return True
										else:
											if(y_velocity <= -0.001300012692809105):
												if(lander_y <= -0.0399930514395237):
													return True
												else:
													if(y_velocity <= -0.009448048658668995):
														return True
													else:
														if(y_velocity <= -0.0020027427235618234):
															if(angle <= 0.27492058277130127):
																if(x_velocity <= -0.02388850599527359):
																	if(angle <= 0.271944522857666):
																		if(lander_y <= -0.03183153457939625):
																			if(angle_velocity <= 0.02463008649647236):
																				if(lander_y <= -0.03319629654288292):
																					if(x_velocity <= -0.06756819784641266):
																						return True
																					else:
																						if(angle_velocity > 0.008943982422351837):
																							if(lander_y <= -0.03799544833600521):
																								return True
																							else:
																								if(x_velocity <= -0.034321149811148643):
																									if(lander_x <= -0.27617640793323517):
																										return True
																									else:
																										if(y_velocity <= -0.004396326374262571):
																											if(lander_x <= -0.2724975496530533):
																												return True
																											else:
																												if(y_velocity <= -0.005186355905607343):
																													if(lander_x <= -0.2676380127668381):
																														return True
																													else:
																														if(angle_velocity > 0.018718767911195755):
																															if(lander_y <= -0.034252943471074104):
																																return True
																			else:
																				return True
																	else:
																		return True
															else:
																return True
														else:
															if(lander_x <= -0.28642332553863525):
																if(x_velocity <= -0.014965435490012169):
																	return True
								else:
									if(y_velocity <= -0.00414756964892149):
										if(lander_x <= -0.2216823771595955):
											return True
										else:
											if(x_velocity <= -0.03225703351199627):
												if(angle <= 0.2706599235534668):
													if(angle_velocity > 0.0208817757666111):
														if(y_velocity > -0.01039180625230074):
															if(lander_x <= -0.2161952704191208):
																return True
															else:
																if(x_velocity <= -0.046815114095807076):
																	if(x_velocity <= -0.05645548179745674):
																		return True
																	else:
																		if(lander_x <= -0.21385163813829422):
																			return True
																		else:
																			if(lander_x <= -0.2128172591328621):
																				if(lander_y > -0.036792315542697906):
																					return True
												else:
													return True
						else:
							if(angle > 0.12490641325712204):
								if(y_velocity <= -0.016846172511577606):
									if(angle <= 0.16777461767196655):
										if(angle <= 0.16400884836912155):
											if(lander_y <= -0.020555618219077587):
												return True
											else:
												if(lander_y > -0.019934686832129955):
													return True
									else:
										return True
								else:
									if(lander_x <= -0.19663996249437332):
										if(lander_x <= -0.20542516559362411):
											return True
										else:
											if(x_velocity <= -0.07825136929750443):
												if(lander_y <= -0.031701572239398956):
													return True
												else:
													if(lander_y > -0.03137205448001623):
														return True
				else:
					if(x_velocity <= -0.0014448040747083724):
						if(x_velocity <= -0.002252619480714202):
							if(lander_y <= -0.041341789066791534):
								if(lander_x <= -0.23093562573194504):
									return True
								else:
									if(y_velocity <= -0.0007678197580389678):
										if(angle_velocity <= 0.0023570136399939656):
											return True
							else:
								if(right_leg_contact != True):
									if(lander_y <= -0.01395166153088212):
										return True
									else:
										if(angle_velocity > 0.0009756921208463609):
											return True
								else:
									if(lander_x <= -0.2923773229122162):
										if(angle_velocity > 0.001023857417749241):
											return True
									else:
										if(x_velocity <= -0.005046358564868569):
											return True
						else:
							if(angle > 0.10238726437091827):
								if(x_velocity <= -0.0015063146129250526):
									if(angle_velocity <= 0.0009597683092579246):
										if(x_velocity <= -0.0015524578629992902):
											return True
										else:
											if(x_velocity > -0.0015518521540798247):
												return True
								else:
									if(angle_velocity <= 0.000487971497932449):
										if(angle > 0.10283709317445755):
											return True
									else:
										if(lander_x <= -0.2934667617082596):
											return True
					else:
						if(angle_velocity <= 0.18233278393745422):
							if(angle <= 0.2907939851284027):
								if(lander_y > -0.02451244741678238):
									if(lander_x <= -0.17154951393604279):
										return True
							else:
								if(lander_x <= -0.23196563869714737):
									return True
						else:
							if(lander_y <= 1.4422094821929932):
								if(angle_velocity <= 0.23621858656406403):
									if(x_velocity <= 0.03866477310657501):
										return True
								else:
									return True
							else:
								if(x_velocity <= 0.40666310489177704):
									return True
								else:
									if(angle > 0.19336441904306412):
										if(angle_velocity > 0.2609146162867546):
											return True
		else:
			if(x_velocity <= 0.18656544387340546):
				if(lander_y <= -0.044073011726140976):
					if(angle_velocity <= -0.0004694566159741953):
						if(angle > 0.30547989904880524):
							return True
					else:
						return True
				else:
					if(x_velocity <= -0.29649674892425537):
						return True
					else:
						if(x_velocity <= -0.13633117079734802):
							if(angle_velocity <= -0.19100315123796463):
								if(angle_velocity <= -0.23226524889469147):
									if(y_velocity > 0.035931989550590515):
										return True
							else:
								return True
						else:
							if(angle <= 0.3047634959220886):
								if(lander_y <= 1.454972743988037):
									if(x_velocity <= 0.17811888456344604):
										if(y_velocity <= -9.444370880373754e-05):
											if(y_velocity <= -9.544390923110768e-05):
												if(angle > 0.10312356427311897):
													if(x_velocity <= -0.0012096493737772107):
														return True
											else:
												return True
								else:
									if(lander_y <= 1.4570536017417908):
										if(x_velocity <= -0.014905132353305817):
											return True
							else:
								if(angle_velocity > -0.00037222792161628604):
									return True
			else:
				if(x_velocity <= 0.44430138170719147):
					if(lander_y > 1.4766086339950562):
						if(angle > 0.14202280342578888):
							return True
	return False

