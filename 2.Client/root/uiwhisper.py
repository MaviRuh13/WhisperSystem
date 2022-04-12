----------------#Find - Arat

import player

----------------#Add - Altýna Ekle

import systemSetting
if app.MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM:
	import uiwhispercolorpanel

----------------#Find - Arat

			self.gamemasterMark = GetObject("gamemastermark")

----------------#Add - Altýna Ekle

			if app.MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM:
				self.whispercolorButton = GetObject("whispercolorbutton")

----------------#Find - Arat

		self.acceptButton.SetEvent(ui.__mem_func__(self.AcceptTarget))

----------------#Add - Altýna Ekle

		if app.MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM:
			self.whispercolorButton.SetEvent(ui.__mem_func__(self.WhisperColorPanel))

----------------#Find - Arat

		self.resizeButton = None

----------------#Add - Altýna Ekle

		if app.MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM:
			self.whispercolorButton = None

----------------#Find - Arat

	def ResizeWhisperDialog(self):
		(xPos, yPos) = self.resizeButton.GetLocalPosition()
		if xPos < 280:
			self.resizeButton.SetPosition(280, yPos)
			return
		if yPos < 150:
			self.resizeButton.SetPosition(xPos, 150)
			return
		self.SetWhisperDialogSize(xPos + 20, yPos + 20)

----------------#Add - Altýna Ekle

	if app.MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM:
		def WhisperColorPanel(self):
			self.WhisperColor = uiwhispercolorpanel.WhisperColor() 
			self.WhisperColor.Show()

----------------#Find - Arat

	def OpenWithTarget(self, targetName):

----------------#Find in - Ýçinde Bul

		self.minimizeButton.Show()

----------------#Add - Altýna Ekle

		if app.MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM:
			self.whispercolorButton.Show()

----------------#Find - Arat

	def OpenWithoutTarget(self, event):

----------------#Find in - Ýçinde Bul

		self.gamemasterMark.Hide()

----------------#Add - Altýna Ekle

		if app.MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM:
			self.whispercolorButton.Hide()

----------------#Find - Arat

			net.SendWhisperPacket(self.targetName, text)

----------------#Change - Deðiþtir

			if app.MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM:
				if systemSetting.GetMaviRuhFisiltiRenkliYazi() == 0:
					net.SendWhisperPacket(self.targetName, text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 1:
					net.SendWhisperPacket(self.targetName, "|cff00ccff" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 2:
					net.SendWhisperPacket(self.targetName, "|cffff0000" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 3:
					net.SendWhisperPacket(self.targetName, "|cffffff00" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 4:
					net.SendWhisperPacket(self.targetName, "|cff00ff00" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 5:
					net.SendWhisperPacket(self.targetName, "|cffFF4500" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 6:
					net.SendWhisperPacket(self.targetName, "|cFF8000FF" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 7:
					net.SendWhisperPacket(self.targetName, "|cFFFF00FF" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 8:
					net.SendWhisperPacket(self.targetName, "|cFF000000" + text)
				else:
					net.SendWhisperPacket(self.targetName, text)
			else:
				net.SendWhisperPacket(self.targetName, text)

----------------#Find - Arat

			chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + text)

----------------#Change - Deðiþtir

			if app.MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM:
				if systemSetting.GetMaviRuhFisiltiRenkliYazi() == 0:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 1:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + "|cff00ccff" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 2:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + "|cffff0000" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 3:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + "|cffffff00" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 4:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + "|cff00ff00" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 5:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + "|cffFF4500" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 6:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + "|cFF8000FF" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 7:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + "|cFFFF00FF" + text)
				elif systemSetting.GetMaviRuhFisiltiRenkliYazi() == 8:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + "|cFF000000" + text)
				else:
					chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + text)
			else:
				chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + text)