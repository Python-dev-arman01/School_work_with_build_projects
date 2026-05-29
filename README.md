# ---------School_read_with_build_projects-------
# 🕒 Python Live Clock Pro

पाइथॉन में बना एक सरल और शक्तिशाली लाइव डिजिटल क्लॉक प्रोग्राम, जो आपके सिस्टम (मोबाइल/कंप्यूटर) के समय को बिना रुके हर सेकंड लाइव अपडेट करता है।

---

## ✨ मुख्य विशेषताएँ (Features)

- **True Live Update:** बिना पेज रीफ्रेश किए हर सेकंड समय बदलता है।
- **Zero Input Required:** यूजर को बार-बार समय टाइप करने की जरूरत नहीं है, यह सीधे सिस्टम क्लॉक से समय उठाता है।
- **Clean Output:** `\r` (Carriage Return) का उपयोग करके समय एक ही लाइन पर डिजिटल घड़ी की तरह चलता है।
- **Memory Efficient:** इसमें अनावश्यक `if-else` या भारी डेटा स्ट्रक्चर्स हटाकर इसे पूरी तरह से ऑप्टिमाइज किया गया है।

---

## 🛠️ उपयोग किए गए कॉन्सेप्ट्स (Concepts Used)

इस प्रोजेक्ट को बनाने में कोर पाइथॉन के निम्नलिखित महत्वपूर्ण विषयों का अभ्यास किया गया है:
1. **Functions (`def`)** - कोड को व्यवस्थित और दोबारा उपयोग के योग्य बनाने के लिए।
2. **Infinite Loops (`while True`)** - घड़ी को लगातार बिना रुके चालू रखने के लिए।
3. **Data Types & Variables (`int`, `str`)** - समय के मानों को सही फॉर्मेट में स्टोर करने के लिए।
4. **Python Built-in Modules (`time`)** - लाइव सिस्टम टाइम और डिले (`time.sleep`) को मैनेज करने के लिए।
5. **String Formatting (`f-string`)** - सिंगल डिजिट समय को `04:05` जैसे प्रोफेशनल फॉर्मेट में दिखाने के लिए।

---

## 🚀 कैसे चलाएं (How to Run)

### मोबाइल पर (Termux / Pydroid 3):
1. अपने पाइथॉन ऐप में एक नई फाइल बनाएं (जैसे: `clock.py`)।
2. इस कोड को पेस्ट करें और **Run** बटन दबाएं।

### कंप्यूटर पर (VS Code / Terminal):
```bash
python clock.py
```

---

## 💻 कोड की झलक (Code Snippet)

```python
import time

def show_time():
    title: str = "[ TRUE LIVE CLOCK ]"
    print(title)
    
    while True:
        hr: int = time.localtime().tm_hour
        mn: int = time.localtime().tm_min
        
        print(f"Current Time is -> {hr:02d}:{mn:02d}", end="\r")
        time.sleep(1)

show_time()
```

---

## 📝 लाइसेंस (License)
यह प्रोजेक्ट ओपन-सोर्स है और सीखने के उद्देश्य से बनाया गया है।
