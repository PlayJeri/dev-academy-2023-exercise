from bike_app.models import Rides

def test_home(client):
    response = client.get("/")
    assert b"<title>Home</title>" in response.data


def test_rides(client):
    response = client.get("/rides/1")
    assert b"<td>Laajalahden aukio</td>" in response.data


def test_stations(client):
    response = client.get("/stations/1")
    assert b'<a href="/station/1">Hanasaari</a>' in response.data


def test_station(client):
    response = client.get("/station/30")
    
    # Tests correct station name
    assert b"<td>Kalevalantie</td>" in response.data 

    # Tests correct top5 stations
    assert b'''<li class="list-group-item d-flex justify-content-between align-items-center">
                      Tyynenmerenkatu
                      <span class="badge bg-danger rounded-pill">3264</span>
                    </li>''' in response.data


def test_search(client):
    response = client.post("search", data={"search": "kalevalantie"})
    assert b'<a href="/station/30">' in response.data


def test_search_redirect_to_stations(client):
    response = client.post("/search", data={"search": "notrealstation"}, follow_redirects=True)

    assert response.status_code == 200
    assert b'Station not found' in response.data



