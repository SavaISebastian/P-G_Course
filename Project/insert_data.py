from sqlalchemy.orm import Session
from database import (
    engine, SessionLocal, Base, create_tables,
    Identifier, Country, ConsumerUnit, Ownership,
    Relationship, Characteristic, IdentifierCharacteristic
)


def insert_data():
    create_tables()
    db = SessionLocal()

    try:
        identifiers = [
            Identifier(identifier_name='88823141', description='Shampoo Product', identifier_type='Finished Product Part'),
            Identifier(identifier_name='88823142', description='Packaging Carton', identifier_type='Packaging Material Part'),
            Identifier(identifier_name='88823143', description='Packaging Box', identifier_type='Packaging Material Part'),
            Identifier(identifier_name='88823144', description='Chemical Substance', identifier_type='Assembled Product Part'),
            Identifier(identifier_name='88823145', description='Water', identifier_type='Assembled Product Part'),
            Identifier(identifier_name='88823146', description='Shampoo Bottle', identifier_type='Material Part'),
        ]
        for item in identifiers:
            db.merge(item)
        db.commit()

        countries = [
            Country(name='Luxembourg', iso_code='LU', short_code='442'),
            Country(name='France', iso_code='FR', short_code='250'),
            Country(name='Germany', iso_code='DE', short_code='276'),
            Country(name='Belgium', iso_code='BE', short_code='056'),
            Country(name='Netherlands', iso_code='NL', short_code='528'),
            Country(name='Sweden', iso_code='SE', short_code='752'),
            Country(name='Norway', iso_code='NO', short_code='578'),
        ]
        for item in countries:
            db.merge(item)
        db.commit()

        consumer_units = [
            ConsumerUnit(number_of_consumers=150, country_name='Luxembourg'),
            ConsumerUnit(number_of_consumers=200, country_name='France'),
            ConsumerUnit(number_of_consumers=100, country_name='Germany'),
            ConsumerUnit(number_of_consumers=120, country_name='Belgium'),
            ConsumerUnit(number_of_consumers=80, country_name='Netherlands'),
            ConsumerUnit(number_of_consumers=60, country_name='Sweden'),
            ConsumerUnit(number_of_consumers=90, country_name='Norway'),
        ]
        for item in consumer_units:
            db.merge(item)
        db.commit()

        ownerships = [
            Ownership(identifier_name='88823141', originator_first_name='Andrea', originator_last_name='Meier',
                      user_id_tnumber='AP5065', user_id_intranet='meier.a.1', email='andrea@example.com',
                      owner_first_name='Andrea', owner_last_name='Meier'),
            Ownership(identifier_name='88823142', originator_first_name='John', originator_last_name='Doe',
                      user_id_tnumber='JD1234', user_id_intranet='doe.j.1', email='john@example.com',
                      owner_first_name='John', owner_last_name='Doe'),
            Ownership(identifier_name='88823143', originator_first_name='Jane', originator_last_name='Smith',
                      user_id_tnumber='JS5678', user_id_intranet='smith.j.2', email='jane@example.com',
                      owner_first_name='Jane', owner_last_name='Smith'),
            Ownership(identifier_name='88823144', originator_first_name='Michael', originator_last_name='Brown',
                      user_id_tnumber='MB9101', user_id_intranet='brown.m.3', email='michael@example.com',
                      owner_first_name='Michael', owner_last_name='Brown'),
            Ownership(identifier_name='88823145', originator_first_name='Emily', originator_last_name='Davis',
                      user_id_tnumber='ED1123', user_id_intranet='davis.e.4', email='emily@example.com',
                      owner_first_name='Emily', owner_last_name='Davis'),
            Ownership(identifier_name='88823146', originator_first_name='David', originator_last_name='Wilson',
                      user_id_tnumber='DW1456', user_id_intranet='wilson.d.5', email='david@example.com',
                      owner_first_name='David', owner_last_name='Wilson'),
        ]
        for item in ownerships:
            db.merge(item)
        db.commit()

        relationships = [
            Relationship(from_identifier_name='88823141', to_identifier_name='88823142', relationship_name='Contains'),
            Relationship(from_identifier_name='88823141', to_identifier_name='88823143', relationship_name='Contains'),
            Relationship(from_identifier_name='88823141', to_identifier_name='88823144', relationship_name='Contains'),
            Relationship(from_identifier_name='88823141', to_identifier_name='88823145', relationship_name='Contains'),
            Relationship(from_identifier_name='88823141', to_identifier_name='88823146', relationship_name='Contains'),
        ]
        for item in relationships:
            db.merge(item)
        db.commit()

        characteristics = [
            Characteristic(master_name='CM-10001', name='Volume', specifics='Shampoo Bottle Volume', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=490.0, lower_limit=490.0, lower_target=500.0, target=505.0, upper_target=510.0, upper_limit=520.0, upper_routine_release_limit=520.0, test_frequency=1, precision=2, engineering_unit='ml'),
            Characteristic(master_name='CM-10002', name='pH Level', specifics='Shampoo pH Level', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=4.0, lower_limit=4.0, lower_target=5.0, target=5.5, upper_target=6.0, upper_limit=7.0, upper_routine_release_limit=7.0, test_frequency=1, precision=2, engineering_unit='pH'),
            Characteristic(master_name='CM-10003', name='Viscosity', specifics='Shampoo Viscosity', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=10.0, lower_limit=10.0, lower_target=15.0, target=20.0, upper_target=25.0, upper_limit=30.0, upper_routine_release_limit=30.0, test_frequency=1, precision=2, engineering_unit='Pa.s'),
            Characteristic(master_name='CM-10004', name='Color', specifics='Shampoo Color', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
            Characteristic(master_name='CM-10005', name='Fragrance', specifics='Shampoo Fragrance', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
            Characteristic(master_name='CM-10006', name='Foam Height', specifics='Shampoo Foam Height', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=10.0, lower_limit=10.0, lower_target=15.0, target=20.0, upper_target=25.0, upper_limit=30.0, upper_routine_release_limit=30.0, test_frequency=1, precision=2, engineering_unit='cm'),
            Characteristic(master_name='CM-10007', name='Density', specifics='Shampoo Density', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=0.9, lower_limit=0.9, lower_target=1.0, target=1.1, upper_target=1.2, upper_limit=1.3, upper_routine_release_limit=1.3, test_frequency=1, precision=3, engineering_unit='g/cm^3'),
            Characteristic(master_name='CM-10008', name='Ingredient A Concentration', specifics='Concentration of Ingredient A', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=0.5, lower_limit=0.5, lower_target=1.0, target=1.5, upper_target=2.0, upper_limit=2.5, upper_routine_release_limit=2.5, test_frequency=1, precision=2, engineering_unit='%'),
            Characteristic(master_name='CM-10009', name='Ingredient B Concentration', specifics='Concentration of Ingredient B', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=1.0, lower_limit=1.0, lower_target=1.5, target=2.0, upper_target=2.5, upper_limit=3.0, upper_routine_release_limit=3.0, test_frequency=1, precision=2, engineering_unit='%'),
            Characteristic(master_name='CM-10010', name='Shelf Life', specifics='Shelf Life of Shampoo', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=12.0, lower_limit=12.0, lower_target=18.0, target=24.0, upper_target=30.0, upper_limit=36.0, upper_routine_release_limit=36.0, test_frequency=1, precision=1, engineering_unit='months'),
            Characteristic(master_name='CM-20001', name='Carton Thickness', specifics='Thickness of Carton', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=1.0, lower_limit=1.0, lower_target=1.5, target=2.0, upper_target=2.5, upper_limit=3.0, upper_routine_release_limit=3.0, test_frequency=1, precision=2, engineering_unit='mm'),
            Characteristic(master_name='CM-20002', name='Carton Weight', specifics='Weight of Carton', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=50.0, lower_limit=50.0, lower_target=55.0, target=60.0, upper_target=65.0, upper_limit=70.0, upper_routine_release_limit=70.0, test_frequency=1, precision=1, engineering_unit='g'),
            Characteristic(master_name='CM-20003', name='Carton Dimensions', specifics='Dimensions of Carton', action_required='CONTROL', report_type='VARIABLE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
            Characteristic(master_name='CM-20004', name='Carton Material', specifics='Material of Carton', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
            Characteristic(master_name='CM-20005', name='Carton Color', specifics='Color of Carton', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
            Characteristic(master_name='CM-30001', name='Box Thickness', specifics='Thickness of Box', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=2.0, lower_limit=2.0, lower_target=2.5, target=3.0, upper_target=3.5, upper_limit=4.0, upper_routine_release_limit=4.0, test_frequency=1, precision=2, engineering_unit='mm'),
            Characteristic(master_name='CM-30002', name='Box Weight', specifics='Weight of Box', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=100.0, lower_limit=100.0, lower_target=110.0, target=120.0, upper_target=130.0, upper_limit=140.0, upper_routine_release_limit=140.0, test_frequency=1, precision=1, engineering_unit='g'),
            Characteristic(master_name='CM-30003', name='Box Dimensions', specifics='Dimensions of Box', action_required='CONTROL', report_type='VARIABLE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
            Characteristic(master_name='CM-30004', name='Box Material', specifics='Material of Box', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
            Characteristic(master_name='CM-30005', name='Box Color', specifics='Color of Box', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
            Characteristic(master_name='CM-40001', name='Chemical Purity', specifics='Purity of Chemical Substance', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=95.0, lower_limit=95.0, lower_target=97.0, target=98.0, upper_target=99.0, upper_limit=100.0, upper_routine_release_limit=100.0, test_frequency=1, precision=1, engineering_unit='%'),
            Characteristic(master_name='CM-40002', name='Chemical Concentration', specifics='Concentration of Chemical Substance', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=10.0, lower_limit=10.0, lower_target=15.0, target=20.0, upper_target=25.0, upper_limit=30.0, upper_routine_release_limit=30.0, test_frequency=1, precision=1, engineering_unit='%'),
            Characteristic(master_name='CM-40003', name='Chemical pH', specifics='pH of Chemical Substance', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=2.0, lower_limit=2.0, lower_target=3.0, target=4.0, upper_target=5.0, upper_limit=6.0, upper_routine_release_limit=6.0, test_frequency=1, precision=2, engineering_unit='pH'),
            Characteristic(master_name='CM-40004', name='Chemical Viscosity', specifics='Viscosity of Chemical Substance', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=5.0, lower_limit=5.0, lower_target=10.0, target=15.0, upper_target=20.0, upper_limit=25.0, upper_routine_release_limit=25.0, test_frequency=1, precision=2, engineering_unit='Pa.s'),
            Characteristic(master_name='CM-40005', name='Chemical Color', specifics='Color of Chemical Substance', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
            Characteristic(master_name='CM-50002', name='Water pH', specifics='pH of Water', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=6.5, lower_limit=6.5, lower_target=7.0, target=7.5, upper_target=8.0, upper_limit=8.5, upper_routine_release_limit=8.5, test_frequency=1, precision=2, engineering_unit='pH'),
            Characteristic(master_name='CM-50003', name='Water Conductivity', specifics='Conductivity of Water', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=0.0, lower_limit=0.0, lower_target=0.1, target=0.2, upper_target=0.3, upper_limit=0.5, upper_routine_release_limit=0.5, test_frequency=1, precision=3, engineering_unit='uS/cm'),
            Characteristic(master_name='CM-50004', name='Water Hardness', specifics='Hardness of Water', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=0.0, lower_limit=0.0, lower_target=1.0, target=2.0, upper_target=3.0, upper_limit=4.0, upper_routine_release_limit=4.0, test_frequency=1, precision=1, engineering_unit='dH'),
            Characteristic(master_name='CM-50005', name='Water Color', specifics='Color of Water', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
            Characteristic(master_name='CM-60001', name='Bottle Volume', specifics='Capacity of Shampoo Bottle', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=490.0, lower_limit=490.0, lower_target=500.0, target=505.0, upper_target=510.0, upper_limit=520.0, upper_routine_release_limit=520.0, test_frequency=1, precision=2, engineering_unit='ml'),
            Characteristic(master_name='CM-60002', name='Bottle Weight', specifics='Weight of Shampoo Bottle', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=30.0, lower_limit=30.0, lower_target=35.0, target=40.0, upper_target=45.0, upper_limit=50.0, upper_routine_release_limit=50.0, test_frequency=1, precision=1, engineering_unit='g'),
            Characteristic(master_name='CM-60003', name='Bottle Height', specifics='Height of Shampoo Bottle', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=180.0, lower_limit=180.0, lower_target=185.0, target=190.0, upper_target=195.0, upper_limit=200.0, upper_routine_release_limit=200.0, test_frequency=1, precision=1, engineering_unit='mm'),
            Characteristic(master_name='CM-60004', name='Bottle Diameter', specifics='Diameter of Shampoo Bottle', action_required='CONTROL', report_type='VARIABLE', data_type='Decimal', lower_routine_release_limit=50.0, lower_limit=50.0, lower_target=55.0, target=60.0, upper_target=65.0, upper_limit=70.0, upper_routine_release_limit=70.0, test_frequency=1, precision=1, engineering_unit='mm'),
            Characteristic(master_name='CM-60005', name='Bottle Material', specifics='Material of Shampoo Bottle', action_required='INSPECT', report_type='ATTRIBUTE', data_type='String', test_frequency=1, precision=0, engineering_unit=''),
        ]
        for item in characteristics:
            db.merge(item)
        db.commit()

        id_chars = [
            IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10001', characteristic_name='Volume'),
            IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10002', characteristic_name='pH Level'),
            IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10003', characteristic_name='Viscosity'),
            IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10004', characteristic_name='Color'),
            IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10005', characteristic_name='Fragrance'),
            IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10006', characteristic_name='Foam Height'),
            IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10007', characteristic_name='Density'),
            IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10008', characteristic_name='Ingredient A Concentration'),
            IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10009', characteristic_name='Ingredient B Concentration'),
            IdentifierCharacteristic(identifier_name='88823141', master_name='CM-10010', characteristic_name='Shelf Life'),
            IdentifierCharacteristic(identifier_name='88823142', master_name='CM-20001', characteristic_name='Carton Thickness'),
            IdentifierCharacteristic(identifier_name='88823142', master_name='CM-20002', characteristic_name='Carton Weight'),
            IdentifierCharacteristic(identifier_name='88823142', master_name='CM-20003', characteristic_name='Carton Dimensions'),
            IdentifierCharacteristic(identifier_name='88823142', master_name='CM-20004', characteristic_name='Carton Material'),
            IdentifierCharacteristic(identifier_name='88823142', master_name='CM-20005', characteristic_name='Carton Color'),
            IdentifierCharacteristic(identifier_name='88823143', master_name='CM-30001', characteristic_name='Box Thickness'),
            IdentifierCharacteristic(identifier_name='88823143', master_name='CM-30002', characteristic_name='Box Weight'),
            IdentifierCharacteristic(identifier_name='88823143', master_name='CM-30003', characteristic_name='Box Dimensions'),
            IdentifierCharacteristic(identifier_name='88823143', master_name='CM-30004', characteristic_name='Box Material'),
            IdentifierCharacteristic(identifier_name='88823143', master_name='CM-30005', characteristic_name='Box Color'),
            IdentifierCharacteristic(identifier_name='88823144', master_name='CM-40001', characteristic_name='Chemical Purity'),
            IdentifierCharacteristic(identifier_name='88823144', master_name='CM-40002', characteristic_name='Chemical Concentration'),
            IdentifierCharacteristic(identifier_name='88823144', master_name='CM-40003', characteristic_name='Chemical pH'),
            IdentifierCharacteristic(identifier_name='88823144', master_name='CM-40004', characteristic_name='Chemical Viscosity'),
            IdentifierCharacteristic(identifier_name='88823144', master_name='CM-40005', characteristic_name='Chemical Color'),
            IdentifierCharacteristic(identifier_name='88823145', master_name='CM-50002', characteristic_name='Water pH'),
            IdentifierCharacteristic(identifier_name='88823145', master_name='CM-50003', characteristic_name='Water Conductivity'),
            IdentifierCharacteristic(identifier_name='88823145', master_name='CM-50004', characteristic_name='Water Hardness'),
            IdentifierCharacteristic(identifier_name='88823145', master_name='CM-50005', characteristic_name='Water Color'),
            IdentifierCharacteristic(identifier_name='88823146', master_name='CM-60001', characteristic_name='Bottle Volume'),
            IdentifierCharacteristic(identifier_name='88823146', master_name='CM-60002', characteristic_name='Bottle Weight'),
            IdentifierCharacteristic(identifier_name='88823146', master_name='CM-60003', characteristic_name='Bottle Height'),
            IdentifierCharacteristic(identifier_name='88823146', master_name='CM-60004', characteristic_name='Bottle Diameter'),
            IdentifierCharacteristic(identifier_name='88823146', master_name='CM-60005', characteristic_name='Bottle Material'),
        ]
        for item in id_chars:
            db.merge(item)
        db.commit()

        print("All data inserted successfully!")

    except Exception as e:
        db.rollback()
        print(f"Error inserting data: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    insert_data()
