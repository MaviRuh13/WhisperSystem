import ui
import net
import chat
import player
import app
import localeInfo
import ime
import chr
import time
import constInfo
import systemSetting

class WhisperColor(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE SYSTEM OPTION DIALOG"

	def __Initialize(self):
		self.tilingMode = 0
		self.titleBar = 0
		self.showcolorTextButtonList = []

	def Destroy(self):
		self.ClearDictionary()
		self.__Initialize()
		print " -------------------------------------- DESTROY SYSTEM OPTION DIALOG"

	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("System.WhisperColor.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.showcolorTextButtonList.append(GetObject("colortext_off_button"))
			self.showcolorTextButtonList.append(GetObject("colortext_blue_button"))
			self.showcolorTextButtonList.append(GetObject("colortext_red_button"))
			self.showcolorTextButtonList.append(GetObject("colortext_yellow_button"))
			self.showcolorTextButtonList.append(GetObject("colortext_green_button"))
			self.showcolorTextButtonList.append(GetObject("colortext_orange_button"))
			self.showcolorTextButtonList.append(GetObject("colortext_purple_button"))
			self.showcolorTextButtonList.append(GetObject("colortext_pink_button"))
			self.showcolorTextButtonList.append(GetObject("colortext_black_button"))

		except:
			import exception
			exception.Abort("WhisperColor.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("uiscript/whispercolorpanel.py")
		self.__Load_BindObject()
		self.SetCenterPosition()
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.showcolorTextButtonList[0].SAFE_SetEvent(self.__OnClickColorTextOffButton)
		self.showcolorTextButtonList[1].SAFE_SetEvent(self.__OnClickColorTextBlueButton)
		self.showcolorTextButtonList[2].SAFE_SetEvent(self.__OnClickColorTextRedButton)
		self.showcolorTextButtonList[3].SAFE_SetEvent(self.__OnClickColorTextYellowButton)
		self.showcolorTextButtonList[4].SAFE_SetEvent(self.__OnClickColorTextGreenButton)
		self.showcolorTextButtonList[5].SAFE_SetEvent(self.__OnClickColorTextOrangeButton)
		self.showcolorTextButtonList[6].SAFE_SetEvent(self.__OnClickColorTextPurpleButton)
		self.showcolorTextButtonList[7].SAFE_SetEvent(self.__OnClickColorTextPinkButton)
		self.showcolorTextButtonList[8].SAFE_SetEvent(self.__OnClickColorTextBlackButton)

	def __OnClickColorTextOffButton(self):
		systemSetting.SetMaviRuhFisiltiRenkliYazi(0)
		self.RefreshColorText()

	def __OnClickColorTextBlueButton(self):
		systemSetting.SetMaviRuhFisiltiRenkliYazi(1)
		self.RefreshColorText()

	def __OnClickColorTextRedButton(self):
		systemSetting.SetMaviRuhFisiltiRenkliYazi(2)
		self.RefreshColorText()

	def __OnClickColorTextYellowButton(self):
		systemSetting.SetMaviRuhFisiltiRenkliYazi(3)
		self.RefreshColorText()

	def __OnClickColorTextGreenButton(self):
		systemSetting.SetMaviRuhFisiltiRenkliYazi(4)
		self.RefreshColorText()

	def __OnClickColorTextOrangeButton(self):
		systemSetting.SetMaviRuhFisiltiRenkliYazi(5)
		self.RefreshColorText()

	def __OnClickColorTextPurpleButton(self):
		systemSetting.SetMaviRuhFisiltiRenkliYazi(6)
		self.RefreshColorText()

	def __OnClickColorTextPinkButton(self):
		systemSetting.SetMaviRuhFisiltiRenkliYazi(7)
		self.RefreshColorText()

	def __OnClickColorTextBlackButton(self):
		systemSetting.SetMaviRuhFisiltiRenkliYazi(8)
		self.RefreshColorText()

	def RefreshColorText(self):
		if systemSetting.GetMaviRuhFisiltiRenkliYazi() == 0:
			self.showcolorTextButtonList[0].Down()
			self.showcolorTextButtonList[1].SetUp()
			self.showcolorTextButtonList[2].SetUp()
			self.showcolorTextButtonList[3].SetUp()
			self.showcolorTextButtonList[4].SetUp()
			self.showcolorTextButtonList[5].SetUp()
			self.showcolorTextButtonList[6].SetUp()
			self.showcolorTextButtonList[7].SetUp()
			self.showcolorTextButtonList[8].SetUp()
		elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 1:
			self.showcolorTextButtonList[0].SetUp()
			self.showcolorTextButtonList[1].Down()
			self.showcolorTextButtonList[2].SetUp()
			self.showcolorTextButtonList[3].SetUp()
			self.showcolorTextButtonList[4].SetUp()
			self.showcolorTextButtonList[5].SetUp()
			self.showcolorTextButtonList[6].SetUp()
			self.showcolorTextButtonList[7].SetUp()
			self.showcolorTextButtonList[8].SetUp()
		elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 2:
			self.showcolorTextButtonList[0].SetUp()
			self.showcolorTextButtonList[1].SetUp()
			self.showcolorTextButtonList[2].Down()
			self.showcolorTextButtonList[3].SetUp()
			self.showcolorTextButtonList[4].SetUp()
			self.showcolorTextButtonList[5].SetUp()
			self.showcolorTextButtonList[6].SetUp()
			self.showcolorTextButtonList[7].SetUp()
			self.showcolorTextButtonList[8].SetUp()
		elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 3:
			self.showcolorTextButtonList[0].SetUp()
			self.showcolorTextButtonList[1].SetUp()
			self.showcolorTextButtonList[2].SetUp()
			self.showcolorTextButtonList[3].Down()
			self.showcolorTextButtonList[4].SetUp()
			self.showcolorTextButtonList[5].SetUp()
			self.showcolorTextButtonList[6].SetUp()
			self.showcolorTextButtonList[7].SetUp()
			self.showcolorTextButtonList[8].SetUp()
		elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 4:
			self.showcolorTextButtonList[0].SetUp()
			self.showcolorTextButtonList[1].SetUp()
			self.showcolorTextButtonList[2].SetUp()
			self.showcolorTextButtonList[3].SetUp()
			self.showcolorTextButtonList[4].Down()
			self.showcolorTextButtonList[5].SetUp()
			self.showcolorTextButtonList[6].SetUp()
			self.showcolorTextButtonList[7].SetUp()
			self.showcolorTextButtonList[8].SetUp()
		elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 5:
			self.showcolorTextButtonList[0].SetUp()
			self.showcolorTextButtonList[1].SetUp()
			self.showcolorTextButtonList[2].SetUp()
			self.showcolorTextButtonList[3].SetUp()
			self.showcolorTextButtonList[4].SetUp()
			self.showcolorTextButtonList[5].Down()
			self.showcolorTextButtonList[6].SetUp()
			self.showcolorTextButtonList[7].SetUp()
			self.showcolorTextButtonList[8].SetUp()
		elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 6:
			self.showcolorTextButtonList[0].SetUp()
			self.showcolorTextButtonList[1].SetUp()
			self.showcolorTextButtonList[2].SetUp()
			self.showcolorTextButtonList[3].SetUp()
			self.showcolorTextButtonList[4].SetUp()
			self.showcolorTextButtonList[5].SetUp()
			self.showcolorTextButtonList[6].Down()
			self.showcolorTextButtonList[7].SetUp()
			self.showcolorTextButtonList[8].SetUp()
		elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 7:
			self.showcolorTextButtonList[0].SetUp()
			self.showcolorTextButtonList[1].SetUp()
			self.showcolorTextButtonList[2].SetUp()
			self.showcolorTextButtonList[3].SetUp()
			self.showcolorTextButtonList[4].SetUp()
			self.showcolorTextButtonList[5].SetUp()
			self.showcolorTextButtonList[6].SetUp()
			self.showcolorTextButtonList[7].Down()
			self.showcolorTextButtonList[8].SetUp()
		else:
			self.showcolorTextButtonList[0].SetUp()
			self.showcolorTextButtonList[1].SetUp()
			self.showcolorTextButtonList[2].SetUp()
			self.showcolorTextButtonList[3].SetUp()
			self.showcolorTextButtonList[4].SetUp()
			self.showcolorTextButtonList[5].SetUp()
			self.showcolorTextButtonList[6].SetUp()
			self.showcolorTextButtonList[7].SetUp()
			self.showcolorTextButtonList[8].Down()

	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return True

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True
	
	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()

	def __NotifyChatLine(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, text)
