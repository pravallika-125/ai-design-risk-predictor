from model import predict_risk

print("=== AI Design Risk Predictor ===")

length = int(input("Enter length: "))
load = int(input("Enter load: "))
material = input("Enter material (steel/aluminum): ")

result = predict_risk(length, load, material)

print("\nPredicted Risk Level:", result)

if result == "high":
    print("⚠️ High risk! Consider reducing load or changing material.")
elif result == "medium":
    print("⚠️ Moderate risk. Review design.")
else:
    print("✅ Safe design.")
