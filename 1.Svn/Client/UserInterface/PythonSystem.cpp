///Find -- Arat
	m_Config.bShowSalesText		= true;

///Add -- Altına Ekle
#ifdef MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM
	m_Config.bMaviRuhFisiltiRenkliYazi	= 0;
#endif

///Find -- Arat
void CPythonSystem::SetShowSalesTextFlag(int iFlag)
{
	m_Config.bShowSalesText = iFlag == 1 ? true : false;
}
///Add -- Altına Ekle
#ifdef MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM
int CPythonSystem::GetMaviRuhFisiltiRenkliYazi(){return m_Config.bMaviRuhFisiltiRenkliYazi;}
void CPythonSystem::SetMaviRuhFisiltiRenkliYazi(unsigned int level){m_Config.bMaviRuhFisiltiRenkliYazi = MIN(level, 8);}
#endif

///Find -- Arat
		else if (!stricmp(command, "SHOW_SALESTEXT"))
			m_Config.bShowSalesText = atoi(value) == 1 ? true : false;

///Add -- Altına Ekle
#ifdef MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM
		else if (!stricmp(command, "MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM"))
			m_Config.bMaviRuhFisiltiRenkliYazi = atoi(value);
#endif

///Find -- Arat
	fprintf(fp, "SHADOW_LEVEL				%d\n", m_Config.iShadowLevel);

///Add -- Altına Ekle
#ifdef MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM
	fprintf(fp, "MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM	%d\n", m_Config.bMaviRuhFisiltiRenkliYazi);
#endif