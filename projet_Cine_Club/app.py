from PySide6 import QtWidgets, QtCore
from movie import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()
    


    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.le_insert_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.le_insert_movieTitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_removeMovies)

    def setup_connections(self):
        
        self.le_insert_movieTitle.returnPressed.connect(self.add_movie)
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)



    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        movieTitle = self.le_insert_movieTitle.text()
        if not movieTitle:
            return False
        
        movie = Movie(title=movieTitle)
        resultat = movie.add_to_movies()
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)
        
        self.le_insert_movieTitle.setText("")

        

    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()


        