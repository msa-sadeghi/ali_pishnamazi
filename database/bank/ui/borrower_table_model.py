from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex


class BorrowerTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data or []
        self._headers = [
            "ID",
            "national code",
            "first name",
            "last name",
            "father name",
            "birth date",
            "phone",
            "mobile",
            "address",
            "postal code",
        ]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):

        return len(self._headers)

    def update_data(self, new_data):
        self.beginResetModel()
        self._data = new_data
        self.endResetModel()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
