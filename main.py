import wx
import os
import data_handler
import converter
from ui_components import ConverterUI


class ConverterApp(ConverterUI):
    def on_convert(self, selected_tables):
        converter.converter(selected_tables)
        wx.MessageBox("Conversion complete!", "Info", wx.OK | wx.ICON_INFORMATION)


def main():
    app = wx.App()
    cb_titles = [table["Tables_in_" + os.environ.get('MYSQL_DB_NAME')] for table in data_handler.get_database_name()]

    dlg = ConverterApp(cb_titles, title='MySQL to CSV Converter by kvzsolt')
    dlg.ShowModal()
    dlg.Destroy()
    app.MainLoop()


if __name__ == "__main__":
    main()
