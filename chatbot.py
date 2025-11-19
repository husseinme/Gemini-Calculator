from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

class AICalculator:

  def __init__(self, api_key=os.getenv("GEMINI_API_KEY"), model="gemini-2.5-flash"):
    self.api_key = api_key
    self.model = model
    self.client = genai.Client(api_key=self.api_key)
  
  def calculate(self, num1:int, num2:int):
    question_content = f"Calculate the result of {num1} x {num2}. Output ONLY the equation anf the final numerical answer, using no words, no explanations."

    response = self.client.models.generate_content(
        model=self.model, contents=question_content
      )
    return response.text
  

if __name__ == "__main__":
  calculator = AICalculator()

  num1 = 3
  num2 = 4

  result = calculator.calculate(num1, num2)

  print(f"Calculation Result: {result}")