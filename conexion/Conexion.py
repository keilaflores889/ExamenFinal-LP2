import psycopg2
class Conexion:

    """Metodo contructor de la materia
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=examenfinalbd user=postgres host=localhost password=12345678")
        
        """getConexion

            retorna la instancia de la base de datos
        """
    def getConexion(self):
        return self.con 