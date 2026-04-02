from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import (
    Identifier, Country, ConsumerUnit, Ownership,
    Relationship, Characteristic, IdentifierCharacteristic, get_db
)

app = FastAPI(title="P&G Manufacturing API")



class IdentifierSchema(BaseModel):
    identifier_name: str
    description: Optional[str] = None
    identifier_type: Optional[str] = None

class CountrySchema(BaseModel):
    name: str
    iso_code: Optional[str] = None
    short_code: Optional[str] = None

class ConsumerUnitSchema(BaseModel):
    number_of_consumers: int
    country_name: str

class OwnershipSchema(BaseModel):
    identifier_name: str
    originator_first_name: Optional[str] = None
    originator_last_name: Optional[str] = None
    user_id_tnumber: str
    user_id_intranet: Optional[str] = None
    email: Optional[str] = None
    owner_first_name: Optional[str] = None
    owner_last_name: Optional[str] = None

class RelationshipSchema(BaseModel):
    from_identifier_name: str
    to_identifier_name: str
    relationship_name: Optional[str] = None

class CharacteristicSchema(BaseModel):
    master_name: str
    name: str
    specifics: Optional[str] = None
    action_required: Optional[str] = None
    report_type: Optional[str] = None
    data_type: Optional[str] = None
    lower_routine_release_limit: Optional[float] = None
    lower_limit: Optional[float] = None
    lower_target: Optional[float] = None
    target: Optional[float] = None
    upper_target: Optional[float] = None
    upper_limit: Optional[float] = None
    upper_routine_release_limit: Optional[float] = None
    test_frequency: Optional[int] = None
    precision: Optional[int] = None
    engineering_unit: Optional[str] = None

class IdentifierCharacteristicSchema(BaseModel):
    identifier_name: str
    master_name: str
    characteristic_name: str


@app.get("/")
def root():
    return {"message": "P&G Manufacturing API"}


@app.get("/identifiers")
def get_identifiers(db: Session = Depends(get_db)):
    return db.query(Identifier).all()


@app.get("/identifiers/{identifier_name}")
def get_identifier(identifier_name: str, db: Session = Depends(get_db)):
    identifier = db.query(Identifier).filter(Identifier.identifier_name == identifier_name).first()
    if not identifier:
        raise HTTPException(status_code=404, detail="Identifier not found")
    return identifier


@app.post("/identifiers")
def create_identifier(data: IdentifierSchema, db: Session = Depends(get_db)):
    existing = db.query(Identifier).filter(Identifier.identifier_name == data.identifier_name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Identifier already exists")
    item = Identifier(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.put("/identifiers/{identifier_name}")
def update_identifier(identifier_name: str, data: IdentifierSchema, db: Session = Depends(get_db)):
    item = db.query(Identifier).filter(Identifier.identifier_name == identifier_name).first()
    if not item:
        raise HTTPException(status_code=404, detail="Identifier not found")
    item.description = data.description
    item.identifier_type = data.identifier_type
    db.commit()
    db.refresh(item)
    return item


@app.delete("/identifiers/{identifier_name}")
def delete_identifier(identifier_name: str, db: Session = Depends(get_db)):
    item = db.query(Identifier).filter(Identifier.identifier_name == identifier_name).first()
    if not item:
        raise HTTPException(status_code=404, detail="Identifier not found")
    db.delete(item)
    db.commit()
    return {"message": "Identifier deleted"}



@app.get("/identifiers/{identifier_name}/characteristics")
def get_identifier_characteristics(identifier_name: str, db: Session = Depends(get_db)):
    identifier = db.query(Identifier).filter(Identifier.identifier_name == identifier_name).first()
    if not identifier:
        raise HTTPException(status_code=404, detail="Identifier not found")
    data = db.query(IdentifierCharacteristic).filter(
        IdentifierCharacteristic.identifier_name == identifier_name
    ).all()
    return data



@app.get("/countries")
def get_countries(db: Session = Depends(get_db)):
    return db.query(Country).all()


@app.get("/countries/{country_name}")
def get_country(country_name: str, db: Session = Depends(get_db)):
    country = db.query(Country).filter(Country.name == country_name).first()
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country


@app.post("/countries")
def create_country(data: CountrySchema, db: Session = Depends(get_db)):
    existing = db.query(Country).filter(Country.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Country already exists")
    item = Country(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.put("/countries/{country_name}")
def update_country(country_name: str, data: CountrySchema, db: Session = Depends(get_db)):
    item = db.query(Country).filter(Country.name == country_name).first()
    if not item:
        raise HTTPException(status_code=404, detail="Country not found")
    item.iso_code = data.iso_code
    item.short_code = data.short_code
    db.commit()
    db.refresh(item)
    return item


@app.delete("/countries/{country_name}")
def delete_country(country_name: str, db: Session = Depends(get_db)):
    item = db.query(Country).filter(Country.name == country_name).first()
    if not item:
        raise HTTPException(status_code=404, detail="Country not found")
    db.delete(item)
    db.commit()
    return {"message": "Country deleted"}



@app.get("/consumer_units")
def get_consumer_units(db: Session = Depends(get_db)):
    return db.query(ConsumerUnit).all()


@app.post("/consumer_units")
def create_consumer_unit(data: ConsumerUnitSchema, db: Session = Depends(get_db)):
    item = ConsumerUnit(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.delete("/consumer_units/{country_name}/{number_of_consumers}")
def delete_consumer_unit(country_name: str, number_of_consumers: int, db: Session = Depends(get_db)):
    item = db.query(ConsumerUnit).filter(
        ConsumerUnit.country_name == country_name,
        ConsumerUnit.number_of_consumers == number_of_consumers
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Consumer unit not found")
    db.delete(item)
    db.commit()
    return {"message": "Consumer unit deleted"}



@app.get("/ownership")
def get_ownership(db: Session = Depends(get_db)):
    return db.query(Ownership).all()


@app.get("/ownership/{identifier_name}")
def get_ownership_by_identifier(identifier_name: str, db: Session = Depends(get_db)):
    data = db.query(Ownership).filter(Ownership.identifier_name == identifier_name).all()
    if not data:
        raise HTTPException(status_code=404, detail="Ownership not found")
    return data


@app.post("/ownership")
def create_ownership(data: OwnershipSchema, db: Session = Depends(get_db)):
    item = Ownership(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.delete("/ownership/{identifier_name}/{user_id_tnumber}")
def delete_ownership(identifier_name: str, user_id_tnumber: str, db: Session = Depends(get_db)):
    item = db.query(Ownership).filter(
        Ownership.identifier_name == identifier_name,
        Ownership.user_id_tnumber == user_id_tnumber
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Ownership not found")
    db.delete(item)
    db.commit()
    return {"message": "Ownership deleted"}



@app.get("/relationships")
def get_relationships(db: Session = Depends(get_db)):
    return db.query(Relationship).all()


@app.post("/relationships")
def create_relationship(data: RelationshipSchema, db: Session = Depends(get_db)):
    item = Relationship(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.delete("/relationships/{from_id}/{to_id}")
def delete_relationship(from_id: str, to_id: str, db: Session = Depends(get_db)):
    item = db.query(Relationship).filter(
        Relationship.from_identifier_name == from_id,
        Relationship.to_identifier_name == to_id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Relationship not found")
    db.delete(item)
    db.commit()
    return {"message": "Relationship deleted"}



@app.get("/characteristics")
def get_characteristics(db: Session = Depends(get_db)):
    return db.query(Characteristic).all()


@app.post("/characteristics")
def create_characteristic(data: CharacteristicSchema, db: Session = Depends(get_db)):
    item = Characteristic(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.delete("/characteristics/{master_name}/{name}")
def delete_characteristic(master_name: str, name: str, db: Session = Depends(get_db)):
    item = db.query(Characteristic).filter(
        Characteristic.master_name == master_name,
        Characteristic.name == name
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Characteristic not found")
    db.delete(item)
    db.commit()
    return {"message": "Characteristic deleted"}



@app.get("/identifier_characteristics")
def get_all_identifier_characteristics(db: Session = Depends(get_db)):
    return db.query(IdentifierCharacteristic).all()


@app.post("/identifier_characteristics")
def create_identifier_characteristic(data: IdentifierCharacteristicSchema, db: Session = Depends(get_db)):
    item = IdentifierCharacteristic(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.delete("/identifier_characteristics/{identifier_name}/{master_name}/{characteristic_name}")
def delete_identifier_characteristic(identifier_name: str, master_name: str, characteristic_name: str, db: Session = Depends(get_db)):
    item = db.query(IdentifierCharacteristic).filter(
        IdentifierCharacteristic.identifier_name == identifier_name,
        IdentifierCharacteristic.master_name == master_name,
        IdentifierCharacteristic.characteristic_name == characteristic_name
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Identifier characteristic not found")
    db.delete(item)
    db.commit()
    return {"message": "Identifier characteristic deleted"}
