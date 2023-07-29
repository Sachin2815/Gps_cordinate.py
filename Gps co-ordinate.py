from geopy.geocoders import Nominatim

def get_address_from_coordinates(latitude, longitude):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True)
    return location.address if location else None

def get_coordinates_from_address(address):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude) if location else None

# Example usage
latitude_india = 20.5937  # Latitude of India
longitude_india = 78.9629  # Longitude of India

address = get_address_from_coordinates(latitude_india, longitude_india)
print(f"Address of India: {address}")

target_address = "city park jaipur, Rajasthan, India"  # Update the target address to "Jaipur, Rajasthan, India"
coordinates = get_coordinates_from_address(target_address)
if coordinates:
    latitude_wtp, longitude_wtp = coordinates
    print(f"Coordinates of Jaipur, Rajasthan: Latitude: {latitude_wtp}, Longitude: {longitude_wtp}")
else:
    print(f"Coordinates of Jaipur, Rajasthan not found.")
