import datetime
import streamlit as st # type: ignore
import base64
# Function to encode the local image to Base64
def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return encoded

# Path to your local image file
image_path = "/Users/heinhtetarkarmg/ai-baydin-name-generator/resources/img/bg.jpeg"  # Replace with your local image path
img_base64 = get_base64_image(image_path)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Example Streamlit elements
st.title("AI Baydin")
d = st.date_input(
    "မွေးနေ့ ရွေးချယ်ပါ",
    datetime.date(1990, 1, 1),
    min_value=datetime.date(1920, 1, 1),
    max_value=datetime.date(2010, 12, 31)
)
st.write("ရွေးချယ်ထားသည့် မွေးနေ့ - ", d)
business = st.selectbox(
    "လုပ်ငန်းအမျိုးအစား ရွေးချယ်ပါ",
    ("စားသောက်ကုန်", 
"ဆေးဝါး", 
"စက်ပစ္စည်း (ကား၊ ကွန်ပြူတာ ၊ စက်ပစ္စည်း အမျိုးမျိုး)", 
"လူသုံးကုန်", 
"အဝတ်အထည်", 
"အလှကုန်", 
"လောင်စာဆီ", 
"ပို့ဆောင်ရေး", 
"ဆက်သွယ်ရေး", 
"ဆေးရုံဆေးခန်း", 
"စားသောက်ဆိုင်", 
"ဖုန်းဆိုင်", 
"ဥပဒေ အကြံပေး", 
"မီးသတ်ပစ္စည်းဆိုင်", 
"အိမ်ဆောက်ပစ္စည်းဆိုင်", 
"အလှပြင်ဆိုင်၊ ဆံပင်ညှပ်ဆိုင်", 
"ပန်း ၊ ပန်းအလှဆင်", 
"နာရေးပစ္စည်းဆိုင်", 
"Animal Service", 
"ဖက်ရှင်ဆိုင်", 
"နိဗ္ဗန်ကုန်", 
"အကျိုးဆောင်", 
"ပွဲရုံလုပ်ငန်း", 
"ခရီးသွားလုပ်ငန်း", 
"ပရိဘောဂလုပ်ငန်း", 
"မိတ္တူ လုပ်ငန်း"
),
)
st.write("ရွေးချယ်ထားသည့် လုပ်ငန်းအမျိုးအစား - ", business)
city= st.selectbox(
    "မြို့ရွေးချယ်ပါ",
    ("ကျိုက်ထို", 
"ပေါက်တော", 
"ကော့မှူး", 
"ရေဦး", 
"မင်းကင်း", 
"လေးမျက်နှာ", 
"လားရှိုး", 
"ခေါင်လန်ဖူး", 
"သရက်", 
"ဆော့လော်", 
"ရမည်းသင်း", 
"စစ်တွေ", 
"မာန်အောင်", 
"လင်းခေး", 
"ကော့သောင်း", 
"ကွမ်းလုံ", 
"သာယာဝတီ", 
"သထုံ", 
"လမ်းမတော်", 
"စမ်းချောင်း", 
"မိုင်းတုံ", 
"အုတ်ဖို", 
"လောက်ကိုင်", 
"ပန်းဘဲတန်း", 
"စဉ့်ကူး", 
"ညောင်တုန်း", 
"သန်လျင်", 
"မိုင်းဖြတ်", 
"မြို့သစ်", 
"တောင်ငူ", 
"သုံးခွ", 
"ဝါးခယ်မ", 
"မြစ်ကြီးနား", 
"ပေါက်ခေါင်း", 
"ဆီဆိုင်", 
"ကျွန်းစု", 
"ပလက်ဝ", 
"ဖာပွန်", 
"မိုးညို", 
"ထန်းတပင်", 
"မအူပင်", 
"တနိုင်း", 
"မင်းတုန်း", 
"နားဖန်း", 
"တောင်ကုတ်", 
"သာပေါင်း", 
"မိုင်းရယ်", 
"ကျောက်ပန်းတောင်း", 
"ဟားခါး", 
"ဖားကန့်", 
"တောင်သာ", 
"ဆိပ်ဖြူ", 
"မယ်စဲ", 
"ပွင့်ဖြူ", 
"ခရမ်း", 
"မိုးကောင်း", 
"မန်တုံ", 
"မြောင်", 
"တာချီလိတ်", 
"ကျိုက်လတ်", 
"မှော်ဘီ", 
"ပန်းတောင်း", 
"ဆားလင်းကြီး", 
"ဘုတ်ပြင်း", 
"လဟယ်", 
"မော်လမြိုင်", 
"အမရပူရ", 
"မိုးမိတ်", 
"မြေပုံ", 
"ကျောက်ကြီး", 
"ပင်းတယ", 
"ချင်းရွှေဟော်", 
"ဝန်းသို", 
"နောင်မွန်း", 
"မိုးနဲ", 
"မြောက်ဥက္ကလာပ", 
"မက်မန်း", 
"ချောင်းဆုံ", 
"ဓနုဖြူ", 
"ဖားဆောင်း", 
"မော်လမြိုင်ကျွန်း", 
"ရွာငံ", 
"လှိုင်းဘွဲ့", 
"တောင်ကြီး", 
"မုဒုံ", 
"ရွှေကျင်", 
"မိုင်းလား", 
"မံစီ", 
"ခင်ဦး", 
"အင်းတော်", 
"ယောင်လင်း", 
"ကျောက်မဲ", 
"မင်္ဂလာဒုံ", 
"ပုဗ္ဗသီရိ", 
"ကန်ကြီးထောင့်", 
"မိုင်းယန်း", 
"မိုင်းကိုင်", 
"ဇီးကုန်း", 
"နမ့်ဆန်", 
"စစ်ကိုင်း", 
"ကောလင်း", 
"နွားထိုးကြီး", 
"လပွတ္တာ", 
"တန့်ယန်း", 
"တိုက်ကြီး", 
"ပေါက်", 
"ကမာရွတ်", 
"ထန်းတပင်", 
"ဟိုတောင်း", 
"ကြည့်မြင်တိုင်", 
"ထီးချိုင့်", 
"ဒီးမော့ဆို", 
"လုံထန်", 
"ထားဝယ်", 
"သာကေတ", 
"ဘီးလင်း", 
"ရွှေကူ", 
"တာမွေ", 
"ပန်းတနော်", 
"မတ္တရာ", 
"ဝမ်းတွင်း", 
"မောင်တော", 
"ပျဉ်းမနား", 
"ဗန်းမော်", 
"ပန်ယန်း", 
"အရာတော်", 
"စဉ့်ကိုင်", 
"ဘူးသီးတောင်", 
"သံတောင်ကြီး", 
"အိုက်ချန်", 
"အုတ်တွင်း", 
"ကလေးဝ", 
"မန်တွန်း", 
"တောင်ဥက္ကလာပ", 
"ဆွမ်ပရာဘွမ်", 
"ဆောင်ဖ", 
"သံတွဲ", 
"ကျောက်တံတား", 
"သာစည်", 
"ကံမ", 
"မိတ္ထီလာ", 
"ခန္တီး", 
"သိန္နီ", 
"ပန်ဆန်း (ပန်ခမ်း)", 
"မိုးညှင်း", 
"ဒဂုံ", 
"ဗန်းမောက်", 
"ဒဂုံမြို့သစ်", 
"ပင်လောင်း", 
"မြဝတီ", 
"ရေစကြို", 
"အမ်း", 
"လသာ", 
"လှိုင်သာယာ", 
"ဒလ", 
"စလင်း", 
"ကလေး", 
"လှိုင်", 
"နန်းယွန်း", 
"ကန့်ဘလူ", 
"နတ်မောက်", 
"မင်းလှ", 
"ပျော်ဘွယ်", 
"အင်းစိန်", 
"ရေတာရှည်", 
"ကွန်ဟိန်း", 
"လက်ပံတန်း", 
"မလှိုင်", 
"ပခုက္ကူ", 
"ရသေ့တောင်", 
"မိုင်းပေါက်", 
"ရွှေတောင်", 
"ဘောလခဲ", 
"မိုင်းခတ်", 
"ကျေးသီး", 
"ဒဂုံမြို့သစ်", 
"သနပ်ပင်", 
"ကုန်းကြမ်း", 
"လဲချား", 
"ကိုကိုးကျွန်း", 
"ညောင်ဦး", 
"မြိုင်", 
"ကောင်မင်ဆန်း", 
"မြန်အောင်", 
"ဒေးဒရဲ", 
"ကလော", 
"မြင်းခြံ", 
"မိုင်းဆတ်", 
"နားကောင်", 
"အောင်လံ", 
"ရင်ဖန့်", 
"မိုင်းကာ", 
"ဇလွန်", 
"မောက်မယ်", 
"လောက်ကိုင်", 
"နမ်ခမ်းဝူး", 
"ပဲခူး", 
"အိမ်မဲ", 
"မကွေး", 
"ဖလမ်း", 
"တန့်ဆည်", 
"ဗဟန်း", 
"မဘိမ်း", 
"ကျွန်းလှ", 
"မိုင်းပျဉ်း", 
"ရေကြည်", 
"ဖရူဆို", 
"ဇမ္ဗူသီရိ", 
"ကသာ", 
"ခွန်းမား", 
"ကလောင်ဖါ", 
"ဆင်ပေါင်ဝဲ", 
"အလုံ", 
"ထန်တလန်", 
"နာဝီး", 
"ကြံခင်း", 
"နမ့် တစ်", 
"ကျိုက်မရော", 
"ဝက်လက်", 
"မတူပီ", 
"လွိုင်လင်", 
"မိုးကုတ်", 
"ထီးလင်း", 
"ဒေါပုံ", 
"မိုင်းပန်", 
"ကျောင်းကုန်း", 
"ပြည်ကြီးတံခွန်", 
"ကျောက်ဖြူ", 
"နမ္မတူ", 
"ပုလဲ", 
"ပြည်", 
"မူဆယ်", 
"သင်္ဃန်းကျွန်း", 
"မိုင်းမော", 
"ကျောက်တန်း", 
"သံဖြူဇရပ်", 
"ကနီ", 
"ဥတ္တရသီရိ", 
"လှည်းကူး", 
"အင်ဂျန်းယန်", 
"ဘိုကလေး", 
"သဲကုန်း", 
"နတ်တလင်း", 
"နမ့်စန်", 
"မန်မန်ဆိုင်", 
"မြစ်သား", 
"ဖျာပုံ", 
"တောင်တွင်းကြီး", 
"ဘားအံ", 
"ဝေါ", 
"ဘုတလင်", 
"ဝိုင်းမော်", 
"ညောင်ရွှေ", 
"မိုးမောက်", 
"မင်းပြား", 
"ဟိုပုံး", 
"ဖောင်းပြင်", 
"ကဝ", 
"လွိုင်ကော်", 
"ပန်ဝိုင်", 
"ဒိုက်ဦး", 
"ပုသိမ်", 
"တပ်ကုန်း", 
"ကြို့ပင်ကောက်", 
"ဂွ", 
"ကွမ်း"
),
)

st.write("ရွေးချယ်ထားသည့်မြို့ - ", city)
# st.write(" - ", d.day)
# st.write(" - ", d.month)
# st.write(" - ", d.year)
mmyear=d.year-638
if d.month <= 4:
       if d.month < 4:
          mmyear=mmyear-1
       else:
            if d.day < 12:
              mmyear=mmyear-1
birth_number=mmyear%7
day_name = d.strftime("%A")

st.write("Day Name:", day_name)
st.write("Birth Number:", birth_number)
st.write("MM year:", mmyear)



# To load the model
import joblib
import numpy as np
import pandas as pd

loaded_model = joblib.load('/Users/heinhtetarkarmg/ai-baydin-name-generator/resources/Astro_random_forest_model.h5')

# Function to take a single input and get predictions based on how many times it appears in the dataset
def test_with_same_input_duplicate_outputs(start_input, end_input):
    # Convert user input to a DataFrame
    input_data = pd.DataFrame({'First Consonant': [start_input], 'Last Consonant': [end_input]})

    # Count how many times this input appears in the original dataset
    duplicate_count = 11

    if duplicate_count == 0:
        return "Input not found in the dataset."


    # Combine numerical 'First Consonant' and encoded Last Consonant'
    input_combined = pd.concat([input_data['First Consonant'].reset_index(drop=True),
                                input_data['Last Consonant'].reset_index(drop=True)], axis=1)


    # Get predicted probabilities for each class
    probabilities = loaded_model.predict_proba(input_combined)

    # Randomly select predictions based on probabilities without duplication
    # First, limit the size to the number of available unique classes to avoid over-selecting
    unique_classes = np.unique(loaded_model.classes_)
    selection_size = min(duplicate_count, len(unique_classes))

    # Choose 'selection_size' number of unique predictions
    top_predictions = np.random.choice(unique_classes, size=selection_size, p=probabilities[0], replace=False)

    return top_predictions

# Example: Test the model with the same input and get outputs based on the number of duplicates
start_input = 2  # Example user input for 'Start'
end_input = 5  # Example user input for 'End'
output_name_list = []

# Call the function to predict the outputs based on the number of duplicates
predicted_labels = test_with_same_input_duplicate_outputs(start_input, end_input)

# Output the predicted labels or error message
if isinstance(predicted_labels, str):
    print(predicted_labels)
else:
    for i, label in enumerate(predicted_labels):
        output_name_list.append(label)
        

output_name = ', '.join(map(str, output_name_list))
st.write("Name : ",output_name)
    
