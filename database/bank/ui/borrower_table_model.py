from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex


class BorrowerTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data or []
        self._headers = []
