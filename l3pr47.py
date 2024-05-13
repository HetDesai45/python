stateCapital = {"AndhraPradesh":"Hyderabad", "Bihar":"Patna","Maharashtra":"Mumbai","Rajasthan":"Jaipur"}

print(stateCapital.get("Bihar"))
print(stateCapital.keys())
print(stateCapital.values())
print(stateCapital.items())
print(len(stateCapital))
print("Maharashtra" in stateCapital)
print(stateCapital.get("Assam"))
del stateCapital["Rajasthan"]
print(stateCapital)