//Find -- Arat
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

///Add -- Altına Ekle
#ifdef MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM
	PyModule_AddIntConstant(poModule, "MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM",	0);
#endif