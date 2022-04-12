import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"

TEMPORARY_X = +13
BUTTON_TEMPORARY_X = 5
PVP_X = -10

LINE_LABEL_X 	= 20
LINE_DATA_X 	= 90
LINE_STEP	= 0
SMALL_BUTTON_WIDTH 	= 45
MIDDLE_BUTTON_WIDTH 	= 65

window = {
	"name" : "WhisperColorDialog",
	"style" : ("movable", "float",),
	"x" : 0,
	"y" : 0,
	"width" : 450,
	"height" : 82,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"x" : 0,
			"y" : 0,
			"width" : 450,
			"height" : 82,
			"children" :
			(
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 8,
					"y" : 8,
					"width" : 435,
					"color" : "gray",
					"children" :
					(
						{ 
						"name":"titlename", "type":"text", "x":0, "y":3, 
						"horizontal_align":"center", "text_horizontal_align":"center",
						"text" : uiScriptLocale.WHISPER_COLOR_TITLE, 
						 },
					),
				},
				{
					"name" : "colortext_off_button",
					"type" : "radio_button",

					"x" : LINE_LABEL_X+SMALL_BUTTON_WIDTH*0,
					"y" : 40,

					"text" : uiScriptLocale.WHISPER_BUTTON_0,
					"tooltip_text" : uiScriptLocale.WHISPER_INFO,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "colortext_blue_button",
					"type" : "radio_button",

					"x" : LINE_LABEL_X+SMALL_BUTTON_WIDTH*1,
					"y" : 40,

					"text" : uiScriptLocale.WHISPER_BUTTON_1,
					"tooltip_text" : uiScriptLocale.WHISPER_INFO,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "colortext_red_button",
					"type" : "radio_button",

					"x" : LINE_LABEL_X+SMALL_BUTTON_WIDTH*2,
					"y" : 40,

					"text" : uiScriptLocale.WHISPER_BUTTON_2,
					"tooltip_text" : uiScriptLocale.WHISPER_INFO,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "colortext_yellow_button",
					"type" : "radio_button",

					"x" : LINE_LABEL_X+SMALL_BUTTON_WIDTH*3,
					"y" : 40,

					"text" : uiScriptLocale.WHISPER_BUTTON_3,
					"tooltip_text" : uiScriptLocale.WHISPER_INFO,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "colortext_green_button",
					"type" : "radio_button",

					"x" : LINE_LABEL_X+SMALL_BUTTON_WIDTH*4,
					"y" : 40,

					"text" : uiScriptLocale.WHISPER_BUTTON_4,
					"tooltip_text" : uiScriptLocale.WHISPER_INFO,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "colortext_orange_button",
					"type" : "radio_button",

					"x" : LINE_LABEL_X+SMALL_BUTTON_WIDTH*5,
					"y" : 40,

					"text" : uiScriptLocale.WHISPER_BUTTON_5,
					"tooltip_text" : uiScriptLocale.WHISPER_INFO,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "colortext_purple_button",
					"type" : "radio_button",

					"x" : LINE_LABEL_X+SMALL_BUTTON_WIDTH*6,
					"y" : 40,

					"text" : uiScriptLocale.WHISPER_BUTTON_6,
					"tooltip_text" : uiScriptLocale.WHISPER_INFO,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "colortext_pink_button",
					"type" : "radio_button",

					"x" : LINE_LABEL_X+SMALL_BUTTON_WIDTH*7,
					"y" : 40,

					"text" : uiScriptLocale.WHISPER_BUTTON_7,
					"tooltip_text" : uiScriptLocale.WHISPER_INFO,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "colortext_black_button",
					"type" : "radio_button",

					"x" : LINE_LABEL_X+SMALL_BUTTON_WIDTH*8,
					"y" : 40,

					"text" : uiScriptLocale.WHISPER_BUTTON_8,
					"tooltip_text" : uiScriptLocale.WHISPER_INFO,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
			),
		},
	),
}
