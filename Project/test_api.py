from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from app import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def setup_module():
    Base.metadata.create_all(bind=engine)


def teardown_module():
    Base.metadata.drop_all(bind=engine)



def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "P&G Manufacturing API"}


# --- Identifiers ---

def test_get_identifiers_empty():
    response = client.get("/identifiers")
    assert response.status_code == 200
    assert response.json() == []


def test_get_identifier_not_found():
    response = client.get("/identifiers/99999")
    assert response.status_code == 404


def test_post_identifier():
    response = client.post("/identifiers", json={
        "identifier_name": "TEST001",
        "description": "Test Product",
        "identifier_type": "Test Part"
    })
    assert response.status_code == 200
    assert response.json()["identifier_name"] == "TEST001"


def test_post_identifier_duplicate():
    response = client.post("/identifiers", json={
        "identifier_name": "TEST001",
        "description": "Duplicate",
        "identifier_type": "Test Part"
    })
    assert response.status_code == 400


def test_get_identifier_after_post():
    response = client.get("/identifiers/TEST001")
    assert response.status_code == 200
    assert response.json()["description"] == "Test Product"


def test_put_identifier():
    response = client.put("/identifiers/TEST001", json={
        "identifier_name": "TEST001",
        "description": "Updated Product",
        "identifier_type": "Updated Part"
    })
    assert response.status_code == 200
    assert response.json()["description"] == "Updated Product"


def test_put_identifier_not_found():
    response = client.put("/identifiers/FAKE", json={
        "identifier_name": "FAKE",
        "description": "x",
        "identifier_type": "x"
    })
    assert response.status_code == 404


def test_delete_identifier():
    response = client.delete("/identifiers/TEST001")
    assert response.status_code == 200
    assert response.json()["message"] == "Identifier deleted"


def test_delete_identifier_not_found():
    response = client.delete("/identifiers/TEST001")
    assert response.status_code == 404


# --- Countries ---

def test_get_countries_empty():
    response = client.get("/countries")
    assert response.status_code == 200


def test_get_country_not_found():
    response = client.get("/countries/Atlantis")
    assert response.status_code == 404


def test_post_country():
    response = client.post("/countries", json={
        "name": "Romania",
        "iso_code": "RO",
        "short_code": "642"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Romania"


def test_post_country_duplicate():
    response = client.post("/countries", json={
        "name": "Romania",
        "iso_code": "RO",
        "short_code": "642"
    })
    assert response.status_code == 400


def test_get_country_after_post():
    response = client.get("/countries/Romania")
    assert response.status_code == 200
    assert response.json()["iso_code"] == "RO"


def test_put_country():
    response = client.put("/countries/Romania", json={
        "name": "Romania",
        "iso_code": "RO",
        "short_code": "999"
    })
    assert response.status_code == 200
    assert response.json()["short_code"] == "999"


def test_delete_country():
    response = client.delete("/countries/Romania")
    assert response.status_code == 200


def test_delete_country_not_found():
    response = client.delete("/countries/Atlantis")
    assert response.status_code == 404


# --- Consumer Units ---

def test_get_consumer_units_empty():
    response = client.get("/consumer_units")
    assert response.status_code == 200


def test_post_consumer_unit():
    client.post("/countries", json={"name": "TestCountry", "iso_code": "TC", "short_code": "001"})
    response = client.post("/consumer_units", json={
        "number_of_consumers": 100,
        "country_name": "TestCountry"
    })
    assert response.status_code == 200


def test_delete_consumer_unit():
    response = client.delete("/consumer_units/TestCountry/100")
    assert response.status_code == 200


# --- Ownership ---

def test_get_ownership_empty():
    response = client.get("/ownership")
    assert response.status_code == 200


def test_get_ownership_not_found():
    response = client.get("/ownership/99999")
    assert response.status_code == 404


def test_post_ownership():
    client.post("/identifiers", json={"identifier_name": "OWN001", "description": "Test", "identifier_type": "Test"})
    response = client.post("/ownership", json={
        "identifier_name": "OWN001",
        "originator_first_name": "Test",
        "originator_last_name": "User",
        "user_id_tnumber": "TU0001",
        "user_id_intranet": "test.u.1",
        "email": "test@example.com",
        "owner_first_name": "Test",
        "owner_last_name": "User"
    })
    assert response.status_code == 200


def test_get_ownership_after_post():
    response = client.get("/ownership/OWN001")
    assert response.status_code == 200
    assert response.json()[0]["email"] == "test@example.com"


def test_delete_ownership():
    response = client.delete("/ownership/OWN001/TU0001")
    assert response.status_code == 200


# --- Relationships ---

def test_get_relationships_empty():
    response = client.get("/relationships")
    assert response.status_code == 200


def test_post_relationship():
    client.post("/identifiers", json={"identifier_name": "REL001", "description": "A", "identifier_type": "T"})
    client.post("/identifiers", json={"identifier_name": "REL002", "description": "B", "identifier_type": "T"})
    response = client.post("/relationships", json={
        "from_identifier_name": "REL001",
        "to_identifier_name": "REL002",
        "relationship_name": "Contains"
    })
    assert response.status_code == 200


def test_delete_relationship():
    response = client.delete("/relationships/REL001/REL002")
    assert response.status_code == 200


# --- Characteristics ---

def test_get_characteristics_empty():
    response = client.get("/characteristics")
    assert response.status_code == 200


def test_post_characteristic():
    response = client.post("/characteristics", json={
        "master_name": "CM-TEST",
        "name": "Test Char",
        "specifics": "Test",
        "action_required": "CONTROL",
        "report_type": "VARIABLE",
        "data_type": "Decimal",
        "target": 5.0,
        "test_frequency": 1,
        "precision": 2,
        "engineering_unit": "ml"
    })
    assert response.status_code == 200


def test_delete_characteristic():
    response = client.delete("/characteristics/CM-TEST/Test Char")
    assert response.status_code == 200


# --- Identifier Characteristics ---

def test_get_identifier_characteristics_empty():
    response = client.get("/identifier_characteristics")
    assert response.status_code == 200


def test_get_identifier_characteristics_not_found():
    response = client.get("/identifiers/99999/characteristics")
    assert response.status_code == 404
