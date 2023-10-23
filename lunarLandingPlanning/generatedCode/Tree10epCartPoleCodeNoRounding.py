def predict(observation):
	action = 0
	cart_position= observation[0]
	cart_velocity= observation[1]
	pole_angle= observation[2]
	pole_angular_velocity= observation[3]

	if weShould_move_left(cart_position, cart_velocity, pole_angle, pole_angular_velocity):
		action = 0
	if weShould_move_right(cart_position, cart_velocity, pole_angle, pole_angular_velocity):
		action = 1

	return action
def weShould_move_left(cart_position, cart_velocity, pole_angle, pole_angular_velocity):
	if(pole_angular_velocity <= -0.003253065049648285):
		if(pole_angular_velocity <= -0.11360538005828857):
			if(pole_angular_velocity <= -0.1374693512916565):
				if(pole_angle <= 0.03329905681312084):
					if(pole_angle <= 0.019715409725904465):
						if(pole_angular_velocity <= -0.14653046429157257):
							if(pole_angle <= 0.009452462196350098):
								return True
							else:
								if(cart_position <= 0.07428273558616638):
									if(pole_angle > 0.00945691904053092):
										if(cart_position <= 0.03926258906722069):
											if(pole_angular_velocity <= -0.15556253492832184):
												if(cart_position <= 0.021309946663677692):
													return True
												else:
													if(cart_position > 0.02163386158645153):
														return True
											else:
												if(pole_angular_velocity > -0.15500760823488235):
													return True
										else:
											if(cart_position <= 0.04036247916519642):
												if(pole_angular_velocity <= -0.20706115663051605):
													return True
											else:
												if(pole_angular_velocity <= -0.20100148767232895):
													return True
												else:
													if(pole_angular_velocity > -0.1999046355485916):
														if(cart_velocity <= 0.2020500972867012):
															return True
														else:
															if(cart_velocity > 0.20310497283935547):
																return True
						else:
							if(pole_angular_velocity > -0.1464993953704834):
								if(cart_position <= 0.15131103247404099):
									if(cart_velocity <= 0.21168674528598785):
										if(pole_angular_velocity <= -0.13848137855529785):
											return True
										else:
											if(pole_angular_velocity > -0.13844990730285645):
												return True
									else:
										if(cart_velocity > 0.2117849364876747):
											return True
								else:
									if(pole_angle <= -0.00297674658941105):
										return True
					else:
						if(pole_angular_velocity <= -0.21702878922224045):
							if(cart_position <= 0.01409118203446269):
								return True
							else:
								if(cart_position > 0.014398430939763784):
									if(pole_angular_velocity <= -0.24181733280420303):
										return True
									else:
										if(pole_angular_velocity > -0.23762138932943344):
											return True
						else:
							if(cart_position <= -0.00821502460166812):
								if(cart_velocity <= 0.22107648104429245):
									if(cart_velocity <= 0.20660416036844254):
										if(pole_angle <= 0.02949636150151491):
											return True
										else:
											if(pole_angle > 0.029754151590168476):
												return True
									else:
										if(cart_velocity > 0.21383391320705414):
											return True
							else:
								if(pole_angular_velocity <= -0.1683526635169983):
									if(cart_position <= 0.03146131616085768):
										if(pole_angular_velocity > -0.21594837307929993):
											return True
									else:
										if(pole_angular_velocity <= -0.21366138011217117):
											return True
										else:
											if(pole_angle > 0.03008658904582262):
												return True
								else:
									if(cart_position <= -0.00214935012627393):
										if(pole_angular_velocity <= -0.15054918825626373):
											return True
				else:
					if(cart_velocity <= 0.1809116005897522):
						if(pole_angular_velocity <= -0.20748944580554962):
							return True
					else:
						if(pole_angular_velocity <= -0.27239927649497986):
							if(pole_angular_velocity <= -0.29517465829849243):
								return True
							else:
								if(pole_angle <= 0.040613604709506035):
									if(cart_velocity <= 0.2402428686618805):
										return True
									else:
										if(pole_angle > 0.03663402795791626):
											return True
						else:
							if(cart_position <= -0.022344418801367283):
								if(cart_velocity <= 0.20063341408967972):
									return True
			else:
				if(pole_angle <= 0.001906043034978211):
					if(cart_velocity <= 0.19710254669189453):
						if(pole_angle <= 0.0009986476507037878):
							return True
						else:
							if(cart_velocity <= 0.17052625864744186):
								return True
							else:
								if(pole_angle > 0.001396112667862326):
									return True
					else:
						if(cart_velocity > 0.19712293148040771):
							return True
				else:
					if(cart_position <= 0.07183830440044403):
						if(pole_angular_velocity <= -0.11723022907972336):
							if(cart_position <= 0.0405742172151804):
								if(pole_angle <= 0.021216497756540775):
									if(cart_velocity <= 0.16247688978910446):
										return True
									else:
										if(cart_velocity > 0.16281072795391083):
											if(pole_angle <= 0.01040760986506939):
												return True
											else:
												if(cart_position <= -0.0009533283300697803):
													return True
								else:
									if(cart_position <= -0.03331857454031706):
										if(pole_angular_velocity <= -0.12031572684645653):
											return True
							else:
								if(cart_velocity <= 0.17861702293157578):
									if(pole_angle <= 0.007500296691432595):
										return True
									else:
										if(cart_position <= 0.0548661220818758):
											if(pole_angular_velocity > -0.1354467123746872):
												return True
						else:
							if(cart_velocity <= 0.1670742779970169):
								if(pole_angle <= 0.0185689153149724):
									return True
								else:
									if(cart_velocity <= 0.1490742340683937):
										return True
					else:
						if(pole_angle <= 0.002420681295916438):
							if(cart_velocity <= 0.1630207970738411):
								if(pole_angular_velocity <= -0.12130266800522804):
									if(pole_angle > 0.0019266984309069812):
										if(cart_velocity <= 0.1500326320528984):
											return True
										else:
											if(cart_velocity > 0.15171755850315094):
												return True
								else:
									if(pole_angle <= 0.002048622351139784):
										return True
						else:
							if(cart_position <= 0.10468507930636406):
								if(pole_angle <= 0.005031617358326912):
									if(cart_position <= 0.08732271194458008):
										return True
									else:
										if(cart_velocity <= 0.14664074778556824):
											return True
										else:
											if(pole_angular_velocity <= -0.12409807741641998):
												if(cart_position > 0.09291469305753708):
													return True
							else:
								if(cart_velocity <= 0.13939200341701508):
									if(pole_angular_velocity <= -0.11515993624925613):
										return True
		else:
			if(pole_angle <= 0.0010587017750367522):
				if(pole_angle <= 0.00028330853092484176):
					if(cart_position <= 0.11699293926358223):
						if(pole_angle <= -0.0008639824518468231):
							if(pole_angle <= -0.0020343047799542546):
								if(pole_angular_velocity <= -0.006532130762934685):
									if(cart_position <= 0.0036839224630966783):
										if(cart_position <= 0.0031606891425326467):
											return True
									else:
										if(pole_angular_velocity <= -0.011174938175827265):
											return True
										else:
											if(pole_angular_velocity > -0.011150849517434835):
												return True
								else:
									if(cart_velocity <= 0.04787500575184822):
										if(cart_velocity <= 0.03879775293171406):
											return True
										else:
											if(cart_position <= 0.10023770108819008):
												if(pole_angle <= -0.0022824308834969997):
													if(pole_angle <= -0.0029028335120528936):
														return True
													else:
														if(cart_position <= 0.0897638313472271):
															return True
												else:
													if(pole_angle > -0.0021750604500994086):
														return True
											else:
												if(cart_velocity > 0.046655233949422836):
													return True
									else:
										if(pole_angle <= -0.006712969159707427):
											return True
							else:
								if(pole_angle > -0.002028372255153954):
									if(cart_velocity <= 0.036504264920949936):
										return True
									else:
										if(pole_angular_velocity <= -0.01829157117754221):
											if(cart_position <= 0.04275096394121647):
												if(pole_angular_velocity <= -0.056223390623927116):
													if(pole_angle <= -0.001235230709426105):
														return True
													else:
														if(pole_angle > -0.0011931427288800478):
															return True
												else:
													if(cart_position <= 0.009685919503681362):
														return True
											else:
												if(cart_position <= 0.060609398409724236):
													if(cart_position <= 0.05896143428981304):
														return True
												else:
													return True
										else:
											if(cart_position <= 0.09587016329169273):
												if(pole_angular_velocity <= -0.007100757444277406):
													return True
												else:
													if(cart_position <= 0.0814383365213871):
														return True
													else:
														if(pole_angle <= -0.0016774393734522164):
															if(cart_position <= 0.08802899345755577):
																return True
						else:
							if(pole_angular_velocity <= -0.03082387987524271):
								if(cart_position <= 0.07184406742453575):
									if(pole_angular_velocity <= -0.09056921303272247):
										return True
									else:
										if(cart_position <= 0.004645733395591378):
											return True
										else:
											if(pole_angle <= -0.0004377610021037981):
												if(pole_angular_velocity <= -0.07080717384815216):
													if(pole_angle <= -0.0008288942917715758):
														if(pole_angular_velocity <= -0.0801316499710083):
															return True
													else:
														return True
												else:
													if(cart_position <= 0.0316010182723403):
														return True
											else:
												if(cart_position <= 0.05625593289732933):
													if(cart_velocity <= 0.14541491866111755):
														if(pole_angular_velocity <= -0.03654707223176956):
															return True
													else:
														if(pole_angular_velocity <= -0.08143047988414764):
															return True
								else:
									return True
							else:
								if(cart_velocity <= 0.02361580077558756):
									if(pole_angular_velocity <= -0.0033567686332389712):
										if(pole_angle > -0.0008618126448709518):
											if(pole_angle <= 0.000277430604910478):
												if(cart_velocity <= 0.019291618838906288):
													return True
												else:
													if(cart_velocity > 0.019374269992113113):
														if(pole_angle <= -0.00017993537039728835):
															return True
														else:
															if(pole_angle > 2.8640497475862503e-05):
																return True
								else:
									if(cart_position <= 0.08625803142786026):
										if(cart_velocity <= 0.04259863682091236):
											if(pole_angle > -0.0007233383075799793):
												if(pole_angle <= -1.716434780973941e-06):
													return True
												else:
													if(pole_angle > 0.00012540707029984333):
														return True
										else:
											if(cart_position > 0.07582515105605125):
												return True
									else:
										if(pole_angle <= -0.0003850711364066228):
											if(cart_velocity <= 0.026718911714851856):
												if(cart_position <= 0.1151961125433445):
													return True
											else:
												if(pole_angular_velocity <= -0.022613422945141792):
													if(cart_velocity <= 0.04706503078341484):
														return True
												else:
													if(cart_velocity <= 0.03990238532423973):
														if(cart_position <= 0.10294193401932716):
															if(pole_angular_velocity <= -0.005820682737976313):
																return True
														else:
															if(pole_angular_velocity <= -0.016403150744736195):
																if(pole_angular_velocity > -0.01673055626451969):
																	return True
										else:
											if(pole_angular_velocity <= -0.02143980748951435):
												if(cart_velocity <= 0.03735995292663574):
													if(cart_position <= 0.1152140386402607):
														return True
													else:
														if(pole_angle > 0.00017101666162488982):
															return True
												else:
													if(cart_position <= 0.10122410580515862):
														return True
											else:
												if(pole_angular_velocity > -0.005723543232306838):
													if(cart_position <= 0.09372953698039055):
														return True
					else:
						if(cart_position <= 0.12571095675230026):
							if(pole_angle <= -3.079258021898568e-05):
								if(cart_position <= 0.1257021278142929):
									if(pole_angle <= -0.001808693166822195):
										if(pole_angle <= -0.0022129229037091136):
											return True
										else:
											if(pole_angle > -0.002183470642194152):
												return True
									else:
										if(pole_angle > -0.001805670268367976):
											if(pole_angular_velocity <= -0.012334023136645555):
												if(cart_velocity <= 0.03678189590573311):
													return True
												else:
													if(pole_angular_velocity <= -0.02482064813375473):
														if(cart_velocity > 0.0370041448622942):
															return True
											else:
												if(cart_velocity <= 0.016742659732699394):
													if(cart_velocity <= 0.00864768959581852):
														return True
													else:
														if(pole_angular_velocity <= -0.006093936040997505):
															return True
														else:
															if(cart_position <= 0.11838433519005775):
																return True
							else:
								if(pole_angle > -2.393804879829986e-05):
									if(cart_position <= 0.1239265725016594):
										if(cart_position <= 0.12334883585572243):
											if(cart_velocity <= 0.04590592347085476):
												if(pole_angle <= 0.00023749886167934164):
													if(cart_position <= 0.122514259070158):
														return True
													else:
														if(pole_angle > 7.291016845556442e-05):
															return True
									else:
										if(pole_angular_velocity <= -0.006434087408706546):
											return True
						else:
							if(cart_velocity <= -0.01584121398627758):
								if(cart_position <= 0.15188637375831604):
									return True
							else:
								if(cart_position <= 0.1705847904086113):
									if(pole_angle <= -8.409176371060312e-05):
										return True
									else:
										if(pole_angular_velocity <= -0.013556430116295815):
											if(cart_velocity <= 0.007086407858878374):
												if(pole_angular_velocity > -0.020445645786821842):
													return True
											else:
												return True
										else:
											if(cart_velocity <= 0.009134095162153244):
												return True
								else:
									if(cart_position > 0.1719667762517929):
										return True
				else:
					if(pole_angular_velocity <= -0.031777963042259216):
						if(cart_position <= 0.12451418489217758):
							if(pole_angular_velocity <= -0.039029402658343315):
								if(pole_angle <= 0.0010245335288345814):
									if(cart_velocity <= 0.1424916386604309):
										return True
									else:
										if(pole_angular_velocity <= -0.09617031738162041):
											if(pole_angular_velocity <= -0.11086485534906387):
												if(pole_angular_velocity <= -0.11194831505417824):
													return True
											else:
												return True
										else:
											if(cart_position <= 0.04341410659253597):
												if(cart_velocity <= 0.17761648446321487):
													if(pole_angular_velocity <= -0.06431064568459988):
														return True
													else:
														if(cart_position <= 0.010899695567786694):
															return True
											else:
												if(pole_angle <= 0.0005269646790111437):
													return True
							else:
								if(cart_velocity <= 0.03996875509619713):
									return True
								else:
									if(pole_angle <= 0.0005572026711888611):
										if(cart_velocity <= 0.04397708922624588):
											return True
										else:
											if(cart_position <= 0.11323864385485649):
												return True
									else:
										if(cart_position <= -0.013533934019505978):
											return True
										else:
											if(pole_angle <= 0.0007179754611570388):
												if(pole_angle > 0.0007157815853133798):
													return True
						else:
							if(cart_position <= 0.13300737738609314):
								if(cart_position <= 0.1329376995563507):
									if(cart_velocity <= 0.04624463431537151):
										if(cart_velocity <= 0.03754439949989319):
											return True
										else:
											if(pole_angular_velocity <= -0.03795726038515568):
												return True
									else:
										if(pole_angular_velocity <= -0.046353939920663834):
											return True
										else:
											if(pole_angle <= 0.0006077363068470731):
												return True
								else:
									if(pole_angle > 0.0009926754282787442):
										return True
							else:
								if(pole_angular_velocity <= -0.050672490149736404):
									return True
								else:
									if(cart_velocity <= 0.042309973388910294):
										if(cart_position <= 0.14716343581676483):
											return True
										else:
											if(cart_position > 0.14740652590990067):
												if(cart_velocity <= 0.021358408499509096):
													return True
												else:
													if(cart_position <= 0.14848751574754715):
														return True
									else:
										if(cart_position <= 0.1351407766342163):
											return True
										else:
											if(cart_velocity <= 0.043236855417490005):
												if(pole_angle > 0.0007050672429613769):
													return True
					else:
						if(cart_velocity <= 0.02771636750549078):
							if(pole_angular_velocity <= -0.02159358188509941):
								if(pole_angle <= 0.0005839763034600765):
									return True
								else:
									if(cart_velocity <= 0.015254498925060034):
										return True
									else:
										if(pole_angular_velocity <= -0.02345014363527298):
											if(cart_velocity <= 0.022680464200675488):
												if(pole_angle <= 0.001002555014565587):
													if(cart_position <= 0.13506783545017242):
														if(pole_angular_velocity <= -0.025470488704741):
															return True
														else:
															if(pole_angular_velocity > -0.02531762793660164):
																if(pole_angular_velocity <= -0.024402308277785778):
																	return True
																else:
																	if(pole_angular_velocity > -0.02407448459416628):
																		return True
												else:
													if(cart_velocity <= 0.016202304046601057):
														return True
													else:
														if(pole_angular_velocity <= -0.028582130558788776):
															return True
											else:
												if(pole_angular_velocity <= -0.03055317886173725):
													if(cart_position <= 0.13425768911838531):
														return True
												else:
													if(cart_position <= 0.12535690516233444):
														if(pole_angular_velocity <= -0.02671567164361477):
															return True
														else:
															if(cart_velocity <= 0.023629698902368546):
																return True
													else:
														if(pole_angular_velocity <= -0.029805298894643784):
															if(pole_angle > 0.0007733646198175848):
																return True
										else:
											if(cart_position <= 0.1193164549767971):
												return True
											else:
												if(cart_velocity <= 0.017730732448399067):
													if(cart_velocity > 0.015332821756601334):
														return True
							else:
								if(pole_angular_velocity <= -0.007243790663778782):
									if(pole_angular_velocity <= -0.014512476045638323):
										if(cart_velocity <= 0.01209763390943408):
											if(cart_velocity <= 0.010027748998254538):
												if(pole_angle <= 0.0010388982482254505):
													if(pole_angle <= 0.0009361956617794931):
														return True
													else:
														if(pole_angular_velocity <= -0.015814324840903282):
															return True
											else:
												if(pole_angular_velocity <= -0.017865844070911407):
													return True
												else:
													if(pole_angle <= 0.0006963309133425355):
														if(cart_position <= 0.13111358880996704):
															if(pole_angular_velocity <= -0.015629718080163002):
																return True
										else:
											if(pole_angle <= 0.00045288850378710777):
												if(cart_velocity <= 0.018499057739973068):
													if(pole_angular_velocity <= -0.016534808091819286):
														return True
											else:
												if(pole_angular_velocity <= -0.014814999420195818):
													if(cart_velocity <= 0.013256147969514132):
														if(cart_velocity > 0.013047343585640192):
															return True
													else:
														if(pole_angle <= 0.0006327963201329112):
															if(pole_angle <= 0.0006123381026554853):
																if(pole_angular_velocity <= -0.01993493363261223):
																	if(cart_position <= 0.12620404362678528):
																		return True
															else:
																return True
												else:
													return True
									else:
										if(cart_velocity <= 0.006650689523667097):
											if(pole_angle <= 0.0009159583132714033):
												if(cart_velocity <= 0.006429050350561738):
													return True
												else:
													if(cart_velocity > 0.006539475172758102):
														return True
											else:
												if(cart_position <= 0.1255113184452057):
													return True
										else:
											if(pole_angle <= 0.0010550384176895022):
												if(cart_position <= 0.1018655002117157):
													return True
												else:
													if(pole_angle <= 0.0004623425775207579):
														if(pole_angle <= 0.0004483100346988067):
															if(cart_position <= 0.10767792910337448):
																return True
															else:
																if(cart_velocity <= 0.010546080768108368):
																	if(cart_position <= 0.1256466545164585):
																		return True
														else:
															return True
													else:
														if(pole_angular_velocity <= -0.013249754440039396):
															if(pole_angular_velocity > -0.01359120151028037):
																if(cart_position > 0.12375534698367119):
																	return True
											else:
												return True
								else:
									if(pole_angle <= 0.0008134859381243587):
										return True
									else:
										if(pole_angle > 0.0008408271824009717):
											if(pole_angular_velocity <= -0.003932083607651293):
												return True
											else:
												if(cart_velocity <= 0.006866135518066585):
													return True
						else:
							if(cart_position <= 0.07523545622825623):
								if(pole_angular_velocity <= -0.008507114020176232):
									return True
							else:
								if(pole_angular_velocity <= -0.029138077050447464):
									if(cart_velocity <= 0.040017081424593925):
										if(cart_position <= 0.12297991290688515):
											if(pole_angular_velocity <= -0.029831531457602978):
												return True
											else:
												if(pole_angle <= 0.00043193751480430365):
													return True
								else:
									if(cart_velocity <= 0.02961812261492014):
										if(cart_velocity > 0.029216542840003967):
											return True
			else:
				if(pole_angle <= 0.0024281212827190757):
					if(pole_angular_velocity <= -0.050080012530088425):
						if(cart_velocity <= 0.13732516020536423):
							if(pole_angular_velocity <= -0.051607755944132805):
								if(pole_angular_velocity <= -0.053916897624731064):
									if(pole_angle <= 0.002379203448072076):
										if(pole_angle <= 0.0022054025903344154):
											return True
										else:
											if(pole_angle > 0.002213880652561784):
												return True
									else:
										if(pole_angle > 0.0023808492114767432):
											if(pole_angular_velocity <= -0.05906503275036812):
												if(cart_position <= 0.14316442608833313):
													if(pole_angular_velocity <= -0.06577883660793304):
														return True
												else:
													return True
											else:
												if(pole_angle > 0.0023926168214529753):
													return True
								else:
									if(pole_angular_velocity <= -0.05365218035876751):
										if(pole_angle <= 0.0018802674603648484):
											if(pole_angle > 0.0011869410518556833):
												return True
										else:
											if(cart_velocity > 0.04175596497952938):
												return True
									else:
										if(cart_velocity <= 0.04190853238105774):
											return True
										else:
											if(cart_position <= 0.13863058388233185):
												if(cart_velocity <= 0.048617949709296227):
													return True
												else:
													if(cart_velocity > 0.049035532400012016):
														return True
							else:
								if(cart_velocity <= 0.04178890772163868):
									if(cart_position <= 0.1467474400997162):
										if(cart_velocity <= 0.038514144718647):
											return True
										else:
											if(cart_velocity > 0.03852866403758526):
												return True
								else:
									if(pole_angle <= 0.001532728027086705):
										if(cart_velocity <= 0.04745253548026085):
											return True
									else:
										if(cart_position <= 0.12371334433555603):
											return True
										else:
											if(pole_angle > 0.0021041654981672764):
												if(pole_angular_velocity <= -0.05110757425427437):
													return True
						else:
							if(cart_position <= 0.029304079711437225):
								if(pole_angular_velocity <= -0.061210693791508675):
									if(pole_angle <= 0.0022235206561163068):
										return True
									else:
										if(cart_position <= 0.0066423727257642895):
											return True
								else:
									if(cart_position <= -0.007602499215863645):
										return True
							else:
								if(pole_angular_velocity <= -0.11121008917689323):
									return True
								else:
									if(pole_angular_velocity <= -0.0871274396777153):
										if(cart_position <= 0.04764518886804581):
											if(cart_velocity <= 0.17396289855241776):
												return True
										else:
											if(cart_velocity <= 0.1383267492055893):
												if(cart_velocity > 0.1379592940211296):
													return True
											else:
												if(pole_angular_velocity <= -0.10701700672507286):
													if(pole_angular_velocity <= -0.10880199819803238):
														if(cart_velocity <= 0.14686476439237595):
															if(pole_angle <= 0.0019934694282710552):
																return True
													else:
														return True
												else:
													if(cart_position <= 0.05699081905186176):
														if(cart_position > 0.052939653396606445):
															return True
									else:
										if(cart_velocity <= 0.142138309776783):
											if(pole_angle <= 0.0014141781721264124):
												return True
					else:
						if(pole_angular_velocity <= -0.029371706768870354):
							if(pole_angle <= 0.0018742188112810254):
								if(cart_velocity <= 0.0330341961234808):
									if(pole_angular_velocity <= -0.03661579638719559):
										if(cart_velocity <= 0.02696643676608801):
											return True
										else:
											if(pole_angular_velocity <= -0.04075665399432182):
												if(pole_angle <= 0.001820835575927049):
													if(cart_position <= 0.14047791063785553):
														if(cart_velocity <= 0.032495055347681046):
															return True
														else:
															if(pole_angle <= 0.0014823063975200057):
																return True
													else:
														if(pole_angle <= 0.001307112688664347):
															return True
												else:
													if(cart_position <= 0.13771459460258484):
														return True
											else:
												if(cart_position <= 0.1351313367486):
													if(cart_velocity <= 0.03166244737803936):
														if(cart_velocity <= 0.030507685616612434):
															return True
														else:
															if(pole_angular_velocity <= -0.03760397061705589):
																return True
												else:
													if(pole_angle <= 0.0014137740363366902):
														if(cart_velocity <= 0.029173417948186398):
															return True
													else:
														if(pole_angular_velocity <= -0.04043135046958923):
															if(pole_angular_velocity > -0.040589589625597):
																return True
									else:
										if(cart_position <= 0.13549768179655075):
											if(cart_velocity <= 0.023564227856695652):
												if(pole_angle <= 0.0017256209393963218):
													if(pole_angular_velocity <= -0.02977080922573805):
														if(pole_angle <= 0.0016492268769070506):
															return True
														else:
															if(pole_angle > 0.0016600610106252134):
																return True
													else:
														if(pole_angular_velocity > -0.029582764953374863):
															return True
												else:
													if(pole_angular_velocity <= -0.031129821203649044):
														if(cart_position <= 0.13293349742889404):
															return True
														else:
															if(pole_angular_velocity <= -0.034659333527088165):
																return True
											else:
												if(cart_position <= 0.12897829711437225):
													if(pole_angle <= 0.0013888367684558034):
														if(cart_velocity <= 0.03108091652393341):
															return True
														else:
															if(pole_angle <= 0.0011762651847675443):
																return True
													else:
														if(pole_angular_velocity <= -0.03121057990938425):
															if(cart_velocity <= 0.03155292011797428):
																if(pole_angle <= 0.0017187854391522706):
																	return True
																else:
																	if(cart_velocity > 0.027369491755962372):
																		return True
												else:
													if(pole_angular_velocity <= -0.03459313325583935):
														if(cart_velocity <= 0.02667234092950821):
															return True
														else:
															if(cart_velocity <= 0.027550161816179752):
																if(pole_angle <= 0.001643442374188453):
																	return True
													else:
														if(pole_angular_velocity > -0.030800125561654568):
															return True
										else:
											if(pole_angular_velocity <= -0.03636337071657181):
												if(pole_angular_velocity > -0.03656227886676788):
													return True
								else:
									if(pole_angle <= 0.0013962979428470135):
										if(pole_angular_velocity <= -0.043066276237368584):
											if(cart_velocity <= 0.040496472269296646):
												if(cart_position <= 0.14295709133148193):
													return True
												else:
													if(pole_angle <= 0.0011369884596206248):
														return True
											else:
												if(cart_position <= 0.13214141875505447):
													if(cart_position <= 0.1287303790450096):
														return True
													else:
														if(cart_position > 0.1302071511745453):
															return True
										else:
											if(cart_position <= 0.030272454023361206):
												return True
									else:
										if(cart_position <= 0.016152012161910534):
											if(pole_angle > 0.0017751044942997396):
												return True
										else:
											if(cart_velocity <= 0.03851357661187649):
												if(cart_velocity <= 0.03839671052992344):
													if(cart_position <= 0.12326744571328163):
														return True
													else:
														if(pole_angle <= 0.0015641851932741702):
															if(cart_position <= 0.13283222168684006):
																return True
															else:
																if(pole_angular_velocity <= -0.048354996368288994):
																	return True
												else:
													return True
							else:
								if(pole_angular_velocity <= -0.04927212931215763):
									if(pole_angle <= 0.002023170585744083):
										return True
									else:
										if(cart_position > 0.13698405027389526):
											return True
								else:
									if(cart_position <= 0.050017378060147166):
										return True
									else:
										if(pole_angular_velocity <= -0.03548646159470081):
											if(cart_velocity <= 0.02577099669724703):
												if(pole_angle <= 0.0022857995936647058):
													if(pole_angular_velocity <= -0.0373199712485075):
														return True
													else:
														if(cart_position <= 0.13446596264839172):
															return True
												else:
													if(pole_angle > 0.0023919768864288926):
														return True
											else:
												if(pole_angular_velocity <= -0.040850136429071426):
													if(cart_velocity <= 0.027722149156033993):
														return True
													else:
														if(pole_angular_velocity <= -0.04813481122255325):
															if(pole_angular_velocity > -0.048945074900984764):
																if(pole_angular_velocity <= -0.0487897340208292):
																	return True
																else:
																	if(pole_angular_velocity <= -0.04831415042281151):
																		if(pole_angular_velocity <= -0.04843960329890251):
																			if(pole_angular_velocity <= -0.04851290211081505):
																				if(pole_angle > 0.00214701727963984):
																					if(cart_velocity <= 0.03535102866590023):
																						return True
																			else:
																				return True
																	else:
																		return True
														else:
															if(cart_velocity <= 0.029312293976545334):
																if(cart_velocity > 0.028147462755441666):
																	return True
															else:
																if(pole_angular_velocity <= -0.04531264863908291):
																	if(cart_velocity <= 0.03415708802640438):
																		if(cart_position <= 0.13754727691411972):
																			return True
																	else:
																		if(pole_angle > 0.0022747264010831714):
																			if(pole_angle <= 0.0022866216022521257):
																				return True
																			else:
																				if(cart_position <= 0.1318056657910347):
																					if(cart_velocity <= 0.041028523817658424):
																						return True
										else:
											if(cart_velocity <= 0.01863882038742304):
												return True
											else:
												if(cart_velocity <= 0.021814710460603237):
													if(pole_angle <= 0.002042517880909145):
														if(cart_position <= 0.1327701434493065):
															return True
						else:
							if(cart_velocity <= 0.00282054184935987):
								if(pole_angle <= 0.0021868631010875106):
									if(cart_position > 0.1076478660106659):
										if(pole_angular_velocity <= -0.0035334256244823337):
											return True
										else:
											if(pole_angular_velocity > -0.003529044450260699):
												return True
								else:
									if(cart_velocity > -0.0002931197814177722):
										return True
							else:
								if(cart_velocity <= 0.006174753187224269):
									if(cart_position <= 0.11734187975525856):
										if(pole_angular_velocity <= -0.0034374238457530737):
											if(cart_velocity <= 0.006066468311473727):
												return True
											else:
												if(pole_angle <= 0.0016553500900045037):
													return True
									else:
										if(pole_angular_velocity <= -0.019297177903354168):
											if(cart_position <= 0.13768305629491806):
												return True
								else:
									if(pole_angular_velocity <= -0.020459745079278946):
										if(cart_velocity <= 0.013552385848015547):
											if(pole_angle <= 0.0017794657032936811):
												if(cart_position <= 0.12944061309099197):
													return True
												else:
													if(pole_angle <= 0.001459748251363635):
														return True
										else:
											if(cart_velocity <= 0.01895028166472912):
												if(pole_angle <= 0.0014069550670683384):
													if(pole_angular_velocity <= -0.022561250254511833):
														if(cart_position <= 0.1306416541337967):
															if(pole_angle > 0.001116048835683614):
																return True
														else:
															if(pole_angle <= 0.0011157062253914773):
																return True
												else:
													if(pole_angular_velocity <= -0.027213552966713905):
														if(cart_velocity <= 0.018711826764047146):
															if(cart_position <= 0.1289253681898117):
																if(cart_velocity > 0.01854969933629036):
																	return True
															else:
																return True
											else:
												if(cart_position <= -0.029484671540558338):
													return True
												else:
													if(pole_angular_velocity <= -0.028337794356048107):
														if(pole_angular_velocity <= -0.028340106830000877):
															if(pole_angle <= 0.0014631999074481428):
																if(cart_velocity <= 0.023814482614398003):
																	if(pole_angle > 0.0011867345892824233):
																		return True
														else:
															return True
									else:
										if(cart_position <= 0.03988335840404034):
											return True
										else:
											if(pole_angular_velocity <= -0.003893062239512801):
												if(cart_velocity <= 0.010502154473215342):
													if(cart_position <= 0.11064057052135468):
														return True
													else:
														if(cart_velocity <= 0.01042317459359765):
															if(pole_angular_velocity <= -0.01692405715584755):
																if(pole_angular_velocity > -0.0170561159029603):
																	return True
														else:
															return True
											else:
												if(pole_angular_velocity <= -0.003818449331447482):
													return True
				else:
					if(cart_position <= 0.028438886627554893):
						if(cart_velocity <= 0.03284766711294651):
							if(pole_angle <= 0.023555129766464233):
								if(pole_angular_velocity <= -0.014416192192584276):
									if(cart_velocity <= 0.025547269731760025):
										return True
									else:
										if(pole_angle <= 0.019437029026448727):
											return True
										else:
											if(pole_angular_velocity <= -0.04076244216412306):
												return True
								else:
									if(cart_velocity <= 0.0071754977107048035):
										if(cart_position <= 0.022905432619154453):
											return True
										else:
											if(pole_angle <= 0.016636349260807037):
												return True
									else:
										if(pole_angle <= 0.01228404464200139):
											return True
										else:
											if(cart_position <= -0.017438925802707672):
												if(pole_angular_velocity <= -0.008135555777698755):
													return True
											else:
												if(pole_angle <= 0.01508592814207077):
													if(pole_angle > 0.013196408748626709):
														return True
							else:
								if(cart_position <= -0.0496489517390728):
									if(pole_angular_velocity <= -0.01198843540623784):
										return True
									else:
										if(pole_angle <= 0.03068393189460039):
											return True
										else:
											if(pole_angular_velocity > -0.01003992510959506):
												return True
								else:
									if(pole_angle <= 0.032017605379223824):
										if(cart_velocity <= -0.006098617101088166):
											if(pole_angular_velocity <= -0.011886980384588242):
												if(pole_angle <= 0.02794093731790781):
													return True
												else:
													if(cart_position <= -0.031096693128347397):
														return True
													else:
														if(pole_angular_velocity <= -0.03933236561715603):
															return True
											else:
												if(cart_velocity <= -0.03853926621377468):
													return True
										else:
											if(pole_angular_velocity <= -0.04562007635831833):
												return True
											else:
												if(cart_velocity <= -0.0026212469092570245):
													if(cart_velocity > -0.0038556245854124427):
														return True
						else:
							if(pole_angle <= 0.01413720939308405):
								if(cart_velocity <= 0.1375659629702568):
									if(pole_angular_velocity <= -0.017094180919229984):
										return True
									else:
										if(cart_position <= 0.01512965327128768):
											return True
										else:
											if(cart_position > 0.021833554841578007):
												return True
								else:
									if(pole_angular_velocity <= -0.071258045732975):
										if(cart_position <= -0.0073337743524461985):
											if(pole_angle <= 0.012528563383966684):
												if(pole_angular_velocity <= -0.09313137456774712):
													return True
												else:
													if(cart_velocity <= 0.16169529408216476):
														if(cart_position <= -0.020131546072661877):
															return True
														else:
															if(pole_angle <= 0.008009798126295209):
																return True
															else:
																if(pole_angular_velocity <= -0.0830874964594841):
																	return True
													else:
														if(pole_angle <= 0.005411121062934399):
															return True
														else:
															if(cart_velocity > 0.17712782323360443):
																return True
											else:
												if(pole_angular_velocity <= -0.09197579324245453):
													if(cart_velocity <= 0.16960160434246063):
														return True
										else:
											if(pole_angle <= 0.008975683711469173):
												if(pole_angular_velocity <= -0.08431228995323181):
													if(cart_velocity <= 0.17762935161590576):
														if(cart_velocity <= 0.1600748673081398):
															if(pole_angle <= 0.008389109279960394):
																return True
															else:
																if(pole_angle > 0.008527236990630627):
																	return True
														else:
															if(pole_angular_velocity <= -0.09964044392108917):
																return True
															else:
																if(pole_angle <= 0.004062330117449164):
																	return True
												else:
													if(pole_angle <= 0.005337200593203306):
														if(cart_velocity <= 0.15902706235647202):
															if(cart_velocity > 0.14211325347423553):
																return True
														else:
															if(pole_angle <= 0.0027316423365846276):
																return True
											else:
												if(pole_angular_velocity <= -0.09626885503530502):
													if(cart_velocity <= 0.1501263976097107):
														if(pole_angular_velocity > -0.10709341242909431):
															return True
									else:
										if(cart_position <= -0.02137991040945053):
											if(pole_angle <= 0.005585101433098316):
												if(pole_angular_velocity <= -0.03189572133123875):
													if(cart_position <= -0.0272954311221838):
														return True
													else:
														if(cart_velocity <= 0.14784640818834305):
															return True
											else:
												if(cart_position <= -0.06655250489711761):
													return True
												else:
													if(pole_angle <= 0.00951764127239585):
														if(pole_angular_velocity <= -0.06430348008871078):
															return True
														else:
															if(cart_position <= -0.056726040318608284):
																return True
															else:
																if(cart_velocity <= 0.14134886115789413):
																	if(pole_angle <= 0.008340653497725725):
																		return True
										else:
											if(pole_angular_velocity <= -0.06356468424201012):
												if(pole_angular_velocity > -0.06537798792123795):
													return True
							else:
								if(cart_velocity <= 0.14591672271490097):
									if(pole_angular_velocity <= -0.028368402272462845):
										if(cart_velocity <= 0.09278042800724506):
											if(pole_angle <= 0.025431196205317974):
												if(cart_position <= 0.006123639876022935):
													if(pole_angle <= 0.024130753241479397):
														return True
													else:
														if(pole_angular_velocity <= -0.0414343886077404):
															return True
											else:
												if(pole_angular_velocity <= -0.04620332084596157):
													return True
										else:
											if(pole_angular_velocity <= -0.1035441942512989):
												if(cart_velocity > 0.14203225076198578):
													if(pole_angular_velocity > -0.11130817607045174):
														return True
											else:
												if(cart_velocity <= 0.14066310226917267):
													if(pole_angular_velocity <= -0.08796336874365807):
														return True
									else:
										if(pole_angle <= 0.015309076756238937):
											if(cart_position <= -0.023979621939361095):
												return True
										else:
											if(cart_velocity > 0.04487010836601257):
												if(cart_velocity <= 0.04550827853381634):
													return True
								else:
									if(cart_position <= -0.05885281413793564):
										if(cart_position <= -0.061288025230169296):
											if(pole_angle <= 0.017926541157066822):
												if(cart_position > -0.0672721415758133):
													return True
										else:
											return True
					else:
						if(pole_angular_velocity <= -0.06643299758434296):
							if(pole_angle <= 0.003843779326416552):
								if(cart_position <= 0.14315197616815567):
									if(cart_position <= 0.05403122678399086):
										if(pole_angular_velocity <= -0.09961220622062683):
											return True
										else:
											if(cart_velocity <= 0.13873457163572311):
												return True
											else:
												if(cart_position <= 0.035960471257567406):
													if(pole_angle <= 0.003041438525542617):
														return True
									else:
										if(cart_velocity <= 0.049660542979836464):
											return True
								else:
									if(pole_angle <= 0.0031002408359199762):
										if(cart_position <= 0.1552405208349228):
											if(cart_position <= 0.15087270736694336):
												if(cart_velocity <= 0.05035465396940708):
													return True
												else:
													if(cart_velocity > 0.05082029663026333):
														return True
											else:
												if(pole_angular_velocity <= -0.07035911455750465):
													return True
												else:
													if(cart_velocity <= 0.04816877469420433):
														if(pole_angular_velocity <= -0.06808415055274963):
															return True
														else:
															if(cart_velocity <= 0.046318696811795235):
																return True
									else:
										if(pole_angular_velocity <= -0.07368836179375648):
											if(pole_angular_velocity <= -0.07532941550016403):
												return True
											else:
												if(cart_velocity <= 0.04986831918358803):
													return True
												else:
													if(pole_angle <= 0.003591612563468516):
														return True
										else:
											if(cart_position <= 0.14987730234861374):
												if(pole_angle <= 0.0034904812928289175):
													if(pole_angular_velocity <= -0.0675150603055954):
														return True
													else:
														if(cart_velocity <= 0.045735858380794525):
															return True
												else:
													if(cart_position > 0.14818403869867325):
														return True
											else:
												if(cart_position <= 0.15241104364395142):
													if(pole_angular_velocity <= -0.07273541390895844):
														if(pole_angle <= 0.0037438870640471578):
															return True
													else:
														if(pole_angle <= 0.0031840638257563114):
															if(cart_position <= 0.15156088769435883):
																return True
														else:
															if(cart_velocity <= 0.04678406938910484):
																if(pole_angular_velocity <= -0.06903228908777237):
																	return True
							else:
								if(pole_angle <= 0.004057509824633598):
									if(pole_angular_velocity <= -0.07288186624646187):
										if(cart_velocity <= 0.049263374879956245):
											return True
										else:
											if(cart_position > 0.10102850012481213):
												if(cart_velocity <= 0.04989118501543999):
													if(pole_angular_velocity > -0.07329099625349045):
														return True
												else:
													return True
									else:
										if(pole_angle > 0.004033996490761638):
											return True
								else:
									if(pole_angular_velocity <= -0.09908933565020561):
										if(pole_angular_velocity > -0.10420261695981026):
											return True
									else:
										if(pole_angle <= 0.004670804366469383):
											if(pole_angle <= 0.004669672343879938):
												if(pole_angular_velocity <= -0.07386050373315811):
													if(cart_velocity <= 0.048539379611611366):
														if(cart_position <= 0.15143024176359177):
															return True
														else:
															if(pole_angular_velocity <= -0.07570376992225647):
																return True
													else:
														if(pole_angular_velocity <= -0.07438009977340698):
															if(cart_velocity <= 0.050113240256905556):
																if(pole_angular_velocity <= -0.07670838758349419):
																	return True
														else:
															if(cart_position <= 0.14699409902095795):
																return True
												else:
													if(cart_velocity <= 0.04578855074942112):
														if(pole_angular_velocity <= -0.07005952298641205):
															if(cart_position <= 0.15029694885015488):
																return True
											else:
												return True
						else:
							if(pole_angle <= 0.003370310296304524):
								if(pole_angular_velocity <= -0.04980311915278435):
									if(cart_velocity <= 0.03435851261019707):
										if(pole_angular_velocity <= -0.0502214040607214):
											if(pole_angle <= 0.0032878780039027333):
												return True
											else:
												if(pole_angular_velocity <= -0.05205398425459862):
													return True
										else:
											if(cart_velocity <= 0.03285261243581772):
												if(pole_angular_velocity > -0.05013013444840908):
													return True
									else:
										if(pole_angle <= 0.002874906058423221):
											if(pole_angular_velocity <= -0.06255181133747101):
												if(cart_velocity <= 0.04539357125759125):
													return True
												else:
													if(cart_position <= 0.14666393399238586):
														return True
													else:
														if(pole_angle > 0.0026258056750521064):
															return True
											else:
												if(cart_position <= 0.14606591314077377):
													if(pole_angular_velocity <= -0.051452044397592545):
														if(cart_velocity <= 0.0449281707406044):
															if(pole_angular_velocity <= -0.05195934697985649):
																if(pole_angle <= 0.0028015930438414216):
																	return True
																else:
																	if(cart_velocity <= 0.042453475296497345):
																		return True
																	else:
																		if(cart_position <= 0.13335401564836502):
																			return True
															else:
																if(pole_angle > 0.0027379372622817755):
																	return True
														else:
															if(pole_angular_velocity <= -0.05991795472800732):
																if(pole_angular_velocity > -0.0611897986382246):
																	return True
															else:
																if(cart_position <= 0.1352398544549942):
																	return True
																else:
																	if(cart_velocity <= 0.0452559869736433):
																		if(pole_angular_velocity <= -0.05851682834327221):
																			return True
													else:
														if(cart_position <= 0.12549088150262833):
															return True
												else:
													if(pole_angle <= 0.002525437856093049):
														if(cart_position > 0.14764633029699326):
															return True
													else:
														if(pole_angular_velocity <= -0.06141536682844162):
															if(pole_angular_velocity > -0.06161227263510227):
																return True
										else:
											if(pole_angular_velocity <= -0.060212790966033936):
												if(cart_velocity <= 0.04162030294537544):
													if(cart_position <= 0.14893507212400436):
														return True
													else:
														if(pole_angle <= 0.0030393695924431086):
															return True
												else:
													if(pole_angular_velocity <= -0.06425890326499939):
														if(cart_velocity <= 0.044002968817949295):
															return True
														else:
															if(pole_angular_velocity <= -0.06443752348423004):
																if(pole_angle > 0.003298952244222164):
																	if(cart_position <= 0.147245354950428):
																		return True
															else:
																return True
													else:
														if(pole_angle <= 0.003118026303127408):
															if(pole_angle <= 0.0031114351004362106):
																if(cart_velocity <= 0.042281677946448326):
																	if(cart_velocity > 0.04190879315137863):
																		return True
																else:
																	if(cart_position <= 0.14293941855430603):
																		if(pole_angle <= 0.0029427262488752604):
																			return True
															else:
																return True
											else:
												if(pole_angular_velocity > -0.05406374670565128):
													if(cart_velocity <= 0.04079323261976242):
														if(cart_position <= 0.13543809950351715):
															return True
													else:
														if(cart_velocity <= 0.043518880382180214):
															if(cart_position <= 0.1296515390276909):
																return True
								else:
									if(pole_angular_velocity <= -0.045062096789479256):
										if(cart_velocity <= 0.02952786348760128):
											return True
										else:
											if(pole_angle <= 0.002617380814626813):
												if(cart_velocity <= 0.03656543791294098):
													if(pole_angular_velocity <= -0.046708159148693085):
														if(cart_position <= 0.13936857879161835):
															return True
														else:
															if(cart_position > 0.14000459760427475):
																return True
											else:
												if(pole_angular_velocity <= -0.04911050945520401):
													if(pole_angular_velocity <= -0.04917146638035774):
														if(pole_angle <= 0.002923046122305095):
															if(pole_angle > 0.0028042810736224055):
																if(cart_velocity <= 0.038219476118683815):
																	return True
													else:
														return True
												else:
													if(pole_angle <= 0.0028745902236551046):
														if(pole_angle > 0.0028594553004950285):
															return True
									else:
										if(cart_position <= 0.04710812121629715):
											return True
										else:
											if(cart_position <= 0.14320603758096695):
												if(cart_position > 0.1377197578549385):
													if(cart_position <= 0.13776663690805435):
														return True
											else:
												if(pole_angular_velocity > -0.0295974500477314):
													return True
							else:
								if(cart_position <= 0.04692660830914974):
									if(pole_angle <= 0.010901434812694788):
										if(pole_angular_velocity <= -0.010088811162859201):
											return True
									else:
										if(cart_position > 0.045163920149207115):
											return True
								else:
									if(pole_angle <= 0.009350965265184641):
										if(pole_angle <= 0.0038000590866431594):
											if(pole_angle <= 0.0037992740981280804):
												if(pole_angular_velocity <= -0.0489039272069931):
													if(cart_velocity <= 0.03192690201103687):
														return True
													else:
														if(cart_velocity <= 0.03251670487225056):
															if(pole_angular_velocity <= -0.052171846851706505):
																return True
															else:
																if(cart_velocity > 0.03247925080358982):
																	return True
														else:
															if(pole_angular_velocity <= -0.06292105093598366):
																if(cart_velocity <= 0.04161643981933594):
																	return True
																else:
																	if(pole_angle <= 0.0034214883344247937):
																		if(cart_position <= 0.14634456485509872):
																			return True
											else:
												return True
										else:
											if(pole_angle <= 0.004083692096173763):
												if(pole_angle <= 0.004083298845216632):
													if(pole_angle <= 0.0040718321688473225):
														if(pole_angular_velocity <= -0.05133263021707535):
															if(cart_velocity <= 0.033010113053023815):
																return True
													else:
														if(pole_angle <= 0.00407233671285212):
															return True
												else:
													return True
									else:
										if(cart_position > 0.050569405779242516):
											return True
	else:
		if(pole_angular_velocity <= 0.08658628165721893):
			if(pole_angle <= -0.0018948267679661512):
				if(pole_angular_velocity <= 0.04840107820928097):
					if(pole_angle <= -0.0027885206509381533):
						if(cart_position <= 0.13545861095190048):
							if(cart_velocity <= 0.010182851459831):
								if(cart_position <= 0.08729403838515282):
									if(pole_angle <= -0.00370804057456553):
										if(pole_angular_velocity <= 0.04686068557202816):
											if(cart_velocity <= 0.008001958020031452):
												return True
											else:
												if(pole_angular_velocity <= 0.04440663941204548):
													return True
										else:
											if(pole_angular_velocity > 0.04693036340177059):
												if(cart_velocity <= 0.004551619291305542):
													return True
												else:
													if(pole_angular_velocity > 0.04735391587018967):
														return True
									else:
										if(pole_angular_velocity <= 0.047627612948417664):
											if(cart_velocity <= -0.003266121493652463):
												if(cart_position <= 0.08519768714904785):
													return True
												else:
													if(cart_position > 0.08615422621369362):
														return True
											else:
												if(pole_angle <= -0.0031583476811647415):
													if(pole_angle <= -0.00346798833925277):
														if(pole_angle <= -0.0035172487841919065):
															if(cart_position <= 0.08237342536449432):
																return True
													else:
														if(cart_position <= 0.08103564381599426):
															return True
														else:
															if(cart_position > 0.0833553597331047):
																return True
												else:
													if(pole_angular_velocity <= 0.03567185625433922):
														if(pole_angle <= -0.0029703809414058924):
															return True
													else:
														if(cart_position <= 0.06665099412202835):
															if(cart_position > 0.06151161529123783):
																return True
										else:
											if(cart_position > 0.08670339360833168):
												return True
								else:
									if(cart_position <= 0.12802743166685104):
										if(pole_angle <= -0.007977426052093506):
											if(pole_angle <= -0.008060711435973644):
												if(cart_position <= 0.12680620700120926):
													return True
										else:
											if(cart_velocity <= 0.004249657969921827):
												if(cart_position <= 0.09331993386149406):
													if(cart_position <= 0.09331368654966354):
														if(pole_angle <= -0.00322956929448992):
															if(pole_angular_velocity <= 0.04804086685180664):
																return True
															else:
																if(pole_angular_velocity > 0.04808006063103676):
																	return True
														else:
															if(pole_angle > -0.0032180165871977806):
																if(cart_velocity <= 0.0012562256306409836):
																	if(cart_velocity <= -0.012060971464961767):
																		return True
																	else:
																		if(cart_velocity > -0.010638115927577019):
																			return True
																else:
																	if(cart_position > 0.0899173729121685):
																		return True
												else:
													if(cart_position <= 0.09528651833534241):
														if(cart_position <= 0.09526034072041512):
															return True
													else:
														return True
											else:
												if(pole_angular_velocity <= 0.028017327189445496):
													if(pole_angle <= -0.0029528032755479217):
														if(cart_position <= 0.12173755466938019):
															return True
														else:
															if(cart_position > 0.12196747586131096):
																return True
													else:
														if(pole_angle > -0.002935857977718115):
															return True
												else:
													if(cart_position <= 0.09477663040161133):
														return True
									else:
										if(pole_angular_velocity <= 0.0408022366464138):
											if(pole_angular_velocity <= 0.018430289812386036):
												if(cart_velocity <= 0.009645860642194748):
													return True
												else:
													if(pole_angular_velocity <= 0.010669208131730556):
														return True
											else:
												if(cart_velocity <= -0.01812083926051855):
													return True
												else:
													if(pole_angle <= -0.009040636010468006):
														return True
													else:
														if(cart_position > 0.13441315293312073):
															return True
										else:
											if(pole_angle <= -0.012659494299441576):
												return True
							else:
								if(pole_angle <= -0.004059867933392525):
									if(pole_angular_velocity <= 0.019134478643536568):
										if(cart_velocity <= 0.04475676827132702):
											if(cart_position <= 0.10239100083708763):
												if(cart_position <= 0.09665311500430107):
													return True
												else:
													if(cart_position > 0.09693354740738869):
														return True
											else:
												if(pole_angular_velocity <= 0.010677686892449856):
													if(cart_velocity <= 0.03272364940494299):
														return True
													else:
														if(pole_angle <= -0.0075622189324349165):
															return True
												else:
													if(pole_angle <= -0.00746310711838305):
														return True
													else:
														if(cart_velocity <= 0.0156573336571455):
															return True
										else:
											if(pole_angular_velocity <= 0.014385002665221691):
												if(cart_velocity > 0.04489663802087307):
													if(pole_angle <= -0.004993703681975603):
														return True
													else:
														if(cart_position <= 0.08459747210144997):
															return True
											else:
												if(cart_velocity > 0.0465648602694273):
													return True
									else:
										if(cart_position <= 0.08565227314829826):
											if(pole_angle <= -0.004352171439677477):
												if(pole_angular_velocity > 0.019218124449253082):
													if(cart_velocity <= 0.046802155673503876):
														if(pole_angular_velocity <= 0.04773455113172531):
															if(pole_angular_velocity <= 0.0415323618799448):
																if(cart_velocity <= 0.0377654992043972):
																	return True
																else:
																	if(cart_position <= 0.06999950483441353):
																		if(pole_angle <= -0.005235082004219294):
																			return True
																		else:
																			if(pole_angular_velocity <= 0.030675822868943214):
																				return True
																			else:
																				if(cart_position <= 0.0369076170027256):
																					return True
																	else:
																		if(pole_angle <= -0.0106420055963099):
																			return True
															else:
																if(cart_position <= 0.04381651058793068):
																	return True
																else:
																	if(cart_velocity <= 0.016267615370452404):
																		return True
																	else:
																		if(pole_angle <= -0.005907225189730525):
																			if(pole_angular_velocity > 0.04201730340719223):
																				if(cart_velocity > 0.01701516006141901):
																					return True
														else:
															if(cart_velocity <= 0.03629193641245365):
																return True
											else:
												if(cart_velocity <= 0.030580700375139713):
													if(pole_angle > -0.004333818098530173):
														return True
												else:
													if(cart_position <= 0.024417977780103683):
														return True
										else:
											if(pole_angle <= -0.010669929441064596):
												if(cart_position > 0.08836940303444862):
													if(cart_velocity <= 0.02640074770897627):
														return True
													else:
														if(pole_angle <= -0.013998669572174549):
															return True
														else:
															if(cart_velocity > 0.044335201382637024):
																return True
											else:
												if(pole_angular_velocity <= 0.025046157650649548):
													if(cart_velocity <= 0.016798446886241436):
														if(cart_position <= 0.1179390586912632):
															return True
													else:
														if(pole_angular_velocity <= 0.021846658550202847):
															return True
														else:
															if(cart_position > 0.1149255521595478):
																return True
												else:
													if(pole_angular_velocity <= 0.03244594298303127):
														if(pole_angle <= -0.006564689567312598):
															if(cart_velocity <= 0.03134188149124384):
																return True
								else:
									if(pole_angular_velocity <= 0.023723806254565716):
										if(cart_velocity <= 0.035604869946837425):
											if(pole_angle > -0.004055808996781707):
												if(cart_velocity > 0.010814413893967867):
													if(pole_angular_velocity <= 0.013891591224819422):
														if(cart_position <= 0.10056750103831291):
															return True
														else:
															if(pole_angular_velocity <= 0.0038936606142669916):
																if(cart_velocity <= 0.029507619328796864):
																	if(pole_angle <= -0.0029048542492091656):
																		return True
																	else:
																		if(pole_angle > -0.0028971917927265167):
																			return True
															else:
																if(pole_angular_velocity <= 0.004967804299667478):
																	if(cart_position <= 0.10610519349575043):
																		return True
													else:
														if(cart_position <= 0.09348141774535179):
															if(pole_angle <= -0.0029353046556934714):
																if(cart_velocity <= 0.030934919603168964):
																	return True
																else:
																	if(cart_velocity > 0.03389703668653965):
																		return True
										else:
											if(cart_position <= 0.06067943572998047):
												if(pole_angle <= -0.003217127756215632):
													return True
												else:
													if(pole_angular_velocity <= 0.015943866223096848):
														return True
													else:
														if(cart_velocity <= 0.03845231980085373):
															return True
											else:
												if(pole_angular_velocity <= 0.011252065654844046):
													if(cart_position <= 0.08284078538417816):
														if(pole_angle <= -0.003520656260661781):
															if(cart_velocity <= 0.03915894031524658):
																return True
														else:
															return True
									else:
										if(cart_position <= 0.016707180999219418):
											if(cart_velocity <= 0.041155051440000534):
												return True
										else:
											if(cart_velocity <= 0.027955709025263786):
												if(pole_angle <= -0.0030310993315652013):
													if(cart_position <= 0.032785420306026936):
														return True
													else:
														if(pole_angular_velocity <= 0.03912240266799927):
															if(pole_angle <= -0.00381067197304219):
																return True
															else:
																if(cart_position <= 0.0525374636054039):
																	return True
																else:
																	if(pole_angular_velocity <= 0.0272164149209857):
																		if(pole_angle <= -0.0033471306087449193):
																			return True
																		else:
																			if(cart_velocity > 0.023487509228289127):
																				return True
																	else:
																		if(cart_velocity <= 0.010945013258606195):
																			if(cart_position <= 0.07721168920397758):
																				return True
												else:
													return True
											else:
												if(cart_position <= 0.0451427660882473):
													if(pole_angular_velocity <= 0.03581596165895462):
														if(cart_velocity <= 0.03921561315655708):
															if(pole_angle <= -0.0035452591255307198):
																return True
															else:
																if(pole_angle > -0.0034620248479768634):
																	return True
													else:
														if(pole_angular_velocity <= 0.04756841994822025):
															if(cart_velocity > 0.04241124168038368):
																if(cart_velocity <= 0.04324964992702007):
																	return True
														else:
															return True
												else:
													if(cart_position > 0.0647168904542923):
														return True
						else:
							if(pole_angular_velocity <= 0.03501200117170811):
								if(pole_angle <= -0.004647788591682911):
									if(cart_velocity <= 0.0021335596102289855):
										if(pole_angular_velocity <= 0.026843409053981304):
											return True
										else:
											if(cart_velocity <= -0.018497398123145103):
												if(cart_position <= 0.15625044703483582):
													return True
												else:
													if(cart_position > 0.15671385824680328):
														if(pole_angle <= -0.005865723127499223):
															return True
														else:
															if(cart_velocity > -0.04620126076042652):
																return True
											else:
												if(pole_angle <= -0.007869185414165258):
													if(cart_velocity > -0.016994466073811054):
														return True
									else:
										if(pole_angle <= -0.009122591931372881):
											return True
										else:
											if(cart_position <= 0.1417383775115013):
												return True
								else:
									if(cart_position <= 0.1556118205189705):
										if(cart_velocity <= -0.027048157528042793):
											if(pole_angle <= -0.002863004570826888):
												if(pole_angular_velocity <= 0.032997315749526024):
													if(cart_velocity <= -0.03298007883131504):
														return True
													else:
														if(pole_angular_velocity <= 0.021276206709444523):
															return True
														else:
															if(cart_position <= 0.1407201811671257):
																return True
												else:
													if(pole_angle <= -0.0034950225381180644):
														return True
										else:
											if(pole_angular_velocity <= 0.013515433296561241):
												if(cart_velocity <= -0.009850638918578625):
													return True
											else:
												if(pole_angular_velocity <= 0.023441744968295097):
													if(pole_angle <= -0.0034919879399240017):
														if(cart_position <= 0.14066915214061737):
															return True
									else:
										if(pole_angular_velocity <= 0.016769805923104286):
											return True
										else:
											if(pole_angle > -0.0034697067458182573):
												if(pole_angle <= -0.0031667385483160615):
													return True
							else:
								if(pole_angle <= -0.00673403381370008):
									if(cart_velocity <= -0.030254825949668884):
										if(cart_position <= 0.16148946434259415):
											return True
										else:
											if(pole_angle <= -0.009226627182215452):
												return True
											else:
												if(cart_velocity <= -0.047227516770362854):
													return True
									else:
										if(pole_angle <= -0.009375588037073612):
											if(cart_position <= 0.16660825908184052):
												if(pole_angle <= -0.010481588542461395):
													return True
												else:
													if(cart_velocity <= -0.016520745120942593):
														return True
								else:
									if(cart_velocity <= -0.04539643041789532):
										if(cart_position <= 0.15098974108695984):
											return True
									else:
										if(pole_angle <= -0.00576742016710341):
											if(cart_velocity <= -0.040021127089858055):
												if(pole_angle > -0.00638415408320725):
													return True
					else:
						if(cart_position <= 0.09331047907471657):
							if(cart_velocity <= -0.020688110031187534):
								if(pole_angle <= -0.002214653533883393):
									return True
								else:
									if(cart_velocity <= -0.023455566726624966):
										return True
							else:
								if(cart_position <= 0.025653474032878876):
									if(cart_velocity <= 0.03904993645846844):
										return True
								else:
									if(cart_position <= 0.08292276412248611):
										if(pole_angular_velocity <= 0.005549541674554348):
											if(cart_position <= 0.07141547277569771):
												return True
											else:
												if(pole_angular_velocity <= 0.0011834462056867778):
													return True
										else:
											if(pole_angle <= -0.0026405659737065434):
												if(pole_angle <= -0.0026862743543460965):
													if(cart_velocity <= -0.010835300199687481):
														return True
													else:
														if(cart_position > 0.07686424627900124):
															if(cart_position <= 0.07982700318098068):
																return True
												else:
													if(pole_angle <= -0.0026656626723706722):
														return True
													else:
														if(cart_velocity <= -0.00040412519592791796):
															return True
											else:
												if(cart_position <= 0.056962911039590836):
													if(cart_velocity <= 0.0164274787530303):
														if(pole_angular_velocity <= 0.04101096652448177):
															return True
														else:
															if(pole_angle <= -0.0024843155406415462):
																return True
													else:
														if(pole_angular_velocity <= 0.012490851804614067):
															return True
														else:
															if(pole_angular_velocity <= 0.033056655898690224):
																if(cart_velocity <= 0.029383954592049122):
																	return True
												else:
													if(cart_velocity <= -0.012185124680399895):
														if(pole_angle > -0.0022241852711886168):
															return True
													else:
														if(pole_angle <= -0.002586945192888379):
															if(pole_angle > -0.002595498342998326):
																return True
														else:
															if(cart_position > 0.07959067076444626):
																if(cart_position <= 0.08023151010274887):
																	return True
									else:
										if(pole_angle <= -0.0022766987094655633):
											if(cart_position <= 0.08629100024700165):
												if(pole_angle <= -0.002646252978593111):
													return True
												else:
													if(cart_velocity > 0.016849886626005173):
														if(pole_angular_velocity > -0.002419115975499153):
															return True
											else:
												if(cart_velocity <= 0.03295582812279463):
													if(cart_position <= 0.09274518489837646):
														if(pole_angle > -0.002771042985841632):
															if(pole_angle <= -0.0023369689006358385):
																return True
															else:
																if(pole_angle > -0.0023349844850599766):
																	return True
													else:
														if(cart_position > 0.09321341663599014):
															return True
										else:
											if(pole_angular_velocity <= -0.0024712298763915896):
												return True
											else:
												if(pole_angular_velocity <= 0.03308551944792271):
													if(cart_velocity <= -0.0004852371057495475):
														if(pole_angular_velocity <= 0.028722570277750492):
															return True
														else:
															if(pole_angular_velocity > 0.03257204219698906):
																return True
													else:
														if(cart_position <= 0.08829068392515182):
															if(pole_angular_velocity <= 0.009508394170552492):
																return True
															else:
																if(cart_position > 0.08785121887922287):
																	return True
												else:
													if(cart_velocity <= -0.01712101884186268):
														if(cart_velocity > -0.01761701237410307):
															return True
						else:
							if(cart_position <= 0.1382184401154518):
								if(cart_position <= 0.10393159091472626):
									if(pole_angle <= -0.0023264142218977213):
										if(cart_velocity <= 0.027831070125102997):
											if(pole_angular_velocity <= 0.04054470546543598):
												if(pole_angular_velocity <= 0.027968290261924267):
													return True
												else:
													if(cart_velocity <= -0.01378049748018384):
														if(pole_angular_velocity <= 0.03783752769231796):
															return True
														else:
															if(pole_angular_velocity > 0.038125962018966675):
																return True
													else:
														if(pole_angle > -0.0024933365639299154):
															return True
											else:
												if(cart_velocity <= -0.030172111466526985):
													if(cart_position <= 0.1033339612185955):
														return True
												else:
													if(cart_velocity <= -0.02677830122411251):
														if(pole_angular_velocity <= 0.04463382437825203):
															return True
														else:
															if(cart_position <= 0.09443212300539017):
																return True
															else:
																if(pole_angle > -0.0023900215746834874):
																	if(cart_position > 0.09918142110109329):
																		return True
									else:
										if(cart_velocity <= -0.027684501372277737):
											if(pole_angle <= -0.0022814898984506726):
												if(pole_angular_velocity <= 0.04210546799004078):
													return True
											else:
												if(pole_angular_velocity <= 0.04817936196923256):
													return True
												else:
													if(cart_velocity <= -0.03428362496197224):
														return True
										else:
											if(pole_angular_velocity <= 0.035358285531401634):
												if(cart_velocity <= -0.015495395753532648):
													return True
												else:
													if(pole_angular_velocity <= 0.028679090552031994):
														if(cart_position <= 0.09936714172363281):
															if(pole_angle <= -0.0020179704297333956):
																if(cart_position <= 0.09833598509430885):
																	if(cart_velocity <= 0.009420171147212386):
																		return True
																	else:
																		if(cart_position <= 0.09641527384519577):
																			if(cart_position <= 0.0939447395503521):
																				return True
																		else:
																			return True
																else:
																	if(cart_velocity <= -0.0027193025161977857):
																		return True
														else:
															if(pole_angle <= -0.001980450004339218):
																return True
															else:
																if(pole_angle > -0.0019481866038404405):
																	return True
													else:
														if(cart_position <= 0.0988062173128128):
															if(cart_velocity <= -0.011521241627633572):
																return True
											else:
												if(pole_angle <= -0.0019059788901358843):
													if(cart_velocity <= -0.021692140959203243):
														if(cart_velocity <= -0.022250782698392868):
															if(cart_position <= 0.098397396504879):
																if(pole_angular_velocity <= 0.041841896250844):
																	return True
														else:
															return True
												else:
													return True
								else:
									if(cart_velocity <= 0.020437492057681084):
										if(cart_velocity <= 0.0036100936122238636):
											if(pole_angular_velocity <= 0.03972897678613663):
												if(cart_position <= 0.12804263830184937):
													if(pole_angular_velocity <= 0.03021401260048151):
														if(pole_angle <= -0.0019759349524974823):
															return True
														else:
															if(pole_angle > -0.0019745066529139876):
																return True
													else:
														if(cart_velocity <= -0.01987559162080288):
															if(pole_angle <= -0.00194970186566934):
																if(cart_velocity <= -0.020240798592567444):
																	if(cart_velocity <= -0.022055163979530334):
																		return True
																	else:
																		if(pole_angular_velocity <= 0.03514138422906399):
																			return True
																else:
																	if(pole_angular_velocity <= 0.03263545781373978):
																		return True
														else:
															if(cart_position <= 0.1056753359735012):
																return True
												else:
													if(cart_velocity <= -0.020138584077358246):
														return True
													else:
														if(cart_position > 0.13476929813623428):
															return True
											else:
												if(cart_velocity <= -0.03153453767299652):
													if(pole_angular_velocity <= 0.04551358334720135):
														return True
													else:
														if(cart_velocity <= -0.0402344074100256):
															if(cart_position <= 0.11741110682487488):
																return True
														else:
															if(cart_position <= 0.10710420086979866):
																if(cart_velocity <= -0.03723311051726341):
																	return True
												else:
													if(pole_angle <= -0.0024027179460972548):
														return True
										else:
											if(pole_angular_velocity <= 0.0013724692398682237):
												if(cart_position <= 0.12767338752746582):
													if(cart_velocity <= 0.016581224277615547):
														return True
													else:
														if(pole_angular_velocity <= -0.000504877622006461):
															return True
												else:
													if(pole_angle > -0.0025479135802015662):
														if(cart_position > 0.1279309317469597):
															if(cart_velocity > 0.0059395707212388515):
																return True
											else:
												if(cart_position <= 0.10786911100149155):
													return True
												else:
													if(pole_angular_velocity <= 0.0021084679756313562):
														if(cart_velocity <= 0.006921001011505723):
															return True
														else:
															if(cart_position <= 0.11562339961528778):
																return True
									else:
										if(pole_angular_velocity <= -0.0016216040239669383):
											return True
										else:
											if(pole_angle <= -0.0026121154660359025):
												return True
							else:
								if(pole_angular_velocity <= 0.030431772582232952):
									if(cart_velocity <= -0.026964817196130753):
										if(pole_angular_velocity <= 0.02668101154267788):
											if(cart_position <= 0.1594286933541298):
												return True
										else:
											if(cart_velocity <= -0.04339595139026642):
												return True
									else:
										if(cart_velocity > -0.015984494239091873):
											return True
								else:
									if(cart_velocity <= -0.049806367605924606):
										return True
									else:
										if(pole_angle > -0.0019152543391101062):
											return True
				else:
					if(pole_angle <= -0.00326326722279191):
						if(cart_velocity <= -0.028177586384117603):
							if(cart_position <= 0.13184284418821335):
								if(pole_angle <= -0.0041852351278066635):
									if(pole_angular_velocity <= 0.07315737009048462):
										if(pole_angular_velocity <= 0.07221377268433571):
											return True
										else:
											if(pole_angular_velocity > 0.07223759591579437):
												return True
									else:
										if(pole_angle <= -0.004658026387915015):
											if(cart_position <= 0.0919075645506382):
												if(pole_angular_velocity > 0.07326892763376236):
													if(pole_angle <= -0.004825372947379947):
														return True
													else:
														if(pole_angular_velocity > 0.0757005363702774):
															if(cart_velocity <= -0.036784423515200615):
																return True
															else:
																if(cart_velocity > -0.03316447418183088):
																	return True
										else:
											if(cart_velocity <= -0.04425456374883652):
												if(pole_angular_velocity <= 0.08257390931248665):
													if(cart_position <= 0.09035815671086311):
														return True
													else:
														if(cart_position > 0.09447632730007172):
															return True
												else:
													if(cart_velocity <= -0.052066951990127563):
														return True
								else:
									if(pole_angular_velocity <= 0.07383685186505318):
										if(pole_angular_velocity <= 0.06224820017814636):
											if(cart_velocity <= -0.03502323478460312):
												return True
											else:
												if(pole_angle <= -0.00339214492123574):
													if(cart_velocity > -0.03438927046954632):
														if(cart_velocity <= -0.02837305422872305):
															return True
														else:
															if(cart_velocity > -0.028252682648599148):
																return True
												else:
													if(cart_position <= 0.10096346959471703):
														if(pole_angular_velocity <= 0.05059307441115379):
															return True
														else:
															if(cart_position <= 0.0929693952202797):
																return True
										else:
											if(pole_angle <= -0.0036747048143297434):
												if(cart_velocity <= -0.03077466692775488):
													if(pole_angle <= -0.004168694140389562):
														if(pole_angular_velocity <= 0.06793864443898201):
															return True
													else:
														if(pole_angular_velocity <= 0.07236640900373459):
															if(pole_angle <= -0.004100146470591426):
																if(pole_angle <= -0.004115262301638722):
																	return True
															else:
																return True
														else:
															if(cart_position <= 0.08831541612744331):
																return True
												else:
													if(pole_angle > -0.0037887056823819876):
														return True
											else:
												if(cart_velocity <= -0.04211982525885105):
													if(pole_angular_velocity <= 0.06598488613963127):
														if(cart_position <= 0.09837179258465767):
															return True
													else:
														if(cart_position <= 0.08665787801146507):
															return True
														else:
															if(pole_angular_velocity <= 0.0695282481610775):
																if(cart_position <= 0.09220806881785393):
																	if(cart_velocity <= -0.04473506473004818):
																		return True
																	else:
																		if(cart_position <= 0.0903465636074543):
																			return True
												else:
													if(cart_position <= 0.09003398567438126):
														if(cart_velocity <= -0.03545811027288437):
															if(pole_angular_velocity <= 0.06628384813666344):
																return True
															else:
																if(pole_angle > -0.003387675271369517):
																	if(cart_velocity <= -0.03758971765637398):
																		return True
									else:
										if(pole_angular_velocity <= 0.07642998918890953):
											if(cart_velocity <= -0.04867844469845295):
												if(cart_position <= 0.0864558070898056):
													return True
												else:
													if(cart_velocity <= -0.051630692556500435):
														return True
													else:
														if(pole_angle <= -0.004020826192572713):
															if(cart_position <= 0.08775181695818901):
																return True
											else:
												if(pole_angular_velocity > 0.07602576538920403):
													return True
										else:
											if(cart_velocity <= -0.051999300718307495):
												if(pole_angle <= -0.0038336300058290362):
													return True
											else:
												if(pole_angle <= -0.004177968483418226):
													return True
							else:
								if(pole_angle <= -0.013499235268682241):
									if(cart_position <= 0.16394741833209991):
										return True
									else:
										if(cart_position > 0.16467012465000153):
											if(pole_angle <= -0.014278823044151068):
												if(cart_velocity <= -0.040243545547127724):
													return True
												else:
													if(pole_angular_velocity <= 0.07440816983580589):
														return True
											else:
												if(pole_angle > -0.013803570531308651):
													return True
								else:
									if(pole_angular_velocity <= 0.049851786345243454):
										if(pole_angle <= -0.009653241373598576):
											return True
									else:
										if(cart_position <= 0.15588058531284332):
											if(cart_position <= 0.1553429514169693):
												if(cart_velocity <= -0.04886636137962341):
													if(pole_angle <= -0.009765552822500467):
														return True
												else:
													if(pole_angular_velocity <= 0.0507539939135313):
														if(cart_velocity > -0.04308514483273029):
															return True
													else:
														if(cart_velocity <= -0.04590136744081974):
															if(cart_velocity > -0.0462156031280756):
																return True
											else:
												return True
						else:
							if(pole_angle <= -0.0043630595318973064):
								if(pole_angle <= -0.009362572804093361):
									if(pole_angle <= -0.01880499441176653):
										if(pole_angular_velocity <= 0.07810256630182266):
											if(cart_position <= 0.14993605017662048):
												return True
											else:
												if(pole_angle <= -0.02112623956054449):
													return True
												else:
													if(cart_velocity <= -0.009810342788114212):
														return True
										else:
											if(pole_angle <= -0.0193949518725276):
												return True
											else:
												if(pole_angular_velocity > 0.08185091987252235):
													return True
									else:
										if(pole_angular_velocity <= 0.0601644404232502):
											if(pole_angle <= -0.013923576567322016):
												if(cart_velocity <= 0.03708532825112343):
													if(cart_velocity <= 0.00636751763522625):
														return True
													else:
														if(cart_position <= 0.12082241103053093):
															return True
											else:
												if(pole_angle <= -0.01039755018427968):
													if(pole_angle <= -0.012933334335684776):
														if(cart_position <= 0.10044464096426964):
															return True
														else:
															if(pole_angular_velocity <= 0.054343149065971375):
																if(cart_velocity <= 0.010982813779264688):
																	return True
												else:
													if(pole_angle <= -0.009649902116507292):
														return True
										else:
											if(cart_position <= 0.0753144882619381):
												if(pole_angular_velocity <= 0.07302021235227585):
													return True
												else:
													if(cart_velocity <= 0.025199464056640863):
														if(pole_angular_velocity <= 0.08341487124562263):
															return True
											else:
												if(cart_velocity <= -0.026865716092288494):
													if(pole_angle <= -0.014148877933621407):
														return True
												else:
													if(pole_angular_velocity > 0.08121298253536224):
														if(pole_angular_velocity <= 0.08173271641135216):
															return True
								else:
									if(pole_angle <= -0.005766119109466672):
										if(cart_position <= 0.09414050355553627):
											if(cart_velocity <= 0.042570214718580246):
												if(cart_velocity <= 0.015517969615757465):
													if(pole_angular_velocity <= 0.0709017887711525):
														if(cart_velocity <= 0.012645615730434656):
															if(cart_position <= 0.07520683482289314):
																return True
															else:
																if(cart_position > 0.07551132142543793):
																	return True
														else:
															if(cart_velocity > 0.01355833699926734):
																return True
													else:
														if(pole_angular_velocity > 0.07112116366624832):
															if(pole_angle <= -0.006047762464731932):
																if(pole_angle <= -0.006618518149480224):
																	return True
																else:
																	if(pole_angle > -0.006579647539183497):
																		if(pole_angular_velocity <= 0.08005568012595177):
																			return True
																		else:
																			if(pole_angular_velocity > 0.08018364012241364):
																				if(cart_position <= 0.051039159297943115):
																					return True
															else:
																if(cart_position <= 0.0492896419018507):
																	if(pole_angle > -0.006000253837555647):
																		return True
																else:
																	if(pole_angle > -0.005824453197419643):
																		return True
												else:
													if(cart_position <= 0.05787615478038788):
														if(pole_angular_velocity <= 0.061242811381816864):
															return True
														else:
															if(cart_position <= 0.01842366438359022):
																if(cart_velocity <= 0.035024991258978844):
																	return True
																else:
																	if(cart_velocity > 0.03996996209025383):
																		return True
															else:
																if(pole_angle <= -0.008809386286884546):
																	return True
																else:
																	if(cart_position <= 0.02217838354408741):
																		if(pole_angular_velocity <= 0.07214377075433731):
																			return True
										else:
											if(pole_angular_velocity <= 0.04977840557694435):
												return True
									else:
										if(cart_position <= 0.06542211771011353):
											if(pole_angular_velocity <= 0.0750722587108612):
												if(cart_velocity <= 0.0034692706540226936):
													if(pole_angular_velocity <= 0.06019025854766369):
														if(cart_position <= 0.06526114419102669):
															return True
													else:
														if(cart_position <= 0.040417058393359184):
															return True
														else:
															if(pole_angle <= -0.0046766651794314384):
																if(pole_angular_velocity <= 0.07268042489886284):
																	if(cart_velocity <= -0.013121559750288725):
																		if(pole_angle <= -0.004880143329501152):
																			return True
																		else:
																			if(pole_angle > -0.004836946958675981):
																				return True
																	else:
																		if(cart_position <= 0.05286150611937046):
																			if(pole_angular_velocity <= 0.07119154930114746):
																				return True
																		else:
																			if(pole_angle <= -0.005623266100883484):
																				return True
																else:
																	if(pole_angular_velocity > 0.07344063743948936):
																		return True
															else:
																if(cart_velocity <= -0.01654118625447154):
																	return True
												else:
													if(cart_position <= 0.03776909410953522):
														if(cart_velocity <= 0.012872098945081234):
															return True
														else:
															if(pole_angle > -0.005708419252187014):
																if(cart_position <= -0.001437941929907538):
																	return True
																else:
																	if(pole_angular_velocity <= 0.0565667599439621):
																		if(cart_position <= 0.03318061679601669):
																			if(cart_velocity <= 0.028245840221643448):
																				return True
																	else:
																		if(pole_angle <= -0.004693459486588836):
																			if(cart_position <= 0.002916772267781198):
																				if(cart_position > 0.001269494867301546):
																					return True
																		else:
																			return True
													else:
														if(pole_angle <= -0.004610700998455286):
															if(cart_velocity > 0.010144409723579884):
																if(pole_angular_velocity > 0.055480148643255234):
																	return True
														else:
															if(cart_velocity <= 0.008009495446458459):
																return True
											else:
												if(pole_angle <= -0.005506416782736778):
													return True
												else:
													if(pole_angle <= -0.004471395397558808):
														if(pole_angular_velocity <= 0.08603126183152199):
															if(pole_angle <= -0.005421989830210805):
																if(cart_velocity <= -0.016374195460230112):
																	return True
															else:
																if(cart_position <= 0.027994547970592976):
																	if(cart_velocity <= -0.009329454507678747):
																		return True
														else:
															return True
													else:
														return True
										else:
											if(cart_velocity <= -0.0021035323152318597):
												if(cart_velocity <= -0.01080691209062934):
													if(pole_angle <= -0.004440441960468888):
														if(pole_angular_velocity <= 0.06449469178915024):
															return True
														else:
															if(cart_position <= 0.0730629675090313):
																return True
													else:
														if(pole_angle > -0.004411063622683287):
															return True
												else:
													if(pole_angular_velocity <= 0.05311620607972145):
														if(cart_velocity > -0.009017333388328552):
															return True
							else:
								if(cart_position <= 0.0870075412094593):
									if(cart_position <= -0.0038404426886700094):
										return True
									else:
										if(cart_position <= 0.027637461200356483):
											if(cart_velocity <= 0.01770114805549383):
												if(pole_angular_velocity <= 0.06912025064229965):
													return True
												else:
													if(cart_velocity <= -0.0053700299467891455):
														return True
													else:
														if(cart_position <= 0.004656660559703596):
															return True
										else:
											if(pole_angular_velocity <= 0.05702747218310833):
												if(pole_angular_velocity <= 0.056696921586990356):
													if(cart_velocity <= -0.01726914569735527):
														if(pole_angle <= -0.0038980102399364114):
															return True
													else:
														if(pole_angle > -0.004034565296024084):
															if(pole_angular_velocity <= 0.05026067979633808):
																if(cart_position <= 0.059557460248470306):
																	if(cart_velocity > 0.015206036623567343):
																		if(cart_velocity <= 0.02136725513264537):
																			return True
																else:
																	if(cart_velocity > -0.015114712063223124):
																		return True
															else:
																if(pole_angle <= -0.003992552636191249):
																	return True
																else:
																	if(cart_position <= 0.04862559773027897):
																		if(cart_position > 0.03894016519188881):
																			return True
												else:
													return True
											else:
												if(pole_angle <= -0.004103736486285925):
													if(cart_velocity <= -0.017528780736029148):
														if(pole_angular_velocity <= 0.07002386078238487):
															if(cart_position <= 0.07142163813114166):
																return True
												else:
													if(cart_velocity <= -0.026572921313345432):
														if(pole_angular_velocity <= 0.06297146156430244):
															return True
								else:
									if(cart_velocity <= -0.022243548184633255):
										if(pole_angle <= -0.0034285085275769234):
											if(cart_position <= 0.09602853283286095):
												return True
											else:
												if(pole_angular_velocity <= 0.04946975223720074):
													return True
									else:
										if(pole_angular_velocity <= 0.04931012541055679):
											if(cart_velocity > -0.021728073246777058):
												return True
					else:
						if(pole_angular_velocity <= 0.06650596857070923):
							if(pole_angle <= -0.0026623549638316035):
								if(cart_velocity <= -0.0409690085798502):
									if(cart_position <= 0.11116202175617218):
										if(pole_angular_velocity <= 0.06589268147945404):
											if(pole_angular_velocity <= 0.06146579049527645):
												return True
											else:
												if(cart_position <= 0.09548598900437355):
													return True
												else:
													if(cart_velocity <= -0.048424385488033295):
														return True
										else:
											if(pole_angular_velocity > 0.06611968576908112):
												return True
									else:
										if(pole_angle <= -0.002914618467912078):
											return True
								else:
									if(pole_angular_velocity <= 0.05113407224416733):
										if(cart_velocity <= -0.030079259537160397):
											return True
										else:
											if(pole_angle <= -0.002947781467810273):
												if(cart_position <= 0.08729927614331245):
													if(cart_velocity <= -0.002407952619250864):
														if(pole_angle <= -0.0031430585077032447):
															return True
														else:
															if(cart_velocity > -0.007466591894626617):
																return True
											else:
												if(pole_angular_velocity > 0.04861811175942421):
													return True
									else:
										if(cart_velocity <= -0.03313852474093437):
											if(pole_angular_velocity <= 0.06050352565944195):
												if(cart_position <= 0.09356216713786125):
													if(pole_angular_velocity <= 0.05786159634590149):
														return True
													else:
														if(cart_velocity <= -0.03866715356707573):
															return True
														else:
															if(cart_position <= 0.09052954241633415):
																return True
												else:
													if(pole_angle <= -0.0029288576915860176):
														if(cart_position > 0.09521977975964546):
															return True
													else:
														if(cart_velocity > -0.03406117856502533):
															return True
											else:
												if(cart_position <= 0.0847288928925991):
													return True
										else:
											if(cart_position <= 0.017315073870122433):
												return True
											else:
												if(pole_angular_velocity <= 0.06630289554595947):
													if(cart_position <= 0.02853291481733322):
														if(cart_velocity <= 0.012296652421355247):
															return True
													else:
														if(cart_position <= 0.04583653807640076):
															if(cart_velocity <= -0.006729455199092627):
																return True
														else:
															if(pole_angle <= -0.003119896864518523):
																if(pole_angle > -0.003131953999400139):
																	return True
												else:
													return True
							else:
								if(cart_position <= 0.017261892091482878):
									if(cart_velocity <= 0.03906405344605446):
										if(cart_velocity <= 0.02911505475640297):
											return True
										else:
											if(cart_velocity > 0.03352705016732216):
												return True
								else:
									if(pole_angular_velocity <= 0.049998046830296516):
										if(cart_velocity <= -0.03396899625658989):
											if(pole_angular_velocity <= 0.0490652434527874):
												if(cart_position <= 0.10621108114719391):
													if(pole_angle <= -0.0019560055807232857):
														return True
											else:
												if(cart_velocity <= -0.03632052801549435):
													return True
												else:
													if(cart_position <= 0.09868581965565681):
														return True
										else:
											if(pole_angular_velocity <= 0.04852062836289406):
												if(cart_velocity > -0.03245381824672222):
													return True
											else:
												if(cart_velocity <= -0.017346044536679983):
													if(cart_position <= 0.08529416099190712):
														return True
													else:
														if(cart_position <= 0.09190772101283073):
															if(cart_velocity <= -0.030077653005719185):
																return True
									else:
										if(cart_velocity <= -0.04699173383414745):
											if(pole_angular_velocity <= 0.057829516008496284):
												if(pole_angle <= -0.001989826268982142):
													return True
											else:
												if(cart_position <= 0.10054532438516617):
													if(pole_angular_velocity <= 0.06564878299832344):
														return True
										else:
											if(pole_angle <= -0.0023287987569347024):
												if(cart_velocity <= -0.043798159807920456):
													if(pole_angular_velocity <= 0.05745659954845905):
														return True
													else:
														if(cart_position <= 0.08938435837626457):
															return True
														else:
															if(pole_angle > -0.0023512464249506593):
																return True
												else:
													if(pole_angle <= -0.002331192488782108):
														if(cart_velocity <= -0.03507396951317787):
															if(pole_angular_velocity <= 0.057600535452365875):
																if(cart_position <= 0.09629738703370094):
																	return True
																else:
																	if(pole_angular_velocity <= 0.05092689208686352):
																		if(pole_angular_velocity > 0.05069569684565067):
																			return True
															else:
																if(pole_angular_velocity <= 0.059339242056012154):
																	if(cart_position <= 0.09278685599565506):
																		if(pole_angular_velocity > 0.05805807374417782):
																			return True
														else:
															if(cart_position <= 0.045522063970565796):
																if(cart_velocity <= 0.00301248487085104):
																	return True
													else:
														return True
											else:
												if(pole_angular_velocity <= 0.05365825071930885):
													if(pole_angular_velocity <= 0.05361645482480526):
														if(cart_velocity <= -0.040743038058280945):
															if(cart_velocity > -0.04246478155255318):
																return True
														else:
															if(cart_velocity <= -0.038528257980942726):
																if(cart_position <= 0.09806263074278831):
																	return True
													else:
														return True
						else:
							if(cart_position <= 0.020634266547858715):
								if(cart_velocity <= 1.2403354048728943e-05):
									if(pole_angular_velocity <= 0.08326425775885582):
										return True
								else:
									if(pole_angle <= -0.0030111162923276424):
										if(pole_angular_velocity <= 0.07370377704501152):
											return True
							else:
								if(pole_angle <= -0.0029084477573633194):
									if(cart_velocity <= -0.04735936410725117):
										if(pole_angular_velocity <= 0.07599300518631935):
											if(cart_position <= 0.08863015845417976):
												if(pole_angle <= -0.0031423838809132576):
													if(pole_angular_velocity <= 0.07113809138536453):
														return True
												else:
													return True
											else:
												if(pole_angular_velocity <= 0.06785981729626656):
													return True
									else:
										if(pole_angular_velocity <= 0.06762143597006798):
											if(pole_angular_velocity > 0.06731854006648064):
												return True
										else:
											if(pole_angle <= -0.0032291592797264457):
												if(pole_angle > -0.0032459113281220198):
													return True
								else:
									if(pole_angular_velocity <= 0.06682152673602104):
										if(pole_angular_velocity > 0.06672388687729836):
											return True
									else:
										if(cart_position <= 0.03819701448082924):
											if(cart_velocity <= -0.02599426545202732):
												return True
											else:
												if(pole_angular_velocity <= 0.06891779974102974):
													if(pole_angular_velocity > 0.06779113784432411):
														return True
										else:
											if(pole_angle <= -0.0027891843346878886):
												if(pole_angle > -0.0027906530303880572):
													return True
			else:
				if(pole_angle <= -0.0007869610853958875):
					if(cart_position <= 0.10362277552485466):
						if(pole_angular_velocity <= 0.0500108078122139):
							if(cart_velocity <= -0.034897370263934135):
								if(pole_angle <= -0.0010334622929804027):
									if(pole_angular_velocity <= 0.04926906153559685):
										return True
									else:
										if(cart_position <= 0.09797405824065208):
											if(pole_angle <= -0.0015414634253829718):
												return True
										else:
											return True
								else:
									if(pole_angle > -0.0009441797155886889):
										return True
							else:
								if(pole_angle <= -0.0013447722303681076):
									if(cart_position <= 0.0996936522424221):
										if(pole_angular_velocity <= -0.001844158861786127):
											if(cart_position > 0.07885867729783058):
												return True
										else:
											if(cart_position <= 0.004009153140941635):
												return True
											else:
												if(cart_velocity <= -0.02901155687868595):
													if(pole_angular_velocity <= 0.04918772540986538):
														if(pole_angle > -0.0018814627546817064):
															if(pole_angle <= -0.0015877680270932615):
																return True
															else:
																if(cart_velocity > -0.029236765578389168):
																	return True
												else:
													if(pole_angular_velocity <= 0.037607358768582344):
														if(cart_position <= 0.029486372135579586):
															return True
														else:
															if(cart_velocity <= -0.020390893332660198):
																return True
															else:
																if(pole_angular_velocity <= 0.02226266171783209):
																	if(cart_velocity <= 0.006061046151444316):
																		if(cart_position <= 0.09523747488856316):
																			if(cart_position <= 0.09065297618508339):
																				return True
																		else:
																			return True
																	else:
																		if(pole_angular_velocity <= 0.006514824228361249):
																			if(pole_angular_velocity <= 0.005106482421979308):
																				if(cart_velocity <= 0.04237558878958225):
																					if(cart_velocity <= 0.03718138858675957):
																						if(cart_position <= 0.09196875244379044):
																							if(pole_angular_velocity <= 0.0014506096486002207):
																								return True
																							else:
																								if(pole_angle <= -0.0017591313808225095):
																									return True
																						else:
																							if(pole_angular_velocity <= -0.0006029208598192781):
																								if(pole_angular_velocity > -0.0009860749123618007):
																									return True
																				else:
																					return True
																			else:
																				if(cart_position <= 0.0826001949608326):
																					return True
																				else:
																					if(cart_velocity <= 0.025851194746792316):
																						return True
																		else:
																			if(cart_position <= 0.04280373826622963):
																				return True
																			else:
																				if(cart_position <= 0.09743732213973999):
																					if(cart_velocity <= 0.008160527795553207):
																						if(cart_velocity > 0.007347285049036145):
																							return True
																				else:
																					return True
																else:
																	if(cart_velocity <= -0.012776792049407959):
																		if(cart_position <= 0.09717381745576859):
																			if(pole_angular_velocity <= 0.035746855661273):
																				return True
																	else:
																		if(pole_angular_velocity <= 0.036909256130456924):
																			if(cart_position <= 0.044387754052877426):
																				if(pole_angular_velocity <= 0.025392592884600163):
																					return True
																			else:
																				if(pole_angle <= -0.0018312832107767463):
																					if(pole_angle > -0.0018383261049166322):
																						return True
																		else:
																			if(pole_angular_velocity <= 0.03741239756345749):
																				return True
													else:
														if(pole_angular_velocity <= 0.04899458773434162):
															if(cart_velocity <= -0.025336971506476402):
																if(pole_angular_velocity <= 0.04110449180006981):
																	if(pole_angle > -0.0015766200376674533):
																		return True
															else:
																if(cart_position <= 0.049203408882021904):
																	if(cart_position > 0.04599659517407417):
																		return True
														else:
															if(cart_velocity <= -0.00534153962507844):
																return True
									else:
										if(pole_angular_velocity <= 0.03780934400856495):
											if(cart_velocity <= -0.007132049184292555):
												if(pole_angular_velocity <= 0.029285434633493423):
													return True
												else:
													if(cart_velocity <= -0.019250383600592613):
														if(cart_position > 0.1001967191696167):
															if(cart_position <= 0.10343831777572632):
																if(cart_position <= 0.10310786589980125):
																	return True
																else:
																	if(cart_position > 0.1032164990901947):
																		return True
													else:
														if(pole_angular_velocity <= 0.0299637820571661):
															if(cart_velocity <= -0.014624059200286865):
																return True
											else:
												if(pole_angular_velocity <= 0.017269905656576157):
													if(pole_angular_velocity <= 0.013039265759289265):
														return True
													else:
														if(pole_angular_velocity > 0.015218986663967371):
															return True
										else:
											if(cart_velocity <= -0.03146792948246002):
												if(cart_position <= 0.10243075713515282):
													return True
											else:
												if(pole_angle <= -0.0017940482357516885):
													if(cart_velocity <= -0.027973808348178864):
														return True
								else:
									if(pole_angular_velocity <= -0.002346172113902867):
										if(pole_angular_velocity <= -0.0026357659371569753):
											if(pole_angle <= -0.0011918052332475781):
												return True
										else:
											return True
									else:
										if(pole_angle <= -0.0007884819933678955):
											if(cart_position <= 0.10288223624229431):
												if(cart_position <= 0.020486188121140003):
													if(cart_velocity <= 0.031239002011716366):
														return True
												else:
													if(cart_velocity <= -0.030336351133883):
														if(pole_angle <= -0.0012401111307553947):
															return True
														else:
															if(cart_position <= 0.09017842262983322):
																if(cart_position > 0.08873986452817917):
																	return True
													else:
														if(pole_angular_velocity <= 0.004391716094687581):
															if(cart_velocity <= 0.017962940968573093):
																return True
															else:
																if(pole_angular_velocity <= 0.0018266490078531206):
																	if(pole_angular_velocity <= 0.00087622000137344):
																		if(pole_angle <= -0.001108424155972898):
																			if(pole_angle > -0.001150874188169837):
																				return True
																	else:
																		if(cart_velocity > 0.02467699721455574):
																			return True
														else:
															if(pole_angle <= -0.0008135005482472479):
																if(pole_angle <= -0.0012278641224838793):
																	if(pole_angle <= -0.0012293452164158225):
																		if(cart_position > 0.10102405771613121):
																			if(cart_position <= 0.10104134678840637):
																				return True
																	else:
																		return True
															else:
																if(pole_angle <= -0.0008071023039519787):
																	return True
											else:
												if(pole_angular_velocity <= 0.026793353259563446):
													if(pole_angle <= -0.0011783482041209936):
														return True
													else:
														if(cart_velocity <= -0.011108689941465855):
															return True
										else:
											return True
						else:
							if(cart_position <= 0.021882755681872368):
								if(pole_angle <= -0.0008649779192637652):
									if(cart_velocity <= 0.008252863772213459):
										if(pole_angular_velocity <= 0.060896722599864006):
											return True
										else:
											if(cart_velocity <= -0.02139565721154213):
												return True
											else:
												if(cart_position <= 0.006778558250516653):
													if(pole_angular_velocity <= 0.0832710787653923):
														return True
												else:
													if(cart_position > 0.02146603725850582):
														return True
									else:
										if(cart_position <= -0.015297706238925457):
											if(pole_angle <= -0.0011868292349390686):
												return True
								else:
									return True
							else:
								if(pole_angular_velocity <= 0.051036763936281204):
									if(pole_angular_velocity <= 0.05101337097585201):
										if(pole_angle <= -0.0018249309505335987):
											if(pole_angle > -0.0018475850811228156):
												return True
									else:
										return True
								else:
									if(cart_position <= 0.09769611060619354):
										if(cart_position <= 0.04073875956237316):
											if(cart_position > 0.040255120024085045):
												return True
									else:
										if(cart_position <= 0.09795217588543892):
											return True
										else:
											if(pole_angular_velocity > 0.054765574634075165):
												if(pole_angular_velocity <= 0.055088818073272705):
													return True
					else:
						if(pole_angular_velocity <= 0.028850995004177094):
							if(pole_angle <= -0.0012334667262621224):
								if(cart_velocity <= 0.0023034142795950174):
									if(cart_position <= 0.15296725183725357):
										if(pole_angular_velocity <= 0.018301178701221943):
											if(cart_position <= 0.12618663161993027):
												if(cart_velocity <= -0.001968914526514709):
													if(cart_position <= 0.10727351158857346):
														if(cart_position <= 0.10717272385954857):
															return True
													else:
														return True
												else:
													if(cart_velocity > -0.0018665562965907156):
														if(pole_angular_velocity <= 0.01370904827490449):
															if(pole_angle <= -0.0012670537689700723):
																return True
															else:
																if(pole_angle > -0.0012523329933173954):
																	return True
														else:
															if(pole_angle > -0.0016023728530853987):
																return True
											else:
												if(cart_velocity <= -0.018275631591677666):
													return True
												else:
													if(pole_angular_velocity <= 0.007243889616802335):
														if(cart_position <= 0.13564038276672363):
															return True
										else:
											if(cart_velocity <= -0.012257265392690897):
												if(pole_angular_velocity <= 0.027718016877770424):
													if(cart_position <= 0.14880792796611786):
														if(cart_position <= 0.13365760445594788):
															if(pole_angle <= -0.001474771008361131):
																return True
															else:
																if(pole_angle > -0.0014695521094836295):
																	if(cart_velocity <= -0.014401994179934263):
																		return True
																	else:
																		if(pole_angular_velocity <= 0.02309029921889305):
																			return True
														else:
															if(cart_velocity <= -0.03610582835972309):
																return True
												else:
													if(cart_position <= 0.10609414055943489):
														return True
													else:
														if(pole_angular_velocity > 0.028338276781141758):
															return True
											else:
												if(pole_angular_velocity <= 0.01994726900011301):
													if(pole_angle <= -0.001530730165541172):
														return True
													else:
														if(cart_velocity <= -0.009864767082035542):
															if(cart_position <= 0.11114397644996643):
																return True
												else:
													if(cart_velocity <= -0.011709703598171473):
														if(cart_velocity <= -0.011744209099560976):
															if(cart_position <= 0.10529864951968193):
																return True
														else:
															return True
								else:
									if(pole_angular_velocity <= 0.001319164759479463):
										if(cart_velocity <= 0.009893775451928377):
											if(cart_position <= 0.1268785148859024):
												return True
										else:
											if(pole_angular_velocity <= -0.000737299065804109):
												if(cart_velocity <= 0.01833813264966011):
													return True
												else:
													if(cart_position <= 0.10664916411042213):
														return True
									else:
										if(cart_position <= 0.10558238625526428):
											return True
										else:
											if(cart_velocity <= 0.003539323224686086):
												if(cart_velocity > 0.0032996053341776133):
													return True
							else:
								if(pole_angular_velocity <= -1.7234428014489822e-05):
									if(cart_velocity <= 0.012621663976460695):
										if(cart_velocity <= 0.008312990423291922):
											return True
										else:
											if(cart_position <= 0.11518201231956482):
												return True
									else:
										if(pole_angle > -0.0009167112875729799):
											return True
								else:
									if(cart_velocity <= 0.0028134946478530765):
										if(pole_angular_velocity <= 0.021130680106580257):
											if(cart_velocity <= -0.010847708210349083):
												if(cart_position <= 0.1311185508966446):
													if(pole_angle <= -0.0008670739771332592):
														return True
													else:
														if(cart_velocity <= -0.011934771202504635):
															return True
												else:
													if(cart_velocity <= -0.0374488215893507):
														return True
													else:
														if(pole_angular_velocity <= 0.006144134560599923):
															return True
														else:
															if(cart_position <= 0.14662156254053116):
																if(cart_velocity <= -0.025750642642378807):
																	return True
											else:
												if(pole_angular_velocity <= 0.015601805411279202):
													if(cart_position <= 0.11229702830314636):
														if(cart_velocity <= -0.0019663007115013897):
															if(pole_angular_velocity <= 0.015253538265824318):
																if(cart_position <= 0.11208513379096985):
																	return True
																else:
																	if(cart_velocity <= -0.005063122604042292):
																		return True
															else:
																if(pole_angle <= -0.0010283809097018093):
																	return True
														else:
															if(pole_angle <= -0.0010301914880983531):
																if(pole_angular_velocity <= 0.011302157305181026):
																	return True
													else:
														if(pole_angular_velocity <= 0.0011481966939754784):
															return True
														else:
															if(cart_velocity <= -0.008820691145956516):
																if(cart_position <= 0.13301662355661392):
																	return True
															else:
																if(cart_position <= 0.1172645352780819):
																	if(pole_angular_velocity <= 0.011808987241238356):
																		if(cart_position > 0.11252396553754807):
																			return True
												else:
													if(pole_angle <= -0.0011256244033575058):
														if(pole_angular_velocity > 0.017829335294663906):
															return True
													else:
														if(cart_velocity > -0.005424595205113292):
															if(pole_angle > -0.0011079993564635515):
																return True
										else:
											if(cart_velocity <= -0.024290835484862328):
												if(cart_position <= 0.13444622606039047):
													return True
												else:
													if(cart_velocity <= -0.04151551052927971):
														return True
											else:
												if(cart_position <= 0.10587016493082047):
													if(cart_velocity <= -0.01637209951877594):
														return True
													else:
														if(cart_position <= 0.10444042831659317):
															if(pole_angle <= -0.0010785507038235664):
																return True
															else:
																if(cart_velocity > -0.011727487202733755):
																	return True
									else:
										if(pole_angular_velocity <= 0.0011975803645327687):
											if(cart_position <= 0.11044373363256454):
												return True
											else:
												if(cart_velocity <= 0.0060984662268310785):
													if(pole_angle <= -0.0009056646085809916):
														return True
						else:
							if(cart_position <= 0.10784570872783661):
								if(pole_angle <= -0.001445499190595001):
									if(cart_velocity <= -0.028178147971630096):
										if(pole_angular_velocity <= 0.05135905370116234):
											if(cart_position <= 0.1067449264228344):
												if(pole_angular_velocity <= 0.04315408132970333):
													return True
												else:
													if(cart_velocity <= -0.039569590240716934):
														return True
													else:
														if(pole_angle <= -0.001830480294302106):
															return True
									else:
										if(cart_velocity <= -0.019301521591842175):
											if(pole_angular_velocity <= 0.032239438965916634):
												return True
											else:
												if(cart_velocity <= -0.02425611112266779):
													if(pole_angular_velocity <= 0.035481346771121025):
														return True
								else:
									if(pole_angular_velocity <= 0.030785996466875076):
										if(pole_angle <= -0.001035229186527431):
											return True
									else:
										if(cart_velocity <= -0.03744406998157501):
											if(pole_angular_velocity <= 0.04403851740062237):
												return True
							else:
								if(cart_position <= 0.1311805248260498):
									if(pole_angle <= -0.0010496255126781762):
										if(pole_angular_velocity <= 0.052206315100193024):
											if(cart_velocity <= -0.03912759944796562):
												if(pole_angular_velocity <= 0.049101509153842926):
													if(pole_angle <= -0.001267004234250635):
														return True
													else:
														if(pole_angular_velocity <= 0.041658032685518265):
															return True
												else:
													if(pole_angular_velocity > 0.05062248185276985):
														return True
											else:
												if(cart_position <= 0.11094875633716583):
													if(pole_angular_velocity <= 0.03622639738023281):
														return True
													else:
														if(cart_position > 0.1098686158657074):
															return True
												else:
													if(pole_angular_velocity <= 0.03134366311132908):
														if(pole_angular_velocity > 0.029076671227812767):
															return True
													else:
														if(pole_angle <= -0.0017356346943415701):
															return True
									else:
										if(cart_velocity <= -0.03338658809661865):
											if(pole_angle <= -0.0008792757580522448):
												if(pole_angle <= -0.0009288129513151944):
													if(cart_velocity <= -0.045310480520129204):
														if(cart_position > 0.11335725709795952):
															return True
													else:
														if(cart_velocity > -0.03519907593727112):
															return True
												else:
													return True
											else:
												if(cart_position <= 0.1129816360771656):
													if(pole_angle <= -0.0008180394943337888):
														return True
								else:
									if(cart_position <= 0.13680364936590195):
										if(pole_angle <= -0.0014759264886379242):
											return True
				else:
					if(pole_angular_velocity <= 0.00011656379865598865):
						if(pole_angle <= 0.0014046219293959439):
							if(pole_angular_velocity <= -0.0013126744888722897):
								if(cart_position <= 0.10912071913480759):
									if(cart_velocity <= 0.03494134359061718):
										if(pole_angular_velocity <= -0.0019076564349234104):
											if(pole_angle <= -0.0005796198383904994):
												return True
											else:
												if(cart_velocity <= 0.021095587871968746):
													if(pole_angle <= 6.516316807392286e-05):
														return True
													else:
														if(pole_angular_velocity > -0.002936433651484549):
															if(pole_angular_velocity <= -0.0025478367460891604):
																return True
															else:
																if(pole_angular_velocity > -0.0022695371881127357):
																	if(pole_angle <= 0.0007893498986959457):
																		return True
												else:
													if(cart_position <= 0.08175721019506454):
														return True
										else:
											if(pole_angular_velocity > -0.0013965822290629148):
												return True
								else:
									if(cart_velocity <= 0.012231000699102879):
										if(cart_velocity <= 0.0028560024220496416):
											if(pole_angle <= 0.0006426000909414142):
												return True
											else:
												if(pole_angle > 0.0006855639221612364):
													if(pole_angular_velocity <= -0.002650237875059247):
														return True
													else:
														if(pole_angular_velocity > -0.002602491294965148):
															if(pole_angle <= 0.0007846708176657557):
																if(cart_position <= 0.11422234028577805):
																	return True
															else:
																if(pole_angle <= 0.0012457349221222103):
																	return True
																else:
																	if(pole_angle > 0.001272618887014687):
																		return True
										else:
											if(pole_angle <= 4.858857391809579e-05):
												if(cart_velocity > 0.0030486909672617912):
													if(pole_angular_velocity <= -0.0013843034394085407):
														return True
													else:
														if(cart_velocity > 0.006210948806256056):
															return True
											else:
												if(pole_angular_velocity <= -0.0017744620563462377):
													if(pole_angle <= 0.0007143965922296047):
														if(cart_velocity <= 0.0086621786467731):
															if(pole_angle > 8.351049473276362e-05):
																return True
													else:
														if(pole_angular_velocity <= -0.002882379572838545):
															if(pole_angle > 0.0009296474454458803):
																return True
												else:
													if(pole_angle > 0.0008878469816409051):
														return True
							else:
								if(cart_position <= 0.11633293703198433):
									if(pole_angle <= 0.0006044152250979096):
										if(cart_velocity <= 0.009170528035610914):
											if(cart_position <= 0.11557662859559059):
												if(cart_position <= 0.10867180675268173):
													return True
												else:
													if(cart_velocity <= 0.003615153837017715):
														if(pole_angle <= 0.0003159066109219566):
															return True
														else:
															if(cart_position <= 0.11312809586524963):
																return True
													else:
														if(pole_angle <= -0.0002454250934533775):
															return True
										else:
											if(pole_angular_velocity <= -0.0012714089243672788):
												return True
											else:
												if(cart_velocity <= 0.034594353288412094):
													if(pole_angular_velocity <= -0.001047052734065801):
														if(pole_angular_velocity > -0.001088727731257677):
															return True
												else:
													return True
									else:
										if(cart_velocity <= 0.0003126727824565023):
											return True
										else:
											if(cart_position <= 0.10458275303244591):
												if(cart_velocity <= 0.010462868493050337):
													return True
								else:
									if(cart_velocity > -0.01572753395885229):
										if(pole_angle <= -0.00011410067236283794):
											return True
										else:
											if(cart_position <= 0.12216505780816078):
												if(cart_position <= 0.11717672273516655):
													if(cart_velocity > 0.0032584171276539564):
														return True
											else:
												if(pole_angle <= 0.0007546172419097275):
													return True
												else:
													if(pole_angle > 0.0010257670655846596):
														return True
						else:
							if(pole_angle <= 0.0020128984469920397):
								if(cart_velocity <= -0.0006849628989584744):
									if(pole_angular_velocity <= -0.0016170403105206788):
										return True
									else:
										if(cart_velocity <= -0.008498610462993383):
											if(pole_angular_velocity > -0.0015521777095273137):
												if(pole_angle <= 0.0017607356421649456):
													return True
												else:
													if(cart_position <= 0.12065679207444191):
														return True
										else:
											if(cart_position <= 0.10997501388192177):
												return True
								else:
									if(pole_angular_velocity <= -0.002863595844246447):
										if(cart_velocity <= 0.002624545944854617):
											if(pole_angular_velocity > -0.0032101585529744625):
												return True
									else:
										if(pole_angular_velocity <= -0.00243143190164119):
											if(pole_angle <= 0.0015904402825981379):
												if(cart_velocity <= 0.012860929477028549):
													return True
										else:
											if(cart_position <= 0.10794447734951973):
												if(cart_position <= 0.10791714861989021):
													if(pole_angular_velocity > -0.00029067623836454004):
														if(cart_position > 0.10144547000527382):
															return True
												else:
													return True
							else:
								if(cart_position <= -0.023050916381180286):
									if(pole_angle <= 0.011909057851880789):
										return True
									else:
										if(cart_velocity <= -0.011730320751667023):
											return True
								else:
									if(cart_velocity <= -0.012443675193935633):
										if(pole_angle <= 0.00549486477393657):
											return True
									else:
										if(cart_position <= 0.052839310839772224):
											if(pole_angle <= 0.009553732350468636):
												if(pole_angular_velocity > -0.0021128241787664592):
													return True
										else:
											if(pole_angle <= 0.0024147351505234838):
												if(pole_angle <= 0.002413004171103239):
													if(pole_angular_velocity <= -0.002986675826832652):
														if(cart_velocity <= -0.0012777462834492326):
															return True
														else:
															if(pole_angle <= 0.002096132026053965):
																if(cart_position > 0.10793261975049973):
																	return True
													else:
														if(cart_velocity <= -0.0012960672611370683):
															if(cart_position <= 0.10999847203493118):
																if(cart_position > 0.10990546643733978):
																	return True
															else:
																if(pole_angle > 0.0022678133100271225):
																	if(pole_angle <= 0.002298617851920426):
																		return True
												else:
													return True
					else:
						if(cart_position <= 0.03744620829820633):
							if(pole_angular_velocity <= 0.028603863902390003):
								if(pole_angle <= 0.007223641499876976):
									if(cart_position <= 0.022547676227986813):
										if(pole_angular_velocity <= 0.024989493191242218):
											if(cart_position <= 0.020183347165584564):
												return True
											else:
												if(pole_angle <= 0.0035149898612871766):
													return True
										else:
											if(pole_angular_velocity > 0.026486787013709545):
												if(cart_position <= 0.009320298908278346):
													return True
												else:
													if(pole_angular_velocity > 0.028086112812161446):
														return True
									else:
										if(cart_velocity <= 0.03422785364091396):
											if(pole_angle <= 0.005311391549184918):
												if(pole_angular_velocity <= 0.02720454055815935):
													return True
											else:
												if(cart_velocity <= 0.00432066572830081):
													return True
										else:
											if(pole_angle <= 7.858108801883645e-06):
												if(pole_angular_velocity <= 0.022670547477900982):
													return True
								else:
									if(cart_velocity <= -0.009203615598380566):
										if(pole_angle <= 0.021133159287273884):
											if(pole_angular_velocity <= 0.013964120764285326):
												if(cart_velocity <= -0.011173926759511232):
													return True
												else:
													if(pole_angle <= 0.018868078477680683):
														return True
											else:
												if(pole_angle <= 0.013876103330403566):
													return True
												else:
													if(cart_position <= -0.037398528307676315):
														return True
													else:
														if(cart_velocity <= -0.03333231061697006):
															return True
										else:
											if(pole_angular_velocity <= 0.0006739983218722045):
												return True
											else:
												if(pole_angle <= 0.0298049533739686):
													if(cart_position <= -0.03493065573275089):
														if(pole_angular_velocity <= 0.022624134086072445):
															if(cart_velocity <= -0.028737761080265045):
																return True
															else:
																if(pole_angular_velocity <= 0.008926928043365479):
																	return True
																else:
																	if(cart_velocity > -0.01293010264635086):
																		return True
													else:
														if(pole_angular_velocity <= 0.004017441533505917):
															if(cart_position <= -0.020138883497565985):
																return True
									else:
										if(pole_angle <= 0.013879377394914627):
											if(pole_angular_velocity <= 0.012472054455429316):
												if(cart_position <= -0.013600466307252645):
													if(cart_velocity <= 0.04411490820348263):
														return True
												else:
													if(cart_velocity <= 0.014767801854759455):
														if(pole_angular_velocity > 0.002872264012694359):
															if(pole_angle <= 0.012523082550615072):
																return True
															else:
																if(pole_angular_velocity <= 0.011774174869060516):
																	return True
											else:
												if(cart_velocity <= 0.016205383464694023):
													if(pole_angle <= 0.008847807999700308):
														return True
													else:
														if(cart_position <= 0.007426499854773283):
															if(cart_velocity <= 0.005745204398408532):
																return True
												else:
													if(cart_position <= -0.04422226920723915):
														return True
										else:
											if(cart_position <= -0.039153097197413445):
												if(cart_position <= -0.040539106354117393):
													if(pole_angle <= 0.016375376842916012):
														if(cart_velocity <= 0.03534078411757946):
															return True
													else:
														if(cart_position > -0.042980536818504333):
															if(pole_angular_velocity <= 0.011228279210627079):
																return True
												else:
													return True
							else:
								if(pole_angular_velocity <= 0.04545587673783302):
									if(pole_angle <= 0.005252976668998599):
										if(cart_velocity <= 0.017389610409736633):
											if(cart_position <= 0.03217468969523907):
												return True
											else:
												if(pole_angle <= 0.003461131011135876):
													return True
										else:
											if(cart_position <= -0.0007413270359393209):
												if(cart_position <= -0.004173326073214412):
													if(cart_position <= -0.019001985900104046):
														if(cart_velocity <= 0.042191898450255394):
															return True
														else:
															if(pole_angular_velocity <= 0.03948473930358887):
																return True
												else:
													return True
											else:
												if(cart_velocity <= 0.02857175190001726):
													if(pole_angle <= 0.0006503885961137712):
														if(cart_position <= 0.031515782698988914):
															return True
													else:
														if(cart_position <= 0.012488130945712328):
															if(pole_angle <= 0.0029251836240291595):
																if(pole_angular_velocity <= 0.042180897668004036):
																	return True
												else:
													if(pole_angle <= 0.00038244931783992797):
														if(pole_angle > 0.00037047098157927394):
															return True
									else:
										if(cart_velocity <= -0.03896486945450306):
											if(pole_angle <= 0.012712803669273853):
												return True
											else:
												if(cart_velocity <= -0.03981430642306805):
													if(cart_position <= -0.06654520332813263):
														if(pole_angle <= 0.02980213426053524):
															return True
													else:
														if(pole_angle <= 0.017600279301404953):
															if(pole_angle > 0.017476043663918972):
																return True
												else:
													return True
										else:
											if(pole_angular_velocity <= 0.045427948236465454):
												if(cart_position <= -0.01211881497874856):
													if(pole_angle <= 0.009831323754042387):
														if(cart_velocity <= 0.026457604952156544):
															return True
													else:
														if(pole_angle <= 0.01586669683456421):
															if(pole_angle > 0.01519037177786231):
																return True
												else:
													if(cart_velocity <= -0.011758758220821619):
														if(pole_angle <= 0.011335297953337431):
															if(cart_position <= 0.025587580166757107):
																return True
											else:
												return True
								else:
									if(cart_position <= 0.037373701110482216):
										if(pole_angle <= 0.002475949004292488):
											if(cart_velocity <= -0.027158853597939014):
												if(cart_position <= 0.03451221063733101):
													if(pole_angle <= 0.0019347769557498395):
														return True
													else:
														if(pole_angular_velocity > 0.08234888687729836):
															return True
											else:
												if(cart_position <= -0.03727083466947079):
													if(cart_velocity <= 0.03526227921247482):
														return True
													else:
														if(cart_velocity > 0.04048801213502884):
															return True
												else:
													if(pole_angle <= 0.002455417881719768):
														if(cart_velocity <= 0.0002601039013825357):
															if(pole_angular_velocity <= 0.062402332201600075):
																if(pole_angle <= 0.0019825262716040015):
																	return True
															else:
																if(cart_position <= 0.010726132430136204):
																	if(cart_velocity <= -0.010564237833023071):
																		if(pole_angular_velocity <= 0.08154378831386566):
																			return True
														else:
															if(cart_position <= -0.024799708276987076):
																if(cart_position > -0.026810452342033386):
																	return True
															else:
																if(pole_angle <= 0.002245826297439635):
																	if(pole_angular_velocity <= 0.04872738942503929):
																		if(cart_velocity <= 0.011678750859573483):
																			return True
																else:
																	if(pole_angle <= 0.002276829443871975):
																		return True
													else:
														return True
										else:
											if(cart_velocity <= -0.011321645695716143):
												if(cart_velocity <= -0.011436357162892818):
													if(pole_angular_velocity <= 0.056732818484306335):
														if(pole_angle <= 0.00998326065018773):
															if(cart_position <= 0.02840342652052641):
																if(cart_velocity <= -0.013181937858462334):
																	if(cart_position <= 0.010660213883966208):
																		if(cart_position <= -0.0043516934383660555):
																			if(pole_angle > 0.009523905348032713):
																				return True
																		else:
																			return True
																	else:
																		if(cart_velocity <= -0.0331419613212347):
																			return True
														else:
															if(pole_angle <= 0.017309832386672497):
																if(cart_position <= -0.023131665773689747):
																	if(cart_velocity <= -0.020813428796827793):
																		return True
													else:
														if(pole_angle <= 0.008263629861176014):
															if(cart_position <= -0.03314007446169853):
																return True
															else:
																if(pole_angular_velocity <= 0.0608696136623621):
																	if(pole_angular_velocity > 0.060008347034454346):
																		return True
																else:
																	if(cart_position <= -0.014149251859635115):
																		if(cart_velocity <= -0.026385577395558357):
																			return True
												else:
													return True
									else:
										return True
						else:
							if(pole_angle <= -0.00044875794264953583):
								if(cart_position <= 0.10647141560912132):
									if(pole_angle <= -0.0004501455696299672):
										if(pole_angular_velocity <= 0.0003389572666492313):
											if(cart_position <= 0.09727071225643158):
												return True
										else:
											if(cart_position <= 0.04411937855184078):
												if(cart_position <= 0.043677445501089096):
													if(pole_angular_velocity <= 0.018740349914878607):
														return True
												else:
													return True
											else:
												if(cart_position <= 0.05311425402760506):
													if(cart_position > 0.05300283804535866):
														return True
												else:
													if(cart_position > 0.09355266392230988):
														if(cart_position <= 0.09362438693642616):
															return True
														else:
															if(pole_angular_velocity <= 0.018854745663702488):
																if(pole_angular_velocity > 0.018545731902122498):
																	return True
															else:
																if(cart_velocity <= -0.043273795396089554):
																	if(cart_velocity > -0.04344455525279045):
																		return True
																else:
																	if(pole_angle > -0.0005090945633128285):
																		if(pole_angle <= -0.0005051517218817025):
																			return True
									else:
										return True
								else:
									if(cart_position <= 0.11999865621328354):
										if(pole_angular_velocity <= 0.02011930476874113):
											if(cart_velocity <= -0.005656035616993904):
												if(pole_angular_velocity <= 0.01433260552585125):
													return True
												else:
													if(cart_velocity <= -0.009932672139257193):
														if(cart_position <= 0.11107796803116798):
															return True
														else:
															if(pole_angular_velocity <= 0.016666874289512634):
																if(cart_velocity <= -0.013063080608844757):
																	return True
											else:
												if(cart_position <= 0.10751760005950928):
													return True
												else:
													if(cart_velocity <= 0.0016663995338603854):
														if(pole_angular_velocity <= 0.00823619682341814):
															return True
														else:
															if(pole_angle > -0.0005287868843879551):
																if(pole_angle <= -0.0005193726101424545):
																	return True
										else:
											if(pole_angle <= -0.0007401364855468273):
												if(pole_angle > -0.0007542782987002283):
													if(cart_position > 0.10830911248922348):
														return True
											else:
												if(cart_position <= 0.10693642124533653):
													if(pole_angular_velocity <= 0.03277997951954603):
														return True
												else:
													if(cart_velocity <= -0.028071196749806404):
														if(cart_velocity > -0.02926174458116293):
															return True
									else:
										if(cart_position <= 0.1303803250193596):
											if(cart_velocity <= -0.016443011350929737):
												return True
											else:
												if(pole_angular_velocity <= 0.00309447234030813):
													if(cart_velocity <= -0.002140330267138779):
														return True
										else:
											if(pole_angular_velocity <= 0.02156649436801672):
												if(cart_velocity <= -0.029280034825205803):
													if(cart_position <= 0.1501598134636879):
														return True
													else:
														if(pole_angular_velocity <= 0.01531897159293294):
															return True
												else:
													if(pole_angular_velocity <= 0.003058918286114931):
														return True
													else:
														if(pole_angle <= -0.0007110483420547098):
															return True
														else:
															if(pole_angle > -0.000452124688308686):
																return True
							else:
								if(cart_position <= 0.11884931474924088):
									if(cart_position <= 0.11044377833604813):
										if(cart_position <= 0.04647211357951164):
											if(pole_angular_velocity <= 0.011097743175923824):
												if(pole_angle > 0.0043534968281164765):
													if(cart_velocity <= -0.0011686317739076912):
														if(pole_angular_velocity > 0.009869765024632215):
															return True
													else:
														return True
											else:
												if(cart_position <= 0.046401720494031906):
													if(cart_velocity <= -0.03406781889498234):
														if(pole_angular_velocity <= 0.05642230436205864):
															return True
													else:
														if(pole_angular_velocity <= 0.02705360110849142):
															if(cart_position <= 0.04574187844991684):
																if(pole_angular_velocity > 0.02692595962435007):
																	return True
															else:
																return True
														else:
															if(pole_angle <= -9.888902422972023e-05):
																if(pole_angle > -0.00011269825699855573):
																	return True
												else:
													return True
										else:
											if(pole_angular_velocity <= 0.0017676502466201782):
												if(pole_angular_velocity <= 0.0017621386796236038):
													if(pole_angle <= 0.0008880606619641185):
														if(pole_angle > 0.0008538564434275031):
															return True
												else:
													return True
											else:
												if(pole_angle <= -0.0002321987849427387):
													if(pole_angle <= -0.00023289088858291507):
														if(cart_position > 0.1080772839486599):
															if(cart_position <= 0.10820045694708824):
																return True
															else:
																if(cart_velocity <= -0.01437301654368639):
																	if(pole_angular_velocity <= 0.020520403049886227):
																		return True
													else:
														if(pole_angular_velocity <= 0.037336152512580156):
															return True
												else:
													if(cart_position <= 0.05854922719299793):
														if(cart_position <= 0.05853167362511158):
															if(cart_position <= 0.058401744812726974):
																if(pole_angle <= 0.0002699494216358289):
																	if(pole_angle > 0.0002577486739028245):
																		return True
															else:
																if(cart_position <= 0.058410828933119774):
																	return True
														else:
															return True
									else:
										if(cart_position <= 0.11044539883732796):
											return True
										else:
											if(pole_angle <= 0.0006637126789428294):
												if(pole_angular_velocity <= 0.00873485766351223):
													if(cart_velocity <= -0.0013656598748639226):
														if(cart_position <= 0.11402270570397377):
															if(cart_velocity <= -0.003252687049098313):
																return True
															else:
																if(pole_angular_velocity <= 0.004430821631103754):
																	return True
																else:
																	if(pole_angle <= -9.744718045112677e-05):
																		return True
													else:
														if(pole_angular_velocity <= 0.000186474688234739):
															return True
														else:
															if(cart_velocity <= 0.00031198924989439547):
																if(cart_velocity <= -0.0007031994173303246):
																	if(pole_angle <= -0.00014767326138098724):
																		if(cart_velocity <= -0.0009257671190425754):
																			return True
																else:
																	return True
															else:
																if(pole_angular_velocity <= 0.0006923042528796941):
																	if(pole_angle <= 7.417183223878965e-05):
																		if(cart_velocity <= 0.002244859002530575):
																			return True
												else:
													if(pole_angle <= -0.0003231718728784472):
														if(pole_angle > -0.0003434540412854403):
															return True
											else:
												if(pole_angle <= 0.0011597705888561904):
													if(pole_angle <= 0.0011483965208753943):
														if(pole_angular_velocity <= 0.0016925145173445344):
															if(pole_angular_velocity > 0.001671956793870777):
																return True
													else:
														return True
								else:
									if(pole_angle <= 0.0008279895700979978):
										if(pole_angular_velocity <= 0.001394132210407406):
											if(cart_velocity <= -0.006811932194977999):
												if(cart_position <= 0.1270744502544403):
													return True
												else:
													if(cart_position > 0.12977157533168793):
														return True
										else:
											if(pole_angle <= -0.00025717433891259134):
												if(pole_angular_velocity <= 0.03397038020193577):
													if(cart_position <= 0.13244838267564774):
														if(pole_angle <= -0.00031231113825924695):
															if(cart_velocity <= -0.021926934830844402):
																if(pole_angle <= -0.0003336476656841114):
																	if(cart_position <= 0.13072174042463303):
																		return True
														else:
															return True
													else:
														if(cart_position <= 0.15664062649011612):
															if(cart_position > 0.14248404651880264):
																if(cart_position <= 0.1431485041975975):
																	return True
														else:
															return True
											else:
												if(pole_angular_velocity <= 0.022739330306649208):
													if(cart_velocity <= -0.015684359706938267):
														if(pole_angular_velocity <= 0.00652582454495132):
															if(pole_angle <= 0.0007726058829575777):
																return True
															else:
																if(cart_velocity > -0.01934719644486904):
																	return True
														else:
															if(cart_position <= 0.12687863409519196):
																if(cart_velocity <= -0.019795864820480347):
																	if(cart_position <= 0.12409746274352074):
																		return True
																	else:
																		if(cart_position > 0.12632184475660324):
																			return True
															else:
																if(pole_angular_velocity <= 0.021735506132245064):
																	if(cart_velocity <= -0.046457648277282715):
																		return True
																	else:
																		if(pole_angle <= -4.205279856250854e-05):
																			if(pole_angle > -0.00010767201820272021):
																				return True
																else:
																	if(pole_angular_velocity <= 0.02223129291087389):
																		return True
																	else:
																		if(pole_angle <= 0.00038336556463036686):
																			return True
												else:
													if(pole_angle <= 8.27543881314341e-05):
														if(pole_angle <= 7.161231224017683e-05):
															if(cart_velocity <= -0.04769342206418514):
																if(cart_velocity > -0.04940928891301155):
																	return True
														else:
															return True
									else:
										if(pole_angular_velocity <= 0.0034605349646881223):
											if(cart_position <= 0.13227352499961853):
												if(pole_angle <= 0.00100948684848845):
													if(cart_position <= 0.12141276523470879):
														return True
											else:
												if(cart_velocity <= -0.018069928511977196):
													return True
		else:
			if(pole_angle <= -0.021388783119618893):
				if(pole_angular_velocity <= 0.327855721116066):
					if(pole_angle <= -0.02184130623936653):
						return True
					else:
						if(pole_angular_velocity <= 0.26855144649744034):
							return True
				else:
					if(pole_angle <= -0.04237775877118111):
						return True
					else:
						if(pole_angular_velocity <= 0.5404111444950104):
							if(cart_velocity <= -0.4140506386756897):
								return True
			else:
				if(pole_angular_velocity <= 0.10921763256192207):
					if(pole_angle <= -0.004830293590202928):
						if(cart_position <= 0.07407906651496887):
							if(pole_angle <= -0.0059919406194239855):
								if(cart_velocity <= 0.011404153890907764):
									if(cart_velocity <= -0.031687356531620026):
										if(cart_velocity <= -0.052826959639787674):
											if(cart_velocity <= -0.05297384411096573):
												return True
										else:
											return True
									else:
										if(cart_position <= 0.05448063090443611):
											if(pole_angle <= -0.007220894331112504):
												if(cart_velocity <= 0.0061305973213166):
													return True
												else:
													if(pole_angular_velocity <= 0.09347179159522057):
														return True
											else:
												if(pole_angular_velocity <= 0.10246559605002403):
													if(cart_velocity <= -0.023156246170401573):
														return True
													else:
														if(cart_position <= 0.02788728103041649):
															if(pole_angle > -0.007100951625034213):
																return True
														else:
															if(pole_angle <= -0.0070207128301262856):
																return True
										else:
											if(cart_velocity <= -0.028760849498212337):
												if(cart_position > 0.058511532843112946):
													return True
							else:
								if(pole_angle <= -0.004922133171930909):
									if(cart_position <= 0.06877182051539421):
										if(pole_angular_velocity <= 0.08694418147206306):
											return True
										else:
											if(cart_velocity <= -0.024376720190048218):
												if(pole_angular_velocity <= 0.09613070636987686):
													if(pole_angle <= -0.005323514342308044):
														return True
													else:
														if(cart_velocity > -0.02963393460959196):
															return True
											else:
												if(cart_position <= 0.01656624861061573):
													if(cart_velocity <= -0.007760149601381272):
														return True
									else:
										return True
								else:
									if(cart_velocity <= -0.039027364924550056):
										return True
									else:
										if(cart_position <= 0.019793258048593998):
											return True
						else:
							if(pole_angular_velocity <= 0.08773228898644447):
								if(cart_velocity <= -0.04411998577415943):
									if(cart_position <= 0.1767510026693344):
										return True
							else:
								if(pole_angular_velocity <= 0.08908318355679512):
									if(pole_angular_velocity > 0.08892759680747986):
										return True
					else:
						if(pole_angle <= -0.004098898032680154):
							if(pole_angle <= -0.004117364762350917):
								if(cart_position <= 0.023970945738255978):
									if(pole_angle > -0.004309472627937794):
										if(cart_velocity <= -0.015758622903376818):
											return True
								else:
									if(pole_angular_velocity <= 0.08698222413659096):
										if(pole_angular_velocity > 0.08682440221309662):
											return True
							else:
								return True
						else:
							if(cart_velocity <= -0.0527329221367836):
								if(cart_velocity <= -0.052738334983587265):
									if(pole_angle <= -0.0021989975939504802):
										if(cart_velocity > -0.0530549343675375):
											return True
								else:
									return True
							else:
								if(cart_position <= -0.01086712023243308):
									if(pole_angle <= -0.0021008006297051907):
										if(cart_velocity <= 0.0008217173162847757):
											return True
									else:
										if(pole_angle <= 0.006444797618314624):
											if(cart_velocity <= -0.028871634043753147):
												if(pole_angular_velocity <= 0.10642605274915695):
													return True
								else:
									if(pole_angle <= -0.002806113217957318):
										if(pole_angle <= -0.0028127903351560235):
											if(pole_angular_velocity <= 0.08728794753551483):
												if(pole_angle <= -0.0036133729154244065):
													return True
										else:
											return True
				else:
					if(cart_position <= 0.018246727995574474):
						if(pole_angle <= -0.00702847121283412):
							if(pole_angular_velocity <= 0.25167079269886017):
								if(cart_velocity <= -0.09172099828720093):
									if(cart_velocity <= -0.15705887228250504):
										return True
									else:
										if(cart_position <= 0.0005599847063422203):
											return True
								else:
									if(cart_position <= 0.007537883473560214):
										return True
							else:
								if(pole_angular_velocity <= 0.29496653378009796):
									if(cart_velocity <= -0.18256930261850357):
										if(cart_position <= 0.005921488860622048):
											return True
										else:
											if(cart_velocity <= -0.20081758499145508):
												return True
								else:
									if(pole_angle <= -0.02040017955005169):
										if(cart_position <= -0.03799070976674557):
											return True
									else:
										if(cart_velocity <= -0.42279061675071716):
											if(pole_angle <= -0.014532058034092188):
												return True
						else:
							if(cart_velocity <= -0.2007414549589157):
								if(pole_angular_velocity <= 0.24254772067070007):
									if(pole_angle <= 0.005136593710631132):
										return True
									else:
										if(cart_position <= -0.07092519477009773):
											if(pole_angle <= 0.021209106780588627):
												return True
										else:
											if(cart_velocity > -0.20084026455879211):
												return True
								else:
									if(cart_position <= 0.016991947777569294):
										if(pole_angle <= 0.0015719927614554763):
											if(pole_angular_velocity <= 0.27247852087020874):
												if(cart_position <= -0.016833505360409617):
													return True
									else:
										return True
							else:
								if(pole_angle <= -0.004579587839543819):
									if(cart_position <= -0.05089338682591915):
										return True
									else:
										if(pole_angle > -0.005015765083953738):
											if(pole_angle <= -0.004970006411895156):
												return True
								else:
									if(pole_angle <= -0.002578179817646742):
										if(pole_angle <= -0.002614683238789439):
											if(cart_position <= -0.04009828716516495):
												return True
										else:
											return True
									else:
										if(cart_position <= -0.08213214576244354):
											if(pole_angle <= 0.01320931245572865):
												return True
					else:
						if(pole_angle <= -0.021060177125036716):
							if(cart_position > 0.029192746616899967):
								return True
						else:
							if(pole_angle <= -0.01868985779583454):
								if(pole_angular_velocity <= 0.28918273746967316):
									return True
							else:
								if(pole_angular_velocity <= 0.1168680489063263):
									if(pole_angular_velocity <= 0.11681690067052841):
										if(cart_velocity <= -0.053347691893577576):
											if(cart_position > 0.047359321266412735):
												return True
										else:
											if(cart_velocity <= -0.04849499650299549):
												if(cart_velocity <= -0.04852821119129658):
													if(cart_position <= 0.032193223014473915):
														if(cart_position > 0.03121611662209034):
															return True
												else:
													return True
									else:
										return True
								else:
									if(cart_position <= 0.024705364368855953):
										if(cart_position <= 0.024628283455967903):
											if(pole_angle <= -0.011511235032230616):
												if(pole_angle > -0.015226411167532206):
													return True
										else:
											return True
	return False

def weShould_move_right(cart_position, cart_velocity, pole_angle, pole_angular_velocity):
	if(pole_angular_velocity <= -0.003253065049648285):
		if(pole_angular_velocity <= -0.11360538005828857):
			if(pole_angular_velocity <= -0.1374693512916565):
				if(pole_angle <= 0.03329905681312084):
					if(pole_angle <= 0.019715409725904465):
						if(pole_angular_velocity <= -0.14653046429157257):
							if(pole_angle > 0.009452462196350098):
								if(cart_position <= 0.07428273558616638):
									if(pole_angle <= 0.00945691904053092):
										return True
									else:
										if(cart_position <= 0.03926258906722069):
											if(pole_angular_velocity <= -0.15556253492832184):
												if(cart_position > 0.021309946663677692):
													if(cart_position <= 0.02163386158645153):
														return True
											else:
												if(pole_angular_velocity <= -0.15500760823488235):
													return True
										else:
											if(cart_position <= 0.04036247916519642):
												if(pole_angular_velocity > -0.20706115663051605):
													return True
											else:
												if(pole_angular_velocity > -0.20100148767232895):
													if(pole_angular_velocity <= -0.1999046355485916):
														return True
													else:
														if(cart_velocity > 0.2020500972867012):
															if(cart_velocity <= 0.20310497283935547):
																return True
								else:
									return True
						else:
							if(pole_angular_velocity <= -0.1464993953704834):
								return True
							else:
								if(cart_position <= 0.15131103247404099):
									if(cart_velocity <= 0.21168674528598785):
										if(pole_angular_velocity > -0.13848137855529785):
											if(pole_angular_velocity <= -0.13844990730285645):
												return True
									else:
										if(cart_velocity <= 0.2117849364876747):
											return True
								else:
									if(pole_angle > -0.00297674658941105):
										return True
					else:
						if(pole_angular_velocity <= -0.21702878922224045):
							if(cart_position > 0.01409118203446269):
								if(cart_position <= 0.014398430939763784):
									return True
								else:
									if(pole_angular_velocity > -0.24181733280420303):
										if(pole_angular_velocity <= -0.23762138932943344):
											return True
						else:
							if(cart_position <= -0.00821502460166812):
								if(cart_velocity <= 0.22107648104429245):
									if(cart_velocity <= 0.20660416036844254):
										if(pole_angle > 0.02949636150151491):
											if(pole_angle <= 0.029754151590168476):
												return True
									else:
										if(cart_velocity <= 0.21383391320705414):
											return True
								else:
									return True
							else:
								if(pole_angular_velocity <= -0.1683526635169983):
									if(cart_position <= 0.03146131616085768):
										if(pole_angular_velocity <= -0.21594837307929993):
											return True
									else:
										if(pole_angular_velocity > -0.21366138011217117):
											if(pole_angle <= 0.03008658904582262):
												return True
								else:
									if(cart_position <= -0.00214935012627393):
										if(pole_angular_velocity > -0.15054918825626373):
											return True
									else:
										return True
				else:
					if(cart_velocity <= 0.1809116005897522):
						if(pole_angular_velocity > -0.20748944580554962):
							return True
					else:
						if(pole_angular_velocity <= -0.27239927649497986):
							if(pole_angular_velocity > -0.29517465829849243):
								if(pole_angle <= 0.040613604709506035):
									if(cart_velocity > 0.2402428686618805):
										if(pole_angle <= 0.03663402795791626):
											return True
								else:
									return True
						else:
							if(cart_position <= -0.022344418801367283):
								if(cart_velocity > 0.20063341408967972):
									return True
							else:
								return True
			else:
				if(pole_angle <= 0.001906043034978211):
					if(cart_velocity <= 0.19710254669189453):
						if(pole_angle > 0.0009986476507037878):
							if(cart_velocity > 0.17052625864744186):
								if(pole_angle <= 0.001396112667862326):
									return True
					else:
						if(cart_velocity <= 0.19712293148040771):
							return True
				else:
					if(cart_position <= 0.07183830440044403):
						if(pole_angular_velocity <= -0.11723022907972336):
							if(cart_position <= 0.0405742172151804):
								if(pole_angle <= 0.021216497756540775):
									if(cart_velocity > 0.16247688978910446):
										if(cart_velocity <= 0.16281072795391083):
											return True
										else:
											if(pole_angle > 0.01040760986506939):
												if(cart_position > -0.0009533283300697803):
													return True
								else:
									if(cart_position <= -0.03331857454031706):
										if(pole_angular_velocity > -0.12031572684645653):
											return True
									else:
										return True
							else:
								if(cart_velocity <= 0.17861702293157578):
									if(pole_angle > 0.007500296691432595):
										if(cart_position <= 0.0548661220818758):
											if(pole_angular_velocity <= -0.1354467123746872):
												return True
										else:
											return True
								else:
									return True
						else:
							if(cart_velocity <= 0.1670742779970169):
								if(pole_angle > 0.0185689153149724):
									if(cart_velocity > 0.1490742340683937):
										return True
							else:
								return True
					else:
						if(pole_angle <= 0.002420681295916438):
							if(cart_velocity <= 0.1630207970738411):
								if(pole_angular_velocity <= -0.12130266800522804):
									if(pole_angle <= 0.0019266984309069812):
										return True
									else:
										if(cart_velocity > 0.1500326320528984):
											if(cart_velocity <= 0.15171755850315094):
												return True
								else:
									if(pole_angle > 0.002048622351139784):
										return True
							else:
								return True
						else:
							if(cart_position <= 0.10468507930636406):
								if(pole_angle <= 0.005031617358326912):
									if(cart_position > 0.08732271194458008):
										if(cart_velocity > 0.14664074778556824):
											if(pole_angular_velocity <= -0.12409807741641998):
												if(cart_position <= 0.09291469305753708):
													return True
											else:
												return True
								else:
									return True
							else:
								if(cart_velocity <= 0.13939200341701508):
									if(pole_angular_velocity > -0.11515993624925613):
										return True
								else:
									return True
		else:
			if(pole_angle <= 0.0010587017750367522):
				if(pole_angle <= 0.00028330853092484176):
					if(cart_position <= 0.11699293926358223):
						if(pole_angle <= -0.0008639824518468231):
							if(pole_angle <= -0.0020343047799542546):
								if(pole_angular_velocity <= -0.006532130762934685):
									if(cart_position <= 0.0036839224630966783):
										if(cart_position > 0.0031606891425326467):
											return True
									else:
										if(pole_angular_velocity > -0.011174938175827265):
											if(pole_angular_velocity <= -0.011150849517434835):
												return True
								else:
									if(cart_velocity <= 0.04787500575184822):
										if(cart_velocity > 0.03879775293171406):
											if(cart_position <= 0.10023770108819008):
												if(pole_angle <= -0.0022824308834969997):
													if(pole_angle > -0.0029028335120528936):
														if(cart_position > 0.0897638313472271):
															return True
												else:
													if(pole_angle <= -0.0021750604500994086):
														return True
											else:
												if(cart_velocity <= 0.046655233949422836):
													return True
									else:
										if(pole_angle > -0.006712969159707427):
											return True
							else:
								if(pole_angle <= -0.002028372255153954):
									return True
								else:
									if(cart_velocity > 0.036504264920949936):
										if(pole_angular_velocity <= -0.01829157117754221):
											if(cart_position <= 0.04275096394121647):
												if(pole_angular_velocity <= -0.056223390623927116):
													if(pole_angle > -0.001235230709426105):
														if(pole_angle <= -0.0011931427288800478):
															return True
												else:
													if(cart_position > 0.009685919503681362):
														return True
											else:
												if(cart_position <= 0.060609398409724236):
													if(cart_position > 0.05896143428981304):
														return True
										else:
											if(cart_position <= 0.09587016329169273):
												if(pole_angular_velocity > -0.007100757444277406):
													if(cart_position > 0.0814383365213871):
														if(pole_angle <= -0.0016774393734522164):
															if(cart_position > 0.08802899345755577):
																return True
														else:
															return True
											else:
												return True
						else:
							if(pole_angular_velocity <= -0.03082387987524271):
								if(cart_position <= 0.07184406742453575):
									if(pole_angular_velocity > -0.09056921303272247):
										if(cart_position > 0.004645733395591378):
											if(pole_angle <= -0.0004377610021037981):
												if(pole_angular_velocity <= -0.07080717384815216):
													if(pole_angle <= -0.0008288942917715758):
														if(pole_angular_velocity > -0.0801316499710083):
															return True
												else:
													if(cart_position > 0.0316010182723403):
														return True
											else:
												if(cart_position <= 0.05625593289732933):
													if(cart_velocity <= 0.14541491866111755):
														if(pole_angular_velocity > -0.03654707223176956):
															return True
													else:
														if(pole_angular_velocity > -0.08143047988414764):
															return True
												else:
													return True
							else:
								if(cart_velocity <= 0.02361580077558756):
									if(pole_angular_velocity <= -0.0033567686332389712):
										if(pole_angle <= -0.0008618126448709518):
											return True
										else:
											if(pole_angle <= 0.000277430604910478):
												if(cart_velocity > 0.019291618838906288):
													if(cart_velocity <= 0.019374269992113113):
														return True
													else:
														if(pole_angle > -0.00017993537039728835):
															if(pole_angle <= 2.8640497475862503e-05):
																return True
											else:
												return True
									else:
										return True
								else:
									if(cart_position <= 0.08625803142786026):
										if(cart_velocity <= 0.04259863682091236):
											if(pole_angle <= -0.0007233383075799793):
												return True
											else:
												if(pole_angle > -1.716434780973941e-06):
													if(pole_angle <= 0.00012540707029984333):
														return True
										else:
											if(cart_position <= 0.07582515105605125):
												return True
									else:
										if(pole_angle <= -0.0003850711364066228):
											if(cart_velocity <= 0.026718911714851856):
												if(cart_position > 0.1151961125433445):
													return True
											else:
												if(pole_angular_velocity <= -0.022613422945141792):
													if(cart_velocity > 0.04706503078341484):
														return True
												else:
													if(cart_velocity <= 0.03990238532423973):
														if(cart_position <= 0.10294193401932716):
															if(pole_angular_velocity > -0.005820682737976313):
																return True
														else:
															if(pole_angular_velocity <= -0.016403150744736195):
																if(pole_angular_velocity <= -0.01673055626451969):
																	return True
															else:
																return True
													else:
														return True
										else:
											if(pole_angular_velocity <= -0.02143980748951435):
												if(cart_velocity <= 0.03735995292663574):
													if(cart_position > 0.1152140386402607):
														if(pole_angle <= 0.00017101666162488982):
															return True
												else:
													if(cart_position > 0.10122410580515862):
														return True
											else:
												if(pole_angular_velocity <= -0.005723543232306838):
													return True
												else:
													if(cart_position > 0.09372953698039055):
														return True
					else:
						if(cart_position <= 0.12571095675230026):
							if(pole_angle <= -3.079258021898568e-05):
								if(cart_position <= 0.1257021278142929):
									if(pole_angle <= -0.001808693166822195):
										if(pole_angle > -0.0022129229037091136):
											if(pole_angle <= -0.002183470642194152):
												return True
									else:
										if(pole_angle <= -0.001805670268367976):
											return True
										else:
											if(pole_angular_velocity <= -0.012334023136645555):
												if(cart_velocity > 0.03678189590573311):
													if(pole_angular_velocity <= -0.02482064813375473):
														if(cart_velocity <= 0.0370041448622942):
															return True
													else:
														return True
											else:
												if(cart_velocity <= 0.016742659732699394):
													if(cart_velocity > 0.00864768959581852):
														if(pole_angular_velocity > -0.006093936040997505):
															if(cart_position > 0.11838433519005775):
																return True
												else:
													return True
								else:
									return True
							else:
								if(pole_angle <= -2.393804879829986e-05):
									return True
								else:
									if(cart_position <= 0.1239265725016594):
										if(cart_position <= 0.12334883585572243):
											if(cart_velocity <= 0.04590592347085476):
												if(pole_angle <= 0.00023749886167934164):
													if(cart_position > 0.122514259070158):
														if(pole_angle <= 7.291016845556442e-05):
															return True
												else:
													return True
											else:
												return True
										else:
											return True
									else:
										if(pole_angular_velocity > -0.006434087408706546):
											return True
						else:
							if(cart_velocity <= -0.01584121398627758):
								if(cart_position > 0.15188637375831604):
									return True
							else:
								if(cart_position <= 0.1705847904086113):
									if(pole_angle > -8.409176371060312e-05):
										if(pole_angular_velocity <= -0.013556430116295815):
											if(cart_velocity <= 0.007086407858878374):
												if(pole_angular_velocity <= -0.020445645786821842):
													return True
										else:
											if(cart_velocity > 0.009134095162153244):
												return True
								else:
									if(cart_position <= 0.1719667762517929):
										return True
				else:
					if(pole_angular_velocity <= -0.031777963042259216):
						if(cart_position <= 0.12451418489217758):
							if(pole_angular_velocity <= -0.039029402658343315):
								if(pole_angle <= 0.0010245335288345814):
									if(cart_velocity > 0.1424916386604309):
										if(pole_angular_velocity <= -0.09617031738162041):
											if(pole_angular_velocity <= -0.11086485534906387):
												if(pole_angular_velocity > -0.11194831505417824):
													return True
										else:
											if(cart_position <= 0.04341410659253597):
												if(cart_velocity <= 0.17761648446321487):
													if(pole_angular_velocity > -0.06431064568459988):
														if(cart_position > 0.010899695567786694):
															return True
												else:
													return True
											else:
												if(pole_angle > 0.0005269646790111437):
													return True
								else:
									return True
							else:
								if(cart_velocity > 0.03996875509619713):
									if(pole_angle <= 0.0005572026711888611):
										if(cart_velocity > 0.04397708922624588):
											if(cart_position > 0.11323864385485649):
												return True
									else:
										if(cart_position > -0.013533934019505978):
											if(pole_angle <= 0.0007179754611570388):
												if(pole_angle <= 0.0007157815853133798):
													return True
											else:
												return True
						else:
							if(cart_position <= 0.13300737738609314):
								if(cart_position <= 0.1329376995563507):
									if(cart_velocity <= 0.04624463431537151):
										if(cart_velocity > 0.03754439949989319):
											if(pole_angular_velocity > -0.03795726038515568):
												return True
									else:
										if(pole_angular_velocity > -0.046353939920663834):
											if(pole_angle > 0.0006077363068470731):
												return True
								else:
									if(pole_angle <= 0.0009926754282787442):
										return True
							else:
								if(pole_angular_velocity > -0.050672490149736404):
									if(cart_velocity <= 0.042309973388910294):
										if(cart_position > 0.14716343581676483):
											if(cart_position <= 0.14740652590990067):
												return True
											else:
												if(cart_velocity > 0.021358408499509096):
													if(cart_position > 0.14848751574754715):
														return True
									else:
										if(cart_position > 0.1351407766342163):
											if(cart_velocity <= 0.043236855417490005):
												if(pole_angle <= 0.0007050672429613769):
													return True
											else:
												return True
					else:
						if(cart_velocity <= 0.02771636750549078):
							if(pole_angular_velocity <= -0.02159358188509941):
								if(pole_angle > 0.0005839763034600765):
									if(cart_velocity > 0.015254498925060034):
										if(pole_angular_velocity <= -0.02345014363527298):
											if(cart_velocity <= 0.022680464200675488):
												if(pole_angle <= 0.001002555014565587):
													if(cart_position <= 0.13506783545017242):
														if(pole_angular_velocity > -0.025470488704741):
															if(pole_angular_velocity <= -0.02531762793660164):
																return True
															else:
																if(pole_angular_velocity > -0.024402308277785778):
																	if(pole_angular_velocity <= -0.02407448459416628):
																		return True
													else:
														return True
												else:
													if(cart_velocity > 0.016202304046601057):
														if(pole_angular_velocity > -0.028582130558788776):
															return True
											else:
												if(pole_angular_velocity <= -0.03055317886173725):
													if(cart_position > 0.13425768911838531):
														return True
												else:
													if(cart_position <= 0.12535690516233444):
														if(pole_angular_velocity > -0.02671567164361477):
															if(cart_velocity > 0.023629698902368546):
																return True
													else:
														if(pole_angular_velocity <= -0.029805298894643784):
															if(pole_angle <= 0.0007733646198175848):
																return True
														else:
															return True
										else:
											if(cart_position > 0.1193164549767971):
												if(cart_velocity <= 0.017730732448399067):
													if(cart_velocity <= 0.015332821756601334):
														return True
												else:
													return True
							else:
								if(pole_angular_velocity <= -0.007243790663778782):
									if(pole_angular_velocity <= -0.014512476045638323):
										if(cart_velocity <= 0.01209763390943408):
											if(cart_velocity <= 0.010027748998254538):
												if(pole_angle <= 0.0010388982482254505):
													if(pole_angle > 0.0009361956617794931):
														if(pole_angular_velocity > -0.015814324840903282):
															return True
												else:
													return True
											else:
												if(pole_angular_velocity > -0.017865844070911407):
													if(pole_angle <= 0.0006963309133425355):
														if(cart_position <= 0.13111358880996704):
															if(pole_angular_velocity > -0.015629718080163002):
																return True
														else:
															return True
													else:
														return True
										else:
											if(pole_angle <= 0.00045288850378710777):
												if(cart_velocity <= 0.018499057739973068):
													if(pole_angular_velocity > -0.016534808091819286):
														return True
												else:
													return True
											else:
												if(pole_angular_velocity <= -0.014814999420195818):
													if(cart_velocity <= 0.013256147969514132):
														if(cart_velocity <= 0.013047343585640192):
															return True
													else:
														if(pole_angle <= 0.0006327963201329112):
															if(pole_angle <= 0.0006123381026554853):
																if(pole_angular_velocity <= -0.01993493363261223):
																	if(cart_position > 0.12620404362678528):
																		return True
																else:
																	return True
														else:
															return True
									else:
										if(cart_velocity <= 0.006650689523667097):
											if(pole_angle <= 0.0009159583132714033):
												if(cart_velocity > 0.006429050350561738):
													if(cart_velocity <= 0.006539475172758102):
														return True
											else:
												if(cart_position > 0.1255113184452057):
													return True
										else:
											if(pole_angle <= 0.0010550384176895022):
												if(cart_position > 0.1018655002117157):
													if(pole_angle <= 0.0004623425775207579):
														if(pole_angle <= 0.0004483100346988067):
															if(cart_position > 0.10767792910337448):
																if(cart_velocity <= 0.010546080768108368):
																	if(cart_position > 0.1256466545164585):
																		return True
																else:
																	return True
													else:
														if(pole_angular_velocity <= -0.013249754440039396):
															if(pole_angular_velocity <= -0.01359120151028037):
																return True
															else:
																if(cart_position <= 0.12375534698367119):
																	return True
														else:
															return True
								else:
									if(pole_angle > 0.0008134859381243587):
										if(pole_angle <= 0.0008408271824009717):
											return True
										else:
											if(pole_angular_velocity > -0.003932083607651293):
												if(cart_velocity > 0.006866135518066585):
													return True
						else:
							if(cart_position <= 0.07523545622825623):
								if(pole_angular_velocity > -0.008507114020176232):
									return True
							else:
								if(pole_angular_velocity <= -0.029138077050447464):
									if(cart_velocity <= 0.040017081424593925):
										if(cart_position <= 0.12297991290688515):
											if(pole_angular_velocity > -0.029831531457602978):
												if(pole_angle > 0.00043193751480430365):
													return True
										else:
											return True
									else:
										return True
								else:
									if(cart_velocity <= 0.02961812261492014):
										if(cart_velocity <= 0.029216542840003967):
											return True
									else:
										return True
			else:
				if(pole_angle <= 0.0024281212827190757):
					if(pole_angular_velocity <= -0.050080012530088425):
						if(cart_velocity <= 0.13732516020536423):
							if(pole_angular_velocity <= -0.051607755944132805):
								if(pole_angular_velocity <= -0.053916897624731064):
									if(pole_angle <= 0.002379203448072076):
										if(pole_angle > 0.0022054025903344154):
											if(pole_angle <= 0.002213880652561784):
												return True
									else:
										if(pole_angle <= 0.0023808492114767432):
											return True
										else:
											if(pole_angular_velocity <= -0.05906503275036812):
												if(cart_position <= 0.14316442608833313):
													if(pole_angular_velocity > -0.06577883660793304):
														return True
											else:
												if(pole_angle <= 0.0023926168214529753):
													return True
								else:
									if(pole_angular_velocity <= -0.05365218035876751):
										if(pole_angle <= 0.0018802674603648484):
											if(pole_angle <= 0.0011869410518556833):
												return True
										else:
											if(cart_velocity <= 0.04175596497952938):
												return True
									else:
										if(cart_velocity > 0.04190853238105774):
											if(cart_position <= 0.13863058388233185):
												if(cart_velocity > 0.048617949709296227):
													if(cart_velocity <= 0.049035532400012016):
														return True
											else:
												return True
							else:
								if(cart_velocity <= 0.04178890772163868):
									if(cart_position <= 0.1467474400997162):
										if(cart_velocity > 0.038514144718647):
											if(cart_velocity <= 0.03852866403758526):
												return True
									else:
										return True
								else:
									if(pole_angle <= 0.001532728027086705):
										if(cart_velocity > 0.04745253548026085):
											return True
									else:
										if(cart_position > 0.12371334433555603):
											if(pole_angle <= 0.0021041654981672764):
												return True
											else:
												if(pole_angular_velocity > -0.05110757425427437):
													return True
						else:
							if(cart_position <= 0.029304079711437225):
								if(pole_angular_velocity <= -0.061210693791508675):
									if(pole_angle > 0.0022235206561163068):
										if(cart_position > 0.0066423727257642895):
											return True
								else:
									if(cart_position > -0.007602499215863645):
										return True
							else:
								if(pole_angular_velocity > -0.11121008917689323):
									if(pole_angular_velocity <= -0.0871274396777153):
										if(cart_position <= 0.04764518886804581):
											if(cart_velocity > 0.17396289855241776):
												return True
										else:
											if(cart_velocity <= 0.1383267492055893):
												if(cart_velocity <= 0.1379592940211296):
													return True
											else:
												if(pole_angular_velocity <= -0.10701700672507286):
													if(pole_angular_velocity <= -0.10880199819803238):
														if(cart_velocity <= 0.14686476439237595):
															if(pole_angle > 0.0019934694282710552):
																return True
														else:
															return True
												else:
													if(cart_position <= 0.05699081905186176):
														if(cart_position <= 0.052939653396606445):
															return True
													else:
														return True
									else:
										if(cart_velocity <= 0.142138309776783):
											if(pole_angle > 0.0014141781721264124):
												return True
										else:
											return True
					else:
						if(pole_angular_velocity <= -0.029371706768870354):
							if(pole_angle <= 0.0018742188112810254):
								if(cart_velocity <= 0.0330341961234808):
									if(pole_angular_velocity <= -0.03661579638719559):
										if(cart_velocity > 0.02696643676608801):
											if(pole_angular_velocity <= -0.04075665399432182):
												if(pole_angle <= 0.001820835575927049):
													if(cart_position <= 0.14047791063785553):
														if(cart_velocity > 0.032495055347681046):
															if(pole_angle > 0.0014823063975200057):
																return True
													else:
														if(pole_angle > 0.001307112688664347):
															return True
												else:
													if(cart_position > 0.13771459460258484):
														return True
											else:
												if(cart_position <= 0.1351313367486):
													if(cart_velocity <= 0.03166244737803936):
														if(cart_velocity > 0.030507685616612434):
															if(pole_angular_velocity > -0.03760397061705589):
																return True
													else:
														return True
												else:
													if(pole_angle <= 0.0014137740363366902):
														if(cart_velocity > 0.029173417948186398):
															return True
													else:
														if(pole_angular_velocity <= -0.04043135046958923):
															if(pole_angular_velocity <= -0.040589589625597):
																return True
														else:
															return True
									else:
										if(cart_position <= 0.13549768179655075):
											if(cart_velocity <= 0.023564227856695652):
												if(pole_angle <= 0.0017256209393963218):
													if(pole_angular_velocity <= -0.02977080922573805):
														if(pole_angle > 0.0016492268769070506):
															if(pole_angle <= 0.0016600610106252134):
																return True
													else:
														if(pole_angular_velocity <= -0.029582764953374863):
															return True
												else:
													if(pole_angular_velocity <= -0.031129821203649044):
														if(cart_position > 0.13293349742889404):
															if(pole_angular_velocity > -0.034659333527088165):
																return True
													else:
														return True
											else:
												if(cart_position <= 0.12897829711437225):
													if(pole_angle <= 0.0013888367684558034):
														if(cart_velocity > 0.03108091652393341):
															if(pole_angle > 0.0011762651847675443):
																return True
													else:
														if(pole_angular_velocity <= -0.03121057990938425):
															if(cart_velocity <= 0.03155292011797428):
																if(pole_angle > 0.0017187854391522706):
																	if(cart_velocity <= 0.027369491755962372):
																		return True
															else:
																return True
														else:
															return True
												else:
													if(pole_angular_velocity <= -0.03459313325583935):
														if(cart_velocity > 0.02667234092950821):
															if(cart_velocity <= 0.027550161816179752):
																if(pole_angle > 0.001643442374188453):
																	return True
															else:
																return True
													else:
														if(pole_angular_velocity <= -0.030800125561654568):
															return True
										else:
											if(pole_angular_velocity <= -0.03636337071657181):
												if(pole_angular_velocity <= -0.03656227886676788):
													return True
											else:
												return True
								else:
									if(pole_angle <= 0.0013962979428470135):
										if(pole_angular_velocity <= -0.043066276237368584):
											if(cart_velocity <= 0.040496472269296646):
												if(cart_position > 0.14295709133148193):
													if(pole_angle > 0.0011369884596206248):
														return True
											else:
												if(cart_position <= 0.13214141875505447):
													if(cart_position > 0.1287303790450096):
														if(cart_position <= 0.1302071511745453):
															return True
												else:
													return True
										else:
											if(cart_position > 0.030272454023361206):
												return True
									else:
										if(cart_position <= 0.016152012161910534):
											if(pole_angle <= 0.0017751044942997396):
												return True
										else:
											if(cart_velocity <= 0.03851357661187649):
												if(cart_velocity <= 0.03839671052992344):
													if(cart_position > 0.12326744571328163):
														if(pole_angle <= 0.0015641851932741702):
															if(cart_position > 0.13283222168684006):
																if(pole_angular_velocity > -0.048354996368288994):
																	return True
														else:
															return True
											else:
												return True
							else:
								if(pole_angular_velocity <= -0.04927212931215763):
									if(pole_angle > 0.002023170585744083):
										if(cart_position <= 0.13698405027389526):
											return True
								else:
									if(cart_position > 0.050017378060147166):
										if(pole_angular_velocity <= -0.03548646159470081):
											if(cart_velocity <= 0.02577099669724703):
												if(pole_angle <= 0.0022857995936647058):
													if(pole_angular_velocity > -0.0373199712485075):
														if(cart_position > 0.13446596264839172):
															return True
												else:
													if(pole_angle <= 0.0023919768864288926):
														return True
											else:
												if(pole_angular_velocity <= -0.040850136429071426):
													if(cart_velocity > 0.027722149156033993):
														if(pole_angular_velocity <= -0.04813481122255325):
															if(pole_angular_velocity <= -0.048945074900984764):
																return True
															else:
																if(pole_angular_velocity > -0.0487897340208292):
																	if(pole_angular_velocity <= -0.04831415042281151):
																		if(pole_angular_velocity <= -0.04843960329890251):
																			if(pole_angular_velocity <= -0.04851290211081505):
																				if(pole_angle <= 0.00214701727963984):
																					return True
																				else:
																					if(cart_velocity > 0.03535102866590023):
																						return True
																		else:
																			return True
														else:
															if(cart_velocity <= 0.029312293976545334):
																if(cart_velocity <= 0.028147462755441666):
																	return True
															else:
																if(pole_angular_velocity <= -0.04531264863908291):
																	if(cart_velocity <= 0.03415708802640438):
																		if(cart_position > 0.13754727691411972):
																			return True
																	else:
																		if(pole_angle <= 0.0022747264010831714):
																			return True
																		else:
																			if(pole_angle > 0.0022866216022521257):
																				if(cart_position <= 0.1318056657910347):
																					if(cart_velocity > 0.041028523817658424):
																						return True
																				else:
																					return True
																else:
																	return True
												else:
													return True
										else:
											if(cart_velocity > 0.01863882038742304):
												if(cart_velocity <= 0.021814710460603237):
													if(pole_angle <= 0.002042517880909145):
														if(cart_position > 0.1327701434493065):
															return True
													else:
														return True
												else:
													return True
						else:
							if(cart_velocity <= 0.00282054184935987):
								if(pole_angle <= 0.0021868631010875106):
									if(cart_position <= 0.1076478660106659):
										return True
									else:
										if(pole_angular_velocity > -0.0035334256244823337):
											if(pole_angular_velocity <= -0.003529044450260699):
												return True
								else:
									if(cart_velocity <= -0.0002931197814177722):
										return True
							else:
								if(cart_velocity <= 0.006174753187224269):
									if(cart_position <= 0.11734187975525856):
										if(pole_angular_velocity <= -0.0034374238457530737):
											if(cart_velocity > 0.006066468311473727):
												if(pole_angle > 0.0016553500900045037):
													return True
										else:
											return True
									else:
										if(pole_angular_velocity <= -0.019297177903354168):
											if(cart_position > 0.13768305629491806):
												return True
										else:
											return True
								else:
									if(pole_angular_velocity <= -0.020459745079278946):
										if(cart_velocity <= 0.013552385848015547):
											if(pole_angle <= 0.0017794657032936811):
												if(cart_position > 0.12944061309099197):
													if(pole_angle > 0.001459748251363635):
														return True
											else:
												return True
										else:
											if(cart_velocity <= 0.01895028166472912):
												if(pole_angle <= 0.0014069550670683384):
													if(pole_angular_velocity <= -0.022561250254511833):
														if(cart_position <= 0.1306416541337967):
															if(pole_angle <= 0.001116048835683614):
																return True
														else:
															if(pole_angle > 0.0011157062253914773):
																return True
													else:
														return True
												else:
													if(pole_angular_velocity <= -0.027213552966713905):
														if(cart_velocity <= 0.018711826764047146):
															if(cart_position <= 0.1289253681898117):
																if(cart_velocity <= 0.01854969933629036):
																	return True
														else:
															return True
													else:
														return True
											else:
												if(cart_position > -0.029484671540558338):
													if(pole_angular_velocity <= -0.028337794356048107):
														if(pole_angular_velocity <= -0.028340106830000877):
															if(pole_angle <= 0.0014631999074481428):
																if(cart_velocity <= 0.023814482614398003):
																	if(pole_angle <= 0.0011867345892824233):
																		return True
																else:
																	return True
															else:
																return True
													else:
														return True
									else:
										if(cart_position > 0.03988335840404034):
											if(pole_angular_velocity <= -0.003893062239512801):
												if(cart_velocity <= 0.010502154473215342):
													if(cart_position > 0.11064057052135468):
														if(cart_velocity <= 0.01042317459359765):
															if(pole_angular_velocity <= -0.01692405715584755):
																if(pole_angular_velocity <= -0.0170561159029603):
																	return True
															else:
																return True
												else:
													return True
											else:
												if(pole_angular_velocity > -0.003818449331447482):
													return True
				else:
					if(cart_position <= 0.028438886627554893):
						if(cart_velocity <= 0.03284766711294651):
							if(pole_angle <= 0.023555129766464233):
								if(pole_angular_velocity <= -0.014416192192584276):
									if(cart_velocity > 0.025547269731760025):
										if(pole_angle > 0.019437029026448727):
											if(pole_angular_velocity > -0.04076244216412306):
												return True
								else:
									if(cart_velocity <= 0.0071754977107048035):
										if(cart_position > 0.022905432619154453):
											if(pole_angle > 0.016636349260807037):
												return True
									else:
										if(pole_angle > 0.01228404464200139):
											if(cart_position <= -0.017438925802707672):
												if(pole_angular_velocity > -0.008135555777698755):
													return True
											else:
												if(pole_angle <= 0.01508592814207077):
													if(pole_angle <= 0.013196408748626709):
														return True
												else:
													return True
							else:
								if(cart_position <= -0.0496489517390728):
									if(pole_angular_velocity > -0.01198843540623784):
										if(pole_angle > 0.03068393189460039):
											if(pole_angular_velocity <= -0.01003992510959506):
												return True
								else:
									if(pole_angle <= 0.032017605379223824):
										if(cart_velocity <= -0.006098617101088166):
											if(pole_angular_velocity <= -0.011886980384588242):
												if(pole_angle > 0.02794093731790781):
													if(cart_position > -0.031096693128347397):
														if(pole_angular_velocity > -0.03933236561715603):
															return True
											else:
												if(cart_velocity > -0.03853926621377468):
													return True
										else:
											if(pole_angular_velocity > -0.04562007635831833):
												if(cart_velocity <= -0.0026212469092570245):
													if(cart_velocity <= -0.0038556245854124427):
														return True
												else:
													return True
									else:
										return True
						else:
							if(pole_angle <= 0.01413720939308405):
								if(cart_velocity <= 0.1375659629702568):
									if(pole_angular_velocity > -0.017094180919229984):
										if(cart_position > 0.01512965327128768):
											if(cart_position <= 0.021833554841578007):
												return True
								else:
									if(pole_angular_velocity <= -0.071258045732975):
										if(cart_position <= -0.0073337743524461985):
											if(pole_angle <= 0.012528563383966684):
												if(pole_angular_velocity > -0.09313137456774712):
													if(cart_velocity <= 0.16169529408216476):
														if(cart_position > -0.020131546072661877):
															if(pole_angle > 0.008009798126295209):
																if(pole_angular_velocity > -0.0830874964594841):
																	return True
													else:
														if(pole_angle > 0.005411121062934399):
															if(cart_velocity <= 0.17712782323360443):
																return True
											else:
												if(pole_angular_velocity <= -0.09197579324245453):
													if(cart_velocity > 0.16960160434246063):
														return True
												else:
													return True
										else:
											if(pole_angle <= 0.008975683711469173):
												if(pole_angular_velocity <= -0.08431228995323181):
													if(cart_velocity <= 0.17762935161590576):
														if(cart_velocity <= 0.1600748673081398):
															if(pole_angle > 0.008389109279960394):
																if(pole_angle <= 0.008527236990630627):
																	return True
														else:
															if(pole_angular_velocity > -0.09964044392108917):
																if(pole_angle > 0.004062330117449164):
																	return True
													else:
														return True
												else:
													if(pole_angle <= 0.005337200593203306):
														if(cart_velocity <= 0.15902706235647202):
															if(cart_velocity <= 0.14211325347423553):
																return True
														else:
															if(pole_angle > 0.0027316423365846276):
																return True
													else:
														return True
											else:
												if(pole_angular_velocity <= -0.09626885503530502):
													if(cart_velocity <= 0.1501263976097107):
														if(pole_angular_velocity <= -0.10709341242909431):
															return True
													else:
														return True
												else:
													return True
									else:
										if(cart_position <= -0.02137991040945053):
											if(pole_angle <= 0.005585101433098316):
												if(pole_angular_velocity <= -0.03189572133123875):
													if(cart_position > -0.0272954311221838):
														if(cart_velocity > 0.14784640818834305):
															return True
												else:
													return True
											else:
												if(cart_position > -0.06655250489711761):
													if(pole_angle <= 0.00951764127239585):
														if(pole_angular_velocity > -0.06430348008871078):
															if(cart_position > -0.056726040318608284):
																if(cart_velocity <= 0.14134886115789413):
																	if(pole_angle > 0.008340653497725725):
																		return True
																else:
																	return True
													else:
														return True
										else:
											if(pole_angular_velocity <= -0.06356468424201012):
												if(pole_angular_velocity <= -0.06537798792123795):
													return True
											else:
												return True
							else:
								if(cart_velocity <= 0.14591672271490097):
									if(pole_angular_velocity <= -0.028368402272462845):
										if(cart_velocity <= 0.09278042800724506):
											if(pole_angle <= 0.025431196205317974):
												if(cart_position <= 0.006123639876022935):
													if(pole_angle > 0.024130753241479397):
														if(pole_angular_velocity > -0.0414343886077404):
															return True
												else:
													return True
											else:
												if(pole_angular_velocity > -0.04620332084596157):
													return True
										else:
											if(pole_angular_velocity <= -0.1035441942512989):
												if(cart_velocity <= 0.14203225076198578):
													return True
												else:
													if(pole_angular_velocity <= -0.11130817607045174):
														return True
											else:
												if(cart_velocity <= 0.14066310226917267):
													if(pole_angular_velocity > -0.08796336874365807):
														return True
												else:
													return True
									else:
										if(pole_angle <= 0.015309076756238937):
											if(cart_position > -0.023979621939361095):
												return True
										else:
											if(cart_velocity <= 0.04487010836601257):
												return True
											else:
												if(cart_velocity > 0.04550827853381634):
													return True
								else:
									if(cart_position <= -0.05885281413793564):
										if(cart_position <= -0.061288025230169296):
											if(pole_angle <= 0.017926541157066822):
												if(cart_position <= -0.0672721415758133):
													return True
											else:
												return True
									else:
										return True
					else:
						if(pole_angular_velocity <= -0.06643299758434296):
							if(pole_angle <= 0.003843779326416552):
								if(cart_position <= 0.14315197616815567):
									if(cart_position <= 0.05403122678399086):
										if(pole_angular_velocity > -0.09961220622062683):
											if(cart_velocity > 0.13873457163572311):
												if(cart_position <= 0.035960471257567406):
													if(pole_angle > 0.003041438525542617):
														return True
												else:
													return True
									else:
										if(cart_velocity > 0.049660542979836464):
											return True
								else:
									if(pole_angle <= 0.0031002408359199762):
										if(cart_position <= 0.1552405208349228):
											if(cart_position <= 0.15087270736694336):
												if(cart_velocity > 0.05035465396940708):
													if(cart_velocity <= 0.05082029663026333):
														return True
											else:
												if(pole_angular_velocity > -0.07035911455750465):
													if(cart_velocity <= 0.04816877469420433):
														if(pole_angular_velocity > -0.06808415055274963):
															if(cart_velocity > 0.046318696811795235):
																return True
													else:
														return True
										else:
											return True
									else:
										if(pole_angular_velocity <= -0.07368836179375648):
											if(pole_angular_velocity > -0.07532941550016403):
												if(cart_velocity > 0.04986831918358803):
													if(pole_angle > 0.003591612563468516):
														return True
										else:
											if(cart_position <= 0.14987730234861374):
												if(pole_angle <= 0.0034904812928289175):
													if(pole_angular_velocity > -0.0675150603055954):
														if(cart_velocity > 0.045735858380794525):
															return True
												else:
													if(cart_position <= 0.14818403869867325):
														return True
											else:
												if(cart_position <= 0.15241104364395142):
													if(pole_angular_velocity <= -0.07273541390895844):
														if(pole_angle > 0.0037438870640471578):
															return True
													else:
														if(pole_angle <= 0.0031840638257563114):
															if(cart_position > 0.15156088769435883):
																return True
														else:
															if(cart_velocity <= 0.04678406938910484):
																if(pole_angular_velocity > -0.06903228908777237):
																	return True
															else:
																return True
												else:
													return True
							else:
								if(pole_angle <= 0.004057509824633598):
									if(pole_angular_velocity <= -0.07288186624646187):
										if(cart_velocity > 0.049263374879956245):
											if(cart_position <= 0.10102850012481213):
												return True
											else:
												if(cart_velocity <= 0.04989118501543999):
													if(pole_angular_velocity <= -0.07329099625349045):
														return True
									else:
										if(pole_angle <= 0.004033996490761638):
											return True
								else:
									if(pole_angular_velocity <= -0.09908933565020561):
										if(pole_angular_velocity <= -0.10420261695981026):
											return True
									else:
										if(pole_angle <= 0.004670804366469383):
											if(pole_angle <= 0.004669672343879938):
												if(pole_angular_velocity <= -0.07386050373315811):
													if(cart_velocity <= 0.048539379611611366):
														if(cart_position > 0.15143024176359177):
															if(pole_angular_velocity > -0.07570376992225647):
																return True
													else:
														if(pole_angular_velocity <= -0.07438009977340698):
															if(cart_velocity <= 0.050113240256905556):
																if(pole_angular_velocity > -0.07670838758349419):
																	return True
															else:
																return True
														else:
															if(cart_position > 0.14699409902095795):
																return True
												else:
													if(cart_velocity <= 0.04578855074942112):
														if(pole_angular_velocity <= -0.07005952298641205):
															if(cart_position > 0.15029694885015488):
																return True
														else:
															return True
													else:
														return True
										else:
											return True
						else:
							if(pole_angle <= 0.003370310296304524):
								if(pole_angular_velocity <= -0.04980311915278435):
									if(cart_velocity <= 0.03435851261019707):
										if(pole_angular_velocity <= -0.0502214040607214):
											if(pole_angle > 0.0032878780039027333):
												if(pole_angular_velocity > -0.05205398425459862):
													return True
										else:
											if(cart_velocity <= 0.03285261243581772):
												if(pole_angular_velocity <= -0.05013013444840908):
													return True
											else:
												return True
									else:
										if(pole_angle <= 0.002874906058423221):
											if(pole_angular_velocity <= -0.06255181133747101):
												if(cart_velocity > 0.04539357125759125):
													if(cart_position > 0.14666393399238586):
														if(pole_angle <= 0.0026258056750521064):
															return True
											else:
												if(cart_position <= 0.14606591314077377):
													if(pole_angular_velocity <= -0.051452044397592545):
														if(cart_velocity <= 0.0449281707406044):
															if(pole_angular_velocity <= -0.05195934697985649):
																if(pole_angle > 0.0028015930438414216):
																	if(cart_velocity > 0.042453475296497345):
																		if(cart_position > 0.13335401564836502):
																			return True
															else:
																if(pole_angle <= 0.0027379372622817755):
																	return True
														else:
															if(pole_angular_velocity <= -0.05991795472800732):
																if(pole_angular_velocity <= -0.0611897986382246):
																	return True
															else:
																if(cart_position > 0.1352398544549942):
																	if(cart_velocity <= 0.0452559869736433):
																		if(pole_angular_velocity > -0.05851682834327221):
																			return True
																	else:
																		return True
													else:
														if(cart_position > 0.12549088150262833):
															return True
												else:
													if(pole_angle <= 0.002525437856093049):
														if(cart_position <= 0.14764633029699326):
															return True
													else:
														if(pole_angular_velocity <= -0.06141536682844162):
															if(pole_angular_velocity <= -0.06161227263510227):
																return True
														else:
															return True
										else:
											if(pole_angular_velocity <= -0.060212790966033936):
												if(cart_velocity <= 0.04162030294537544):
													if(cart_position > 0.14893507212400436):
														if(pole_angle > 0.0030393695924431086):
															return True
												else:
													if(pole_angular_velocity <= -0.06425890326499939):
														if(cart_velocity > 0.044002968817949295):
															if(pole_angular_velocity <= -0.06443752348423004):
																if(pole_angle <= 0.003298952244222164):
																	return True
																else:
																	if(cart_position > 0.147245354950428):
																		return True
													else:
														if(pole_angle <= 0.003118026303127408):
															if(pole_angle <= 0.0031114351004362106):
																if(cart_velocity <= 0.042281677946448326):
																	if(cart_velocity <= 0.04190879315137863):
																		return True
																else:
																	if(cart_position <= 0.14293941855430603):
																		if(pole_angle > 0.0029427262488752604):
																			return True
																	else:
																		return True
														else:
															return True
											else:
												if(pole_angular_velocity <= -0.05406374670565128):
													return True
												else:
													if(cart_velocity <= 0.04079323261976242):
														if(cart_position > 0.13543809950351715):
															return True
													else:
														if(cart_velocity <= 0.043518880382180214):
															if(cart_position > 0.1296515390276909):
																return True
														else:
															return True
								else:
									if(pole_angular_velocity <= -0.045062096789479256):
										if(cart_velocity > 0.02952786348760128):
											if(pole_angle <= 0.002617380814626813):
												if(cart_velocity <= 0.03656543791294098):
													if(pole_angular_velocity <= -0.046708159148693085):
														if(cart_position > 0.13936857879161835):
															if(cart_position <= 0.14000459760427475):
																return True
													else:
														return True
												else:
													return True
											else:
												if(pole_angular_velocity <= -0.04911050945520401):
													if(pole_angular_velocity <= -0.04917146638035774):
														if(pole_angle <= 0.002923046122305095):
															if(pole_angle <= 0.0028042810736224055):
																return True
															else:
																if(cart_velocity > 0.038219476118683815):
																	return True
														else:
															return True
												else:
													if(pole_angle <= 0.0028745902236551046):
														if(pole_angle <= 0.0028594553004950285):
															return True
													else:
														return True
									else:
										if(cart_position > 0.04710812121629715):
											if(cart_position <= 0.14320603758096695):
												if(cart_position <= 0.1377197578549385):
													return True
												else:
													if(cart_position > 0.13776663690805435):
														return True
											else:
												if(pole_angular_velocity <= -0.0295974500477314):
													return True
							else:
								if(cart_position <= 0.04692660830914974):
									if(pole_angle <= 0.010901434812694788):
										if(pole_angular_velocity > -0.010088811162859201):
											return True
									else:
										if(cart_position <= 0.045163920149207115):
											return True
								else:
									if(pole_angle <= 0.009350965265184641):
										if(pole_angle <= 0.0038000590866431594):
											if(pole_angle <= 0.0037992740981280804):
												if(pole_angular_velocity <= -0.0489039272069931):
													if(cart_velocity > 0.03192690201103687):
														if(cart_velocity <= 0.03251670487225056):
															if(pole_angular_velocity > -0.052171846851706505):
																if(cart_velocity <= 0.03247925080358982):
																	return True
														else:
															if(pole_angular_velocity <= -0.06292105093598366):
																if(cart_velocity > 0.04161643981933594):
																	if(pole_angle <= 0.0034214883344247937):
																		if(cart_position > 0.14634456485509872):
																			return True
																	else:
																		return True
															else:
																return True
												else:
													return True
										else:
											if(pole_angle <= 0.004083692096173763):
												if(pole_angle <= 0.004083298845216632):
													if(pole_angle <= 0.0040718321688473225):
														if(pole_angular_velocity <= -0.05133263021707535):
															if(cart_velocity > 0.033010113053023815):
																return True
														else:
															return True
													else:
														if(pole_angle > 0.00407233671285212):
															return True
											else:
												return True
									else:
										if(cart_position <= 0.050569405779242516):
											return True
	else:
		if(pole_angular_velocity <= 0.08658628165721893):
			if(pole_angle <= -0.0018948267679661512):
				if(pole_angular_velocity <= 0.04840107820928097):
					if(pole_angle <= -0.0027885206509381533):
						if(cart_position <= 0.13545861095190048):
							if(cart_velocity <= 0.010182851459831):
								if(cart_position <= 0.08729403838515282):
									if(pole_angle <= -0.00370804057456553):
										if(pole_angular_velocity <= 0.04686068557202816):
											if(cart_velocity > 0.008001958020031452):
												if(pole_angular_velocity > 0.04440663941204548):
													return True
										else:
											if(pole_angular_velocity <= 0.04693036340177059):
												return True
											else:
												if(cart_velocity > 0.004551619291305542):
													if(pole_angular_velocity <= 0.04735391587018967):
														return True
									else:
										if(pole_angular_velocity <= 0.047627612948417664):
											if(cart_velocity <= -0.003266121493652463):
												if(cart_position > 0.08519768714904785):
													if(cart_position <= 0.08615422621369362):
														return True
											else:
												if(pole_angle <= -0.0031583476811647415):
													if(pole_angle <= -0.00346798833925277):
														if(pole_angle <= -0.0035172487841919065):
															if(cart_position > 0.08237342536449432):
																return True
														else:
															return True
													else:
														if(cart_position > 0.08103564381599426):
															if(cart_position <= 0.0833553597331047):
																return True
												else:
													if(pole_angular_velocity <= 0.03567185625433922):
														if(pole_angle > -0.0029703809414058924):
															return True
													else:
														if(cart_position <= 0.06665099412202835):
															if(cart_position <= 0.06151161529123783):
																return True
														else:
															return True
										else:
											if(cart_position <= 0.08670339360833168):
												return True
								else:
									if(cart_position <= 0.12802743166685104):
										if(pole_angle <= -0.007977426052093506):
											if(pole_angle <= -0.008060711435973644):
												if(cart_position > 0.12680620700120926):
													return True
											else:
												return True
										else:
											if(cart_velocity <= 0.004249657969921827):
												if(cart_position <= 0.09331993386149406):
													if(cart_position <= 0.09331368654966354):
														if(pole_angle <= -0.00322956929448992):
															if(pole_angular_velocity > 0.04804086685180664):
																if(pole_angular_velocity <= 0.04808006063103676):
																	return True
														else:
															if(pole_angle <= -0.0032180165871977806):
																return True
															else:
																if(cart_velocity <= 0.0012562256306409836):
																	if(cart_velocity > -0.012060971464961767):
																		if(cart_velocity <= -0.010638115927577019):
																			return True
																else:
																	if(cart_position <= 0.0899173729121685):
																		return True
													else:
														return True
												else:
													if(cart_position <= 0.09528651833534241):
														if(cart_position > 0.09526034072041512):
															return True
											else:
												if(pole_angular_velocity <= 0.028017327189445496):
													if(pole_angle <= -0.0029528032755479217):
														if(cart_position > 0.12173755466938019):
															if(cart_position <= 0.12196747586131096):
																return True
													else:
														if(pole_angle <= -0.002935857977718115):
															return True
												else:
													if(cart_position > 0.09477663040161133):
														return True
									else:
										if(pole_angular_velocity <= 0.0408022366464138):
											if(pole_angular_velocity <= 0.018430289812386036):
												if(cart_velocity > 0.009645860642194748):
													if(pole_angular_velocity > 0.010669208131730556):
														return True
											else:
												if(cart_velocity > -0.01812083926051855):
													if(pole_angle > -0.009040636010468006):
														if(cart_position <= 0.13441315293312073):
															return True
										else:
											if(pole_angle > -0.012659494299441576):
												return True
							else:
								if(pole_angle <= -0.004059867933392525):
									if(pole_angular_velocity <= 0.019134478643536568):
										if(cart_velocity <= 0.04475676827132702):
											if(cart_position <= 0.10239100083708763):
												if(cart_position > 0.09665311500430107):
													if(cart_position <= 0.09693354740738869):
														return True
											else:
												if(pole_angular_velocity <= 0.010677686892449856):
													if(cart_velocity > 0.03272364940494299):
														if(pole_angle > -0.0075622189324349165):
															return True
												else:
													if(pole_angle > -0.00746310711838305):
														if(cart_velocity > 0.0156573336571455):
															return True
										else:
											if(pole_angular_velocity <= 0.014385002665221691):
												if(cart_velocity <= 0.04489663802087307):
													return True
												else:
													if(pole_angle > -0.004993703681975603):
														if(cart_position > 0.08459747210144997):
															return True
											else:
												if(cart_velocity <= 0.0465648602694273):
													return True
									else:
										if(cart_position <= 0.08565227314829826):
											if(pole_angle <= -0.004352171439677477):
												if(pole_angular_velocity <= 0.019218124449253082):
													return True
												else:
													if(cart_velocity <= 0.046802155673503876):
														if(pole_angular_velocity <= 0.04773455113172531):
															if(pole_angular_velocity <= 0.0415323618799448):
																if(cart_velocity > 0.0377654992043972):
																	if(cart_position <= 0.06999950483441353):
																		if(pole_angle > -0.005235082004219294):
																			if(pole_angular_velocity > 0.030675822868943214):
																				if(cart_position > 0.0369076170027256):
																					return True
																	else:
																		if(pole_angle > -0.0106420055963099):
																			return True
															else:
																if(cart_position > 0.04381651058793068):
																	if(cart_velocity > 0.016267615370452404):
																		if(pole_angle <= -0.005907225189730525):
																			if(pole_angular_velocity <= 0.04201730340719223):
																				return True
																			else:
																				if(cart_velocity <= 0.01701516006141901):
																					return True
																		else:
																			return True
														else:
															if(cart_velocity > 0.03629193641245365):
																return True
													else:
														return True
											else:
												if(cart_velocity <= 0.030580700375139713):
													if(pole_angle <= -0.004333818098530173):
														return True
												else:
													if(cart_position > 0.024417977780103683):
														return True
										else:
											if(pole_angle <= -0.010669929441064596):
												if(cart_position <= 0.08836940303444862):
													return True
												else:
													if(cart_velocity > 0.02640074770897627):
														if(pole_angle > -0.013998669572174549):
															if(cart_velocity <= 0.044335201382637024):
																return True
											else:
												if(pole_angular_velocity <= 0.025046157650649548):
													if(cart_velocity <= 0.016798446886241436):
														if(cart_position > 0.1179390586912632):
															return True
													else:
														if(pole_angular_velocity > 0.021846658550202847):
															if(cart_position <= 0.1149255521595478):
																return True
												else:
													if(pole_angular_velocity <= 0.03244594298303127):
														if(pole_angle <= -0.006564689567312598):
															if(cart_velocity > 0.03134188149124384):
																return True
														else:
															return True
													else:
														return True
								else:
									if(pole_angular_velocity <= 0.023723806254565716):
										if(cart_velocity <= 0.035604869946837425):
											if(pole_angle <= -0.004055808996781707):
												return True
											else:
												if(cart_velocity <= 0.010814413893967867):
													return True
												else:
													if(pole_angular_velocity <= 0.013891591224819422):
														if(cart_position > 0.10056750103831291):
															if(pole_angular_velocity <= 0.0038936606142669916):
																if(cart_velocity <= 0.029507619328796864):
																	if(pole_angle > -0.0029048542492091656):
																		if(pole_angle <= -0.0028971917927265167):
																			return True
																else:
																	return True
															else:
																if(pole_angular_velocity <= 0.004967804299667478):
																	if(cart_position > 0.10610519349575043):
																		return True
																else:
																	return True
													else:
														if(cart_position <= 0.09348141774535179):
															if(pole_angle <= -0.0029353046556934714):
																if(cart_velocity > 0.030934919603168964):
																	if(cart_velocity <= 0.03389703668653965):
																		return True
															else:
																return True
														else:
															return True
										else:
											if(cart_position <= 0.06067943572998047):
												if(pole_angle > -0.003217127756215632):
													if(pole_angular_velocity > 0.015943866223096848):
														if(cart_velocity > 0.03845231980085373):
															return True
											else:
												if(pole_angular_velocity <= 0.011252065654844046):
													if(cart_position <= 0.08284078538417816):
														if(pole_angle <= -0.003520656260661781):
															if(cart_velocity > 0.03915894031524658):
																return True
													else:
														return True
												else:
													return True
									else:
										if(cart_position <= 0.016707180999219418):
											if(cart_velocity > 0.041155051440000534):
												return True
										else:
											if(cart_velocity <= 0.027955709025263786):
												if(pole_angle <= -0.0030310993315652013):
													if(cart_position > 0.032785420306026936):
														if(pole_angular_velocity <= 0.03912240266799927):
															if(pole_angle > -0.00381067197304219):
																if(cart_position > 0.0525374636054039):
																	if(pole_angular_velocity <= 0.0272164149209857):
																		if(pole_angle > -0.0033471306087449193):
																			if(cart_velocity <= 0.023487509228289127):
																				return True
																	else:
																		if(cart_velocity <= 0.010945013258606195):
																			if(cart_position > 0.07721168920397758):
																				return True
																		else:
																			return True
														else:
															return True
											else:
												if(cart_position <= 0.0451427660882473):
													if(pole_angular_velocity <= 0.03581596165895462):
														if(cart_velocity <= 0.03921561315655708):
															if(pole_angle > -0.0035452591255307198):
																if(pole_angle <= -0.0034620248479768634):
																	return True
														else:
															return True
													else:
														if(pole_angular_velocity <= 0.04756841994822025):
															if(cart_velocity <= 0.04241124168038368):
																return True
															else:
																if(cart_velocity > 0.04324964992702007):
																	return True
												else:
													if(cart_position <= 0.0647168904542923):
														return True
						else:
							if(pole_angular_velocity <= 0.03501200117170811):
								if(pole_angle <= -0.004647788591682911):
									if(cart_velocity <= 0.0021335596102289855):
										if(pole_angular_velocity > 0.026843409053981304):
											if(cart_velocity <= -0.018497398123145103):
												if(cart_position > 0.15625044703483582):
													if(cart_position <= 0.15671385824680328):
														return True
													else:
														if(pole_angle > -0.005865723127499223):
															if(cart_velocity <= -0.04620126076042652):
																return True
											else:
												if(pole_angle <= -0.007869185414165258):
													if(cart_velocity <= -0.016994466073811054):
														return True
												else:
													return True
									else:
										if(pole_angle > -0.009122591931372881):
											if(cart_position > 0.1417383775115013):
												return True
								else:
									if(cart_position <= 0.1556118205189705):
										if(cart_velocity <= -0.027048157528042793):
											if(pole_angle <= -0.002863004570826888):
												if(pole_angular_velocity <= 0.032997315749526024):
													if(cart_velocity > -0.03298007883131504):
														if(pole_angular_velocity > 0.021276206709444523):
															if(cart_position > 0.1407201811671257):
																return True
												else:
													if(pole_angle > -0.0034950225381180644):
														return True
											else:
												return True
										else:
											if(pole_angular_velocity <= 0.013515433296561241):
												if(cart_velocity > -0.009850638918578625):
													return True
											else:
												if(pole_angular_velocity <= 0.023441744968295097):
													if(pole_angle <= -0.0034919879399240017):
														if(cart_position > 0.14066915214061737):
															return True
													else:
														return True
												else:
													return True
									else:
										if(pole_angular_velocity > 0.016769805923104286):
											if(pole_angle <= -0.0034697067458182573):
												return True
											else:
												if(pole_angle > -0.0031667385483160615):
													return True
							else:
								if(pole_angle <= -0.00673403381370008):
									if(cart_velocity <= -0.030254825949668884):
										if(cart_position > 0.16148946434259415):
											if(pole_angle > -0.009226627182215452):
												if(cart_velocity > -0.047227516770362854):
													return True
									else:
										if(pole_angle <= -0.009375588037073612):
											if(cart_position <= 0.16660825908184052):
												if(pole_angle > -0.010481588542461395):
													if(cart_velocity > -0.016520745120942593):
														return True
											else:
												return True
										else:
											return True
								else:
									if(cart_velocity <= -0.04539643041789532):
										if(cart_position > 0.15098974108695984):
											return True
									else:
										if(pole_angle <= -0.00576742016710341):
											if(cart_velocity <= -0.040021127089858055):
												if(pole_angle <= -0.00638415408320725):
													return True
											else:
												return True
										else:
											return True
					else:
						if(cart_position <= 0.09331047907471657):
							if(cart_velocity <= -0.020688110031187534):
								if(pole_angle > -0.002214653533883393):
									if(cart_velocity > -0.023455566726624966):
										return True
							else:
								if(cart_position <= 0.025653474032878876):
									if(cart_velocity > 0.03904993645846844):
										return True
								else:
									if(cart_position <= 0.08292276412248611):
										if(pole_angular_velocity <= 0.005549541674554348):
											if(cart_position > 0.07141547277569771):
												if(pole_angular_velocity > 0.0011834462056867778):
													return True
										else:
											if(pole_angle <= -0.0026405659737065434):
												if(pole_angle <= -0.0026862743543460965):
													if(cart_velocity > -0.010835300199687481):
														if(cart_position <= 0.07686424627900124):
															return True
														else:
															if(cart_position > 0.07982700318098068):
																return True
												else:
													if(pole_angle > -0.0026656626723706722):
														if(cart_velocity > -0.00040412519592791796):
															return True
											else:
												if(cart_position <= 0.056962911039590836):
													if(cart_velocity <= 0.0164274787530303):
														if(pole_angular_velocity > 0.04101096652448177):
															if(pole_angle > -0.0024843155406415462):
																return True
													else:
														if(pole_angular_velocity > 0.012490851804614067):
															if(pole_angular_velocity <= 0.033056655898690224):
																if(cart_velocity > 0.029383954592049122):
																	return True
															else:
																return True
												else:
													if(cart_velocity <= -0.012185124680399895):
														if(pole_angle <= -0.0022241852711886168):
															return True
													else:
														if(pole_angle <= -0.002586945192888379):
															if(pole_angle <= -0.002595498342998326):
																return True
														else:
															if(cart_position <= 0.07959067076444626):
																return True
															else:
																if(cart_position > 0.08023151010274887):
																	return True
									else:
										if(pole_angle <= -0.0022766987094655633):
											if(cart_position <= 0.08629100024700165):
												if(pole_angle > -0.002646252978593111):
													if(cart_velocity <= 0.016849886626005173):
														return True
													else:
														if(pole_angular_velocity <= -0.002419115975499153):
															return True
											else:
												if(cart_velocity <= 0.03295582812279463):
													if(cart_position <= 0.09274518489837646):
														if(pole_angle <= -0.002771042985841632):
															return True
														else:
															if(pole_angle > -0.0023369689006358385):
																if(pole_angle <= -0.0023349844850599766):
																	return True
													else:
														if(cart_position <= 0.09321341663599014):
															return True
												else:
													return True
										else:
											if(pole_angular_velocity > -0.0024712298763915896):
												if(pole_angular_velocity <= 0.03308551944792271):
													if(cart_velocity <= -0.0004852371057495475):
														if(pole_angular_velocity > 0.028722570277750492):
															if(pole_angular_velocity <= 0.03257204219698906):
																return True
													else:
														if(cart_position <= 0.08829068392515182):
															if(pole_angular_velocity > 0.009508394170552492):
																if(cart_position <= 0.08785121887922287):
																	return True
														else:
															return True
												else:
													if(cart_velocity <= -0.01712101884186268):
														if(cart_velocity <= -0.01761701237410307):
															return True
													else:
														return True
						else:
							if(cart_position <= 0.1382184401154518):
								if(cart_position <= 0.10393159091472626):
									if(pole_angle <= -0.0023264142218977213):
										if(cart_velocity <= 0.027831070125102997):
											if(pole_angular_velocity <= 0.04054470546543598):
												if(pole_angular_velocity > 0.027968290261924267):
													if(cart_velocity <= -0.01378049748018384):
														if(pole_angular_velocity > 0.03783752769231796):
															if(pole_angular_velocity <= 0.038125962018966675):
																return True
													else:
														if(pole_angle <= -0.0024933365639299154):
															return True
											else:
												if(cart_velocity <= -0.030172111466526985):
													if(cart_position > 0.1033339612185955):
														return True
												else:
													if(cart_velocity <= -0.02677830122411251):
														if(pole_angular_velocity > 0.04463382437825203):
															if(cart_position > 0.09443212300539017):
																if(pole_angle <= -0.0023900215746834874):
																	return True
																else:
																	if(cart_position <= 0.09918142110109329):
																		return True
													else:
														return True
										else:
											return True
									else:
										if(cart_velocity <= -0.027684501372277737):
											if(pole_angle <= -0.0022814898984506726):
												if(pole_angular_velocity > 0.04210546799004078):
													return True
											else:
												if(pole_angular_velocity > 0.04817936196923256):
													if(cart_velocity > -0.03428362496197224):
														return True
										else:
											if(pole_angular_velocity <= 0.035358285531401634):
												if(cart_velocity > -0.015495395753532648):
													if(pole_angular_velocity <= 0.028679090552031994):
														if(cart_position <= 0.09936714172363281):
															if(pole_angle <= -0.0020179704297333956):
																if(cart_position <= 0.09833598509430885):
																	if(cart_velocity > 0.009420171147212386):
																		if(cart_position <= 0.09641527384519577):
																			if(cart_position > 0.0939447395503521):
																				return True
																else:
																	if(cart_velocity > -0.0027193025161977857):
																		return True
															else:
																return True
														else:
															if(pole_angle > -0.001980450004339218):
																if(pole_angle <= -0.0019481866038404405):
																	return True
													else:
														if(cart_position <= 0.0988062173128128):
															if(cart_velocity > -0.011521241627633572):
																return True
														else:
															return True
											else:
												if(pole_angle <= -0.0019059788901358843):
													if(cart_velocity <= -0.021692140959203243):
														if(cart_velocity <= -0.022250782698392868):
															if(cart_position <= 0.098397396504879):
																if(pole_angular_velocity > 0.041841896250844):
																	return True
															else:
																return True
													else:
														return True
								else:
									if(cart_velocity <= 0.020437492057681084):
										if(cart_velocity <= 0.0036100936122238636):
											if(pole_angular_velocity <= 0.03972897678613663):
												if(cart_position <= 0.12804263830184937):
													if(pole_angular_velocity <= 0.03021401260048151):
														if(pole_angle > -0.0019759349524974823):
															if(pole_angle <= -0.0019745066529139876):
																return True
													else:
														if(cart_velocity <= -0.01987559162080288):
															if(pole_angle <= -0.00194970186566934):
																if(cart_velocity <= -0.020240798592567444):
																	if(cart_velocity > -0.022055163979530334):
																		if(pole_angular_velocity > 0.03514138422906399):
																			return True
																else:
																	if(pole_angular_velocity > 0.03263545781373978):
																		return True
															else:
																return True
														else:
															if(cart_position > 0.1056753359735012):
																return True
												else:
													if(cart_velocity > -0.020138584077358246):
														if(cart_position <= 0.13476929813623428):
															return True
											else:
												if(cart_velocity <= -0.03153453767299652):
													if(pole_angular_velocity > 0.04551358334720135):
														if(cart_velocity <= -0.0402344074100256):
															if(cart_position > 0.11741110682487488):
																return True
														else:
															if(cart_position <= 0.10710420086979866):
																if(cart_velocity > -0.03723311051726341):
																	return True
															else:
																return True
												else:
													if(pole_angle > -0.0024027179460972548):
														return True
										else:
											if(pole_angular_velocity <= 0.0013724692398682237):
												if(cart_position <= 0.12767338752746582):
													if(cart_velocity > 0.016581224277615547):
														if(pole_angular_velocity > -0.000504877622006461):
															return True
												else:
													if(pole_angle <= -0.0025479135802015662):
														return True
													else:
														if(cart_position <= 0.1279309317469597):
															return True
														else:
															if(cart_velocity <= 0.0059395707212388515):
																return True
											else:
												if(cart_position > 0.10786911100149155):
													if(pole_angular_velocity <= 0.0021084679756313562):
														if(cart_velocity > 0.006921001011505723):
															if(cart_position > 0.11562339961528778):
																return True
													else:
														return True
									else:
										if(pole_angular_velocity > -0.0016216040239669383):
											if(pole_angle > -0.0026121154660359025):
												return True
							else:
								if(pole_angular_velocity <= 0.030431772582232952):
									if(cart_velocity <= -0.026964817196130753):
										if(pole_angular_velocity <= 0.02668101154267788):
											if(cart_position > 0.1594286933541298):
												return True
										else:
											if(cart_velocity > -0.04339595139026642):
												return True
									else:
										if(cart_velocity <= -0.015984494239091873):
											return True
								else:
									if(cart_velocity > -0.049806367605924606):
										if(pole_angle <= -0.0019152543391101062):
											return True
				else:
					if(pole_angle <= -0.00326326722279191):
						if(cart_velocity <= -0.028177586384117603):
							if(cart_position <= 0.13184284418821335):
								if(pole_angle <= -0.0041852351278066635):
									if(pole_angular_velocity <= 0.07315737009048462):
										if(pole_angular_velocity > 0.07221377268433571):
											if(pole_angular_velocity <= 0.07223759591579437):
												return True
									else:
										if(pole_angle <= -0.004658026387915015):
											if(cart_position <= 0.0919075645506382):
												if(pole_angular_velocity <= 0.07326892763376236):
													return True
												else:
													if(pole_angle > -0.004825372947379947):
														if(pole_angular_velocity <= 0.0757005363702774):
															return True
														else:
															if(cart_velocity > -0.036784423515200615):
																if(cart_velocity <= -0.03316447418183088):
																	return True
											else:
												return True
										else:
											if(cart_velocity <= -0.04425456374883652):
												if(pole_angular_velocity <= 0.08257390931248665):
													if(cart_position > 0.09035815671086311):
														if(cart_position <= 0.09447632730007172):
															return True
												else:
													if(cart_velocity > -0.052066951990127563):
														return True
											else:
												return True
								else:
									if(pole_angular_velocity <= 0.07383685186505318):
										if(pole_angular_velocity <= 0.06224820017814636):
											if(cart_velocity > -0.03502323478460312):
												if(pole_angle <= -0.00339214492123574):
													if(cart_velocity <= -0.03438927046954632):
														return True
													else:
														if(cart_velocity > -0.02837305422872305):
															if(cart_velocity <= -0.028252682648599148):
																return True
												else:
													if(cart_position <= 0.10096346959471703):
														if(pole_angular_velocity > 0.05059307441115379):
															if(cart_position > 0.0929693952202797):
																return True
													else:
														return True
										else:
											if(pole_angle <= -0.0036747048143297434):
												if(cart_velocity <= -0.03077466692775488):
													if(pole_angle <= -0.004168694140389562):
														if(pole_angular_velocity > 0.06793864443898201):
															return True
													else:
														if(pole_angular_velocity <= 0.07236640900373459):
															if(pole_angle <= -0.004100146470591426):
																if(pole_angle > -0.004115262301638722):
																	return True
														else:
															if(cart_position > 0.08831541612744331):
																return True
												else:
													if(pole_angle <= -0.0037887056823819876):
														return True
											else:
												if(cart_velocity <= -0.04211982525885105):
													if(pole_angular_velocity <= 0.06598488613963127):
														if(cart_position > 0.09837179258465767):
															return True
													else:
														if(cart_position > 0.08665787801146507):
															if(pole_angular_velocity <= 0.0695282481610775):
																if(cart_position <= 0.09220806881785393):
																	if(cart_velocity > -0.04473506473004818):
																		if(cart_position > 0.0903465636074543):
																			return True
																else:
																	return True
															else:
																return True
												else:
													if(cart_position <= 0.09003398567438126):
														if(cart_velocity <= -0.03545811027288437):
															if(pole_angular_velocity > 0.06628384813666344):
																if(pole_angle <= -0.003387675271369517):
																	return True
																else:
																	if(cart_velocity > -0.03758971765637398):
																		return True
														else:
															return True
													else:
														return True
									else:
										if(pole_angular_velocity <= 0.07642998918890953):
											if(cart_velocity <= -0.04867844469845295):
												if(cart_position > 0.0864558070898056):
													if(cart_velocity > -0.051630692556500435):
														if(pole_angle <= -0.004020826192572713):
															if(cart_position > 0.08775181695818901):
																return True
														else:
															return True
											else:
												if(pole_angular_velocity <= 0.07602576538920403):
													return True
										else:
											if(cart_velocity <= -0.051999300718307495):
												if(pole_angle > -0.0038336300058290362):
													return True
											else:
												if(pole_angle > -0.004177968483418226):
													return True
							else:
								if(pole_angle <= -0.013499235268682241):
									if(cart_position > 0.16394741833209991):
										if(cart_position <= 0.16467012465000153):
											return True
										else:
											if(pole_angle <= -0.014278823044151068):
												if(cart_velocity > -0.040243545547127724):
													if(pole_angular_velocity > 0.07440816983580589):
														return True
											else:
												if(pole_angle <= -0.013803570531308651):
													return True
								else:
									if(pole_angular_velocity <= 0.049851786345243454):
										if(pole_angle > -0.009653241373598576):
											return True
									else:
										if(cart_position <= 0.15588058531284332):
											if(cart_position <= 0.1553429514169693):
												if(cart_velocity <= -0.04886636137962341):
													if(pole_angle > -0.009765552822500467):
														return True
												else:
													if(pole_angular_velocity <= 0.0507539939135313):
														if(cart_velocity <= -0.04308514483273029):
															return True
													else:
														if(cart_velocity <= -0.04590136744081974):
															if(cart_velocity <= -0.0462156031280756):
																return True
														else:
															return True
										else:
											return True
						else:
							if(pole_angle <= -0.0043630595318973064):
								if(pole_angle <= -0.009362572804093361):
									if(pole_angle <= -0.01880499441176653):
										if(pole_angular_velocity <= 0.07810256630182266):
											if(cart_position > 0.14993605017662048):
												if(pole_angle > -0.02112623956054449):
													if(cart_velocity > -0.009810342788114212):
														return True
										else:
											if(pole_angle > -0.0193949518725276):
												if(pole_angular_velocity <= 0.08185091987252235):
													return True
									else:
										if(pole_angular_velocity <= 0.0601644404232502):
											if(pole_angle <= -0.013923576567322016):
												if(cart_velocity <= 0.03708532825112343):
													if(cart_velocity > 0.00636751763522625):
														if(cart_position > 0.12082241103053093):
															return True
												else:
													return True
											else:
												if(pole_angle <= -0.01039755018427968):
													if(pole_angle <= -0.012933334335684776):
														if(cart_position > 0.10044464096426964):
															if(pole_angular_velocity <= 0.054343149065971375):
																if(cart_velocity > 0.010982813779264688):
																	return True
															else:
																return True
													else:
														return True
												else:
													if(pole_angle > -0.009649902116507292):
														return True
										else:
											if(cart_position <= 0.0753144882619381):
												if(pole_angular_velocity > 0.07302021235227585):
													if(cart_velocity <= 0.025199464056640863):
														if(pole_angular_velocity > 0.08341487124562263):
															return True
													else:
														return True
											else:
												if(cart_velocity <= -0.026865716092288494):
													if(pole_angle > -0.014148877933621407):
														return True
												else:
													if(pole_angular_velocity <= 0.08121298253536224):
														return True
													else:
														if(pole_angular_velocity > 0.08173271641135216):
															return True
								else:
									if(pole_angle <= -0.005766119109466672):
										if(cart_position <= 0.09414050355553627):
											if(cart_velocity <= 0.042570214718580246):
												if(cart_velocity <= 0.015517969615757465):
													if(pole_angular_velocity <= 0.0709017887711525):
														if(cart_velocity <= 0.012645615730434656):
															if(cart_position > 0.07520683482289314):
																if(cart_position <= 0.07551132142543793):
																	return True
														else:
															if(cart_velocity <= 0.01355833699926734):
																return True
													else:
														if(pole_angular_velocity <= 0.07112116366624832):
															return True
														else:
															if(pole_angle <= -0.006047762464731932):
																if(pole_angle > -0.006618518149480224):
																	if(pole_angle <= -0.006579647539183497):
																		return True
																	else:
																		if(pole_angular_velocity > 0.08005568012595177):
																			if(pole_angular_velocity <= 0.08018364012241364):
																				return True
																			else:
																				if(cart_position > 0.051039159297943115):
																					return True
															else:
																if(cart_position <= 0.0492896419018507):
																	if(pole_angle <= -0.006000253837555647):
																		return True
																else:
																	if(pole_angle <= -0.005824453197419643):
																		return True
												else:
													if(cart_position <= 0.05787615478038788):
														if(pole_angular_velocity > 0.061242811381816864):
															if(cart_position <= 0.01842366438359022):
																if(cart_velocity > 0.035024991258978844):
																	if(cart_velocity <= 0.03996996209025383):
																		return True
															else:
																if(pole_angle > -0.008809386286884546):
																	if(cart_position <= 0.02217838354408741):
																		if(pole_angular_velocity > 0.07214377075433731):
																			return True
																	else:
																		return True
													else:
														return True
											else:
												return True
										else:
											if(pole_angular_velocity > 0.04977840557694435):
												return True
									else:
										if(cart_position <= 0.06542211771011353):
											if(pole_angular_velocity <= 0.0750722587108612):
												if(cart_velocity <= 0.0034692706540226936):
													if(pole_angular_velocity <= 0.06019025854766369):
														if(cart_position > 0.06526114419102669):
															return True
													else:
														if(cart_position > 0.040417058393359184):
															if(pole_angle <= -0.0046766651794314384):
																if(pole_angular_velocity <= 0.07268042489886284):
																	if(cart_velocity <= -0.013121559750288725):
																		if(pole_angle > -0.004880143329501152):
																			if(pole_angle <= -0.004836946958675981):
																				return True
																	else:
																		if(cart_position <= 0.05286150611937046):
																			if(pole_angular_velocity > 0.07119154930114746):
																				return True
																		else:
																			if(pole_angle > -0.005623266100883484):
																				return True
																else:
																	if(pole_angular_velocity <= 0.07344063743948936):
																		return True
															else:
																if(cart_velocity > -0.01654118625447154):
																	return True
												else:
													if(cart_position <= 0.03776909410953522):
														if(cart_velocity > 0.012872098945081234):
															if(pole_angle <= -0.005708419252187014):
																return True
															else:
																if(cart_position > -0.001437941929907538):
																	if(pole_angular_velocity <= 0.0565667599439621):
																		if(cart_position <= 0.03318061679601669):
																			if(cart_velocity > 0.028245840221643448):
																				return True
																		else:
																			return True
																	else:
																		if(pole_angle <= -0.004693459486588836):
																			if(cart_position <= 0.002916772267781198):
																				if(cart_position <= 0.001269494867301546):
																					return True
																			else:
																				return True
													else:
														if(pole_angle <= -0.004610700998455286):
															if(cart_velocity <= 0.010144409723579884):
																return True
															else:
																if(pole_angular_velocity <= 0.055480148643255234):
																	return True
														else:
															if(cart_velocity > 0.008009495446458459):
																return True
											else:
												if(pole_angle > -0.005506416782736778):
													if(pole_angle <= -0.004471395397558808):
														if(pole_angular_velocity <= 0.08603126183152199):
															if(pole_angle <= -0.005421989830210805):
																if(cart_velocity > -0.016374195460230112):
																	return True
															else:
																if(cart_position <= 0.027994547970592976):
																	if(cart_velocity > -0.009329454507678747):
																		return True
																else:
																	return True
										else:
											if(cart_velocity <= -0.0021035323152318597):
												if(cart_velocity <= -0.01080691209062934):
													if(pole_angle <= -0.004440441960468888):
														if(pole_angular_velocity > 0.06449469178915024):
															if(cart_position > 0.0730629675090313):
																return True
													else:
														if(pole_angle <= -0.004411063622683287):
															return True
												else:
													if(pole_angular_velocity <= 0.05311620607972145):
														if(cart_velocity <= -0.009017333388328552):
															return True
													else:
														return True
											else:
												return True
							else:
								if(cart_position <= 0.0870075412094593):
									if(cart_position > -0.0038404426886700094):
										if(cart_position <= 0.027637461200356483):
											if(cart_velocity <= 0.01770114805549383):
												if(pole_angular_velocity > 0.06912025064229965):
													if(cart_velocity > -0.0053700299467891455):
														if(cart_position > 0.004656660559703596):
															return True
											else:
												return True
										else:
											if(pole_angular_velocity <= 0.05702747218310833):
												if(pole_angular_velocity <= 0.056696921586990356):
													if(cart_velocity <= -0.01726914569735527):
														if(pole_angle > -0.0038980102399364114):
															return True
													else:
														if(pole_angle <= -0.004034565296024084):
															return True
														else:
															if(pole_angular_velocity <= 0.05026067979633808):
																if(cart_position <= 0.059557460248470306):
																	if(cart_velocity <= 0.015206036623567343):
																		return True
																	else:
																		if(cart_velocity > 0.02136725513264537):
																			return True
																else:
																	if(cart_velocity <= -0.015114712063223124):
																		return True
															else:
																if(pole_angle > -0.003992552636191249):
																	if(cart_position <= 0.04862559773027897):
																		if(cart_position <= 0.03894016519188881):
																			return True
																	else:
																		return True
											else:
												if(pole_angle <= -0.004103736486285925):
													if(cart_velocity <= -0.017528780736029148):
														if(pole_angular_velocity <= 0.07002386078238487):
															if(cart_position > 0.07142163813114166):
																return True
														else:
															return True
													else:
														return True
												else:
													if(cart_velocity <= -0.026572921313345432):
														if(pole_angular_velocity > 0.06297146156430244):
															return True
													else:
														return True
								else:
									if(cart_velocity <= -0.022243548184633255):
										if(pole_angle <= -0.0034285085275769234):
											if(cart_position > 0.09602853283286095):
												if(pole_angular_velocity > 0.04946975223720074):
													return True
										else:
											return True
									else:
										if(pole_angular_velocity <= 0.04931012541055679):
											if(cart_velocity <= -0.021728073246777058):
												return True
										else:
											return True
					else:
						if(pole_angular_velocity <= 0.06650596857070923):
							if(pole_angle <= -0.0026623549638316035):
								if(cart_velocity <= -0.0409690085798502):
									if(cart_position <= 0.11116202175617218):
										if(pole_angular_velocity <= 0.06589268147945404):
											if(pole_angular_velocity > 0.06146579049527645):
												if(cart_position > 0.09548598900437355):
													if(cart_velocity > -0.048424385488033295):
														return True
										else:
											if(pole_angular_velocity <= 0.06611968576908112):
												return True
									else:
										if(pole_angle > -0.002914618467912078):
											return True
								else:
									if(pole_angular_velocity <= 0.05113407224416733):
										if(cart_velocity > -0.030079259537160397):
											if(pole_angle <= -0.002947781467810273):
												if(cart_position <= 0.08729927614331245):
													if(cart_velocity <= -0.002407952619250864):
														if(pole_angle > -0.0031430585077032447):
															if(cart_velocity <= -0.007466591894626617):
																return True
													else:
														return True
												else:
													return True
											else:
												if(pole_angular_velocity <= 0.04861811175942421):
													return True
									else:
										if(cart_velocity <= -0.03313852474093437):
											if(pole_angular_velocity <= 0.06050352565944195):
												if(cart_position <= 0.09356216713786125):
													if(pole_angular_velocity > 0.05786159634590149):
														if(cart_velocity > -0.03866715356707573):
															if(cart_position > 0.09052954241633415):
																return True
												else:
													if(pole_angle <= -0.0029288576915860176):
														if(cart_position <= 0.09521977975964546):
															return True
													else:
														if(cart_velocity <= -0.03406117856502533):
															return True
											else:
												if(cart_position > 0.0847288928925991):
													return True
										else:
											if(cart_position > 0.017315073870122433):
												if(pole_angular_velocity <= 0.06630289554595947):
													if(cart_position <= 0.02853291481733322):
														if(cart_velocity > 0.012296652421355247):
															return True
													else:
														if(cart_position <= 0.04583653807640076):
															if(cart_velocity > -0.006729455199092627):
																return True
														else:
															if(pole_angle <= -0.003119896864518523):
																if(pole_angle <= -0.003131953999400139):
																	return True
															else:
																return True
							else:
								if(cart_position <= 0.017261892091482878):
									if(cart_velocity <= 0.03906405344605446):
										if(cart_velocity > 0.02911505475640297):
											if(cart_velocity <= 0.03352705016732216):
												return True
									else:
										return True
								else:
									if(pole_angular_velocity <= 0.049998046830296516):
										if(cart_velocity <= -0.03396899625658989):
											if(pole_angular_velocity <= 0.0490652434527874):
												if(cart_position <= 0.10621108114719391):
													if(pole_angle > -0.0019560055807232857):
														return True
												else:
													return True
											else:
												if(cart_velocity > -0.03632052801549435):
													if(cart_position > 0.09868581965565681):
														return True
										else:
											if(pole_angular_velocity <= 0.04852062836289406):
												if(cart_velocity <= -0.03245381824672222):
													return True
											else:
												if(cart_velocity <= -0.017346044536679983):
													if(cart_position > 0.08529416099190712):
														if(cart_position <= 0.09190772101283073):
															if(cart_velocity > -0.030077653005719185):
																return True
														else:
															return True
												else:
													return True
									else:
										if(cart_velocity <= -0.04699173383414745):
											if(pole_angular_velocity <= 0.057829516008496284):
												if(pole_angle > -0.001989826268982142):
													return True
											else:
												if(cart_position <= 0.10054532438516617):
													if(pole_angular_velocity > 0.06564878299832344):
														return True
												else:
													return True
										else:
											if(pole_angle <= -0.0023287987569347024):
												if(cart_velocity <= -0.043798159807920456):
													if(pole_angular_velocity > 0.05745659954845905):
														if(cart_position > 0.08938435837626457):
															if(pole_angle <= -0.0023512464249506593):
																return True
												else:
													if(pole_angle <= -0.002331192488782108):
														if(cart_velocity <= -0.03507396951317787):
															if(pole_angular_velocity <= 0.057600535452365875):
																if(cart_position > 0.09629738703370094):
																	if(pole_angular_velocity <= 0.05092689208686352):
																		if(pole_angular_velocity <= 0.05069569684565067):
																			return True
																	else:
																		return True
															else:
																if(pole_angular_velocity <= 0.059339242056012154):
																	if(cart_position <= 0.09278685599565506):
																		if(pole_angular_velocity <= 0.05805807374417782):
																			return True
																	else:
																		return True
																else:
																	return True
														else:
															if(cart_position <= 0.045522063970565796):
																if(cart_velocity > 0.00301248487085104):
																	return True
															else:
																return True
											else:
												if(pole_angular_velocity <= 0.05365825071930885):
													if(pole_angular_velocity <= 0.05361645482480526):
														if(cart_velocity <= -0.040743038058280945):
															if(cart_velocity <= -0.04246478155255318):
																return True
														else:
															if(cart_velocity <= -0.038528257980942726):
																if(cart_position > 0.09806263074278831):
																	return True
															else:
																return True
												else:
													return True
						else:
							if(cart_position <= 0.020634266547858715):
								if(cart_velocity <= 1.2403354048728943e-05):
									if(pole_angular_velocity > 0.08326425775885582):
										return True
								else:
									if(pole_angle <= -0.0030111162923276424):
										if(pole_angular_velocity > 0.07370377704501152):
											return True
									else:
										return True
							else:
								if(pole_angle <= -0.0029084477573633194):
									if(cart_velocity <= -0.04735936410725117):
										if(pole_angular_velocity <= 0.07599300518631935):
											if(cart_position <= 0.08863015845417976):
												if(pole_angle <= -0.0031423838809132576):
													if(pole_angular_velocity > 0.07113809138536453):
														return True
											else:
												if(pole_angular_velocity > 0.06785981729626656):
													return True
										else:
											return True
									else:
										if(pole_angular_velocity <= 0.06762143597006798):
											if(pole_angular_velocity <= 0.06731854006648064):
												return True
										else:
											if(pole_angle <= -0.0032291592797264457):
												if(pole_angle <= -0.0032459113281220198):
													return True
											else:
												return True
								else:
									if(pole_angular_velocity <= 0.06682152673602104):
										if(pole_angular_velocity <= 0.06672388687729836):
											return True
									else:
										if(cart_position <= 0.03819701448082924):
											if(cart_velocity > -0.02599426545202732):
												if(pole_angular_velocity <= 0.06891779974102974):
													if(pole_angular_velocity <= 0.06779113784432411):
														return True
												else:
													return True
										else:
											if(pole_angle <= -0.0027891843346878886):
												if(pole_angle <= -0.0027906530303880572):
													return True
											else:
												return True
			else:
				if(pole_angle <= -0.0007869610853958875):
					if(cart_position <= 0.10362277552485466):
						if(pole_angular_velocity <= 0.0500108078122139):
							if(cart_velocity <= -0.034897370263934135):
								if(pole_angle <= -0.0010334622929804027):
									if(pole_angular_velocity > 0.04926906153559685):
										if(cart_position <= 0.09797405824065208):
											if(pole_angle > -0.0015414634253829718):
												return True
								else:
									if(pole_angle <= -0.0009441797155886889):
										return True
							else:
								if(pole_angle <= -0.0013447722303681076):
									if(cart_position <= 0.0996936522424221):
										if(pole_angular_velocity <= -0.001844158861786127):
											if(cart_position <= 0.07885867729783058):
												return True
										else:
											if(cart_position > 0.004009153140941635):
												if(cart_velocity <= -0.02901155687868595):
													if(pole_angular_velocity <= 0.04918772540986538):
														if(pole_angle <= -0.0018814627546817064):
															return True
														else:
															if(pole_angle > -0.0015877680270932615):
																if(cart_velocity <= -0.029236765578389168):
																	return True
													else:
														return True
												else:
													if(pole_angular_velocity <= 0.037607358768582344):
														if(cart_position > 0.029486372135579586):
															if(cart_velocity > -0.020390893332660198):
																if(pole_angular_velocity <= 0.02226266171783209):
																	if(cart_velocity <= 0.006061046151444316):
																		if(cart_position <= 0.09523747488856316):
																			if(cart_position > 0.09065297618508339):
																				return True
																	else:
																		if(pole_angular_velocity <= 0.006514824228361249):
																			if(pole_angular_velocity <= 0.005106482421979308):
																				if(cart_velocity <= 0.04237558878958225):
																					if(cart_velocity <= 0.03718138858675957):
																						if(cart_position <= 0.09196875244379044):
																							if(pole_angular_velocity > 0.0014506096486002207):
																								if(pole_angle > -0.0017591313808225095):
																									return True
																						else:
																							if(pole_angular_velocity <= -0.0006029208598192781):
																								if(pole_angular_velocity <= -0.0009860749123618007):
																									return True
																							else:
																								return True
																					else:
																						return True
																			else:
																				if(cart_position > 0.0826001949608326):
																					if(cart_velocity > 0.025851194746792316):
																						return True
																		else:
																			if(cart_position > 0.04280373826622963):
																				if(cart_position <= 0.09743732213973999):
																					if(cart_velocity <= 0.008160527795553207):
																						if(cart_velocity <= 0.007347285049036145):
																							return True
																					else:
																						return True
																else:
																	if(cart_velocity <= -0.012776792049407959):
																		if(cart_position <= 0.09717381745576859):
																			if(pole_angular_velocity > 0.035746855661273):
																				return True
																		else:
																			return True
																	else:
																		if(pole_angular_velocity <= 0.036909256130456924):
																			if(cart_position <= 0.044387754052877426):
																				if(pole_angular_velocity > 0.025392592884600163):
																					return True
																			else:
																				if(pole_angle <= -0.0018312832107767463):
																					if(pole_angle <= -0.0018383261049166322):
																						return True
																				else:
																					return True
																		else:
																			if(pole_angular_velocity > 0.03741239756345749):
																				return True
													else:
														if(pole_angular_velocity <= 0.04899458773434162):
															if(cart_velocity <= -0.025336971506476402):
																if(pole_angular_velocity <= 0.04110449180006981):
																	if(pole_angle <= -0.0015766200376674533):
																		return True
																else:
																	return True
															else:
																if(cart_position <= 0.049203408882021904):
																	if(cart_position <= 0.04599659517407417):
																		return True
																else:
																	return True
														else:
															if(cart_velocity > -0.00534153962507844):
																return True
									else:
										if(pole_angular_velocity <= 0.03780934400856495):
											if(cart_velocity <= -0.007132049184292555):
												if(pole_angular_velocity > 0.029285434633493423):
													if(cart_velocity <= -0.019250383600592613):
														if(cart_position <= 0.1001967191696167):
															return True
														else:
															if(cart_position <= 0.10343831777572632):
																if(cart_position > 0.10310786589980125):
																	if(cart_position <= 0.1032164990901947):
																		return True
															else:
																return True
													else:
														if(pole_angular_velocity <= 0.0299637820571661):
															if(cart_velocity > -0.014624059200286865):
																return True
														else:
															return True
											else:
												if(pole_angular_velocity <= 0.017269905656576157):
													if(pole_angular_velocity > 0.013039265759289265):
														if(pole_angular_velocity <= 0.015218986663967371):
															return True
												else:
													return True
										else:
											if(cart_velocity <= -0.03146792948246002):
												if(cart_position > 0.10243075713515282):
													return True
											else:
												if(pole_angle <= -0.0017940482357516885):
													if(cart_velocity > -0.027973808348178864):
														return True
												else:
													return True
								else:
									if(pole_angular_velocity <= -0.002346172113902867):
										if(pole_angular_velocity <= -0.0026357659371569753):
											if(pole_angle > -0.0011918052332475781):
												return True
									else:
										if(pole_angle <= -0.0007884819933678955):
											if(cart_position <= 0.10288223624229431):
												if(cart_position <= 0.020486188121140003):
													if(cart_velocity > 0.031239002011716366):
														return True
												else:
													if(cart_velocity <= -0.030336351133883):
														if(pole_angle > -0.0012401111307553947):
															if(cart_position <= 0.09017842262983322):
																if(cart_position <= 0.08873986452817917):
																	return True
															else:
																return True
													else:
														if(pole_angular_velocity <= 0.004391716094687581):
															if(cart_velocity > 0.017962940968573093):
																if(pole_angular_velocity <= 0.0018266490078531206):
																	if(pole_angular_velocity <= 0.00087622000137344):
																		if(pole_angle <= -0.001108424155972898):
																			if(pole_angle <= -0.001150874188169837):
																				return True
																		else:
																			return True
																	else:
																		if(cart_velocity <= 0.02467699721455574):
																			return True
																else:
																	return True
														else:
															if(pole_angle <= -0.0008135005482472479):
																if(pole_angle <= -0.0012278641224838793):
																	if(pole_angle <= -0.0012293452164158225):
																		if(cart_position <= 0.10102405771613121):
																			return True
																		else:
																			if(cart_position > 0.10104134678840637):
																				return True
																else:
																	return True
															else:
																if(pole_angle > -0.0008071023039519787):
																	return True
											else:
												if(pole_angular_velocity <= 0.026793353259563446):
													if(pole_angle > -0.0011783482041209936):
														if(cart_velocity > -0.011108689941465855):
															return True
												else:
													return True
						else:
							if(cart_position <= 0.021882755681872368):
								if(pole_angle <= -0.0008649779192637652):
									if(cart_velocity <= 0.008252863772213459):
										if(pole_angular_velocity > 0.060896722599864006):
											if(cart_velocity > -0.02139565721154213):
												if(cart_position <= 0.006778558250516653):
													if(pole_angular_velocity > 0.0832710787653923):
														return True
												else:
													if(cart_position <= 0.02146603725850582):
														return True
									else:
										if(cart_position <= -0.015297706238925457):
											if(pole_angle > -0.0011868292349390686):
												return True
										else:
											return True
							else:
								if(pole_angular_velocity <= 0.051036763936281204):
									if(pole_angular_velocity <= 0.05101337097585201):
										if(pole_angle <= -0.0018249309505335987):
											if(pole_angle <= -0.0018475850811228156):
												return True
										else:
											return True
								else:
									if(cart_position <= 0.09769611060619354):
										if(cart_position <= 0.04073875956237316):
											if(cart_position <= 0.040255120024085045):
												return True
										else:
											return True
									else:
										if(cart_position > 0.09795217588543892):
											if(pole_angular_velocity <= 0.054765574634075165):
												return True
											else:
												if(pole_angular_velocity > 0.055088818073272705):
													return True
					else:
						if(pole_angular_velocity <= 0.028850995004177094):
							if(pole_angle <= -0.0012334667262621224):
								if(cart_velocity <= 0.0023034142795950174):
									if(cart_position <= 0.15296725183725357):
										if(pole_angular_velocity <= 0.018301178701221943):
											if(cart_position <= 0.12618663161993027):
												if(cart_velocity <= -0.001968914526514709):
													if(cart_position <= 0.10727351158857346):
														if(cart_position > 0.10717272385954857):
															return True
												else:
													if(cart_velocity <= -0.0018665562965907156):
														return True
													else:
														if(pole_angular_velocity <= 0.01370904827490449):
															if(pole_angle > -0.0012670537689700723):
																if(pole_angle <= -0.0012523329933173954):
																	return True
														else:
															if(pole_angle <= -0.0016023728530853987):
																return True
											else:
												if(cart_velocity > -0.018275631591677666):
													if(pole_angular_velocity <= 0.007243889616802335):
														if(cart_position > 0.13564038276672363):
															return True
													else:
														return True
										else:
											if(cart_velocity <= -0.012257265392690897):
												if(pole_angular_velocity <= 0.027718016877770424):
													if(cart_position <= 0.14880792796611786):
														if(cart_position <= 0.13365760445594788):
															if(pole_angle > -0.001474771008361131):
																if(pole_angle <= -0.0014695521094836295):
																	return True
																else:
																	if(cart_velocity > -0.014401994179934263):
																		if(pole_angular_velocity > 0.02309029921889305):
																			return True
														else:
															if(cart_velocity > -0.03610582835972309):
																return True
													else:
														return True
												else:
													if(cart_position > 0.10609414055943489):
														if(pole_angular_velocity <= 0.028338276781141758):
															return True
											else:
												if(pole_angular_velocity <= 0.01994726900011301):
													if(pole_angle > -0.001530730165541172):
														if(cart_velocity <= -0.009864767082035542):
															if(cart_position > 0.11114397644996643):
																return True
														else:
															return True
												else:
													if(cart_velocity <= -0.011709703598171473):
														if(cart_velocity <= -0.011744209099560976):
															if(cart_position > 0.10529864951968193):
																return True
													else:
														return True
									else:
										return True
								else:
									if(pole_angular_velocity <= 0.001319164759479463):
										if(cart_velocity <= 0.009893775451928377):
											if(cart_position > 0.1268785148859024):
												return True
										else:
											if(pole_angular_velocity <= -0.000737299065804109):
												if(cart_velocity > 0.01833813264966011):
													if(cart_position > 0.10664916411042213):
														return True
											else:
												return True
									else:
										if(cart_position > 0.10558238625526428):
											if(cart_velocity <= 0.003539323224686086):
												if(cart_velocity <= 0.0032996053341776133):
													return True
											else:
												return True
							else:
								if(pole_angular_velocity <= -1.7234428014489822e-05):
									if(cart_velocity <= 0.012621663976460695):
										if(cart_velocity > 0.008312990423291922):
											if(cart_position > 0.11518201231956482):
												return True
									else:
										if(pole_angle <= -0.0009167112875729799):
											return True
								else:
									if(cart_velocity <= 0.0028134946478530765):
										if(pole_angular_velocity <= 0.021130680106580257):
											if(cart_velocity <= -0.010847708210349083):
												if(cart_position <= 0.1311185508966446):
													if(pole_angle > -0.0008670739771332592):
														if(cart_velocity > -0.011934771202504635):
															return True
												else:
													if(cart_velocity > -0.0374488215893507):
														if(pole_angular_velocity > 0.006144134560599923):
															if(cart_position <= 0.14662156254053116):
																if(cart_velocity > -0.025750642642378807):
																	return True
															else:
																return True
											else:
												if(pole_angular_velocity <= 0.015601805411279202):
													if(cart_position <= 0.11229702830314636):
														if(cart_velocity <= -0.0019663007115013897):
															if(pole_angular_velocity <= 0.015253538265824318):
																if(cart_position > 0.11208513379096985):
																	if(cart_velocity > -0.005063122604042292):
																		return True
															else:
																if(pole_angle > -0.0010283809097018093):
																	return True
														else:
															if(pole_angle <= -0.0010301914880983531):
																if(pole_angular_velocity > 0.011302157305181026):
																	return True
															else:
																return True
													else:
														if(pole_angular_velocity > 0.0011481966939754784):
															if(cart_velocity <= -0.008820691145956516):
																if(cart_position > 0.13301662355661392):
																	return True
															else:
																if(cart_position <= 0.1172645352780819):
																	if(pole_angular_velocity <= 0.011808987241238356):
																		if(cart_position <= 0.11252396553754807):
																			return True
																	else:
																		return True
																else:
																	return True
												else:
													if(pole_angle <= -0.0011256244033575058):
														if(pole_angular_velocity <= 0.017829335294663906):
															return True
													else:
														if(cart_velocity <= -0.005424595205113292):
															return True
														else:
															if(pole_angle <= -0.0011079993564635515):
																return True
										else:
											if(cart_velocity <= -0.024290835484862328):
												if(cart_position > 0.13444622606039047):
													if(cart_velocity > -0.04151551052927971):
														return True
											else:
												if(cart_position <= 0.10587016493082047):
													if(cart_velocity > -0.01637209951877594):
														if(cart_position <= 0.10444042831659317):
															if(pole_angle > -0.0010785507038235664):
																if(cart_velocity <= -0.011727487202733755):
																	return True
														else:
															return True
												else:
													return True
									else:
										if(pole_angular_velocity <= 0.0011975803645327687):
											if(cart_position > 0.11044373363256454):
												if(cart_velocity <= 0.0060984662268310785):
													if(pole_angle > -0.0009056646085809916):
														return True
												else:
													return True
										else:
											return True
						else:
							if(cart_position <= 0.10784570872783661):
								if(pole_angle <= -0.001445499190595001):
									if(cart_velocity <= -0.028178147971630096):
										if(pole_angular_velocity <= 0.05135905370116234):
											if(cart_position <= 0.1067449264228344):
												if(pole_angular_velocity > 0.04315408132970333):
													if(cart_velocity > -0.039569590240716934):
														if(pole_angle > -0.001830480294302106):
															return True
											else:
												return True
										else:
											return True
									else:
										if(cart_velocity <= -0.019301521591842175):
											if(pole_angular_velocity > 0.032239438965916634):
												if(cart_velocity <= -0.02425611112266779):
													if(pole_angular_velocity > 0.035481346771121025):
														return True
												else:
													return True
										else:
											return True
								else:
									if(pole_angular_velocity <= 0.030785996466875076):
										if(pole_angle > -0.001035229186527431):
											return True
									else:
										if(cart_velocity <= -0.03744406998157501):
											if(pole_angular_velocity > 0.04403851740062237):
												return True
										else:
											return True
							else:
								if(cart_position <= 0.1311805248260498):
									if(pole_angle <= -0.0010496255126781762):
										if(pole_angular_velocity <= 0.052206315100193024):
											if(cart_velocity <= -0.03912759944796562):
												if(pole_angular_velocity <= 0.049101509153842926):
													if(pole_angle > -0.001267004234250635):
														if(pole_angular_velocity > 0.041658032685518265):
															return True
												else:
													if(pole_angular_velocity <= 0.05062248185276985):
														return True
											else:
												if(cart_position <= 0.11094875633716583):
													if(pole_angular_velocity > 0.03622639738023281):
														if(cart_position <= 0.1098686158657074):
															return True
												else:
													if(pole_angular_velocity <= 0.03134366311132908):
														if(pole_angular_velocity <= 0.029076671227812767):
															return True
													else:
														if(pole_angle > -0.0017356346943415701):
															return True
										else:
											return True
									else:
										if(cart_velocity <= -0.03338658809661865):
											if(pole_angle <= -0.0008792757580522448):
												if(pole_angle <= -0.0009288129513151944):
													if(cart_velocity <= -0.045310480520129204):
														if(cart_position <= 0.11335725709795952):
															return True
													else:
														if(cart_velocity <= -0.03519907593727112):
															return True
											else:
												if(cart_position <= 0.1129816360771656):
													if(pole_angle > -0.0008180394943337888):
														return True
												else:
													return True
										else:
											return True
								else:
									if(cart_position <= 0.13680364936590195):
										if(pole_angle > -0.0014759264886379242):
											return True
									else:
										return True
				else:
					if(pole_angular_velocity <= 0.00011656379865598865):
						if(pole_angle <= 0.0014046219293959439):
							if(pole_angular_velocity <= -0.0013126744888722897):
								if(cart_position <= 0.10912071913480759):
									if(cart_velocity <= 0.03494134359061718):
										if(pole_angular_velocity <= -0.0019076564349234104):
											if(pole_angle > -0.0005796198383904994):
												if(cart_velocity <= 0.021095587871968746):
													if(pole_angle > 6.516316807392286e-05):
														if(pole_angular_velocity <= -0.002936433651484549):
															return True
														else:
															if(pole_angular_velocity > -0.0025478367460891604):
																if(pole_angular_velocity <= -0.0022695371881127357):
																	return True
																else:
																	if(pole_angle > 0.0007893498986959457):
																		return True
												else:
													if(cart_position > 0.08175721019506454):
														return True
										else:
											if(pole_angular_velocity <= -0.0013965822290629148):
												return True
									else:
										return True
								else:
									if(cart_velocity <= 0.012231000699102879):
										if(cart_velocity <= 0.0028560024220496416):
											if(pole_angle > 0.0006426000909414142):
												if(pole_angle <= 0.0006855639221612364):
													return True
												else:
													if(pole_angular_velocity > -0.002650237875059247):
														if(pole_angular_velocity <= -0.002602491294965148):
															return True
														else:
															if(pole_angle <= 0.0007846708176657557):
																if(cart_position > 0.11422234028577805):
																	return True
															else:
																if(pole_angle > 0.0012457349221222103):
																	if(pole_angle <= 0.001272618887014687):
																		return True
										else:
											if(pole_angle <= 4.858857391809579e-05):
												if(cart_velocity <= 0.0030486909672617912):
													return True
												else:
													if(pole_angular_velocity > -0.0013843034394085407):
														if(cart_velocity <= 0.006210948806256056):
															return True
											else:
												if(pole_angular_velocity <= -0.0017744620563462377):
													if(pole_angle <= 0.0007143965922296047):
														if(cart_velocity <= 0.0086621786467731):
															if(pole_angle <= 8.351049473276362e-05):
																return True
														else:
															return True
													else:
														if(pole_angular_velocity <= -0.002882379572838545):
															if(pole_angle <= 0.0009296474454458803):
																return True
														else:
															return True
												else:
													if(pole_angle <= 0.0008878469816409051):
														return True
									else:
										return True
							else:
								if(cart_position <= 0.11633293703198433):
									if(pole_angle <= 0.0006044152250979096):
										if(cart_velocity <= 0.009170528035610914):
											if(cart_position <= 0.11557662859559059):
												if(cart_position > 0.10867180675268173):
													if(cart_velocity <= 0.003615153837017715):
														if(pole_angle > 0.0003159066109219566):
															if(cart_position > 0.11312809586524963):
																return True
													else:
														if(pole_angle > -0.0002454250934533775):
															return True
											else:
												return True
										else:
											if(pole_angular_velocity > -0.0012714089243672788):
												if(cart_velocity <= 0.034594353288412094):
													if(pole_angular_velocity <= -0.001047052734065801):
														if(pole_angular_velocity <= -0.001088727731257677):
															return True
													else:
														return True
									else:
										if(cart_velocity > 0.0003126727824565023):
											if(cart_position <= 0.10458275303244591):
												if(cart_velocity > 0.010462868493050337):
													return True
											else:
												return True
								else:
									if(cart_velocity <= -0.01572753395885229):
										return True
									else:
										if(pole_angle > -0.00011410067236283794):
											if(cart_position <= 0.12216505780816078):
												if(cart_position <= 0.11717672273516655):
													if(cart_velocity <= 0.0032584171276539564):
														return True
												else:
													return True
											else:
												if(pole_angle > 0.0007546172419097275):
													if(pole_angle <= 0.0010257670655846596):
														return True
						else:
							if(pole_angle <= 0.0020128984469920397):
								if(cart_velocity <= -0.0006849628989584744):
									if(pole_angular_velocity > -0.0016170403105206788):
										if(cart_velocity <= -0.008498610462993383):
											if(pole_angular_velocity <= -0.0015521777095273137):
												return True
											else:
												if(pole_angle > 0.0017607356421649456):
													if(cart_position > 0.12065679207444191):
														return True
										else:
											if(cart_position > 0.10997501388192177):
												return True
								else:
									if(pole_angular_velocity <= -0.002863595844246447):
										if(cart_velocity <= 0.002624545944854617):
											if(pole_angular_velocity <= -0.0032101585529744625):
												return True
										else:
											return True
									else:
										if(pole_angular_velocity <= -0.00243143190164119):
											if(pole_angle <= 0.0015904402825981379):
												if(cart_velocity > 0.012860929477028549):
													return True
											else:
												return True
										else:
											if(cart_position <= 0.10794447734951973):
												if(cart_position <= 0.10791714861989021):
													if(pole_angular_velocity <= -0.00029067623836454004):
														return True
													else:
														if(cart_position <= 0.10144547000527382):
															return True
											else:
												return True
							else:
								if(cart_position <= -0.023050916381180286):
									if(pole_angle > 0.011909057851880789):
										if(cart_velocity > -0.011730320751667023):
											return True
								else:
									if(cart_velocity <= -0.012443675193935633):
										if(pole_angle > 0.00549486477393657):
											return True
									else:
										if(cart_position <= 0.052839310839772224):
											if(pole_angle <= 0.009553732350468636):
												if(pole_angular_velocity <= -0.0021128241787664592):
													return True
											else:
												return True
										else:
											if(pole_angle <= 0.0024147351505234838):
												if(pole_angle <= 0.002413004171103239):
													if(pole_angular_velocity <= -0.002986675826832652):
														if(cart_velocity > -0.0012777462834492326):
															if(pole_angle <= 0.002096132026053965):
																if(cart_position <= 0.10793261975049973):
																	return True
															else:
																return True
													else:
														if(cart_velocity <= -0.0012960672611370683):
															if(cart_position <= 0.10999847203493118):
																if(cart_position <= 0.10990546643733978):
																	return True
															else:
																if(pole_angle <= 0.0022678133100271225):
																	return True
																else:
																	if(pole_angle > 0.002298617851920426):
																		return True
														else:
															return True
											else:
												return True
					else:
						if(cart_position <= 0.03744620829820633):
							if(pole_angular_velocity <= 0.028603863902390003):
								if(pole_angle <= 0.007223641499876976):
									if(cart_position <= 0.022547676227986813):
										if(pole_angular_velocity <= 0.024989493191242218):
											if(cart_position > 0.020183347165584564):
												if(pole_angle > 0.0035149898612871766):
													return True
										else:
											if(pole_angular_velocity <= 0.026486787013709545):
												return True
											else:
												if(cart_position > 0.009320298908278346):
													if(pole_angular_velocity <= 0.028086112812161446):
														return True
									else:
										if(cart_velocity <= 0.03422785364091396):
											if(pole_angle <= 0.005311391549184918):
												if(pole_angular_velocity > 0.02720454055815935):
													return True
											else:
												if(cart_velocity > 0.00432066572830081):
													return True
										else:
											if(pole_angle <= 7.858108801883645e-06):
												if(pole_angular_velocity > 0.022670547477900982):
													return True
											else:
												return True
								else:
									if(cart_velocity <= -0.009203615598380566):
										if(pole_angle <= 0.021133159287273884):
											if(pole_angular_velocity <= 0.013964120764285326):
												if(cart_velocity > -0.011173926759511232):
													if(pole_angle > 0.018868078477680683):
														return True
											else:
												if(pole_angle > 0.013876103330403566):
													if(cart_position > -0.037398528307676315):
														if(cart_velocity > -0.03333231061697006):
															return True
										else:
											if(pole_angular_velocity > 0.0006739983218722045):
												if(pole_angle <= 0.0298049533739686):
													if(cart_position <= -0.03493065573275089):
														if(pole_angular_velocity <= 0.022624134086072445):
															if(cart_velocity > -0.028737761080265045):
																if(pole_angular_velocity > 0.008926928043365479):
																	if(cart_velocity <= -0.01293010264635086):
																		return True
														else:
															return True
													else:
														if(pole_angular_velocity <= 0.004017441533505917):
															if(cart_position > -0.020138883497565985):
																return True
														else:
															return True
												else:
													return True
									else:
										if(pole_angle <= 0.013879377394914627):
											if(pole_angular_velocity <= 0.012472054455429316):
												if(cart_position <= -0.013600466307252645):
													if(cart_velocity > 0.04411490820348263):
														return True
												else:
													if(cart_velocity <= 0.014767801854759455):
														if(pole_angular_velocity <= 0.002872264012694359):
															return True
														else:
															if(pole_angle > 0.012523082550615072):
																if(pole_angular_velocity > 0.011774174869060516):
																	return True
													else:
														return True
											else:
												if(cart_velocity <= 0.016205383464694023):
													if(pole_angle > 0.008847807999700308):
														if(cart_position <= 0.007426499854773283):
															if(cart_velocity > 0.005745204398408532):
																return True
														else:
															return True
												else:
													if(cart_position > -0.04422226920723915):
														return True
										else:
											if(cart_position <= -0.039153097197413445):
												if(cart_position <= -0.040539106354117393):
													if(pole_angle <= 0.016375376842916012):
														if(cart_velocity > 0.03534078411757946):
															return True
													else:
														if(cart_position <= -0.042980536818504333):
															return True
														else:
															if(pole_angular_velocity > 0.011228279210627079):
																return True
											else:
												return True
							else:
								if(pole_angular_velocity <= 0.04545587673783302):
									if(pole_angle <= 0.005252976668998599):
										if(cart_velocity <= 0.017389610409736633):
											if(cart_position > 0.03217468969523907):
												if(pole_angle > 0.003461131011135876):
													return True
										else:
											if(cart_position <= -0.0007413270359393209):
												if(cart_position <= -0.004173326073214412):
													if(cart_position <= -0.019001985900104046):
														if(cart_velocity > 0.042191898450255394):
															if(pole_angular_velocity > 0.03948473930358887):
																return True
													else:
														return True
											else:
												if(cart_velocity <= 0.02857175190001726):
													if(pole_angle <= 0.0006503885961137712):
														if(cart_position > 0.031515782698988914):
															return True
													else:
														if(cart_position <= 0.012488130945712328):
															if(pole_angle <= 0.0029251836240291595):
																if(pole_angular_velocity > 0.042180897668004036):
																	return True
															else:
																return True
														else:
															return True
												else:
													if(pole_angle <= 0.00038244931783992797):
														if(pole_angle <= 0.00037047098157927394):
															return True
													else:
														return True
									else:
										if(cart_velocity <= -0.03896486945450306):
											if(pole_angle > 0.012712803669273853):
												if(cart_velocity <= -0.03981430642306805):
													if(cart_position <= -0.06654520332813263):
														if(pole_angle > 0.02980213426053524):
															return True
													else:
														if(pole_angle <= 0.017600279301404953):
															if(pole_angle <= 0.017476043663918972):
																return True
														else:
															return True
										else:
											if(pole_angular_velocity <= 0.045427948236465454):
												if(cart_position <= -0.01211881497874856):
													if(pole_angle <= 0.009831323754042387):
														if(cart_velocity > 0.026457604952156544):
															return True
													else:
														if(pole_angle <= 0.01586669683456421):
															if(pole_angle <= 0.01519037177786231):
																return True
														else:
															return True
												else:
													if(cart_velocity <= -0.011758758220821619):
														if(pole_angle <= 0.011335297953337431):
															if(cart_position > 0.025587580166757107):
																return True
														else:
															return True
													else:
														return True
								else:
									if(cart_position <= 0.037373701110482216):
										if(pole_angle <= 0.002475949004292488):
											if(cart_velocity <= -0.027158853597939014):
												if(cart_position <= 0.03451221063733101):
													if(pole_angle > 0.0019347769557498395):
														if(pole_angular_velocity <= 0.08234888687729836):
															return True
												else:
													return True
											else:
												if(cart_position <= -0.03727083466947079):
													if(cart_velocity > 0.03526227921247482):
														if(cart_velocity <= 0.04048801213502884):
															return True
												else:
													if(pole_angle <= 0.002455417881719768):
														if(cart_velocity <= 0.0002601039013825357):
															if(pole_angular_velocity <= 0.062402332201600075):
																if(pole_angle > 0.0019825262716040015):
																	return True
															else:
																if(cart_position <= 0.010726132430136204):
																	if(cart_velocity <= -0.010564237833023071):
																		if(pole_angular_velocity > 0.08154378831386566):
																			return True
																	else:
																		return True
																else:
																	return True
														else:
															if(cart_position <= -0.024799708276987076):
																if(cart_position <= -0.026810452342033386):
																	return True
															else:
																if(pole_angle <= 0.002245826297439635):
																	if(pole_angular_velocity <= 0.04872738942503929):
																		if(cart_velocity > 0.011678750859573483):
																			return True
																	else:
																		return True
																else:
																	if(pole_angle > 0.002276829443871975):
																		return True
										else:
											if(cart_velocity <= -0.011321645695716143):
												if(cart_velocity <= -0.011436357162892818):
													if(pole_angular_velocity <= 0.056732818484306335):
														if(pole_angle <= 0.00998326065018773):
															if(cart_position <= 0.02840342652052641):
																if(cart_velocity <= -0.013181937858462334):
																	if(cart_position <= 0.010660213883966208):
																		if(cart_position <= -0.0043516934383660555):
																			if(pole_angle <= 0.009523905348032713):
																				return True
																	else:
																		if(cart_velocity > -0.0331419613212347):
																			return True
																else:
																	return True
															else:
																return True
														else:
															if(pole_angle <= 0.017309832386672497):
																if(cart_position <= -0.023131665773689747):
																	if(cart_velocity > -0.020813428796827793):
																		return True
																else:
																	return True
															else:
																return True
													else:
														if(pole_angle <= 0.008263629861176014):
															if(cart_position > -0.03314007446169853):
																if(pole_angular_velocity <= 0.0608696136623621):
																	if(pole_angular_velocity <= 0.060008347034454346):
																		return True
																else:
																	if(cart_position <= -0.014149251859635115):
																		if(cart_velocity > -0.026385577395558357):
																			return True
																	else:
																		return True
														else:
															return True
											else:
												return True
						else:
							if(pole_angle <= -0.00044875794264953583):
								if(cart_position <= 0.10647141560912132):
									if(pole_angle <= -0.0004501455696299672):
										if(pole_angular_velocity <= 0.0003389572666492313):
											if(cart_position > 0.09727071225643158):
												return True
										else:
											if(cart_position <= 0.04411937855184078):
												if(cart_position <= 0.043677445501089096):
													if(pole_angular_velocity > 0.018740349914878607):
														return True
											else:
												if(cart_position <= 0.05311425402760506):
													if(cart_position <= 0.05300283804535866):
														return True
												else:
													if(cart_position <= 0.09355266392230988):
														return True
													else:
														if(cart_position > 0.09362438693642616):
															if(pole_angular_velocity <= 0.018854745663702488):
																if(pole_angular_velocity <= 0.018545731902122498):
																	return True
															else:
																if(cart_velocity <= -0.043273795396089554):
																	if(cart_velocity <= -0.04344455525279045):
																		return True
																else:
																	if(pole_angle <= -0.0005090945633128285):
																		return True
																	else:
																		if(pole_angle > -0.0005051517218817025):
																			return True
								else:
									if(cart_position <= 0.11999865621328354):
										if(pole_angular_velocity <= 0.02011930476874113):
											if(cart_velocity <= -0.005656035616993904):
												if(pole_angular_velocity > 0.01433260552585125):
													if(cart_velocity <= -0.009932672139257193):
														if(cart_position > 0.11107796803116798):
															if(pole_angular_velocity <= 0.016666874289512634):
																if(cart_velocity > -0.013063080608844757):
																	return True
															else:
																return True
													else:
														return True
											else:
												if(cart_position > 0.10751760005950928):
													if(cart_velocity <= 0.0016663995338603854):
														if(pole_angular_velocity > 0.00823619682341814):
															if(pole_angle <= -0.0005287868843879551):
																return True
															else:
																if(pole_angle > -0.0005193726101424545):
																	return True
													else:
														return True
										else:
											if(pole_angle <= -0.0007401364855468273):
												if(pole_angle <= -0.0007542782987002283):
													return True
												else:
													if(cart_position <= 0.10830911248922348):
														return True
											else:
												if(cart_position <= 0.10693642124533653):
													if(pole_angular_velocity > 0.03277997951954603):
														return True
												else:
													if(cart_velocity <= -0.028071196749806404):
														if(cart_velocity <= -0.02926174458116293):
															return True
													else:
														return True
									else:
										if(cart_position <= 0.1303803250193596):
											if(cart_velocity > -0.016443011350929737):
												if(pole_angular_velocity <= 0.00309447234030813):
													if(cart_velocity > -0.002140330267138779):
														return True
												else:
													return True
										else:
											if(pole_angular_velocity <= 0.02156649436801672):
												if(cart_velocity <= -0.029280034825205803):
													if(cart_position > 0.1501598134636879):
														if(pole_angular_velocity > 0.01531897159293294):
															return True
												else:
													if(pole_angular_velocity > 0.003058918286114931):
														if(pole_angle > -0.0007110483420547098):
															if(pole_angle <= -0.000452124688308686):
																return True
											else:
												return True
							else:
								if(cart_position <= 0.11884931474924088):
									if(cart_position <= 0.11044377833604813):
										if(cart_position <= 0.04647211357951164):
											if(pole_angular_velocity <= 0.011097743175923824):
												if(pole_angle <= 0.0043534968281164765):
													return True
												else:
													if(cart_velocity <= -0.0011686317739076912):
														if(pole_angular_velocity <= 0.009869765024632215):
															return True
											else:
												if(cart_position <= 0.046401720494031906):
													if(cart_velocity <= -0.03406781889498234):
														if(pole_angular_velocity > 0.05642230436205864):
															return True
													else:
														if(pole_angular_velocity <= 0.02705360110849142):
															if(cart_position <= 0.04574187844991684):
																if(pole_angular_velocity <= 0.02692595962435007):
																	return True
														else:
															if(pole_angle <= -9.888902422972023e-05):
																if(pole_angle <= -0.00011269825699855573):
																	return True
															else:
																return True
										else:
											if(pole_angular_velocity <= 0.0017676502466201782):
												if(pole_angular_velocity <= 0.0017621386796236038):
													if(pole_angle <= 0.0008880606619641185):
														if(pole_angle <= 0.0008538564434275031):
															return True
													else:
														return True
											else:
												if(pole_angle <= -0.0002321987849427387):
													if(pole_angle <= -0.00023289088858291507):
														if(cart_position <= 0.1080772839486599):
															return True
														else:
															if(cart_position > 0.10820045694708824):
																if(cart_velocity <= -0.01437301654368639):
																	if(pole_angular_velocity > 0.020520403049886227):
																		return True
																else:
																	return True
													else:
														if(pole_angular_velocity > 0.037336152512580156):
															return True
												else:
													if(cart_position <= 0.05854922719299793):
														if(cart_position <= 0.05853167362511158):
															if(cart_position <= 0.058401744812726974):
																if(pole_angle <= 0.0002699494216358289):
																	if(pole_angle <= 0.0002577486739028245):
																		return True
																else:
																	return True
															else:
																if(cart_position > 0.058410828933119774):
																	return True
													else:
														return True
									else:
										if(cart_position > 0.11044539883732796):
											if(pole_angle <= 0.0006637126789428294):
												if(pole_angular_velocity <= 0.00873485766351223):
													if(cart_velocity <= -0.0013656598748639226):
														if(cart_position <= 0.11402270570397377):
															if(cart_velocity > -0.003252687049098313):
																if(pole_angular_velocity > 0.004430821631103754):
																	if(pole_angle > -9.744718045112677e-05):
																		return True
														else:
															return True
													else:
														if(pole_angular_velocity > 0.000186474688234739):
															if(cart_velocity <= 0.00031198924989439547):
																if(cart_velocity <= -0.0007031994173303246):
																	if(pole_angle <= -0.00014767326138098724):
																		if(cart_velocity > -0.0009257671190425754):
																			return True
																	else:
																		return True
															else:
																if(pole_angular_velocity <= 0.0006923042528796941):
																	if(pole_angle <= 7.417183223878965e-05):
																		if(cart_velocity > 0.002244859002530575):
																			return True
																	else:
																		return True
																else:
																	return True
												else:
													if(pole_angle <= -0.0003231718728784472):
														if(pole_angle <= -0.0003434540412854403):
															return True
													else:
														return True
											else:
												if(pole_angle <= 0.0011597705888561904):
													if(pole_angle <= 0.0011483965208753943):
														if(pole_angular_velocity <= 0.0016925145173445344):
															if(pole_angular_velocity <= 0.001671956793870777):
																return True
														else:
															return True
												else:
													return True
								else:
									if(pole_angle <= 0.0008279895700979978):
										if(pole_angular_velocity <= 0.001394132210407406):
											if(cart_velocity <= -0.006811932194977999):
												if(cart_position > 0.1270744502544403):
													if(cart_position <= 0.12977157533168793):
														return True
											else:
												return True
										else:
											if(pole_angle <= -0.00025717433891259134):
												if(pole_angular_velocity <= 0.03397038020193577):
													if(cart_position <= 0.13244838267564774):
														if(pole_angle <= -0.00031231113825924695):
															if(cart_velocity <= -0.021926934830844402):
																if(pole_angle <= -0.0003336476656841114):
																	if(cart_position > 0.13072174042463303):
																		return True
																else:
																	return True
															else:
																return True
													else:
														if(cart_position <= 0.15664062649011612):
															if(cart_position <= 0.14248404651880264):
																return True
															else:
																if(cart_position > 0.1431485041975975):
																	return True
												else:
													return True
											else:
												if(pole_angular_velocity <= 0.022739330306649208):
													if(cart_velocity <= -0.015684359706938267):
														if(pole_angular_velocity <= 0.00652582454495132):
															if(pole_angle > 0.0007726058829575777):
																if(cart_velocity <= -0.01934719644486904):
																	return True
														else:
															if(cart_position <= 0.12687863409519196):
																if(cart_velocity <= -0.019795864820480347):
																	if(cart_position > 0.12409746274352074):
																		if(cart_position <= 0.12632184475660324):
																			return True
																else:
																	return True
															else:
																if(pole_angular_velocity <= 0.021735506132245064):
																	if(cart_velocity > -0.046457648277282715):
																		if(pole_angle <= -4.205279856250854e-05):
																			if(pole_angle <= -0.00010767201820272021):
																				return True
																		else:
																			return True
																else:
																	if(pole_angular_velocity > 0.02223129291087389):
																		if(pole_angle > 0.00038336556463036686):
																			return True
													else:
														return True
												else:
													if(pole_angle <= 8.27543881314341e-05):
														if(pole_angle <= 7.161231224017683e-05):
															if(cart_velocity <= -0.04769342206418514):
																if(cart_velocity <= -0.04940928891301155):
																	return True
															else:
																return True
													else:
														return True
									else:
										if(pole_angular_velocity <= 0.0034605349646881223):
											if(cart_position <= 0.13227352499961853):
												if(pole_angle <= 0.00100948684848845):
													if(cart_position > 0.12141276523470879):
														return True
												else:
													return True
											else:
												if(cart_velocity > -0.018069928511977196):
													return True
										else:
											return True
		else:
			if(pole_angle <= -0.021388783119618893):
				if(pole_angular_velocity <= 0.327855721116066):
					if(pole_angle > -0.02184130623936653):
						if(pole_angular_velocity > 0.26855144649744034):
							return True
				else:
					if(pole_angle > -0.04237775877118111):
						if(pole_angular_velocity <= 0.5404111444950104):
							if(cart_velocity > -0.4140506386756897):
								return True
						else:
							return True
			else:
				if(pole_angular_velocity <= 0.10921763256192207):
					if(pole_angle <= -0.004830293590202928):
						if(cart_position <= 0.07407906651496887):
							if(pole_angle <= -0.0059919406194239855):
								if(cart_velocity <= 0.011404153890907764):
									if(cart_velocity <= -0.031687356531620026):
										if(cart_velocity <= -0.052826959639787674):
											if(cart_velocity > -0.05297384411096573):
												return True
									else:
										if(cart_position <= 0.05448063090443611):
											if(pole_angle <= -0.007220894331112504):
												if(cart_velocity > 0.0061305973213166):
													if(pole_angular_velocity > 0.09347179159522057):
														return True
											else:
												if(pole_angular_velocity <= 0.10246559605002403):
													if(cart_velocity > -0.023156246170401573):
														if(cart_position <= 0.02788728103041649):
															if(pole_angle <= -0.007100951625034213):
																return True
														else:
															if(pole_angle > -0.0070207128301262856):
																return True
												else:
													return True
										else:
											if(cart_velocity <= -0.028760849498212337):
												if(cart_position <= 0.058511532843112946):
													return True
											else:
												return True
								else:
									return True
							else:
								if(pole_angle <= -0.004922133171930909):
									if(cart_position <= 0.06877182051539421):
										if(pole_angular_velocity > 0.08694418147206306):
											if(cart_velocity <= -0.024376720190048218):
												if(pole_angular_velocity <= 0.09613070636987686):
													if(pole_angle > -0.005323514342308044):
														if(cart_velocity <= -0.02963393460959196):
															return True
												else:
													return True
											else:
												if(cart_position <= 0.01656624861061573):
													if(cart_velocity > -0.007760149601381272):
														return True
												else:
													return True
								else:
									if(cart_velocity > -0.039027364924550056):
										if(cart_position > 0.019793258048593998):
											return True
						else:
							if(pole_angular_velocity <= 0.08773228898644447):
								if(cart_velocity <= -0.04411998577415943):
									if(cart_position > 0.1767510026693344):
										return True
								else:
									return True
							else:
								if(pole_angular_velocity <= 0.08908318355679512):
									if(pole_angular_velocity <= 0.08892759680747986):
										return True
								else:
									return True
					else:
						if(pole_angle <= -0.004098898032680154):
							if(pole_angle <= -0.004117364762350917):
								if(cart_position <= 0.023970945738255978):
									if(pole_angle <= -0.004309472627937794):
										return True
									else:
										if(cart_velocity > -0.015758622903376818):
											return True
								else:
									if(pole_angular_velocity <= 0.08698222413659096):
										if(pole_angular_velocity <= 0.08682440221309662):
											return True
									else:
										return True
						else:
							if(cart_velocity <= -0.0527329221367836):
								if(cart_velocity <= -0.052738334983587265):
									if(pole_angle <= -0.0021989975939504802):
										if(cart_velocity <= -0.0530549343675375):
											return True
									else:
										return True
							else:
								if(cart_position <= -0.01086712023243308):
									if(pole_angle <= -0.0021008006297051907):
										if(cart_velocity > 0.0008217173162847757):
											return True
									else:
										if(pole_angle <= 0.006444797618314624):
											if(cart_velocity <= -0.028871634043753147):
												if(pole_angular_velocity > 0.10642605274915695):
													return True
											else:
												return True
										else:
											return True
								else:
									if(pole_angle <= -0.002806113217957318):
										if(pole_angle <= -0.0028127903351560235):
											if(pole_angular_velocity <= 0.08728794753551483):
												if(pole_angle > -0.0036133729154244065):
													return True
											else:
												return True
									else:
										return True
				else:
					if(cart_position <= 0.018246727995574474):
						if(pole_angle <= -0.00702847121283412):
							if(pole_angular_velocity <= 0.25167079269886017):
								if(cart_velocity <= -0.09172099828720093):
									if(cart_velocity > -0.15705887228250504):
										if(cart_position > 0.0005599847063422203):
											return True
								else:
									if(cart_position > 0.007537883473560214):
										return True
							else:
								if(pole_angular_velocity <= 0.29496653378009796):
									if(cart_velocity <= -0.18256930261850357):
										if(cart_position > 0.005921488860622048):
											if(cart_velocity > -0.20081758499145508):
												return True
									else:
										return True
								else:
									if(pole_angle <= -0.02040017955005169):
										if(cart_position > -0.03799070976674557):
											return True
									else:
										if(cart_velocity <= -0.42279061675071716):
											if(pole_angle > -0.014532058034092188):
												return True
										else:
											return True
						else:
							if(cart_velocity <= -0.2007414549589157):
								if(pole_angular_velocity <= 0.24254772067070007):
									if(pole_angle > 0.005136593710631132):
										if(cart_position <= -0.07092519477009773):
											if(pole_angle > 0.021209106780588627):
												return True
										else:
											if(cart_velocity <= -0.20084026455879211):
												return True
								else:
									if(cart_position <= 0.016991947777569294):
										if(pole_angle <= 0.0015719927614554763):
											if(pole_angular_velocity <= 0.27247852087020874):
												if(cart_position > -0.016833505360409617):
													return True
											else:
												return True
										else:
											return True
							else:
								if(pole_angle <= -0.004579587839543819):
									if(cart_position > -0.05089338682591915):
										if(pole_angle <= -0.005015765083953738):
											return True
										else:
											if(pole_angle > -0.004970006411895156):
												return True
								else:
									if(pole_angle <= -0.002578179817646742):
										if(pole_angle <= -0.002614683238789439):
											if(cart_position > -0.04009828716516495):
												return True
									else:
										if(cart_position <= -0.08213214576244354):
											if(pole_angle > 0.01320931245572865):
												return True
										else:
											return True
					else:
						if(pole_angle <= -0.021060177125036716):
							if(cart_position <= 0.029192746616899967):
								return True
						else:
							if(pole_angle <= -0.01868985779583454):
								if(pole_angular_velocity > 0.28918273746967316):
									return True
							else:
								if(pole_angular_velocity <= 0.1168680489063263):
									if(pole_angular_velocity <= 0.11681690067052841):
										if(cart_velocity <= -0.053347691893577576):
											if(cart_position <= 0.047359321266412735):
												return True
										else:
											if(cart_velocity <= -0.04849499650299549):
												if(cart_velocity <= -0.04852821119129658):
													if(cart_position <= 0.032193223014473915):
														if(cart_position <= 0.03121611662209034):
															return True
													else:
														return True
											else:
												return True
								else:
									if(cart_position <= 0.024705364368855953):
										if(cart_position <= 0.024628283455967903):
											if(pole_angle <= -0.011511235032230616):
												if(pole_angle <= -0.015226411167532206):
													return True
											else:
												return True
									else:
										return True
	return False

