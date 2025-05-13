🏙️ Avenue Segment Assessments on Roads
This project analyzes road lane segments using computer vision techniques to detect lane lines, measure road conditions, and assess segment quality. 🚀

🚀 Key Features:
✅ Lane Detection using Canny Edge Detection & Hough Transform

✅ Road Condition Analysis with Region of Interest Masking

✅ Frame-by-Frame Video Processing using OpenCV

✅ Customizable Parameters for better accuracy

📂 Project Structure
plaintext
Copy
Edit
📁 Avenue-Segment-Project
├── 📜 app.py              # Python script for road lane detection
├── 📜 Video_1             # Sample video 1
├── 📜 Video_2             # Sample video 2
├── 📜 Video_3             # Sample video 3
├── 📜 README.md           # Project documentation
└── 📜 requirements.txt    # List of dependencies
⚙️ Technologies Used
🐍 Python

🎥 OpenCV (Computer Vision)

🔢 NumPy (Numerical Computations)

🌐 Streamlit (for Web App Interface)

🚀 How to Run
1️⃣ Clone the repository:

bash
Copy
Edit
git clone https://github.com/rohithdannana156/Avenue-Segment-Assessments-on-Roads.git
2️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Once the app is running, you can upload a video to the web interface, and lane detection will be performed on the video.

🛠️ How It Works
1️⃣ The app reads video footage from the uploaded file.
2️⃣ It applies Canny Edge Detection to identify lane edges.
3️⃣ Region of Interest Masking is used to focus on road lanes.
4️⃣ Hough Line Transformation detects lanes.
5️⃣ The detected lane lines are overlaid on the video for visualization.

🏗️ Future Enhancements
🔹 Support for real-time video analysis

🔹 Improved lane detection algorithms using Deep Learning

🔹 Integration with GPS data for road segment mapping

📜 License
This project is open-source and available for educational and research purposes.

🎉 Feel free to contribute, improve, or fork this project! 🚀