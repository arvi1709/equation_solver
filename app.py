import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import re
from sympy import sympify, solve, symbols, latex
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Handwritten Equation Solver",
    page_icon="📐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .header {
            text-align: center;
            color: #1f77b4;
        }
        .success-box {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724;
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }
        .error-box {
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            color: #721c24;
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='header'>📐 Handwritten Equation Solver</h1>", unsafe_allow_html=True)
st.markdown("Convert handwritten equations to text and solve them automatically!")

# Sidebar for API key configuration
st.sidebar.header("⚙️ Configuration")

# Try to load API key from .env file first
env_api_key = os.getenv("GEMINI_API_KEY")

# Check if .env file exists and has the default value
if env_api_key and env_api_key == "your_api_key_here":
    st.sidebar.warning("⚠️ Please set your Gemini API key in the .env file")
    api_key = st.sidebar.text_input(
        "Or enter your Google Gemini API Key here",
        type="password",
        help="Get your API key from https://makersuite.google.com/app/apikey"
    )
elif env_api_key:
    st.sidebar.success(f"✓ API Key loaded from .env file")
    api_key = env_api_key
    # Optional: Allow user to override
    if st.sidebar.checkbox("Use different API key?"):
        api_key = st.sidebar.text_input(
            "Enter your Google Gemini API Key",
            type="password",
            help="Get your API key from https://makersuite.google.com/app/apikey"
        )
else:
    st.sidebar.info("ℹ️ No API key found in .env file")
    api_key = st.sidebar.text_input(
        "Enter your Google Gemini API Key",
        type="password",
        help="Get your API key from https://makersuite.google.com/app/apikey"
    )

if api_key:
    genai.configure(api_key=api_key)
    if not env_api_key or env_api_key != api_key:
        st.sidebar.success("✓ API Key configured")
else:
    st.sidebar.error("❌ No API key available")

# Main app content
st.markdown("### 📸 Upload or Capture Your Equation")

# Create tabs for upload and camera
tab1, tab2 = st.tabs(["📤 Upload Image", "📷 Capture from Camera"])

uploaded_image = None
image_source = None

with tab1:
    uploaded_file = st.file_uploader(
        "Choose an image of a handwritten equation",
        type=["jpg", "jpeg", "png", "bmp", "gif"]
    )
    if uploaded_file is not None:
        uploaded_image = Image.open(uploaded_file)
        image_source = "upload"

with tab2:
    captured_image = st.camera_input("Take a photo of your equation")
    if captured_image is not None:
        uploaded_image = Image.open(captured_image)
        image_source = "camera"

# Process the image
if uploaded_image is not None and api_key:
    st.markdown("### 📝 Processing Image...")
    
    # Display the uploaded/captured image
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(uploaded_image, caption="Your Image", use_column_width=True)
    
    with col2:
        st.info("Analyzing the equation...", icon="🔍")
    
    try:
        # Convert image to bytes for Gemini API
        img_byte_arr = io.BytesIO()
        uploaded_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        # Use Gemini to recognize the equation
        model = genai.GenerativeModel('gemini-3-flash-preview')
        
        # Prompt to extract the mathematical equation
        prompt = """Please analyze this image and extract the mathematical equation written in it.
        Return ONLY the equation in a format that can be solved, using standard mathematical notation:
        - Use * for multiplication (e.g., 2*x instead of 2x)
        - Use / for division
        - Use ** for exponents
        - Use = for equals
        - Use standard variable names like x, y, z
        
        Example outputs:
        - 2*x + 5 = 15
        - 3*y - 2 = 10
        - x**2 + 2*x = 8
        
        Return ONLY the equation, nothing else."""
        
        # Send image to Gemini (processing happens silently)
        response = model.generate_content([prompt, uploaded_image])
        detected_equation = response.text.strip()
        
        # Clean up the equation
        # Add * between digit and variable if not already present
        cleaned_equation = re.sub(r'(\d)([xy])', r'\1*\2', detected_equation)
        cleaned_equation = cleaned_equation.replace('−', '-')  # Replace minus sign variants
        
        # Solve the equation
        st.markdown("### 🎯 Solution")
        
        try:
            if '=' in cleaned_equation:
                # Split into left and right sides
                parts = cleaned_equation.split('=')
                if len(parts) == 2:
                    lhs_str, rhs_str = parts
                    
                    # Extract variables
                    var_pattern = r'[a-zA-Z]'
                    vars_in_eq = set(re.findall(var_pattern, cleaned_equation))
                    
                    if vars_in_eq:
                        vars_in_eq = sorted(list(vars_in_eq))
                        vars_symbols = symbols(' '.join(vars_in_eq))
                        
                        # Handle single variable case
                        if len(vars_in_eq) == 1:
                            var = vars_symbols
                        else:
                            var = vars_symbols
                        
                        # Parse expressions
                        lhs = sympify(lhs_str)
                        rhs = sympify(rhs_str)
                        
                        # Solve the equation
                        solution = solve(lhs - rhs, var)
                        
                        # Display solution
                        if solution:
                            st.markdown("### 🎯 Equation Solution")
                            if isinstance(solution, dict):
                                for var_name, value in solution.items():
                                    st.write(f"**{var_name} = {value}**")
                            elif isinstance(solution, list):
                                for i, sol in enumerate(solution, 1):
                                    if len(vars_in_eq) == 1:
                                        st.write(f"**{vars_in_eq[0]} = {sol}**")
                                    else:
                                        st.write(f"Solution {i}: {sol}")
                            else:
                                st.write(f"**Solution: {solution}**")
                            
                            # Display LaTeX form of the equation
                            st.markdown("### 📐 LaTeX Form")
                            try:
                                lhs_latex = latex(lhs)
                                rhs_latex = latex(rhs)
                                full_latex = f"{lhs_latex} = {rhs_latex}"
                                st.latex(full_latex)
                                st.code(full_latex, language="latex")
                            except:
                                st.info("LaTeX form not available for this equation.")
                            
                            st.markdown("""
                            <div class='success-box'>
                            ✓ Equation solved successfully!
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.warning("No solution found for this equation.")
                    else:
                        st.error("No variables found in the equation.")
                else:
                    st.error("Equation must contain exactly one '=' sign.")
            else:
                st.error("Please ensure the equation contains an '=' sign.")
                
        except Exception as e:
            st.markdown("""
            <div class='error-box'>
            ⚠️ Error solving equation
            </div>
            """, unsafe_allow_html=True)
            st.error(f"**Error:** {str(e)}")
            st.info("Please make sure the detected equation is valid and follows standard mathematical notation.")
    
    except Exception as e:
        st.markdown("""
        <div class='error-box'>
        ⚠️ Error processing image
        </div>
        """, unsafe_allow_html=True)
        st.error(f"**Error:** {str(e)}")
        st.info("Please try uploading a clearer image of the equation.")

elif uploaded_image is not None and not api_key:
    st.error("Please enter your Gemini API key in the sidebar to continue.")

# Footer
st.markdown("---")
st.markdown("""
### 📖 How to Use:
1. Enter your Google Gemini API key in the sidebar
2. Upload an image or capture a photo of your handwritten equation
3. The system will recognize the equation using AI
4. The equation will be solved automatically

### 💡 Tips:
- Use clear, legible handwriting
- Ensure the equation is well-lit in the photo
- Try to avoid shadows or reflections
- Use standard mathematical notation (x, y for variables)
""")

st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8rem; margin-top: 2rem;'>
Made with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
