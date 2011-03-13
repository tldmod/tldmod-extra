from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *
from module_constants import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_tld_down = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
#pf_tld_down    = pf_is_static|pf_always_visible|pf_show_faction
pf_tld_down  = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small
#pf_tld_down = pf_is_static|pf_always_visible|pf_show_faction|pf_hide_defenders|pf_label_large

#sample_party = [(trp_veteran_knight_of_gondor,1,0), (trp_swadian_peasant,10,0), (trp_archer_of_gondor,1,0), (trp_knight_of_the_citadel, 1, 0), (trp_footmen_of_gondor, 1, 0), (trp_gondor_militiamen,1,0)]
#!
parties = [
  ("main_party","Main_Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17,52.50),[(trp_player,1,0)]),
  ("temp_party","temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_unarmed_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed","enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_ally","collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  #  volunteers parties (one per city)
  # ] +concatenate_scripts([
  #		("volunteers_"+str(x), "_+_",   pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[],0)
  # ] for x in range(150)) +  [
  


  ("town_merc_1","sargoth_mercs",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,0),[]),

  ("zendar","Brigand Fort", icon_castle_c|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.97,-6.21),[]),

#TLD TOWNS
    # Gondor towns
    ("town_minas_tirith","Minas_Tirith",    icon_minas_tirith       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.5,20.5),[],205),
    ("town_pelargir","Pelargir",            icon_gondortown         |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.48,59.15),[],240),
    ("town_linhir","Linhir",                icon_castle_gondor_small|pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.7,57.2),[],170),
    ("town_dol_amroth","Dol_Amroth",        icon_dolamroth          |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.4,62.3),[],280),
    ("town_edhellond","Edhellond",          icon_gondortown         |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.63,43.62),[],170),
    ("town_lossarnach","Lossarnach",        icon_gondortown         |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.6,34),[],170),
    ("town_tarnost","Tarnost",              icon_castle_gondor_small|pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.29,62.21),[],170),
    ("town_erech","Erech",                  icon_castle_gondor_small|pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.33,4.47),[],170),
    ("town_pinnath_gelin","Pinnath_Gelin",  icon_gondortown         |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.72,27.45),[],170),
    ("town_west_osgiliath","West_Osgiliath",icon_west_osgilliath    |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.93,16.46),[],0),
    ("town_henneth_annun","Henneth_Annun",  icon_henneth_annun      |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64,-21.05),[],170),
    ("town_cair_andros","Cair_Andros",      icon_cairandros         |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.01,-1.80),[],170),
    ("town_ethring","Ethring",              icon_gondortown         |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.5,27.5),[],50),
	# Rohan towns
    ("town_edoras","Edoras",                icon_edoras     |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.65,-21.77),[],215),
    ("town_aldburg","Aldburg",              icon_rohantown1 |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.70,-14.76),[],170),
    ("town_hornburg","Hornburg",            icon_helms_deep |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.5,-18.7 ),[],190),
    ("town_east_emnet","East_Emnet",        icon_rohantown1 |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.82,-37.07),[],170),
    ("town_westfold","Westfold",            icon_rohantown1 |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54,-38),[],260),
    ("town_west_emnet","West_Emnet",        icon_rohantown1 |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.51,-50.23),[],250),
    ("town_eastfold","Eastfold",            icon_rohantown1 |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.05,-6.20),[],170),
# Mordor towns
    ("town_barad_dur","Barad_Dur",            icon_baraddur   |pf_tld_down,  no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103.55,-9.55),[],170),
    ("town_morannon","Morannon",              icon_morannon   |pf_tld_down,  no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.11,-43.50),[],170),
    ("town_minas_morgul","Minas_Morgul",      icon_minasmorgul|pf_tld_down,  no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73,20),[],170),
    ("town_mount_doom","Mount_Doom",          icon_orodruin   |pf_tld_down,  no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.53,-3.95),[],170),
    ("town_cirith_ungol","Cirith_Ungol",      icon_cirithungol|pf_tld_down,  no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70,14.6),[],170),
    ("town_east_osgiliath","East_Osgiliath",icon_east_osgilliath|pf_tld_down,no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.2,16.6),[],0),
    ("town_orc_sentry_camp","Orc_Sentry_Camp",icon_orctower   |pf_tld_down,  no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.09,27.05),[],170),
# Isengard towns
    ("town_isengard","Isengard",                   icon_isengard|pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.25,-70.42),[],170),
    ("town_urukhai_outpost","Uruk_Hai_Outpost",    icon_orctower|pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.80,-64.32),[],170),
    ("town_urukhai_h_camp","Uruk_Hai_Hunting_camp",icon_orctower|pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.67,-95.38),[],170),
    ("town_urukhai_r_camp","Uruk_Hai_River_camp",  icon_orctower|pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.17,-66.30),[],170),
# Lothlorien towns
    ("town_caras_galadhon","Caras_Galadhon",  icon_grove      |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1,-161),[],350),
    ("town_cerin_dolen","Cerin_Dolen",        icon_town       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.58,-166.84),[],170),
    ("town_cerin_amroth","Cerin_Amroth",      icon_town       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.79,-165.02),[],170),
# Woodelves towns
    ("town_thranduils_halls","Thranduil's_Halls",   icon_town       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.60,-331.71),[],170),
    ("town_woodelf_camp","Woodelf_Camp",            icon_camp       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.95,-185.61),[],170),
    ("town_woodelf_west_camp","Woodelf_West_Camp",  icon_camp       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15,-317),[],170),
    ("town_woodelf_north_camp","Woodelf_North_Camp",icon_town       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38,-340),[],170),
# Woodmen and Beorning towns   
    ("town_woodsmen_village","Woodsmen_Village",      icon_smallvillage |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.08,-257),[],170),
    ("town_beorning_village","Beorning_Village",      icon_smallvillage |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.4,-236.4),[],170),
    ("town_beorn_house","Beorn's House",              icon_smallvillage |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10,-290),[],170),
# Moria towns
    ("town_moria","Moria",                 icon_moria      |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.5,-188),[],200),
    ("town_troll_cave","Troll_Cave",       icon_town       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.26,-114.10),[],170),
# Dale towns
    ("town_dale","Dale",                   icon_town       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.26,-333.53),[],170),
    ("town_esgaroth","Esgaroth",           icon_town       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.25,-323.59),[],170),
    ("town_dale_town","Dale Town",         icon_town       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94,-297),[],170),
# Dunlanders towns
    ("town_dunland_camp","Dunlander_Camp", icon_nomadcamp_b|pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61,-54),[],350),
# Haradrim towns
    ("town_harad_camp","Haradrim_Camp",    icon_haradcamp  |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.72,66.13),[],170),
# Khand towns
    ("town_khand_camp","Khand_Camp",       icon_nomadcamp  |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.46,-56.10),[],170),
# Umbar towns
    ("town_umbar_camp","Corsair_Camp",     icon_corsaircamp|pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.70,64.21),[],175),
# Imladris towns
    ("town_imladris_camp","Rivendell_Camp",icon_camp       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.47,-179.53),[],170),
# Dol Guldur towns
    ("town_dol_guldur","Dol_Guldur",       icon_dolguldur  |pf_tld_down,   no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.72,-160.69),[],170),
    ("town_dol_guldur_north_outpost","Dol_Guldur North Outpost",  icon_dolguldur  |pf_tld_down,   no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63,-261),[],170),
# Rhun towns (Formerly Northmen)
    ("town_north_rhun_camp","Northern_Rhun_Camp",     icon_nomadcamp  |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120,-332),[],170),
#    ("town_rhun_encampment","Rhun_Encampment",        icon_nomadcamp  |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.09,-365.12),[],170),
    ("town_rhun_south_camp","Rhun_Southern Outpost",  icon_nomadcamp  |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121,-270),[],170),
    ("town_rhun_north_camp","Rhun_Northern Outpost",  icon_nomadcamp  |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120,-369),[],170),
# Gundabad towns
    ("town_gundabad_camp","Mt._Gundabad_Orc_Camp",                icon_camp       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16,-321),[],170),
    ("town_gundabad_ne_outpost","Mt._Gundabad_NE_Outpost",        icon_camp       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77,-377),[],170),
    ("town_gundabad_nw_outpost","Mt._Gundabad_NW_Outpost",        icon_camp       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27,-363),[],170),
    ("town_goblin_north_outpost","Mtn. Goblin Northern Outpost",  icon_camp       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27,-313),[],170),
    ("town_goblin_south_outpost","Mtn._Goblin Southern Outpost",  icon_camp       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22,-277),[],170),
    ("town_gundabad_mirkwood_outpost","Mt._Gundabad_Mirkwood_Outpost",  icon_camp |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44,-320),[],170),

# Dwarves towns
    ("town_erebor"       ,"Erebor",                 icon_town       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.08,-339.50),[],170),
    ("town_erebor_mining_camp","Erebor Mining Camp",icon_camp       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72,-366),[],170),
    ("town_ironhill_camp","Iron_Hill_Dwarf_Camp",   icon_camp       |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-88,-365),[],170),

#    ("town_pelargir_port","Port",            icon_gondortown         |pf_tld_down, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.48,59.15),[],240),

####DONE TLD TOWNS

# stuff from native
 ("castle_1","Ethring",icon_castle_a|pf_tld_down|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.5,27.5),[],50),
# ("village_1", "Yaragar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15,0),[], 100),

### TLD map icons
   ("Argonath","argonath",icon_argonath|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.8,-62.7),[],180),
   ("Argonath2","argonath",icon_argonath|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33,-62.7),[],180),
   #("Hand1","hand_isen",icon_hand_isen|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.8,-59.1),[],75),
   #("Hand2","hand_isen",icon_hand_isen|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.4,-57.3),[],75),
   #("Hand3","hand_isen",icon_hand_isen|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.5,-64.5),[],5),
   #("Hand4","hand_isen",icon_hand_isen|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.4,-64.5),[],5),
   ("hand_isen","hand_isen",icon_hand_isen|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.3,-64.5),[],185),

  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.83,-18.22),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.75,-4.49),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.80,-19.60),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.80,-16.60),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.48,-16.77),[]),

  ("training_ground"  ,"Training_Ground", pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.29,-12.72),[]),
  ("training_ground_1","Training_Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44,61),[],100),
  ("training_ground_2","Training_Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.66,55.54),[],100),
  ("training_ground_3","Training_Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.58,14.22),[],100),
  ("training_ground_4","Training_Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.51,-83.37),[],100),
  ("training_ground_5","Training_Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.32,-39.36),[],100),

#  bridge_a
  ("looter_spawn_point"   ,"looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(31.99,78.70),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"steppe_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(42,-73.30),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"forest_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35.23,1.85),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","mountain_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(46.40,22.40),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"sea_raider_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.13,-11.12),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"sea_raider_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(54.66,42.45),[(trp_looter,15,0)]),
 
 #####TLD PARTIES BEGIN##########
  ("gondor_test"  ,"gondor_test_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.4,-11.4),[(trp_looter,15,0)]),
  ("mordor_test"  ,"mordor_test_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.2,-11.1),[(trp_looter,15,0)]),
  ("gondor_allies_test"  ,"gondor_allies_test_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.4,-11.2),[(trp_looter,15,0)]),
  ("isengard_test"  ,"isengard_test_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.2,-11.2),[(trp_looter,15,0)]),
  ("isen_rohan"  ,"isen_rohan_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(46.4,-36.4),[(trp_looter,15,0)]),
  ("mordor_gondor"  ,"mordor_gondor_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(41.4,-31.4),[(trp_looter,15,0)]),
  ("harad_gondor"  ,"harad_gondor_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(49.4,-39.4),[(trp_looter,15,0)]),
  ("corsair_gondor"  ,"corsair_gondor_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.2,-11.1),[(trp_looter,15,0)]),
  ("rhun_gondor"  ,"rhun_gondor_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.2,-11.1),[(trp_looter,15,0)]),
  ("khand_gondor"  ,"khand_gondor_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.2,-11.1),[(trp_looter,15,0)]),
  ("lorien_moria"  ,"lorien_moria_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.2,-11.1),[(trp_looter,15,0)]),
  ("gunda_woodelves"  ,"gunda_woodelves_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.2,-11.1),[(trp_looter,15,0)]),
  ("gunda_dwarves"  ,"gunda_dwarves_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-2.2,-11.1),[(trp_looter,15,0)]),
 
 # add extra towns before this point 
  ("spawn_points_end","last_spawn_point",pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(-3.05,-3.61),[(trp_looter,15,0)]),
 # pointers for scripting purposes
  ("pointer_player"           ,"bug",pf_disabled|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.48,-16.77),[]),
  ("pointer_z_0_steppe"       ,"bug",pf_disabled|pf_no_label|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210,87.9),[]),
  ("pointer_z_0_plain"        ,"bug",pf_disabled|pf_no_label|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210,83.0),[]),
  ("pointer_z_0_snow"         ,"bug",pf_disabled|pf_no_label|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210,78.6),[]),
  ("pointer_z_0_desert"       ,"bug",pf_disabled|pf_no_label|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210,74.5),[]),
  ("pointer_z_0_steppe_forest","bug",pf_disabled|pf_no_label|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213,87.9),[]),
  ("pointer_z_0_plain_forest" ,"bug",pf_disabled|pf_no_label|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213,83.0),[]),
  ("pointer_z_0_snow_forest"  ,"bug",pf_disabled|pf_no_label|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213,78.6),[]),
  ("pointer_z_0_desert_forest","bug",pf_disabled|pf_no_label|pf_hide_defenders|pf_is_static, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213,74.5),[]),
  ]
