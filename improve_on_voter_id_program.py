# ======is program ko likhne mai 30min ka time laga !
def validate_voter_data(name, age):
   
    if len(name.strip()) == 0:
        raise ValueError("नाम खाली नहीं छोड़ा जा सकता!")
        
    
    if age <= 0:
        raise ValueError("अमान्य उम्र! उम्र 0 या माइनस में नहीं हो सकती।")
    if age < 18:
        raise ValueError("आपकी उम्र 18 से कम है, आप अभी वोट नहीं दे सकते।")
    if age > 120:
        raise ValueError("अमान्य उम्र! इंसान की उम्र 120 से ज्यादा नहीं हो सकती।")

    print(f"\n🎉 बधाई हो {name}! आप वोट डालने के लिए पूरी तरह पात्र (Eligible) हैं। 🗳️")

while True:
    try:
        voter_name = input("\nअपना नाम दर्ज करें: ")
        voter_age = int(input("अपनी उम्र (Age) दर्ज करें: "))
        
       
        validate_voter_data(voter_name, voter_age)
        break 

    except ValueError as error:
        print(f"❌ गड़बड़: {error}")
        print("कृपया दोबारा सही जानकारी भरें।")

print("\n[वोटिंग प्रक्रिया सुरक्षित समाप्त हुई।]")
