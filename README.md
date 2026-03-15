# 📐 Handwritten Equation Solver - Streamlit Edition

A modern web application that uses Google's Gemini AI for OCR to recognize handwritten mathematical equations and solve them automatically.

## Features

✨ **Key Features:**
- 📷 **Camera Capture** - Take photos directly from your device
- 📤 **Image Upload** - Upload saved images from your computer  
- 🤖 **AI-Powered OCR** - Uses Google Gemini for accurate equation recognition
- 🧮 **Automatic Solving** - Solves detected equations using SymPy
- 🎨 **Beautiful UI** - Clean, intuitive Streamlit interface
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile

## Prerequisites

Before you start, make sure you have:
- Python 3.8 or higher
- A Google account
- Google Gemini API key (free tier available)
- Internet connection

## Setup Instructions

### Step 1: Get Your Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key" button
4. Copy the generated API key
5. Keep it safe - you'll need it to run the app

### Step 2: Install Required Packages

The packages are already installed from our earlier setup:
```bash
pip install streamlit google-generativeai pillow
```

If needed, you can reinstall them manually:
```bash
pip install streamlit google-generativeai pillow sympy
```

### Step 3: Run the Streamlit App

1. Navigate to your project directory:
```bash
cd c:\Users\SPARKZ EDUCATION\Desktop\capstone_project_eq_solver
```

2. Activate your virtual environment (if using one):
```bash
venv\Scripts\activate
```

3. Launch the Streamlit app:
```bash
streamlit run app.py
```

4. Your browser should automatically open to `http://localhost:8501`

## How to Use the App

### Method 1: Upload an Image
1. Click on the **"📤 Upload Image"** tab
2. Click **"Browse files"** and select a photo of your handwritten equation
3. The app will automatically process it

### Method 2: Capture with Camera
1. Click on the **"📷 Capture from Camera"** tab
2. Click **"Take photo"** to capture an image with your device's camera
3. The app will automatically process it

### After Image Selection:
1. Enter your **Gemini API key** in the sidebar
2. The app will:
   - Display your image
   - Recognize the equation using Gemini AI
   - Clean up the detected text
   - Solve the equation
   - Show the solution

## Tips for Best Results

📝 **Handwriting Tips:**
- Write clearly and legibly
- Use standard mathematical notation
- Avoid touching or overlapping characters
- Use variables like x, y, z
- Make equations left-to-right, top-to-bottom

📸 **Photo Tips:**
- Ensure good lighting
- Avoid shadows and reflections
- Use a plain background (white paper recommended)
- Hold camera straight/perpendicular to the paper
- Include the entire equation in the frame
- Avoid tilting or rotating the image

🎯 **Equation Tips:**
- Use standard notation (e.g., "2x" for "2 times x")
- Include an equals sign (=)
- Use parentheses for grouping: (x + 2)
- Use ^ or ** for exponents: x^2 or x**2
- Supported operators: +, -, *, /, =

## Examples of Supported Equations

✅ **Supported:**
- 7 - 4x = 11
- 2x + 5 = 15
- 3y - 2 = 10
- x^2 + 2x = 8
- 5(x + 2) = 35

## Supported Solutions

The app can solve:
- Linear equations: `ax + b = c`
- Quadratic equations: `ax^2 + bx + c = 0`
- Multi-variable equations: `ax + by = c`
- Systems of equations (if detected separately)

## Troubleshooting

### "API Key not configured"
- Make sure you've entered a valid Gemini API key in the sidebar
- Check that your API key has no extra spaces
- Verify the key is from https://makersuite.google.com/app/apikey

### "Equation not detected"
- Try using a clearer image
- Ensure the equation is well-lit
- Write the equation larger and more clearly
- Avoid messy or overlapping handwriting

### "Error solving equation"
- Verify the detected equation is correct
- Check that the equation uses standard notation
- Use * for multiplication (e.g., 2*x not 2x in the detected text)
- Ensure variables are single letters (x, y, z)

### Streamlit won't start
- Make sure you're in the correct directory
- Check that your virtual environment is activated
- Try: `streamlit run app.py --logger.level=debug`

## File Structure

```
capstone_project_eq_solver/
├── app.py                          # Main Streamlit application
├── solve_equation.py               # Original CNN-based solver (legacy)
├── handwritten-mathematical-equation-solver.ipynb  # Training notebook
├── equation_solver.h5              # Trained model (optional)
└── requirements.txt                # Python dependencies
```

## Keyboard Shortcuts (in Streamlit)

- **C** - Rerun the app
- **R** - Refresh
- **S** - Open settings

## Performance Notes

- ⚡ First run takes ~5-10 seconds (model loading)
- 📊 Subsequent runs are faster (~2-3 seconds)
- 🌐 Requires internet connection for Gemini API
- 🔄 Rate limits: Free tier has some limitations

## API Costs

Google's Gemini API has:
- ✅ **Free tier**: 60 requests per minute
- ✅ **Paid tier**: Pay as you go (very affordable)
- Check pricing at: https://cloud.google.com/generative-ai/pricing

## Common Equations to Test

Try these equations to test the system:

1. Simple: `7 - 4x = 11`
2. Addition: `2x + 5 = 15`
3. Subtraction: `10 - 3y = 4`
4. Multiplication: `5x = 25`
5. Fractions: `x/2 + 3 = 7`
6. Quadratic: `x^2 + 2x + 1 = 0`

## Project Structure

This project consists of three approaches:

1. **CNN-Based (Original)**: `handwritten-mathematical-equation-solver.ipynb`
   - Trains a neural network on dataset
   - Saved model: `equation_solver.h5`
   - Script: `solve_equation.py`

2. **Gemini API (Current - Recommended)**: `app.py`
   - Uses Google's pre-trained Gemini model
   - Much more accurate
   - No training required

## Future Enhancements

🚀 **Possible improvements:**
- Support for LaTeX equations
- Step-by-step solution display
- Multiple equation systems
- Graphing capabilities
- Equation history/saved results
- Dark/Light theme toggle

## License

This project is open source and available for educational purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Verify your Gemini API key is valid
3. Try with a different, clearer image
4. Check internet connection

## Credits

- **Gemini API**: Google AI
- **Frontend**: Streamlit
- **Solver**: SymPy
- **Image Processing**: OpenCV, Pillow

---

**Happy Solving! 📐✨**
