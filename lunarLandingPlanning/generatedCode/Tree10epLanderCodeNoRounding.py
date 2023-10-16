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
	if(right_leg_contact != True):
		if(y_velocity > -0.2117035612463951):
			if(y_velocity <= -0.04625159688293934):
				if(angle_velocity <= -0.020012114197015762):
					if(x_velocity <= -0.062468184158205986):
						if(lander_y > 1.470240831375122):
							return True
					else:
						if(angle <= 0.004466760903596878):
							if(lander_y <= 1.4811075925827026):
								if(angle_velocity <= -0.03305315971374512):
									if(y_velocity > -0.08007068186998367):
										if(angle <= -0.01638783421367407):
											return True
							else:
								return True
			else:
				if(x_velocity <= 0.174779012799263):
					if(x_velocity > -0.2148854210972786):
						if(lander_x <= 0.021488094702363014):
							if(angle_velocity <= 0.014317034743726254):
								if(angle <= 0.006493317196145654):
									if(y_velocity <= 0.013756581582129002):
										if(y_velocity <= -0.0018054824322462082):
											return True
									else:
										return True
						else:
							if(lander_y <= 1.5249958634376526):
								if(lander_y <= 1.524039626121521):
									if(angle_velocity <= 0.04660855606198311):
										if(angle > -0.019474213011562824):
											if(angle_velocity <= 0.046594636514782906):
												return True
									else:
										return True
							else:
								return True
				else:
					if(angle <= 0.00974681880325079):
						if(y_velocity <= 0.48677924275398254):
							if(angle_velocity > 0.08938105404376984):
								if(angle_velocity <= 0.09051741287112236):
									return True
						else:
							return True
					else:
						if(x_velocity <= 0.37852008640766144):
							if(y_velocity <= 0.015188325196504593):
								if(lander_y <= 1.470399022102356):
									if(y_velocity > -0.01794116967357695):
										return True
							else:
								if(angle_velocity > 0.13082655519247055):
									if(y_velocity <= 0.12223021313548088):
										if(angle_velocity > 0.16748209297657013):
											if(x_velocity <= 0.3723883479833603):
												return True
									else:
										return True
						else:
							if(y_velocity > 0.24036910384893417):
								if(y_velocity <= 0.2668374180793762):
									return True
	else:
		if(angle_velocity > -0.6027695834636688):
			if(angle_velocity <= 0.4368469715118408):
				if(lander_x <= -0.25580425560474396):
					if(lander_x <= -0.2580711096525192):
						return True
				else:
					return True
			else:
				if(y_velocity > -0.12551017105579376):
					if(y_velocity <= -0.111349917948246):
						return True
	return False

def weShould_left_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(right_leg_contact != True):
		if(y_velocity <= -0.2117035612463951):
			if(angle_velocity <= -0.01971765235066414):
				if(x_velocity > -0.6401405930519104):
					if(angle <= 0.012781189288944006):
						if(x_velocity <= -0.06513240933418274):
							if(angle_velocity <= -0.05249720998108387):
								if(lander_y <= 1.3048996925354004):
									if(y_velocity <= -0.30372199416160583):
										if(angle <= -0.02758705895394087):
											if(y_velocity <= -0.4094874709844589):
												if(angle <= -0.1925167441368103):
													if(y_velocity > -0.595160037279129):
														if(angle_velocity <= -0.19597181677818298):
															if(x_velocity > -0.6303410828113556):
																if(lander_y <= 1.2961935997009277):
																	if(lander_y <= 1.1847355365753174):
																		if(lander_y <= 1.1744208335876465):
																			if(x_velocity > -0.6107936501502991):
																				if(angle <= -0.3179901987314224):
																					return True
																				else:
																					if(lander_y <= 1.093873918056488):
																						return True
																					else:
																						if(lander_x > -0.13199067115783691):
																							return True
																	else:
																		if(angle <= -0.2488991916179657):
																			return True
																		else:
																			if(angle_velocity <= -0.4059401899576187):
																				return True
														else:
															if(angle <= -0.2821303606033325):
																if(y_velocity <= -0.5001321136951447):
																	if(angle <= -0.33944448828697205):
																		if(y_velocity <= -0.5490778088569641):
																			if(angle <= -0.4060227870941162):
																				if(x_velocity > -0.5743975639343262):
																					return True
																			else:
																				if(lander_y > 1.1120012402534485):
																					if(lander_x <= -0.1866186559200287):
																						return True
																		else:
																			return True
																else:
																	if(lander_y > 0.5280610918998718):
																		if(angle <= -0.29706355929374695):
																			return True
																		else:
																			if(y_velocity > -0.4716564267873764):
																				return True
															else:
																if(y_velocity > -0.4552428871393204):
																	return True
												else:
													if(angle <= -0.05963918752968311):
														if(lander_y <= 0.7037343382835388):
															if(y_velocity > -0.44581790268421173):
																return True
											else:
												if(angle_velocity <= -0.07099784910678864):
													if(angle_velocity > -0.4391088932752609):
														if(x_velocity <= -0.10546019300818443):
															return True
														else:
															if(y_velocity > -0.31656259298324585):
																return True
												else:
													if(angle_velocity > -0.06470226496458054):
														if(angle_velocity <= -0.06276504695415497):
															return True
														else:
															if(angle <= -0.0328125786036253):
																if(y_velocity <= -0.30547480285167694):
																	if(x_velocity <= -0.17753219604492188):
																		if(y_velocity > -0.33098115026950836):
																			return True
																else:
																	return True
															else:
																return True
										else:
											if(angle <= 0.0052619194611907005):
												if(lander_y <= 0.8310801386833191):
													return True
											else:
												if(x_velocity <= -0.09490720555186272):
													return True
									else:
										if(lander_y <= 0.43368667364120483):
											if(y_velocity <= -0.24037925899028778):
												if(x_velocity <= -0.13334935158491135):
													return True
											else:
												if(lander_x <= 0.09381012618541718):
													return True
												else:
													if(angle_velocity <= -0.08190915361046791):
														return True
													else:
														if(x_velocity > -0.09435850754380226):
															if(x_velocity <= -0.07662615180015564):
																return True
										else:
											if(angle <= 0.003303513047285378):
												if(lander_x <= 0.0578050147742033):
													if(x_velocity <= -0.10827558860182762):
														if(angle <= -0.04051966778934002):
															return True
													else:
														if(lander_x <= 0.05524273030459881):
															if(lander_x <= -0.04958477057516575):
																if(lander_x <= -0.05036306381225586):
																	return True
															else:
																return True
												else:
													return True
											else:
												if(y_velocity > -0.28821198642253876):
													if(lander_y <= 0.9289388954639435):
														return True
								else:
									if(x_velocity <= -0.28267785906791687):
										if(angle <= -0.1505107581615448):
											return True
									else:
										if(x_velocity <= -0.27727390825748444):
											if(lander_x <= -0.044144392013549805):
												return True
										else:
											return True
							else:
								if(y_velocity <= -0.3092031627893448):
									if(lander_x <= 0.034208107739686966):
										if(x_velocity <= -0.07069391012191772):
											if(angle <= -0.058789392933249474):
												if(lander_y <= 0.9564158618450165):
													return True
												else:
													if(y_velocity <= -0.39373779296875):
														if(lander_y <= 0.98670294880867):
															if(angle <= -0.35545089840888977):
																return True
														else:
															if(x_velocity <= -0.2154904454946518):
																if(angle_velocity <= -0.0469475407153368):
																	if(y_velocity > -0.5579902827739716):
																		return True
															else:
																return True
													else:
														if(angle_velocity <= -0.03710435330867767):
															return True
											else:
												if(x_velocity > -0.3226556330919266):
													if(x_velocity > -0.07414290308952332):
														if(x_velocity <= -0.07244673371315002):
															return True
										else:
											return True
									else:
										if(y_velocity <= -0.31185534596443176):
											if(lander_y <= 0.7093349397182465):
												if(angle_velocity > -0.044822121039032936):
													return True
										else:
											if(angle <= -0.033107586205005646):
												if(angle_velocity <= -0.034461623057723045):
													return True
								else:
									if(lander_y <= 0.7466024160385132):
										if(angle <= -0.03484991937875748):
											if(x_velocity <= -0.08155859261751175):
												if(angle_velocity <= -0.022684134542942047):
													if(y_velocity <= -0.2341933324933052):
														if(angle_velocity <= -0.028814148157835007):
															if(angle_velocity <= -0.03044154029339552):
																if(angle <= -0.05913454294204712):
																	if(angle > -0.061223698779940605):
																		return True
																else:
																	if(x_velocity <= -0.09463442116975784):
																		if(angle_velocity > -0.0401531346142292):
																			if(y_velocity <= -0.2861316651105881):
																				return True
															else:
																if(lander_y > 0.591789647936821):
																	return True
													else:
														return True
												else:
													if(angle <= -0.053620295599102974):
														return True
											else:
												if(angle <= -0.03599567338824272):
													if(angle > -0.06680350378155708):
														if(y_velocity <= -0.2807130515575409):
															if(angle <= -0.04795508272945881):
																return True
														else:
															return True
										else:
											if(y_velocity > -0.2367466762661934):
												if(angle <= -0.013058193027973175):
													if(angle_velocity <= -0.044335465878248215):
														return True
									else:
										if(y_velocity <= -0.2770034819841385):
											if(lander_y <= 0.9185478091239929):
												if(angle <= -0.0332136545330286):
													if(angle_velocity <= -0.02201506309211254):
														if(x_velocity > -0.10539235919713974):
															return True
											else:
												if(angle > -0.016147284768521786):
													if(angle <= 0.00015097158029675484):
														return True
										else:
											if(angle <= -0.02650956902652979):
												if(angle > -0.030107329599559307):
													return True
						else:
							if(angle_velocity <= -0.05213030055165291):
								if(lander_y > 0.026998624205589294):
									if(lander_y <= 0.45490846037864685):
										if(y_velocity <= -0.22937697172164917):
											if(angle <= -0.018974131904542446):
												return True
											else:
												if(lander_x <= 0.015254211612045765):
													if(y_velocity > -0.24898098409175873):
														if(lander_y <= 0.3079184591770172):
															if(y_velocity <= -0.23525803536176682):
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
								if(lander_x <= 0.006706619169563055):
									if(angle <= -0.011310861445963383):
										if(y_velocity <= -0.23208345472812653):
											if(lander_y <= 0.3656506836414337):
												if(angle <= -0.03730302304029465):
													if(lander_y <= 0.3085542172193527):
														return True
												else:
													if(lander_x <= -0.15789341926574707):
														if(lander_x > -0.21045448631048203):
															return True
											else:
												if(x_velocity <= -0.04091320000588894):
													if(y_velocity <= -0.24923568964004517):
														if(angle_velocity <= -0.040699757635593414):
															if(y_velocity <= -0.29631151258945465):
																if(lander_y > 1.1595101654529572):
																	return True
															else:
																return True
														else:
															if(lander_y > 0.9674433171749115):
																if(y_velocity > -0.3275309354066849):
																	return True
												else:
													if(angle <= -0.04664045386016369):
														if(angle_velocity > -0.023225690238177776):
															return True
													else:
														return True
										else:
											if(y_velocity <= -0.2172534391283989):
												if(lander_y > 0.01735436636954546):
													if(lander_x <= -0.2258301004767418):
														if(lander_x <= -0.2450345754623413):
															return True
													else:
														return True
									else:
										if(lander_y <= 1.0421459078788757):
											if(y_velocity <= -0.21985971182584763):
												if(angle_velocity <= -0.033265724778175354):
													if(lander_y <= 0.3868452161550522):
														if(angle <= -0.0037476179422810674):
															if(y_velocity > -0.23523617535829544):
																if(angle_velocity <= -0.038739876821637154):
																	return True
														else:
															if(lander_x > -0.0060964582953602076):
																return True
													else:
														if(y_velocity <= -0.281961053609848):
															if(x_velocity <= -0.03690149076282978):
																return True
														else:
															if(lander_x > -0.12462563440203667):
																return True
											else:
												if(x_velocity <= 0.03791380859911442):
													if(lander_y > 0.2066478729248047):
														return True
												else:
													if(lander_x > -0.2716696262359619):
														return True
										else:
											if(x_velocity > -0.03997028432786465):
												return True
								else:
									if(y_velocity <= -0.2660217881202698):
										if(lander_y <= 0.7570912539958954):
											if(x_velocity <= -0.06046063452959061):
												return True
											else:
												if(lander_x > 0.12493033334612846):
													if(lander_x <= 0.13070178031921387):
														return True
										else:
											if(y_velocity > -0.2922917902469635):
												return True
									else:
										if(angle <= 0.002455090289004147):
											if(lander_y > 0.004407272324897349):
												if(angle_velocity <= -0.045211587101221085):
													if(lander_y <= 0.22236651182174683):
														if(y_velocity > -0.2337423786520958):
															return True
													else:
														return True
												else:
													if(lander_x <= 0.06801901012659073):
														return True
													else:
														if(lander_x <= 0.07907114177942276):
															if(angle_velocity > -0.03367750532925129):
																if(angle > -0.010514833498746157):
																	if(lander_y <= 0.39454948902130127):
																		return True
														else:
															return True
										else:
											if(angle_velocity <= -0.03174342028796673):
												if(y_velocity <= -0.23556186258792877):
													return True
											else:
												if(y_velocity <= -0.2321210727095604):
													if(lander_x > 0.11557965353131294):
														return True
												else:
													if(lander_y <= 0.4520876258611679):
														if(y_velocity > -0.22256776690483093):
															return True
					else:
						if(y_velocity <= -0.2789912819862366):
							if(angle_velocity <= -0.09004996344447136):
								if(angle <= 0.08533484488725662):
									if(y_velocity > -0.3096257150173187):
										if(lander_x <= 0.18775305151939392):
											if(angle > 0.015496364794671535):
												if(x_velocity <= 0.011610974557697773):
													return True
												else:
													if(x_velocity > 0.02092286106199026):
														return True
							else:
								if(angle <= 0.021439004689455032):
									if(x_velocity > -0.05827265419065952):
										if(angle_velocity <= -0.026983673684298992):
											return True
								else:
									if(angle <= 0.3775688335299492):
										if(y_velocity > -0.284874826669693):
											if(y_velocity <= -0.28447917103767395):
												return True
						else:
							if(lander_y <= 0.3803439140319824):
								if(angle_velocity <= -0.0659567192196846):
									if(lander_y <= 0.30862589180469513):
										if(x_velocity > -0.02822474204003811):
											return True
								else:
									if(angle_velocity <= -0.05572383664548397):
										if(angle_velocity > -0.05819185450673103):
											return True
							else:
								if(x_velocity > -0.0604530181735754):
									if(angle <= 0.16142796725034714):
										if(angle_velocity <= -0.08607826009392738):
											if(y_velocity <= -0.2488519698381424):
												if(lander_y <= 1.2703145742416382):
													if(lander_y <= 1.1099320650100708):
														if(angle <= 0.11882057413458824):
															if(x_velocity <= -0.02919619996100664):
																if(lander_x <= 0.1030145138502121):
																	return True
															else:
																return True
													else:
														return True
												else:
													if(angle > 0.14005474001169205):
														return True
											else:
												if(x_velocity <= 0.06888234242796898):
													if(angle <= 0.12855295836925507):
														if(y_velocity > -0.24604059755802155):
															if(angle_velocity <= -0.1274324506521225):
																return True
															else:
																if(lander_x <= -0.057015541940927505):
																	return True
												else:
													return True
										else:
											if(y_velocity <= -0.2474518120288849):
												if(x_velocity <= 0.005094257416203618):
													if(lander_y <= 0.9323590397834778):
														if(lander_y > 0.7673076391220093):
															if(angle_velocity <= -0.05070433206856251):
																return True
															else:
																if(lander_x <= 0.0711735226213932):
																	return True
													else:
														if(y_velocity <= -0.26060667634010315):
															if(angle <= 0.060243748128414154):
																if(angle_velocity <= -0.037429384887218475):
																	if(y_velocity <= -0.27316708862781525):
																		if(y_velocity <= -0.27879194915294647):
																			return True
																		else:
																			if(angle > 0.05794862471520901):
																				return True
																	else:
																		return True
												else:
													if(y_velocity <= -0.2529370039701462):
														if(angle_velocity <= -0.08128143846988678):
															if(y_velocity > -0.2695906460285187):
																return True
														else:
															if(lander_y <= 1.288892149925232):
																if(lander_y <= 1.116899013519287):
																	if(lander_x <= 0.06785836070775986):
																		if(x_velocity > 0.0815524123609066):
																			return True
																	else:
																		if(angle_velocity <= -0.04478166997432709):
																			return True
																		else:
																			if(y_velocity <= -0.26847679913043976):
																				return True
																else:
																	if(lander_x <= 0.04910011403262615):
																		return True
																	else:
																		if(angle_velocity <= -0.06591363810002804):
																			if(x_velocity <= 0.06677966564893723):
																				return True
													else:
														if(angle_velocity <= -0.0572066493332386):
															return True
														else:
															if(x_velocity > 0.08906363695859909):
																return True
											else:
												if(lander_y <= 1.1120572686195374):
													if(x_velocity <= 0.022168805822730064):
														if(y_velocity <= -0.2292398437857628):
															if(lander_y <= 1.0322741270065308):
																if(y_velocity <= -0.245970718562603):
																	if(lander_x > 0.07522673532366753):
																		return True
																else:
																	return True
															else:
																if(x_velocity > -0.014843103243038058):
																	return True
													else:
														if(y_velocity <= -0.24030151218175888):
															if(x_velocity > 0.08545957133173943):
																return True
														else:
															if(x_velocity <= 0.03946295753121376):
																if(lander_x > -0.07193389162421227):
																	return True
															else:
																if(y_velocity <= -0.22815317660570145):
																	if(lander_x <= -0.07420191541314125):
																		if(lander_x <= -0.2219446375966072):
																			return True
																		else:
																			if(y_velocity > -0.23037920147180557):
																				if(lander_x > -0.08087301254272461):
																					return True
																	else:
																		return True
																else:
																	if(angle_velocity <= -0.038002848625183105):
																		if(x_velocity <= 0.08357850089669228):
																			return True
																	else:
																		return True
												else:
													if(x_velocity > 0.0538919772952795):
														if(angle <= 0.12973199039697647):
															if(angle_velocity <= -0.03532067779451609):
																return True
														else:
															if(y_velocity <= -0.23639965057373047):
																if(y_velocity <= -0.24073318392038345):
																	if(lander_y > 1.2715017199516296):
																		return True
									else:
										if(angle_velocity <= -0.1415172442793846):
											return True
										else:
											if(y_velocity <= -0.22405388206243515):
												if(lander_x <= 0.07194094732403755):
													if(x_velocity > 0.14968694746494293):
														return True
												else:
													if(angle_velocity <= -0.08016607165336609):
														if(angle <= 0.1941826343536377):
															if(y_velocity > -0.2504490092396736):
																if(x_velocity > 0.10351002216339111):
																	return True
											else:
												if(angle <= 0.22229371219873428):
													if(x_velocity > 0.19005534052848816):
														return True
												else:
													if(lander_y > 1.3832947611808777):
														return True
			else:
				if(lander_y <= 0.44464150071144104):
					if(x_velocity <= -0.030995020642876625):
						if(y_velocity <= -0.2285304218530655):
							if(y_velocity <= -0.2425948679447174):
								if(angle_velocity <= 0.18433533608913422):
									if(angle <= -0.1823166161775589):
										if(y_velocity <= -0.35034099221229553):
											if(angle_velocity <= 0.020756579469889402):
												return True
											else:
												if(y_velocity > -0.37872400879859924):
													if(x_velocity <= -0.2565072849392891):
														return True
										else:
											if(angle_velocity <= 0.16256096959114075):
												return True
									else:
										if(angle_velocity <= -0.01853099837899208):
											if(x_velocity <= -0.04702067747712135):
												return True
										else:
											if(y_velocity <= -0.2446996495127678):
												if(y_velocity > -0.25114379823207855):
													if(angle <= -0.049739085137844086):
														return True
							else:
								if(lander_y > 0.21119682490825653):
									if(x_velocity <= -0.04663626477122307):
										if(y_velocity <= -0.23095610737800598):
											if(lander_x > 0.052344704046845436):
												return True
						else:
							if(lander_y > 0.06979820504784584):
								if(y_velocity <= -0.22340109944343567):
									if(y_velocity <= -0.2253951132297516):
										if(lander_x <= -0.08593611791729927):
											return True
										else:
											if(y_velocity > -0.22636540234088898):
												return True
					else:
						if(angle <= -0.018957579508423805):
							if(angle_velocity <= -0.010836374945938587):
								if(angle <= -0.02005318272858858):
									return True
								else:
									if(lander_y > 0.20038695260882378):
										return True
							else:
								if(angle_velocity <= 0.015236042439937592):
									if(x_velocity <= 0.02032781345769763):
										if(lander_x <= 0.022630739491432905):
											if(angle_velocity <= 0.013318499084562063):
												if(x_velocity > 0.010799406562000513):
													if(x_velocity <= 0.012684646993875504):
														return True
											else:
												return True
										else:
											if(y_velocity > -0.24603844434022903):
												return True
									else:
										return True
								else:
									if(y_velocity <= -0.21480269730091095):
										if(lander_x > -0.1693543866276741):
											if(y_velocity <= -0.21757720410823822):
												if(x_velocity > 0.03027899842709303):
													if(lander_x <= -0.027924250811338425):
														return True
											else:
												if(y_velocity <= -0.21713373064994812):
													return True
						else:
							if(x_velocity <= 0.15747050940990448):
								if(y_velocity > -0.2333202287554741):
									if(angle <= 0.017681497149169445):
										if(lander_y <= 0.3060990273952484):
											if(lander_y <= 1.520871592219919e-05):
												if(y_velocity <= -0.21956631541252136):
													return True
											else:
												if(y_velocity > -0.21841178089380264):
													if(lander_y <= 0.21786969155073166):
														if(angle > 0.01190967345610261):
															if(x_velocity > 0.04904969595372677):
																return True
													else:
														if(lander_y > 0.245440311729908):
															if(lander_y <= 0.26980745792388916):
																return True
															else:
																if(x_velocity > 0.07172374054789543):
																	return True
										else:
											if(y_velocity <= -0.22006822377443314):
												if(angle_velocity <= -0.0023580207052873448):
													if(lander_y <= 0.38160085678100586):
														if(lander_y <= 0.3212590664625168):
															return True
													else:
														return True
												else:
													if(angle <= -0.004273940809071064):
														if(angle <= -0.014122632332146168):
															if(x_velocity <= 0.017201653216034174):
																return True
											else:
												if(x_velocity <= -0.011793314944952726):
													return True
							else:
								return True
				else:
					if(y_velocity <= -0.2594956308603287):
						if(x_velocity <= 0.6525615453720093):
							if(lander_x <= 0.02307958621531725):
								if(lander_y <= 1.373055338859558):
									if(y_velocity <= -0.29296332597732544):
										if(x_velocity <= -0.10625281929969788):
											if(y_velocity <= -0.3361341655254364):
												if(angle_velocity <= -0.016051679383963346):
													return True
												else:
													if(lander_y <= 1.3320707082748413):
														if(angle_velocity <= 0.19024396687746048):
															if(lander_x <= -0.27865569293498993):
																if(y_velocity > -0.5708374083042145):
																	if(lander_y <= 0.9304526746273041):
																		if(y_velocity <= -0.4900723993778229):
																			if(angle_velocity <= 0.07761191949248314):
																				if(lander_y <= 0.9092622697353363):
																					return True
																			else:
																				if(lander_y > 0.8301143646240234):
																					if(y_velocity > -0.5267745554447174):
																						if(x_velocity <= -0.21264638006687164):
																							return True
																		else:
																			if(angle <= -0.3217872977256775):
																				return True
																			else:
																				if(angle > -0.2993170768022537):
																					return True
																	else:
																		return True
															else:
																if(angle_velocity <= 0.030084882862865925):
																	if(y_velocity <= -0.3749479651451111):
																		if(lander_x <= -0.2462327927350998):
																			if(x_velocity > -0.46916714310646057):
																				return True
																		else:
																			if(lander_y <= 0.919672816991806):
																				return True
																			else:
																				if(x_velocity <= -0.19646716117858887):
																					if(lander_x <= -0.21625898033380508):
																						if(angle > -0.36997316777706146):
																							return True
																				else:
																					if(angle_velocity <= 0.006126062478870153):
																						return True
																	else:
																		if(angle <= -0.11535299941897392):
																			return True
																else:
																	if(y_velocity <= -0.3564331829547882):
																		if(lander_y <= 0.7881717085838318):
																			return True
																		else:
																			if(angle <= -0.2667078524827957):
																				if(angle <= -0.2748633772134781):
																					if(y_velocity <= -0.45100337266921997):
																						if(angle_velocity <= 0.04467276483774185):
																							if(lander_y <= 0.9391319453716278):
																								return True
																						else:
																							if(lander_y > 1.0466598868370056):
																								if(lander_y <= 1.0578892230987549):
																									return True
																					else:
																						if(angle <= -0.29316338896751404):
																							return True
																				else:
																					return True
											else:
												if(x_velocity <= -0.11953193694353104):
													if(lander_x > -0.1192496307194233):
														return True
												else:
													if(y_velocity > -0.32181912660598755):
														return True
										else:
											if(x_velocity <= 0.24357302486896515):
												if(angle <= -0.2787962257862091):
													if(lander_x <= -0.3146837204694748):
														return True
												else:
													if(y_velocity <= -0.31527596712112427):
														if(lander_y <= 1.3443206548690796):
															if(angle <= -0.2267390713095665):
																if(y_velocity > -0.3536236584186554):
																	if(angle_velocity <= 0.2365514561533928):
																		return True
															else:
																if(x_velocity <= -0.0838325135409832):
																	if(x_velocity > -0.08487306162714958):
																		return True
														else:
															if(lander_y <= 1.3504712581634521):
																return True
													else:
														if(lander_y <= 1.1467329859733582):
															if(angle <= -0.19269920140504837):
																if(angle > -0.210196815431118):
																	return True
															else:
																if(y_velocity > -0.3152293413877487):
																	if(angle_velocity <= -0.017945660278201103):
																		return True
																	else:
																		if(lander_x <= 0.0148178581148386):
																			if(angle <= -0.06394661590456963):
																				if(angle_velocity <= 0.08804255723953247):
																					if(lander_y <= 1.0991204977035522):
																						if(y_velocity > -0.3100430518388748):
																							return True
																			else:
																				if(x_velocity > -0.07739036530256271):
																					if(angle <= -0.05298611894249916):
																						if(angle > -0.0566953644156456):
																							return True
																		else:
																			return True
														else:
															if(x_velocity > -0.03966103307902813):
																if(angle <= -0.013819488696753979):
																	return True
																else:
																	if(lander_x <= -0.027727698907256126):
																		return True
											else:
												return True
									else:
										if(lander_y <= 0.6716166436672211):
											if(angle <= -0.13102174922823906):
												if(lander_x <= -0.3646543025970459):
													return True
											else:
												if(x_velocity <= -0.07650924474000931):
													if(angle_velocity <= 0.02510820794850588):
														if(y_velocity > -0.27965205907821655):
															return True
												else:
													if(angle_velocity <= 0.005553795723244548):
														if(angle_velocity <= 0.004267820157110691):
															if(angle <= -0.04568473622202873):
																if(x_velocity > -0.06198539957404137):
																	if(angle <= -0.047806499525904655):
																		return True
																	else:
																		if(lander_x <= -0.16671299934387207):
																			return True
															else:
																if(lander_x > -0.0005010127788409591):
																	if(lander_y <= 0.6457030475139618):
																		return True
														else:
															return True
													else:
														if(angle > -0.10513648390769958):
															if(angle <= -0.06310204230248928):
																if(angle_velocity <= 0.10332319140434265):
																	return True
										else:
											if(x_velocity <= -0.023015913553535938):
												if(y_velocity <= -0.2758352607488632):
													if(lander_y <= 0.9605807363986969):
														if(angle > -0.05462417006492615):
															if(angle <= -0.043146610260009766):
																if(lander_y <= 0.8127729296684265):
																	return True
													else:
														if(lander_x <= -0.03730282746255398):
															if(angle <= -0.023724621161818504):
																return True
												else:
													if(lander_y <= 0.6850554943084717):
														return True
													else:
														if(lander_y <= 1.0657299160957336):
															if(angle_velocity <= -0.006892556499224156):
																if(lander_x <= -0.044910430908203125):
																	return True
														else:
															return True
											else:
												if(angle <= -0.05630537122488022):
													if(x_velocity <= 0.03674690052866936):
														if(y_velocity > -0.26706530153751373):
															return True
												else:
													if(angle_velocity <= 0.029466263949871063):
														if(angle <= 0.008146327221766114):
															if(y_velocity <= -0.284311980009079):
																if(x_velocity <= 0.003164541267324239):
																	if(angle <= -0.038382926024496555):
																		return True
																else:
																	return True
															else:
																if(lander_x <= -0.009977101814001799):
																	return True
																else:
																	if(y_velocity <= -0.2799728512763977):
																		return True
													else:
														if(lander_y <= 1.0080597698688507):
															if(lander_y > 0.9281871616840363):
																if(x_velocity > 0.06501607969403267):
																	return True
														else:
															if(angle_velocity <= 0.07091180607676506):
																if(x_velocity > 0.0017973128706216812):
																	return True
								else:
									if(x_velocity > -0.05172503925859928):
										if(y_velocity > -0.333544060587883):
											return True
							else:
								if(lander_x <= 0.22602467983961105):
									if(x_velocity <= -0.07535390555858612):
										if(y_velocity <= -0.28644469380378723):
											if(lander_y <= 1.0477442741394043):
												if(angle <= -0.11666755005717278):
													if(y_velocity > -0.31631308794021606):
														return True
										else:
											if(lander_x <= 0.09229903295636177):
												if(angle_velocity <= -0.008074681041762233):
													if(x_velocity > -0.09963561594486237):
														return True
												else:
													if(y_velocity <= -0.27435214817523956):
														if(lander_y <= 0.7805542349815369):
															if(lander_y <= 0.596069872379303):
																return True
									else:
										if(y_velocity > -0.2709008604288101):
											if(lander_x <= 0.14790429919958115):
												if(angle <= -0.03736453130841255):
													if(angle <= -0.03991925157606602):
														return True
												else:
													if(angle_velocity > -0.01852460578083992):
														if(lander_y <= 1.433857500553131):
															if(y_velocity <= -0.26241831481456757):
																if(angle_velocity <= -0.01747903134673834):
																	if(lander_y <= 0.7911043167114258):
																		return True
															else:
																if(lander_x <= 0.08574771881103516):
																	if(lander_x <= 0.02779297810047865):
																		return True
																else:
																	if(angle <= -0.0007919874042272568):
																		return True
						else:
							return True
					else:
						if(x_velocity <= 0.009772160556167364):
							if(y_velocity <= -0.24483375251293182):
								if(lander_y <= 0.6944023370742798):
									if(x_velocity <= -0.04959486611187458):
										if(angle_velocity <= -0.004452854162082076):
											if(lander_y > 0.5145226567983627):
												return True
									else:
										if(angle_velocity <= 0.016676543280482292):
											if(angle <= -0.008457919582724571):
												return True
											else:
												if(lander_x <= 0.08355550840497017):
													if(lander_y > 0.6842318773269653):
														return True
												else:
													if(angle_velocity <= -0.0051709983963519335):
														return True
								else:
									if(angle_velocity <= -0.011723455041646957):
										if(x_velocity > -0.053443145006895065):
											if(x_velocity <= -0.018804423045367002):
												return True
									else:
										if(x_velocity <= 0.006656566169112921):
											if(y_velocity <= -0.24526099860668182):
												if(lander_y <= 0.764032632112503):
													if(angle_velocity <= -0.003753315657377243):
														if(angle <= -0.0035565290600061417):
															return True
										else:
											if(lander_y <= 0.7904876172542572):
												return True
							else:
								if(angle_velocity <= -0.017813351936638355):
									return True
								else:
									if(angle <= -0.031075498089194298):
										if(lander_x <= 0.04992971383035183):
											if(x_velocity <= -0.01454231794923544):
												if(angle > -0.04000113159418106):
													if(angle_velocity <= 0.022110107820481062):
														return True
											else:
												if(y_velocity > -0.23755423724651337):
													return True
										else:
											return True
									else:
										if(angle_velocity <= -0.005560303805395961):
											if(angle <= -0.007473527453839779):
												if(y_velocity <= -0.22866062074899673):
													return True
										else:
											if(x_velocity > -0.018309815786778927):
												if(lander_x <= 0.08038429915904999):
													if(x_velocity <= -0.01509121898561716):
														if(angle <= -4.667416214942932e-05):
															return True
						else:
							if(y_velocity <= -0.2244303897023201):
								if(lander_y <= 0.6337423324584961):
									if(angle > -0.05921509116888046):
										if(y_velocity > -0.2429022565484047):
											if(x_velocity <= 0.01496987696737051):
												return True
											else:
												if(angle <= 0.02831197716295719):
													if(angle_velocity <= 0.04527553729712963):
														if(angle <= 0.013827523216605186):
															if(x_velocity <= 0.08098047971725464):
																if(lander_y <= 0.46728184819221497):
																	if(angle_velocity > 0.010481433477252722):
																		return True
															else:
																return True
														else:
															if(x_velocity <= 0.13157899677753448):
																if(angle_velocity > 0.03676746226847172):
																	return True
															else:
																return True
													else:
														if(x_velocity > 0.1530468538403511):
															return True
								else:
									if(angle <= 0.13975286483764648):
										if(y_velocity <= -0.249237060546875):
											if(lander_y <= 1.2836709022521973):
												if(angle_velocity <= 0.105367511510849):
													if(angle_velocity > -0.019210652448236942):
														if(x_velocity <= 0.014196524396538734):
															if(angle > 0.03387469984591007):
																return True
														else:
															if(x_velocity > 0.10053893178701401):
																if(lander_x <= -0.10623187944293022):
																	return True
												else:
													return True
										else:
											if(lander_y <= 0.926637202501297):
												if(angle <= 0.012374273966997862):
													if(x_velocity > 0.07312560081481934):
														if(lander_y > 0.6474784016609192):
															return True
												else:
													if(y_velocity <= -0.23654136061668396):
														if(x_velocity > 0.1023041196167469):
															return True
											else:
												if(lander_y <= 1.3702694177627563):
													if(y_velocity <= -0.24629773199558258):
														if(angle <= 0.11105184629559517):
															return True
													else:
														if(angle_velocity <= -0.012375698890537024):
															if(x_velocity <= 0.07926076650619507):
																if(y_velocity > -0.2296822965145111):
																	return True
												else:
													if(angle_velocity <= 0.12907720357179642):
														if(angle_velocity > 0.01062967290636152):
															return True
							else:
								if(angle_velocity <= 0.05199507810175419):
									if(angle_velocity <= 0.034516019746661186):
										if(angle <= 0.0669519193470478):
											if(x_velocity > 0.06815199181437492):
												if(lander_y <= 0.7828270196914673):
													return True
									else:
										if(lander_x > -0.01775689097121358):
											return True
								else:
									if(x_velocity <= 0.25101426988840103):
										if(lander_y <= 0.5400468111038208):
											if(x_velocity > 0.11229487136006355):
												if(angle <= -0.05024145543575287):
													return True
										else:
											if(angle_velocity <= 0.24486032128334045):
												if(angle <= -0.043392933905124664):
													if(lander_x > -0.2998668700456619):
														return True
											else:
												return True
									else:
										return True
		else:
			if(y_velocity <= -0.04625159688293934):
				if(angle_velocity <= -0.020012114197015762):
					if(x_velocity <= -0.062468184158205986):
						if(lander_y <= 1.470240831375122):
							if(x_velocity > -0.217918299138546):
								if(lander_x <= -0.012781954137608409):
									return True
								else:
									if(angle <= -0.017480780370533466):
										if(angle_velocity <= -0.040706194937229156):
											if(angle_velocity > -0.07470352947711945):
												return True
					else:
						if(angle <= 0.004466760903596878):
							if(lander_y <= 1.4811075925827026):
								if(angle_velocity <= -0.03305315971374512):
									if(y_velocity <= -0.08007068186998367):
										if(y_velocity <= -0.21059369295835495):
											if(angle_velocity <= -0.051847146824002266):
												return True
										else:
											return True
									else:
										if(angle > -0.01638783421367407):
											return True
								else:
									if(x_velocity > -0.025241411291062832):
										if(lander_y > 0.07490148209035397):
											if(angle_velocity > -0.03234349191188812):
												return True
						else:
							if(y_velocity <= -0.19456586986780167):
								if(lander_y <= 0.3112007826566696):
									if(angle_velocity <= -0.03830353356897831):
										if(angle > 0.010316614527255297):
											if(angle_velocity <= -0.059264520183205605):
												return True
											else:
												if(lander_y <= 0.2251387983560562):
													if(x_velocity > 0.023855773732066154):
														if(lander_x > -0.2420194074511528):
															return True
												else:
													if(lander_y <= 0.2838802933692932):
														return True
									else:
										if(x_velocity > -0.04011731967329979):
											if(x_velocity <= 0.10860027000308037):
												if(angle <= 0.02127546537667513):
													if(angle > 0.014985323883593082):
														if(lander_x <= -0.048516225069761276):
															return True
											else:
												return True
								else:
									if(lander_y <= 0.3769782781600952):
										if(lander_x <= -0.007061862852424383):
											if(angle <= 0.06673962250351906):
												return True
											else:
												if(y_velocity > -0.20471953600645065):
													return True
									else:
										if(x_velocity <= 0.19233880192041397):
											if(angle_velocity <= -0.1404288038611412):
												return True
											else:
												if(lander_x <= -0.23554258048534393):
													if(angle > 0.014951597433537245):
														return True
										else:
											if(x_velocity <= 0.27829059958457947):
												if(lander_y <= 1.313782513141632):
													return True
											else:
												return True
							else:
								if(lander_x <= 0.09790630266070366):
									if(angle_velocity <= -0.04235716536641121):
										if(lander_y <= 0.27968253195285797):
											if(angle <= 0.04661379009485245):
												return True
											else:
												if(angle > 0.05018204264342785):
													return True
										else:
											if(x_velocity <= 0.06659107282757759):
												if(angle_velocity <= -0.061794960871338844):
													if(y_velocity <= -0.1837133765220642):
														return True
											else:
												return True
									else:
										if(y_velocity <= -0.16684778034687042):
											if(x_velocity > 0.0077046051155775785):
												if(angle <= 0.06907186284661293):
													if(lander_x <= -0.07053551450371742):
														if(x_velocity > 0.057628123089671135):
															if(angle <= 0.03962137922644615):
																return True
													else:
														if(angle_velocity > -0.03958926163613796):
															if(x_velocity <= 0.020452387165278196):
																if(lander_y > 0.05385594069957733):
																	if(angle <= 0.025027060182765126):
																		return True
															else:
																return True
								else:
									if(x_velocity <= 0.2305583357810974):
										if(y_velocity <= -0.1862800344824791):
											if(y_velocity > -0.18919487297534943):
												return True
									else:
										if(x_velocity <= 0.23397155106067657):
											return True
				else:
					if(y_velocity <= -0.18436022847890854):
						if(x_velocity <= -0.0069253817200660706):
							if(lander_y <= 0.0211697556078434):
								if(lander_y > 0.01586259389296174):
									if(lander_x > -0.03813023492693901):
										return True
							else:
								if(lander_x <= 0.11992516368627548):
									if(angle <= -0.03051120787858963):
										if(x_velocity <= -0.0323156900703907):
											if(lander_x <= -0.025156640447676182):
												if(lander_x > -0.02635092753916979):
													return True
										else:
											if(angle_velocity <= 0.017021882347762585):
												return True
									else:
										if(y_velocity > -0.21088775247335434):
											if(x_velocity > -0.011651167646050453):
												if(x_velocity <= -0.01106531172990799):
													return True
						else:
							if(lander_x <= -0.042762136086821556):
								if(y_velocity <= -0.20255107432603836):
									if(lander_y <= 0.4827624410390854):
										if(x_velocity <= 0.051810845732688904):
											if(lander_y <= 0.15091170370578766):
												if(angle_velocity <= -0.013167968951165676):
													return True
												else:
													if(angle > -0.023265200667083263):
														if(y_velocity <= -0.20862088352441788):
															if(angle_velocity <= 0.001374891260638833):
																return True
											else:
												if(y_velocity > -0.20258718729019165):
													return True
										else:
											if(angle <= -0.009217553306370974):
												return True
											else:
												if(angle_velocity <= -0.012879056856036186):
													return True
												else:
													if(lander_x > -0.11576604470610619):
														if(x_velocity > 0.059141192585229874):
															if(angle <= 0.02305728243663907):
																return True
															else:
																if(x_velocity > 0.1062653698027134):
																	if(angle_velocity <= 0.052790841087698936):
																		return True
									else:
										if(angle_velocity <= 0.017661770689301193):
											if(x_velocity > 0.0928075909614563):
												return True
								else:
									if(lander_y <= 0.3891821354627609):
										if(x_velocity <= 0.07820967957377434):
											if(lander_y > 0.0024011230270843953):
												if(angle_velocity <= -0.0004889809933956712):
													if(x_velocity <= 0.05140134133398533):
														if(lander_y <= 0.08781356364488602):
															if(angle_velocity > -0.01603021938353777):
																return True
														else:
															if(x_velocity > 0.03584926202893257):
																if(angle <= 0.0028147652046754956):
																	if(lander_x <= -0.20212462544441223):
																		if(y_velocity <= -0.19196707010269165):
																			return True
																	else:
																		return True
													else:
														if(y_velocity > -0.20081204921007156):
															if(angle_velocity <= -0.0030889732879586518):
																return True
												else:
													if(y_velocity > -0.18582746386528015):
														if(lander_x > -0.1992006078362465):
															return True
										else:
											if(lander_x > -0.2274240478873253):
												if(x_velocity <= 0.11670643836259842):
													if(y_velocity > -0.18645817041397095):
														if(lander_x <= -0.17339437454938889):
															return True
												else:
													return True
									else:
										if(x_velocity > 0.13976705819368362):
											if(angle_velocity <= 0.0705386446788907):
												return True
							else:
								if(angle <= 0.03075925912708044):
									if(lander_y <= 0.23827283084392548):
										if(angle_velocity <= 0.005395429907366633):
											if(lander_y <= 0.051877399906516075):
												if(y_velocity <= -0.19031043350696564):
													if(x_velocity <= 0.0019591117452364415):
														return True
													else:
														if(angle_velocity > 0.0029652915545739233):
															return True
											else:
												return True
										else:
											if(angle_velocity <= 0.11614060401916504):
												if(y_velocity > -0.18809842318296432):
													if(lander_x > -0.019969177432358265):
														return True
											else:
												if(x_velocity > 0.06585400551557541):
													return True
									else:
										if(x_velocity <= 0.038285283371806145):
											if(angle_velocity <= 0.035340841859579086):
												if(x_velocity > 0.004353738273493946):
													return True
										else:
											return True
								else:
									if(lander_y <= 0.2757747322320938):
										if(y_velocity <= -0.18958498537540436):
											if(x_velocity <= 0.08819332346320152):
												if(y_velocity <= -0.19091307371854782):
													if(angle_velocity <= -0.01807697955518961):
														if(angle_velocity > -0.0195396663621068):
															return True
												else:
													if(y_velocity <= -0.1902071237564087):
														return True
											else:
												return True
									else:
										if(x_velocity <= 0.2683706134557724):
											if(lander_x <= 0.03540916554629803):
												if(lander_y > 0.9386655986309052):
													return True
											else:
												if(lander_y <= 0.4122486710548401):
													if(y_velocity <= -0.19863538444042206):
														if(angle <= 0.05365173518657684):
															if(x_velocity > 0.04408101551234722):
																return True
													else:
														if(angle_velocity <= 0.005234683980233967):
															return True
												else:
													if(lander_x <= 0.13416848331689835):
														if(lander_y > 1.480635404586792):
															return True
					else:
						if(x_velocity <= 0.3691508024930954):
							if(lander_y > -0.001645400479901582):
								if(x_velocity <= 0.04088269919157028):
									if(y_velocity <= -0.18427950888872147):
										if(lander_x > -0.04821448400616646):
											return True
									else:
										if(lander_y <= 0.020615647546947002):
											if(x_velocity > 0.02952624950557947):
												return True
								else:
									if(lander_y <= 0.11264903098344803):
										if(angle_velocity <= 0.004053640004713088):
											if(lander_x > -0.2499690279364586):
												return True
										else:
											if(y_velocity <= -0.16221347451210022):
												if(angle <= 0.03342198394238949):
													if(angle_velocity <= 0.04894179664552212):
														if(x_velocity <= 0.0869213379919529):
															return True
									else:
										if(y_velocity <= -0.1415981501340866):
											if(angle_velocity <= 0.010637735482305288):
												if(lander_x > -0.10494113247841597):
													if(angle <= 0.0517528411000967):
														return True
													else:
														if(angle_velocity > 0.009012272581458092):
															return True
											else:
												if(y_velocity > -0.18348319083452225):
													if(lander_y > 0.41426412761211395):
														if(lander_y <= 0.4249081611633301):
															return True
														else:
															if(angle <= 0.02259056642651558):
																if(lander_y > 0.9383572489023209):
																	return True
															else:
																if(y_velocity > -0.1785217523574829):
																	if(lander_y > 1.4533974528312683):
																		if(lander_y <= 1.4590007066726685):
																			return True
										else:
											if(angle_velocity <= 0.14730069041252136):
												return True
											else:
												if(angle_velocity <= 0.1730458214879036):
													if(lander_x > 0.04646463505923748):
														return True
						else:
							if(y_velocity > -0.1733998954296112):
								if(lander_x <= 0.06330790743231773):
									return True
								else:
									if(x_velocity > 0.37721721827983856):
										if(y_velocity > -0.15873125195503235):
											return True
			else:
				if(x_velocity <= 0.174779012799263):
					if(x_velocity > -0.2148854210972786):
						if(lander_x > 0.021488094702363014):
							if(lander_y <= 1.5249958634376526):
								if(lander_y <= 1.524039626121521):
									if(angle_velocity <= 0.04660855606198311):
										if(angle <= -0.019474213011562824):
											return True
										else:
											if(angle_velocity > 0.046594636514782906):
												return True
								else:
									return True
				else:
					if(angle <= 0.00974681880325079):
						if(y_velocity <= 0.48677924275398254):
							if(angle_velocity <= 0.08938105404376984):
								return True
							else:
								if(angle_velocity > 0.09051741287112236):
									return True
					else:
						if(x_velocity <= 0.37852008640766144):
							if(y_velocity <= 0.015188325196504593):
								if(lander_y <= 1.470399022102356):
									if(y_velocity <= -0.01794116967357695):
										return True
							else:
								if(angle_velocity <= 0.13082655519247055):
									return True
								else:
									if(y_velocity <= 0.12223021313548088):
										if(angle_velocity <= 0.16748209297657013):
											return True
										else:
											if(x_velocity > 0.3723883479833603):
												return True
						else:
							if(y_velocity <= 0.24036910384893417):
								return True
							else:
								if(y_velocity > 0.2668374180793762):
									return True
	else:
		if(angle_velocity <= -0.6027695834636688):
			return True
		else:
			if(angle_velocity <= 0.4368469715118408):
				if(lander_x <= -0.25580425560474396):
					if(lander_x > -0.2580711096525192):
						return True
	return False

def weShould_main_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(right_leg_contact != True):
		if(y_velocity <= -0.2117035612463951):
			if(angle_velocity <= -0.01971765235066414):
				if(x_velocity <= -0.6401405930519104):
					if(y_velocity <= -0.522825300693512):
						return True
				else:
					if(angle <= 0.012781189288944006):
						if(x_velocity <= -0.06513240933418274):
							if(angle_velocity <= -0.05249720998108387):
								if(lander_y <= 1.3048996925354004):
									if(y_velocity <= -0.30372199416160583):
										if(angle <= -0.02758705895394087):
											if(y_velocity <= -0.4094874709844589):
												if(angle <= -0.1925167441368103):
													if(y_velocity <= -0.595160037279129):
														return True
													else:
														if(angle_velocity <= -0.19597181677818298):
															if(x_velocity <= -0.6303410828113556):
																return True
															else:
																if(lander_y <= 1.2961935997009277):
																	if(lander_y <= 1.1847355365753174):
																		if(lander_y <= 1.1744208335876465):
																			if(x_velocity <= -0.6107936501502991):
																				return True
																			else:
																				if(angle > -0.3179901987314224):
																					if(lander_y > 1.093873918056488):
																						if(lander_x <= -0.13199067115783691):
																							return True
																		else:
																			return True
																	else:
																		if(angle > -0.2488991916179657):
																			if(angle_velocity > -0.4059401899576187):
																				return True
																else:
																	return True
														else:
															if(angle <= -0.2821303606033325):
																if(y_velocity <= -0.5001321136951447):
																	if(angle <= -0.33944448828697205):
																		if(y_velocity <= -0.5490778088569641):
																			if(angle <= -0.4060227870941162):
																				if(x_velocity <= -0.5743975639343262):
																					return True
																			else:
																				if(lander_y <= 1.1120012402534485):
																					return True
																				else:
																					if(lander_x > -0.1866186559200287):
																						return True
																	else:
																		return True
																else:
																	if(lander_y <= 0.5280610918998718):
																		return True
																	else:
																		if(angle > -0.29706355929374695):
																			if(y_velocity <= -0.4716564267873764):
																				return True
															else:
																if(y_velocity <= -0.4552428871393204):
																	return True
												else:
													if(angle <= -0.05963918752968311):
														if(lander_y <= 0.7037343382835388):
															if(y_velocity <= -0.44581790268421173):
																return True
														else:
															if(x_velocity <= -0.4614197462797165):
																if(y_velocity <= -0.48226308822631836):
																	return True
																else:
																	if(lander_y <= 1.1638135313987732):
																		return True
															else:
																return True
													else:
														if(x_velocity > -0.5055150985717773):
															return True
											else:
												if(angle_velocity <= -0.07099784910678864):
													if(angle_velocity <= -0.4391088932752609):
														return True
													else:
														if(x_velocity > -0.10546019300818443):
															if(y_velocity <= -0.31656259298324585):
																return True
												else:
													if(angle_velocity <= -0.06470226496458054):
														return True
													else:
														if(angle_velocity > -0.06276504695415497):
															if(angle <= -0.0328125786036253):
																if(y_velocity <= -0.30547480285167694):
																	if(x_velocity <= -0.17753219604492188):
																		if(y_velocity <= -0.33098115026950836):
																			return True
																	else:
																		return True
										else:
											if(angle <= 0.0052619194611907005):
												if(lander_y > 0.8310801386833191):
													if(y_velocity <= -0.3124561607837677):
														return True
													else:
														if(y_velocity > -0.31065545976161957):
															return True
											else:
												if(x_velocity > -0.09490720555186272):
													return True
									else:
										if(lander_y <= 0.43368667364120483):
											if(y_velocity <= -0.24037925899028778):
												if(x_velocity > -0.13334935158491135):
													return True
											else:
												if(lander_x > 0.09381012618541718):
													if(angle_velocity > -0.08190915361046791):
														if(x_velocity <= -0.09435850754380226):
															return True
														else:
															if(x_velocity > -0.07662615180015564):
																return True
										else:
											if(angle <= 0.003303513047285378):
												if(lander_x <= 0.0578050147742033):
													if(x_velocity <= -0.10827558860182762):
														if(angle > -0.04051966778934002):
															if(y_velocity <= -0.2685312330722809):
																return True
													else:
														if(lander_x <= 0.05524273030459881):
															if(lander_x <= -0.04958477057516575):
																if(lander_x > -0.05036306381225586):
																	return True
														else:
															return True
											else:
												if(y_velocity <= -0.28821198642253876):
													return True
								else:
									if(x_velocity <= -0.28267785906791687):
										if(angle > -0.1505107581615448):
											if(x_velocity > -0.5018223226070404):
												if(y_velocity <= -0.3828060030937195):
													return True
							else:
								if(y_velocity <= -0.3092031627893448):
									if(lander_x <= 0.034208107739686966):
										if(x_velocity <= -0.07069391012191772):
											if(angle <= -0.058789392933249474):
												if(lander_y > 0.9564158618450165):
													if(y_velocity <= -0.39373779296875):
														if(lander_y <= 0.98670294880867):
															if(angle > -0.35545089840888977):
																return True
														else:
															if(x_velocity <= -0.2154904454946518):
																if(angle_velocity <= -0.0469475407153368):
																	if(y_velocity <= -0.5579902827739716):
																		return True
																else:
																	return True
													else:
														if(angle_velocity > -0.03710435330867767):
															if(x_velocity > -0.18838712573051453):
																return True
											else:
												if(x_velocity > -0.3226556330919266):
													if(x_velocity <= -0.07414290308952332):
														return True
													else:
														if(x_velocity > -0.07244673371315002):
															return True
									else:
										if(y_velocity <= -0.31185534596443176):
											if(lander_y <= 0.7093349397182465):
												if(angle_velocity <= -0.044822121039032936):
													return True
											else:
												if(y_velocity <= -0.31443098187446594):
													return True
												else:
													if(y_velocity > -0.31403957307338715):
														return True
										else:
											if(angle <= -0.033107586205005646):
												if(angle_velocity > -0.034461623057723045):
													return True
											else:
												return True
								else:
									if(lander_y <= 0.7466024160385132):
										if(angle <= -0.03484991937875748):
											if(x_velocity <= -0.08155859261751175):
												if(angle_velocity <= -0.022684134542942047):
													if(y_velocity <= -0.2341933324933052):
														if(angle_velocity <= -0.028814148157835007):
															if(angle_velocity <= -0.03044154029339552):
																if(angle <= -0.05913454294204712):
																	if(angle <= -0.061223698779940605):
																		return True
																else:
																	if(x_velocity <= -0.09463442116975784):
																		if(angle_velocity <= -0.0401531346142292):
																			return True
																	else:
																		return True
														else:
															return True
											else:
												if(angle <= -0.03599567338824272):
													if(angle <= -0.06680350378155708):
														return True
													else:
														if(y_velocity <= -0.2807130515575409):
															if(angle > -0.04795508272945881):
																return True
										else:
											if(y_velocity <= -0.2367466762661934):
												if(angle <= -0.002169712446630001):
													return True
												else:
													if(lander_x > 0.0646444782614708):
														return True
											else:
												if(angle > -0.013058193027973175):
													return True
									else:
										if(y_velocity <= -0.2770034819841385):
											if(lander_y <= 0.9185478091239929):
												if(angle <= -0.0332136545330286):
													if(angle_velocity > -0.02201506309211254):
														return True
												else:
													return True
						else:
							if(angle_velocity <= -0.05213030055165291):
								if(lander_y <= 0.026998624205589294):
									return True
								else:
									if(lander_y <= 0.45490846037864685):
										if(y_velocity <= -0.22937697172164917):
											if(angle > -0.018974131904542446):
												if(lander_x <= 0.015254211612045765):
													if(y_velocity <= -0.24898098409175873):
														return True
													else:
														if(lander_y <= 0.3079184591770172):
															if(y_velocity > -0.23525803536176682):
																return True
							else:
								if(lander_x <= 0.006706619169563055):
									if(angle <= -0.011310861445963383):
										if(y_velocity <= -0.23208345472812653):
											if(lander_y <= 0.3656506836414337):
												if(angle <= -0.03730302304029465):
													if(lander_y > 0.3085542172193527):
														return True
												else:
													if(lander_x <= -0.15789341926574707):
														if(lander_x <= -0.21045448631048203):
															return True
													else:
														return True
											else:
												if(x_velocity <= -0.04091320000588894):
													if(y_velocity <= -0.24923568964004517):
														if(angle_velocity <= -0.040699757635593414):
															if(y_velocity <= -0.29631151258945465):
																if(lander_y <= 1.1595101654529572):
																	return True
														else:
															if(lander_y <= 0.9674433171749115):
																return True
															else:
																if(y_velocity <= -0.3275309354066849):
																	return True
												else:
													if(angle <= -0.04664045386016369):
														if(angle_velocity <= -0.023225690238177776):
															return True
										else:
											if(y_velocity <= -0.2172534391283989):
												if(lander_y <= 0.01735436636954546):
													return True
												else:
													if(lander_x <= -0.2258301004767418):
														if(lander_x > -0.2450345754623413):
															return True
											else:
												return True
									else:
										if(lander_y <= 1.0421459078788757):
											if(y_velocity <= -0.21985971182584763):
												if(angle_velocity <= -0.033265724778175354):
													if(lander_y <= 0.3868452161550522):
														if(angle <= -0.0037476179422810674):
															if(y_velocity <= -0.23523617535829544):
																return True
															else:
																if(angle_velocity > -0.038739876821637154):
																	return True
														else:
															if(lander_x <= -0.0060964582953602076):
																return True
													else:
														if(y_velocity <= -0.281961053609848):
															if(x_velocity > -0.03690149076282978):
																return True
														else:
															if(lander_x <= -0.12462563440203667):
																return True
												else:
													if(angle_velocity <= -0.020480354316532612):
														if(lander_y <= 0.42272621393203735):
															return True
														else:
															if(lander_x <= -0.035082245245575905):
																if(x_velocity > 0.029348866548389196):
																	return True
															else:
																return True
											else:
												if(x_velocity <= 0.03791380859911442):
													if(lander_y <= 0.2066478729248047):
														return True
												else:
													if(lander_x <= -0.2716696262359619):
														return True
										else:
											if(x_velocity <= -0.03997028432786465):
												return True
								else:
									if(y_velocity <= -0.2660217881202698):
										if(lander_y <= 0.7570912539958954):
											if(x_velocity > -0.06046063452959061):
												if(lander_x <= 0.12493033334612846):
													return True
												else:
													if(lander_x > 0.13070178031921387):
														return True
										else:
											if(y_velocity <= -0.2922917902469635):
												return True
									else:
										if(angle <= 0.002455090289004147):
											if(lander_y <= 0.004407272324897349):
												return True
											else:
												if(angle_velocity <= -0.045211587101221085):
													if(lander_y <= 0.22236651182174683):
														if(y_velocity <= -0.2337423786520958):
															return True
												else:
													if(lander_x > 0.06801901012659073):
														if(lander_x <= 0.07907114177942276):
															if(angle_velocity > -0.03367750532925129):
																if(angle <= -0.010514833498746157):
																	return True
																else:
																	if(lander_y > 0.39454948902130127):
																		return True
										else:
											if(angle_velocity <= -0.03174342028796673):
												if(y_velocity > -0.23556186258792877):
													return True
											else:
												if(y_velocity <= -0.2321210727095604):
													if(lander_x <= 0.11557965353131294):
														return True
												else:
													if(lander_y <= 0.4520876258611679):
														if(y_velocity <= -0.22256776690483093):
															return True
					else:
						if(y_velocity <= -0.2789912819862366):
							if(angle_velocity <= -0.09004996344447136):
								if(angle <= 0.08533484488725662):
									if(y_velocity <= -0.3096257150173187):
										return True
									else:
										if(lander_x <= 0.18775305151939392):
											if(angle > 0.015496364794671535):
												if(x_velocity > 0.011610974557697773):
													if(x_velocity <= 0.02092286106199026):
														return True
										else:
											return True
								else:
									if(y_velocity <= -0.3927517533302307):
										return True
									else:
										if(angle <= 0.2851242274045944):
											if(x_velocity <= -0.3852566331624985):
												if(lander_y <= 0.8057451844215393):
													return True
											else:
												return True
										else:
											if(x_velocity <= -0.09542341157793999):
												if(angle <= 0.4136881083250046):
													if(lander_y > 0.8929497301578522):
														return True
											else:
												if(lander_y <= 1.0349815487861633):
													return True
							else:
								if(angle <= 0.021439004689455032):
									if(x_velocity <= -0.05827265419065952):
										if(x_velocity > -0.12656989693641663):
											return True
									else:
										if(angle_velocity > -0.026983673684298992):
											return True
								else:
									if(angle <= 0.3775688335299492):
										if(y_velocity <= -0.284874826669693):
											if(lander_y <= 1.2326122522354126):
												return True
											else:
												if(lander_y > 1.2358664274215698):
													return True
										else:
											if(y_velocity > -0.28447917103767395):
												return True
									else:
										if(lander_y > 1.050563395023346):
											return True
						else:
							if(lander_y <= 0.3803439140319824):
								if(angle_velocity <= -0.0659567192196846):
									if(lander_y <= 0.30862589180469513):
										if(x_velocity <= -0.02822474204003811):
											return True
									else:
										return True
								else:
									if(angle_velocity <= -0.05572383664548397):
										if(angle_velocity <= -0.05819185450673103):
											return True
									else:
										return True
							else:
								if(x_velocity <= -0.0604530181735754):
									if(angle_velocity > -0.03455090709030628):
										return True
								else:
									if(angle <= 0.16142796725034714):
										if(angle_velocity <= -0.08607826009392738):
											if(y_velocity <= -0.2488519698381424):
												if(lander_y <= 1.2703145742416382):
													if(lander_y <= 1.1099320650100708):
														if(angle <= 0.11882057413458824):
															if(x_velocity <= -0.02919619996100664):
																if(lander_x > 0.1030145138502121):
																	return True
														else:
															return True
												else:
													if(angle <= 0.14005474001169205):
														return True
											else:
												if(x_velocity <= 0.06888234242796898):
													if(angle <= 0.12855295836925507):
														if(y_velocity <= -0.24604059755802155):
															return True
										else:
											if(y_velocity <= -0.2474518120288849):
												if(x_velocity <= 0.005094257416203618):
													if(lander_y <= 0.9323590397834778):
														if(lander_y <= 0.7673076391220093):
															return True
														else:
															if(angle_velocity > -0.05070433206856251):
																if(lander_x > 0.0711735226213932):
																	return True
													else:
														if(y_velocity <= -0.26060667634010315):
															if(angle <= 0.060243748128414154):
																if(angle_velocity <= -0.037429384887218475):
																	if(y_velocity <= -0.27316708862781525):
																		if(y_velocity > -0.27879194915294647):
																			if(angle <= 0.05794862471520901):
																				return True
															else:
																if(y_velocity <= -0.26502393186092377):
																	if(x_velocity > -0.032922858372330666):
																		if(y_velocity <= -0.2686959505081177):
																			return True
																		else:
																			if(angle > 0.09161268919706345):
																				return True
												else:
													if(y_velocity <= -0.2529370039701462):
														if(angle_velocity <= -0.08128143846988678):
															if(y_velocity <= -0.2695906460285187):
																return True
														else:
															if(lander_y <= 1.288892149925232):
																if(lander_y <= 1.116899013519287):
																	if(lander_x <= 0.06785836070775986):
																		if(x_velocity <= 0.0815524123609066):
																			return True
																	else:
																		if(angle_velocity > -0.04478166997432709):
																			if(y_velocity > -0.26847679913043976):
																				return True
																else:
																	if(lander_x > 0.04910011403262615):
																		if(angle_velocity <= -0.06591363810002804):
																			if(x_velocity > 0.06677966564893723):
																				return True
																		else:
																			return True
															else:
																if(x_velocity > 0.028238259255886078):
																	return True
													else:
														if(angle_velocity > -0.0572066493332386):
															if(x_velocity <= 0.08906363695859909):
																return True
											else:
												if(lander_y <= 1.1120572686195374):
													if(x_velocity > 0.022168805822730064):
														if(y_velocity <= -0.24030151218175888):
															if(x_velocity <= 0.08545957133173943):
																return True
														else:
															if(x_velocity > 0.03946295753121376):
																if(y_velocity <= -0.22815317660570145):
																	if(lander_x <= -0.07420191541314125):
																		if(lander_x > -0.2219446375966072):
																			if(y_velocity <= -0.23037920147180557):
																				return True
																			else:
																				if(lander_x <= -0.08087301254272461):
																					return True
																else:
																	if(angle_velocity <= -0.038002848625183105):
																		if(x_velocity > 0.08357850089669228):
																			return True
												else:
													if(x_velocity > 0.0538919772952795):
														if(angle <= 0.12973199039697647):
															if(angle_velocity > -0.03532067779451609):
																return True
														else:
															if(y_velocity <= -0.23639965057373047):
																if(y_velocity > -0.24073318392038345):
																	return True
									else:
										if(angle_velocity > -0.1415172442793846):
											if(y_velocity <= -0.22405388206243515):
												if(lander_x <= 0.07194094732403755):
													if(x_velocity <= 0.14968694746494293):
														return True
												else:
													if(angle_velocity <= -0.08016607165336609):
														if(angle <= 0.1941826343536377):
															if(y_velocity <= -0.2504490092396736):
																return True
															else:
																if(x_velocity <= 0.10351002216339111):
																	if(lander_y > 1.2780703902244568):
																		return True
														else:
															return True
													else:
														return True
											else:
												if(angle > 0.22229371219873428):
													if(lander_y <= 1.3832947611808777):
														return True
			else:
				if(lander_y <= 0.44464150071144104):
					if(x_velocity <= -0.030995020642876625):
						if(y_velocity <= -0.2285304218530655):
							if(y_velocity <= -0.2425948679447174):
								if(angle_velocity <= 0.18433533608913422):
									if(angle <= -0.1823166161775589):
										if(y_velocity <= -0.35034099221229553):
											if(angle_velocity > 0.020756579469889402):
												if(y_velocity <= -0.37872400879859924):
													return True
												else:
													if(x_velocity > -0.2565072849392891):
														return True
										else:
											if(angle_velocity > 0.16256096959114075):
												return True
									else:
										if(angle_velocity <= -0.01853099837899208):
											if(x_velocity > -0.04702067747712135):
												return True
										else:
											if(y_velocity <= -0.2446996495127678):
												if(y_velocity <= -0.25114379823207855):
													return True
												else:
													if(angle > -0.049739085137844086):
														return True
											else:
												if(lander_y <= 0.29604822397232056):
													return True
								else:
									if(lander_y > 0.31003719568252563):
										return True
							else:
								if(lander_y <= 0.21119682490825653):
									if(lander_x > -0.09682907909154892):
										if(y_velocity <= -0.22970101237297058):
											return True
										else:
											if(lander_x > -0.0134868617169559):
												return True
								else:
									if(x_velocity <= -0.04663626477122307):
										if(y_velocity > -0.23095610737800598):
											return True
									else:
										return True
						else:
							if(lander_y <= 0.06979820504784584):
								return True
							else:
								if(y_velocity <= -0.22340109944343567):
									if(y_velocity > -0.2253951132297516):
										return True
								else:
									if(angle_velocity <= -0.014180924743413925):
										if(lander_y <= 0.2906220406293869):
											return True
					else:
						if(angle <= -0.018957579508423805):
							if(angle_velocity <= -0.010836374945938587):
								if(angle > -0.02005318272858858):
									if(lander_y <= 0.20038695260882378):
										return True
							else:
								if(angle_velocity <= 0.015236042439937592):
									if(x_velocity <= 0.02032781345769763):
										if(lander_x <= 0.022630739491432905):
											if(angle_velocity <= 0.013318499084562063):
												if(x_velocity <= 0.010799406562000513):
													return True
												else:
													if(x_velocity > 0.012684646993875504):
														return True
										else:
											if(y_velocity <= -0.24603844434022903):
												return True
								else:
									if(y_velocity <= -0.21480269730091095):
										if(lander_x > -0.1693543866276741):
											if(y_velocity <= -0.21757720410823822):
												if(x_velocity <= 0.03027899842709303):
													return True
												else:
													if(lander_x > -0.027924250811338425):
														return True
											else:
												if(y_velocity > -0.21713373064994812):
													return True
						else:
							if(x_velocity <= 0.15747050940990448):
								if(y_velocity <= -0.2333202287554741):
									return True
								else:
									if(angle <= 0.017681497149169445):
										if(lander_y <= 0.3060990273952484):
											if(lander_y <= 1.520871592219919e-05):
												if(y_velocity > -0.21956631541252136):
													return True
											else:
												if(y_velocity <= -0.21841178089380264):
													return True
												else:
													if(lander_y <= 0.21786969155073166):
														if(angle <= 0.01190967345610261):
															if(y_velocity <= -0.21697809547185898):
																if(y_velocity <= -0.21709344536066055):
																	return True
															else:
																return True
														else:
															if(x_velocity <= 0.04904969595372677):
																return True
													else:
														if(lander_y <= 0.245440311729908):
															if(y_velocity <= -0.21642522513866425):
																return True
														else:
															if(lander_y > 0.26980745792388916):
																if(x_velocity <= 0.07172374054789543):
																	return True
										else:
											if(y_velocity <= -0.22006822377443314):
												if(angle_velocity <= -0.0023580207052873448):
													if(lander_y <= 0.38160085678100586):
														if(lander_y > 0.3212590664625168):
															return True
												else:
													if(angle <= -0.004273940809071064):
														if(angle <= -0.014122632332146168):
															if(x_velocity > 0.017201653216034174):
																return True
													else:
														if(angle_velocity <= 0.015930761583149433):
															if(x_velocity > -0.0025078682228922844):
																return True
														else:
															return True
									else:
										return True
				else:
					if(y_velocity <= -0.2594956308603287):
						if(x_velocity <= 0.6525615453720093):
							if(lander_x <= 0.02307958621531725):
								if(lander_y <= 1.373055338859558):
									if(y_velocity <= -0.29296332597732544):
										if(x_velocity <= -0.10625281929969788):
											if(y_velocity <= -0.3361341655254364):
												if(angle_velocity > -0.016051679383963346):
													if(lander_y <= 1.3320707082748413):
														if(angle_velocity <= 0.19024396687746048):
															if(lander_x <= -0.27865569293498993):
																if(y_velocity <= -0.5708374083042145):
																	return True
																else:
																	if(lander_y <= 0.9304526746273041):
																		if(y_velocity <= -0.4900723993778229):
																			if(angle_velocity <= 0.07761191949248314):
																				if(lander_y > 0.9092622697353363):
																					return True
																			else:
																				if(lander_y <= 0.8301143646240234):
																					return True
																				else:
																					if(y_velocity <= -0.5267745554447174):
																						return True
																					else:
																						if(x_velocity > -0.21264638006687164):
																							return True
																		else:
																			if(angle > -0.3217872977256775):
																				if(angle <= -0.2993170768022537):
																					return True
															else:
																if(angle_velocity <= 0.030084882862865925):
																	if(y_velocity <= -0.3749479651451111):
																		if(lander_x <= -0.2462327927350998):
																			if(x_velocity <= -0.46916714310646057):
																				return True
																		else:
																			if(lander_y > 0.919672816991806):
																				if(x_velocity <= -0.19646716117858887):
																					if(lander_x <= -0.21625898033380508):
																						if(angle <= -0.36997316777706146):
																							return True
																					else:
																						return True
																				else:
																					if(angle_velocity > 0.006126062478870153):
																						return True
																	else:
																		if(angle > -0.11535299941897392):
																			return True
																else:
																	if(y_velocity <= -0.3564331829547882):
																		if(lander_y > 0.7881717085838318):
																			if(angle <= -0.2667078524827957):
																				if(angle <= -0.2748633772134781):
																					if(y_velocity <= -0.45100337266921997):
																						if(angle_velocity <= 0.04467276483774185):
																							if(lander_y > 0.9391319453716278):
																								return True
																						else:
																							if(lander_y <= 1.0466598868370056):
																								return True
																							else:
																								if(lander_y > 1.0578892230987549):
																									return True
																					else:
																						if(angle > -0.29316338896751404):
																							return True
																			else:
																				return True
																	else:
																		if(x_velocity > -0.14268840849399567):
																			return True
														else:
															return True
													else:
														if(y_velocity > -0.46590209007263184):
															if(x_velocity <= -0.2255719006061554):
																return True
											else:
												if(x_velocity > -0.11953193694353104):
													if(y_velocity <= -0.32181912660598755):
														return True
										else:
											if(x_velocity <= 0.24357302486896515):
												if(angle <= -0.2787962257862091):
													if(lander_x > -0.3146837204694748):
														return True
												else:
													if(y_velocity <= -0.31527596712112427):
														if(lander_y <= 1.3443206548690796):
															if(angle <= -0.2267390713095665):
																if(y_velocity <= -0.3536236584186554):
																	return True
																else:
																	if(angle_velocity > 0.2365514561533928):
																		return True
															else:
																if(x_velocity <= -0.0838325135409832):
																	if(x_velocity <= -0.08487306162714958):
																		return True
																else:
																	return True
														else:
															if(lander_y > 1.3504712581634521):
																return True
													else:
														if(lander_y <= 1.1467329859733582):
															if(angle > -0.19269920140504837):
																if(y_velocity > -0.3152293413877487):
																	if(angle_velocity > -0.017945660278201103):
																		if(lander_x <= 0.0148178581148386):
																			if(angle <= -0.06394661590456963):
																				if(angle_velocity <= 0.08804255723953247):
																					if(lander_y <= 1.0991204977035522):
																						if(y_velocity <= -0.3100430518388748):
																							return True
																				else:
																					if(lander_y <= 0.8191960752010345):
																						return True
																					else:
																						if(angle_velocity <= 0.1113610602915287):
																							return True
																						else:
																							if(angle <= -0.15219192951917648):
																								return True
																			else:
																				if(x_velocity <= -0.07739036530256271):
																					if(x_velocity <= -0.07816635444760323):
																						return True
																				else:
																					if(angle <= -0.05298611894249916):
																						if(angle <= -0.0566953644156456):
																							return True
																					else:
																						return True
														else:
															if(x_velocity <= -0.03966103307902813):
																if(angle <= -0.020699504762887955):
																	if(y_velocity <= -0.3070172220468521):
																		return True
															else:
																if(angle > -0.013819488696753979):
																	if(lander_x > -0.027727698907256126):
																		return True
									else:
										if(lander_y <= 0.6716166436672211):
											if(angle > -0.13102174922823906):
												if(x_velocity <= -0.07650924474000931):
													if(angle_velocity <= 0.02510820794850588):
														if(y_velocity <= -0.27965205907821655):
															return True
												else:
													if(angle_velocity <= 0.005553795723244548):
														if(angle_velocity <= 0.004267820157110691):
															if(angle <= -0.04568473622202873):
																if(x_velocity <= -0.06198539957404137):
																	return True
																else:
																	if(angle > -0.047806499525904655):
																		if(lander_x > -0.16671299934387207):
																			return True
															else:
																if(lander_x <= -0.0005010127788409591):
																	return True
																else:
																	if(lander_y > 0.6457030475139618):
																		return True
													else:
														if(angle <= -0.10513648390769958):
															if(x_velocity > 0.03779068402945995):
																return True
														else:
															if(angle <= -0.06310204230248928):
																if(angle_velocity > 0.10332319140434265):
																	return True
															else:
																return True
										else:
											if(x_velocity <= -0.023015913553535938):
												if(y_velocity <= -0.2758352607488632):
													if(lander_y <= 0.9605807363986969):
														if(angle > -0.05462417006492615):
															if(angle <= -0.043146610260009766):
																if(lander_y > 0.8127729296684265):
																	return True
															else:
																if(y_velocity <= -0.27999627590179443):
																	return True
																else:
																	if(y_velocity > -0.2784825712442398):
																		return True
													else:
														if(lander_x <= -0.03730282746255398):
															if(angle > -0.023724621161818504):
																if(x_velocity > -0.04813620634377003):
																	return True
											else:
												if(angle <= -0.05630537122488022):
													if(x_velocity > 0.03674690052866936):
														if(y_velocity <= -0.275630459189415):
															return True
												else:
													if(angle_velocity <= 0.029466263949871063):
														if(angle <= 0.008146327221766114):
															if(y_velocity <= -0.284311980009079):
																if(x_velocity <= 0.003164541267324239):
																	if(angle > -0.038382926024496555):
																		return True
															else:
																if(lander_x > -0.009977101814001799):
																	if(y_velocity > -0.2799728512763977):
																		return True
														else:
															if(angle_velocity <= 0.026611480861902237):
																if(y_velocity <= -0.2637462913990021):
																	return True
																else:
																	if(y_velocity > -0.2631078213453293):
																		return True
													else:
														if(lander_y <= 1.0080597698688507):
															if(lander_y <= 0.9281871616840363):
																return True
															else:
																if(x_velocity <= 0.06501607969403267):
																	return True
														else:
															if(angle_velocity > 0.07091180607676506):
																return True
								else:
									if(x_velocity <= -0.05172503925859928):
										if(x_velocity <= -0.05421929992735386):
											if(angle <= -0.1460430920124054):
												return True
											else:
												if(x_velocity > -0.06594342179596424):
													if(y_velocity <= -0.32653066515922546):
														return True
										else:
											return True
									else:
										if(y_velocity <= -0.333544060587883):
											return True
							else:
								if(lander_x <= 0.22602467983961105):
									if(x_velocity <= -0.07535390555858612):
										if(y_velocity <= -0.28644469380378723):
											if(lander_y <= 1.0477442741394043):
												if(angle <= -0.11666755005717278):
													if(y_velocity <= -0.31631308794021606):
														if(angle <= -0.11735211685299873):
															return True
												else:
													return True
											else:
												if(y_velocity <= -0.3154904693365097):
													return True
										else:
											if(lander_x <= 0.09229903295636177):
												if(angle_velocity <= -0.008074681041762233):
													if(x_velocity <= -0.09963561594486237):
														if(y_velocity <= -0.27557606995105743):
															return True
												else:
													if(y_velocity <= -0.27435214817523956):
														if(lander_y <= 0.7805542349815369):
															if(lander_y > 0.596069872379303):
																if(angle > -0.10737456381320953):
																	return True
											else:
												return True
									else:
										if(y_velocity <= -0.2709008604288101):
											return True
										else:
											if(lander_x <= 0.14790429919958115):
												if(angle > -0.03736453130841255):
													if(angle_velocity <= -0.01852460578083992):
														if(lander_y <= 0.8436659574508667):
															return True
													else:
														if(lander_y <= 1.433857500553131):
															if(y_velocity <= -0.26241831481456757):
																if(angle_velocity <= -0.01747903134673834):
																	if(lander_y > 0.7911043167114258):
																		return True
																else:
																	return True
															else:
																if(lander_x <= 0.08574771881103516):
																	if(lander_x > 0.02779297810047865):
																		if(y_velocity <= -0.2608637511730194):
																			if(y_velocity <= -0.26097172498703003):
																				if(lander_x <= 0.06775975227355957):
																					return True
																		else:
																			return True
														else:
															if(y_velocity > -0.2648572474718094):
																return True
								else:
									if(y_velocity <= -0.3299812525510788):
										return True
									else:
										if(x_velocity > 0.14926587045192719):
											if(y_velocity <= -0.28549303114414215):
												return True
					else:
						if(x_velocity <= 0.009772160556167364):
							if(y_velocity <= -0.24483375251293182):
								if(lander_y <= 0.6944023370742798):
									if(x_velocity <= -0.04959486611187458):
										if(angle_velocity <= -0.004452854162082076):
											if(lander_y <= 0.5145226567983627):
												return True
										else:
											if(lander_y > 0.6500652432441711):
												if(lander_x <= 0.10824999958276749):
													return True
									else:
										if(angle_velocity <= 0.016676543280482292):
											if(angle > -0.008457919582724571):
												if(lander_x <= 0.08355550840497017):
													if(lander_y <= 0.6842318773269653):
														return True
												else:
													if(angle_velocity > -0.0051709983963519335):
														return True
										else:
											if(angle > -0.04912423528730869):
												if(angle <= 0.013461377006024122):
													if(lander_y <= 0.6135468184947968):
														return True
													else:
														if(angle > -0.017647644970566034):
															return True
								else:
									if(angle_velocity > -0.011723455041646957):
										if(x_velocity <= 0.006656566169112921):
											if(y_velocity <= -0.24526099860668182):
												if(lander_y <= 0.764032632112503):
													if(angle_velocity <= -0.003753315657377243):
														if(angle > -0.0035565290600061417):
															return True
													else:
														if(y_velocity <= -0.2589692771434784):
															return True
											else:
												return True
										else:
											if(lander_y > 0.7904876172542572):
												return True
							else:
								if(angle_velocity > -0.017813351936638355):
									if(angle > -0.031075498089194298):
										if(angle_velocity <= -0.005560303805395961):
											if(angle > -0.007473527453839779):
												if(lander_y <= 0.49512678384780884):
													return True
										else:
											if(x_velocity > -0.018309815786778927):
												if(lander_x > 0.08038429915904999):
													if(lander_x <= 0.10624818876385689):
														return True
						else:
							if(y_velocity <= -0.2244303897023201):
								if(lander_y <= 0.6337423324584961):
									if(angle <= -0.05921509116888046):
										if(y_velocity <= -0.24954859167337418):
											return True
									else:
										if(y_velocity <= -0.2429022565484047):
											return True
										else:
											if(x_velocity > 0.01496987696737051):
												if(angle <= 0.02831197716295719):
													if(angle_velocity <= 0.04527553729712963):
														if(angle <= 0.013827523216605186):
															if(x_velocity <= 0.08098047971725464):
																if(lander_y <= 0.46728184819221497):
																	if(angle_velocity <= 0.010481433477252722):
																		return True
																else:
																	return True
														else:
															if(x_velocity <= 0.13157899677753448):
																if(angle_velocity <= 0.03676746226847172):
																	return True
													else:
														if(x_velocity <= 0.1530468538403511):
															if(x_velocity <= 0.0677870661020279):
																if(angle_velocity <= 0.09733923897147179):
																	if(lander_y <= 0.596748024225235):
																		return True
																	else:
																		if(angle_velocity <= 0.06928367167711258):
																			return True
															else:
																return True
												else:
													return True
								else:
									if(angle <= 0.13975286483764648):
										if(y_velocity <= -0.249237060546875):
											if(lander_y <= 1.2836709022521973):
												if(angle_velocity <= 0.105367511510849):
													if(angle_velocity > -0.019210652448236942):
														if(x_velocity <= 0.014196524396538734):
															if(angle <= 0.03387469984591007):
																return True
														else:
															if(x_velocity <= 0.10053893178701401):
																return True
															else:
																if(lander_x > -0.10623187944293022):
																	return True
											else:
												if(x_velocity > 0.1511201709508896):
													return True
										else:
											if(lander_y <= 0.926637202501297):
												if(angle > 0.012374273966997862):
													if(y_velocity <= -0.23654136061668396):
														if(x_velocity <= 0.1023041196167469):
															return True
													else:
														if(x_velocity <= 0.09398551657795906):
															if(angle > 0.05475660040974617):
																return True
														else:
															return True
											else:
												if(lander_y <= 1.3702694177627563):
													if(y_velocity <= -0.24629773199558258):
														if(angle > 0.11105184629559517):
															return True
													else:
														if(angle_velocity <= -0.012375698890537024):
															if(x_velocity > 0.07926076650619507):
																return True
														else:
															if(y_velocity <= -0.24415922909975052):
																if(x_velocity > 0.08026551268994808):
																	return True
												else:
													if(angle_velocity > 0.12907720357179642):
														if(x_velocity <= 0.1977105289697647):
															return True
									else:
										if(angle <= 0.46861210465431213):
											return True
							else:
								if(angle_velocity <= 0.05199507810175419):
									if(angle_velocity <= 0.034516019746661186):
										if(angle <= 0.0669519193470478):
											if(x_velocity > 0.06815199181437492):
												if(lander_y > 0.7828270196914673):
													return True
										else:
											if(x_velocity > 0.25485916435718536):
												return True
									else:
										if(lander_x <= -0.01775689097121358):
											if(x_velocity > 0.061260635033249855):
												return True
								else:
									if(x_velocity <= 0.25101426988840103):
										if(lander_y <= 0.5400468111038208):
											if(x_velocity <= 0.11229487136006355):
												if(lander_y <= 0.4670831710100174):
													return True
											else:
												if(angle > -0.05024145543575287):
													if(lander_y > 0.45589679479599):
														return True
		else:
			if(y_velocity <= -0.04625159688293934):
				if(angle_velocity <= -0.020012114197015762):
					if(x_velocity > -0.062468184158205986):
						if(angle <= 0.004466760903596878):
							if(lander_y <= 1.4811075925827026):
								if(angle_velocity > -0.03305315971374512):
									if(x_velocity > -0.025241411291062832):
										if(lander_y <= 0.07490148209035397):
											return True
						else:
							if(y_velocity <= -0.19456586986780167):
								if(lander_y <= 0.3112007826566696):
									if(angle_velocity <= -0.03830353356897831):
										if(angle > 0.010316614527255297):
											if(angle_velocity > -0.059264520183205605):
												if(lander_y <= 0.2251387983560562):
													if(x_velocity <= 0.023855773732066154):
														return True
													else:
														if(lander_x <= -0.2420194074511528):
															return True
												else:
													if(lander_y > 0.2838802933692932):
														return True
									else:
										if(x_velocity > -0.04011731967329979):
											if(x_velocity <= 0.10860027000308037):
												if(angle <= 0.02127546537667513):
													if(angle <= 0.014985323883593082):
														return True
													else:
														if(lander_x > -0.048516225069761276):
															if(angle_velocity <= -0.03418443538248539):
																return True
												else:
													return True
								else:
									if(lander_y <= 0.3769782781600952):
										if(lander_x <= -0.007061862852424383):
											if(angle > 0.06673962250351906):
												if(y_velocity <= -0.20471953600645065):
													return True
									else:
										if(x_velocity <= 0.19233880192041397):
											if(angle_velocity > -0.1404288038611412):
												if(lander_x > -0.23554258048534393):
													if(lander_y <= 0.43535158038139343):
														return True
										else:
											if(x_velocity <= 0.27829059958457947):
												if(lander_y > 1.313782513141632):
													return True
							else:
								if(lander_x <= 0.09790630266070366):
									if(angle_velocity <= -0.04235716536641121):
										if(lander_y <= 0.27968253195285797):
											if(angle > 0.04661379009485245):
												if(angle <= 0.05018204264342785):
													return True
									else:
										if(y_velocity <= -0.16684778034687042):
											if(x_velocity > 0.0077046051155775785):
												if(angle <= 0.06907186284661293):
													if(lander_x > -0.07053551450371742):
														if(angle_velocity > -0.03958926163613796):
															if(x_velocity <= 0.020452387165278196):
																if(lander_y > 0.05385594069957733):
																	if(angle > 0.025027060182765126):
																		return True
												else:
													return True
								else:
									if(x_velocity > 0.2305583357810974):
										if(x_velocity > 0.23397155106067657):
											return True
				else:
					if(y_velocity <= -0.18436022847890854):
						if(x_velocity <= -0.0069253817200660706):
							if(lander_y <= 0.0211697556078434):
								if(lander_y <= 0.01586259389296174):
									if(angle_velocity > 0.20008431375026703):
										return True
								else:
									if(lander_x <= -0.03813023492693901):
										return True
							else:
								if(lander_x <= 0.11992516368627548):
									if(angle > -0.03051120787858963):
										if(y_velocity <= -0.21088775247335434):
											if(y_velocity > -0.21097326278686523):
												return True
								else:
									return True
						else:
							if(lander_x <= -0.042762136086821556):
								if(y_velocity <= -0.20255107432603836):
									if(lander_y <= 0.4827624410390854):
										if(x_velocity <= 0.051810845732688904):
											if(lander_y <= 0.15091170370578766):
												if(angle_velocity > -0.013167968951165676):
													if(angle > -0.023265200667083263):
														if(y_velocity <= -0.20862088352441788):
															if(angle_velocity > 0.001374891260638833):
																if(angle <= -0.0063715053256601095):
																	return True
														else:
															return True
										else:
											if(angle > -0.009217553306370974):
												if(angle_velocity > -0.012879056856036186):
													if(lander_x <= -0.11576604470610619):
														if(y_velocity <= -0.20508630573749542):
															return True
														else:
															if(y_velocity <= -0.2043422982096672):
																if(angle > 0.04920308105647564):
																	return True
															else:
																return True
													else:
														if(x_velocity > 0.059141192585229874):
															if(angle > 0.02305728243663907):
																if(x_velocity <= 0.1062653698027134):
																	return True
																else:
																	if(angle_velocity > 0.052790841087698936):
																		return True
								else:
									if(lander_y <= 0.3891821354627609):
										if(x_velocity <= 0.07820967957377434):
											if(lander_y <= 0.0024011230270843953):
												return True
											else:
												if(angle_velocity <= -0.0004889809933956712):
													if(x_velocity > 0.05140134133398533):
														if(y_velocity <= -0.20081204921007156):
															return True
														else:
															if(angle_velocity > -0.0030889732879586518):
																if(y_velocity > -0.1959468051791191):
																	return True
												else:
													if(y_velocity <= -0.18582746386528015):
														if(lander_x <= -0.05756807327270508):
															if(lander_y <= 0.06238576024770737):
																if(lander_y > 0.05784710496664047):
																	return True
														else:
															if(lander_x <= -0.056616783142089844):
																return True
										else:
											if(lander_x <= -0.2274240478873253):
												if(x_velocity > 0.11409883201122284):
													if(x_velocity <= 0.1454349085688591):
														return True
											else:
												if(x_velocity <= 0.11670643836259842):
													if(y_velocity <= -0.18645817041397095):
														return True
													else:
														if(lander_x > -0.17339437454938889):
															return True
							else:
								if(angle <= 0.03075925912708044):
									if(lander_y <= 0.23827283084392548):
										if(angle_velocity <= 0.005395429907366633):
											if(lander_y <= 0.051877399906516075):
												if(y_velocity <= -0.19031043350696564):
													if(x_velocity > 0.0019591117452364415):
														if(angle_velocity <= 0.0029652915545739233):
															return True
										else:
											if(angle_velocity <= 0.11614060401916504):
												if(y_velocity <= -0.18809842318296432):
													if(angle_velocity <= 0.04781189560890198):
														return True
													else:
														if(lander_y > 0.12213743850588799):
															return True
												else:
													if(lander_x <= -0.019969177432358265):
														return True
								else:
									if(lander_y <= 0.2757747322320938):
										if(y_velocity <= -0.18958498537540436):
											if(x_velocity <= 0.08819332346320152):
												if(y_velocity <= -0.19091307371854782):
													if(angle_velocity <= -0.01807697955518961):
														if(angle_velocity <= -0.0195396663621068):
															return True
													else:
														return True
												else:
													if(y_velocity > -0.1902071237564087):
														return True
										else:
											if(lander_y > 0.11388849839568138):
												if(lander_y <= 0.15782561898231506):
													return True
												else:
													if(angle_velocity <= 0.016652418300509453):
														return True
									else:
										if(x_velocity <= 0.2683706134557724):
											if(lander_x <= 0.03540916554629803):
												if(lander_y <= 0.9386655986309052):
													return True
											else:
												if(lander_y <= 0.4122486710548401):
													if(y_velocity <= -0.19863538444042206):
														if(angle <= 0.05365173518657684):
															if(x_velocity <= 0.04408101551234722):
																return True
														else:
															return True
												else:
													if(lander_x > 0.13416848331689835):
														return True
										else:
											return True
					else:
						if(x_velocity <= 0.3691508024930954):
							if(lander_y <= -0.001645400479901582):
								if(lander_y > -0.006369378650560975):
									return True
							else:
								if(x_velocity > 0.04088269919157028):
									if(lander_y <= 0.11264903098344803):
										if(angle_velocity > 0.004053640004713088):
											if(y_velocity <= -0.16221347451210022):
												if(angle <= 0.03342198394238949):
													if(angle_velocity <= 0.04894179664552212):
														if(x_velocity > 0.0869213379919529):
															return True
												else:
													return True
									else:
										if(y_velocity <= -0.1415981501340866):
											if(angle_velocity > 0.010637735482305288):
												if(y_velocity <= -0.18348319083452225):
													return True
												else:
													if(lander_y > 0.41426412761211395):
														if(lander_y > 0.4249081611633301):
															if(angle > 0.02259056642651558):
																if(y_velocity <= -0.1785217523574829):
																	if(lander_y > 0.9679950177669525):
																		return True
						else:
							if(y_velocity <= -0.1733998954296112):
								return True
	return False

def weShould_right_engine(lander_x, lander_y, x_velocity, y_velocity, angle, angle_velocity, left_leg_contact, right_leg_contact):
	if(right_leg_contact != True):
		if(y_velocity <= -0.2117035612463951):
			if(angle_velocity <= -0.01971765235066414):
				if(x_velocity <= -0.6401405930519104):
					if(y_velocity > -0.522825300693512):
						return True
				else:
					if(angle <= 0.012781189288944006):
						if(x_velocity <= -0.06513240933418274):
							if(angle_velocity <= -0.05249720998108387):
								if(lander_y <= 1.3048996925354004):
									if(y_velocity <= -0.30372199416160583):
										if(angle <= -0.02758705895394087):
											if(y_velocity <= -0.4094874709844589):
												if(angle > -0.1925167441368103):
													if(angle <= -0.05963918752968311):
														if(lander_y > 0.7037343382835388):
															if(x_velocity <= -0.4614197462797165):
																if(y_velocity > -0.48226308822631836):
																	if(lander_y > 1.1638135313987732):
																		return True
													else:
														if(x_velocity <= -0.5055150985717773):
															return True
										else:
											if(angle <= 0.0052619194611907005):
												if(lander_y > 0.8310801386833191):
													if(y_velocity > -0.3124561607837677):
														if(y_velocity <= -0.31065545976161957):
															return True
									else:
										if(lander_y > 0.43368667364120483):
											if(angle <= 0.003303513047285378):
												if(lander_x <= 0.0578050147742033):
													if(x_velocity <= -0.10827558860182762):
														if(angle > -0.04051966778934002):
															if(y_velocity > -0.2685312330722809):
																return True
											else:
												if(y_velocity > -0.28821198642253876):
													if(lander_y > 0.9289388954639435):
														return True
								else:
									if(x_velocity <= -0.28267785906791687):
										if(angle > -0.1505107581615448):
											if(x_velocity <= -0.5018223226070404):
												return True
											else:
												if(y_velocity > -0.3828060030937195):
													return True
									else:
										if(x_velocity <= -0.27727390825748444):
											if(lander_x > -0.044144392013549805):
												return True
							else:
								if(y_velocity <= -0.3092031627893448):
									if(lander_x <= 0.034208107739686966):
										if(x_velocity <= -0.07069391012191772):
											if(angle <= -0.058789392933249474):
												if(lander_y > 0.9564158618450165):
													if(y_velocity > -0.39373779296875):
														if(angle_velocity > -0.03710435330867767):
															if(x_velocity <= -0.18838712573051453):
																return True
											else:
												if(x_velocity <= -0.3226556330919266):
													return True
									else:
										if(y_velocity <= -0.31185534596443176):
											if(lander_y > 0.7093349397182465):
												if(y_velocity > -0.31443098187446594):
													if(y_velocity <= -0.31403957307338715):
														return True
								else:
									if(lander_y <= 0.7466024160385132):
										if(angle <= -0.03484991937875748):
											if(x_velocity <= -0.08155859261751175):
												if(angle_velocity <= -0.022684134542942047):
													if(y_velocity <= -0.2341933324933052):
														if(angle_velocity <= -0.028814148157835007):
															if(angle_velocity <= -0.03044154029339552):
																if(angle > -0.05913454294204712):
																	if(x_velocity <= -0.09463442116975784):
																		if(angle_velocity > -0.0401531346142292):
																			if(y_velocity > -0.2861316651105881):
																				return True
															else:
																if(lander_y <= 0.591789647936821):
																	return True
												else:
													if(angle > -0.053620295599102974):
														return True
											else:
												if(angle > -0.03599567338824272):
													return True
										else:
											if(y_velocity <= -0.2367466762661934):
												if(angle > -0.002169712446630001):
													if(lander_x <= 0.0646444782614708):
														return True
											else:
												if(angle <= -0.013058193027973175):
													if(angle_velocity > -0.044335465878248215):
														return True
									else:
										if(y_velocity <= -0.2770034819841385):
											if(lander_y <= 0.9185478091239929):
												if(angle <= -0.0332136545330286):
													if(angle_velocity <= -0.02201506309211254):
														if(x_velocity <= -0.10539235919713974):
															return True
											else:
												if(angle <= -0.016147284768521786):
													return True
												else:
													if(angle > 0.00015097158029675484):
														return True
										else:
											if(angle <= -0.02650956902652979):
												if(angle <= -0.030107329599559307):
													return True
											else:
												return True
						else:
							if(angle_velocity > -0.05213030055165291):
								if(lander_x <= 0.006706619169563055):
									if(angle <= -0.011310861445963383):
										if(y_velocity <= -0.23208345472812653):
											if(lander_y > 0.3656506836414337):
												if(x_velocity <= -0.04091320000588894):
													if(y_velocity > -0.24923568964004517):
														return True
									else:
										if(lander_y <= 1.0421459078788757):
											if(y_velocity <= -0.21985971182584763):
												if(angle_velocity > -0.033265724778175354):
													if(angle_velocity <= -0.020480354316532612):
														if(lander_y > 0.42272621393203735):
															if(lander_x <= -0.035082245245575905):
																if(x_velocity <= 0.029348866548389196):
																	return True
													else:
														return True
								else:
									if(y_velocity > -0.2660217881202698):
										if(angle <= 0.002455090289004147):
											if(lander_y > 0.004407272324897349):
												if(angle_velocity > -0.045211587101221085):
													if(lander_x > 0.06801901012659073):
														if(lander_x <= 0.07907114177942276):
															if(angle_velocity <= -0.03367750532925129):
																return True
										else:
											if(angle_velocity > -0.03174342028796673):
												if(y_velocity > -0.2321210727095604):
													if(lander_y > 0.4520876258611679):
														return True
					else:
						if(y_velocity <= -0.2789912819862366):
							if(angle_velocity <= -0.09004996344447136):
								if(angle <= 0.08533484488725662):
									if(y_velocity > -0.3096257150173187):
										if(lander_x <= 0.18775305151939392):
											if(angle <= 0.015496364794671535):
												return True
								else:
									if(y_velocity > -0.3927517533302307):
										if(angle <= 0.2851242274045944):
											if(x_velocity <= -0.3852566331624985):
												if(lander_y > 0.8057451844215393):
													return True
										else:
											if(x_velocity <= -0.09542341157793999):
												if(angle <= 0.4136881083250046):
													if(lander_y <= 0.8929497301578522):
														return True
												else:
													return True
											else:
												if(lander_y > 1.0349815487861633):
													return True
							else:
								if(angle <= 0.021439004689455032):
									if(x_velocity <= -0.05827265419065952):
										if(x_velocity <= -0.12656989693641663):
											return True
								else:
									if(angle <= 0.3775688335299492):
										if(y_velocity <= -0.284874826669693):
											if(lander_y > 1.2326122522354126):
												if(lander_y <= 1.2358664274215698):
													return True
									else:
										if(lander_y <= 1.050563395023346):
											return True
						else:
							if(lander_y > 0.3803439140319824):
								if(x_velocity <= -0.0604530181735754):
									if(angle_velocity <= -0.03455090709030628):
										return True
								else:
									if(angle <= 0.16142796725034714):
										if(angle_velocity <= -0.08607826009392738):
											if(y_velocity > -0.2488519698381424):
												if(x_velocity <= 0.06888234242796898):
													if(angle <= 0.12855295836925507):
														if(y_velocity > -0.24604059755802155):
															if(angle_velocity > -0.1274324506521225):
																if(lander_x > -0.057015541940927505):
																	return True
													else:
														return True
										else:
											if(y_velocity <= -0.2474518120288849):
												if(x_velocity <= 0.005094257416203618):
													if(lander_y > 0.9323590397834778):
														if(y_velocity <= -0.26060667634010315):
															if(angle <= 0.060243748128414154):
																if(angle_velocity > -0.037429384887218475):
																	return True
															else:
																if(y_velocity <= -0.26502393186092377):
																	if(x_velocity <= -0.032922858372330666):
																		return True
																	else:
																		if(y_velocity > -0.2686959505081177):
																			if(angle <= 0.09161268919706345):
																				return True
																else:
																	return True
														else:
															return True
												else:
													if(y_velocity <= -0.2529370039701462):
														if(angle_velocity > -0.08128143846988678):
															if(lander_y > 1.288892149925232):
																if(x_velocity <= 0.028238259255886078):
																	return True
											else:
												if(lander_y <= 1.1120572686195374):
													if(x_velocity <= 0.022168805822730064):
														if(y_velocity <= -0.2292398437857628):
															if(lander_y <= 1.0322741270065308):
																if(y_velocity <= -0.245970718562603):
																	if(lander_x <= 0.07522673532366753):
																		return True
															else:
																if(x_velocity <= -0.014843103243038058):
																	return True
														else:
															return True
													else:
														if(y_velocity > -0.24030151218175888):
															if(x_velocity <= 0.03946295753121376):
																if(lander_x <= -0.07193389162421227):
																	return True
												else:
													if(x_velocity <= 0.0538919772952795):
														return True
													else:
														if(angle > 0.12973199039697647):
															if(y_velocity <= -0.23639965057373047):
																if(y_velocity <= -0.24073318392038345):
																	if(lander_y <= 1.2715017199516296):
																		return True
															else:
																return True
									else:
										if(angle_velocity > -0.1415172442793846):
											if(y_velocity <= -0.22405388206243515):
												if(lander_x > 0.07194094732403755):
													if(angle_velocity <= -0.08016607165336609):
														if(angle <= 0.1941826343536377):
															if(y_velocity > -0.2504490092396736):
																if(x_velocity <= 0.10351002216339111):
																	if(lander_y <= 1.2780703902244568):
																		return True
											else:
												if(angle <= 0.22229371219873428):
													if(x_velocity <= 0.19005534052848816):
														return True
			else:
				if(lander_y <= 0.44464150071144104):
					if(x_velocity <= -0.030995020642876625):
						if(y_velocity <= -0.2285304218530655):
							if(y_velocity <= -0.2425948679447174):
								if(angle_velocity <= 0.18433533608913422):
									if(angle > -0.1823166161775589):
										if(angle_velocity > -0.01853099837899208):
											if(y_velocity > -0.2446996495127678):
												if(lander_y > 0.29604822397232056):
													return True
								else:
									if(lander_y <= 0.31003719568252563):
										return True
							else:
								if(lander_y <= 0.21119682490825653):
									if(lander_x <= -0.09682907909154892):
										return True
									else:
										if(y_velocity > -0.22970101237297058):
											if(lander_x <= -0.0134868617169559):
												return True
								else:
									if(x_velocity <= -0.04663626477122307):
										if(y_velocity <= -0.23095610737800598):
											if(lander_x <= 0.052344704046845436):
												return True
						else:
							if(lander_y > 0.06979820504784584):
								if(y_velocity <= -0.22340109944343567):
									if(y_velocity <= -0.2253951132297516):
										if(lander_x > -0.08593611791729927):
											if(y_velocity <= -0.22636540234088898):
												return True
								else:
									if(angle_velocity <= -0.014180924743413925):
										if(lander_y > 0.2906220406293869):
											return True
									else:
										return True
					else:
						if(angle <= -0.018957579508423805):
							if(angle_velocity > -0.010836374945938587):
								if(angle_velocity > 0.015236042439937592):
									if(y_velocity <= -0.21480269730091095):
										if(lander_x <= -0.1693543866276741):
											return True
									else:
										return True
						else:
							if(x_velocity <= 0.15747050940990448):
								if(y_velocity > -0.2333202287554741):
									if(angle <= 0.017681497149169445):
										if(lander_y <= 0.3060990273952484):
											if(lander_y > 1.520871592219919e-05):
												if(y_velocity > -0.21841178089380264):
													if(lander_y <= 0.21786969155073166):
														if(angle <= 0.01190967345610261):
															if(y_velocity <= -0.21697809547185898):
																if(y_velocity > -0.21709344536066055):
																	return True
													else:
														if(lander_y <= 0.245440311729908):
															if(y_velocity > -0.21642522513866425):
																return True
										else:
											if(y_velocity <= -0.22006822377443314):
												if(angle_velocity > -0.0023580207052873448):
													if(angle <= -0.004273940809071064):
														if(angle > -0.014122632332146168):
															return True
													else:
														if(angle_velocity <= 0.015930761583149433):
															if(x_velocity <= -0.0025078682228922844):
																return True
											else:
												if(x_velocity > -0.011793314944952726):
													return True
				else:
					if(y_velocity <= -0.2594956308603287):
						if(x_velocity <= 0.6525615453720093):
							if(lander_x <= 0.02307958621531725):
								if(lander_y <= 1.373055338859558):
									if(y_velocity <= -0.29296332597732544):
										if(x_velocity <= -0.10625281929969788):
											if(y_velocity <= -0.3361341655254364):
												if(angle_velocity > -0.016051679383963346):
													if(lander_y <= 1.3320707082748413):
														if(angle_velocity <= 0.19024396687746048):
															if(lander_x > -0.27865569293498993):
																if(angle_velocity > 0.030084882862865925):
																	if(y_velocity > -0.3564331829547882):
																		if(x_velocity <= -0.14268840849399567):
																			return True
													else:
														if(y_velocity <= -0.46590209007263184):
															return True
														else:
															if(x_velocity > -0.2255719006061554):
																return True
											else:
												if(x_velocity <= -0.11953193694353104):
													if(lander_x <= -0.1192496307194233):
														return True
										else:
											if(x_velocity <= 0.24357302486896515):
												if(angle > -0.2787962257862091):
													if(y_velocity > -0.31527596712112427):
														if(lander_y <= 1.1467329859733582):
															if(angle <= -0.19269920140504837):
																if(angle <= -0.210196815431118):
																	return True
															else:
																if(y_velocity <= -0.3152293413877487):
																	return True
																else:
																	if(angle_velocity > -0.017945660278201103):
																		if(lander_x <= 0.0148178581148386):
																			if(angle <= -0.06394661590456963):
																				if(angle_velocity <= 0.08804255723953247):
																					if(lander_y > 1.0991204977035522):
																						return True
																				else:
																					if(lander_y > 0.8191960752010345):
																						if(angle_velocity > 0.1113610602915287):
																							if(angle > -0.15219192951917648):
																								return True
																			else:
																				if(x_velocity <= -0.07739036530256271):
																					if(x_velocity > -0.07816635444760323):
																						return True
														else:
															if(x_velocity <= -0.03966103307902813):
																if(angle <= -0.020699504762887955):
																	if(y_velocity > -0.3070172220468521):
																		return True
																else:
																	return True
									else:
										if(lander_y <= 0.6716166436672211):
											if(angle <= -0.13102174922823906):
												if(lander_x > -0.3646543025970459):
													return True
											else:
												if(x_velocity <= -0.07650924474000931):
													if(angle_velocity > 0.02510820794850588):
														return True
												else:
													if(angle_velocity > 0.005553795723244548):
														if(angle <= -0.10513648390769958):
															if(x_velocity <= 0.03779068402945995):
																return True
										else:
											if(x_velocity <= -0.023015913553535938):
												if(y_velocity <= -0.2758352607488632):
													if(lander_y <= 0.9605807363986969):
														if(angle <= -0.05462417006492615):
															return True
														else:
															if(angle > -0.043146610260009766):
																if(y_velocity > -0.27999627590179443):
																	if(y_velocity <= -0.2784825712442398):
																		return True
													else:
														if(lander_x <= -0.03730282746255398):
															if(angle > -0.023724621161818504):
																if(x_velocity <= -0.04813620634377003):
																	return True
														else:
															return True
												else:
													if(lander_y > 0.6850554943084717):
														if(lander_y <= 1.0657299160957336):
															if(angle_velocity <= -0.006892556499224156):
																if(lander_x > -0.044910430908203125):
																	return True
															else:
																return True
											else:
												if(angle <= -0.05630537122488022):
													if(x_velocity <= 0.03674690052866936):
														if(y_velocity <= -0.26706530153751373):
															return True
													else:
														if(y_velocity > -0.275630459189415):
															return True
												else:
													if(angle_velocity <= 0.029466263949871063):
														if(angle > 0.008146327221766114):
															if(angle_velocity <= 0.026611480861902237):
																if(y_velocity > -0.2637462913990021):
																	if(y_velocity <= -0.2631078213453293):
																		return True
															else:
																return True
													else:
														if(lander_y > 1.0080597698688507):
															if(angle_velocity <= 0.07091180607676506):
																if(x_velocity <= 0.0017973128706216812):
																	return True
								else:
									if(x_velocity <= -0.05172503925859928):
										if(x_velocity <= -0.05421929992735386):
											if(angle > -0.1460430920124054):
												if(x_velocity <= -0.06594342179596424):
													return True
												else:
													if(y_velocity > -0.32653066515922546):
														return True
							else:
								if(lander_x <= 0.22602467983961105):
									if(x_velocity <= -0.07535390555858612):
										if(y_velocity <= -0.28644469380378723):
											if(lander_y <= 1.0477442741394043):
												if(angle <= -0.11666755005717278):
													if(y_velocity <= -0.31631308794021606):
														if(angle > -0.11735211685299873):
															return True
											else:
												if(y_velocity > -0.3154904693365097):
													return True
										else:
											if(lander_x <= 0.09229903295636177):
												if(angle_velocity <= -0.008074681041762233):
													if(x_velocity <= -0.09963561594486237):
														if(y_velocity > -0.27557606995105743):
															return True
												else:
													if(y_velocity <= -0.27435214817523956):
														if(lander_y <= 0.7805542349815369):
															if(lander_y > 0.596069872379303):
																if(angle <= -0.10737456381320953):
																	return True
														else:
															return True
													else:
														return True
									else:
										if(y_velocity > -0.2709008604288101):
											if(lander_x <= 0.14790429919958115):
												if(angle <= -0.03736453130841255):
													if(angle > -0.03991925157606602):
														return True
												else:
													if(angle_velocity <= -0.01852460578083992):
														if(lander_y > 0.8436659574508667):
															return True
													else:
														if(lander_y <= 1.433857500553131):
															if(y_velocity > -0.26241831481456757):
																if(lander_x <= 0.08574771881103516):
																	if(lander_x > 0.02779297810047865):
																		if(y_velocity <= -0.2608637511730194):
																			if(y_velocity <= -0.26097172498703003):
																				if(lander_x > 0.06775975227355957):
																					return True
																			else:
																				return True
																else:
																	if(angle > -0.0007919874042272568):
																		return True
														else:
															if(y_velocity <= -0.2648572474718094):
																return True
											else:
												return True
								else:
									if(y_velocity > -0.3299812525510788):
										if(x_velocity <= 0.14926587045192719):
											return True
										else:
											if(y_velocity > -0.28549303114414215):
												return True
					else:
						if(x_velocity <= 0.009772160556167364):
							if(y_velocity <= -0.24483375251293182):
								if(lander_y <= 0.6944023370742798):
									if(x_velocity <= -0.04959486611187458):
										if(angle_velocity > -0.004452854162082076):
											if(lander_y <= 0.6500652432441711):
												return True
											else:
												if(lander_x > 0.10824999958276749):
													return True
									else:
										if(angle_velocity > 0.016676543280482292):
											if(angle <= -0.04912423528730869):
												return True
											else:
												if(angle <= 0.013461377006024122):
													if(lander_y > 0.6135468184947968):
														if(angle <= -0.017647644970566034):
															return True
												else:
													return True
								else:
									if(angle_velocity <= -0.011723455041646957):
										if(x_velocity <= -0.053443145006895065):
											return True
										else:
											if(x_velocity > -0.018804423045367002):
												return True
									else:
										if(x_velocity <= 0.006656566169112921):
											if(y_velocity <= -0.24526099860668182):
												if(lander_y <= 0.764032632112503):
													if(angle_velocity > -0.003753315657377243):
														if(y_velocity > -0.2589692771434784):
															return True
												else:
													return True
							else:
								if(angle_velocity > -0.017813351936638355):
									if(angle <= -0.031075498089194298):
										if(lander_x <= 0.04992971383035183):
											if(x_velocity <= -0.01454231794923544):
												if(angle <= -0.04000113159418106):
													return True
												else:
													if(angle_velocity > 0.022110107820481062):
														return True
											else:
												if(y_velocity <= -0.23755423724651337):
													return True
									else:
										if(angle_velocity <= -0.005560303805395961):
											if(angle <= -0.007473527453839779):
												if(y_velocity > -0.22866062074899673):
													return True
											else:
												if(lander_y > 0.49512678384780884):
													return True
										else:
											if(x_velocity <= -0.018309815786778927):
												return True
											else:
												if(lander_x <= 0.08038429915904999):
													if(x_velocity <= -0.01509121898561716):
														if(angle > -4.667416214942932e-05):
															return True
													else:
														return True
												else:
													if(lander_x > 0.10624818876385689):
														return True
						else:
							if(y_velocity <= -0.2244303897023201):
								if(lander_y <= 0.6337423324584961):
									if(angle <= -0.05921509116888046):
										if(y_velocity > -0.24954859167337418):
											return True
									else:
										if(y_velocity > -0.2429022565484047):
											if(x_velocity > 0.01496987696737051):
												if(angle <= 0.02831197716295719):
													if(angle_velocity > 0.04527553729712963):
														if(x_velocity <= 0.1530468538403511):
															if(x_velocity <= 0.0677870661020279):
																if(angle_velocity <= 0.09733923897147179):
																	if(lander_y > 0.596748024225235):
																		if(angle_velocity > 0.06928367167711258):
																			return True
																else:
																	return True
								else:
									if(angle <= 0.13975286483764648):
										if(y_velocity <= -0.249237060546875):
											if(lander_y <= 1.2836709022521973):
												if(angle_velocity <= 0.105367511510849):
													if(angle_velocity <= -0.019210652448236942):
														return True
											else:
												if(x_velocity <= 0.1511201709508896):
													return True
										else:
											if(lander_y <= 0.926637202501297):
												if(angle <= 0.012374273966997862):
													if(x_velocity <= 0.07312560081481934):
														return True
													else:
														if(lander_y <= 0.6474784016609192):
															return True
												else:
													if(y_velocity > -0.23654136061668396):
														if(x_velocity <= 0.09398551657795906):
															if(angle <= 0.05475660040974617):
																return True
											else:
												if(lander_y <= 1.3702694177627563):
													if(y_velocity > -0.24629773199558258):
														if(angle_velocity <= -0.012375698890537024):
															if(x_velocity <= 0.07926076650619507):
																if(y_velocity <= -0.2296822965145111):
																	return True
														else:
															if(y_velocity <= -0.24415922909975052):
																if(x_velocity <= 0.08026551268994808):
																	return True
															else:
																return True
												else:
													if(angle_velocity <= 0.12907720357179642):
														if(angle_velocity <= 0.01062967290636152):
															return True
													else:
														if(x_velocity > 0.1977105289697647):
															return True
									else:
										if(angle > 0.46861210465431213):
											return True
							else:
								if(angle_velocity <= 0.05199507810175419):
									if(angle_velocity <= 0.034516019746661186):
										if(angle <= 0.0669519193470478):
											if(x_velocity <= 0.06815199181437492):
												return True
										else:
											if(x_velocity <= 0.25485916435718536):
												return True
									else:
										if(lander_x <= -0.01775689097121358):
											if(x_velocity <= 0.061260635033249855):
												return True
								else:
									if(x_velocity <= 0.25101426988840103):
										if(lander_y <= 0.5400468111038208):
											if(x_velocity <= 0.11229487136006355):
												if(lander_y > 0.4670831710100174):
													return True
											else:
												if(angle > -0.05024145543575287):
													if(lander_y <= 0.45589679479599):
														return True
										else:
											if(angle_velocity <= 0.24486032128334045):
												if(angle <= -0.043392933905124664):
													if(lander_x <= -0.2998668700456619):
														return True
												else:
													return True
		else:
			if(y_velocity <= -0.04625159688293934):
				if(angle_velocity <= -0.020012114197015762):
					if(x_velocity <= -0.062468184158205986):
						if(lander_y <= 1.470240831375122):
							if(x_velocity <= -0.217918299138546):
								return True
							else:
								if(lander_x > -0.012781954137608409):
									if(angle <= -0.017480780370533466):
										if(angle_velocity <= -0.040706194937229156):
											if(angle_velocity <= -0.07470352947711945):
												return True
										else:
											return True
									else:
										return True
					else:
						if(angle <= 0.004466760903596878):
							if(lander_y <= 1.4811075925827026):
								if(angle_velocity <= -0.03305315971374512):
									if(y_velocity <= -0.08007068186998367):
										if(y_velocity <= -0.21059369295835495):
											if(angle_velocity > -0.051847146824002266):
												return True
								else:
									if(x_velocity <= -0.025241411291062832):
										return True
									else:
										if(lander_y > 0.07490148209035397):
											if(angle_velocity <= -0.03234349191188812):
												return True
						else:
							if(y_velocity <= -0.19456586986780167):
								if(lander_y <= 0.3112007826566696):
									if(angle_velocity <= -0.03830353356897831):
										if(angle <= 0.010316614527255297):
											return True
									else:
										if(x_velocity <= -0.04011731967329979):
											return True
										else:
											if(x_velocity <= 0.10860027000308037):
												if(angle <= 0.02127546537667513):
													if(angle > 0.014985323883593082):
														if(lander_x > -0.048516225069761276):
															if(angle_velocity > -0.03418443538248539):
																return True
								else:
									if(lander_y <= 0.3769782781600952):
										if(lander_x > -0.007061862852424383):
											return True
									else:
										if(x_velocity <= 0.19233880192041397):
											if(angle_velocity > -0.1404288038611412):
												if(lander_x <= -0.23554258048534393):
													if(angle <= 0.014951597433537245):
														return True
												else:
													if(lander_y > 0.43535158038139343):
														return True
							else:
								if(lander_x <= 0.09790630266070366):
									if(angle_velocity <= -0.04235716536641121):
										if(lander_y > 0.27968253195285797):
											if(x_velocity <= 0.06659107282757759):
												if(angle_velocity <= -0.061794960871338844):
													if(y_velocity > -0.1837133765220642):
														return True
												else:
													return True
									else:
										if(y_velocity <= -0.16684778034687042):
											if(x_velocity <= 0.0077046051155775785):
												return True
											else:
												if(angle <= 0.06907186284661293):
													if(lander_x <= -0.07053551450371742):
														if(x_velocity <= 0.057628123089671135):
															return True
														else:
															if(angle > 0.03962137922644615):
																return True
													else:
														if(angle_velocity <= -0.03958926163613796):
															return True
														else:
															if(x_velocity <= 0.020452387165278196):
																if(lander_y <= 0.05385594069957733):
																	return True
										else:
											return True
								else:
									if(x_velocity <= 0.2305583357810974):
										if(y_velocity <= -0.1862800344824791):
											if(y_velocity <= -0.18919487297534943):
												return True
										else:
											return True
				else:
					if(y_velocity <= -0.18436022847890854):
						if(x_velocity <= -0.0069253817200660706):
							if(lander_y <= 0.0211697556078434):
								if(lander_y <= 0.01586259389296174):
									if(angle_velocity <= 0.20008431375026703):
										return True
							else:
								if(lander_x <= 0.11992516368627548):
									if(angle <= -0.03051120787858963):
										if(x_velocity <= -0.0323156900703907):
											if(lander_x <= -0.025156640447676182):
												if(lander_x <= -0.02635092753916979):
													return True
											else:
												return True
										else:
											if(angle_velocity > 0.017021882347762585):
												return True
									else:
										if(y_velocity <= -0.21088775247335434):
											if(y_velocity <= -0.21097326278686523):
												return True
										else:
											if(x_velocity <= -0.011651167646050453):
												return True
											else:
												if(x_velocity > -0.01106531172990799):
													return True
						else:
							if(lander_x <= -0.042762136086821556):
								if(y_velocity <= -0.20255107432603836):
									if(lander_y <= 0.4827624410390854):
										if(x_velocity <= 0.051810845732688904):
											if(lander_y <= 0.15091170370578766):
												if(angle_velocity > -0.013167968951165676):
													if(angle <= -0.023265200667083263):
														return True
													else:
														if(y_velocity <= -0.20862088352441788):
															if(angle_velocity > 0.001374891260638833):
																if(angle > -0.0063715053256601095):
																	return True
											else:
												if(y_velocity <= -0.20258718729019165):
													return True
										else:
											if(angle > -0.009217553306370974):
												if(angle_velocity > -0.012879056856036186):
													if(lander_x <= -0.11576604470610619):
														if(y_velocity > -0.20508630573749542):
															if(y_velocity <= -0.2043422982096672):
																if(angle <= 0.04920308105647564):
																	return True
													else:
														if(x_velocity <= 0.059141192585229874):
															return True
									else:
										if(angle_velocity <= 0.017661770689301193):
											if(x_velocity <= 0.0928075909614563):
												return True
										else:
											return True
								else:
									if(lander_y <= 0.3891821354627609):
										if(x_velocity <= 0.07820967957377434):
											if(lander_y > 0.0024011230270843953):
												if(angle_velocity <= -0.0004889809933956712):
													if(x_velocity <= 0.05140134133398533):
														if(lander_y <= 0.08781356364488602):
															if(angle_velocity <= -0.01603021938353777):
																return True
														else:
															if(x_velocity <= 0.03584926202893257):
																return True
															else:
																if(angle <= 0.0028147652046754956):
																	if(lander_x <= -0.20212462544441223):
																		if(y_velocity > -0.19196707010269165):
																			return True
																else:
																	return True
													else:
														if(y_velocity > -0.20081204921007156):
															if(angle_velocity > -0.0030889732879586518):
																if(y_velocity <= -0.1959468051791191):
																	return True
												else:
													if(y_velocity <= -0.18582746386528015):
														if(lander_x <= -0.05756807327270508):
															if(lander_y <= 0.06238576024770737):
																if(lander_y <= 0.05784710496664047):
																	return True
															else:
																return True
														else:
															if(lander_x > -0.056616783142089844):
																return True
													else:
														if(lander_x <= -0.1992006078362465):
															return True
										else:
											if(lander_x <= -0.2274240478873253):
												if(x_velocity <= 0.11409883201122284):
													return True
												else:
													if(x_velocity > 0.1454349085688591):
														return True
									else:
										if(x_velocity <= 0.13976705819368362):
											return True
										else:
											if(angle_velocity > 0.0705386446788907):
												return True
							else:
								if(angle <= 0.03075925912708044):
									if(lander_y <= 0.23827283084392548):
										if(angle_velocity <= 0.005395429907366633):
											if(lander_y <= 0.051877399906516075):
												if(y_velocity > -0.19031043350696564):
													return True
										else:
											if(angle_velocity <= 0.11614060401916504):
												if(y_velocity <= -0.18809842318296432):
													if(angle_velocity > 0.04781189560890198):
														if(lander_y <= 0.12213743850588799):
															return True
											else:
												if(x_velocity <= 0.06585400551557541):
													return True
									else:
										if(x_velocity <= 0.038285283371806145):
											if(angle_velocity <= 0.035340841859579086):
												if(x_velocity <= 0.004353738273493946):
													return True
											else:
												return True
								else:
									if(lander_y <= 0.2757747322320938):
										if(y_velocity > -0.18958498537540436):
											if(lander_y <= 0.11388849839568138):
												return True
											else:
												if(lander_y > 0.15782561898231506):
													if(angle_velocity > 0.016652418300509453):
														return True
									else:
										if(x_velocity <= 0.2683706134557724):
											if(lander_x > 0.03540916554629803):
												if(lander_y <= 0.4122486710548401):
													if(y_velocity > -0.19863538444042206):
														if(angle_velocity > 0.005234683980233967):
															return True
												else:
													if(lander_x <= 0.13416848331689835):
														if(lander_y <= 1.480635404586792):
															return True
					else:
						if(x_velocity <= 0.3691508024930954):
							if(lander_y <= -0.001645400479901582):
								if(lander_y <= -0.006369378650560975):
									return True
							else:
								if(x_velocity <= 0.04088269919157028):
									if(y_velocity <= -0.18427950888872147):
										if(lander_x <= -0.04821448400616646):
											return True
									else:
										if(lander_y <= 0.020615647546947002):
											if(x_velocity <= 0.02952624950557947):
												return True
										else:
											return True
								else:
									if(lander_y <= 0.11264903098344803):
										if(angle_velocity <= 0.004053640004713088):
											if(lander_x <= -0.2499690279364586):
												return True
										else:
											if(y_velocity <= -0.16221347451210022):
												if(angle <= 0.03342198394238949):
													if(angle_velocity > 0.04894179664552212):
														return True
											else:
												return True
									else:
										if(y_velocity <= -0.1415981501340866):
											if(angle_velocity <= 0.010637735482305288):
												if(lander_x <= -0.10494113247841597):
													return True
												else:
													if(angle > 0.0517528411000967):
														if(angle_velocity <= 0.009012272581458092):
															return True
											else:
												if(y_velocity > -0.18348319083452225):
													if(lander_y <= 0.41426412761211395):
														return True
													else:
														if(lander_y > 0.4249081611633301):
															if(angle <= 0.02259056642651558):
																if(lander_y <= 0.9383572489023209):
																	return True
															else:
																if(y_velocity <= -0.1785217523574829):
																	if(lander_y <= 0.9679950177669525):
																		return True
																else:
																	if(lander_y <= 1.4533974528312683):
																		return True
																	else:
																		if(lander_y > 1.4590007066726685):
																			return True
										else:
											if(angle_velocity > 0.14730069041252136):
												if(angle_velocity <= 0.1730458214879036):
													if(lander_x <= 0.04646463505923748):
														return True
												else:
													return True
						else:
							if(y_velocity > -0.1733998954296112):
								if(lander_x > 0.06330790743231773):
									if(x_velocity <= 0.37721721827983856):
										return True
									else:
										if(y_velocity <= -0.15873125195503235):
											return True
			else:
				if(x_velocity <= 0.174779012799263):
					if(x_velocity <= -0.2148854210972786):
						return True
					else:
						if(lander_x <= 0.021488094702363014):
							if(angle_velocity <= 0.014317034743726254):
								if(angle <= 0.006493317196145654):
									if(y_velocity <= 0.013756581582129002):
										if(y_velocity > -0.0018054824322462082):
											return True
								else:
									return True
							else:
								return True
				else:
					if(angle > 0.00974681880325079):
						if(x_velocity <= 0.37852008640766144):
							if(y_velocity <= 0.015188325196504593):
								if(lander_y > 1.470399022102356):
									return True
	else:
		if(angle_velocity > -0.6027695834636688):
			if(angle_velocity > 0.4368469715118408):
				if(y_velocity <= -0.12551017105579376):
					return True
				else:
					if(y_velocity > -0.111349917948246):
						return True
	return False

