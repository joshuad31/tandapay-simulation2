from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QMessageBox


class TimerMessageBox(QMessageBox):

    def __init__(self, timeout=None, parent=None):
        super(TimerMessageBox, self).__init__(parent)
        self.setWindowTitle("TandaPay Simulation")
        if timeout is not None:
            self.timer = QTimer(self)
            self.timer.setInterval(timeout * 1000)
            self.timer.timeout.connect(self._on_timeout)
            self.timer.start()

    def _on_timeout(self):
        self.timer.stop()
        self.close()

    def closeEvent(self, event):
        if hasattr(self, 'timer'):
            self.timer.stop()
        event.accept()


def show_message(msg, msg_type='Information', auto_close_time=None):
    """
    :param auto_close_time:
    :param msg:
    :param msg_type: Information/Warning/Critical/Question
    :return:
    """
    m = TimerMessageBox(timeout=auto_close_time)
    m.setIcon(getattr(m.Icon, msg_type) if hasattr(m.Icon, msg_type) else m.Icon.NoIcon)
    m.setText(msg)
    m.exec_()
