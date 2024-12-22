#include <mc_proto/universal_types.h>
typedef mc_proto_varint mc_proto_69_optvarint;

typedef struct {
	uint8_t *data;
	mc_proto_varint len;
} mc_proto_69_ByteArray;

typedef char *mc_proto_69_string;

typedef struct {
	float x;
	float y;
} mc_proto_69_vec2f;

typedef struct {
	float x;
	float y;
	float z;
} mc_proto_69_vec3f;

typedef struct {
	float x;
	float y;
	float z;
	float w;
} mc_proto_69_vec4f;

typedef struct {
	double x;
	double y;
	double z;
} mc_proto_69_vec3f64;

typedef /* <class 'jinja2.exceptions.TemplateNotFound'>: registryEntryHolderSet/structline.j2 */

	typedef mc_proto_varint mc_proto_69_ContainerID;

typedef struct {
	mc_proto_69_string soundName;
	struct {
		bool present;
		float data;
	} fixedRange;
} mc_proto_69_SoundEvent;

typedef struct {
	enum {
		mc_proto_69_SlotDisplay_type_empty = 0,
		mc_proto_69_SlotDisplay_type_any_fuel = 1,
		mc_proto_69_SlotDisplay_type_item = 2,
		mc_proto_69_SlotDisplay_type_item_stack = 3,
		mc_proto_69_SlotDisplay_type_tag = 4,
		mc_proto_69_SlotDisplay_type_smithing_trim = 5,
		mc_proto_69_SlotDisplay_type_with_remainder = 6,
		mc_proto_69_SlotDisplay_type_composite = 7,
	} type;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
		mc_proto_varint item;
		mc_proto_69_Slot item_stack;
		mc_proto_69_string tag;
		struct {
			mc_proto_69_SlotDisplay base;
			mc_proto_69_SlotDisplay material;
			mc_proto_69_SlotDisplay pattern;
		} simthing_trim;
		struct {
			mc_proto_69_SlotDisplay input;
			mc_proto_69_SlotDisplay remainder;
		} with_remainder;
		struct {
			mc_proto_varint count;
			mc_proto_69_SlotDisplay data[];
		} composite;
	} data;
} mc_proto_69_SlotDisplay;


typedef struct {
	enum {
		mc_proto_69_RecipeDisplay_type_crafting_shapeless = 0,
		mc_proto_69_RecipeDisplay_type_crafting_shaped = 1,
		mc_proto_69_RecipeDisplay_type_furnace = 2,
		mc_proto_69_RecipeDisplay_type_stonecutter = 3,
		mc_proto_69_RecipeDisplay_type_smithing = 4,
	} type;
	union {
		struct {
			struct {
				mc_proto_varint count;
				mc_proto_69_SlotDisplay data[];
			} ingredients;
			mc_proto_69_SlotDisplay result;
			mc_proto_69_SlotDisplay craftingStation;
		} crafting_shapeless;
		struct {
			mc_proto_varint width;
			mc_proto_varint height;
			struct {
				mc_proto_varint count;
				mc_proto_69_SlotDisplay data[];
			} ingredients;
			mc_proto_69_SlotDisplay result;
			mc_proto_69_SlotDisplay craftingStation;
		} crafting_shaped;
		struct {
			mc_proto_69_SlotDisplay ingredient;
			mc_proto_69_SlotDisplay fuel;
			mc_proto_69_SlotDisplay result;
			mc_proto_69_SlotDisplay craftingStation;
			mc_proto_varint duration;
			float experience;
		} furnace;
		struct {
			mc_proto_69_SlotDisplay ingredient;
			mc_proto_69_SlotDisplay result;
			mc_proto_69_SlotDisplay craftingStation;
		} stonecutter;
		struct {
			mc_proto_69_SlotDisplay template;
			mc_proto_69_SlotDisplay base;
			mc_proto_69_SlotDisplay addition;
			mc_proto_69_SlotDisplay result;
			mc_proto_69_SlotDisplay craftingStation;
		} smithing;
	} data;
} mc_proto_69_RecipeDisplay;
typedef enum {
	mc_proto_69_SlotComponentType_custom_data = 0,
	mc_proto_69_SlotComponentType_max_stack_size = 1,
	mc_proto_69_SlotComponentType_max_damage = 2,
	mc_proto_69_SlotComponentType_damage = 3,
	mc_proto_69_SlotComponentType_unbreakable = 4,
	mc_proto_69_SlotComponentType_custom_name = 5,
	mc_proto_69_SlotComponentType_item_name = 6,
	mc_proto_69_SlotComponentType_item_model = 7,
	mc_proto_69_SlotComponentType_lore = 8,
	mc_proto_69_SlotComponentType_rarity = 9,
	mc_proto_69_SlotComponentType_enchantments = 10,
	mc_proto_69_SlotComponentType_can_place_on = 11,
	mc_proto_69_SlotComponentType_can_break = 12,
	mc_proto_69_SlotComponentType_attribute_modifiers = 13,
	mc_proto_69_SlotComponentType_custom_model_data = 14,
	mc_proto_69_SlotComponentType_hide_additional_tooltip = 15,
	mc_proto_69_SlotComponentType_hide_tooltip = 16,
	mc_proto_69_SlotComponentType_repair_cost = 17,
	mc_proto_69_SlotComponentType_creative_slot_lock = 18,
	mc_proto_69_SlotComponentType_enchantment_glint_override = 19,
	mc_proto_69_SlotComponentType_intangible_projectile = 20,
	mc_proto_69_SlotComponentType_food = 21,
	mc_proto_69_SlotComponentType_consumable = 22,
	mc_proto_69_SlotComponentType_use_remainder = 23,
	mc_proto_69_SlotComponentType_use_cooldown = 24,
	mc_proto_69_SlotComponentType_damage_resistant = 25,
	mc_proto_69_SlotComponentType_tool = 26,
	mc_proto_69_SlotComponentType_enchantable = 27,
	mc_proto_69_SlotComponentType_equippable = 28,
	mc_proto_69_SlotComponentType_repairable = 29,
	mc_proto_69_SlotComponentType_glider = 30,
	mc_proto_69_SlotComponentType_tooltip_style = 31,
	mc_proto_69_SlotComponentType_death_protection = 32,
	mc_proto_69_SlotComponentType_stored_enchantments = 33,
	mc_proto_69_SlotComponentType_dyed_color = 34,
	mc_proto_69_SlotComponentType_map_color = 35,
	mc_proto_69_SlotComponentType_map_id = 36,
	mc_proto_69_SlotComponentType_map_decorations = 37,
	mc_proto_69_SlotComponentType_map_post_processing = 38,
	mc_proto_69_SlotComponentType_charged_projectiles = 39,
	mc_proto_69_SlotComponentType_bundle_contents = 40,
	mc_proto_69_SlotComponentType_potion_contents = 41,
	mc_proto_69_SlotComponentType_suspicious_stew_effects = 42,
	mc_proto_69_SlotComponentType_writable_book_content = 43,
	mc_proto_69_SlotComponentType_written_book_content = 44,
	mc_proto_69_SlotComponentType_trim = 45,
	mc_proto_69_SlotComponentType_debug_stick_state = 46,
	mc_proto_69_SlotComponentType_entity_data = 47,
	mc_proto_69_SlotComponentType_bucket_entity_data = 48,
	mc_proto_69_SlotComponentType_block_entity_data = 49,
	mc_proto_69_SlotComponentType_instrument = 50,
	mc_proto_69_SlotComponentType_ominous_bottle_amplifier = 51,
	mc_proto_69_SlotComponentType_jukebox_playable = 52,
	mc_proto_69_SlotComponentType_recipes = 53,
	mc_proto_69_SlotComponentType_lodestone_tracker = 54,
	mc_proto_69_SlotComponentType_firework_explosion = 55,
	mc_proto_69_SlotComponentType_fireworks = 56,
	mc_proto_69_SlotComponentType_profile = 57,
	mc_proto_69_SlotComponentType_note_block_sound = 58,
	mc_proto_69_SlotComponentType_banner_patterns = 59,
	mc_proto_69_SlotComponentType_base_color = 60,
	mc_proto_69_SlotComponentType_pot_decorations = 61,
	mc_proto_69_SlotComponentType_container = 62,
	mc_proto_69_SlotComponentType_block_state = 63,
	mc_proto_69_SlotComponentType_bees = 64,
	mc_proto_69_SlotComponentType_lock = 65,
	mc_proto_69_SlotComponentType_container_loot = 66,
} mc_proto_69_SlotComponentType;

typedef struct {
	mc_proto_69_SlotComponentType type;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		mc_proto_varint max_stack_size;
		mc_proto_varint max_damage;
		mc_proto_varint damage;
		bool unbreakable;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		mc_proto_69_string item_model;
		struct {
			mc_proto_varint count;
  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonOptionalNbt/structline.j2 */ } lore;
  enum {
	  mc_proto_69_SlotComponent_rarity_common = 0,
	  mc_proto_69_SlotComponent_rarity_uncommon = 1,
	  mc_proto_69_SlotComponent_rarity_rare = 2,
	  mc_proto_69_SlotComponent_rarity_epic = 3,
  } rarity;
  struct {
	  struct {
		  mc_proto_varint count;
		  struct {
			  mc_proto_varint id;
			  mc_proto_varint level;
		  } data[];
	  } enchantments;
	  bool showTooltip;
  } enchantments;
  struct {
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_BlockPredicate data[];
	  } predicates;
	  bool showTooltip;
  } can_place_on;
  struct {
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_BlockPredicate data[];
	  } predicates;
	  bool showTooltip;
  } can_break;
  struct {
	  struct {
		  mc_proto_varint count;
		  struct {
			  mc_proto_varint typeId;
			  mc_proto_69_string name;
			  double value;
			  enum {
				  mc_proto_69_SlotComponent_operation_add = 0,
				  mc_proto_69_SlotComponent_operation_multiply_base = 1,
				  mc_proto_69_SlotComponent_operation_multiply_total = 2,
			  } operation;
			  enum {
				  mc_proto_69_SlotComponent_slot_any = 0,
				  mc_proto_69_SlotComponent_slot_main_hand = 1,
				  mc_proto_69_SlotComponent_slot_off_hand = 2,
				  mc_proto_69_SlotComponent_slot_hand = 3,
				  mc_proto_69_SlotComponent_slot_feet = 4,
				  mc_proto_69_SlotComponent_slot_legs = 5,
				  mc_proto_69_SlotComponent_slot_chest = 6,
				  mc_proto_69_SlotComponent_slot_head = 7,
				  mc_proto_69_SlotComponent_slot_armor = 8,
				  mc_proto_69_SlotComponent_slot_body = 9,
			  } slot;
		  } data[];
	  } attributes;
	  bool showTooltip;
  } attribute_modifiers;
  mc_proto_varint custom_model_data;
  /* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
  /* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
  mc_proto_varint repair_cost;
  /* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
  bool enchantment_glint_override;
  /* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
  struct {
	  mc_proto_varint nutrition;
	  float saturationModifier;
	  bool canAlwaysEat;
  } food;
  struct {
	  float consume_seconds;
	  enum {
		  mc_proto_69_SlotComponent_animation_none = 0,
		  mc_proto_69_SlotComponent_animation_eat = 1,
		  mc_proto_69_SlotComponent_animation_drink = 2,
		  mc_proto_69_SlotComponent_animation_block = 3,
		  mc_proto_69_SlotComponent_animation_bow = 4,
		  mc_proto_69_SlotComponent_animation_spear = 5,
		  mc_proto_69_SlotComponent_animation_crossbow = 6,
		  mc_proto_69_SlotComponent_animation_spyglass = 7,
		  mc_proto_69_SlotComponent_animation_toot_horn = 8,
		  mc_proto_69_SlotComponent_animation_brush = 9,
	  } animation;
	  /* <class 'jinja2.exceptions.TemplateNotFound'>: registryEntryHolder/structline.j2 */
	  bool makes_particles;
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_ConsumeEffect data[];
	  } effects;
  } consumable;
  mc_proto_69_Slot use_remainder;
  struct {
	  float seconds;
	  struct {
		  bool present;
		  mc_proto_69_string data;
	  } cooldownGroup;
  } use_cooldown;
  mc_proto_69_string damage_resistant;
  struct {
	  struct {
		  mc_proto_varint count;
		  struct {
			  mc_proto_69_IDSet blocks;
			  struct {
				  bool present;
				  float data;
			  } speed;
			  struct {
				  bool present;
				  bool data;
			  } correctDropForBlocks;
		  } data[];
	  } rules;
	  float defaultMiningSpeed;
	  mc_proto_varint damagePerBlock;
  } tool;
  mc_proto_varint enchantable;
  struct {
	  enum {
		  mc_proto_69_SlotComponent_slot_main_hand = 0,
		  mc_proto_69_SlotComponent_slot_off_hand = 1,
		  mc_proto_69_SlotComponent_slot_feet = 2,
		  mc_proto_69_SlotComponent_slot_legs = 3,
		  mc_proto_69_SlotComponent_slot_chest = 4,
		  mc_proto_69_SlotComponent_slot_head = 5,
		  mc_proto_69_SlotComponent_slot_body = 6,
	  } slot;
	  /* <class 'jinja2.exceptions.TemplateNotFound'>: registryEntryHolder/structline.j2 */
	  struct {
		  bool present;
		  mc_proto_69_string data;
	  } model;
	  struct {
		  bool present;
		  mc_proto_69_string data;
	  } cameraOverlay;
	  struct {
		  bool present;
		  mc_proto_69_IDSet data;
	  } allowedEntities;
	  bool dispensable;
	  bool swappable;
	  bool damageable;
  } equippable;
  struct {
	  mc_proto_69_IDSet items;
  } repairable;
  mc_proto_69_string tooltip_style;
  struct {
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_ConsumeEffect data[];
	  } effects;
  } death_protection;
  struct {
	  struct {
		  mc_proto_varint count;
		  struct {
			  mc_proto_varint id;
			  mc_proto_varint level;
		  } data[];
	  } enchantments;
	  bool showInTooltip;
  } stored_enchantments;
  struct {
	  mc_proto_varint color;
	  bool showTooltip;
  } dyed_color;
  mc_proto_varint map_color;
  mc_proto_varint map_id;
  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonOptionalNbt/structline.j2 */
  mc_proto_varint map_post_processing;
  struct {
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_Slot data[];
	  } projectiles;
  } charged_projectiles;
  struct {
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_Slot data[];
	  } contents;
  } bundle_contents;
  struct {
	  struct {
		  bool present;
		  mc_proto_varint data;
	  } potionId;
	  struct {
		  bool present;
		  mc_proto_varint data;
	  } customColor;
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_PotionEffect data[];
	  } customEffects;
	  mc_proto_69_string customName;
  } potion_contents;
  struct {
	  struct {
		  mc_proto_varint count;
		  struct {
			  mc_proto_varint effect;
			  mc_proto_varint duration;
		  } data[];
	  } effects;
  } suspicious_stew_effects;
  struct {
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_BookPage data[];
	  } pages;
  } writable_book_content;
  struct {
	  mc_proto_69_string rawTitle;
	  struct {
		  bool present;
		  mc_proto_69_string data;
	  } filteredTitle;
	  mc_proto_69_string author;
	  mc_proto_varint generation;
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_BookPage data[];
	  } pages;
	  bool resolved;
  } written_book_content;
  struct {
	  mc_proto_varint materialType;
	  union {
		  struct {
			  mc_proto_69_string assetName;
			  mc_proto_varint ingredientId;
			  float itemModelIndex;
			  mc_proto_69_optvarint numberOfOverrides;
			  struct {
				  mc_proto_varint count;
				  struct {
					  mc_proto_varint armorMaterialType;
					  mc_proto_69_string overridenAssetName;
				  } data[];
			  } override;
			  mc_proto_69_string description;
		  } 0;
	  };
	  mc_proto_varint trimPatternType;
	  union {
		  struct {
			  mc_proto_69_string assetName;
			  mc_proto_varint templateItem;
			  mc_proto_69_string description;
			  bool decal;
		  } 0;
	  };
	  bool showInTooltip;
  } trim;
  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
  struct {
	  mc_proto_varint instrumentType;
	  union {
		  struct {
			  mc_proto_69_string soundEvent;
			  float useDuration;
			  float range;
		  } 0;
	  };
  } instrument;
  mc_proto_varint ominous_bottle_amplifier;
  struct {
	  bool directMode;
	  union {
		  struct {
			  mc_proto_69_string jukeboxSongName;
			  mc_proto_varint jukeboxSongType;
			  union {
				  struct {
					  struct {
						  mc_proto_varint soundEventType;
						  union {
							  struct {
								  mc_proto_69_string soundName;
								  struct {
									  bool present;
									  float data;
								  } fixedRange;
							  } 0;
						  };
					  } soundEvent;
				  } 0;
			  };
			  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
			  float duration;
			  mc_proto_varint output;
		  } true;
		  struct {
			  mc_proto_69_string songLocation;
		  } false;
	  };
	  bool showInTooltip;
  } jukebox_playable;
  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
  struct {
	  struct {
		  bool present;
		  struct {
			  mc_proto_69_string dimension;
			  mc_proto_69_position position;
		  } data;
	  } globalPosition;
	  bool tracked;
  } lodestone_tracker;
  mc_proto_69_FireworkExplosion firework_explosion;
  struct {
	  mc_proto_varint flightDuration;
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_FireworkExplosion data[];
	  } explosions;
  } fireworks;
  struct {
	  bool hasName;
	  mc_proto_69_string name;
	  bool hasUniqueId;
	  /* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
	  struct {
		  mc_proto_varint count;
		  struct {
			  mc_proto_69_string property;
			  mc_proto_69_string value;
			  bool hasSignature;
			  mc_proto_69_string signature;
		  } data[];
	  } properties;
  } profile;
  mc_proto_69_string note_block_sound;
  struct {
	  struct {
		  mc_proto_varint count;
		  struct {
			  mc_proto_varint patternType;
			  union {
				  struct {
					  mc_proto_69_string assetId;
					  mc_proto_69_string translationKey;
				  } 0;
			  };
			  mc_proto_varint color;
		  } data[];
	  } layers;
  } banner_patterns;
  mc_proto_varint base_color;
  struct {
	  struct {
		  mc_proto_varint count;
		  mc_proto_varint data[];
	  } decorations;
  } pot_decorations;
  struct {
	  struct {
		  mc_proto_varint count;
		  mc_proto_69_Slot data[];
	  } contents;
  } container;
  struct {
	  struct {
		  mc_proto_varint count;
		  struct {
			  mc_proto_69_string property;
			  mc_proto_69_string value;
		  } data[];
	  } properties;
  } block_state;
  struct {
	  struct {
		  mc_proto_varint count;
		  struct {
			  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
			  mc_proto_varint ticksInHive;
			  mc_proto_varint minTicksInHive;
		  } data[];
	  } bees;
  } bees;
  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
  /* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} data;
} mc_proto_69_SlotComponent;

typedef struct {
	mc_proto_varint itemCount;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
	};
} mc_proto_69_Slot;

typedef struct {
	enum {
		mc_proto_69_FireworkExplosion_shape_small_ball = 0,
		mc_proto_69_FireworkExplosion_shape_large_ball = 1,
		mc_proto_69_FireworkExplosion_shape_star = 2,
		mc_proto_69_FireworkExplosion_shape_creeper = 3,
		mc_proto_69_FireworkExplosion_shape_burst = 4,
	} shape;
	struct {
		mc_proto_varint count;
		int32_t data[];
	} colors;
	struct {
		mc_proto_varint count;
		int32_t data[];
	} fadeColors;
	bool hasTrail;
	bool hasTwinkle;
} mc_proto_69_FireworkExplosion;

typedef struct {
	mc_proto_69_string content;
	struct {
		bool present;
		mc_proto_69_string data;
	} filteredContent;
} mc_proto_69_BookPage;

typedef struct {
	mc_proto_varint amplifier;
	mc_proto_varint duration;
	bool ambient;
	bool showParticles;
	bool showIcon;
	struct {
		bool present;
		mc_proto_69_EffectDetail data;
	} hiddenEffect;
} mc_proto_69_EffectDetail;

typedef struct {
	mc_proto_varint id;
	mc_proto_69_EffectDetail details;
} mc_proto_69_PotionEffect;

typedef struct {
	enum {
		mc_proto_69_ConsumeEffect_type_apply_effects = 0,
		mc_proto_69_ConsumeEffect_type_remove_effects = 1,
		mc_proto_69_ConsumeEffect_type_clear_all_effects = 2,
		mc_proto_69_ConsumeEffect_type_teleport_randomly = 3,
		mc_proto_69_ConsumeEffect_type_play_sound = 4,
	} type;
	union {
		struct {
			struct {
				mc_proto_varint count;
				mc_proto_69_PotionEffect data[];
			} effects;
			float probability;
		} apply_effects;
		struct {
			mc_proto_69_IDSet effects;
		} remove_effects;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
		struct {
			float diameter;
		} teleport_randomly;
		struct {
			/* <class 'jinja2.exceptions.TemplateNotFound'>: registryEntryHolder/structline.j2 */
		} play_sound;
	};
} mc_proto_69_ConsumeEffect;

typedef struct {
	mc_proto_69_string name;
	bool isExactMatch;
	struct {
		bool present;
		mc_proto_69_string data;
	} exactValue;
	struct {
		bool present;
		mc_proto_69_string data;
	} minValue;
	struct {
		bool present;
		mc_proto_69_string data;
	} maxValue;
} mc_proto_69_BlockProperty;

typedef struct {
	struct {
		bool present;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: registryEntryHolderSet/structline.j2 */
	} blockSet;
	struct {
		bool present;
		struct {
			mc_proto_varint count;
			mc_proto_69_BlockProperty data[];
		} data;
	} properties;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonOptionalNbt/structline.j2 */
} mc_proto_69_BlockPredicate;

typedef struct {
	enum {
		mc_proto_69_Particle_type_angry_villager = 0,
		mc_proto_69_Particle_type_block = 1,
		mc_proto_69_Particle_type_block_marker = 2,
		mc_proto_69_Particle_type_bubble = 3,
		mc_proto_69_Particle_type_cloud = 4,
		mc_proto_69_Particle_type_crit = 5,
		mc_proto_69_Particle_type_damage_indicator = 6,
		mc_proto_69_Particle_type_dragon_breath = 7,
		mc_proto_69_Particle_type_dripping_lava = 8,
		mc_proto_69_Particle_type_falling_lava = 9,
		mc_proto_69_Particle_type_landing_lava = 10,
		mc_proto_69_Particle_type_dripping_water = 11,
		mc_proto_69_Particle_type_falling_water = 12,
		mc_proto_69_Particle_type_dust = 13,
		mc_proto_69_Particle_type_dust_color_transition = 14,
		mc_proto_69_Particle_type_effect = 15,
		mc_proto_69_Particle_type_elder_guardian = 16,
		mc_proto_69_Particle_type_enchanted_hit = 17,
		mc_proto_69_Particle_type_enchant = 18,
		mc_proto_69_Particle_type_end_rod = 19,
		mc_proto_69_Particle_type_entity_effect = 20,
		mc_proto_69_Particle_type_explosion_emitter = 21,
		mc_proto_69_Particle_type_explosion = 22,
		mc_proto_69_Particle_type_gust = 23,
		mc_proto_69_Particle_type_small_gust = 24,
		mc_proto_69_Particle_type_gust_emitter_large = 25,
		mc_proto_69_Particle_type_gust_emitter_small = 26,
		mc_proto_69_Particle_type_sonic_boom = 27,
		mc_proto_69_Particle_type_falling_dust = 28,
		mc_proto_69_Particle_type_firework = 29,
		mc_proto_69_Particle_type_fishing = 30,
		mc_proto_69_Particle_type_flame = 31,
		mc_proto_69_Particle_type_infested = 32,
		mc_proto_69_Particle_type_cherry_leaves = 33,
		mc_proto_69_Particle_type_sculk_soul = 34,
		mc_proto_69_Particle_type_sculk_charge = 35,
		mc_proto_69_Particle_type_sculk_charge_pop = 36,
		mc_proto_69_Particle_type_soul_fire_flame = 37,
		mc_proto_69_Particle_type_soul = 38,
		mc_proto_69_Particle_type_flash = 39,
		mc_proto_69_Particle_type_happy_villager = 40,
		mc_proto_69_Particle_type_composter = 41,
		mc_proto_69_Particle_type_heart = 42,
		mc_proto_69_Particle_type_instant_effect = 43,
		mc_proto_69_Particle_type_item = 44,
		mc_proto_69_Particle_type_vibration = 45,
		mc_proto_69_Particle_type_trail = 46,
		mc_proto_69_Particle_type_item_slime = 47,
		mc_proto_69_Particle_type_item_cobweb = 48,
		mc_proto_69_Particle_type_item_snowball = 49,
		mc_proto_69_Particle_type_large_smoke = 50,
		mc_proto_69_Particle_type_lava = 51,
		mc_proto_69_Particle_type_mycelium = 52,
		mc_proto_69_Particle_type_note = 53,
		mc_proto_69_Particle_type_poof = 54,
		mc_proto_69_Particle_type_portal = 55,
		mc_proto_69_Particle_type_rain = 56,
		mc_proto_69_Particle_type_smoke = 57,
		mc_proto_69_Particle_type_white_smoke = 58,
		mc_proto_69_Particle_type_sneeze = 59,
		mc_proto_69_Particle_type_spit = 60,
		mc_proto_69_Particle_type_squid_ink = 61,
		mc_proto_69_Particle_type_sweep_attack = 62,
		mc_proto_69_Particle_type_totem_of_undying = 63,
		mc_proto_69_Particle_type_underwater = 64,
		mc_proto_69_Particle_type_splash = 65,
		mc_proto_69_Particle_type_witch = 66,
		mc_proto_69_Particle_type_bubble_pop = 67,
		mc_proto_69_Particle_type_current_down = 68,
		mc_proto_69_Particle_type_bubble_column_up = 69,
		mc_proto_69_Particle_type_nautilus = 70,
		mc_proto_69_Particle_type_dolphin = 71,
		mc_proto_69_Particle_type_campfire_cosy_smoke = 72,
		mc_proto_69_Particle_type_campfire_signal_smoke = 73,
		mc_proto_69_Particle_type_dripping_honey = 74,
		mc_proto_69_Particle_type_falling_honey = 75,
		mc_proto_69_Particle_type_landing_honey = 76,
		mc_proto_69_Particle_type_falling_nectar = 77,
		mc_proto_69_Particle_type_falling_spore_blossom = 78,
		mc_proto_69_Particle_type_ash = 79,
		mc_proto_69_Particle_type_crimson_spore = 80,
		mc_proto_69_Particle_type_warped_spore = 81,
		mc_proto_69_Particle_type_spore_blossom_air = 82,
		mc_proto_69_Particle_type_dripping_obsidian_tear = 83,
		mc_proto_69_Particle_type_falling_obsidian_tear = 84,
		mc_proto_69_Particle_type_landing_obsidian_tear = 85,
		mc_proto_69_Particle_type_reverse_portal = 86,
		mc_proto_69_Particle_type_white_ash = 87,
		mc_proto_69_Particle_type_small_flame = 88,
		mc_proto_69_Particle_type_snowflake = 89,
		mc_proto_69_Particle_type_dripping_dripstone_lava = 90,
		mc_proto_69_Particle_type_falling_dripstone_lava = 91,
		mc_proto_69_Particle_type_dripping_dripstone_water = 92,
		mc_proto_69_Particle_type_falling_dripstone_water = 93,
		mc_proto_69_Particle_type_glow_squid_ink = 94,
		mc_proto_69_Particle_type_glow = 95,
		mc_proto_69_Particle_type_wax_on = 96,
		mc_proto_69_Particle_type_wax_off = 97,
		mc_proto_69_Particle_type_electric_spark = 98,
		mc_proto_69_Particle_type_scrape = 99,
		mc_proto_69_Particle_type_shriek = 100,
		mc_proto_69_Particle_type_egg_crack = 101,
		mc_proto_69_Particle_type_dust_plume = 102,
		mc_proto_69_Particle_type_trial_spawner_detected_player = 103,
		mc_proto_69_Particle_type_trial_spawner_detected_player_ominous = 104,
		mc_proto_69_Particle_type_vault_connection = 105,
		mc_proto_69_Particle_type_dust_pillar = 106,
		mc_proto_69_Particle_type_ominous_spawning = 107,
		mc_proto_69_Particle_type_raid_omen = 108,
		mc_proto_69_Particle_type_trial_omen = 109,
		mc_proto_69_Particle_type_block_crumble = 110,
	} type;
	union {
		mc_proto_varint block;
		mc_proto_varint block_marker;
		mc_proto_varint falling_dust;
		mc_proto_varint dust_pillar;
		mc_proto_varint block_crumble;
		struct {
			float red;
			float green;
			float blue;
			float scale;
		} dust;
		struct {
			float fromRed;
			float fromGreen;
			float fromBlue;
			float scale;
			float toRed;
			float toGreen;
			float toBlue;
		} dust_color_transition;
		int32_t entity_effect;
		mc_proto_69_Slot item;
		float sculk_charge;
		mc_proto_varint shriek;
		struct {
			enum {
				mc_proto_69_Particle_position_type_block = 0,
				mc_proto_69_Particle_position_type_entity = 1,
			} position_type;
			union {
				mc_proto_69_position block;
				struct {
					mc_proto_varint entityId;
					float entity_eye_height;
				} entity;
			} position;
			mc_proto_varint ticks;
		} vibration;
		struct {
			mc_proto_69_vec3f64 target;
			uint8_t color;
		} trail;
	} data;
} mc_proto_69_Particle;

typedef struct {
	mc_proto_varint count;
	mc_proto_69_Slot data[];
} mc_proto_69_ingredient;

typedef struct {
	int32_t x : 26;
	int32_t z : 26;
	int32_t y : 12;
} mc_proto_69_position;

typedef enum {
	mc_proto_69_soundSource_master = 0,
	mc_proto_69_soundSource_music = 1,
	mc_proto_69_soundSource_record = 2,
	mc_proto_69_soundSource_weather = 3,
	mc_proto_69_soundSource_block = 4,
	mc_proto_69_soundSource_hostile = 5,
	mc_proto_69_soundSource_neutral = 6,
	mc_proto_69_soundSource_player = 7,
	mc_proto_69_soundSource_ambient = 8,
	mc_proto_69_soundSource_voice = 9,
} mc_proto_69_soundSource;

typedef struct {
	int32_t z;
	int32_t x;
} mc_proto_69_packedChunkPos;

typedef struct {
	mc_proto_varint count;
	struct {
		mc_proto_varint id;
		union {
			uint8_t 0 [256];
		} signature;
	} data[];
} mc_proto_69_previousMessages;

typedef struct {
	uint8_t key;
	enum {
		mc_proto_69_entityMetadataEntry_type_byte = 0,
		mc_proto_69_entityMetadataEntry_type_int = 1,
		mc_proto_69_entityMetadataEntry_type_long = 2,
		mc_proto_69_entityMetadataEntry_type_float = 3,
		mc_proto_69_entityMetadataEntry_type_string = 4,
		mc_proto_69_entityMetadataEntry_type_component = 5,
		mc_proto_69_entityMetadataEntry_type_optional_component = 6,
		mc_proto_69_entityMetadataEntry_type_item_stack = 7,
		mc_proto_69_entityMetadataEntry_type_boolean = 8,
		mc_proto_69_entityMetadataEntry_type_rotations = 9,
		mc_proto_69_entityMetadataEntry_type_block_pos = 10,
		mc_proto_69_entityMetadataEntry_type_optional_block_pos = 11,
		mc_proto_69_entityMetadataEntry_type_direction = 12,
		mc_proto_69_entityMetadataEntry_type_optional_uuid = 13,
		mc_proto_69_entityMetadataEntry_type_block_state = 14,
		mc_proto_69_entityMetadataEntry_type_optional_block_state = 15,
		mc_proto_69_entityMetadataEntry_type_compound_tag = 16,
		mc_proto_69_entityMetadataEntry_type_particle = 17,
		mc_proto_69_entityMetadataEntry_type_particles = 18,
		mc_proto_69_entityMetadataEntry_type_villager_data = 19,
		mc_proto_69_entityMetadataEntry_type_optional_unsigned_int = 20,
		mc_proto_69_entityMetadataEntry_type_pose = 21,
		mc_proto_69_entityMetadataEntry_type_cat_variant = 22,
		mc_proto_69_entityMetadataEntry_type_wolf_variant = 23,
		mc_proto_69_entityMetadataEntry_type_frog_variant = 24,
		mc_proto_69_entityMetadataEntry_type_optional_global_pos = 25,
		mc_proto_69_entityMetadataEntry_type_painting_variant = 26,
		mc_proto_69_entityMetadataEntry_type_sniffer_state = 27,
		mc_proto_69_entityMetadataEntry_type_armadillo_state = 28,
		mc_proto_69_entityMetadataEntry_type_vector3 = 29,
		mc_proto_69_entityMetadataEntry_type_quaternion = 30,
	} type;
	union {
		int8_t byte;
		mc_proto_varint int;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: varlong/structline.j2 */
		float float;
		mc_proto_69_string string;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		struct {
			bool present;
			/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		} optional_component;
		mc_proto_69_Slot item_stack;
		bool boolean;
		struct {
			float pitch;
			float yaw;
			float roll;
		} rotations;
		mc_proto_69_position block_pos;
		struct {
			bool present;
			mc_proto_69_position data;
		} optional_block_pos;
		mc_proto_varint direction;
		struct {
			bool present;
			/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
		} optional_uuid;
		mc_proto_varint block_state;
		mc_proto_69_optvarint optional_block_state;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		mc_proto_69_Particle particle;
		struct {
			mc_proto_varint count;
			mc_proto_69_Particle data[];
		} particles;
		struct {
			mc_proto_varint villagerType;
			mc_proto_varint villagerProfession;
			mc_proto_varint level;
		} villager_data;
		mc_proto_69_optvarint optional_unsigned_int;
		mc_proto_varint pose;
		mc_proto_varint cat_variant;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: registryEntryHolder/structline.j2 */
		mc_proto_varint frog_variant;
		struct {
			bool present;
			mc_proto_69_string data;
		} optional_global_pos;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: registryEntryHolder/structline.j2 */
		mc_proto_varint sniffer_state;
		mc_proto_varint armadillo_state;
		mc_proto_69_vec3f vector3;
		mc_proto_69_vec4f quaternion;
	} value;
} mc_proto_69_entityMetadataEntry;

typedef struct {
	int32_t width;
	int32_t height;
	mc_proto_69_string assetId;
	struct {
		bool present;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} title;
	struct {
		bool present;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} author;
} mc_proto_69_EntityMetadataPaintingVariant;

typedef struct {
	mc_proto_69_string wildTexture;
	mc_proto_69_string tameTexture;
	mc_proto_69_string angryTexture;
	mc_proto_69_IDSet biome;
} mc_proto_69_EntityMetadataWolfVariant;

typedef /* <class 'jinja2.exceptions.TemplateNotFound'>: entityMetadataLoop/structline.j2 */

	typedef struct {
	mc_proto_varint count;
	struct {
		mc_proto_69_string tagName;
		struct {
			mc_proto_varint count;
			mc_proto_varint data[];
		} entries;
	} data[];
} mc_proto_69_tags;

typedef struct {
	struct {
		uint32_t x : 4;
		uint32_t z : 4;
	};
	int16_t y;
	mc_proto_varint type;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonOptionalNbt/structline.j2 */
} mc_proto_69_chunkBlockEntity;

typedef struct {
	bool present;
	struct {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
		struct {
			int64_t expireTime;
			struct {
				uint8_t *data;
				mc_proto_varint len;
			} keyBytes;
			struct {
				uint8_t *data;
				mc_proto_varint len;
			} keySignature;
		} publicKey;
	} data;
} mc_proto_69_chat_session;

typedef struct {
	mc_proto_69_string name;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string key;
			mc_proto_69_string value;
			struct {
				bool present;
				mc_proto_69_string data;
			} signature;
		} data[];
	} properties;
} mc_proto_69_game_profile;

typedef struct {
	struct {
		uint32_t unused : 3;
		uint32_t has_custom_suggestions : 1;
		uint32_t has_redirect_node : 1;
		uint32_t has_command : 1;
		uint32_t command_node_type : 2;
	} flags;
	struct {
		mc_proto_varint count;
		mc_proto_varint data[];
	} children;
	union {
		mc_proto_varint 1;
	} redirectNode;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
		struct {
			mc_proto_69_string name;
		} 1;
		struct {
			mc_proto_69_string name;
			enum {
				mc_proto_69_command_node_parser_brigadier : bool = 0,
				mc_proto_69_command_node_parser_brigadier : float = 1,
				mc_proto_69_command_node_parser_brigadier : double = 2,
				mc_proto_69_command_node_parser_brigadier : integer = 3,
				mc_proto_69_command_node_parser_brigadier : long = 4,
				mc_proto_69_command_node_parser_brigadier : string = 5,
				mc_proto_69_command_node_parser_minecraft : entity = 6,
				mc_proto_69_command_node_parser_minecraft : game_profile = 7,
				mc_proto_69_command_node_parser_minecraft : block_pos = 8,
				mc_proto_69_command_node_parser_minecraft : column_pos = 9,
				mc_proto_69_command_node_parser_minecraft : vec3 = 10,
				mc_proto_69_command_node_parser_minecraft : vec2 = 11,
				mc_proto_69_command_node_parser_minecraft : block_state = 12,
				mc_proto_69_command_node_parser_minecraft : block_predicate = 13,
				mc_proto_69_command_node_parser_minecraft : item_stack = 14,
				mc_proto_69_command_node_parser_minecraft : item_predicate = 15,
				mc_proto_69_command_node_parser_minecraft : color = 16,
				mc_proto_69_command_node_parser_minecraft : component = 17,
				mc_proto_69_command_node_parser_minecraft : style = 18,
				mc_proto_69_command_node_parser_minecraft : message = 19,
				mc_proto_69_command_node_parser_minecraft : nbt = 20,
				mc_proto_69_command_node_parser_minecraft : nbt_tag = 21,
				mc_proto_69_command_node_parser_minecraft : nbt_path = 22,
				mc_proto_69_command_node_parser_minecraft : objective = 23,
				mc_proto_69_command_node_parser_minecraft : objective_criteria = 24,
				mc_proto_69_command_node_parser_minecraft : operation = 25,
				mc_proto_69_command_node_parser_minecraft : particle = 26,
				mc_proto_69_command_node_parser_minecraft : angle = 27,
				mc_proto_69_command_node_parser_minecraft : rotation = 28,
				mc_proto_69_command_node_parser_minecraft : scoreboard_slot = 29,
				mc_proto_69_command_node_parser_minecraft : score_holder = 30,
				mc_proto_69_command_node_parser_minecraft : swizzle = 31,
				mc_proto_69_command_node_parser_minecraft : team = 32,
				mc_proto_69_command_node_parser_minecraft : item_slot = 33,
				mc_proto_69_command_node_parser_minecraft : item_slots = 34,
				mc_proto_69_command_node_parser_minecraft : resource_location = 35,
				mc_proto_69_command_node_parser_minecraft : function = 36,
				mc_proto_69_command_node_parser_minecraft : entity_anchor = 37,
				mc_proto_69_command_node_parser_minecraft : int_range = 38,
				mc_proto_69_command_node_parser_minecraft : float_range = 39,
				mc_proto_69_command_node_parser_minecraft : dimension = 40,
				mc_proto_69_command_node_parser_minecraft : gamemode = 41,
				mc_proto_69_command_node_parser_minecraft : time = 42,
				mc_proto_69_command_node_parser_minecraft : resource_or_tag = 43,
				mc_proto_69_command_node_parser_minecraft : resource_or_tag_key = 44,
				mc_proto_69_command_node_parser_minecraft : resource = 45,
				mc_proto_69_command_node_parser_minecraft : resource_key = 46,
				mc_proto_69_command_node_parser_minecraft : template_mirror = 47,
				mc_proto_69_command_node_parser_minecraft : template_rotation = 48,
				mc_proto_69_command_node_parser_minecraft : heightmap = 49,
				mc_proto_69_command_node_parser_minecraft : loot_table = 50,
				mc_proto_69_command_node_parser_minecraft : loot_predicate = 51,
				mc_proto_69_command_node_parser_minecraft : loot_modifier = 52,
				mc_proto_69_command_node_parser_minecraft : uuid = 53,
			} parser;
			union {
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				struct {
					struct {
						uint32_t unused : 6;
						uint32_t max_present : 1;
						uint32_t min_present : 1;
					} flags;
					union {
						float 1;
					} min;
					union {
						float 1;
					} max;
				} brigadier : float;
				struct {
					struct {
						uint32_t unused : 6;
						uint32_t max_present : 1;
						uint32_t min_present : 1;
					} flags;
					union {
						double 1;
					} min;
					union {
						double 1;
					} max;
				} brigadier : double;
				struct {
					struct {
						uint32_t unused : 6;
						uint32_t max_present : 1;
						uint32_t min_present : 1;
					} flags;
					union {
						int32_t 1;
					} min;
					union {
						int32_t 1;
					} max;
				} brigadier : integer;
				struct {
					struct {
						uint32_t unused : 6;
						uint32_t max_present : 1;
						uint32_t min_present : 1;
					} flags;
					union {
						int64_t 1;
					} min;
					union {
						int64_t 1;
					} max;
				} brigadier : long;
				enum {
					mc_proto_69_command_node_brigadier : string_SINGLE_WORD = 0,
					mc_proto_69_command_node_brigadier : string_QUOTABLE_PHRASE = 1,
					mc_proto_69_command_node_brigadier : string_GREEDY_PHRASE = 2,
				} brigadier : string;
				struct {
					uint32_t unused : 6;
					uint32_t onlyAllowPlayers : 1;
					uint32_t onlyAllowEntities : 1;
				} minecraft : entity;
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				struct {
					uint32_t unused : 7;
					uint32_t allowMultiple : 1;
				} minecraft : score_holder;
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				struct {
					int32_t min;
				} minecraft : time;
				struct {
					mc_proto_69_string registry;
				} minecraft : resource_or_tag;
				struct {
					mc_proto_69_string registry;
				} minecraft : resource_or_tag_key;
				struct {
					mc_proto_69_string registry;
				} minecraft : resource;
				struct {
					mc_proto_69_string registry;
				} minecraft : resource_key;
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
				/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
			} properties;
			union {
				mc_proto_69_string 1;
			} suggestionType;
		} 2;
	} extraNodeData;
} mc_proto_69_command_node;

typedef struct {
	mc_proto_69_string cookie;
} mc_proto_69_packet_common_cookie_request;

typedef struct {
	mc_proto_69_string key;
	mc_proto_69_ByteArray value;
} mc_proto_69_packet_common_store_cookie;

typedef struct {
	mc_proto_69_string host;
	mc_proto_varint port;
} mc_proto_69_packet_common_transfer;

typedef struct {
	mc_proto_69_string key;
	mc_proto_69_ByteArray value;
} mc_proto_69_packet_common_cookie_response;

typedef struct {
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string namespace;
			mc_proto_69_string id;
			mc_proto_69_string version;
		} data[];
	} packs;
} mc_proto_69_packet_common_select_known_packs;

typedef struct {
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string key;
			mc_proto_69_string value;
		} data[];
	} details;
} mc_proto_69_packet_common_custom_report_details;

typedef struct {
	struct {
		bool present;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
	} uuid;
} mc_proto_69_packet_common_remove_resource_pack;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
	mc_proto_69_string url;
	mc_proto_69_string hash;
	bool forced;
	struct {
		bool present;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} promptMessage;
} mc_proto_69_packet_common_add_resource_pack;

typedef enum {
	mc_proto_69_ServerLinkType_bug_report = 0,
	mc_proto_69_ServerLinkType_community_guidelines = 1,
	mc_proto_69_ServerLinkType_support = 2,
	mc_proto_69_ServerLinkType_status = 3,
	mc_proto_69_ServerLinkType_feedback = 4,
	mc_proto_69_ServerLinkType_community = 5,
	mc_proto_69_ServerLinkType_website = 6,
	mc_proto_69_ServerLinkType_forums = 7,
	mc_proto_69_ServerLinkType_news = 8,
	mc_proto_69_ServerLinkType_announcements = 9,
} mc_proto_69_ServerLinkType;

typedef struct {
	struct {
		mc_proto_varint count;
		struct {
			bool hasKnownType;
			union {
				mc_proto_69_ServerLinkType true;
			} knownType;
			union {
				/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
			} unknownType;
			mc_proto_69_string link;
		} data[];
	} links;
} mc_proto_69_packet_common_server_links;

typedef struct {
	enum {} name;
	union {
	} params;
} mc_proto_69_handshaking_toClient_packet;

typedef struct {
	mc_proto_varint protocolVersion;
	mc_proto_69_string serverHost;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: u16/structline.j2 */
	mc_proto_varint nextState;
} mc_proto_69_handshaking_toServer_packet_set_protocol;

typedef struct {
	uint8_t payload;
} mc_proto_69_handshaking_toServer_packet_legacy_server_list_ping;

typedef struct {
	enum {
		mc_proto_69_handshaking_toServer_packet_name_set_protocol = 0x00,
		mc_proto_69_handshaking_toServer_packet_name_legacy_server_list_ping = 0xfe,
	} name;
	union {
		mc_proto_69_packet_set_protocol set_protocol;
		mc_proto_69_packet_legacy_server_list_ping legacy_server_list_ping;
	} params;
} mc_proto_69_handshaking_toServer_packet;

typedef struct {
	mc_proto_69_string response;
} mc_proto_69_status_toClient_packet_server_info;

typedef struct {
	int64_t time;
} mc_proto_69_status_toClient_packet_ping;

typedef struct {
	enum {
		mc_proto_69_status_toClient_packet_name_server_info = 0x00,
		mc_proto_69_status_toClient_packet_name_ping = 0x01,
	} name;
	union {
		mc_proto_69_packet_server_info server_info;
		mc_proto_69_packet_ping ping;
	} params;
} mc_proto_69_status_toClient_packet;

typedef struct {
} mc_proto_69_status_toServer_packet_ping_start;

typedef struct {
	int64_t time;
} mc_proto_69_status_toServer_packet_ping;

typedef struct {
	enum {
		mc_proto_69_status_toServer_packet_name_ping_start = 0x00,
		mc_proto_69_status_toServer_packet_name_ping = 0x01,
	} name;
	union {
		mc_proto_69_packet_ping_start ping_start;
		mc_proto_69_packet_ping ping;
	} params;
} mc_proto_69_status_toServer_packet;

typedef struct {
	mc_proto_69_string reason;
} mc_proto_69_login_toClient_packet_disconnect;

typedef struct {
	mc_proto_69_string serverId;
	struct {
		uint8_t *data;
		mc_proto_varint len;
	} publicKey;
	struct {
		uint8_t *data;
		mc_proto_varint len;
	} verifyToken;
	bool shouldAuthenticate;
} mc_proto_69_login_toClient_packet_encryption_begin;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
	mc_proto_69_string username;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string name;
			mc_proto_69_string value;
			struct {
				bool present;
				mc_proto_69_string data;
			} signature;
		} data[];
	} properties;
} mc_proto_69_login_toClient_packet_success;

typedef struct {
	mc_proto_varint threshold;
} mc_proto_69_login_toClient_packet_compress;

typedef struct {
	mc_proto_varint messageId;
	mc_proto_69_string channel;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: restBuffer/structline.j2 */
} mc_proto_69_login_toClient_packet_login_plugin_request;

typedef struct {
	enum {
		mc_proto_69_login_toClient_packet_name_disconnect = 0x00,
		mc_proto_69_login_toClient_packet_name_encryption_begin = 0x01,
		mc_proto_69_login_toClient_packet_name_success = 0x02,
		mc_proto_69_login_toClient_packet_name_compress = 0x03,
		mc_proto_69_login_toClient_packet_name_login_plugin_request = 0x04,
		mc_proto_69_login_toClient_packet_name_cookie_request = 0x05,
	} name;
	union {
		mc_proto_69_packet_disconnect disconnect;
		mc_proto_69_packet_encryption_begin encryption_begin;
		mc_proto_69_packet_success success;
		mc_proto_69_packet_compress compress;
		mc_proto_69_packet_login_plugin_request login_plugin_request;
		mc_proto_69_packet_common_cookie_request cookie_request;
	} params;
} mc_proto_69_login_toClient_packet;

typedef struct {
	mc_proto_69_string username;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
} mc_proto_69_login_toServer_packet_login_start;

typedef struct {
	struct {
		uint8_t *data;
		mc_proto_varint len;
	} sharedSecret;
	struct {
		uint8_t *data;
		mc_proto_varint len;
	} verifyToken;
} mc_proto_69_login_toServer_packet_encryption_begin;

typedef struct {
	mc_proto_varint messageId;
	struct {
		bool present;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: restBuffer/structline.j2 */
	} data;
} mc_proto_69_login_toServer_packet_login_plugin_response;

typedef struct {
} mc_proto_69_login_toServer_packet_login_acknowledged;

typedef struct {
	enum {
		mc_proto_69_login_toServer_packet_name_login_start = 0x00,
		mc_proto_69_login_toServer_packet_name_encryption_begin = 0x01,
		mc_proto_69_login_toServer_packet_name_login_plugin_response = 0x02,
		mc_proto_69_login_toServer_packet_name_login_acknowledged = 0x03,
		mc_proto_69_login_toServer_packet_name_cookie_response = 0x04,
	} name;
	union {
		mc_proto_69_packet_login_start login_start;
		mc_proto_69_packet_encryption_begin encryption_begin;
		mc_proto_69_packet_login_plugin_response login_plugin_response;
		mc_proto_69_packet_login_acknowledged login_acknowledged;
		mc_proto_69_packet_common_cookie_response cookie_response;
	} params;
} mc_proto_69_login_toServer_packet;

typedef struct {
	mc_proto_69_string channel;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: restBuffer/structline.j2 */
} mc_proto_69_configuration_toClient_packet_custom_payload;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
} mc_proto_69_configuration_toClient_packet_disconnect;

typedef struct {
} mc_proto_69_configuration_toClient_packet_finish_configuration;

typedef struct {
	int64_t keepAliveId;
} mc_proto_69_configuration_toClient_packet_keep_alive;

typedef struct {
	int32_t id;
} mc_proto_69_configuration_toClient_packet_ping;

typedef struct {
} mc_proto_69_configuration_toClient_packet_reset_chat;

typedef struct {
	mc_proto_69_string id;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string key;
			struct {
				bool present;
				/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
			} value;
		} data[];
	} entries;
} mc_proto_69_configuration_toClient_packet_registry_data;

typedef struct {
	struct {
		mc_proto_varint count;
		mc_proto_69_string data[];
	} features;
} mc_proto_69_configuration_toClient_packet_feature_flags;

typedef struct {
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string tagType;
			mc_proto_69_tags tags;
		} data[];
	} tags;
} mc_proto_69_configuration_toClient_packet_tags;

typedef struct {
	enum {
		mc_proto_69_configuration_toClient_packet_name_cookie_request = 0x00,
		mc_proto_69_configuration_toClient_packet_name_custom_payload = 0x01,
		mc_proto_69_configuration_toClient_packet_name_disconnect = 0x02,
		mc_proto_69_configuration_toClient_packet_name_finish_configuration = 0x03,
		mc_proto_69_configuration_toClient_packet_name_keep_alive = 0x04,
		mc_proto_69_configuration_toClient_packet_name_ping = 0x05,
		mc_proto_69_configuration_toClient_packet_name_reset_chat = 0x06,
		mc_proto_69_configuration_toClient_packet_name_registry_data = 0x07,
		mc_proto_69_configuration_toClient_packet_name_remove_resource_pack = 0x08,
		mc_proto_69_configuration_toClient_packet_name_add_resource_pack = 0x09,
		mc_proto_69_configuration_toClient_packet_name_store_cookie = 0x0a,
		mc_proto_69_configuration_toClient_packet_name_transfer = 0x0b,
		mc_proto_69_configuration_toClient_packet_name_feature_flags = 0x0c,
		mc_proto_69_configuration_toClient_packet_name_tags = 0x0d,
		mc_proto_69_configuration_toClient_packet_name_select_known_packs = 0x0e,
		mc_proto_69_configuration_toClient_packet_name_custom_report_details = 0x0f,
		mc_proto_69_configuration_toClient_packet_name_server_links = 0x10,
	} name;
	union {
		mc_proto_69_packet_common_cookie_request cookie_request;
		mc_proto_69_packet_custom_payload custom_payload;
		mc_proto_69_packet_disconnect disconnect;
		mc_proto_69_packet_finish_configuration finish_configuration;
		mc_proto_69_packet_keep_alive keep_alive;
		mc_proto_69_packet_ping ping;
		mc_proto_69_packet_reset_chat reset_chat;
		mc_proto_69_packet_registry_data registry_data;
		mc_proto_69_packet_common_remove_resource_pack remove_resource_pack;
		mc_proto_69_packet_common_add_resource_pack add_resource_pack;
		mc_proto_69_packet_common_store_cookie store_cookie;
		mc_proto_69_packet_common_transfer transfer;
		mc_proto_69_packet_feature_flags feature_flags;
		mc_proto_69_packet_tags tags;
		mc_proto_69_packet_common_select_known_packs select_known_packs;
		mc_proto_69_packet_common_custom_report_details custom_report_details;
		mc_proto_69_packet_common_server_links server_links;
	} params;
} mc_proto_69_configuration_toClient_packet;

typedef struct {
	mc_proto_69_string locale;
	int8_t viewDistance;
	mc_proto_varint chatFlags;
	bool chatColors;
	uint8_t skinParts;
	mc_proto_varint mainHand;
	bool enableTextFiltering;
	bool enableServerListing;
	mc_proto_varint particles;
} mc_proto_69_configuration_toServer_packet_settings;

typedef struct {
	mc_proto_69_string channel;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: restBuffer/structline.j2 */
} mc_proto_69_configuration_toServer_packet_custom_payload;

typedef struct {
} mc_proto_69_configuration_toServer_packet_finish_configuration;

typedef struct {
	int64_t keepAliveId;
} mc_proto_69_configuration_toServer_packet_keep_alive;

typedef struct {
	int32_t id;
} mc_proto_69_configuration_toServer_packet_pong;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
	mc_proto_varint result;
} mc_proto_69_configuration_toServer_packet_resource_pack_receive;

typedef struct {
	enum {
		mc_proto_69_configuration_toServer_packet_name_settings = 0x00,
		mc_proto_69_configuration_toServer_packet_name_cookie_response = 0x01,
		mc_proto_69_configuration_toServer_packet_name_custom_payload = 0x02,
		mc_proto_69_configuration_toServer_packet_name_finish_configuration = 0x03,
		mc_proto_69_configuration_toServer_packet_name_keep_alive = 0x04,
		mc_proto_69_configuration_toServer_packet_name_pong = 0x05,
		mc_proto_69_configuration_toServer_packet_name_resource_pack_receive = 0x06,
		mc_proto_69_configuration_toServer_packet_name_select_known_packs = 0x07,
		mc_proto_69_configuration_toServer_packet_name_custom_report_details = 0x08,
		mc_proto_69_configuration_toServer_packet_name_server_links = 0x09,
	} name;
	union {
		mc_proto_69_packet_settings settings;
		mc_proto_69_packet_common_cookie_response cookie_response;
		mc_proto_69_packet_custom_payload custom_payload;
		mc_proto_69_packet_finish_configuration finish_configuration;
		mc_proto_69_packet_keep_alive keep_alive;
		mc_proto_69_packet_pong pong;
		mc_proto_69_packet_resource_pack_receive resource_pack_receive;
		mc_proto_69_packet_common_select_known_packs select_known_packs;
		mc_proto_69_packet_common_custom_report_details custom_report_details;
		mc_proto_69_packet_common_server_links server_links;
	} params;
} mc_proto_69_configuration_toServer_packet;

typedef struct {
	mc_proto_varint dimension;
	mc_proto_69_string name;
	int64_t hashedSeed;
	enum {
		mc_proto_69_play_toClient_SpawnInfo_gamemode_survival = 0,
		mc_proto_69_play_toClient_SpawnInfo_gamemode_creative = 1,
		mc_proto_69_play_toClient_SpawnInfo_gamemode_adventure = 2,
		mc_proto_69_play_toClient_SpawnInfo_gamemode_spectator = 3,
	} gamemode;
	uint8_t previousGamemode;
	bool isDebug;
	bool isFlat;
	struct {
		bool present;
		struct {
			mc_proto_69_string dimensionName;
			mc_proto_69_position location;
		} data;
	} death;
	mc_proto_varint portalCooldown;
	mc_proto_varint seaLevel;
} mc_proto_69_play_toClient_SpawnInfo;

typedef struct {
	mc_proto_varint entityId;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
	mc_proto_varint type;
	double x;
	double y;
	double z;
	int8_t pitch;
	int8_t yaw;
	int8_t headPitch;
	mc_proto_varint objectData;
	int16_t velocityX;
	int16_t velocityY;
	int16_t velocityZ;
} mc_proto_69_play_toClient_packet_spawn_entity;

typedef struct {
	mc_proto_varint entityId;
	double x;
	double y;
	double z;
	int16_t count;
} mc_proto_69_play_toClient_packet_spawn_entity_experience_orb;

typedef struct {
	mc_proto_varint entityId;
	uint8_t animation;
} mc_proto_69_play_toClient_packet_animation;

typedef struct {
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_varint categoryId;
			mc_proto_varint statisticId;
			mc_proto_varint value;
		} data[];
	} entries;
} mc_proto_69_play_toClient_packet_statistics;

typedef struct {
	mc_proto_varint sequenceId;
} mc_proto_69_play_toClient_packet_acknowledge_player_digging;

typedef struct {
	mc_proto_varint entityId;
	mc_proto_69_position location;
	int8_t destroyStage;
} mc_proto_69_play_toClient_packet_block_break_animation;

typedef struct {
	mc_proto_69_position location;
	mc_proto_varint action;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonOptionalNbt/structline.j2 */
} mc_proto_69_play_toClient_packet_tile_entity_data;

typedef struct {
	mc_proto_69_position location;
	uint8_t byte1;
	uint8_t byte2;
	mc_proto_varint blockId;
} mc_proto_69_play_toClient_packet_block_action;

typedef struct {
	mc_proto_69_position location;
	mc_proto_varint type;
} mc_proto_69_play_toClient_packet_block_change;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
	mc_proto_varint action;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} title;
	union {
		float 0;
		float 2;
	} health;
	union {
		mc_proto_varint 0;
		mc_proto_varint 4;
	} color;
	union {
		mc_proto_varint 0;
		mc_proto_varint 4;
	} dividers;
	union {
		uint8_t 0;
		uint8_t 5;
	} flags;
} mc_proto_69_play_toClient_packet_boss_bar;

typedef struct {
	uint8_t difficulty;
	bool difficultyLocked;
} mc_proto_69_play_toClient_packet_difficulty;

typedef struct {
	mc_proto_varint batchSize;
} mc_proto_69_play_toClient_packet_chunk_batch_finished;

typedef struct {
} mc_proto_69_play_toClient_packet_chunk_batch_start;

typedef struct {
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_packedChunkPos position;
			mc_proto_69_ByteArray data;
		} data[];
	} biomes;
} mc_proto_69_play_toClient_packet_chunk_biomes;

typedef struct {
	bool reset;
} mc_proto_69_play_toClient_packet_clear_titles;

typedef struct {
	mc_proto_varint transactionId;
	mc_proto_varint start;
	mc_proto_varint length;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string match;
			struct {
				bool present;
				/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
			} tooltip;
		} data[];
	} matches;
} mc_proto_69_play_toClient_packet_tab_complete;

typedef struct {
	struct {
		mc_proto_varint count;
		mc_proto_69_command_node data[];
	} nodes;
	mc_proto_varint rootIndex;
} mc_proto_69_play_toClient_packet_declare_commands;

typedef struct {
	mc_proto_69_ContainerID windowId;
} mc_proto_69_play_toClient_packet_close_window;

typedef struct {
	mc_proto_69_ContainerID windowId;
	mc_proto_varint stateId;
	struct {
		mc_proto_varint count;
		mc_proto_69_Slot data[];
	} items;
	mc_proto_69_Slot carriedItem;
} mc_proto_69_play_toClient_packet_window_items;

typedef struct {
	mc_proto_69_ContainerID windowId;
	int16_t property;
	int16_t value;
} mc_proto_69_play_toClient_packet_craft_progress_bar;

typedef struct {
	mc_proto_69_ContainerID windowId;
	mc_proto_varint stateId;
	int16_t slot;
	mc_proto_69_Slot item;
} mc_proto_69_play_toClient_packet_set_slot;

typedef struct {
	mc_proto_69_string cooldownGroup;
	mc_proto_varint cooldownTicks;
} mc_proto_69_play_toClient_packet_set_cooldown;

typedef struct {
	mc_proto_varint action;
	struct {
		mc_proto_varint count;
		mc_proto_69_string data[];
	} entries;
} mc_proto_69_play_toClient_packet_chat_suggestions;

typedef struct {
	mc_proto_69_string channel;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: restBuffer/structline.j2 */
} mc_proto_69_play_toClient_packet_custom_payload;

typedef struct {
	mc_proto_varint entityId;
	mc_proto_varint sourceTypeId;
	mc_proto_varint sourceCauseId;
	mc_proto_varint sourceDirectId;
	struct {
		bool present;
		mc_proto_69_vec3f64 data;
	} sourcePosition;
} mc_proto_69_play_toClient_packet_damage_event;

typedef struct {
	struct {
		mc_proto_varint count;
		int64_t data[];
	} sample;
	mc_proto_varint type;
} mc_proto_69_play_toClient_packet_debug_sample;

typedef struct {
	mc_proto_varint id;
	union {
		uint8_t 0 [256];
	} signature;
} mc_proto_69_play_toClient_packet_hide_message;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
} mc_proto_69_play_toClient_packet_kick_disconnect;

typedef enum {
	mc_proto_69_play_toClient_ChatTypeParameterType_content = 0,
	mc_proto_69_play_toClient_ChatTypeParameterType_sender = 1,
	mc_proto_69_play_toClient_ChatTypeParameterType_target = 2,
} mc_proto_69_play_toClient_ChatTypeParameterType;

typedef struct {
	mc_proto_69_string translationKey;
	struct {
		mc_proto_varint count;
		mc_proto_69_ChatTypeParameterType data[];
	} parameters;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
} mc_proto_69_play_toClient_ChatType;

typedef struct {
	mc_proto_varint registryIndex;
	union {
		struct {
			mc_proto_69_ChatType chat;
			mc_proto_69_ChatType narration;
		} 0;
	};
} mc_proto_69_play_toClient_ChatTypes;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	mc_proto_69_ChatTypes type;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	struct {
		bool present;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} target;
} mc_proto_69_play_toClient_packet_profileless_chat;

typedef struct {
	int32_t entityId;
	int8_t entityStatus;
} mc_proto_69_play_toClient_packet_entity_status;

typedef struct {
	mc_proto_varint entityId;
	double x;
	double y;
	double z;
	double dx;
	double dy;
	double dz;
	float yaw;
	float pitch;
	bool onGround;
} mc_proto_69_play_toClient_packet_sync_entity_position;

typedef struct {
	mc_proto_69_vec3f center;
	struct {
		bool present;
		mc_proto_69_vec3f data;
	} playerKnockback;
	mc_proto_69_Particle explosionParticle;
	mc_proto_varint soundId;
	union {
		struct {
			mc_proto_69_string soundName;
			struct {
				bool present;
				float data;
			} range;
		} 0;
	};
} mc_proto_69_play_toClient_packet_explosion;

typedef struct {
	int32_t chunkZ;
	int32_t chunkX;
} mc_proto_69_play_toClient_packet_unload_chunk;

typedef struct {
	uint8_t reason;
	float gameMode;
} mc_proto_69_play_toClient_packet_game_state_change;

typedef struct {
	mc_proto_69_ContainerID windowId;
	mc_proto_varint nbSlots;
	int32_t entityId;
} mc_proto_69_play_toClient_packet_open_horse_window;

typedef struct {
	mc_proto_varint entityId;
	float yaw;
} mc_proto_69_play_toClient_packet_hurt_animation;

typedef struct {
	double x;
	double z;
	double oldDiameter;
	double newDiameter;
	mc_proto_varint speed;
	mc_proto_varint portalTeleportBoundary;
	mc_proto_varint warningBlocks;
	mc_proto_varint warningTime;
} mc_proto_69_play_toClient_packet_initialize_world_border;

typedef struct {
	int64_t keepAliveId;
} mc_proto_69_play_toClient_packet_keep_alive;

typedef struct {
	int32_t x;
	int32_t z;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	struct {
		uint8_t *data;
		mc_proto_varint len;
	} chunkData;
	struct {
		mc_proto_varint count;
		mc_proto_69_chunkBlockEntity data[];
	} blockEntities;
	struct {
		mc_proto_varint count;
		int64_t data[];
	} skyLightMask;
	struct {
		mc_proto_varint count;
		int64_t data[];
	} blockLightMask;
	struct {
		mc_proto_varint count;
		int64_t data[];
	} emptySkyLightMask;
	struct {
		mc_proto_varint count;
		int64_t data[];
	} emptyBlockLightMask;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_varint count;
			uint8_t data[];
		} data[];
	} skyLight;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_varint count;
			uint8_t data[];
		} data[];
	} blockLight;
} mc_proto_69_play_toClient_packet_map_chunk;

typedef struct {
	int32_t effectId;
	mc_proto_69_position location;
	int32_t data;
	bool global;
} mc_proto_69_play_toClient_packet_world_event;

typedef struct {
	bool longDistance;
	double x;
	double y;
	double z;
	float offsetX;
	float offsetY;
	float offsetZ;
	float velocityOffset;
	int32_t amount;
	mc_proto_69_Particle particle;
} mc_proto_69_play_toClient_packet_world_particles;

typedef struct {
	mc_proto_varint chunkX;
	mc_proto_varint chunkZ;
	struct {
		mc_proto_varint count;
		int64_t data[];
	} skyLightMask;
	struct {
		mc_proto_varint count;
		int64_t data[];
	} blockLightMask;
	struct {
		mc_proto_varint count;
		int64_t data[];
	} emptySkyLightMask;
	struct {
		mc_proto_varint count;
		int64_t data[];
	} emptyBlockLightMask;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_varint count;
			uint8_t data[];
		} data[];
	} skyLight;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_varint count;
			uint8_t data[];
		} data[];
	} blockLight;
} mc_proto_69_play_toClient_packet_update_light;

typedef struct {
	int32_t entityId;
	bool isHardcore;
	struct {
		mc_proto_varint count;
		mc_proto_69_string data[];
	} worldNames;
	mc_proto_varint maxPlayers;
	mc_proto_varint viewDistance;
	mc_proto_varint simulationDistance;
	bool reducedDebugInfo;
	bool enableRespawnScreen;
	bool doLimitedCrafting;
	mc_proto_69_SpawnInfo worldState;
	bool enforcesSecureChat;
} mc_proto_69_play_toClient_packet_login;

typedef struct {
	mc_proto_varint itemDamage;
	int8_t scale;
	bool locked;
	struct {
		bool present;
		struct {
			mc_proto_varint count;
			struct {
				mc_proto_varint type;
				int8_t x;
				int8_t z;
				uint8_t direction;
				struct {
					bool present;
					/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
				} displayName;
			} data[];
		} data;
	} icons;
	uint8_t columns;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
	} rows;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
	} x;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
	} y;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
	} data;
} mc_proto_69_play_toClient_packet_map;

typedef struct {
	mc_proto_69_ContainerID windowId;
	struct {
		mc_proto_varint count;
		struct {
			struct {
				mc_proto_varint itemId;
				mc_proto_varint itemCount;
				mc_proto_varint addedComponentCount;
				/* <class 'ValueError'>: not enough values to unpack (expected 2, got 0) */
			} inputItem1;
			mc_proto_69_Slot outputItem;
			struct {
				bool present;
				struct {
					mc_proto_varint itemId;
					mc_proto_varint itemCount;
					mc_proto_varint addedComponentCount;
					/* <class 'ValueError'>: not enough values to unpack (expected 2, got 0) */
				} data;
			} inputItem2;
			bool tradeDisabled;
			int32_t nbTradeUses;
			int32_t maximumNbTradeUses;
			int32_t xp;
			int32_t specialPrice;
			float priceMultiplier;
			int32_t demand;
		} data[];
	} trades;
	mc_proto_varint villagerLevel;
	mc_proto_varint experience;
	bool isRegularVillager;
	bool canRestock;
} mc_proto_69_play_toClient_packet_trade_list;

typedef struct {
	mc_proto_varint entityId;
	int16_t dX;
	int16_t dY;
	int16_t dZ;
	bool onGround;
} mc_proto_69_play_toClient_packet_rel_entity_move;

typedef struct {
	mc_proto_varint entityId;
	int16_t dX;
	int16_t dY;
	int16_t dZ;
	int8_t yaw;
	int8_t pitch;
	bool onGround;
} mc_proto_69_play_toClient_packet_entity_move_look;

typedef struct {
	mc_proto_varint entityId;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_vec3f position;
			mc_proto_69_vec3f movement;
			float yaw;
			float pitch;
			float weight;
		} data[];
	} steps;
} mc_proto_69_play_toClient_packet_move_minecart;

typedef struct {
	mc_proto_varint entityId;
	int8_t yaw;
	int8_t pitch;
	bool onGround;
} mc_proto_69_play_toClient_packet_entity_look;

typedef struct {
	double x;
	double y;
	double z;
	float yaw;
	float pitch;
} mc_proto_69_play_toClient_packet_vehicle_move;

typedef struct {
	mc_proto_varint hand;
} mc_proto_69_play_toClient_packet_open_book;

typedef struct {
	mc_proto_varint windowId;
	mc_proto_varint inventoryType;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
} mc_proto_69_play_toClient_packet_open_window;

typedef struct {
	mc_proto_69_position location;
	bool isFrontText;
} mc_proto_69_play_toClient_packet_open_sign_entity;

typedef struct {
	int32_t id;
} mc_proto_69_play_toClient_packet_ping;

typedef struct {
	int64_t id;
} mc_proto_69_play_toClient_packet_ping_response;

typedef struct {
	mc_proto_69_ContainerID windowId;
	mc_proto_69_RecipeDisplay recipeDisplay;
} mc_proto_69_play_toClient_packet_craft_recipe_response;

typedef struct {
	int8_t flags;
	float flyingSpeed;
	float walkingSpeed;
} mc_proto_69_play_toClient_packet_abilities;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
	mc_proto_varint index;
	struct {
		bool present;
		uint8_t data[256];
	} signature;
	mc_proto_69_string plainMessage;
	int64_t timestamp;
	int64_t salt;
	mc_proto_69_previousMessages previousMessages;
	struct {
		bool present;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} unsignedChatContent;
	mc_proto_varint filterType;
	union {
		struct {
			mc_proto_varint count;
			int64_t data[];
		} 2;
	} filterTypeMask;
	mc_proto_69_ChatTypes type;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	struct {
		bool present;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} networkTargetName;
} mc_proto_69_play_toClient_packet_player_chat;

typedef struct {
	mc_proto_varint duration;
} mc_proto_69_play_toClient_packet_end_combat_event;

typedef struct {
} mc_proto_69_play_toClient_packet_enter_combat_event;

typedef struct {
	mc_proto_varint playerId;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
} mc_proto_69_play_toClient_packet_death_combat_event;

typedef struct {
	struct {
		mc_proto_varint count;
  /* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */ } players;
} mc_proto_69_play_toClient_packet_player_remove;

typedef struct {
	struct {
		uint32_t unused : 1;
		uint32_t update_priority : 1;
		uint32_t update_display_name : 1;
		uint32_t update_latency : 1;
		uint32_t update_listed : 1;
		uint32_t update_game_mode : 1;
		uint32_t initialize_chat : 1;
		uint32_t add_player : 1;
	} action;
	struct {
		mc_proto_varint count;
		struct {
			/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
			union {
				mc_proto_69_game_profile 1;
			} player;
			union {
				mc_proto_69_chat_session 1;
			} chatSession;
			union {
				mc_proto_varint 1;
			} gamemode;
			union {
				mc_proto_varint 1;
			} listed;
			union {
				mc_proto_varint 1;
			} latency;
			union {
				struct {
					bool present;
					/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
				} 1;
			} displayName;
			union {
				mc_proto_varint 1;
			} listPriority;
		} data[];
	} data;
} mc_proto_69_play_toClient_packet_player_info;

typedef struct {
	mc_proto_varint feet_eyes;
	double x;
	double y;
	double z;
	bool isEntity;
	union {
		mc_proto_varint true;
	} entityId;
	union {
		mc_proto_varint true;
	} entity_feet_eyes;
} mc_proto_69_play_toClient_packet_face_player;

typedef /* <class 'jinja2.exceptions.TemplateNotFound'>: bitflags/structline.j2 */

	typedef struct {
	mc_proto_varint teleportId;
	double x;
	double y;
	double z;
	double dx;
	double dy;
	double dz;
	float yaw;
	float pitch;
	mc_proto_69_PositionUpdateRelatives flags;
} mc_proto_69_play_toClient_packet_position;

typedef struct {
	float yaw;
	float pitch;
} mc_proto_69_play_toClient_packet_player_rotation;

typedef struct {
	struct {
		mc_proto_varint count;
		struct {
			struct {
				mc_proto_varint displayId;
				mc_proto_69_RecipeDisplay display;
				mc_proto_69_optvarint group;
				enum {
					mc_proto_69_play_toClient_packet_recipe_book_add_category_crafting_building_blocks =
						0,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_crafting_redstone = 1,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_crafting_equipment =
						2,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_crafting_misc = 3,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_furnace_food = 4,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_furnace_blocks = 5,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_furnace_misc = 6,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_blast_furnace_blocks =
						7,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_blast_furnace_misc =
						8,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_smoker_food = 9,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_stonecutter = 10,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_smithing = 11,
					mc_proto_69_play_toClient_packet_recipe_book_add_category_campfire = 12,
				} category;
				struct {
					bool present;
					struct {
						mc_proto_varint count;
						mc_proto_69_IDSet data[];
					} data;
				} craftingRequirements;
			} recipe;
			/* <class 'jinja2.exceptions.TemplateNotFound'>: bitflags/structline.j2 */
		} data[];
	} entries;
	bool replace;
} mc_proto_69_play_toClient_packet_recipe_book_add;

typedef struct {
	struct {
		mc_proto_varint count;
		mc_proto_varint data[];
	} recipeIds;
} mc_proto_69_play_toClient_packet_recipe_book_remove;

typedef struct {
	bool craftingGuiOpen;
	bool craftingFilteringCraftable;
	bool smeltingGuiOpen;
	bool smeltingFilteringCraftable;
	bool blastGuiOpen;
	bool blastFilteringCraftable;
	bool smokerGuiOpen;
	bool smokerFilteringCraftable;
} mc_proto_69_play_toClient_packet_recipe_book_settings;

typedef struct {
	struct {
		mc_proto_varint count;
		mc_proto_varint data[];
	} entityIds;
} mc_proto_69_play_toClient_packet_entity_destroy;

typedef struct {
	mc_proto_varint entityId;
	mc_proto_varint effectId;
} mc_proto_69_play_toClient_packet_remove_entity_effect;

typedef struct {
	mc_proto_69_string entity_name;
	struct {
		bool present;
		mc_proto_69_string data;
	} objective_name;
} mc_proto_69_play_toClient_packet_reset_score;

typedef struct {
	mc_proto_69_SpawnInfo worldState;
	uint8_t copyMetadata;
} mc_proto_69_play_toClient_packet_respawn;

typedef struct {
	mc_proto_varint entityId;
	int8_t headYaw;
} mc_proto_69_play_toClient_packet_entity_head_rotation;

typedef struct {
	struct {
		int32_t x : 22;
		int32_t z : 22;
		int32_t y : 20;
	} chunkCoordinates;
	struct {
		mc_proto_varint count;
		mc_proto_varint data[];
	} records;
} mc_proto_69_play_toClient_packet_multi_block_change;

typedef struct {
	struct {
		bool present;
		mc_proto_69_string data;
	} id;
} mc_proto_69_play_toClient_packet_select_advancement_tab;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	struct {
		bool present;
		mc_proto_69_ByteArray data;
	} iconBytes;
} mc_proto_69_play_toClient_packet_server_data;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
} mc_proto_69_play_toClient_packet_action_bar;

typedef struct {
	double x;
	double z;
} mc_proto_69_play_toClient_packet_world_border_center;

typedef struct {
	double oldDiameter;
	double newDiameter;
	mc_proto_varint speed;
} mc_proto_69_play_toClient_packet_world_border_lerp_size;

typedef struct {
	double diameter;
} mc_proto_69_play_toClient_packet_world_border_size;

typedef struct {
	mc_proto_varint warningTime;
} mc_proto_69_play_toClient_packet_world_border_warning_delay;

typedef struct {
	mc_proto_varint warningBlocks;
} mc_proto_69_play_toClient_packet_world_border_warning_reach;

typedef struct {
	mc_proto_varint cameraId;
} mc_proto_69_play_toClient_packet_camera;

typedef struct {
	mc_proto_varint chunkX;
	mc_proto_varint chunkZ;
} mc_proto_69_play_toClient_packet_update_view_position;

typedef struct {
	mc_proto_varint viewDistance;
} mc_proto_69_play_toClient_packet_update_view_distance;

typedef struct {
	struct {
		bool present;
		mc_proto_69_Slot data;
	} contents;
} mc_proto_69_play_toClient_packet_set_cursor_item;

typedef struct {
	mc_proto_69_position location;
	float angle;
} mc_proto_69_play_toClient_packet_spawn_position;

typedef struct {
	mc_proto_varint position;
	mc_proto_69_string name;
} mc_proto_69_play_toClient_packet_scoreboard_display_objective;

typedef struct {
	mc_proto_varint entityId;
	mc_proto_69_entityMetadata metadata;
} mc_proto_69_play_toClient_packet_entity_metadata;

typedef struct {
	int32_t entityId;
	int32_t vehicleId;
} mc_proto_69_play_toClient_packet_attach_entity;

typedef struct {
	mc_proto_varint entityId;
	int16_t velocityX;
	int16_t velocityY;
	int16_t velocityZ;
} mc_proto_69_play_toClient_packet_entity_velocity;

typedef struct {
	mc_proto_varint entityId;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: topBitSetTerminatedArray/structline.j2 */
} mc_proto_69_play_toClient_packet_entity_equipment;

typedef struct {
	float experienceBar;
	mc_proto_varint level;
	mc_proto_varint totalExperience;
} mc_proto_69_play_toClient_packet_experience;

typedef struct {
	float health;
	mc_proto_varint food;
	float foodSaturation;
} mc_proto_69_play_toClient_packet_update_health;

typedef struct {
	int8_t slot;
} mc_proto_69_play_toClient_packet_held_item_slot;

typedef struct {
	mc_proto_69_string name;
	int8_t action;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} displayText;
	union {
		mc_proto_varint 0;
		mc_proto_varint 2;
	} type;
	union {
		struct {
			bool present;
			mc_proto_varint data;
		} 0;
		struct {
			bool present;
			mc_proto_varint data;
		} 2;
	} number_format;
	union {
		union {
			/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
			/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		} 0;
		union {
			/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
			/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		} 2;
	} styling;
} mc_proto_69_play_toClient_packet_scoreboard_objective;

typedef struct {
	mc_proto_varint entityId;
	struct {
		mc_proto_varint count;
		mc_proto_varint data[];
	} passengers;
} mc_proto_69_play_toClient_packet_set_passengers;

typedef struct {
	mc_proto_varint slotId;
	struct {
		bool present;
		mc_proto_69_Slot data;
	} contents;
} mc_proto_69_play_toClient_packet_set_player_inventory;

typedef struct {
	mc_proto_69_string team;
	int8_t mode;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} name;
	union {
		int8_t 0;
		int8_t 2;
	} friendlyFire;
	union {
		mc_proto_69_string 0;
		mc_proto_69_string 2;
	} nameTagVisibility;
	union {
		mc_proto_69_string 0;
		mc_proto_69_string 2;
	} collisionRule;
	union {
		mc_proto_varint 0;
		mc_proto_varint 2;
	} formatting;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} prefix;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} suffix;
	union {
		struct {
			mc_proto_varint count;
			mc_proto_69_string data[];
		} 0;
		struct {
			mc_proto_varint count;
			mc_proto_69_string data[];
		} 3;
		struct {
			mc_proto_varint count;
			mc_proto_69_string data[];
		} 4;
	} players;
} mc_proto_69_play_toClient_packet_teams;

typedef struct {
	mc_proto_69_string itemName;
	mc_proto_69_string scoreName;
	mc_proto_varint value;
	struct {
		bool present;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} display_name;
	struct {
		bool present;
		mc_proto_varint data;
	} number_format;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
		/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	} styling;
} mc_proto_69_play_toClient_packet_scoreboard_score;

typedef struct {
	mc_proto_varint distance;
} mc_proto_69_play_toClient_packet_simulation_distance;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
} mc_proto_69_play_toClient_packet_set_title_subtitle;

typedef struct {
	int64_t age;
	int64_t time;
	bool tickDayTime;
} mc_proto_69_play_toClient_packet_update_time;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
} mc_proto_69_play_toClient_packet_set_title_text;

typedef struct {
	int32_t fadeIn;
	int32_t stay;
	int32_t fadeOut;
} mc_proto_69_play_toClient_packet_set_title_time;

typedef struct {
	mc_proto_varint soundId;
	union {
		struct {
			mc_proto_69_string resource;
			struct {
				bool present;
				float data;
			} range;
		} 0;
	} soundEvent;
	mc_proto_69_soundSource soundCategory;
	mc_proto_varint entityId;
	float volume;
	float pitch;
	int64_t seed;
} mc_proto_69_play_toClient_packet_entity_sound_effect;

typedef struct {
	mc_proto_varint soundId;
	union {
		struct {
			mc_proto_69_string resource;
			struct {
				bool present;
				float data;
			} range;
		} 0;
	} soundEvent;
	mc_proto_69_soundSource soundCategory;
	int32_t x;
	int32_t y;
	int32_t z;
	float volume;
	float pitch;
	int64_t seed;
} mc_proto_69_play_toClient_packet_sound_effect;

typedef struct {
} mc_proto_69_play_toClient_packet_start_configuration;

typedef struct {
	int8_t flags;
	union {
		mc_proto_varint 1;
		mc_proto_varint 3;
	} source;
	union {
		mc_proto_69_string 2;
		mc_proto_69_string 3;
	} sound;
} mc_proto_69_play_toClient_packet_stop_sound;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	bool isActionBar;
} mc_proto_69_play_toClient_packet_system_chat;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2 */
} mc_proto_69_play_toClient_packet_playerlist_header;

typedef struct {
	mc_proto_varint transactionId;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: anonOptionalNbt/structline.j2 */
} mc_proto_69_play_toClient_packet_nbt_query_response;

typedef struct {
	mc_proto_varint collectedEntityId;
	mc_proto_varint collectorEntityId;
	mc_proto_varint pickupItemCount;
} mc_proto_69_play_toClient_packet_collect;

typedef struct {
	mc_proto_varint entityId;
	double x;
	double y;
	double z;
	int8_t yaw;
	int8_t pitch;
	bool onGround;
} mc_proto_69_play_toClient_packet_entity_teleport;

typedef struct {
	float tick_rate;
	bool is_frozen;
} mc_proto_69_play_toClient_packet_set_ticking_state;

typedef struct {
	mc_proto_varint tick_steps;
} mc_proto_69_play_toClient_packet_step_tick;

typedef struct {
	bool reset;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string key;
			struct {
				struct {
					bool present;
					mc_proto_69_string data;
				} parentId;
				struct {
					bool present;
					struct {
						/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2
						 */
						/* <class 'jinja2.exceptions.TemplateNotFound'>: anonymousNbt/structline.j2
						 */
						mc_proto_69_Slot icon;
						mc_proto_varint frameType;
						struct {
							uint32_t unused : 29;
							uint32_t hidden : 1;
							uint32_t show_toast : 1;
							uint32_t has_background_texture : 1;
						} flags;
						union {
							mc_proto_69_string 1;
						} backgroundTexture;
						float xCord;
						float yCord;
					} data;
				} displayData;
				struct {
					mc_proto_varint count;
					struct {
						mc_proto_varint count;
						mc_proto_69_string data[];
					} data[];
				} requirements;
				bool sendsTelemtryData;
			} value;
		} data[];
	} advancementMapping;
	struct {
		mc_proto_varint count;
		mc_proto_69_string data[];
	} identifiers;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string key;
			struct {
				mc_proto_varint count;
				struct {
					mc_proto_69_string criterionIdentifier;
					struct {
						bool present;
						int64_t data;
					} criterionProgress;
				} data[];
			} value;
		} data[];
	} progressMapping;
} mc_proto_69_play_toClient_packet_advancements;

typedef struct {
	mc_proto_varint entityId;
	struct {
		mc_proto_varint count;
		struct {
			enum {
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic.armor = 0,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic
					.armor_toughness = 1,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic
					.attack_damage = 2,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic
					.attack_knockback = 3,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic.attack_speed =
					4,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_player
					.block_break_speed = 5,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_player
					.block_interaction_range = 6,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_player
					.entity_interaction_range = 7,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic
					.fall_damage_multiplier = 8,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic.flying_speed =
					9,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic.follow_range =
					10,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic.gravity = 11,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic
					.jump_strength = 12,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic
					.knockback_resistance = 13,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic.luck = 14,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic
					.max_absorption = 15,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic.max_health =
					16,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic
					.movement_speed = 17,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic
					.safe_fall_distance = 18,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic.scale = 19,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_zombie
					.spawn_reinforcements = 20,
				mc_proto_69_play_toClient_packet_entity_update_attributes_key_generic.step_height =
					21,
			} key;
			double value;
			struct {
				mc_proto_varint count;
				struct {
					mc_proto_69_string uuid;
					double amount;
					int8_t operation;
				} data[];
			} modifiers;
		} data[];
	} properties;
} mc_proto_69_play_toClient_packet_entity_update_attributes;

typedef struct {
	mc_proto_varint entityId;
	mc_proto_varint effectId;
	mc_proto_varint amplifier;
	mc_proto_varint duration;
	uint8_t flags;
} mc_proto_69_play_toClient_packet_entity_effect;

typedef struct {
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string name;
			struct {
				mc_proto_varint count;
				mc_proto_varint data[];
			} items;
		} data[];
	} recipes;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_IDSet input;
			mc_proto_69_SlotDisplay slotDisplay;
		} data[];
	} stoneCutterRecipes;
} mc_proto_69_play_toClient_packet_declare_recipes;

typedef struct {
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string tagType;
			mc_proto_69_tags tags;
		} data[];
	} tags;
} mc_proto_69_play_toClient_packet_tags;

typedef struct {
	mc_proto_varint id;
	double accelerationPower;
} mc_proto_69_play_toClient_packet_set_projectile_power;

typedef struct {
	enum {
		mc_proto_69_play_toClient_packet_name_bundle_delimiter = 0x00,
		mc_proto_69_play_toClient_packet_name_spawn_entity = 0x01,
		mc_proto_69_play_toClient_packet_name_spawn_entity_experience_orb = 0x02,
		mc_proto_69_play_toClient_packet_name_animation = 0x03,
		mc_proto_69_play_toClient_packet_name_statistics = 0x04,
		mc_proto_69_play_toClient_packet_name_acknowledge_player_digging = 0x05,
		mc_proto_69_play_toClient_packet_name_block_break_animation = 0x06,
		mc_proto_69_play_toClient_packet_name_tile_entity_data = 0x07,
		mc_proto_69_play_toClient_packet_name_block_action = 0x08,
		mc_proto_69_play_toClient_packet_name_block_change = 0x09,
		mc_proto_69_play_toClient_packet_name_boss_bar = 0x0a,
		mc_proto_69_play_toClient_packet_name_difficulty = 0x0b,
		mc_proto_69_play_toClient_packet_name_chunk_batch_finished = 0x0c,
		mc_proto_69_play_toClient_packet_name_chunk_batch_start = 0x0d,
		mc_proto_69_play_toClient_packet_name_chunk_biomes = 0x0e,
		mc_proto_69_play_toClient_packet_name_clear_titles = 0x0f,
		mc_proto_69_play_toClient_packet_name_tab_complete = 0x10,
		mc_proto_69_play_toClient_packet_name_declare_commands = 0x11,
		mc_proto_69_play_toClient_packet_name_close_window = 0x12,
		mc_proto_69_play_toClient_packet_name_window_items = 0x13,
		mc_proto_69_play_toClient_packet_name_craft_progress_bar = 0x14,
		mc_proto_69_play_toClient_packet_name_set_slot = 0x15,
		mc_proto_69_play_toClient_packet_name_cookie_request = 0x16,
		mc_proto_69_play_toClient_packet_name_set_cooldown = 0x17,
		mc_proto_69_play_toClient_packet_name_chat_suggestions = 0x18,
		mc_proto_69_play_toClient_packet_name_custom_payload = 0x19,
		mc_proto_69_play_toClient_packet_name_damage_event = 0x1a,
		mc_proto_69_play_toClient_packet_name_debug_sample = 0x1b,
		mc_proto_69_play_toClient_packet_name_hide_message = 0x1c,
		mc_proto_69_play_toClient_packet_name_kick_disconnect = 0x1d,
		mc_proto_69_play_toClient_packet_name_profileless_chat = 0x1e,
		mc_proto_69_play_toClient_packet_name_entity_status = 0x1f,
		mc_proto_69_play_toClient_packet_name_sync_entity_position = 0x20,
		mc_proto_69_play_toClient_packet_name_explosion = 0x21,
		mc_proto_69_play_toClient_packet_name_unload_chunk = 0x22,
		mc_proto_69_play_toClient_packet_name_game_state_change = 0x23,
		mc_proto_69_play_toClient_packet_name_open_horse_window = 0x24,
		mc_proto_69_play_toClient_packet_name_hurt_animation = 0x25,
		mc_proto_69_play_toClient_packet_name_initialize_world_border = 0x26,
		mc_proto_69_play_toClient_packet_name_keep_alive = 0x27,
		mc_proto_69_play_toClient_packet_name_map_chunk = 0x28,
		mc_proto_69_play_toClient_packet_name_world_event = 0x29,
		mc_proto_69_play_toClient_packet_name_world_particles = 0x2a,
		mc_proto_69_play_toClient_packet_name_update_light = 0x2b,
		mc_proto_69_play_toClient_packet_name_login = 0x2c,
		mc_proto_69_play_toClient_packet_name_map = 0x2d,
		mc_proto_69_play_toClient_packet_name_trade_list = 0x2e,
		mc_proto_69_play_toClient_packet_name_rel_entity_move = 0x2f,
		mc_proto_69_play_toClient_packet_name_entity_move_look = 0x30,
		mc_proto_69_play_toClient_packet_name_move_minecart = 0x31,
		mc_proto_69_play_toClient_packet_name_entity_look = 0x32,
		mc_proto_69_play_toClient_packet_name_vehicle_move = 0x33,
		mc_proto_69_play_toClient_packet_name_open_book = 0x34,
		mc_proto_69_play_toClient_packet_name_open_window = 0x35,
		mc_proto_69_play_toClient_packet_name_open_sign_entity = 0x36,
		mc_proto_69_play_toClient_packet_name_ping = 0x37,
		mc_proto_69_play_toClient_packet_name_ping_response = 0x38,
		mc_proto_69_play_toClient_packet_name_craft_recipe_response = 0x39,
		mc_proto_69_play_toClient_packet_name_abilities = 0x3a,
		mc_proto_69_play_toClient_packet_name_player_chat = 0x3b,
		mc_proto_69_play_toClient_packet_name_end_combat_event = 0x3c,
		mc_proto_69_play_toClient_packet_name_enter_combat_event = 0x3d,
		mc_proto_69_play_toClient_packet_name_death_combat_event = 0x3e,
		mc_proto_69_play_toClient_packet_name_player_remove = 0x3f,
		mc_proto_69_play_toClient_packet_name_player_info = 0x40,
		mc_proto_69_play_toClient_packet_name_face_player = 0x41,
		mc_proto_69_play_toClient_packet_name_position = 0x42,
		mc_proto_69_play_toClient_packet_name_player_rotation = 0x43,
		mc_proto_69_play_toClient_packet_name_recipe_book_add = 0x44,
		mc_proto_69_play_toClient_packet_name_recipe_book_remove = 0x45,
		mc_proto_69_play_toClient_packet_name_recipe_book_settings = 0x46,
		mc_proto_69_play_toClient_packet_name_entity_destroy = 0x47,
		mc_proto_69_play_toClient_packet_name_remove_entity_effect = 0x48,
		mc_proto_69_play_toClient_packet_name_reset_score = 0x49,
		mc_proto_69_play_toClient_packet_name_remove_resource_pack = 0x4a,
		mc_proto_69_play_toClient_packet_name_add_resource_pack = 0x4b,
		mc_proto_69_play_toClient_packet_name_respawn = 0x4c,
		mc_proto_69_play_toClient_packet_name_entity_head_rotation = 0x4d,
		mc_proto_69_play_toClient_packet_name_multi_block_change = 0x4e,
		mc_proto_69_play_toClient_packet_name_select_advancement_tab = 0x4f,
		mc_proto_69_play_toClient_packet_name_server_data = 0x50,
		mc_proto_69_play_toClient_packet_name_action_bar = 0x51,
		mc_proto_69_play_toClient_packet_name_world_border_center = 0x52,
		mc_proto_69_play_toClient_packet_name_world_border_lerp_size = 0x53,
		mc_proto_69_play_toClient_packet_name_world_border_size = 0x54,
		mc_proto_69_play_toClient_packet_name_world_border_warning_delay = 0x55,
		mc_proto_69_play_toClient_packet_name_world_border_warning_reach = 0x56,
		mc_proto_69_play_toClient_packet_name_camera = 0x57,
		mc_proto_69_play_toClient_packet_name_update_view_position = 0x58,
		mc_proto_69_play_toClient_packet_name_update_view_distance = 0x59,
		mc_proto_69_play_toClient_packet_name_set_cursor_item = 0x5a,
		mc_proto_69_play_toClient_packet_name_spawn_position = 0x5b,
		mc_proto_69_play_toClient_packet_name_scoreboard_display_objective = 0x5c,
		mc_proto_69_play_toClient_packet_name_entity_metadata = 0x5d,
		mc_proto_69_play_toClient_packet_name_attach_entity = 0x5e,
		mc_proto_69_play_toClient_packet_name_entity_velocity = 0x5f,
		mc_proto_69_play_toClient_packet_name_entity_equipment = 0x60,
		mc_proto_69_play_toClient_packet_name_experience = 0x61,
		mc_proto_69_play_toClient_packet_name_update_health = 0x62,
		mc_proto_69_play_toClient_packet_name_held_item_slot = 0x63,
		mc_proto_69_play_toClient_packet_name_scoreboard_objective = 0x64,
		mc_proto_69_play_toClient_packet_name_set_passengers = 0x65,
		mc_proto_69_play_toClient_packet_name_set_player_inventory = 0x66,
		mc_proto_69_play_toClient_packet_name_teams = 0x67,
		mc_proto_69_play_toClient_packet_name_scoreboard_score = 0x68,
		mc_proto_69_play_toClient_packet_name_simulation_distance = 0x69,
		mc_proto_69_play_toClient_packet_name_set_title_subtitle = 0x6a,
		mc_proto_69_play_toClient_packet_name_update_time = 0x6b,
		mc_proto_69_play_toClient_packet_name_set_title_text = 0x6c,
		mc_proto_69_play_toClient_packet_name_set_title_time = 0x6d,
		mc_proto_69_play_toClient_packet_name_entity_sound_effect = 0x6e,
		mc_proto_69_play_toClient_packet_name_sound_effect = 0x6f,
		mc_proto_69_play_toClient_packet_name_start_configuration = 0x70,
		mc_proto_69_play_toClient_packet_name_stop_sound = 0x71,
		mc_proto_69_play_toClient_packet_name_store_cookie = 0x72,
		mc_proto_69_play_toClient_packet_name_system_chat = 0x73,
		mc_proto_69_play_toClient_packet_name_playerlist_header = 0x74,
		mc_proto_69_play_toClient_packet_name_nbt_query_response = 0x75,
		mc_proto_69_play_toClient_packet_name_collect = 0x76,
		mc_proto_69_play_toClient_packet_name_entity_teleport = 0x77,
		mc_proto_69_play_toClient_packet_name_set_ticking_state = 0x78,
		mc_proto_69_play_toClient_packet_name_step_tick = 0x79,
		mc_proto_69_play_toClient_packet_name_transfer = 0x7a,
		mc_proto_69_play_toClient_packet_name_advancements = 0x7b,
		mc_proto_69_play_toClient_packet_name_entity_update_attributes = 0x7c,
		mc_proto_69_play_toClient_packet_name_entity_effect = 0x7d,
		mc_proto_69_play_toClient_packet_name_declare_recipes = 0x7e,
		mc_proto_69_play_toClient_packet_name_tags = 0x7f,
		mc_proto_69_play_toClient_packet_name_set_projectile_power = 0x80,
		mc_proto_69_play_toClient_packet_name_custom_report_details = 0x81,
		mc_proto_69_play_toClient_packet_name_server_links = 0x82,
	} name;
	union {
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
		mc_proto_69_packet_spawn_entity spawn_entity;
		mc_proto_69_packet_spawn_entity_experience_orb spawn_entity_experience_orb;
		mc_proto_69_packet_animation animation;
		mc_proto_69_packet_statistics statistics;
		mc_proto_69_packet_acknowledge_player_digging acknowledge_player_digging;
		mc_proto_69_packet_block_break_animation block_break_animation;
		mc_proto_69_packet_tile_entity_data tile_entity_data;
		mc_proto_69_packet_block_action block_action;
		mc_proto_69_packet_block_change block_change;
		mc_proto_69_packet_boss_bar boss_bar;
		mc_proto_69_packet_difficulty difficulty;
		mc_proto_69_packet_chunk_batch_finished chunk_batch_finished;
		mc_proto_69_packet_chunk_batch_start chunk_batch_start;
		mc_proto_69_packet_chunk_biomes chunk_biomes;
		mc_proto_69_packet_clear_titles clear_titles;
		mc_proto_69_packet_tab_complete tab_complete;
		mc_proto_69_packet_declare_commands declare_commands;
		mc_proto_69_packet_close_window close_window;
		mc_proto_69_packet_window_items window_items;
		mc_proto_69_packet_craft_progress_bar craft_progress_bar;
		mc_proto_69_packet_set_slot set_slot;
		mc_proto_69_packet_common_cookie_request cookie_request;
		mc_proto_69_packet_set_cooldown set_cooldown;
		mc_proto_69_packet_chat_suggestions chat_suggestions;
		mc_proto_69_packet_custom_payload custom_payload;
		mc_proto_69_packet_damage_event damage_event;
		mc_proto_69_packet_debug_sample debug_sample;
		mc_proto_69_packet_hide_message hide_message;
		mc_proto_69_packet_kick_disconnect kick_disconnect;
		mc_proto_69_packet_profileless_chat profileless_chat;
		mc_proto_69_packet_entity_status entity_status;
		mc_proto_69_packet_sync_entity_position sync_entity_position;
		mc_proto_69_packet_explosion explosion;
		mc_proto_69_packet_unload_chunk unload_chunk;
		mc_proto_69_packet_game_state_change game_state_change;
		mc_proto_69_packet_open_horse_window open_horse_window;
		mc_proto_69_packet_hurt_animation hurt_animation;
		mc_proto_69_packet_initialize_world_border initialize_world_border;
		mc_proto_69_packet_keep_alive keep_alive;
		mc_proto_69_packet_map_chunk map_chunk;
		mc_proto_69_packet_world_event world_event;
		mc_proto_69_packet_world_particles world_particles;
		mc_proto_69_packet_update_light update_light;
		mc_proto_69_packet_login login;
		mc_proto_69_packet_map map;
		mc_proto_69_packet_trade_list trade_list;
		mc_proto_69_packet_rel_entity_move rel_entity_move;
		mc_proto_69_packet_entity_move_look entity_move_look;
		mc_proto_69_packet_move_minecart move_minecart;
		mc_proto_69_packet_entity_look entity_look;
		mc_proto_69_packet_vehicle_move vehicle_move;
		mc_proto_69_packet_open_book open_book;
		mc_proto_69_packet_open_window open_window;
		mc_proto_69_packet_open_sign_entity open_sign_entity;
		mc_proto_69_packet_ping ping;
		mc_proto_69_packet_ping_response ping_response;
		mc_proto_69_packet_craft_recipe_response craft_recipe_response;
		mc_proto_69_packet_abilities abilities;
		mc_proto_69_packet_player_chat player_chat;
		mc_proto_69_packet_end_combat_event end_combat_event;
		mc_proto_69_packet_enter_combat_event enter_combat_event;
		mc_proto_69_packet_death_combat_event death_combat_event;
		mc_proto_69_packet_player_remove player_remove;
		mc_proto_69_packet_player_info player_info;
		mc_proto_69_packet_face_player face_player;
		mc_proto_69_packet_position position;
		mc_proto_69_packet_player_rotation player_rotation;
		mc_proto_69_packet_recipe_book_add recipe_book_add;
		mc_proto_69_packet_recipe_book_remove recipe_book_remove;
		mc_proto_69_packet_recipe_book_settings recipe_book_settings;
		mc_proto_69_packet_entity_destroy entity_destroy;
		mc_proto_69_packet_remove_entity_effect remove_entity_effect;
		mc_proto_69_packet_reset_score reset_score;
		mc_proto_69_packet_common_remove_resource_pack remove_resource_pack;
		mc_proto_69_packet_common_add_resource_pack add_resource_pack;
		mc_proto_69_packet_respawn respawn;
		mc_proto_69_packet_entity_head_rotation entity_head_rotation;
		mc_proto_69_packet_multi_block_change multi_block_change;
		mc_proto_69_packet_select_advancement_tab select_advancement_tab;
		mc_proto_69_packet_server_data server_data;
		mc_proto_69_packet_action_bar action_bar;
		mc_proto_69_packet_world_border_center world_border_center;
		mc_proto_69_packet_world_border_lerp_size world_border_lerp_size;
		mc_proto_69_packet_world_border_size world_border_size;
		mc_proto_69_packet_world_border_warning_delay world_border_warning_delay;
		mc_proto_69_packet_world_border_warning_reach world_border_warning_reach;
		mc_proto_69_packet_camera camera;
		mc_proto_69_packet_update_view_position update_view_position;
		mc_proto_69_packet_update_view_distance update_view_distance;
		mc_proto_69_packet_set_cursor_item set_cursor_item;
		mc_proto_69_packet_held_item_slot held_item_slot;
		mc_proto_69_packet_spawn_position spawn_position;
		mc_proto_69_packet_scoreboard_display_objective scoreboard_display_objective;
		mc_proto_69_packet_entity_metadata entity_metadata;
		mc_proto_69_packet_attach_entity attach_entity;
		mc_proto_69_packet_entity_velocity entity_velocity;
		mc_proto_69_packet_entity_equipment entity_equipment;
		mc_proto_69_packet_experience experience;
		mc_proto_69_packet_update_health update_health;
		mc_proto_69_packet_scoreboard_objective scoreboard_objective;
		mc_proto_69_packet_set_passengers set_passengers;
		mc_proto_69_packet_set_player_inventory set_player_inventory;
		mc_proto_69_packet_teams teams;
		mc_proto_69_packet_scoreboard_score scoreboard_score;
		mc_proto_69_packet_simulation_distance simulation_distance;
		mc_proto_69_packet_set_title_subtitle set_title_subtitle;
		mc_proto_69_packet_update_time update_time;
		mc_proto_69_packet_set_title_text set_title_text;
		mc_proto_69_packet_set_title_time set_title_time;
		mc_proto_69_packet_entity_sound_effect entity_sound_effect;
		mc_proto_69_packet_sound_effect sound_effect;
		mc_proto_69_packet_start_configuration start_configuration;
		mc_proto_69_packet_stop_sound stop_sound;
		mc_proto_69_packet_common_store_cookie store_cookie;
		mc_proto_69_packet_system_chat system_chat;
		mc_proto_69_packet_playerlist_header playerlist_header;
		mc_proto_69_packet_nbt_query_response nbt_query_response;
		mc_proto_69_packet_collect collect;
		mc_proto_69_packet_entity_teleport entity_teleport;
		mc_proto_69_packet_set_ticking_state set_ticking_state;
		mc_proto_69_packet_step_tick step_tick;
		mc_proto_69_packet_common_transfer transfer;
		mc_proto_69_packet_advancements advancements;
		mc_proto_69_packet_entity_update_attributes entity_update_attributes;
		mc_proto_69_packet_entity_effect entity_effect;
		mc_proto_69_packet_declare_recipes declare_recipes;
		mc_proto_69_packet_tags tags;
		mc_proto_69_packet_set_projectile_power set_projectile_power;
		mc_proto_69_packet_common_custom_report_details custom_report_details;
		mc_proto_69_packet_common_server_links server_links;
	} params;
} mc_proto_69_play_toClient_packet;

typedef struct {
	mc_proto_varint teleportId;
} mc_proto_69_play_toServer_packet_teleport_confirm;

typedef struct {
	mc_proto_varint transactionId;
	mc_proto_69_position location;
} mc_proto_69_play_toServer_packet_query_block_nbt;

typedef struct {
	mc_proto_varint slotId;
	mc_proto_varint selectedItemIndex;
} mc_proto_69_play_toServer_packet_select_bundle_item;

typedef struct {
	uint8_t newDifficulty;
} mc_proto_69_play_toServer_packet_set_difficulty;

typedef struct {
	mc_proto_varint count;
} mc_proto_69_play_toServer_packet_message_acknowledgement;

typedef struct {
	mc_proto_69_string command;
} mc_proto_69_play_toServer_packet_chat_command;

typedef struct {
	mc_proto_69_string command;
	int64_t timestamp;
	int64_t salt;
	struct {
		mc_proto_varint count;
		struct {
			mc_proto_69_string argumentName;
			uint8_t signature[256];
		} data[];
	} argumentSignatures;
	mc_proto_varint messageCount;
	uint8_t acknowledged[3];
} mc_proto_69_play_toServer_packet_chat_command_signed;

typedef struct {
	mc_proto_69_string message;
	int64_t timestamp;
	int64_t salt;
	struct {
		bool present;
		uint8_t data[256];
	} signature;
	mc_proto_varint offset;
	uint8_t acknowledged[3];
} mc_proto_69_play_toServer_packet_chat_message;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
	int64_t expireTime;
	mc_proto_69_ByteArray publicKey;
	mc_proto_69_ByteArray signature;
} mc_proto_69_play_toServer_packet_chat_session_update;

typedef struct {
	float chunksPerTick;
} mc_proto_69_play_toServer_packet_chunk_batch_received;

typedef struct {
	mc_proto_varint actionId;
} mc_proto_69_play_toServer_packet_client_command;

typedef struct {
} mc_proto_69_play_toServer_packet_tick_end;

typedef struct {
	mc_proto_69_string locale;
	int8_t viewDistance;
	mc_proto_varint chatFlags;
	bool chatColors;
	uint8_t skinParts;
	mc_proto_varint mainHand;
	bool enableTextFiltering;
	bool enableServerListing;
	enum {
		mc_proto_69_play_toServer_packet_settings_particleStatus_all = 0,
		mc_proto_69_play_toServer_packet_settings_particleStatus_decreased = 1,
		mc_proto_69_play_toServer_packet_settings_particleStatus_minimal = 2,
	} particleStatus;
} mc_proto_69_play_toServer_packet_settings;

typedef struct {
	mc_proto_varint transactionId;
	mc_proto_69_string text;
} mc_proto_69_play_toServer_packet_tab_complete;

typedef struct {
} mc_proto_69_play_toServer_packet_configuration_acknowledged;

typedef struct {
	mc_proto_69_ContainerID windowId;
	int8_t enchantment;
} mc_proto_69_play_toServer_packet_enchant_item;

typedef struct {
	mc_proto_69_ContainerID windowId;
	mc_proto_varint stateId;
	int16_t slot;
	int8_t mouseButton;
	mc_proto_varint mode;
	struct {
		mc_proto_varint count;
		struct {
			int16_t location;
			mc_proto_69_Slot item;
		} data[];
	} changedSlots;
	mc_proto_69_Slot cursorItem;
} mc_proto_69_play_toServer_packet_window_click;

typedef struct {
	mc_proto_69_ContainerID windowId;
} mc_proto_69_play_toServer_packet_close_window;

typedef struct {
	mc_proto_varint slot_id;
	mc_proto_69_ContainerID window_id;
	bool state;
} mc_proto_69_play_toServer_packet_set_slot_state;

typedef struct {
	mc_proto_69_string channel;
	/* <class 'jinja2.exceptions.TemplateNotFound'>: restBuffer/structline.j2 */
} mc_proto_69_play_toServer_packet_custom_payload;

typedef struct {
	mc_proto_varint type;
} mc_proto_69_play_toServer_packet_debug_sample_subscription;

typedef struct {
	mc_proto_varint hand;
	struct {
		mc_proto_varint count;
		mc_proto_69_string data[];
	} pages;
	struct {
		bool present;
		mc_proto_69_string data;
	} title;
} mc_proto_69_play_toServer_packet_edit_book;

typedef struct {
	mc_proto_varint transactionId;
	mc_proto_varint entityId;
} mc_proto_69_play_toServer_packet_query_entity_nbt;

typedef struct {
	mc_proto_varint target;
	mc_proto_varint mouse;
	union {
		float 2;
	} x;
	union {
		float 2;
	} y;
	union {
		float 2;
	} z;
	union {
		mc_proto_varint 0;
		mc_proto_varint 2;
	} hand;
	bool sneaking;
} mc_proto_69_play_toServer_packet_use_entity;

typedef struct {
	mc_proto_69_position location;
	mc_proto_varint levels;
	bool keepJigsaws;
} mc_proto_69_play_toServer_packet_generate_structure;

typedef struct {
	int64_t keepAliveId;
} mc_proto_69_play_toServer_packet_keep_alive;

typedef struct {
	bool locked;
} mc_proto_69_play_toServer_packet_lock_difficulty;

typedef /* <class 'jinja2.exceptions.TemplateNotFound'>: bitflags/structline.j2 */

	typedef struct {
	double x;
	double y;
	double z;
	mc_proto_69_MovementFlags flags;
} mc_proto_69_play_toServer_packet_position;

typedef struct {
	double x;
	double y;
	double z;
	float yaw;
	float pitch;
	mc_proto_69_MovementFlags flags;
} mc_proto_69_play_toServer_packet_position_look;

typedef struct {
	float yaw;
	float pitch;
	mc_proto_69_MovementFlags flags;
} mc_proto_69_play_toServer_packet_look;

typedef struct {
	mc_proto_69_MovementFlags flags;
} mc_proto_69_play_toServer_packet_flying;

typedef struct {
	double x;
	double y;
	double z;
	float yaw;
	float pitch;
} mc_proto_69_play_toServer_packet_vehicle_move;

typedef struct {
	bool leftPaddle;
	bool rightPaddle;
} mc_proto_69_play_toServer_packet_steer_boat;

typedef struct {
	mc_proto_varint slot;
} mc_proto_69_play_toServer_packet_pick_item;

typedef struct {
	int64_t id;
} mc_proto_69_play_toServer_packet_ping_request;

typedef struct {
	mc_proto_69_ContainerID windowId;
	mc_proto_varint recipeId;
	bool makeAll;
} mc_proto_69_play_toServer_packet_craft_recipe_request;

typedef struct {
	int8_t flags;
} mc_proto_69_play_toServer_packet_abilities;

typedef struct {
	mc_proto_varint status;
	mc_proto_69_position location;
	int8_t face;
	mc_proto_varint sequence;
} mc_proto_69_play_toServer_packet_block_dig;

typedef struct {
	mc_proto_varint entityId;
	mc_proto_varint actionId;
	mc_proto_varint jumpBoost;
} mc_proto_69_play_toServer_packet_entity_action;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: bitflags/structline.j2 */
} mc_proto_69_play_toServer_packet_player_input;

typedef struct {
	int32_t id;
} mc_proto_69_play_toServer_packet_pong;

typedef struct {
	mc_proto_varint bookId;
	bool bookOpen;
	bool filterActive;
} mc_proto_69_play_toServer_packet_recipe_book;

typedef struct {
	mc_proto_varint recipeId;
} mc_proto_69_play_toServer_packet_displayed_recipe;

typedef struct {
	mc_proto_69_string name;
} mc_proto_69_play_toServer_packet_name_item;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
	mc_proto_varint result;
} mc_proto_69_play_toServer_packet_resource_pack_receive;

typedef struct {
	mc_proto_varint action;
	union {
		mc_proto_69_string 0;
		/* <class 'jinja2.exceptions.TemplateNotFound'>: void/structline.j2 */
	} tabId;
} mc_proto_69_play_toServer_packet_advancement_tab;

typedef struct {
	mc_proto_varint slot;
} mc_proto_69_play_toServer_packet_select_trade;

typedef struct {
	struct {
		bool present;
		mc_proto_varint data;
	} primary_effect;
	struct {
		bool present;
		mc_proto_varint data;
	} secondary_effect;
} mc_proto_69_play_toServer_packet_set_beacon_effect;

typedef struct {
	int16_t slotId;
} mc_proto_69_play_toServer_packet_held_item_slot;

typedef struct {
	mc_proto_69_position location;
	mc_proto_69_string command;
	mc_proto_varint mode;
	uint8_t flags;
} mc_proto_69_play_toServer_packet_update_command_block;

typedef struct {
	mc_proto_varint entityId;
	mc_proto_69_string command;
	bool track_output;
} mc_proto_69_play_toServer_packet_update_command_block_minecart;

typedef struct {
	int16_t slot;
	mc_proto_69_Slot item;
} mc_proto_69_play_toServer_packet_set_creative_slot;

typedef struct {
	mc_proto_69_position location;
	mc_proto_69_string name;
	mc_proto_69_string target;
	mc_proto_69_string pool;
	mc_proto_69_string finalState;
	mc_proto_69_string jointType;
	mc_proto_varint selection_priority;
	mc_proto_varint placement_priority;
} mc_proto_69_play_toServer_packet_update_jigsaw_block;

typedef struct {
	mc_proto_69_position location;
	mc_proto_varint action;
	mc_proto_varint mode;
	mc_proto_69_string name;
	int8_t offset_x;
	int8_t offset_y;
	int8_t offset_z;
	int8_t size_x;
	int8_t size_y;
	int8_t size_z;
	mc_proto_varint mirror;
	mc_proto_varint rotation;
	mc_proto_69_string metadata;
	float integrity;
	mc_proto_varint seed;
	uint8_t flags;
} mc_proto_69_play_toServer_packet_update_structure_block;

typedef struct {
	mc_proto_69_position location;
	bool isFrontText;
	mc_proto_69_string text1;
	mc_proto_69_string text2;
	mc_proto_69_string text3;
	mc_proto_69_string text4;
} mc_proto_69_play_toServer_packet_update_sign;

typedef struct {
	mc_proto_varint hand;
} mc_proto_69_play_toServer_packet_arm_animation;

typedef struct {
	/* <class 'jinja2.exceptions.TemplateNotFound'>: UUID/structline.j2 */
} mc_proto_69_play_toServer_packet_spectate;

typedef struct {
	mc_proto_varint hand;
	mc_proto_69_position location;
	mc_proto_varint direction;
	float cursorX;
	float cursorY;
	float cursorZ;
	bool insideBlock;
	bool worldBorderHit;
	mc_proto_varint sequence;
} mc_proto_69_play_toServer_packet_block_place;

typedef struct {
	mc_proto_varint hand;
	mc_proto_varint sequence;
	mc_proto_69_vec2f rotation;
} mc_proto_69_play_toServer_packet_use_item;

typedef struct {
	enum {
		mc_proto_69_play_toServer_packet_name_teleport_confirm = 0x00,
		mc_proto_69_play_toServer_packet_name_query_block_nbt = 0x01,
		mc_proto_69_play_toServer_packet_name_select_bundle_item = 0x02,
		mc_proto_69_play_toServer_packet_name_set_difficulty = 0x03,
		mc_proto_69_play_toServer_packet_name_message_acknowledgement = 0x04,
		mc_proto_69_play_toServer_packet_name_chat_command = 0x05,
		mc_proto_69_play_toServer_packet_name_chat_command_signed = 0x06,
		mc_proto_69_play_toServer_packet_name_chat_message = 0x07,
		mc_proto_69_play_toServer_packet_name_chat_session_update = 0x08,
		mc_proto_69_play_toServer_packet_name_chunk_batch_received = 0x09,
		mc_proto_69_play_toServer_packet_name_client_command = 0x0a,
		mc_proto_69_play_toServer_packet_name_tick_end = 0x0b,
		mc_proto_69_play_toServer_packet_name_settings = 0x0c,
		mc_proto_69_play_toServer_packet_name_tab_complete = 0x0d,
		mc_proto_69_play_toServer_packet_name_configuration_acknowledged = 0x0e,
		mc_proto_69_play_toServer_packet_name_enchant_item = 0x0f,
		mc_proto_69_play_toServer_packet_name_window_click = 0x10,
		mc_proto_69_play_toServer_packet_name_close_window = 0x11,
		mc_proto_69_play_toServer_packet_name_set_slot_state = 0x12,
		mc_proto_69_play_toServer_packet_name_cookie_response = 0x13,
		mc_proto_69_play_toServer_packet_name_custom_payload = 0x14,
		mc_proto_69_play_toServer_packet_name_debug_sample_subscription = 0x15,
		mc_proto_69_play_toServer_packet_name_edit_book = 0x16,
		mc_proto_69_play_toServer_packet_name_query_entity_nbt = 0x17,
		mc_proto_69_play_toServer_packet_name_use_entity = 0x18,
		mc_proto_69_play_toServer_packet_name_generate_structure = 0x19,
		mc_proto_69_play_toServer_packet_name_keep_alive = 0x1a,
		mc_proto_69_play_toServer_packet_name_lock_difficulty = 0x1b,
		mc_proto_69_play_toServer_packet_name_position = 0x1c,
		mc_proto_69_play_toServer_packet_name_position_look = 0x1d,
		mc_proto_69_play_toServer_packet_name_look = 0x1e,
		mc_proto_69_play_toServer_packet_name_flying = 0x1f,
		mc_proto_69_play_toServer_packet_name_vehicle_move = 0x20,
		mc_proto_69_play_toServer_packet_name_steer_boat = 0x21,
		mc_proto_69_play_toServer_packet_name_pick_item = 0x22,
		mc_proto_69_play_toServer_packet_name_ping_request = 0x23,
		mc_proto_69_play_toServer_packet_name_craft_recipe_request = 0x24,
		mc_proto_69_play_toServer_packet_name_abilities = 0x25,
		mc_proto_69_play_toServer_packet_name_block_dig = 0x26,
		mc_proto_69_play_toServer_packet_name_entity_action = 0x27,
		mc_proto_69_play_toServer_packet_name_player_input = 0x28,
		mc_proto_69_play_toServer_packet_name_pong = 0x29,
		mc_proto_69_play_toServer_packet_name_recipe_book = 0x2a,
		mc_proto_69_play_toServer_packet_name_displayed_recipe = 0x2b,
		mc_proto_69_play_toServer_packet_name_name_item = 0x2c,
		mc_proto_69_play_toServer_packet_name_resource_pack_receive = 0x2d,
		mc_proto_69_play_toServer_packet_name_advancement_tab = 0x2e,
		mc_proto_69_play_toServer_packet_name_select_trade = 0x2f,
		mc_proto_69_play_toServer_packet_name_set_beacon_effect = 0x30,
		mc_proto_69_play_toServer_packet_name_held_item_slot = 0x31,
		mc_proto_69_play_toServer_packet_name_update_command_block = 0x32,
		mc_proto_69_play_toServer_packet_name_update_command_block_minecart = 0x33,
		mc_proto_69_play_toServer_packet_name_set_creative_slot = 0x34,
		mc_proto_69_play_toServer_packet_name_update_jigsaw_block = 0x35,
		mc_proto_69_play_toServer_packet_name_update_structure_block = 0x36,
		mc_proto_69_play_toServer_packet_name_update_sign = 0x37,
		mc_proto_69_play_toServer_packet_name_arm_animation = 0x38,
		mc_proto_69_play_toServer_packet_name_spectate = 0x39,
		mc_proto_69_play_toServer_packet_name_block_place = 0x3a,
		mc_proto_69_play_toServer_packet_name_use_item = 0x3b,
	} name;
	union {
		mc_proto_69_packet_teleport_confirm teleport_confirm;
		mc_proto_69_packet_query_block_nbt query_block_nbt;
		mc_proto_69_packet_select_bundle_item select_bundle_item;
		mc_proto_69_packet_set_difficulty set_difficulty;
		mc_proto_69_packet_message_acknowledgement message_acknowledgement;
		mc_proto_69_packet_chat_command chat_command;
		mc_proto_69_packet_chat_command_signed chat_command_signed;
		mc_proto_69_packet_chat_message chat_message;
		mc_proto_69_packet_chat_session_update chat_session_update;
		mc_proto_69_packet_chunk_batch_received chunk_batch_received;
		mc_proto_69_packet_client_command client_command;
		mc_proto_69_packet_tick_end tick_end;
		mc_proto_69_packet_settings settings;
		mc_proto_69_packet_tab_complete tab_complete;
		mc_proto_69_packet_configuration_acknowledged configuration_acknowledged;
		mc_proto_69_packet_enchant_item enchant_item;
		mc_proto_69_packet_window_click window_click;
		mc_proto_69_packet_close_window close_window;
		mc_proto_69_packet_set_slot_state set_slot_state;
		mc_proto_69_packet_common_cookie_response cookie_response;
		mc_proto_69_packet_custom_payload custom_payload;
		mc_proto_69_packet_edit_book edit_book;
		mc_proto_69_packet_query_entity_nbt query_entity_nbt;
		mc_proto_69_packet_use_entity use_entity;
		mc_proto_69_packet_generate_structure generate_structure;
		mc_proto_69_packet_keep_alive keep_alive;
		mc_proto_69_packet_lock_difficulty lock_difficulty;
		mc_proto_69_packet_position position;
		mc_proto_69_packet_position_look position_look;
		mc_proto_69_packet_look look;
		mc_proto_69_packet_flying flying;
		mc_proto_69_packet_vehicle_move vehicle_move;
		mc_proto_69_packet_steer_boat steer_boat;
		mc_proto_69_packet_pick_item pick_item;
		mc_proto_69_packet_ping_request ping_request;
		mc_proto_69_packet_craft_recipe_request craft_recipe_request;
		mc_proto_69_packet_abilities abilities;
		mc_proto_69_packet_block_dig block_dig;
		mc_proto_69_packet_entity_action entity_action;
		mc_proto_69_packet_player_input player_input;
		mc_proto_69_packet_pong pong;
		mc_proto_69_packet_recipe_book recipe_book;
		mc_proto_69_packet_displayed_recipe displayed_recipe;
		mc_proto_69_packet_name_item name_item;
		mc_proto_69_packet_resource_pack_receive resource_pack_receive;
		mc_proto_69_packet_advancement_tab advancement_tab;
		mc_proto_69_packet_select_trade select_trade;
		mc_proto_69_packet_set_beacon_effect set_beacon_effect;
		mc_proto_69_packet_held_item_slot held_item_slot;
		mc_proto_69_packet_update_command_block update_command_block;
		mc_proto_69_packet_update_command_block_minecart update_command_block_minecart;
		mc_proto_69_packet_set_creative_slot set_creative_slot;
		mc_proto_69_packet_update_jigsaw_block update_jigsaw_block;
		mc_proto_69_packet_update_structure_block update_structure_block;
		mc_proto_69_packet_update_sign update_sign;
		mc_proto_69_packet_arm_animation arm_animation;
		mc_proto_69_packet_spectate spectate;
		mc_proto_69_packet_block_place block_place;
		mc_proto_69_packet_use_item use_item;
	} params;
} mc_proto_69_play_toServer_packet;
