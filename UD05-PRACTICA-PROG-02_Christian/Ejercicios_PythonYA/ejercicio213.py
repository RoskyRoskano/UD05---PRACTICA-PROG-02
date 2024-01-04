import wx
# Muestra un pop up con el mensaje "Hola mundo"
aplicacion = wx.App()
ventana = wx.Frame(parent=None,title="Hola Mundo")
ventana.Show()
aplicacion.MainLoop()