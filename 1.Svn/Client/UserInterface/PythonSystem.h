//Find -- Arat
			bool			bShowSalesText;
			
///Add -- Altına Ekle
#ifdef MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM
			int				bMaviRuhFisiltiRenkliYazi;
#endif

//Find -- Arat
		void							SetShowSalesTextFlag(int iFlag);
		
///Add -- Altına Ekle
#ifdef MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM
		void							SetMaviRuhFisiltiRenkliYazi(unsigned int level);
		int								GetMaviRuhFisiltiRenkliYazi();
#endif