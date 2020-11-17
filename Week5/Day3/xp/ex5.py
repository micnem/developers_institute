def how_old(seconds, planet):
    if planet == "Earth":
        return (seconds / 86400)/365.25
    elif planet == "Mercury":
        return (seconds / 86400)/(365.25 * 0.2408467)
    elif planet == "Venus":
        return (seconds / 86400)/(365.25 * 0.61519726)
    elif planet == "Mars":
        return (seconds / 86400)/(365.25 * 1.8808158)
    elif planet == "Jupiter":
        return (seconds / 86400)/(365.25 * 11.862615)
    elif planet == "Saturn":
        return (seconds / 86400)/(365.25 * 29.447498)
    elif planet == "Uranus":
        return (seconds / 86400)/(365.25 * 84.016846)
    elif planet == "Neptune":
        return (seconds / 86400)/(365.25 * 164.79132)

    
