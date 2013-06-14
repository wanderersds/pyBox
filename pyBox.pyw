#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
import mainform

def main():
  app = QtGui.QApplication(sys.argv)
  form = mainform.MainForm()
  form.show()
  app.exec()

if __name__ == "__main__":
  sys.exit(main()) 
