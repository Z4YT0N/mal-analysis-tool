#!/usr/bin/python3

import os
import sys
import getpass
import subprocess
import configparser
import shutil
import time
import json
import base64
import hashlib
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, 
                             QPushButton, QLabel, QFileDialog, QLineEdit, QTextEdit, 
                             QHBoxLayout, QGroupBox, QScrollArea, QSplitter, QStatusBar, 
                             QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox,
                             QDialog, QDialogButtonBox)
from PyQt5.QtCore import Qt, QProcess, pyqtSignal, QThread
from PyQt5.QtGui import QIcon, QPixmap, QFont

# Import custom style
from gui.style import get_stylesheet, get_palette

# Import app modules
from gui.home_tab import HomeTab
from gui.analyzer_tab import AnalyzerTab
from gui.utils_tab import UtilsTab
from gui.settings_tab import SettingsTab
from gui.dynamic_tab import DynamicTab
from gui.document_tab import DocumentTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qu1cksc0pe - Malware Analysis Tool")
        self.resize(1200, 800)
        
        # Set up environment variables and paths
        self.setup_environment()
        
        # Create the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Create main layout
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Create tab widget
        self.tabs = QTabWidget()
        
        # Add tabs
        self.home_tab = HomeTab(self)
        self.analyzer_tab = AnalyzerTab(self)
        self.dynamic_tab = DynamicTab(self)
        self.document_tab = DocumentTab(self)
        self.utils_tab = UtilsTab(self)
        self.settings_tab = SettingsTab(self)
        
        self.tabs.addTab(self.home_tab, "Home")
        self.tabs.addTab(self.analyzer_tab, "Static Analysis")
        self.tabs.addTab(self.dynamic_tab, "Dynamic Analysis")
        self.tabs.addTab(self.document_tab, "Document Analysis")
        self.tabs.addTab(self.utils_tab, "Utilities")
        self.tabs.addTab(self.settings_tab, "Settings")
        
        # Add tabs to main layout
        self.main_layout.addWidget(self.tabs)
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        # Apply style
        self.apply_style()

    def setup_environment(self):
        """Setup environment variables and paths"""
        self.username = getpass.getuser()
        self.home_dir = os.path.expanduser("~")
        
        # Path separator based on OS
        self.path_separator = "/"
        self.strings_param = "--all"
        if sys.platform == "win32":
            self.path_separator = "\\"
            self.strings_param = "-a"
        elif sys.platform == "darwin":
            self.strings_param = "-a"
        
        # Get python binary
        if shutil.which("python"):
            self.py_binary = "python"
        else:
            self.py_binary = "python3"
        
        # Get application path
        self.sc0pe_path = os.getcwd()
        
        # Create .path_handler file
        with open(".path_handler", "w") as path_handler:
            path_handler.write(self.sc0pe_path)
            
        # Colors for rich output
        self.infoS = "[bold cyan][[bold red]*[bold cyan]][white]"
        self.foundS = "[bold cyan][[bold red]+[bold cyan]][white]"
        self.errorS = "[bold cyan][[bold red]![bold cyan]][white]"

    def apply_style(self):
        """Apply custom style to the application"""
        # Set custom stylesheet
        self.setStyleSheet(get_stylesheet())
        
        # Set custom palette
        QApplication.setPalette(get_palette())

def main():
    app = QApplication(sys.argv)
    
    # Set application attributes for better UI rendering
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    # Create and show the main window
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 