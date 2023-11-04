import wx
import math

PADDING = 5
GRID_PADDING = 40
STATIC_BOX_PADDING = 10
BUTTON_BORDER = 10


class ConverterUI(wx.Dialog):
    def __init__(self, cb_titles, title):
        super().__init__(None, title=title)
        self.cb_labels = cb_titles
        self.panel = wx.Panel(self)
        self.initUI()
        self.Centre()

    def initUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self._set_grid(vbox)
        border = wx.BoxSizer()
        border.Add(vbox, 1, wx.ALL | wx.EXPAND, PADDING)
        self.panel.SetSizer(border)
        self.panel.Fit()
        self.Fit()

    def _set_grid(self, vbox):
        n_cbs = len(self.cb_labels)
        n_col = int(math.sqrt(n_cbs))
        n_row = n_col
        while n_row * n_col < n_cbs:
            n_row += 1
        sb = wx.StaticBox(self.panel, wx.ID_ANY, 'Select tables:')
        sb_sizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        grid_sizer = wx.GridSizer(n_row, n_col, GRID_PADDING)

        for cb_label in self.cb_labels:
            cb = wx.CheckBox(self.panel, label=cb_label)
            grid_sizer.Add(cb, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND)
        sb_sizer.Add(grid_sizer, 1, wx.ALL | wx.CENTER, STATIC_BOX_PADDING)
        vbox.Add(sb_sizer, 1, wx.CENTER, 0)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        pt = font.GetPointSize()
        width_factor = len(max(self.cb_labels, key=len)) * n_col + (pt * (n_col - 1))
        width = (width_factor * pt)
        self.SetSize(width, wx.ID_ANY)

        convert_button = wx.Button(self.panel, label="Convert")
        convert_button.Bind(wx.EVT_BUTTON, self._on_convert)
        vbox.Add(convert_button, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=BUTTON_BORDER)

    def _on_convert(self, event):
        selected_tables = [checkbox.GetLabel() for checkbox in self.panel.GetChildren() if isinstance(checkbox, wx.CheckBox) and checkbox.GetValue()]
        if selected_tables:
            self.on_convert(selected_tables)
        else:
            wx.MessageBox("No tables selected!", "Error", wx.OK | wx.ICON_ERROR)

    def on_convert(self, selected_tables):
        pass
