"""
Script for invoking pytest with options to select Qt library
"""

import sys
import pytest

args = sys.argv[1:]
if '--pyside' in args:
    args.remove('--pyside')
    import PySide
elif '--pyqt4' in args:
    args.remove('--pyqt4')
    import PyQt4
elif '--pyqt5' in args:
    args.remove('--pyqt5')
    import PyQt5
elif '--pyside2' in args:
    args.remove('--pyside2')
    import PySide2

import pyqtgraph as pg
pg.systemInfo()
qApp = pg.mkQApp()
desktop = qApp.desktop().screenGeometry()
print("\n\nDesktop Resolution: {} x {}\n\n".format(desktop.width(), desktop.height()))
pytest.main(args)
    
    