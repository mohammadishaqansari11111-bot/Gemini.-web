html>
<body>
<script>
import google.generativeai as genai
from google.colab import userdata
genai.configure(api_key=userdata.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')
def summarize(text):
return model.generate_content(f"Aap research analyst ho. Ise 3 parts me summarize karo:\n\n{text}").text
</script>
</body>
</html>
