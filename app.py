from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit, QCompleter, QPushButton
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    # Override class constructor
    def __init__(self):
        # You must call the super class method
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(480, 80))         # Set sizes
        self.setWindowTitle('Line Edit IP Address') # Set the window title
        central_widget = QWidget(self)              # Create a central widget
        self.setCentralWidget(central_widget)       # Install the central widget

        grid_layout = QGridLayout(self)         # Create QGridLayout
        central_widget.setLayout(grid_layout)   # Set this accommodation in central widget

        grid_layout.addWidget(QLabel('Autocompletion check', self), 0, 0)
        grid_layout.addWidget(QPushButton('click'))
        

        # Create an input field
        lineEdit = QLineEdit(self)
        strList = ['git add',
                   'git commit',
                   'git remote',
                   'git status',
                   'git reset',
                   'git branch',
                   'git checkout',
                   'git clone',
                   'git pull',
                   'git rebase',
                   'git merge',
                   'git stash',
                   'git blame',
                   'git reset',
                   'git cherry-pick'
                   'git show',
                   'git diff',
                   ]    # Create a list of words
        # We create QCompleter, in which we establish the list, and also the pointer to the parent
        completer = QCompleter(strList, lineEdit)
        lineEdit.setCompleter(completer)        # Set QCompleter in the input field
        grid_layout.addWidget(lineEdit, 0, 1)   # Add the input field to the grid


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
