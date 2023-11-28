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
	if(pole_angular_velocity <= -0.001056914043147117):
		if(pole_angular_velocity <= -0.11168522387742996):
			if(pole_angle <= 0.0435353834182024):
				if(pole_angle <= 0.028814715333282948):
					if(pole_angular_velocity <= -0.12227915972471237):
						if(pole_angular_velocity <= -0.16087956726551056):
							return True
						else:
							if(pole_angle <= 0.01632925309240818):
								if(cart_velocity <= 0.21683362126350403):
									if(pole_angular_velocity <= -0.1313457116484642):
										return True
									else:
										if(pole_angular_velocity > -0.13116808235645294):
											return True
								else:
									if(pole_angular_velocity <= -0.15125498920679092):
										return True
					else:
						if(pole_angle <= 0.011601763311773539):
							if(pole_angular_velocity > -0.12205393612384796):
								return True
				else:
					if(pole_angular_velocity <= -0.2324235513806343):
						return True
					else:
						if(cart_velocity <= 0.18984787911176682):
							return True
		else:
			if(pole_angle <= 0.0024072423111647367):
				if(pole_angle <= 0.0009942651959136128):
					if(pole_angular_velocity <= -0.027150047942996025):
						if(pole_angular_velocity <= -0.0337833259254694):
							if(pole_angle <= 0.0006919058505445719):
								return True
							else:
								if(pole_angle > 0.0007121902599465102):
									return True
						else:
							if(pole_angular_velocity > -0.03359393775463104):
								if(pole_angle <= 0.00031055374711286277):
									return True
								else:
									if(pole_angle > 0.00039808718429412693):
										return True
					else:
						if(pole_angle <= -0.0010248684557154775):
							if(pole_angular_velocity <= -0.0015943230828270316):
								if(cart_position <= 0.1308077871799469):
									return True
								else:
									if(cart_position > 0.1351337507367134):
										return True
						else:
							if(cart_velocity <= 0.009002386126667261):
								if(cart_position <= 0.1554829478263855):
									return True
				else:
					if(pole_angular_velocity <= -0.04119704104959965):
						if(pole_angular_velocity <= -0.05268966220319271):
							if(cart_velocity <= 0.17555220425128937):
								if(pole_angle <= 0.0022679868852719665):
									return True
								else:
									if(pole_angle > 0.002287497976794839):
										return True
						else:
							if(cart_position > 0.1306065320968628):
								if(cart_position <= 0.14431656152009964):
									if(cart_velocity <= 0.0344028091058135):
										return True
									else:
										if(pole_angular_velocity <= -0.047602782025933266):
											if(cart_position <= 0.13740278035402298):
												if(cart_velocity > 0.04527042619884014):
													return True
											else:
												return True
					else:
						if(pole_angular_velocity <= -0.003488773014396429):
							if(cart_velocity <= -0.010641646105796099):
								if(cart_position > 0.13402516394853592):
									return True
							else:
								if(pole_angular_velocity <= -0.038695190101861954):
									if(pole_angular_velocity > -0.039679672569036484):
										return True
						else:
							return True
			else:
				if(cart_position <= 0.006577720865607262):
					if(cart_position > -0.04931931383907795):
						return True
				else:
					if(pole_angle <= 0.0029615063685923815):
						if(pole_angular_velocity <= -0.058647435158491135):
							if(pole_angular_velocity > -0.10350216925144196):
								if(pole_angle <= 0.002505871932953596):
									if(pole_angle <= 0.0024951520608738065):
										return True
								else:
									return True
						else:
							if(pole_angular_velocity <= -0.052467312663793564):
								if(pole_angle <= 0.002612773678265512):
									return True
					else:
						if(pole_angular_velocity <= -0.07236583158373833):
							if(pole_angle <= 0.004140501609072089):
								if(pole_angle <= 0.0036199729656800628):
									if(cart_position <= 0.05358771048486233):
										return True
									else:
										if(cart_velocity <= 0.04935034364461899):
											return True
										else:
											if(pole_angle <= 0.00333931902423501):
												if(cart_velocity > 0.05250141769647598):
													return True
								else:
									if(pole_angle <= 0.003932052291929722):
										return True
									else:
										if(pole_angle > 0.004051179857924581):
											return True
							else:
								if(cart_position <= 0.010859388392418623):
									return True
								else:
									if(cart_position <= 0.04652666114270687):
										if(cart_position > 0.04061276651918888):
											return True
						else:
							if(pole_angle <= 0.0032702491153031588):
								if(pole_angle <= 0.003186986898072064):
									if(cart_position <= 0.07512899115681648):
										return True
								else:
									if(cart_position <= 0.14812767505645752):
										return True
									else:
										if(pole_angle <= 0.0032302794279530644):
											return True
							else:
								if(pole_angle <= 0.0038892384618520737):
									if(pole_angle <= 0.0038870680145919323):
										if(cart_velocity <= 0.03468157723546028):
											if(cart_velocity > 0.030545624904334545):
												return True
									else:
										return True
	else:
		if(pole_angular_velocity <= 0.07712621986865997):
			if(pole_angle <= -0.0018073087558150291):
				if(pole_angular_velocity <= 0.049246687442064285):
					if(cart_position <= 0.14249490201473236):
						if(cart_velocity <= 0.026813521049916744):
							if(pole_angle <= -0.0022676829248666763):
								if(cart_position <= 0.0964159369468689):
									if(pole_angle <= -0.0024187612580135465):
										if(cart_velocity <= -0.005836862372234464):
											return True
										else:
											if(pole_angular_velocity <= 0.03726978041231632):
												return True
								else:
									return True
							else:
								if(pole_angular_velocity <= 0.037834953516721725):
									if(cart_position <= 0.10806652531027794):
										if(cart_position <= 0.10510853677988052):
											return True
									else:
										return True
								else:
									if(cart_velocity <= -0.02584335394203663):
										return True
									else:
										if(pole_angular_velocity <= 0.04030117765069008):
											if(pole_angle > -0.002005667774938047):
												return True
						else:
							if(pole_angular_velocity <= 0.021167196333408356):
								if(pole_angle <= -0.0025466304505243897):
									if(cart_velocity <= 0.048853978514671326):
										if(cart_position <= 0.12171127274632454):
											return True
										else:
											if(cart_position > 0.13175131380558014):
												return True
									else:
										if(cart_velocity > 0.04894106090068817):
											return True
							else:
								if(pole_angle <= -0.0044856141321361065):
									if(cart_velocity > 0.034820832312107086):
										return True
					else:
						if(pole_angle <= -0.00447660218924284):
							if(cart_velocity <= -0.01298590051010251):
								if(pole_angular_velocity <= 0.04752647876739502):
									return True
							else:
								if(cart_position > 0.168153278529644):
									return True
				else:
					if(pole_angle <= -0.003623445867560804):
						if(cart_velocity <= 0.02510908991098404):
							if(cart_position <= 0.1305934526026249):
								if(pole_angular_velocity <= 0.07190298289060593):
									if(pole_angle <= -0.004309994867071509):
										return True
									else:
										if(cart_velocity <= -0.02671036869287491):
											return True
										else:
											if(pole_angle <= -0.004067844012752175):
												if(pole_angle > -0.004183893324807286):
													return True
								else:
									if(pole_angle <= -0.006594409933313727):
										return True
							else:
								if(pole_angle <= -0.014067811891436577):
									return True
						else:
							if(pole_angular_velocity <= 0.054253680631518364):
								return True
							else:
								if(cart_velocity > 0.04607934691011906):
									if(cart_position <= 0.007170069497078657):
										return True
					else:
						if(pole_angular_velocity <= 0.051302650943398476):
							if(cart_velocity <= -0.026113626547157764):
								if(pole_angle > -0.0035034221364185214):
									if(pole_angle <= -0.0020662646275013685):
										return True
						else:
							if(pole_angle <= -0.0033336078049615026):
								if(pole_angular_velocity <= 0.05581972748041153):
									return True
							else:
								if(pole_angular_velocity <= 0.05220218747854233):
									if(pole_angle > -0.0027100639417767525):
										return True
			else:
				if(pole_angle <= -0.000723920064046979):
					if(cart_position <= 0.10611807182431221):
						if(pole_angle <= -0.0014514601207338274):
							if(pole_angular_velocity <= 0.04808228462934494):
								if(cart_velocity <= -0.034325193613767624):
									return True
								else:
									if(pole_angular_velocity <= 0.03544281981885433):
										if(cart_velocity <= 0.021461173426359892):
											return True
							else:
								if(pole_angle > -0.0015140084433369339):
									return True
						else:
							if(cart_velocity <= -0.03450912982225418):
								if(pole_angular_velocity <= 0.049110569059848785):
									return True
					else:
						if(cart_position <= 0.1375362053513527):
							if(pole_angle <= -0.0011775328894145787):
								return True
							else:
								if(pole_angle <= -0.000915214914130047):
									if(cart_position <= 0.11067021265625954):
										return True
									else:
										if(cart_position > 0.11372625827789307):
											if(pole_angle > -0.001111638790462166):
												return True
								else:
									return True
				else:
					if(cart_position <= 0.02185653243213892):
						if(pole_angular_velocity <= 0.019094476476311684):
							if(pole_angle <= 0.0200874675065279):
								return True
						else:
							if(cart_velocity <= -0.039010634645819664):
								return True
							else:
								if(pole_angle <= 0.0061255942564457655):
									if(pole_angle > 0.0036959591088816524):
										return True
								else:
									if(pole_angle <= 0.014996613375842571):
										if(pole_angular_velocity <= 0.04858178086578846):
											if(cart_velocity <= 0.016782082617282867):
												return True
					else:
						if(pole_angular_velocity <= 0.0006876701954752207):
							if(cart_velocity <= -0.01115456223487854):
								if(cart_position <= 0.12779760360717773):
									return True
						else:
							if(pole_angle <= -0.00035479031794238836):
								if(pole_angular_velocity <= 0.016356573440134525):
									if(cart_position > 0.10971590876579285):
										return True
							else:
								if(pole_angular_velocity <= 0.002783765667118132):
									if(pole_angular_velocity > 0.002434652531519532):
										return True
		else:
			if(pole_angular_velocity <= 0.09360167384147644):
				if(pole_angle <= -0.004684025654569268):
					if(cart_velocity <= -0.025252354331314564):
						if(cart_velocity > -0.03804493509232998):
							return True
					else:
						if(cart_position <= 0.03510122932493687):
							if(pole_angle <= -0.0070336509961634874):
								return True
				else:
					if(pole_angle <= -0.0042084818705916405):
						if(pole_angle > -0.004396843258291483):
							return True
					else:
						if(cart_velocity > -0.00807809503749013):
							if(cart_velocity <= -0.008056782186031342):
								return True
			else:
				if(pole_angle <= -0.023049098439514637):
					return True
				else:
					if(pole_angular_velocity <= 0.1067345142364502):
						if(pole_angular_velocity <= 0.10633914545178413):
							if(pole_angle <= -0.007005021441727877):
								if(cart_position <= 0.04588693077675998):
									return True
						else:
							return True
					else:
						if(cart_position <= -0.01831588800996542):
							if(pole_angle <= -0.005495909950695932):
								return True
	return False

def weShould_move_right(cart_position, cart_velocity, pole_angle, pole_angular_velocity):
	if(pole_angular_velocity <= -0.001056914043147117):
		if(pole_angular_velocity <= -0.11168522387742996):
			if(pole_angle <= 0.0435353834182024):
				if(pole_angle <= 0.028814715333282948):
					if(pole_angular_velocity <= -0.12227915972471237):
						if(pole_angular_velocity > -0.16087956726551056):
							if(pole_angle <= 0.01632925309240818):
								if(cart_velocity <= 0.21683362126350403):
									if(pole_angular_velocity > -0.1313457116484642):
										if(pole_angular_velocity <= -0.13116808235645294):
											return True
								else:
									if(pole_angular_velocity > -0.15125498920679092):
										return True
							else:
								return True
					else:
						if(pole_angle <= 0.011601763311773539):
							if(pole_angular_velocity <= -0.12205393612384796):
								return True
						else:
							return True
				else:
					if(pole_angular_velocity > -0.2324235513806343):
						if(cart_velocity > 0.18984787911176682):
							return True
			else:
				return True
		else:
			if(pole_angle <= 0.0024072423111647367):
				if(pole_angle <= 0.0009942651959136128):
					if(pole_angular_velocity <= -0.027150047942996025):
						if(pole_angular_velocity <= -0.0337833259254694):
							if(pole_angle > 0.0006919058505445719):
								if(pole_angle <= 0.0007121902599465102):
									return True
						else:
							if(pole_angular_velocity <= -0.03359393775463104):
								return True
							else:
								if(pole_angle > 0.00031055374711286277):
									if(pole_angle <= 0.00039808718429412693):
										return True
					else:
						if(pole_angle <= -0.0010248684557154775):
							if(pole_angular_velocity <= -0.0015943230828270316):
								if(cart_position > 0.1308077871799469):
									if(cart_position <= 0.1351337507367134):
										return True
							else:
								return True
						else:
							if(cart_velocity <= 0.009002386126667261):
								if(cart_position > 0.1554829478263855):
									return True
							else:
								return True
				else:
					if(pole_angular_velocity <= -0.04119704104959965):
						if(pole_angular_velocity <= -0.05268966220319271):
							if(cart_velocity <= 0.17555220425128937):
								if(pole_angle > 0.0022679868852719665):
									if(pole_angle <= 0.002287497976794839):
										return True
							else:
								return True
						else:
							if(cart_position <= 0.1306065320968628):
								return True
							else:
								if(cart_position <= 0.14431656152009964):
									if(cart_velocity > 0.0344028091058135):
										if(pole_angular_velocity <= -0.047602782025933266):
											if(cart_position <= 0.13740278035402298):
												if(cart_velocity <= 0.04527042619884014):
													return True
										else:
											return True
								else:
									return True
					else:
						if(pole_angular_velocity <= -0.003488773014396429):
							if(cart_velocity <= -0.010641646105796099):
								if(cart_position <= 0.13402516394853592):
									return True
							else:
								if(pole_angular_velocity <= -0.038695190101861954):
									if(pole_angular_velocity <= -0.039679672569036484):
										return True
								else:
									return True
			else:
				if(cart_position <= 0.006577720865607262):
					if(cart_position <= -0.04931931383907795):
						return True
				else:
					if(pole_angle <= 0.0029615063685923815):
						if(pole_angular_velocity <= -0.058647435158491135):
							if(pole_angular_velocity <= -0.10350216925144196):
								return True
							else:
								if(pole_angle <= 0.002505871932953596):
									if(pole_angle > 0.0024951520608738065):
										return True
						else:
							if(pole_angular_velocity <= -0.052467312663793564):
								if(pole_angle > 0.002612773678265512):
									return True
							else:
								return True
					else:
						if(pole_angular_velocity <= -0.07236583158373833):
							if(pole_angle <= 0.004140501609072089):
								if(pole_angle <= 0.0036199729656800628):
									if(cart_position > 0.05358771048486233):
										if(cart_velocity > 0.04935034364461899):
											if(pole_angle <= 0.00333931902423501):
												if(cart_velocity <= 0.05250141769647598):
													return True
											else:
												return True
								else:
									if(pole_angle > 0.003932052291929722):
										if(pole_angle <= 0.004051179857924581):
											return True
							else:
								if(cart_position > 0.010859388392418623):
									if(cart_position <= 0.04652666114270687):
										if(cart_position <= 0.04061276651918888):
											return True
									else:
										return True
						else:
							if(pole_angle <= 0.0032702491153031588):
								if(pole_angle <= 0.003186986898072064):
									if(cart_position > 0.07512899115681648):
										return True
								else:
									if(cart_position > 0.14812767505645752):
										if(pole_angle > 0.0032302794279530644):
											return True
							else:
								if(pole_angle <= 0.0038892384618520737):
									if(pole_angle <= 0.0038870680145919323):
										if(cart_velocity <= 0.03468157723546028):
											if(cart_velocity <= 0.030545624904334545):
												return True
										else:
											return True
								else:
									return True
	else:
		if(pole_angular_velocity <= 0.07712621986865997):
			if(pole_angle <= -0.0018073087558150291):
				if(pole_angular_velocity <= 0.049246687442064285):
					if(cart_position <= 0.14249490201473236):
						if(cart_velocity <= 0.026813521049916744):
							if(pole_angle <= -0.0022676829248666763):
								if(cart_position <= 0.0964159369468689):
									if(pole_angle <= -0.0024187612580135465):
										if(cart_velocity > -0.005836862372234464):
											if(pole_angular_velocity > 0.03726978041231632):
												return True
									else:
										return True
							else:
								if(pole_angular_velocity <= 0.037834953516721725):
									if(cart_position <= 0.10806652531027794):
										if(cart_position > 0.10510853677988052):
											return True
								else:
									if(cart_velocity > -0.02584335394203663):
										if(pole_angular_velocity <= 0.04030117765069008):
											if(pole_angle <= -0.002005667774938047):
												return True
										else:
											return True
						else:
							if(pole_angular_velocity <= 0.021167196333408356):
								if(pole_angle <= -0.0025466304505243897):
									if(cart_velocity <= 0.048853978514671326):
										if(cart_position > 0.12171127274632454):
											if(cart_position <= 0.13175131380558014):
												return True
									else:
										if(cart_velocity <= 0.04894106090068817):
											return True
								else:
									return True
							else:
								if(pole_angle <= -0.0044856141321361065):
									if(cart_velocity <= 0.034820832312107086):
										return True
								else:
									return True
					else:
						if(pole_angle <= -0.00447660218924284):
							if(cart_velocity <= -0.01298590051010251):
								if(pole_angular_velocity > 0.04752647876739502):
									return True
							else:
								if(cart_position <= 0.168153278529644):
									return True
						else:
							return True
				else:
					if(pole_angle <= -0.003623445867560804):
						if(cart_velocity <= 0.02510908991098404):
							if(cart_position <= 0.1305934526026249):
								if(pole_angular_velocity <= 0.07190298289060593):
									if(pole_angle > -0.004309994867071509):
										if(cart_velocity > -0.02671036869287491):
											if(pole_angle <= -0.004067844012752175):
												if(pole_angle <= -0.004183893324807286):
													return True
											else:
												return True
								else:
									if(pole_angle > -0.006594409933313727):
										return True
							else:
								if(pole_angle > -0.014067811891436577):
									return True
						else:
							if(pole_angular_velocity > 0.054253680631518364):
								if(cart_velocity <= 0.04607934691011906):
									return True
								else:
									if(cart_position > 0.007170069497078657):
										return True
					else:
						if(pole_angular_velocity <= 0.051302650943398476):
							if(cart_velocity <= -0.026113626547157764):
								if(pole_angle <= -0.0035034221364185214):
									return True
								else:
									if(pole_angle > -0.0020662646275013685):
										return True
							else:
								return True
						else:
							if(pole_angle <= -0.0033336078049615026):
								if(pole_angular_velocity > 0.05581972748041153):
									return True
							else:
								if(pole_angular_velocity <= 0.05220218747854233):
									if(pole_angle <= -0.0027100639417767525):
										return True
								else:
									return True
			else:
				if(pole_angle <= -0.000723920064046979):
					if(cart_position <= 0.10611807182431221):
						if(pole_angle <= -0.0014514601207338274):
							if(pole_angular_velocity <= 0.04808228462934494):
								if(cart_velocity > -0.034325193613767624):
									if(pole_angular_velocity <= 0.03544281981885433):
										if(cart_velocity > 0.021461173426359892):
											return True
									else:
										return True
							else:
								if(pole_angle <= -0.0015140084433369339):
									return True
						else:
							if(cart_velocity <= -0.03450912982225418):
								if(pole_angular_velocity > 0.049110569059848785):
									return True
							else:
								return True
					else:
						if(cart_position <= 0.1375362053513527):
							if(pole_angle > -0.0011775328894145787):
								if(pole_angle <= -0.000915214914130047):
									if(cart_position > 0.11067021265625954):
										if(cart_position <= 0.11372625827789307):
											return True
										else:
											if(pole_angle <= -0.001111638790462166):
												return True
						else:
							return True
				else:
					if(cart_position <= 0.02185653243213892):
						if(pole_angular_velocity <= 0.019094476476311684):
							if(pole_angle > 0.0200874675065279):
								return True
						else:
							if(cart_velocity > -0.039010634645819664):
								if(pole_angle <= 0.0061255942564457655):
									if(pole_angle <= 0.0036959591088816524):
										return True
								else:
									if(pole_angle <= 0.014996613375842571):
										if(pole_angular_velocity <= 0.04858178086578846):
											if(cart_velocity > 0.016782082617282867):
												return True
										else:
											return True
									else:
										return True
					else:
						if(pole_angular_velocity <= 0.0006876701954752207):
							if(cart_velocity <= -0.01115456223487854):
								if(cart_position > 0.12779760360717773):
									return True
							else:
								return True
						else:
							if(pole_angle <= -0.00035479031794238836):
								if(pole_angular_velocity <= 0.016356573440134525):
									if(cart_position <= 0.10971590876579285):
										return True
								else:
									return True
							else:
								if(pole_angular_velocity <= 0.002783765667118132):
									if(pole_angular_velocity <= 0.002434652531519532):
										return True
								else:
									return True
		else:
			if(pole_angular_velocity <= 0.09360167384147644):
				if(pole_angle <= -0.004684025654569268):
					if(cart_velocity <= -0.025252354331314564):
						if(cart_velocity <= -0.03804493509232998):
							return True
					else:
						if(cart_position <= 0.03510122932493687):
							if(pole_angle > -0.0070336509961634874):
								return True
						else:
							return True
				else:
					if(pole_angle <= -0.0042084818705916405):
						if(pole_angle <= -0.004396843258291483):
							return True
					else:
						if(cart_velocity <= -0.00807809503749013):
							return True
						else:
							if(cart_velocity > -0.008056782186031342):
								return True
			else:
				if(pole_angle > -0.023049098439514637):
					if(pole_angular_velocity <= 0.1067345142364502):
						if(pole_angular_velocity <= 0.10633914545178413):
							if(pole_angle <= -0.007005021441727877):
								if(cart_position > 0.04588693077675998):
									return True
							else:
								return True
					else:
						if(cart_position <= -0.01831588800996542):
							if(pole_angle > -0.005495909950695932):
								return True
						else:
							return True
	return False

