import sqlite3

from src.dto.request_property import RequestProperty
from src.dto.response_property import ResponseProperty, ResponseLocation, ResponseAddress


class PropertyRepository:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS address (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            street VARCHAR NOT NULL,
            number INTEGER NOT NULL,
            floor INTEGER,
            apartment VARCHAR,
            zip_code VARCHAR NOT NULL,
            locality VARCHAR NOT NULL,
            country VARCHAR NOT NULL
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS location (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude FLOAT NOT NULL,
            longitude FLOAT NOT NULL
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS property (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            address_id INTEGER NOT NULL,
            location_id INTEGER NOT NULL,
            price INTEGER NOT NULL,
            FOREIGN KEY (address_id) REFERENCES address (id),
            FOREIGN KEY (location_id) REFERENCES location0 (id)
        )
        """)
        self.conn.commit()

    def get_property(self, property_id):
        self.cursor.execute("SELECT * FROM property WHERE id = ?", (property_id,))
        row = self.cursor.fetchone()
        if row:
            self.cursor.execute("SELECT * FROM address WHERE id = ?", (row[1],))
            address_row = self.cursor.fetchone()
            address = ResponseAddress(id=address_row[0], street=address_row[1], number=address_row[2],
                                      floor=address_row[3],
                                      apartment=address_row[4], zip_code=address_row[5], locality=address_row[6],
                                      country=address_row[7])

            self.cursor.execute("SELECT * FROM location WHERE id = ?", (row[2],))
            location_row = self.cursor.fetchone()
            location = ResponseLocation(id=location_row[0], latitude=location_row[1], longitude=location_row[2])

            return ResponseProperty(id=row[0], address=address, location=location, price=row[3])
        else:
            return "Not found"

    def create_property(self, property: RequestProperty):
        # TODO Refactor: antes de querer crearlo chequear si existe
        self.cursor.execute("INSERT INTO address (street, number, floor, apartment, zip_code, locality, country) "
                            "VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (property.address.street, property.address.number, property.address.floor,
                             property.address.apartment,
                             property.address.zip_code, property.address.locality, property.address.country))
        self.conn.commit()
        address_id = self.cursor.lastrowid

        self.cursor.execute("INSERT INTO location (latitude, longitude) VALUES (?, ?)",
                            (property.location.latitude, property.location.longitude))
        self.conn.commit()
        location_id = self.cursor.lastrowid

        self.cursor.execute("INSERT INTO property (address_id, location_id, price) VALUES (?, ?, ?)",
                            (address_id, location_id, property.price))
        self.conn.commit()
        row_id = self.cursor.lastrowid

        if row_id:
            return f"Property with propertyId {row_id} is created"
        else:
            return "Not created"

    def update_property(self, property: RequestProperty, property_id: str):
        property_obtain = self.get_property(property_id)
        if property_obtain == "Not found":
            return "Not found"

        self.cursor.execute("UPDATE address SET street = ?, number = ?, floor = ?, "
                            "apartment = ?, zip_code = ?, locality = ?, country = ? WHERE id = ?",
                            (property.address.street, property.address.number, property.address.floor,
                             property.address.apartment,
                             property.address.zip_code, property.address.locality, property.address.country,
                             property_obtain.address.id))
        self.conn.commit()

        self.cursor.execute("UPDATE location SET latitude = ?, longitude = ? WHERE id = ?",
                            (property.location.latitude, property.location.longitude, property_obtain.location.id))
        self.conn.commit()

        self.cursor.execute("UPDATE property SET price = ? WHERE id = ?",
                            (property.price, property_id))
        self.conn.commit()

        rowcount = self.cursor.rowcount

        if rowcount != 0:
            return f"Property with propertyId {property_id} is updated"
        else:
            return "Not updated"

    def delete_property(self, property_id):

        property = self.get_property(property_id)

        self.cursor.execute("DELETE FROM address WHERE id = ?", (property.address.id,))
        self.conn.commit()

        self.cursor.execute("DELETE FROM location WHERE id = ?", (property.location.id,))
        self.conn.commit()

        self.cursor.execute("DELETE FROM property WHERE id = ?", (property_id,))
        self.conn.commit()

        rowcount = self.cursor.rowcount

        if rowcount != 0:
            return f"Property with propertyId {property_id} is deleted"
        else:
            return "Not deleted"

    def close_connection(self):
        self.conn.close()
