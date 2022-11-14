# Acá va el código para conectarse a la BD.

import mysql.connector
from mysql.connector import Error



class DAO:

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='123456',
                db='cordobares'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def leer_bares(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM bar ORDER BY nombre ASC")
                results = cursor.fetchall()
                return results
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def crear_bar(self, bar):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO bar (codigo, nombre, direccion) VALUES ('{0}', '{1}', {2})"
                cursor.execute(sql.format(bar[0], bar[1], bar[2]))
                self.connection.commit()
                print("¡Bar registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizar_bar(self, bar):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "UPDATE bar SET nombre = '{0}', direccion = {1} WHERE codigo = '{2}'"
                cursor.execute(sql.format(bar[1], bar[2], bar[0]))
                self.connection.commit()
                print("¡Bar actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminar_bar(self, codigo_bar):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM bar WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigo_bar))
                self.connection.commit()
                print("¡Bar eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))