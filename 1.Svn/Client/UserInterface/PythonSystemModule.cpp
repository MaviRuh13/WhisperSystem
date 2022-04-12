//Find -- Arat
PyObject * systemIsShowSalesText(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonSystem::Instance().IsShowSalesText());
}

///Add -- Altına Ekle
#ifdef MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM
PyObject * systemSetMaviRuhFisiltiRenkliYazi(PyObject * poSelf, PyObject * poArgs){int level;if (!PyTuple_GetInteger(poArgs, 0, &level))return Py_BuildException();if (level >= 0)CPythonSystem::Instance().SetMaviRuhFisiltiRenkliYazi(level);return Py_BuildNone();}
PyObject * systemGetMaviRuhFisiltiRenkliYazi(PyObject * poSelf, PyObject * poArgs){return Py_BuildValue("i", CPythonSystem::Instance().GetMaviRuhFisiltiRenkliYazi());}
#endif

//Find -- Arat
		{ "IsShowSalesText",			systemIsShowSalesText,			METH_VARARGS },
	
///Add -- Altına Ekle
#ifdef MAVIRUH_WHISPER_COLOR_TEXT_SYSTEM
		{ "GetMaviRuhFisiltiRenkliYazi",		systemGetMaviRuhFisiltiRenkliYazi,		METH_VARARGS },
		{ "SetMaviRuhFisiltiRenkliYazi",		systemSetMaviRuhFisiltiRenkliYazi,		METH_VARARGS },
#endif