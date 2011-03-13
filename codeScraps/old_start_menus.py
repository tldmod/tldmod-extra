#MEN FACTION PAGE
("start_man_2",menu_text_color(0xFF000000)|mnf_disable_all_keys,
 "^^^^^^^^To whom are you in service?..", "none",[],
 [("start_gondor"  ,[],"Gondor"  ,[(call_script,"script_player_join_faction","fac_gondor"  ),(troop_set_type,"trp_player",tf_gondor),(jump_to_menu,"mnu_start_character_gondor"),]),
  ("start_rohan"   ,[],"Rohan"   ,[(call_script,"script_player_join_faction","fac_rohan"   ),(troop_set_type,"trp_player",tf_rohan ),(jump_to_menu,"mnu_start_character_rohan"),]),
  ("start_northmen",[],"Northmen",[(call_script,"script_player_join_faction","fac_gondor"  ),(jump_to_menu,"mnu_start_northmen_2"),]),
  ("start_isengard",[],"Isengard",[(call_script,"script_player_join_faction","fac_isengard"),(jump_to_menu,"mnu_start_character_isengard"),]),
  ("start_mordor"  ,[],"Mordor"  ,[(call_script,"script_player_join_faction","fac_mordor"  ),(jump_to_menu,"mnu_start_character_mordor"),]),
  ("go_back"       ,[],"Go back" ,[(change_screen_quit),]),    ]
),

#elf start
("start_elf_1",menu_text_color(0xFF000000)|mnf_disable_all_keys,
 "^^^^^^^^Select your character's gender...", "none",[],
 [("start_male"  ,[],"Male"   ,[(assign,"$character_gender",tf_male  ),(jump_to_menu,"mnu_start_elf_2"),]),
  ("start_female",[],"Female" ,[(assign,"$character_gender",tf_female),(jump_to_menu,"mnu_start_elf_2"),]),
  ("go_back"     ,[],"Go back",[(change_screen_quit),]),    ]
),
#ELF FACTION PAGE
("start_elf_2",menu_text_color(0xFF000000)|mnf_disable_all_keys,
 "^^^^^^^^Choose your heritage...", "none",[],
 [("start_loth"     ,[],"An elf of Lothlorien" ,[(call_script,"script_player_join_faction","fac_lorien" ),(troop_set_type,"trp_player",tf_lothlorien),(jump_to_menu,"mnu_start_character_loth_elf"),]),
  ("start_mirkwood" ,[],"A woodelf of Mirkwood",[(call_script,"script_player_join_faction","fac_woodelf"),(troop_set_type,"trp_player",tf_mirkwood  ),(jump_to_menu,"mnu_start_character_mirkwood_elf"),]),
#  ("start_rivendell",[],"An elf of Imladris"   ,[(call_script,"script_player_join_faction","fac_imladris"),(troop_set_type,"trp_player",tf_imladris),(jump_to_menu,"mnu_start_character_imladris_elf"), ]),
  ("go_back"        ,[],"Go back"              ,[(change_screen_quit),]),    ]
), 

#dwarf start
("start_dwarf_1",menu_text_color(0xFF000000)|mnf_disable_all_keys,
 "^^^^^^^^Choose your heritage...", "none",[(assign,"$character_gender",tf_male),],
 [("start_dwarf",[],"A Dwarf of Erebor",[(call_script, "script_player_join_faction", "fac_dwarf"), (troop_set_type,"trp_player",tf_dwarf),(jump_to_menu,"mnu_start_character_dwarf_2"),]),
  ("go_back"    ,[],"Go back"          ,[(change_screen_quit),]),    ]
), 
#beast start 
("start_beast_1",menu_text_color(0xFF000000)|mnf_disable_all_keys,
 "^^^^^^^^What kind of beast are you?..", "none",[(assign,"$character_gender",tf_male),],
 [("start_orc_sallow"   ,[],"Orc"                     ,[(troop_set_type,"trp_player",tf_orc    ),(jump_to_menu,"mnu_start_orc_2"                  ),]),
  ("start_uruk_mordor"  ,[],"Uruk (Mordor only)"      ,[(call_script,"script_player_join_faction","fac_mordor"  ),(troop_set_type,"trp_player",tf_uruk   ),(jump_to_menu,"mnu_start_character_uruk_mordor"  ),]),
  ("start_uruk_isengard",[],"Uruk-hai (Isengard only)",[(call_script,"script_player_join_faction","fac_isengard"),(troop_set_type,"trp_player",tf_urukhai),(jump_to_menu,"mnu_start_character_uruk_isengard"),]),
  ("go_back"            ,[],"Go back"                 ,[(change_screen_quit),]),     ]
), 
#ORC FACTION PAGE
("start_orc_2",menu_text_color(0xFF000000)|mnf_disable_all_keys,
 "^^^^^^^^Choose your path...", "none",[(troop_set_type,"trp_player",tf_orc),],
 [("start_orc_isen"  ,[],"Isengard",[(call_script, "script_player_join_faction", "fac_isengard"),(jump_to_menu,"mnu_start_character_orc_isengard"),]),
  ("start_orc_mordor",[],"Mordor"  ,[(call_script, "script_player_join_faction", "fac_mordor"  ),(jump_to_menu,"mnu_start_character_orc_mordor"  ),]),
  ("go_back"         ,[],"Go back" ,[(change_screen_quit),]),    ]
),   
#NORTHMEN FACTION PAGE
("start_northmen_2",menu_text_color(0xFF000000)|mnf_disable_all_keys,
 "^^^^^^^^Choose your path...", "none",[],
 [("start_northmen_dale",[],"Dale"    ,[(jump_to_menu,"mnu_start_character_orc_isengard"),]),
  ("start_dunedain"     ,[],"Dunedain",[(jump_to_menu,"mnu_start_dunedain_3"            ),]),
  ("go_back"            ,[],"Go back" ,[(change_screen_quit), ]),    ]
), 
#Dunedain heritage PAGE
("start_dunedain_3",menu_text_color(0xFF000000)|mnf_disable_all_keys,
 "^^^^^^^^You journeyed from...", "none", [],
 [("start_dunedain_2",[],"Rivendell",[(troop_set_type,"trp_player",tf_dunedain),(jump_to_menu,"mnu_start_character_orc_isengard"),]),
  ("go_back"         ,[],"Go back"  ,[(change_screen_quit),]),    ]
),


#Gondor character start
  ( "start_character_gondor",mnf_disable_all_keys,
    "^^^^^^^For many years you now have plied^your trade under the shadow of war...", "none", [],
    [("start_gondor_man_at_arms",[],"Gondorian Man-at-Arms",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_gondor_man_at_arms][1][x]) for x in range(len(start_chars[s_gondor_man_at_arms][1])) if start_chars[s_gondor_man_at_arms][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_gondor_man_at_arms][2][x]) for x in range(len(start_chars[s_gondor_man_at_arms][2])) if start_chars[s_gondor_man_at_arms][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_gondor_man_at_arms][3][x]) for x in range(len(start_chars[s_gondor_man_at_arms][3])) if start_chars[s_gondor_man_at_arms][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_gondor_man_at_arms][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_gondor_man_at_arms][5][2*x],start_chars[s_gondor_man_at_arms][5][2*x+1]) for x in range(len(start_chars[s_gondor_man_at_arms][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Gondor Squire
    ("start_gondor_squire",[],"Gondorian Squire",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_gondor_squire][1][x]) for x in range(len(start_chars[s_gondor_squire][1])) if start_chars[s_gondor_squire][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_gondor_squire][2][x]) for x in range(len(start_chars[s_gondor_squire][2])) if start_chars[s_gondor_squire][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_gondor_squire][3][x]) for x in range(len(start_chars[s_gondor_squire][3])) if start_chars[s_gondor_squire][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_gondor_squire][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_gondor_squire][5][2*x],start_chars[s_gondor_squire][5][2*x+1]) for x in range(len(start_chars[s_gondor_squire][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Gondor  Ranger_of_Ithilien
    ("start_ranger_of_ithilien",[],"Ranger of Ithilien",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_gondor_ranger][1][x]) for x in range(len(start_chars[s_gondor_ranger][1])) if start_chars[s_gondor_ranger][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_gondor_ranger][2][x]) for x in range(len(start_chars[s_gondor_ranger][2])) if start_chars[s_gondor_ranger][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_gondor_ranger][3][x]) for x in range(len(start_chars[s_gondor_ranger][3])) if start_chars[s_gondor_ranger][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_gondor_ranger][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_gondor_ranger][5][2*x],start_chars[s_gondor_ranger][5][2*x+1]) for x in range(len(start_chars[s_gondor_ranger][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Gondor Merchant
#    ("start_merchant",[],"A merchant.",[
#]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_gondor_merchant][1][x]) for x in range(len(start_chars[s_gondor_merchant][1])) if start_chars[s_gondor_merchant][1][x] != 0
#]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_gondor_merchant][2][x]) for x in range(len(start_chars[s_gondor_merchant][2])) if start_chars[s_gondor_merchant][2][x] != 0
#]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_gondor_merchant][3][x]) for x in range(len(start_chars[s_gondor_merchant][3])) if start_chars[s_gondor_merchant][3][x] != 0
#]+[  (troop_add_gold,         "trp_player",        start_chars[s_gondor_merchant][4]),
#]+[  (troop_add_item,         "trp_player", start_chars[s_gondor_merchant][5][2*x],start_chars[s_gondor_merchant][5][2*x+1]) for x in range(len(start_chars[s_gondor_merchant][5])/2) ]+[
#     (jump_to_menu,"mnu_choose_skill"),
#     ]),
    ("go_back",[],"Go back",[(jump_to_menu,"mnu_start_game_1"),]),
    ]
  ),  
################################
 # Rohan start
  ( "start_character_rohan",mnf_disable_all_keys,
    "^^^^^^^For many years you have plied ^your trade under the shadow of war...", "none", [],
   [("start_rider_of_rohan",[],"Rider of Rohan",
	 [#  (assign,"$background_type",cb_noble),
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_rohan_rider][1][x]) for x in range(len(start_chars[s_rohan_rider][1])) if start_chars[s_rohan_rider][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_rohan_rider][2][x]) for x in range(len(start_chars[s_rohan_rider][2])) if start_chars[s_rohan_rider][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_rohan_rider][3][x]) for x in range(len(start_chars[s_rohan_rider][3])) if start_chars[s_rohan_rider][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_rohan_rider][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_rohan_rider][5][2*x],start_chars[s_rohan_rider][5][2*x+1]) for x in range(len(start_chars[s_rohan_rider][5])/2) ]+[

     (jump_to_menu,"mnu_choose_skill"),
    ]),
#spearmen of rohan
    ("start_spearman_or_rohan",[],"Spearman of Rohan",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_rohan_spearman][1][x]) for x in range(len(start_chars[s_rohan_spearman][1])) if start_chars[s_rohan_spearman][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_rohan_spearman][2][x]) for x in range(len(start_chars[s_rohan_spearman][2])) if start_chars[s_rohan_spearman][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_rohan_spearman][3][x]) for x in range(len(start_chars[s_rohan_spearman][3])) if start_chars[s_rohan_spearman][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_rohan_spearman][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_rohan_spearman][5][2*x],start_chars[s_rohan_spearman][5][2*x+1]) for x in range(len(start_chars[s_rohan_spearman][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#scout of rohan
    ("start_scout_of_rohan",[],"Scout of Rohan",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_rohan_scout][1][x]) for x in range(len(start_chars[s_rohan_scout][1])) if start_chars[s_rohan_scout][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_rohan_scout][2][x]) for x in range(len(start_chars[s_rohan_scout][2])) if start_chars[s_rohan_scout][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_rohan_scout][3][x]) for x in range(len(start_chars[s_rohan_scout][3])) if start_chars[s_rohan_scout][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_rohan_scout][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_rohan_scout][5][2*x],start_chars[s_rohan_scout][5][2*x+1]) for x in range(len(start_chars[s_rohan_scout][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#rohan merchant
#    ("start_wandering_merchant",[],"A Wandering merchant",[
#]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_rohan_merchant][1][x]) for x in range(len(start_chars[s_rohan_merchant][1])) if start_chars[s_rohan_merchant][1][x] != 0
#]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_rohan_merchant][2][x]) for x in range(len(start_chars[s_rohan_merchant][2])) if start_chars[s_rohan_merchant][2][x] != 0
#]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_rohan_merchant][3][x]) for x in range(len(start_chars[s_rohan_merchant][3])) if start_chars[s_rohan_merchant][3][x] != 0
#]+[  (troop_add_gold,         "trp_player",        start_chars[s_rohan_merchant][4]),
#]+[  (troop_add_item,         "trp_player", start_chars[s_rohan_merchant][5][2*x],start_chars[s_rohan_merchant][5][2*x+1]) for x in range(len(start_chars[s_rohan_merchant][5])/2) ]+[
#     (jump_to_menu,"mnu_choose_skill"),
#    ]),
    ("go_back",[],"Go back",[(jump_to_menu,"mnu_start_game_1"),]),
   ]
  ), 

################################
 #Isengard start
  
  ( "start_character_isengard",mnf_disable_all_keys,
    "^^^^^^^For many years you have plied ^your trade under the shadow of war...", "none", [],
    [
#These four will need their faction applied now and not in the faction screen.
    ("start_dunlending_warrior",[],"Dunlending Warrior",[
        (troop_set_type,"trp_player",4),
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_dun_warrior][1][x]) for x in range(len(start_chars[s_dun_warrior][1])) if start_chars[s_dun_warrior][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_dun_warrior][2][x]) for x in range(len(start_chars[s_dun_warrior][2])) if start_chars[s_dun_warrior][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_dun_warrior][3][x]) for x in range(len(start_chars[s_dun_warrior][3])) if start_chars[s_dun_warrior][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_dun_warrior][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_dun_warrior][5][2*x],start_chars[s_dun_warrior][5][2*x+1]) for x in range(len(start_chars[s_dun_warrior][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#dunlending horsemen
    ("start_dunlending_horseman",[],"Dunlending Horseman",[
        (troop_set_type,"trp_player",4),
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_dun_horseman][1][x]) for x in range(len(start_chars[s_dun_horseman][1])) if start_chars[s_dun_horseman][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_dun_horseman][2][x]) for x in range(len(start_chars[s_dun_horseman][2])) if start_chars[s_dun_horseman][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_dun_horseman][3][x]) for x in range(len(start_chars[s_dun_horseman][3])) if start_chars[s_dun_horseman][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_dun_horseman][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_dun_horseman][5][2*x],start_chars[s_dun_horseman][5][2*x+1]) for x in range(len(start_chars[s_dun_horseman][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Spy of isengard
    ("start_spy_of_isengard",[],"Spy of Isengard",[
        (troop_set_type,"trp_player",15),
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_isengard_spy][1][x]) for x in range(len(start_chars[s_isengard_spy][1])) if start_chars[s_isengard_spy][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_isengard_spy][2][x]) for x in range(len(start_chars[s_isengard_spy][2])) if start_chars[s_isengard_spy][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_isengard_spy][3][x]) for x in range(len(start_chars[s_isengard_spy][3])) if start_chars[s_isengard_spy][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_isengard_spy][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_isengard_spy][5][2*x],start_chars[s_isengard_spy][5][2*x+1]) for x in range(len(start_chars[s_isengard_spy][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#isengard prophet
    ("start_isengard_prophet",[],"Prophet of Isengard",[
        (troop_set_type,"trp_player",15),
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_isengard_prophet][1][x]) for x in range(len(start_chars[s_isengard_prophet][1])) if start_chars[s_isengard_prophet][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_isengard_prophet][2][x]) for x in range(len(start_chars[s_isengard_prophet][2])) if start_chars[s_isengard_prophet][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_isengard_prophet][3][x]) for x in range(len(start_chars[s_isengard_prophet][3])) if start_chars[s_isengard_prophet][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_isengard_prophet][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_isengard_prophet][5][2*x],start_chars[s_isengard_prophet][5][2*x+1]) for x in range(len(start_chars[s_isengard_prophet][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
    ("go_back",[],"Go back",
     [(jump_to_menu,"mnu_start_game_1"),
    ]),
    ]
  ), 

################################
 #Mordor start
  ( "start_character_mordor",mnf_disable_all_keys,
    "^^^^^^^^For many years you have plied ^your trade under the shadow of war...",
    "none",
    [ (str_clear,s10), (str_clear,s11), (str_clear,s12), (str_clear,s13), (str_clear,s14), (str_clear,s15),],
    [
#These four will need their faction applied now and not in the faction screen.
    ("start_warrior_of_sauron",[],"Warrior of Sauron",[
        (troop_set_type,"trp_player",15),
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_warrior_sauron][1][x]) for x in range(len(start_chars[s_warrior_sauron][1])) if start_chars[s_warrior_sauron][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_warrior_sauron][2][x]) for x in range(len(start_chars[s_warrior_sauron][2])) if start_chars[s_warrior_sauron][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_warrior_sauron][3][x]) for x in range(len(start_chars[s_warrior_sauron][3])) if start_chars[s_warrior_sauron][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_warrior_sauron][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_warrior_sauron][5][2*x],start_chars[s_warrior_sauron][5][2*x+1]) for x in range(len(start_chars[s_warrior_sauron][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#easterling  horsemen
    ("start_easterling_horsemen",[],"Easterling Horseman",[
        (troop_set_type,"trp_player",15),
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_east_horseman][1][x]) for x in range(len(start_chars[s_east_horseman][1])) if start_chars[s_east_horseman][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_east_horseman][2][x]) for x in range(len(start_chars[s_east_horseman][2])) if start_chars[s_east_horseman][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_east_horseman][3][x]) for x in range(len(start_chars[s_east_horseman][3])) if start_chars[s_east_horseman][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_east_horseman][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_east_horseman][5][2*x],start_chars[s_east_horseman][5][2*x+1]) for x in range(len(start_chars[s_east_horseman][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),

#haradrim archer
    ("start_haradrim_archer",[],"Haradrim Archer",[
        (troop_set_type,"trp_player",8),
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_harad_archer][1][x]) for x in range(len(start_chars[s_harad_archer][1])) if start_chars[s_harad_archer][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_harad_archer][2][x]) for x in range(len(start_chars[s_harad_archer][2])) if start_chars[s_harad_archer][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_harad_archer][3][x]) for x in range(len(start_chars[s_harad_archer][3])) if start_chars[s_harad_archer][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_harad_archer][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_harad_archer][5][2*x],start_chars[s_harad_archer][5][2*x+1]) for x in range(len(start_chars[s_harad_archer][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
	
#Warrior of Rhun	
    ("start_warrior_of_rhun",[],"Warrior of Rhun",[
        (troop_set_type,"trp_player",15),
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_rhun_warrior][1][x]) for x in range(len(start_chars[s_rhun_warrior][1])) if start_chars[s_rhun_warrior][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_rhun_warrior][2][x]) for x in range(len(start_chars[s_rhun_warrior][2])) if start_chars[s_rhun_warrior][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_rhun_warrior][3][x]) for x in range(len(start_chars[s_rhun_warrior][3])) if start_chars[s_rhun_warrior][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_rhun_warrior][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_rhun_warrior][5][2*x],start_chars[s_rhun_warrior][5][2*x+1]) for x in range(len(start_chars[s_rhun_warrior][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
	
#mordor priest
    ("start_priest_of_eye",[],"Priest of the Lidless Eye",[
        (troop_set_type,"trp_player",15),
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_mordor_priest][1][x]) for x in range(len(start_chars[s_mordor_priest][1])) if start_chars[s_mordor_priest][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_mordor_priest][2][x]) for x in range(len(start_chars[s_mordor_priest][2])) if start_chars[s_mordor_priest][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_mordor_priest][3][x]) for x in range(len(start_chars[s_mordor_priest][3])) if start_chars[s_mordor_priest][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_mordor_priest][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_mordor_priest][5][2*x],start_chars[s_mordor_priest][5][2*x+1]) for x in range(len(start_chars[s_mordor_priest][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
    ("go_back",[],"Go back",
     [(jump_to_menu,"mnu_start_game_1"),
    ]),
    ]
  ), 
  
################################Knight of Rivendell
#LOTHLORIEN start
  ( "start_character_loth_elf",mnf_disable_all_keys,
    "^^^^^^^^Your previous training...",
    "none",
    [ (str_clear,s10), (str_clear,s11), (str_clear,s12), (str_clear,s13), (str_clear,s14), (str_clear,s15), ],
    [
#These four will need their faction applied now and not in the faction screen.
    ("start_loth_swordsman",[],"Lothlorien Swordsman",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_lorien_swordsman][1][x]) for x in range(len(start_chars[s_lorien_swordsman][1])) if start_chars[s_lorien_swordsman][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_lorien_swordsman][2][x]) for x in range(len(start_chars[s_lorien_swordsman][2])) if start_chars[s_lorien_swordsman][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_lorien_swordsman][3][x]) for x in range(len(start_chars[s_lorien_swordsman][3])) if start_chars[s_lorien_swordsman][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_lorien_swordsman][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_lorien_swordsman][5][2*x],start_chars[s_lorien_swordsman][5][2*x+1]) for x in range(len(start_chars[s_lorien_swordsman][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#rivendell rider	
    ("start_rider_of_rivendell",[],"Rider of Rivendell",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_rivendell_rider][1][x]) for x in range(len(start_chars[s_rivendell_rider][1])) if start_chars[s_rivendell_rider][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_rivendell_rider][2][x]) for x in range(len(start_chars[s_rivendell_rider][2])) if start_chars[s_rivendell_rider][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_rivendell_rider][3][x]) for x in range(len(start_chars[s_rivendell_rider][3])) if start_chars[s_rivendell_rider][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_rivendell_rider][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_rivendell_rider][5][2*x],start_chars[s_rivendell_rider][5][2*x+1]) for x in range(len(start_chars[s_rivendell_rider][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
	
#A forest Warden
    ("start_loth_warden",[],"A forest Warden",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_lorien_warden][1][x]) for x in range(len(start_chars[s_lorien_warden][1])) if start_chars[s_lorien_warden][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_lorien_warden][2][x]) for x in range(len(start_chars[s_lorien_warden][2])) if start_chars[s_lorien_warden][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_lorien_warden][3][x]) for x in range(len(start_chars[s_lorien_warden][3])) if start_chars[s_lorien_warden][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_lorien_warden][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_lorien_warden][5][2*x],start_chars[s_lorien_warden][5][2*x+1]) for x in range(len(start_chars[s_lorien_warden][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),

#Loth archer
    ("start_loth_archer",[],"Lothlorien Archer",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_lorien_archer][1][x]) for x in range(len(start_chars[s_lorien_archer][1])) if start_chars[s_lorien_archer][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_lorien_archer][2][x]) for x in range(len(start_chars[s_lorien_archer][2])) if start_chars[s_lorien_archer][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_lorien_archer][3][x]) for x in range(len(start_chars[s_lorien_archer][3])) if start_chars[s_lorien_archer][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_lorien_archer][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_lorien_archer][5][2*x],start_chars[s_lorien_archer][5][2*x+1]) for x in range(len(start_chars[s_lorien_archer][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
	
#loth healer
    ("start_loth_healer",[],"A lay Healer",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_lorien_healer][1][x]) for x in range(len(start_chars[s_lorien_healer][1])) if start_chars[s_lorien_healer][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_lorien_healer][2][x]) for x in range(len(start_chars[s_lorien_healer][2])) if start_chars[s_lorien_healer][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_lorien_healer][3][x]) for x in range(len(start_chars[s_lorien_healer][3])) if start_chars[s_lorien_healer][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_lorien_healer][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_lorien_healer][5][2*x],start_chars[s_lorien_healer][5][2*x+1]) for x in range(len(start_chars[s_lorien_healer][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
    ("go_back",[],"Go back",[(jump_to_menu,"mnu_start_game_1"),]),
   ]
  ),   


################################
 #MIRKWOOD start
  
 ( "start_character_mirkwood_elf",mnf_disable_all_keys,
   "^^^^^^^^Your previous training...",
   "none",
   [(str_clear,s10),(str_clear,s11),(str_clear,s12),(str_clear,s13),(str_clear,s14),(str_clear,s15),],
   [
#These four will need their faction applied now and not in the faction screen.
    ("start_mirkwood_swordsman",[],"Mirkwood Spearman",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_woodelf_swordsman][1][x]) for x in range(len(start_chars[s_woodelf_swordsman][1])) if start_chars[s_woodelf_swordsman][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_woodelf_swordsman][2][x]) for x in range(len(start_chars[s_woodelf_swordsman][2])) if start_chars[s_woodelf_swordsman][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_woodelf_swordsman][3][x]) for x in range(len(start_chars[s_woodelf_swordsman][3])) if start_chars[s_woodelf_swordsman][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_woodelf_swordsman][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_woodelf_swordsman][5][2*x],start_chars[s_woodelf_swordsman][5][2*x+1]) for x in range(len(start_chars[s_woodelf_swordsman][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#A mirkwood Warden
    ("start_mirkwood_warden",[],"A forest Warden",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_woodelf_warden][1][x]) for x in range(len(start_chars[s_woodelf_warden][1])) if start_chars[s_woodelf_warden][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_woodelf_warden][2][x]) for x in range(len(start_chars[s_woodelf_warden][2])) if start_chars[s_woodelf_warden][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_woodelf_warden][3][x]) for x in range(len(start_chars[s_woodelf_warden][3])) if start_chars[s_woodelf_warden][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_woodelf_warden][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_woodelf_warden][5][2*x],start_chars[s_woodelf_warden][5][2*x+1]) for x in range(len(start_chars[s_woodelf_warden][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#mirkwood archer
    ("start_mirk_archer",[],"Mirkwood Archer",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_woodelf_archer][1][x]) for x in range(len(start_chars[s_woodelf_archer][1])) if start_chars[s_woodelf_archer][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_woodelf_archer][2][x]) for x in range(len(start_chars[s_woodelf_archer][2])) if start_chars[s_woodelf_archer][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_woodelf_archer][3][x]) for x in range(len(start_chars[s_woodelf_archer][3])) if start_chars[s_woodelf_archer][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_woodelf_archer][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_woodelf_archer][5][2*x],start_chars[s_woodelf_archer][5][2*x+1]) for x in range(len(start_chars[s_woodelf_archer][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#mirkwood healer
    ("start_mirk_healer",[],"A lay Healer",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_woodelf_healer][1][x]) for x in range(len(start_chars[s_woodelf_healer][1])) if start_chars[s_woodelf_healer][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_woodelf_healer][2][x]) for x in range(len(start_chars[s_woodelf_healer][2])) if start_chars[s_woodelf_healer][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_woodelf_healer][3][x]) for x in range(len(start_chars[s_woodelf_healer][3])) if start_chars[s_woodelf_healer][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_woodelf_healer][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_woodelf_healer][5][2*x],start_chars[s_woodelf_healer][5][2*x+1]) for x in range(len(start_chars[s_woodelf_healer][5])/2) ]+[
      (jump_to_menu,"mnu_choose_skill"),
      ]),
    ("go_back",[],"Go back",[(jump_to_menu,"mnu_start_game_1"),]),
   ]
  ),   
  
 
################################
 #Isengard orc start
  ( "start_character_orc_isengard",mnf_disable_all_keys,
    "^^^^^^^^For many years now you have prepared for the war behind impenetrable Isengard walls.^Soon your wait will be over...", "none",
    [(str_clear,s10),(str_clear,s11),(str_clear,s12),(str_clear,s13),(str_clear,s14),(str_clear,s15),],
    [ #These four will need their faction applied now and not in the faction screen.
    ("start_orc_warrior",[],"Orc Warrior",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_isen_orc_warrior][1][x]) for x in range(len(start_chars[s_isen_orc_warrior][1])) if start_chars[s_isen_orc_warrior][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_isen_orc_warrior][2][x]) for x in range(len(start_chars[s_isen_orc_warrior][2])) if start_chars[s_isen_orc_warrior][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_isen_orc_warrior][3][x]) for x in range(len(start_chars[s_isen_orc_warrior][3])) if start_chars[s_isen_orc_warrior][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_isen_orc_warrior][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_isen_orc_warrior][5][2*x],start_chars[s_isen_orc_warrior][5][2*x+1]) for x in range(len(start_chars[s_isen_orc_warrior][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Wolf Rider
    ("start_worlf_rider",[],"Wolf Rider",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_isen_wolf_rider][1][x]) for x in range(len(start_chars[s_isen_wolf_rider][1])) if start_chars[s_isen_wolf_rider][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_isen_wolf_rider][2][x]) for x in range(len(start_chars[s_isen_wolf_rider][2])) if start_chars[s_isen_wolf_rider][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_isen_wolf_rider][3][x]) for x in range(len(start_chars[s_isen_wolf_rider][3])) if start_chars[s_isen_wolf_rider][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_isen_wolf_rider][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_isen_wolf_rider][5][2*x],start_chars[s_isen_wolf_rider][5][2*x+1]) for x in range(len(start_chars[s_isen_wolf_rider][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#orc tracker
    ("start_orc_tracker",[],"Orc Tracker",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_isen_orc_tracker][1][x]) for x in range(len(start_chars[s_isen_orc_tracker][1])) if start_chars[s_isen_orc_tracker][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_isen_orc_tracker][2][x]) for x in range(len(start_chars[s_isen_orc_tracker][2])) if start_chars[s_isen_orc_tracker][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_isen_orc_tracker][3][x]) for x in range(len(start_chars[s_isen_orc_tracker][3])) if start_chars[s_isen_orc_tracker][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_isen_orc_tracker][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_isen_orc_tracker][5][2*x],start_chars[s_isen_orc_tracker][5][2*x+1]) for x in range(len(start_chars[s_isen_orc_tracker][5])/2) ]+[
      (jump_to_menu,"mnu_choose_skill"),
      ]),
    ("go_back",[],"Go back",[(jump_to_menu,"mnu_start_game_1"),]),
    ]
  ),  
  
################################
 #Mordor orc start
  ( "start_character_orc_mordor",mnf_disable_all_keys,
    "^^^^^^^^For many years now you have prepared for war in vast Gorgoroth camps.^Soon your wait will be over...",
    "none",
    [(str_clear,s10),(str_clear,s11),(str_clear,s12),(str_clear,s13),(str_clear,s14),(str_clear,s15),],
    [#These four will need their faction applied now and not in the faction screen.
    ("start_orc_warrior_m",[],"Orc Warrior",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_mordor_orc_warrior][1][x]) for x in range(len(start_chars[s_mordor_orc_warrior][1])) if start_chars[s_mordor_orc_warrior][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_mordor_orc_warrior][2][x]) for x in range(len(start_chars[s_mordor_orc_warrior][2])) if start_chars[s_mordor_orc_warrior][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_mordor_orc_warrior][3][x]) for x in range(len(start_chars[s_mordor_orc_warrior][3])) if start_chars[s_mordor_orc_warrior][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_mordor_orc_warrior][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_mordor_orc_warrior][5][2*x],start_chars[s_mordor_orc_warrior][5][2*x+1]) for x in range(len(start_chars[s_mordor_orc_warrior][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Wolf Rider mordor
    ("start_warg_rider_m",[],"Warg Rider",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_mordor_warg_rider][1][x]) for x in range(len(start_chars[s_mordor_warg_rider][1])) if start_chars[s_mordor_warg_rider][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_mordor_warg_rider][2][x]) for x in range(len(start_chars[s_mordor_warg_rider][2])) if start_chars[s_mordor_warg_rider][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_mordor_warg_rider][3][x]) for x in range(len(start_chars[s_mordor_warg_rider][3])) if start_chars[s_mordor_warg_rider][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_mordor_warg_rider][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_mordor_warg_rider][5][2*x],start_chars[s_mordor_warg_rider][5][2*x+1]) for x in range(len(start_chars[s_mordor_warg_rider][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#orc tracker mordor
    ("start_orc_tracker_m",[],"Orc Tracker",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_mordor_orc_tracker][1][x]) for x in range(len(start_chars[s_mordor_orc_tracker][1])) if start_chars[s_mordor_orc_tracker][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_mordor_orc_tracker][2][x]) for x in range(len(start_chars[s_mordor_orc_tracker][2])) if start_chars[s_mordor_orc_tracker][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_mordor_orc_tracker][3][x]) for x in range(len(start_chars[s_mordor_orc_tracker][3])) if start_chars[s_mordor_orc_tracker][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_mordor_orc_tracker][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_mordor_orc_tracker][5][2*x],start_chars[s_mordor_orc_tracker][5][2*x+1]) for x in range(len(start_chars[s_mordor_orc_tracker][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
	("go_back",[],"Go back",[(jump_to_menu,"mnu_start_game_1"),]),
    ]
  ),    

################################
#Mordor uruk start
  ( "start_character_uruk_mordor",mnf_disable_all_keys,
    "^^^^^^^^For many years now you have prepared for war in vast Gorgoroth camps.^Soon your wait will be over...",
    "none",
    [ (str_clear,s10), (str_clear,s11), (str_clear,s12), (str_clear,s13), (str_clear,s14), (str_clear,s15), ],
    [
#These four will need their faction applied now and not in the faction screen.
    ("start_uruk_warrior_m",[],"Uruk Warrior",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_mordor_uruk_warrior][1][x]) for x in range(len(start_chars[s_mordor_uruk_warrior][1])) if start_chars[s_mordor_uruk_warrior][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_mordor_uruk_warrior][2][x]) for x in range(len(start_chars[s_mordor_uruk_warrior][2])) if start_chars[s_mordor_uruk_warrior][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_mordor_uruk_warrior][3][x]) for x in range(len(start_chars[s_mordor_uruk_warrior][3])) if start_chars[s_mordor_uruk_warrior][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_mordor_uruk_warrior][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_mordor_uruk_warrior][5][2*x],start_chars[s_mordor_uruk_warrior][5][2*x+1]) for x in range(len(start_chars[s_mordor_uruk_warrior][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Uruk Tracker
    ("start_uruk_tracker",[],"Uruk Tracker",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_mordor_uruk_tracker][1][x]) for x in range(len(start_chars[s_mordor_uruk_tracker][1])) if start_chars[s_mordor_uruk_tracker][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_mordor_uruk_tracker][2][x]) for x in range(len(start_chars[s_mordor_uruk_tracker][2])) if start_chars[s_mordor_uruk_tracker][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_mordor_uruk_tracker][3][x]) for x in range(len(start_chars[s_mordor_uruk_tracker][3])) if start_chars[s_mordor_uruk_tracker][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_mordor_uruk_tracker][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_mordor_uruk_tracker][5][2*x],start_chars[s_mordor_uruk_tracker][5][2*x+1]) for x in range(len(start_chars[s_mordor_uruk_tracker][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Uruk Berserker
    ("start_uruk_bers",[],"Uruk Berserker",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_mordor_uruk_berserk][1][x]) for x in range(len(start_chars[s_mordor_uruk_berserk][1])) if start_chars[s_mordor_uruk_berserk][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_mordor_uruk_berserk][2][x]) for x in range(len(start_chars[s_mordor_uruk_berserk][2])) if start_chars[s_mordor_uruk_berserk][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_mordor_uruk_berserk][3][x]) for x in range(len(start_chars[s_mordor_uruk_berserk][3])) if start_chars[s_mordor_uruk_berserk][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_mordor_uruk_berserk][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_mordor_uruk_berserk][5][2*x],start_chars[s_mordor_uruk_berserk][5][2*x+1]) for x in range(len(start_chars[s_mordor_uruk_berserk][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
	("go_back",[],"Go back",[(jump_to_menu,"mnu_start_game_1"),]),
    ]
  ),
  
################################
 #Isengard uruk-hai start
  
  ( "start_character_uruk_isengard",mnf_disable_all_keys,
    "^^^^^^^You have just been hatched from your breeding pen.^All you think about now is war!",
    "none",
    [(str_clear,s10),(str_clear,s11),(str_clear,s12),(str_clear,s13),(str_clear,s14),(str_clear,s15),],
    [
#These four will need their faction applied now and not in the faction screen.
    ("start_uruk-hai_warrior",[],"Uruk-hai Warrior",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_isen_uhai_warrior][1][x]) for x in range(len(start_chars[s_isen_uhai_warrior][1])) if start_chars[s_isen_uhai_warrior][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_isen_uhai_warrior][2][x]) for x in range(len(start_chars[s_isen_uhai_warrior][2])) if start_chars[s_isen_uhai_warrior][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_isen_uhai_warrior][3][x]) for x in range(len(start_chars[s_isen_uhai_warrior][3])) if start_chars[s_isen_uhai_warrior][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_isen_uhai_warrior][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_isen_uhai_warrior][5][2*x],start_chars[s_isen_uhai_warrior][5][2*x+1]) for x in range(len(start_chars[s_isen_uhai_warrior][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Uruk-hai Tracker
    ("start_urukhai_tracker",[],"Uruk-hai Archer",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_isen_uhai_tracker][1][x]) for x in range(len(start_chars[s_isen_uhai_tracker][1])) if start_chars[s_isen_uhai_tracker][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_isen_uhai_tracker][2][x]) for x in range(len(start_chars[s_isen_uhai_tracker][2])) if start_chars[s_isen_uhai_tracker][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_isen_uhai_tracker][3][x]) for x in range(len(start_chars[s_isen_uhai_tracker][3])) if start_chars[s_isen_uhai_tracker][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_isen_uhai_tracker][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_isen_uhai_tracker][5][2*x],start_chars[s_isen_uhai_tracker][5][2*x+1]) for x in range(len(start_chars[s_isen_uhai_tracker][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Uruk-hai Berserker
    ("start_urukhai_bers",[],"Uruk-hai Berserker",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_isen_uhai_berserk][1][x]) for x in range(len(start_chars[s_isen_uhai_berserk][1])) if start_chars[s_isen_uhai_berserk][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_isen_uhai_berserk][2][x]) for x in range(len(start_chars[s_isen_uhai_berserk][2])) if start_chars[s_isen_uhai_berserk][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_isen_uhai_berserk][3][x]) for x in range(len(start_chars[s_isen_uhai_berserk][3])) if start_chars[s_isen_uhai_berserk][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_isen_uhai_berserk][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_isen_uhai_berserk][5][2*x],start_chars[s_isen_uhai_berserk][5][2*x+1]) for x in range(len(start_chars[s_isen_uhai_berserk][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
	("go_back",[],"Go back", [(jump_to_menu,"mnu_start_game_1"),]),
   ]
  ),  
  
  ################################
 #Erebor dwarf start
  ( "start_character_dwarf_2",mnf_disable_all_keys,
    "^^^^^^^^For many years now you have plied ^your trade under the shadow of war...", "none",
    [(str_clear,s10),(str_clear,s11),(str_clear,s12),(str_clear,s13),(str_clear,s14),(str_clear,s15),],
    [#These four will need their faction applied now and not in the faction screen.
     ("start_dwarf_warrior",[],"Dwarf Warrior",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_dwarf_warrior][1][x]) for x in range(len(start_chars[s_dwarf_warrior][1])) if start_chars[s_dwarf_warrior][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_dwarf_warrior][2][x]) for x in range(len(start_chars[s_dwarf_warrior][2])) if start_chars[s_dwarf_warrior][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_dwarf_warrior][3][x]) for x in range(len(start_chars[s_dwarf_warrior][3])) if start_chars[s_dwarf_warrior][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_dwarf_warrior][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_dwarf_warrior][5][2*x],start_chars[s_dwarf_warrior][5][2*x+1]) for x in range(len(start_chars[s_dwarf_warrior][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#Dwarf Archer
    ("start_dwarf_archer",[],"Dwarf Archer",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_dwarf_archer][1][x]) for x in range(len(start_chars[s_dwarf_archer][1])) if start_chars[s_dwarf_archer][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_dwarf_archer][2][x]) for x in range(len(start_chars[s_dwarf_archer][2])) if start_chars[s_dwarf_archer][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_dwarf_archer][3][x]) for x in range(len(start_chars[s_dwarf_archer][3])) if start_chars[s_dwarf_archer][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_dwarf_archer][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_dwarf_archer][5][2*x],start_chars[s_dwarf_archer][5][2*x+1]) for x in range(len(start_chars[s_dwarf_archer][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
#dwarf_crafstman
    ("start_dwarf_crafstman",[],"Dwarf Craftsman",[
]+[  (troop_raise_attribute,  "trp_player",x     , start_chars[s_dwarf_craftsman][1][x]) for x in range(len(start_chars[s_dwarf_craftsman][1])) if start_chars[s_dwarf_craftsman][1][x] != 0
]+[  (troop_raise_skill,"trp_player",skl_order[x], start_chars[s_dwarf_craftsman][2][x]) for x in range(len(start_chars[s_dwarf_craftsman][2])) if start_chars[s_dwarf_craftsman][2][x] != 0
]+[  (troop_raise_proficiency,"trp_player",x     , start_chars[s_dwarf_craftsman][3][x]) for x in range(len(start_chars[s_dwarf_craftsman][3])) if start_chars[s_dwarf_craftsman][3][x] != 0
]+[  (troop_add_gold,         "trp_player",        start_chars[s_dwarf_craftsman][4]),
]+[  (troop_add_item,         "trp_player", start_chars[s_dwarf_craftsman][5][2*x],start_chars[s_dwarf_craftsman][5][2*x+1]) for x in range(len(start_chars[s_dwarf_craftsman][5])/2) ]+[
     (jump_to_menu,"mnu_choose_skill"),
    ]),
	("go_back",[],"Go back", [(jump_to_menu,"mnu_start_game_1"),]),
   ]
  ),  
